from __future__ import annotations

import datetime
import typing
from typing import List, Optional

from Cryptodome.PublicKey import RSA

from bunq.sdk.context.api_environment_type import ApiEnvironmentType
from bunq.sdk.context.installation_context import InstallationContext
from bunq.sdk.context.session_context import SessionContext
from bunq.sdk.exception.bunq_exception import BunqException
from bunq.sdk.json import converter
from bunq.sdk.model.core.payment_service_provider_credential_internal import PaymentServiceProviderCredentialInternal
from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated.endpoint import UserCredentialPasswordIp, UserPaymentServiceProvider
from bunq.sdk.security import security

if typing.TYPE_CHECKING:
    from bunq.sdk.model.core.session_server import SessionServer


class ApiContext:
    """
    :type _environment_type: ApiEnvironmentType
    :type _api_key: str|None
    :type _session_context: SessionContext|None
    :type _installation_context: InstallationContext|None
    :type _proxy_url: str|None
    """

    # File mode for saving and restoring the context
    _FILE_MODE_WRITE = 'w'
    _FILE_MODE_READ = 'r'

    # Minimum time to session expiry not requiring session reset
    _TIME_TO_SESSION_EXPIRY_MINIMUM_SECONDS = 30

    # Dummy ID to pass to Session endpoint
    _SESSION_ID_DUMMY = 0

    # Default path to the file storing serialized API context
    _PATH_API_CONTEXT_DEFAULT = 'bunq.conf'

    def __init__(self,
                 environment_type: ApiEnvironmentType,
                 proxy_url: List[str] = None) -> None:
        self._environment_type = environment_type
        self._proxy_url = proxy_url
        self._api_key = None
        self._installation_context = None
        self._session_context = None

    @classmethod
    def create(cls,
               environment_type: ApiEnvironmentType,
               api_key: str,
               description: str,
               all_permitted_ip: List[str] = None,
               proxy_url: List[str] = None) -> ApiContext:
        api_context = cls(environment_type, proxy_url)

        api_context._api_key = api_key

        api_context.__initialize_installation()
        api_context.__register_device(description, all_permitted_ip)
        api_context.__initialize_session()

        return api_context

    @classmethod
    def create_for_psd2(cls,
                        environment_type: ApiEnvironmentType,
                        certificate: str,
                        private_key: str,
                        all_chain_certificate: List[str],
                        description: str,
                        all_permitted_ip: List[str] = None,
                        proxy_url: List[str] = None) -> ApiContext:
        api_context = cls(environment_type, proxy_url)

        api_context.__initialize_installation()

        service_provider_credential = api_context.__initialize_psd2_credential(
            certificate,
            private_key,
            all_chain_certificate
        )

        api_context._api_key = service_provider_credential.token_value

        api_context.__register_device(description, all_permitted_ip)
        api_context.__initialize_session_for_psd2(service_provider_credential)

        return api_context

    def __initialize_installation(self) -> None:
        from bunq.sdk.model.core.installation import Installation

        private_key_client = security.generate_rsa_private_key()

        installation = Installation.create(
            self,
            security.public_key_to_string(private_key_client.publickey())
        ).value
        token = installation.token.token
        public_key_server_string = \
            installation.server_public_key.server_public_key
        public_key_server = RSA.import_key(public_key_server_string)

        self._installation_context = InstallationContext(
            token,
            private_key_client,
            public_key_server
        )

    def __initialize_psd2_credential(self,
                                     certificate: str,
                                     private_key: str,
                                     all_chain_certificate: List[str], ) -> UserCredentialPasswordIp:
        session_token = self.installation_context.token
        client_key_pair = self.installation_context.private_key_client

        string_to_sign = security.public_key_to_string(client_key_pair.publickey()) + "\n" + session_token
        encoded_signature = security.generate_signature(string_to_sign, security.rsa_key_from_string(private_key))

        payment_response_provider = PaymentServiceProviderCredentialInternal.create_with_api_context(
            certificate,
            security.get_certificate_chain_string(all_chain_certificate),
            encoded_signature,
            self
        )

        return payment_response_provider

    def __register_device(self,
                          device_description: str,
                          permitted_ips: List[str]) -> None:
        from bunq.sdk.model.core.device_server_internal import DeviceServerInternal

        DeviceServerInternal.create(
            device_description,
            self.api_key,
            permitted_ips,
            api_context=self
        )

    def __initialize_session(self) -> None:
        from bunq.sdk.model.core.session_server import SessionServer

        session_server = SessionServer.create(self).value
        token = session_server.token.token
        expiry_time = self._get_expiry_timestamp(session_server)
        user_id = session_server.get_referenced_user().id_

        self._session_context = SessionContext(token, expiry_time, user_id)

    def __initialize_session_for_psd2(self, user_payment_service_provider: UserPaymentServiceProvider) -> None:
        from bunq.sdk.model.core.session_server import SessionServer

        session_server = SessionServer.create(self).value

        token = session_server.token.token
        expiry_time = self._get_expiry_timestamp(session_server)
        user_id = session_server.get_referenced_user().id_

        self._session_context = SessionContext(token, expiry_time, user_id)

    @classmethod
    def _get_expiry_timestamp(cls, session_server: SessionServer) -> datetime.datetime:
        timeout_seconds = cls._get_session_timeout_seconds(session_server)
        time_now = datetime.datetime.now()

        return time_now + datetime.timedelta(seconds=timeout_seconds)

    @classmethod
    def _get_session_timeout_seconds(cls, session_server: SessionServer) -> int:
        if session_server.user_company is not None:
            return session_server.user_company.session_timeout
        elif session_server.user_person is not None:
            return session_server.user_person.session_timeout
        elif session_server.user_payment_service_provider is not None:
            return session_server.user_payment_service_provider.session_timeout
        elif session_server.user_api_key is not None:
            return session_server \
                .user_api_key \
                .requested_by_user \
                .get_referenced_object() \
                .session_timeout
        else:
            raise BunqException()

    def ensure_session_active(self) -> bool:
        """
        Resets the session if it has expired.

        """

        if not self.is_session_active():
            self.reset_session()

            return True

        return False

    def is_session_active(self) -> bool:
        if self.session_context is None:
            return False

        time_now = datetime.datetime.now()
        time_to_expiry = self.session_context.expiry_time - time_now
        time_to_expiry_minimum = datetime.timedelta(
            seconds=self._TIME_TO_SESSION_EXPIRY_MINIMUM_SECONDS
        )

        return time_to_expiry > time_to_expiry_minimum

    def reset_session(self) -> None:
        """
        Closes the current session and opens a new one.

        """

        self._drop_session_context()
        self.__initialize_session()

    def _drop_session_context(self) -> None:
        self._session_context = None

    def close_session(self) -> None:
        """
        Closes the current session.

        """

        self._delete_session()
        self._drop_session_context()

    def _delete_session(self) -> None:
        endpoint.Session.delete(self._SESSION_ID_DUMMY)

    @property
    def environment_type(self) -> ApiEnvironmentType:
        return self._environment_type

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def token(self) -> Optional[str]:
        if self._session_context is not None:
            return self.session_context.token
        elif self._installation_context is not None:
            return self.installation_context.token
        else:
            return None

    @property
    def installation_context(self) -> InstallationContext:
        return self._installation_context

    @property
    def session_context(self) -> SessionContext:
        return self._session_context

    @property
    def proxy_url(self) -> str:
        return self._proxy_url

    def save(self, path: str = None) -> None:
        if path is None:
            path = self._PATH_API_CONTEXT_DEFAULT

        with open(path, self._FILE_MODE_WRITE) as file_:
            file_.write(self.to_json())

    def to_json(self) -> str:
        """
        Serializes an ApiContext to JSON string.

        """

        return converter.class_to_json(self)

    @classmethod
    def restore(cls, path: str = None) -> ApiContext:
        if path is None:
            path = cls._PATH_API_CONTEXT_DEFAULT

        with open(path, cls._FILE_MODE_READ) as file_:
            return cls.from_json(file_.read())

    @classmethod
    def from_json(cls, json_str: str) -> ApiContext:
        """
        Creates an ApiContext instance from JSON string.

        """

        return converter.json_to_class(ApiContext, json_str)

    def __eq__(self, other: ApiContext) -> bool:
        return (self.token == other.token and
                self.api_key == other.api_key and
                self.environment_type == other.environment_type)

import datetime

import aenum
from Cryptodome.PublicKey import RSA

from bunq.sdk import security
from bunq.sdk.exception import BunqException
from bunq.sdk.json import converter
from bunq.sdk.model import core
from bunq.sdk.model.generated import endpoint


class ApiEnvironmentType(aenum.AutoNumberEnum):
    """
    :type PRODUCTION: ApiEnvironmentType
    :type SANDBOX: ApiEnvironmentType
    :type uri_base: str
    """

    PRODUCTION = 'https://api.bunq.com/v1/'
    SANDBOX = 'https://public-api.sandbox.bunq.com/v1/'

    def __init__(self, uri_base):
        """
        :type uri_base: str
        """

        self._uri_base = uri_base

    @property
    def uri_base(self):
        """
        :rtype: str
        """

        return self._uri_base


class ApiContext(object):
    """
    :type _environment_type: ApiEnvironmentType
    :type _api_key: str
    :type _session_context: SessionContext
    :type _installation_context: InstallationContext
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

    def __init__(self, environment_type, api_key, device_description,
                 permitted_ips=None, proxy_url=None):
        """
        :type environment_type: ApiEnvironmentType
        :type api_key: str
        :type device_description: str
        :type permitted_ips: list[str]|None
        :type proxy_url: str|None
        """

        if permitted_ips is None:
            permitted_ips = []

        self._environment_type = environment_type
        self._api_key = api_key
        self._installation_context = None
        self._session_context = None
        self._proxy_url = proxy_url
        self._initialize(device_description, permitted_ips)

    def _initialize(self, device_description, permitted_ips):
        """
        :type device_description: str
        :type permitted_ips: list[str]

        :rtype: None
        """

        self._initialize_installation()
        self._register_device(device_description, permitted_ips)
        self._initialize_session()

    def _initialize_installation(self):
        """
        :rtype: None
        """

        private_key_client = security.generate_rsa_private_key()
        installation = core.Installation.create(
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

    def _register_device(self, device_description,
                         permitted_ips):
        """
        :type device_description: str
        :type permitted_ips: list[]

        :rtype: None
        """

        from bunq.sdk.model.device_server_internal import DeviceServerInternal

        DeviceServerInternal.create(
            device_description,
            self.api_key,
            permitted_ips,
            api_context=self
        )

    def _initialize_session(self):
        """
        :rtype: None
        """

        session_server = core.SessionServer.create(self).value
        token = session_server.token.token
        expiry_time = self._get_expiry_timestamp(session_server)
        user_id = session_server.get_referenced_user().id_

        self._session_context = SessionContext(token, expiry_time, user_id)

    @classmethod
    def _get_expiry_timestamp(cls, session_server):
        """
        :type session_server: core.SessionServer

        :rtype: datetime.datetime
        """

        timeout_seconds = cls._get_session_timeout_seconds(session_server)
        time_now = datetime.datetime.now()

        return time_now + datetime.timedelta(seconds=timeout_seconds)

    @classmethod
    def _get_session_timeout_seconds(cls, session_server):
        """
        :type session_server: core.SessionServer

        :rtype: int
        """

        if session_server.user_company is not None:
            return session_server.user_company.session_timeout
        elif session_server.user_person is not None:
            return session_server.user_person.session_timeout
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

        :rtype: bool
        """

        if not self.is_session_active():
            self.reset_session()

            return True

        return False

    def is_session_active(self):
        """
        :rtype: bool
        """

        if self.session_context is None:
            return False

        time_now = datetime.datetime.now()
        time_to_expiry = self.session_context.expiry_time - time_now
        time_to_expiry_minimum = datetime.timedelta(
            seconds=self._TIME_TO_SESSION_EXPIRY_MINIMUM_SECONDS
        )

        return time_to_expiry > time_to_expiry_minimum

    def reset_session(self):
        """
        Closes the current session and opens a new one.

        :rtype: None
        """

        self._drop_session_context()
        self._initialize_session()

    def _drop_session_context(self):
        """
        :rtype: None
        """

        self._session_context = None

    def close_session(self):
        """
        Closes the current session.

        :rtype: None
        """

        self._delete_session()
        self._drop_session_context()

    def _delete_session(self):
        """
        :rtype: None
        """

        endpoint.Session.delete(self._SESSION_ID_DUMMY)

    @property
    def environment_type(self):
        """
        :rtype: ApiEnvironmentType
        """

        return self._environment_type

    @property
    def api_key(self):
        """
        :rtype: str
        """

        return self._api_key

    @property
    def token(self):
        """
        :rtype: str
        """

        if self._session_context is not None:
            return self.session_context.token
        elif self._installation_context is not None:
            return self.installation_context.token
        else:
            return None

    @property
    def installation_context(self):
        """
        :rtype: InstallationContext
        """

        return self._installation_context

    @property
    def session_context(self):
        """
        :rtype: SessionContext
        """

        return self._session_context

    @property
    def proxy_url(self):
        """
        :rtype: str
        """

        return self._proxy_url

    def save(self, path=None):
        """
        :type path: str

        :rtype: None
        """

        if path is None:
            path = self._PATH_API_CONTEXT_DEFAULT

        with open(path, self._FILE_MODE_WRITE) as file_:
            file_.write(self.to_json())

    def to_json(self):
        """
        Serializes an ApiContext to JSON string.

        :rtype: str
        """

        return converter.class_to_json(self)

    @classmethod
    def restore(cls, path=None):
        """
        :type path: str

        :rtype: ApiContext
        """

        if path is None:
            path = cls._PATH_API_CONTEXT_DEFAULT

        with open(path, cls._FILE_MODE_READ) as file_:
            return cls.from_json(file_.read())

    @classmethod
    def from_json(cls, json_str):
        """
        Creates an ApiContext instance from JSON string.

        :type json_str: str

        :rtype: ApiContext
        """

        return converter.json_to_class(ApiContext, json_str)

    def __eq__(self, other):
        return (self.token == other.token and
                self.api_key == other.api_key and
                self.environment_type == other.environment_type)


class InstallationContext(object):
    """
    :type _token: str
    :type _private_key_client: RSA.RsaKey
    :type _public_key_server: RSA.RsaKey
    """

    def __init__(self, token, private_key_client, public_key_server):
        """
        :type token: str
        :type private_key_client: RSA.RsaKey
        :type public_key_server: RSA.RsaKey
        """

        self._token = token
        self._private_key_client = private_key_client
        self._public_key_server = public_key_server

    @property
    def token(self):
        """
        :rtype: str
        """

        return self._token

    @property
    def private_key_client(self):
        """
        :rtype: RSA.RsaKey
        """

        return self._private_key_client

    @property
    def public_key_server(self):
        """
        :rtype: RSA.RsaKey
        """

        return self._public_key_server


class SessionContext(object):
    """
    :type _token: str
    :type _expiry_time: datetime.datetime
    :type _user_id: int
    """

    def __init__(self, token, expiry_time, user_id):
        """
        :type token: str
        :type expiry_time: datetime.datetime
        """

        self._token = token
        self._expiry_time = expiry_time
        self._user_id = user_id

    @property
    def token(self):
        """
        :rtype: str
        """

        return self._token

    @property
    def expiry_time(self):
        """
        :rtype: datetime.datetime
        """

        return self._expiry_time

    @property
    def user_id(self):
        return self._user_id


class UserContext(object):
    _ERROR_UNEXPECTED_USER_INSTANCE = '"{}" is unexpected user instance.'
    _ERROR_NO_ACTIVE_MONETARY_ACCOUNT_FOUND = \
        'No active monetary account found.'
    _STATUS_ACTIVE = 'ACTIVE'

    def __init__(self, user_id):
        """
        :type user_id: int
        """

        self._user_id = user_id
        self._user_person = None
        self._user_company = None
        self._user_api_key = None
        self._primary_monetary_account = None

        self._set_user(self.__get_user_object())

    @staticmethod
    def __get_user_object():
        """
        :rtype: core.BunqModel
        """

        return endpoint.User.list().value[0].get_referenced_object()

    def _set_user(self, user):
        if isinstance(user, endpoint.UserPerson):
            self._user_person = user

        elif isinstance(user, endpoint.UserCompany):
            self._user_company = user

        elif isinstance(user, endpoint.UserApiKey):
            self._user_api_key = user

        else:
            raise BunqException(
                self._ERROR_UNEXPECTED_USER_INSTANCE.format(user.__class__))

    def init_main_monetary_account(self):
        all_monetary_account = endpoint.MonetaryAccountBank.list().value

        for account in all_monetary_account:
            if account.status == self._STATUS_ACTIVE:
                self._primary_monetary_account = account

                return

        raise BunqException(self._ERROR_NO_ACTIVE_MONETARY_ACCOUNT_FOUND)

    @property
    def user_id(self):
        return self._user_id

    def is_only_user_person_set(self):
        """
        :rtype: bool
        """

        return self._user_person is not None \
            and self._user_company is None \
            and self._user_api_key is None

    def is_only_user_company_set(self):
        """
        :rtype: bool
        """

        return self._user_company is not None \
            and self._user_person is None \
            and self._user_api_key is None

    def is_only_user_api_key_set(self):
        """
        :rtype: bool
        """

        return self._user_api_key is not None \
            and self._user_company is None \
            and self._user_person is None

    def is_all_user_type_set(self):
        """
        :rtype: bool
        """

        return self._user_company is not None \
            and self._user_person is not None \
            and self._user_api_key is not None

    def refresh_user_context(self):
        """
        """

        self._set_user(self.__get_user_object())
        self.init_main_monetary_account()

    @property
    def user_company(self):
        """
        :rtype: endpoint.UserCompany
        """

        return self._user_company

    @property
    def user_person(self):
        """
        :rtype: endpoint.UserPerson
        """

        return self._user_person

    @property
    def user_api_key(self):
        """
        :rtype: endpoint.UserApiKey
        """

        return self._user_api_key

    @property
    def primary_monetary_account(self):
        """
        :rtype: endpoint.MonetaryAccountBank
        """

        return self._primary_monetary_account


class BunqContext(object):
    _ERROR_CLASS_SHOULD_NOT_BE_INITIALIZED = \
        'This class should not be instantiated'
    _ERROR_API_CONTEXT_HAS_NOT_BEEN_LOADED = \
        'ApiContext has not been loaded. Please load ApiContext in BunqContext'
    _ERROR_USER_CONTEXT_HAS_NOT_BEEN_LOADED = \
        'UserContext has not been loaded, please load this' \
        ' by loading ApiContext.'

    _api_context = None
    _user_context = None

    def __init__(self):
        raise TypeError(self._ERROR_CLASS_SHOULD_NOT_BE_INITIALIZED)

    @classmethod
    def load_api_context(cls, api_context):
        """
        :type api_context: ApiContext
        """

        cls._api_context = api_context
        cls._user_context = UserContext(api_context.session_context.user_id)
        cls._user_context.init_main_monetary_account()

    @classmethod
    def api_context(cls):
        """
        :rtype: ApiContext
        """

        if cls._api_context is not None:
            return cls._api_context

        raise BunqException(cls._ERROR_API_CONTEXT_HAS_NOT_BEEN_LOADED)

    @classmethod
    def user_context(cls):
        """
        :rtype: UserContext
        """

        if cls._user_context is not None:
            return cls._user_context

        raise BunqException(cls._ERROR_USER_CONTEXT_HAS_NOT_BEEN_LOADED)

    @classmethod
    def update_api_context(cls, api_context: ApiContext):
        """
        :type api_context: ApiContext
        """

        cls._api_context = api_context

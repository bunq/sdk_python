from __future__ import annotations

from typing import Optional

from bunq.sdk.context.api_context import ApiContext
from bunq.sdk.exception.bunq_exception import BunqException
from bunq.sdk.http.api_client import ApiClient
from bunq.sdk.http.bunq_response import BunqResponse
from bunq.sdk.json import converter
from bunq.sdk.model.core.bunq_model import BunqModel
from bunq.sdk.model.core.id import Id
from bunq.sdk.model.core.session_token import SessionToken
from bunq.sdk.model.generated.endpoint import UserPerson, UserCompany, UserApiKey, UserPaymentServiceProvider


class SessionServer(BunqModel):
    """
    :type _id_: Id|None
    :type _token: SessionToken|None
    :type _user_person: UserPerson|None
    :type _user_company: UserCompany|None
    :type _user_api_key: UserApiKey|None
    :type _user_payment_service_provider: UserPaymentServiceProvider|None
    """

    # Endpoint name.
    _ENDPOINT_URL_POST = "session-server"

    # Field constants
    FIELD_SECRET = "secret"

    # Error constants
    _ERROR_ALL_FIELD_IS_NULL = 'All fields are null'

    @property
    def id_(self) -> Optional[Id]:
        return self._id_

    @property
    def token(self) -> Optional[SessionToken]:
        return self._token

    @property
    def user_person(self) -> Optional[UserPerson]:
        return self._user_person

    @property
    def user_company(self) -> Optional[UserCompany]:
        return self._user_company

    @property
    def user_api_key(self) -> Optional[UserApiKey]:
        return self._user_api_key

    @property
    def user_payment_service_provider(self) -> Optional[UserPaymentServiceProvider]:
        return self._user_payment_service_provider

    def __init__(self) -> None:
        self._user_person = None
        self._user_company = None
        self._user_api_key = None
        self._user_payment_service_provider = None
        self._token = None
        self._id_ = None

    @classmethod
    def create(cls, api_context: ApiContext) -> BunqResponse[SessionServer]:
        cls.__init__(cls)
        api_client = ApiClient(api_context)
        body_bytes = cls.generate_request_body_bytes(api_context.api_key)
        response_raw = api_client.post(cls._ENDPOINT_URL_POST, body_bytes, {})

        return cls._from_json_array_nested(response_raw)

    @classmethod
    def generate_request_body_bytes(cls, secret: str) -> bytes:
        return converter.class_to_json({cls.FIELD_SECRET: secret}).encode()

    def is_all_field_none(self) -> bool:
        if self.id_ is not None:
            return False
        elif self.token is not None:
            return False
        elif self.user_person is not None:
            return False
        elif self.user_company is not None:
            return False
        elif self.user_api_key is not None:
            return False
        elif self.user_payment_service_provider is not None:
            return False
        else:
            return True

    def get_user_reference(self) -> BunqModel:
        if self.user_person is not None:
            return self.user_person
        elif self.user_company is not None:
            return self.user_company
        elif self.user_api_key is not None:
            return self.user_api_key
        elif self.user_payment_service_provider is not None:
            return self.user_payment_service_provider
        else:
            raise BunqException(self._ERROR_ALL_FIELD_IS_NULL)

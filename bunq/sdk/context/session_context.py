from __future__ import annotations

import datetime
from typing import Optional

from bunq.sdk.exception.bunq_exception import BunqException
from bunq.sdk.model.core.bunq_model import BunqModel
from bunq.sdk.model.core.session_token import SessionToken
from bunq.sdk.model.generated.endpoint import UserPerson, UserCompany, UserApiKey, UserPaymentServiceProvider


class SessionContext:
    """
    :type _token: str
    :type _expiry_time: datetime.datetime
    :type _user_id: int
    :type _user_person: UserPerson|None
    :type _user_company: UserCompany|None
    :type _user_api_key: UserApiKey|None
    :type _user_payment_service_provider: UserPaymentServiceProvider|None
    """

    # Error constants
    _ERROR_ALL_FIELD_IS_NULL = 'All fields are null'
    _ERROR_UNEXPECTED_USER_INSTANCE = '"{}" is unexpected user instance.'

    @property
    def token(self) -> str:
        return self._token

    @property
    def expiry_time(self) -> datetime.datetime:
        return self._expiry_time

    @property
    def user_id(self) -> int:
        return self._user_id

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

    def __init__(self, token: SessionToken, expiry_time: datetime.datetime, user: BunqModel) -> None:
        self._user_person = None
        self._user_company = None
        self._user_api_key = None
        self._user_payment_service_provider = None
        self._token = token.token
        self._expiry_time = expiry_time
        self._user_id = self.__get_user_id(user)
        self.__set_user(user)

    def __get_user_id(self, user: BunqModel) -> int:
        if isinstance(user, UserPerson):
            return user.id_

        if isinstance(user, UserCompany):
            return user.id_

        if isinstance(user, UserApiKey):
            return user.id_

        if isinstance(user, UserPaymentServiceProvider):
            return user.id_

        raise BunqException(self._ERROR_UNEXPECTED_USER_INSTANCE)

    def __set_user(self, user: BunqModel):
        if isinstance(user, UserPerson):
            self._user_person = user
        elif isinstance(user, UserCompany):
            self._user_company = user
        elif isinstance(user, UserApiKey):
            self._user_api_key = user
        elif isinstance(user, UserPaymentServiceProvider):
            self._user_payment_service_provider = user
        else:
            raise BunqException(self._ERROR_UNEXPECTED_USER_INSTANCE)

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

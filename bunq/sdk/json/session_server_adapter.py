from typing import Type, List

from bunq.sdk.exception.bunq_exception import BunqException
from bunq.sdk.json import converter
from bunq.sdk.model.core.id import Id
from bunq.sdk.model.core.session_server import SessionServer
from bunq.sdk.model.core.session_token import SessionToken
from bunq.sdk.model.generated import endpoint


class SessionServerAdapter(converter.JsonAdapter):
    # Error constants.
    _ERROR_COULD_NOT_DETERMINE_USER = 'Could not determine user.'

    # Id constants
    _ATTRIBUTE_ID = '_id_'
    _INDEX_ID = 0
    _FIELD_ID = 'Id'

    # Token constants
    _ATTRIBUTE_TOKEN = '_token'
    _INDEX_TOKEN = 1
    _FIELD_TOKEN = 'Token'

    # User constants
    _INDEX_USER = 2

    # UserCompany constants
    _ATTRIBUTE_USER_COMPANY = '_user_company'
    _FIELD_USER_COMPANY = 'UserCompany'

    # UserPerson constants
    _ATTRIBUTE_USER_PERSON = '_user_person'
    _FIELD_USER_PERSON = 'UserPerson'

    # UserApiKey constants
    _ATTRIBUTE_USER_API_KEY = '_user_api_key'
    _FIELD_USER_API_KEY = 'UserApiKey'

    # UserPaymentServiceProvider constants
    _ATTRIBUTE_USER_PAYMENT_SERVER_PROVIDER = '_user_payment_service_provider'
    _FIELD_USER_PAYMENT_SERVER_PROVIDER = 'UserPaymentServiceProvider'

    @classmethod
    def deserialize(cls,
                    target_class: Type[SessionServer],
                    array: List) -> SessionServer:
        session_server = target_class.__new__(target_class)
        session_server.__dict__ = {
            cls._ATTRIBUTE_ID: converter.deserialize(
                Id,
                array[cls._INDEX_ID][cls._FIELD_ID]
            ),
            cls._ATTRIBUTE_TOKEN: converter.deserialize(
                SessionToken,
                array[cls._INDEX_TOKEN][cls._FIELD_TOKEN]
            ),
            cls._ATTRIBUTE_USER_COMPANY: None,
            cls._ATTRIBUTE_USER_PERSON: None,
            cls._ATTRIBUTE_USER_PAYMENT_SERVER_PROVIDER: None,
        }

        user_dict_wrapped = array[cls._INDEX_USER]

        if cls._FIELD_USER_COMPANY in user_dict_wrapped:
            session_server.__dict__[cls._ATTRIBUTE_USER_COMPANY] = \
                converter.deserialize(
                    endpoint.UserCompany,
                    user_dict_wrapped[cls._FIELD_USER_COMPANY]
                )
        elif cls._FIELD_USER_PERSON in user_dict_wrapped:
            session_server.__dict__[cls._ATTRIBUTE_USER_PERSON] = \
                converter.deserialize(
                    endpoint.UserPerson,
                    user_dict_wrapped[cls._FIELD_USER_PERSON]
                )
        elif cls._FIELD_USER_API_KEY in user_dict_wrapped:
            session_server.__dict__[cls._ATTRIBUTE_USER_API_KEY] = \
                converter.deserialize(
                    endpoint.UserApiKey,
                    user_dict_wrapped[cls._FIELD_USER_API_KEY]
                )
        elif cls._FIELD_USER_PAYMENT_SERVER_PROVIDER in user_dict_wrapped:
            session_server.__dict__[cls._ATTRIBUTE_USER_PAYMENT_SERVER_PROVIDER] = \
                converter.deserialize(
                    endpoint.UserPaymentServiceProvider,
                    user_dict_wrapped[cls._FIELD_USER_PAYMENT_SERVER_PROVIDER]
                )
        else:
            raise BunqException(cls._ERROR_COULD_NOT_DETERMINE_USER)

        return session_server

    @classmethod
    def serialize(cls, session_server: SessionServer) -> List:
        return [
            {cls._FIELD_ID: converter.serialize(session_server.id_)},
            {cls._FIELD_TOKEN: converter.serialize(session_server.token)},
            {
                cls._FIELD_USER_COMPANY:
                    converter.serialize(session_server.user_company),
            },
            {
                cls._FIELD_USER_PERSON:
                    converter.serialize(session_server.user_person),
            },
            {
                cls._FIELD_USER_API_KEY:
                    converter.serialize(session_server.user_api_key),
            },
            {
                cls._FIELD_USER_PAYMENT_SERVER_PROVIDER:
                    converter.serialize(session_server.user_payment_service_provider),
            },
        ]

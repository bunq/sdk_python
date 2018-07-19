import datetime
import urllib.parse as urlparse

from bunq.sdk import client
from bunq.sdk import context
from bunq.sdk import security
from bunq.sdk.exception import BunqException
from bunq.sdk.json import converter
from bunq.sdk.model import core
from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated import object_


class AnchoredObjectModelAdapter(converter.JsonAdapter):
    _ERROR_MODEL_NOT_FOUND = '{} is not in endpoint nor object.'

    __STRING_FORMAT_UNDERSCORE = '_'

    _override_field_map = {
        'ScheduledPayment': 'SchedulePayment',
        'ScheduledInstance': 'ScheduleInstance',
    }

    @classmethod
    def deserialize(cls, cls_target, obj_raw):
        """
        :type cls_target: core.BunqModel
        :type obj_raw: int|str|bool|float|list|dict|None

        :rtype: T
        """

        model_ = super()._deserialize_default(cls_target, obj_raw)

        if isinstance(
                model_,
                core.AnchoredObjectInterface
        ) and model_.is_all_field_none():
            for field in model_.__dict__:
                object_class = cls._get_object_class(field)
                contents = super()._deserialize_default(object_class, obj_raw)

                if contents.is_all_field_none():
                    setattr(model_, field, None)
                else:
                    setattr(model_, field, contents)

        return model_

    @classmethod
    def can_serialize(cls):
        return False

    @classmethod
    def _get_object_class(cls, class_name):
        """
        :type class_name: str
        :rtype: core.BunqModel
        """

        class_name = class_name.lstrip(cls.__STRING_FORMAT_UNDERSCORE)

        if class_name in cls._override_field_map:
            class_name = cls._override_field_map[class_name]

        try:
            return getattr(endpoint, class_name)
        except AttributeError:
            pass

        try:
            return getattr(object_, class_name)
        except AttributeError:
            pass

        raise BunqException(cls._ERROR_MODEL_NOT_FOUND.format(class_name))


class InstallationAdapter(converter.JsonAdapter):
    # Id constants
    _ATTRIBUTE_ID = '_id_'
    _INDEX_ID = 0
    _FIELD_ID = 'Id'

    # Token constants
    _ATTRIBUTE_TOKEN = '_token'
    _INDEX_TOKEN = 1
    _FIELD_TOKEN = 'Token'

    # Server Public Key constants
    _ATTRIBUTE_SERVER_PUBLIC_KEY = '_server_public_key'
    _INDEX_SERVER_PUBLIC_KEY = 2
    _FIELD_SERVER_PUBLIC_KEY = 'ServerPublicKey'

    @classmethod
    def deserialize(cls, target_class, array):
        """
        :type target_class: core.Installation|type
        :type array: list

        :rtype: core.Installation
        """

        installation = target_class.__new__(target_class)
        server_public_key_wrapped = array[cls._INDEX_SERVER_PUBLIC_KEY]
        installation.__dict__ = {
            cls._ATTRIBUTE_ID: converter.deserialize(
                core.Id,
                array[cls._INDEX_ID][cls._FIELD_ID]
            ),
            cls._ATTRIBUTE_TOKEN: converter.deserialize(
                core.SessionToken,
                array[cls._INDEX_TOKEN][cls._FIELD_TOKEN]
            ),
            cls._ATTRIBUTE_SERVER_PUBLIC_KEY: converter.deserialize(
                core.PublicKeyServer,
                server_public_key_wrapped[cls._FIELD_SERVER_PUBLIC_KEY]
            ),
        }

        return installation

    @classmethod
    def serialize(cls, installation):
        """
        :type installation: core.Installation

        :rtype: list
        """

        return [
            {cls._FIELD_ID: converter.serialize(installation.id_)},
            {cls._FIELD_TOKEN: converter.serialize(installation.token)},
            {
                cls._FIELD_SERVER_PUBLIC_KEY: converter.serialize(
                    installation.server_public_key
                ),
            },
        ]


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

    @classmethod
    def deserialize(cls, target_class, array):
        """
        :type target_class: core.SessionServer|type
        :type array: list

        :rtype: core.SessionServer
        """

        session_server = target_class.__new__(target_class)
        session_server.__dict__ = {
            cls._ATTRIBUTE_ID: converter.deserialize(
                core.Id,
                array[cls._INDEX_ID][cls._FIELD_ID]
            ),
            cls._ATTRIBUTE_TOKEN: converter.deserialize(
                core.SessionToken,
                array[cls._INDEX_TOKEN][cls._FIELD_TOKEN]
            ),
            cls._ATTRIBUTE_USER_COMPANY: None,
            cls._ATTRIBUTE_USER_PERSON: None,
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
        else:
            raise BunqException(cls._ERROR_COULD_NOT_DETERMINE_USER)

        return session_server

    @classmethod
    def serialize(cls, session_server):
        """
        :type session_server: core.SessionServer

        :rtype: list
        """

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
        ]


class InstallationContextAdapter(converter.JsonAdapter):
    # Attribute/Field constants
    _ATTRIBUTE_TOKEN = '_token'
    _FIELD_TOKEN = 'token'

    _ATTRIBUTE_PRIVATE_KEY_CLIENT = '_private_key_client'
    _FIELD_PRIVATE_KEY_CLIENT = 'private_key_client'

    _ATTRIBUTE_PUBLIC_KEY_CLIENT = '_public_key_client'
    _FIELD_PUBLIC_KEY_CLIENT = 'public_key_client'

    _ATTRIBUTE_PUBLIC_KEY_SERVER = '_public_key_server'
    _FIELD_PUBLIC_KEY_SERVER = 'public_key_server'

    @classmethod
    def deserialize(cls, target_class, obj):
        """
        :type target_class: context.InstallationContext|type
        :type obj: dict

        :rtype: context.InstallationContext
        """

        installation_context = target_class.__new__(target_class)
        private_key_client = security.rsa_key_from_string(
            obj[cls._FIELD_PRIVATE_KEY_CLIENT]
        )
        public_key_client = security.rsa_key_from_string(
            obj[cls._FIELD_PUBLIC_KEY_CLIENT]
        )
        public_key_server = security.rsa_key_from_string(
            obj[cls._FIELD_PUBLIC_KEY_SERVER]
        )
        installation_context.__dict__ = {
            cls._ATTRIBUTE_TOKEN: obj[cls._FIELD_TOKEN],
            cls._ATTRIBUTE_PRIVATE_KEY_CLIENT: private_key_client,
            cls._ATTRIBUTE_PUBLIC_KEY_CLIENT: public_key_client,
            cls._ATTRIBUTE_PUBLIC_KEY_SERVER: public_key_server,
        }

        return installation_context

    @classmethod
    def serialize(cls, installation_context):
        """
        :type installation_context: context.InstallationContext

        :rtype: dict
        """

        return {
            cls._FIELD_TOKEN: installation_context.token,
            cls._FIELD_PUBLIC_KEY_CLIENT: security.public_key_to_string(
                installation_context.private_key_client.publickey()
            ),
            cls._FIELD_PRIVATE_KEY_CLIENT: security.private_key_to_string(
                installation_context.private_key_client
            ),
            cls._FIELD_PUBLIC_KEY_SERVER: security.public_key_to_string(
                installation_context.public_key_server
            ),
        }


class ApiEnvironmentTypeAdapter(converter.JsonAdapter):
    @classmethod
    def deserialize(cls, target_class, name):
        """
        :type target_class: context.ApiEnvironmentType|type
        :type name: str

        :rtype: context.ApiEnvironmentType
        """

        _ = target_class

        return context.ApiEnvironmentType[name]

    @classmethod
    def serialize(cls, api_environment_type):
        """
        :type api_environment_type: context.ApiEnvironmentType

        :rtype: str
        """

        return api_environment_type.name


class FloatAdapter(converter.JsonAdapter):
    # Precision to round the floats to before outputting them
    _PRECISION_FLOAT = 2

    @classmethod
    def deserialize(cls, target_class, string):
        """
        :type target_class: float|type
        :type string: str

        :rtype: float
        """

        _ = target_class

        return float(string)

    @classmethod
    def serialize(cls, number):
        """
        :type number: float

        :rtype: str
        """

        return str(round(number, cls._PRECISION_FLOAT))


class GeolocationAdapter(converter.JsonAdapter):
    # Field constants
    _FIELD_LATITUDE = 'latitude'
    _FIELD_LONGITUDE = 'longitude'
    _FIELD_ALTITUDE = 'altitude'
    _FIELD_RADIUS = 'radius'

    @classmethod
    def can_deserialize(cls):
        """
        :rtype: bool
        """

        return False

    @classmethod
    def deserialize(cls, target_class, obj):
        """
        :type target_class: float|type
        :type obj: dict

        :raise: NotImplementedError
        """

        _ = target_class, obj

        raise NotImplementedError()

    @classmethod
    def serialize(cls, geolocation):
        """
        :type geolocation: object_.Geolocation

        :rtype: dict
        """

        obj = {}

        cls.add_if_not_none(obj, cls._FIELD_LATITUDE, geolocation.latitude)
        cls.add_if_not_none(obj, cls._FIELD_LONGITUDE, geolocation.longitude)
        cls.add_if_not_none(obj, cls._FIELD_ALTITUDE, geolocation.altitude)
        cls.add_if_not_none(obj, cls._FIELD_RADIUS, geolocation.radius)

        return obj

    @classmethod
    def add_if_not_none(cls, dict_, key, value):
        """
        :type dict_: dict[str, str]
        :type key: str
        :type value: float

        :rtype: None
        """

        if value is not None:
            dict_[key] = str(value)


class MonetaryAccountReferenceAdapter(converter.JsonAdapter):
    @classmethod
    def deserialize(cls, target_class, obj):
        """
        :type target_class: object_.MonetaryAccountReference|type
        :type obj: dict

        :rtype: object_.MonetaryAccountReference
        """

        label_monetary_account = converter.deserialize(
            object_.LabelMonetaryAccount,
            obj
        )

        return target_class.create_from_label_monetary_account(
            label_monetary_account
        )

    @classmethod
    def serialize(cls, monetary_account_reference):
        """
        :type monetary_account_reference: object_.MonetaryAccountReference

        :rtype: dict
        """

        return converter.serialize(monetary_account_reference.pointer)


class ShareDetailAdapter(converter.JsonAdapter):
    # Attribute/Field constants
    _ATTRIBUTE_PAYMENT = 'payment'
    _FIELD_PAYMENT = 'ShareDetailPayment'

    _ATTRIBUTE_READ_ONLY = 'read_only'
    _FIELD_READ_ONLY = 'ShareDetailReadOnly'

    _ATTRIBUTE_DRAFT_PAYMENT = 'draft_payment'
    _FIELD_DRAFT_PAYMENT = 'ShareDetailDraftPayment'

    @classmethod
    def deserialize(cls, target_class, obj):
        """
        :type target_class: object_.ShareDetail|type
        :type obj: dict

        :rtype: object_.ShareDetail
        """

        share_detail = target_class.__new__(target_class)
        share_detail.__dict__ = {
            cls._ATTRIBUTE_PAYMENT: converter.deserialize(
                object_.ShareDetailPayment,
                cls._get_field_or_none(cls._FIELD_DRAFT_PAYMENT, obj)
            ),
            cls._ATTRIBUTE_READ_ONLY: converter.deserialize(
                object_.ShareDetailReadOnly,
                cls._get_field_or_none(cls._FIELD_READ_ONLY, obj)
            ),
            cls._ATTRIBUTE_DRAFT_PAYMENT: converter.deserialize(
                object_.ShareDetailDraftPayment,
                cls._get_field_or_none(cls._FIELD_DRAFT_PAYMENT, obj)
            ),
        }

        return share_detail

    @staticmethod
    def _get_field_or_none(field, obj):
        """
        :type field: str
        :type obj: dict

        :return: dict|None
        """

        return obj[field] if field in obj else None

    @classmethod
    def serialize(cls, share_detail):
        """
        :type share_detail: object_.ShareDetail

        :rtype: dict
        """

        return {
            cls._FIELD_PAYMENT: converter.serialize(
                share_detail._payment_field_for_request),
            cls._FIELD_READ_ONLY: converter.serialize(
                share_detail._read_only_field_for_request),
            cls._FIELD_DRAFT_PAYMENT: converter.serialize(
                share_detail._draft_payment
            ),
        }


class DateTimeAdapter(converter.JsonAdapter):
    # bunq timestamp format
    _FORMAT_TIMESTAMP = '%Y-%m-%d %H:%M:%S.%f'

    @classmethod
    def deserialize(cls, target_class, string):
        """
        :type target_class: datetime.datetime|type
        :type string: str

        :rtype: datetime.datetime
        """

        return target_class.strptime(string, cls._FORMAT_TIMESTAMP)

    @classmethod
    def serialize(cls, timestamp):
        """
        :type timestamp: datetime.datetime

        :rtype: dict
        """

        return timestamp.strftime(cls._FORMAT_TIMESTAMP)


class PaginationAdapter(converter.JsonAdapter):
    # Raw pagination response field constants.
    _FIELD_FUTURE_URL = 'future_url'
    _FIELD_NEWER_URL = 'newer_url'
    _FIELD_OLDER_URL = 'older_url'

    # Processed pagination field constants.
    _FIELD_OLDER_ID = 'older_id'
    _FIELD_NEWER_ID = 'newer_id'
    _FIELD_FUTURE_ID = 'future_id'
    _FIELD_COUNT = 'count'

    # Very first index in an array.
    _INDEX_FIRST = 0

    @classmethod
    def deserialize(cls, target_class, pagination_response):
        """
        :type target_class: client.Pagination|type
        :type pagination_response: dict

        :rtype: client.Pagination
        """

        pagination = client.Pagination()
        pagination.__dict__.update(
            cls.parse_pagination_dict(pagination_response)
        )

        return pagination

    @classmethod
    def parse_pagination_dict(cls, response_obj):
        """
        :type response_obj: dict

        :rtype: dict
        """

        pagination_dict = {}

        cls.update_dict_id_field_from_response_field(
            pagination_dict,
            cls._FIELD_OLDER_ID,
            response_obj,
            cls._FIELD_OLDER_URL,
            client.Pagination.PARAM_OLDER_ID
        )
        cls.update_dict_id_field_from_response_field(
            pagination_dict,
            cls._FIELD_NEWER_ID,
            response_obj,
            cls._FIELD_NEWER_URL,
            client.Pagination.PARAM_NEWER_ID
        )
        cls.update_dict_id_field_from_response_field(
            pagination_dict,
            cls._FIELD_FUTURE_ID,
            response_obj,
            cls._FIELD_FUTURE_URL,
            client.Pagination.PARAM_NEWER_ID
        )

        return pagination_dict

    @classmethod
    def update_dict_id_field_from_response_field(cls, dict_, dict_id_field,
                                                 response_obj, response_field,
                                                 response_param):
        """
        :type dict_: dict
        :type dict_id_field: str
        :type response_obj: dict
        :type response_field: str
        :type response_param: str
        """

        url = response_obj[response_field]

        if url is not None:
            url_parsed = urlparse.urlparse(url)
            parameters = urlparse.parse_qs(url_parsed.query)
            dict_[dict_id_field] = int(
                parameters[response_param][cls._INDEX_FIRST]
            )

            if cls._FIELD_COUNT in parameters and cls._FIELD_COUNT not in dict_:
                dict_[cls._FIELD_COUNT] = int(
                    parameters[client.Pagination.PARAM_COUNT][cls._INDEX_FIRST]
                )

    @classmethod
    def serialize(cls, pagination):
        """
        :type pagination: client.Pagination

        :raise: NotImplementedError
        """

        _ = pagination

        raise NotImplementedError()

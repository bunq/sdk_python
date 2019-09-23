from bunq import Pagination
from bunq.sdk.http.bunq_response import BunqResponse
from bunq.sdk.json import converter


class BunqModel(object):
    # Field constants
    _FIELD_RESPONSE = 'Response'
    _FIELD_PAGINATION = 'Pagination'
    _FIELD_ID = 'Id'
    _FIELD_UUID = 'Uuid'

    # The very first index of an array
    _INDEX_FIRST = 0

    __STRING_FORMAT_EMPTY = ''
    __STRING_FORMAT_FIELD_FOR_REQUEST_ONE_UNDERSCORE = '_field_for_request'
    __STRING_FORMAT_FIELD_FOR_REQUEST_TWO_UNDERSCORE = '__field_for_request'

    def is_all_field_none(self):
        raise NotImplementedError

    def to_json(self):
        """
        :rtype: str
        """

        return converter.class_to_json(self)

    @staticmethod
    def from_json(json_str):
        raise NotImplementedError

    @classmethod
    def _from_json_array_nested(cls, response_raw):
        """
        :type response_raw: BunqResponseRaw

        :rtype: BunqResponse[cls]
        """

        json = response_raw.body_bytes.decode()
        obj = converter.json_to_class(dict, json)
        value = converter.deserialize(cls, obj[cls._FIELD_RESPONSE])

        return BunqResponse(value, response_raw.headers)

    @classmethod
    def _from_json(cls, response_raw, wrapper=None):
        """
        :type response_raw: BunqResponseRaw
        :type wrapper: str|None

        :rtype: BunqResponse[cls]
        """

        json = response_raw.body_bytes.decode()
        obj = converter.json_to_class(dict, json)
        value = converter.deserialize(
            cls,
            cls._unwrap_response_single(obj, wrapper)
        )

        return BunqResponse(value, response_raw.headers)

    @classmethod
    def _unwrap_response_single(cls, obj, wrapper=None):
        """
        :type obj: dict
        :type wrapper: str|None

        :rtype: dict
        """

        if wrapper is not None:
            return obj[cls._FIELD_RESPONSE][cls._INDEX_FIRST][wrapper]

        return obj[cls._FIELD_RESPONSE][cls._INDEX_FIRST]

    @classmethod
    def _process_for_id(cls, response_raw):
        """
        :type response_raw: BunqResponseRaw

        :rtype: BunqResponse[int]
        """

        from bunq.sdk.model.core.id import Id

        json = response_raw.body_bytes.decode()
        obj = converter.json_to_class(dict, json)
        id_ = converter.deserialize(
            Id,
            cls._unwrap_response_single(obj, cls._FIELD_ID)
        )

        return BunqResponse(id_.id_, response_raw.headers)

    @classmethod
    def _process_for_uuid(cls, response_raw):
        """
        :type response_raw: BunqResponseRaw

        :rtype: BunqResponse[str]
        """

        from bunq.sdk.model.core.uuid import Uuid

        json = response_raw.body_bytes.decode()
        obj = converter.json_to_class(dict, json)
        uuid = converter.deserialize(
            Uuid,
            cls._unwrap_response_single(obj, cls._FIELD_UUID)
        )

        return BunqResponse(uuid.uuid, response_raw.headers)

    @classmethod
    def _from_json_list(cls, response_raw, wrapper=None):
        """
        :type response_raw: BunqResponseRaw
        :type wrapper: str|None

        :rtype: BunqResponse[list[cls]]
        """

        json = response_raw.body_bytes.decode()
        obj = converter.json_to_class(dict, json)
        array = obj[cls._FIELD_RESPONSE]
        array_deserialized = []

        for item in array:
            item_unwrapped = item if wrapper is None else item[wrapper]
            item_deserialized = converter.deserialize(cls, item_unwrapped)
            array_deserialized.append(item_deserialized)

        pagination = converter.deserialize(Pagination, obj[cls._FIELD_PAGINATION])

        return BunqResponse(array_deserialized, response_raw.headers, pagination)

    @classmethod
    def _get_api_context(cls):
        """
        :rtype: ApiContext
        """

        from bunq.sdk.context.bunq_context import BunqContext

        return BunqContext.api_context()

    @classmethod
    def _determine_user_id(cls):
        """
        :rtype: int
        """

        from bunq.sdk.context.bunq_context import BunqContext

        return BunqContext.user_context().user_id

    @classmethod
    def _determine_monetary_account_id(cls, monetary_account_id=None):
        """
        :type monetary_account_id: int

        :rtype: int
        """

        from bunq.sdk.context.bunq_context import BunqContext

        if monetary_account_id is None:
            return BunqContext.user_context().primary_monetary_account.id_

        return monetary_account_id

    @classmethod
    def _remove_field_for_request(cls, json_str: str):
        return json_str.replace(
            cls.__STRING_FORMAT_FIELD_FOR_REQUEST_TWO_UNDERSCORE,
            cls.__STRING_FORMAT_EMPTY
        ).replace(
            cls.__STRING_FORMAT_FIELD_FOR_REQUEST_ONE_UNDERSCORE,
            cls.__STRING_FORMAT_EMPTY
        )

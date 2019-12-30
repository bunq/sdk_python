import urllib.parse as urlparse
from typing import Type, Dict

from bunq import Pagination
from bunq.sdk.json import converter


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
    def deserialize(cls,
                    target_class: Type[Pagination],
                    pagination_response: Dict) -> Pagination:
        pagination = Pagination()
        pagination.__dict__.update(
            cls.parse_pagination_dict(pagination_response)
        )

        return pagination

    @classmethod
    def parse_pagination_dict(cls, response_obj: Dict) -> Dict:
        pagination_dict = {}

        cls.update_dict_id_field_from_response_field(
            pagination_dict,
            cls._FIELD_OLDER_ID,
            response_obj,
            cls._FIELD_OLDER_URL,
            Pagination.PARAM_OLDER_ID
        )
        cls.update_dict_id_field_from_response_field(
            pagination_dict,
            cls._FIELD_NEWER_ID,
            response_obj,
            cls._FIELD_NEWER_URL,
            Pagination.PARAM_NEWER_ID
        )
        cls.update_dict_id_field_from_response_field(
            pagination_dict,
            cls._FIELD_FUTURE_ID,
            response_obj,
            cls._FIELD_FUTURE_URL,
            Pagination.PARAM_NEWER_ID
        )

        return pagination_dict

    @classmethod
    def update_dict_id_field_from_response_field(cls, dict_: Dict,
                                                 dict_id_field: str,
                                                 response_obj: Dict,
                                                 response_field: str,
                                                 response_param: str) -> None:
        url = response_obj[response_field]

        if url is not None:
            url_parsed = urlparse.urlparse(url)
            parameters = urlparse.parse_qs(url_parsed.query)
            dict_[dict_id_field] = int(
                parameters[response_param][cls._INDEX_FIRST]
            )

            if cls._FIELD_COUNT in parameters and cls._FIELD_COUNT not in dict_:
                dict_[cls._FIELD_COUNT] = int(
                    parameters[Pagination.PARAM_COUNT][cls._INDEX_FIRST]
                )

    @classmethod
    def serialize(cls, pagination: Pagination) -> None:
        raise NotImplementedError()

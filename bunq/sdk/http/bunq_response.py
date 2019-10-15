from __future__ import annotations

# from types import ModuleType
from typing import Dict, TypeVar

from bunq import Pagination


class BunqResponse:
    """
    :type _value: T
    :type _headers: dict[str, str]
    :type _pagination: Pagination|None
    """

    T = TypeVar('T')

    def __init__(self,
                 value: T,
                 headers: Dict[str, str],
                 pagination: Pagination = None) -> None:
        """

        :param value:
        :param headers:
        :param pagination:
        """

        self._value = value
        self._headers = headers
        self._pagination = pagination

    @property
    def value(self) -> T:
        return self._value

    @property
    def headers(self) -> Dict[str, str]:
        return self._headers

    @property
    def pagination(self) -> Pagination:
        return self._pagination

    @classmethod
    def cast_from_bunq_response(cls, bunq_response: BunqResponse) -> BunqResponse:
        """
        :type bunq_response: BunqResponse
        """

        return cls(
            bunq_response.value,
            bunq_response.headers,
            bunq_response.pagination
        )

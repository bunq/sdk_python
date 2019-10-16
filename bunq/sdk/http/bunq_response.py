from __future__ import annotations

from typing import Dict, Generic

from bunq import Pagination
from bunq.sdk.util.type_alias import T


class BunqResponse(Generic[T]):
    """
    :type _value: T
    :type _headers: dict[str, str]
    :type _pagination: Pagination|None
    """

    def __init__(self,
                 value: T,
                 headers: Dict[str, str],
                 pagination: Pagination = None) -> None:
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
        return cls(
            bunq_response.value,
            bunq_response.headers,
            bunq_response.pagination
        )

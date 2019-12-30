from typing import Dict


class BunqResponseRaw:
    """
    :type _body_bytes: bytes
    :type _headers: dict[str, str]
    """

    def __init__(self,
                 body_bytes: bytes,
                 headers: Dict[str, str]) -> None:
        self._body_bytes = body_bytes
        self._headers = headers

    @property
    def body_bytes(self) -> bytes:
        return self._body_bytes

    @property
    def headers(self) -> Dict[str, str]:
        return self._headers

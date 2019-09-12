class BunqResponseRaw(object):
    """
    :type _body_bytes: bytes
    :type _headers: dict[str, str]
    """

    def __init__(self, body_bytes, headers):
        """
        :type body_bytes: bytes
        :type headers: dict[str, str]
        """

        self._body_bytes = body_bytes
        self._headers = headers

    @property
    def body_bytes(self):
        """
        :rtype: bytes
        """

        return self._body_bytes

    @property
    def headers(self):
        """
        :rtype: dict[str, str]
        """

        return self._headers

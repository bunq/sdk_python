class BunqResponse(object):
    """
    :type _value: T
    :type _headers: dict[str, str]
    :type _pagination: Pagination|None
    """

    def __init__(self, value, headers, pagination=None):
        """
        :type value: T
        :type headers: dict[str, str]
        :type pagination Pagination|None
        """

        self._value = value
        self._headers = headers
        self._pagination = pagination

    @property
    def value(self):
        """
        :rtype: T
        """

        return self._value

    @property
    def headers(self):
        """
        :rtype: dict[str, str]
        """

        return self._headers

    @property
    def pagination(self):
        """
        :rtype: Pagination
        """

        return self._pagination

    @classmethod
    def cast_from_bunq_response(cls, bunq_response):
        """
        :type bunq_response: BunqResponse
        """

        return cls(
            bunq_response.value,
            bunq_response.headers,
            bunq_response.pagination
        )

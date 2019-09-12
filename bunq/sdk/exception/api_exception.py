class ApiException(Exception):
    def __init__(self, message, response_code, response_id):
        """
        :type response_id: str
        :type message: str
        :type response_code: int
        """

        self._response_id = response_id
        self._message = message
        self._response_code = response_code

        super(ApiException, self).__init__(message)

    @property
    def message(self):
        """
        :rtype: str
        """

        return self._message

    @property
    def response_code(self):
        """
        :rtype: int
        """

        return self._response_code

    @property
    def response_id(self):
        """
        :rtype: str
        """

        return self._response_id

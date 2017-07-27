class ApiException(Exception):
    """
    :type _response_code: int
    """

    # Constants for formatting messages
    _FORMAT_RESPONSE_CODE_LINE = 'HTTP Response Code: {}'
    _GLUE_ERROR_MESSAGES = '\n'

    def __init__(self, response_code, messages):
        """
        :type response_code: int
        :type messages: list[str]
        """

        super(ApiException, self).__init__(
            self.generate_message_error(response_code, messages)
        )
        self._response_code = response_code

    def generate_message_error(self, response_code, messages):
        """
        :type response_code: int
        :type messages: list[str]

        :rtype: str
        """

        line_response_code = self._FORMAT_RESPONSE_CODE_LINE \
            .format(response_code)

        return self.glue_messages([line_response_code] + messages)

    def glue_messages(self, messages):
        """
        :type messages: list[str]

        :rtype: str
        """

        return self._GLUE_ERROR_MESSAGES.join(messages)

    @property
    def response_code(self):
        """
        :rtype: int
        """

        return self._response_code


class BunqException(Exception):
    def __init__(self, message):
        super(BunqException, self).__init__(message)

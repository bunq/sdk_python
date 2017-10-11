class ApiException(Exception):
    def __init__(self, message, response_code):
        """
        :type message: str
        :type response_code: int
        """

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


class BunqException(Exception):
    def __init__(self, message):
        super(BunqException, self).__init__(message)


class UnknownApiErrorException(ApiException):
    pass


class BadRequestException(ApiException):
    pass


class UnauthorizedException(ApiException):
    pass


class ForbiddenException(ApiException):
    pass


class NotFoundException(ApiException):
    pass


class MethodNotAllowedException(ApiException):
    pass


class TooManyRequestsException(ApiException):
    pass


class PleaseContactBunqException(ApiException):
    pass

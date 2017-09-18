class BunqError(Exception):
    def __init__(self, message, response_code):
        """
        :type message: str
        :type response_code: int
        """

        self._response_code = response_code
        self._message = message

        super(BunqError, self).__init__(message)

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


class ApiException(BunqError):
    pass


class BadRequestException(BunqError):
    pass


class UnauthorizedException(BunqError):
    pass


class ForbiddenException(BunqError):
    pass


class NotFoundException(BunqError):
    pass


class MethodNotAllowedException(BunqError):
    pass


class ToManyRequestsException(BunqError):
    pass


class PleaseContactBunqException(BunqError):
    pass


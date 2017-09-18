class BunqError(Exception):
    def __init__(self, message, response_code):
        self._response_code = response_code
        self._message = message

        super(BunqError, self).__init__(message)

    @property
    def message(self):
        return self._message

    @property
    def response_code(self):
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


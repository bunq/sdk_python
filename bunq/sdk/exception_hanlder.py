from bunq.sdk.exception import BadRequestException
from bunq.sdk.exception import UnauthorizedException
from bunq.sdk.exception import ForbiddenException
from bunq.sdk.exception import NotFoundException
from bunq.sdk.exception import MethodNotAllowedException
from bunq.sdk.exception import ToManyRequestsException
from bunq.sdk.exception import PleaseContactBunqException
from bunq.sdk.exception import ApiException


class ExceptionHandler(Exception):
    # Error response code constants
    _HTTP_RESPONSE_CODE_BAD_REQUEST = 400
    _HTTP_RESPONSE_CODE_UNAUTHORIZED = 401
    _HTTP_RESPONSE_CODE_FORBIDDEN = 403
    _HTTP_RESPONSE_CODE_NOT_FOUND = 404
    _HTTP_RESPONSE_CODE_METHOD_NOT_ALLOWED = 405
    _HTTP_RESPONSE_CODE_TOO_MANY_REQUESTS = 429
    _HTTP_RESPONSE_CODE_INTERNAL_SERVER_ERROR = 500

    # Constants for formatting messages
    _FORMAT_RESPONSE_CODE_LINE = 'HTTP Response Code: {}'
    _GLUE_ERROR_MESSAGES = '\n'

    @classmethod
    def create_exception_for_response(cls, response_code, messages):
        error_message = cls._generate_message_error(response_code, messages)

        if response_code == cls._HTTP_RESPONSE_CODE_BAD_REQUEST:
            return BadRequestException(error_message, response_code)
        if response_code == cls._HTTP_RESPONSE_CODE_UNAUTHORIZED:
            return UnauthorizedException(error_message, response_code)
        if response_code == cls._HTTP_RESPONSE_CODE_FORBIDDEN:
            return ForbiddenException(error_message, response_code)
        if response_code == cls._HTTP_RESPONSE_CODE_NOT_FOUND:
            return NotFoundException(error_message, response_code)
        if response_code == cls._HTTP_RESPONSE_CODE_METHOD_NOT_ALLOWED:
            return MethodNotAllowedException(error_message, response_code)
        if response_code == cls._HTTP_RESPONSE_CODE_TOO_MANY_REQUESTS:
            return ToManyRequestsException(error_message, response_code)
        if response_code == cls._HTTP_RESPONSE_CODE_INTERNAL_SERVER_ERROR:
            return PleaseContactBunqException(error_message, response_code)

        return ApiException(error_message, response_code)

    @classmethod
    def _generate_message_error(cls, response_code, messages):
        """
        :type response_code: int
        :type messages: list[str]

        :rtype: str
        """

        line_response_code = cls._FORMAT_RESPONSE_CODE_LINE \
            .format(response_code)

        return cls._glue_messages([line_response_code] + messages)

    @classmethod
    def _glue_messages(cls, messages):
        """
        :type messages: list[str]

        :rtype: str
        """

        return cls._GLUE_ERROR_MESSAGES.join(messages)

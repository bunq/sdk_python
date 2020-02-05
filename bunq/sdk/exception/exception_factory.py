from typing import List

from bunq.sdk.exception.api_exception import ApiException
from bunq.sdk.exception.bad_request_exception import BadRequestException
from bunq.sdk.exception.forbidden_exception import ForbiddenException
from bunq.sdk.exception.method_not_allowed_exception import MethodNotAllowedException
from bunq.sdk.exception.not_found_exception import NotFoundException
from bunq.sdk.exception.please_contact_bunq_exception import PleaseContactBunqException
from bunq.sdk.exception.too_many_requests_exception import TooManyRequestsException
from bunq.sdk.exception.unauthorized_exception import UnauthorizedException
from bunq.sdk.exception.unknown_api_error_exception import UnknownApiErrorException


class ExceptionFactory:
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
    _FORMAT_RESPONSE_ID_LINE = 'The response id to help bunq debug: {}'
    _FORMAT_ERROR_MESSAGE_LINE = 'Error message: {}'
    _GLUE_ERROR_MESSAGE_NEW_LINE = '\n'
    _GLUE_ERROR_MESSAGE_STRING_EMPTY = ''

    @classmethod
    def create_exception_for_response(
            cls,
            response_code: int,
            messages: List[str],
            response_id: str
    ) -> ApiException:
        """

        :return: The exception according to the status code.
        """

        error_message = cls._generate_message_error(
            response_code,
            messages,
            response_id
        )

        if response_code == cls._HTTP_RESPONSE_CODE_BAD_REQUEST:
            return BadRequestException(
                error_message,
                response_code,
                response_id
            )
        if response_code == cls._HTTP_RESPONSE_CODE_UNAUTHORIZED:
            return UnauthorizedException(
                error_message,
                response_code,
                response_id
            )
        if response_code == cls._HTTP_RESPONSE_CODE_FORBIDDEN:
            return ForbiddenException(
                error_message,
                response_code,
                response_id
            )
        if response_code == cls._HTTP_RESPONSE_CODE_NOT_FOUND:
            return NotFoundException(
                error_message,
                response_code,
                response_id
            )
        if response_code == cls._HTTP_RESPONSE_CODE_METHOD_NOT_ALLOWED:
            return MethodNotAllowedException(
                error_message,
                response_code,
                response_id
            )
        if response_code == cls._HTTP_RESPONSE_CODE_TOO_MANY_REQUESTS:
            return TooManyRequestsException(
                error_message,
                response_code,
                response_id
            )
        if response_code == cls._HTTP_RESPONSE_CODE_INTERNAL_SERVER_ERROR:
            return PleaseContactBunqException(
                error_message,
                response_code,
                response_id
            )

        return UnknownApiErrorException(
            error_message,
            response_code,
            response_id
        )

    @classmethod
    def _generate_message_error(cls,
                                response_code: int,
                                messages: List[str],
                                response_id: str) -> str:
        line_response_code = cls._FORMAT_RESPONSE_CODE_LINE.format(response_code)
        line_response_id = cls._FORMAT_RESPONSE_ID_LINE.format(response_id)
        line_error_message = cls._FORMAT_ERROR_MESSAGE_LINE.format(cls._GLUE_ERROR_MESSAGE_STRING_EMPTY.join(messages))

        return cls._glue_all_error_message([line_response_code, line_response_id, line_error_message])

    @classmethod
    def _glue_all_error_message(cls, messages: List[str]) -> str:
        return cls._GLUE_ERROR_MESSAGE_NEW_LINE.join(messages)

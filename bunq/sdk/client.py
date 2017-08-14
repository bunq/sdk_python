import uuid

# Due to compatibility requirements, we are importing a class here.
try:
    from json import JSONDecodeError
except ImportError:
    from simplejson import JSONDecodeError

import requests

from bunq.sdk.json import converter
from bunq.sdk import security
from bunq.sdk import context
from bunq.sdk import exception


class ApiClient(object):
    """
    :type _api_context: context.ApiContext
    """

    # Header constants
    HEADER_ATTACHMENT_DESCRIPTION = 'X-Bunq-Attachment-Description'
    HEADER_CONTENT_TYPE = 'Content-Type'
    HEADER_CACHE_CONTROL = 'Cache-Control'
    HEADER_USER_AGENT = 'User-Agent'
    HEADER_LANGUAGE = 'X-Bunq-Language'
    HEADER_REGION = 'X-Bunq-Region'
    HEADER_REQUEST_ID = 'X-Bunq-Client-Request-Id'
    HEADER_GEOLOCATION = 'X-Bunq-Geolocation'
    HEADER_SIGNATURE = 'X-Bunq-Client-Signature'
    HEADER_AUTHENTICATION = 'X-Bunq-Client-Authentication'

    # Default header values
    _USER_AGENT_BUNQ = 'bunq-sdk-python/0.9.1'
    _GEOLOCATION_ZERO = '0 0 0 0 NL'
    _LANGUAGE_EN_US = 'en_US'
    _REGION_NL_NL = 'nl_NL'
    _CACHE_CONTROL_NONE = 'no-cache'

    # Request method names
    _METHOD_POST = 'POST'
    _METHOD_PUT = 'PUT'
    _METHOD_GET = 'GET'
    _METHOD_DELETE = 'DELETE'

    # Status code for successful execution
    _STATUS_CODE_OK = 200

    # Fields for fetching errors
    _FIELD_ERROR = 'Error'
    _FIELD_ERROR_DESCRIPTION = 'error_description'

    # Empty string
    _STRING_EMPTY = ''

    # Empty bytes
    _BYTES_EMPTY = b''

    def __init__(self, api_context):
        self._api_context = api_context

    def post(self, uri_relative, request_bytes, custom_headers):
        """
        :type uri_relative: str
        :type request_bytes: bytes
        :type custom_headers: dict[str, str]

        :return: BunqResponseRaw
        """

        return self._request(
            self._METHOD_POST,
            uri_relative,
            request_bytes,
            custom_headers
        )

    def _request(self, method, uri_relative, request_bytes, custom_headers):
        """
        :type method: str
        :type uri_relative: str
        :type request_bytes: bytes
        :type custom_headers: dict[str, str]

        :return: BunqResponseRaw
        """

        self._api_context.ensure_session_active()
        all_headers = self._get_all_headers(
            method,
            uri_relative,
            request_bytes,
            custom_headers
        )

        response = requests.request(
            method,
            self._get_uri_full(uri_relative),
            data=request_bytes,
            headers=all_headers
        )

        self._assert_response_success(response)

        if self._api_context.installation_context is not None:
            security.validate_response(
                self._api_context.installation_context.public_key_server,
                response.status_code,
                response.content,
                response.headers
            )

        return self._create_bunq_response_raw(response)

    def _get_all_headers(self, method, endpoint, request_bytes, custom_headers):
        """
        :type method: str
        :type endpoint: str
        :type request_bytes: bytes
        :type custom_headers: dict[str, str]

        :rtype: dict[str, str]
        """

        headers = self._get_default_headers()
        headers.update(custom_headers)

        if self._api_context.token is not None:
            headers[self.HEADER_AUTHENTICATION] = self._api_context.token
            headers[self.HEADER_SIGNATURE] = security.sign_request(
                self._api_context.installation_context.private_key_client,
                method,
                endpoint,
                request_bytes,
                headers
            )

        return headers

    @classmethod
    def _get_default_headers(cls):
        """
        :rtype: dict[str, str]
        """

        return {
            cls.HEADER_USER_AGENT: cls._USER_AGENT_BUNQ,
            cls.HEADER_REQUEST_ID: cls._generate_random_request_id(),
            cls.HEADER_GEOLOCATION: cls._GEOLOCATION_ZERO,
            cls.HEADER_LANGUAGE: cls._LANGUAGE_EN_US,
            cls.HEADER_REGION: cls._REGION_NL_NL,
            cls.HEADER_CACHE_CONTROL: cls._CACHE_CONTROL_NONE,
        }

    @staticmethod
    def _generate_random_request_id():
        """
        :rtype: str
        """

        return str(uuid.uuid4())

    def _get_uri_full(self, uri_relative):
        """
        :type uri_relative: str

        :rtype: str
        """

        return self._api_context.environment_type.uri_base + uri_relative

    def _assert_response_success(self, response):
        """
        :type response: requests.Response

        :rtype: None
        :raise ApiException: When the response is not successful.
        """

        if response.status_code != self._STATUS_CODE_OK:
            raise exception.ApiException(
                response.status_code,
                self._fetch_error_messages(response)
            )

    @classmethod
    def _create_bunq_response_raw(cls, response):
        """
        :type response: requests.Response

        :rtype: BunqResponseRaw
        """

        return BunqResponseRaw(response.content, response.headers)

    def _fetch_error_messages(self, response):
        """
        :type response: requests.Response

        :rtype: list[str]
        """

        response_content_string = response.content.decode()

        try:
            error_dict = converter.json_to_class(dict, response_content_string)

            return self._fetch_error_descriptions(error_dict)
        except JSONDecodeError:
            return [response_content_string]

    def _fetch_error_descriptions(self, error_dict):
        """
        :type error_dict: dict[str, list[dict[str, str]]

        :rtype: list[str]
        """

        error_descriptions = []

        for error in error_dict[self._FIELD_ERROR]:
            description = error[self._FIELD_ERROR_DESCRIPTION]
            error_descriptions.append(description)

        return error_descriptions

    def put(self, uri_relative, request_bytes, custom_headers):
        """
        :type uri_relative: str
        :type request_bytes: bytes
        :type custom_headers: dict[str, str]

        :rtype: BunqResponseRaw
        """

        return self._request(
            self._METHOD_PUT,
            uri_relative,
            request_bytes,
            custom_headers
        )

    def get(self, uri_relative, custom_headers):
        """
        :type uri_relative: str
        :type custom_headers: dict[str, str]

        :rtype: BunqResponseRaw
        """

        return self._request(
            self._METHOD_GET,
            uri_relative,
            self._BYTES_EMPTY,
            custom_headers
        )

    def delete(self, uri_relative, custom_headers):
        """
        :type uri_relative: str
        :type custom_headers: dict[str, str]

        :rtype: BunqResponseRaw
        """

        return self._request(
            self._METHOD_DELETE,
            uri_relative,
            self._BYTES_EMPTY,
            custom_headers
        )


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


class BunqResponse(object):
    """
    :type _value: T
    :type _headers: dict[str, str]
    """

    def __init__(self, value, headers):
        """
        :type value: T
        :type headers: dict[str, str]
        """

        self._value = value
        self._headers = headers

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

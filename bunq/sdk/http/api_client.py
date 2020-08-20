from __future__ import annotations

import typing
import uuid
from typing import Dict, List
from urllib.parse import urlencode

import requests
from requests import Response

from bunq.sdk.exception.exception_factory import ExceptionFactory
from bunq.sdk.http.bunq_response_raw import BunqResponseRaw
from bunq.sdk.json import converter
from bunq.sdk.security import security

if typing.TYPE_CHECKING:
    from bunq.sdk.context.api_context import ApiContext


class ApiClient:
    """
    :type _api_context: ApiContext
    """

    # Error constants
    _ERROR_COULD_NOT_DETERMINE_RESPONSE_ID_HEADER = ('The response header'
                                                     '"X-Bunq-Client-Response-'
                                                     'Id" or "x-bunq-client-'
                                                     'response-id" could not '
                                                     'be found.')

    # Endpoints not requiring active session for the request to succeed.
    _URL_DEVICE_SERVER = 'device-server'
    _URI_INSTALLATION = 'installation'
    _URI_SESSION_SERVER = 'session-server'
    _URL_PAYMENT_SERVICE_PROVIDER_CREDENTIAL = 'payment-service-provider-credential'
    _URIS_NOT_REQUIRING_ACTIVE_SESSION = [
        _URI_INSTALLATION,
        _URI_SESSION_SERVER,
        _URL_DEVICE_SERVER,
        _URL_PAYMENT_SERVICE_PROVIDER_CREDENTIAL,
    ]

    # HTTPS type of proxy, the only used at bunq
    FIELD_PROXY_HTTPS = 'https'

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
    HEADER_RESPONSE_ID_UPPER_CASED = 'X-Bunq-Client-Response-Id'
    HEADER_RESPONSE_ID_LOWER_CASED = 'x-bunq-client-response-id'

    # Default header values
    USER_AGENT_BUNQ = 'bunq-sdk-python/1.14.1'
    GEOLOCATION_ZERO = '0 0 0 0 NL'
    LANGUAGE_EN_US = 'en_US'
    REGION_NL_NL = 'nl_NL'
    CACHE_CONTROL_NONE = 'no-cache'

    # Request method names
    METHOD_POST = 'POST'
    METHOD_PUT = 'PUT'
    METHOD_GET = 'GET'
    METHOD_DELETE = 'DELETE'

    # Delimiter between path and params in URL
    DELIMITER_URL_QUERY = '?'

    # Status code for successful execution
    STATUS_CODE_OK = 200

    # Fields for fetching errors
    FIELD_ERROR = 'Error'
    FIELD_ERROR_DESCRIPTION = 'error_description'

    # Empty string
    STRING_EMPTY = ''

    # Empty bytes
    BYTES_EMPTY = b''

    def __init__(self, api_context: ApiContext) -> None:
        self._api_context = api_context

    def post(self,
             uri_relative: str,
             request_bytes: bytes,
             custom_headers: Dict[str, str]) -> BunqResponseRaw:
        return self._request(
            self.METHOD_POST,
            uri_relative,
            request_bytes,
            {},
            custom_headers
        )

    def _request(self,
                 method: str,
                 uri_relative: str,
                 request_bytes: bytes,
                 params: Dict[str, str],
                 custom_headers: Dict[str, str]) -> BunqResponseRaw:
        from bunq.sdk.context.bunq_context import BunqContext

        uri_relative_with_params = self._append_params_to_uri(uri_relative, params)
        if uri_relative not in self._URIS_NOT_REQUIRING_ACTIVE_SESSION:
            if self._api_context.ensure_session_active():
                BunqContext.update_api_context(self._api_context)

        all_headers = self._get_all_headers(
            request_bytes,
            custom_headers
        )

        response = requests.request(
            method,
            self._get_uri_full(uri_relative_with_params),
            data=request_bytes,
            headers=all_headers,
            proxies={self.FIELD_PROXY_HTTPS: self._api_context.proxy_url},
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

    @classmethod
    def _append_params_to_uri(cls,
                              uri: str,
                              params: Dict[str, str]) -> str:
        if params:
            return uri + cls.DELIMITER_URL_QUERY + urlencode(params)

        return uri

    def _get_all_headers(self,
                         request_bytes: bytes,
                         custom_headers: Dict[str, str]) -> Dict[str, str]:
        headers = self._get_default_headers()
        headers.update(custom_headers)

        if self._api_context.token is not None:
            headers[self.HEADER_AUTHENTICATION] = self._api_context.token
            headers[self.HEADER_SIGNATURE] = security.sign_request(
                self._api_context.installation_context.private_key_client,
                request_bytes
            )

        return headers

    @classmethod
    def _get_default_headers(cls) -> Dict[str, str]:
        return {
            cls.HEADER_USER_AGENT: cls.USER_AGENT_BUNQ,
            cls.HEADER_REQUEST_ID: cls._generate_random_request_id(),
            cls.HEADER_GEOLOCATION: cls.GEOLOCATION_ZERO,
            cls.HEADER_LANGUAGE: cls.LANGUAGE_EN_US,
            cls.HEADER_REGION: cls.REGION_NL_NL,
            cls.HEADER_CACHE_CONTROL: cls.CACHE_CONTROL_NONE,
        }

    @staticmethod
    def _generate_random_request_id() -> str:
        return str(uuid.uuid4())

    def _get_uri_full(self, uri_relative: str) -> str:
        return self._api_context.environment_type.uri_base + uri_relative

    def _assert_response_success(self, response: Response) -> None:
        """

        :raise ApiException: When the response is not successful.
        """

        if response.status_code != self.STATUS_CODE_OK:
            raise ExceptionFactory.create_exception_for_response(
                response.status_code,
                self._fetch_all_error_message(response),
                self._fetch_response_id(response)
            )

    @classmethod
    def _create_bunq_response_raw(cls, response: Response) -> BunqResponseRaw:
        return BunqResponseRaw(response.content, response.headers)

    def _fetch_all_error_message(self, response: Response) -> List[str]:
        response_content_string = response.content.decode()

        try:
            error_dict = converter.json_to_class(dict, response_content_string)

            return self._fetch_error_descriptions(error_dict)
        except ValueError:
            return [response_content_string]

    def _fetch_error_descriptions(self, error_dict: Dict[str, List[Dict[str, str]]]) -> List[str]:
        error_descriptions = []

        for error in error_dict[self.FIELD_ERROR]:
            description = error[self.FIELD_ERROR_DESCRIPTION]
            error_descriptions.append(description)

        return error_descriptions

    def _fetch_response_id(self, response: Response) -> str:
        headers = response.headers

        if self.HEADER_RESPONSE_ID_UPPER_CASED in headers:
            return headers[self.HEADER_RESPONSE_ID_UPPER_CASED]

        if self.HEADER_RESPONSE_ID_LOWER_CASED in headers:
            return headers[self.HEADER_RESPONSE_ID_LOWER_CASED]

        return self._ERROR_COULD_NOT_DETERMINE_RESPONSE_ID_HEADER

    def put(self,
            uri_relative: str,
            request_bytes: bytes,
            custom_headers: Dict) -> BunqResponseRaw:
        return self._request(
            self.METHOD_PUT,
            uri_relative,
            request_bytes,
            {},
            custom_headers
        )

    def get(self,
            uri_relative: str,
            params: Dict[str, str],
            custom_headers: Dict[str, str]) -> BunqResponseRaw:
        return self._request(
            self.METHOD_GET,
            uri_relative,
            self.BYTES_EMPTY,
            params,
            custom_headers
        )

    def delete(self,
               uri_relative: str,
               custom_headers: Dict[str, str]) -> BunqResponseRaw:
        return self._request(
            self.METHOD_DELETE,
            uri_relative,
            self.BYTES_EMPTY,
            {},
            custom_headers
        )

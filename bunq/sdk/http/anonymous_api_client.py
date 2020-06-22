from typing import Dict

import requests

from bunq.sdk.context.api_context import ApiContext
from bunq.sdk.http.api_client import ApiClient
from bunq.sdk.http.bunq_response_raw import BunqResponseRaw
from bunq.sdk.security import security


class AnonymousApiClient(ApiClient):

    def __init__(self, api_context: ApiContext) -> None:
        super().__init__(api_context)

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
            uri_relative_with_params,
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

        return BunqResponseRaw(response.content, response.headers)

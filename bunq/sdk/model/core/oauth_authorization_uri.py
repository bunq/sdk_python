from __future__ import annotations

from bunq import ApiEnvironmentType
from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.exception.bunq_exception import BunqException
from bunq.sdk.http.http_util import HttpUtil
from bunq.sdk.model.core.bunq_model import BunqModel
from bunq.sdk.model.core.oauth_response_type import OauthResponseType
from bunq.sdk.model.generated.endpoint import OauthClient


class OauthAuthorizationUri(BunqModel):
    # Auth constants.
    AUTH_URI_FORMAT_SANDBOX = "https://oauth.sandbox.bunq.com/auth?{}"
    AUTH_URI_FORMAT_PRODUCTION = "https://oauth.bunq.com/auth?{}"

    # Field constants
    FIELD_RESPONSE_TYPE = "response_type"
    FIELD_REDIRECT_URI = "redirect_uri"
    FIELD_STATE = "state"
    FIELD_CLIENT_ID = "client_id"

    # Error constants.
    ERROR_ENVIRONMENT_TYPE_NOT_SUPPORTED = "You are trying to use an unsupported environment type."

    def __init__(self, authorization_uri: str) -> None:
        self._authorization_uri = authorization_uri

    @property
    def authorization_uri(self) -> str:
        return self._authorization_uri

    @classmethod
    def create(cls,
               response_type: OauthResponseType,
               redirect_uri: str,
               client: OauthClient,
               state: str = None) -> OauthAuthorizationUri:
        all_request_parameter = {
            cls.FIELD_REDIRECT_URI: redirect_uri,
            cls.FIELD_RESPONSE_TYPE: response_type.name.lower()
        }

        if client.client_id is not None:
            all_request_parameter[cls.FIELD_CLIENT_ID] = client.client_id

        if state is not None:
            all_request_parameter[cls.FIELD_STATE] = state

        return OauthAuthorizationUri(
            cls.determine_auth_uri_format().format(HttpUtil.create_query_string(all_request_parameter))
        )

    def get_authorization_uri(self) -> str:
        return self._authorization_uri

    def is_all_field_none(self) -> bool:
        if self._authorization_uri is None:
            return True
        else:
            return False

    @classmethod
    def determine_auth_uri_format(cls) -> str:
        environment_type = BunqContext.api_context().environment_type

        if ApiEnvironmentType.PRODUCTION == environment_type:
            return cls.AUTH_URI_FORMAT_PRODUCTION

        if ApiEnvironmentType.SANDBOX == environment_type:
            return cls.AUTH_URI_FORMAT_SANDBOX

        raise BunqException(cls.ERROR_ENVIRONMENT_TYPE_NOT_SUPPORTED)

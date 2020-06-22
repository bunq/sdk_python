from __future__ import annotations

from typing import Optional, Type

from bunq import ApiEnvironmentType
from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.exception.bunq_exception import BunqException
from bunq.sdk.http.anonymous_api_client import AnonymousApiClient
from bunq.sdk.http.bunq_response import BunqResponse
from bunq.sdk.http.bunq_response_raw import BunqResponseRaw
from bunq.sdk.http.http_util import HttpUtil
from bunq.sdk.json import converter
from bunq.sdk.model.core.bunq_model import BunqModel
from bunq.sdk.model.core.oauth_grant_type import OauthGrantType
from bunq.sdk.model.generated.endpoint import OauthClient
from bunq.sdk.util.type_alias import T


class OauthAccessToken(BunqModel):
    # Field constants.
    FIELD_GRANT_TYPE = "grant_type"
    FIELD_CODE = "code"
    FIELD_REDIRECT_URI = "redirect_uri"
    FIELD_CLIENT_ID = "client_id"
    FIELD_CLIENT_SECRET = "client_secret"

    # Token constants.
    TOKEN_URI_FORMAT_SANDBOX = "https://api-oauth.sandbox.bunq.com/v1/token?%s"
    TOKEN_URI_FORMAT_PRODUCTION = "https://api.oauth.bunq.com/v1/token?%s"

    # Error constants.
    ERROR_ENVIRONMENT_TYPE_NOT_SUPPORTED = "You are trying to use an unsupported environment type."

    def __init__(self, token: str, token_type: str, state: str = None) -> None:
        self._token = token
        self._token_type = token_type
        self._state = state

    @property
    def token(self) -> str:
        return self._token

    @property
    def token_type(self) -> str:
        return self._token_type

    @property
    def state(self) -> Optional[str]:
        return self._state

    @classmethod
    def create(cls,
               grant_type: OauthGrantType,
               oauth_code: str,
               redirect_uri: str,
               client: OauthClient) -> OauthAccessToken:
        api_client = AnonymousApiClient(BunqContext.api_context())
        response_raw = api_client.post(
            cls.create_token_uri(grant_type.value, oauth_code, redirect_uri, client),
            bytearray(),
            {}
        )

        return cls.from_json(OauthAccessToken, response_raw).value

    @classmethod
    def create_token_uri(cls, grant_type: str, auth_code: str, redirect_uri: str, client: OauthClient) -> str:
        all_token_parameter = {
            cls.FIELD_GRANT_TYPE: grant_type,
            cls.FIELD_CODE: auth_code,
            cls.FIELD_REDIRECT_URI: redirect_uri,
            cls.FIELD_CLIENT_ID: client.id_,
            cls.FIELD_CLIENT_SECRET: client.secret,
        }

        return cls.determine_auth_uri_format().format(HttpUtil.create_query_string(all_token_parameter))

    def is_all_field_none(self) -> bool:
        if self._token is not None:
            return False
        elif self._token_type is not None:
            return False
        elif self._state is not None:
            return False

        return True

    @classmethod
    def from_json(cls, class_of_object: Type[T], response_raw: BunqResponseRaw):
        response_item_object = converter.deserialize(class_of_object, response_raw)
        response_value = converter.json_to_class(class_of_object, response_item_object)

        return BunqResponse(response_value, response_raw.headers)

    @classmethod
    def determine_auth_uri_format(cls) -> str:
        environment_type = BunqContext.api_context().environment_type

        if ApiEnvironmentType.PRODUCTION == environment_type:
            return cls.TOKEN_URI_FORMAT_PRODUCTION

        if ApiEnvironmentType.SANDBOX == environment_type:
            return cls.TOKEN_URI_FORMAT_SANDBOX

        raise BunqException(cls.ERROR_ENVIRONMENT_TYPE_NOT_SUPPORTED)

from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.model.core.oauth_authorization_uri import OauthAuthorizationUri
from bunq.sdk.model.core.oauth_response_type import OauthResponseType
from bunq.sdk.model.generated.endpoint import OauthClient
from tests.bunq_test import BunqSdkTestCase


class TestOauthAuthorizationUri(BunqSdkTestCase):
    _TEST_EXPECT_URI = 'https://oauth.sandbox.bunq.com/auth?redirect_uri=redirecturi&response_type=code&state=state'
    _TEST_REDIRECT_URI = 'redirecturi'
    _TEST_STATUS = 'status'
    _TEST_STATE = 'state'

    @classmethod
    def setUpClass(cls) -> None:
        BunqContext.load_api_context(cls._get_api_context())

    def test_oauth_authorization_uri_create(self) -> None:
        uri = OauthAuthorizationUri.create(
            OauthResponseType(OauthResponseType.CODE),
            self._TEST_REDIRECT_URI,
            OauthClient(self._TEST_STATUS),
            self._TEST_STATE
        ).get_authorization_uri()

        self.assertEqual(self._TEST_EXPECT_URI, uri)

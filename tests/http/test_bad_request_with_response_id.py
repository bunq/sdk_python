from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.exception.api_exception import ApiException
from bunq.sdk.model.generated.endpoint import MonetaryAccountBank
from tests.bunq_test import BunqSdkTestCase


class TestPagination(BunqSdkTestCase):
    """
    Tests if the response id from a failed request can be retrieved
    successfully.
    """

    _INVALID_MONETARY_ACCOUNT_ID = 0

    def test_bad_request_with_response_id(self):
        BunqContext.load_api_context(self._get_api_context())

        with self.assertRaises(ApiException) as caught_exception:
            MonetaryAccountBank.get(self._INVALID_MONETARY_ACCOUNT_ID)
        self.assertIsNotNone(caught_exception.exception.response_id)

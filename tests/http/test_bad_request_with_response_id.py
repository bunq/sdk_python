from bunq.sdk.exception import ApiException
from bunq.sdk.model.generated.endpoint import UserPerson
from tests.bunq_test import BunqSdkTestCase


class TestPagination(BunqSdkTestCase):
    """
    Tests if the response id from a failed request can be retrieved
    successfully.
    """

    _INVALID_USER_PERSON_ID = 0

    def test_bad_request_with_response_id(self):
        """
        """

        with self.assertRaises(ApiException) as caught_exception:
            UserPerson.get(
                self._get_api_context(),
                self._INVALID_USER_PERSON_ID
            )

        self.assertIsNotNone(caught_exception.exception.response_id)

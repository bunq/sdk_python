from bunq.sdk.exception import BadRequestException
from bunq.sdk.model.generated.endpoint import UserPerson
from tests.bunq_test import BunqSdkTestCase


class TestPagination(BunqSdkTestCase):

    _INVALID_USER_PERSON_ID = 0

    def test_bad_request_with_response_id(self):
        caught_exception = None

        try:
            UserPerson.get(
                self._get_api_context(),
                self._INVALID_USER_PERSON_ID
            )
        except BadRequestException as exception:
            caught_exception = exception

        self.assertIsNotNone(caught_exception)
        self.assertIsNotNone(caught_exception.response_id)

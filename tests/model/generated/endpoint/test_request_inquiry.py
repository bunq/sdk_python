from bunq.sdk.model.generated.endpoint import RequestInquiry
from bunq.sdk.model.generated.endpoint import RequestResponse
from bunq.sdk.model.generated.object_ import Amount
from tests.bunq_test import BunqSdkTestCase


class TestRequestEnquiry(BunqSdkTestCase):
    """
    Tests:
        RequestInquiry
        RequestResponse
    """

    _REQUEST_AMOUNT_EUR = '0.01'
    _REQUEST_CURRENCY = 'EUR'
    _DESCRIPTION = 'Python unit test request'
    _STATUS = 'ACCEPTED'

    def test_sending_and_accepting_request(self):
        """
        Tests sending a request from monetary account 1 to monetary account 2
        and accepting this request

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        self.send_request()

        request_response_id = RequestResponse.list(self._second_monetary_account.id_).value[self._FIRST_INDEX].id_

        self.accept_request(request_response_id)

    def send_request(self) -> None:
        RequestInquiry.create(
            Amount(self._REQUEST_AMOUNT_EUR, self._REQUEST_CURRENCY),
            self._get_alias_second_account(),
            self._DESCRIPTION,
            False
        )

    def accept_request(self, response_id: int) -> None:
        RequestResponse.update(response_id, monetary_account_id=self._second_monetary_account.id_, status=self._STATUS)

from bunq.sdk.context import BunqContext
from bunq.sdk.model.generated.endpoint import RequestInquiry
from bunq.sdk.model.generated.endpoint import RequestResponse
from bunq.sdk.model.generated.object_ import Amount
from tests.bunq_test import BunqSdkTestCase
from tests.config import Config


class TestRequestEnquiry(BunqSdkTestCase):
    """
    Tests:
        RequestInquiry
        RequestResponse
    """

    @classmethod
    def setUpClass(cls):
        cls._REQUEST_AMOUNT_EUR = '0.01'
        cls._REQUEST_CURRENCY = 'EUR'
        cls._DESCRIPTION = 'Python unit test request'
        cls._STATUS = 'ACCEPTED'
        cls._FIRST_INDEX = 0
        cls._USER_ID = Config.get_user_id()
        cls._COUNTER_PARTY_SAME_USER = Config.get_pointer_counter_party_self()
        cls._MONETARY_ACCOUNT_ID = Config.get_monetary_account_id_1()
        cls._MONETARY_ACCOUNT_ID2 = Config.get_monetary_account_id_2()
        BunqContext.load_api_context(cls._get_api_context())

    def test_sending_and_accepting_request(self):
        """
        Tests sending a request from monetary account 1 to monetary account 2
        and accepting this request

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        self.send_request()

        request_response_id = RequestResponse.list().value[
            self._FIRST_INDEX].id_

        self.accept_request(request_response_id)

    def send_request(self):
        """
        :rtype: None
        """

        RequestInquiry.create(
            Amount(self._REQUEST_AMOUNT_EUR, self._REQUEST_CURRENCY),
            self._COUNTER_PARTY_SAME_USER,
            self._DESCRIPTION,
            False
        )

    def accept_request(self, response_id):
        """
        :param response_id:
        :rtype response_id: int
        """

        RequestResponse.update(response_id, status=self._STATUS)

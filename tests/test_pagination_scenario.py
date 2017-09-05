from bunq.sdk import client
from tests.bunq_test import BunqSdkTestCase
from tests.bunq_test import Config


class TestPaginationScenario(BunqSdkTestCase):
    """
    Tests:
        Pagination
    """

    @classmethod
    def setUpClass(cls):
        cls._USER_ID = Config.get_user_id()
        cls._MONETARY_ACCOUNT_ID = Config.get_monetary_account_id_1()
        cls._COUNTER_PARTY_ALIAS_OTHER =\
            Config.get_pointer_counter_party_other()
        cls._API_CONTEXT = cls._get_api_context()
        cls._PAYMENT_LISTING_PAGE_SIZE = 2
        cls._PAYMENT_REQUIRED_COUNT_MINIMUM = cls._PAYMENT_LISTING_PAGE_SIZE * 2
        cls._NUMBER_ZERO = 0
        cls._AMOUNT_EUR = '0.01'
        cls._CURRENCY = 'EUR'
        cls._PAYMENT_DESCRIPTION = 'Python test Payment'
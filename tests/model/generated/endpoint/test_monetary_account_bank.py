from secrets import token_hex

from bunq.sdk.context import BunqContext
from bunq.sdk.model.generated.endpoint import MonetaryAccountBank
from tests.bunq_test import BunqSdkTestCase
from tests.config import Config


class TestMonetaryAccount(BunqSdkTestCase):
    """
    Tests:
        MonetaryAccountBank
    """

    @classmethod
    def setUpClass(cls):
        cls._STATUS = 'CANCELLED'
        cls._SUB_STATUS = 'REDEMPTION_VOLUNTARY'
        cls._REASON = 'OTHER'
        cls._REASON_DESCRIPTION = 'Because this is a test'
        cls._CURRENCY = 'EUR'
        cls._MONETARY_ACCOUNT_PREFIX = 'Python_test'
        cls._USER_ID = Config.get_user_id()
        BunqContext.load_api_context(cls._get_api_context())

    def test_create_new_monetary_account(self):
        """
        Tests the creation of a new monetary account. This account will be
        deleted after test exited with code 0.

        This test has no assertion as  of its testing to see if the code runs
        without errors
        """

        monetary_account_id = MonetaryAccountBank.create(self._CURRENCY,
                                                         self._MONETARY_ACCOUNT_PREFIX + token_hex()).value

        MonetaryAccountBank.update(monetary_account_id,
                                   status=self._STATUS,
                                   sub_status=self._SUB_STATUS,
                                   reason=self._REASON,
                                   reason_description=self._REASON_DESCRIPTION
                                   )

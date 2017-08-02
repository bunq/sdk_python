from secrets import token_hex

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
        cls._FIELD_STATUS = 'CANCELLED'
        cls._FIELD_SUB_STATUS = 'REDEMPTION_VOLUNTARY'
        cls._FIELD_REASON = 'OTHER'
        cls._FIELD_REASON_DESCRIPTION = 'Because this is a test'
        cls._FIELD_CURRENCY = 'EUR'
        cls._MONETARY_ACCOUNT_PREFIX = 'Python_test'
        cls._USER_ID = Config.get_user_id()
        cls._API_CONTEXT = cls._get_api_context()

    def test_create_new_monetary_account(self):
        """
        Tests the creation of a new monetary account. This account will be
        deleted after test exited with code 0.

        This test has no assertion as  of its testing to see if the code runs
        without errors
        """

        create_map = {
            MonetaryAccountBank.FIELD_CURRENCY: self._FIELD_CURRENCY,
            MonetaryAccountBank.FIELD_DESCRIPTION:
                self._MONETARY_ACCOUNT_PREFIX + token_hex()
        }
        monetary_account_id = MonetaryAccountBank.create(self._API_CONTEXT,
                                                         create_map,
                                                         self._USER_ID)

        update_map = {
            MonetaryAccountBank.FIELD_STATUS: self._FIELD_STATUS,
            MonetaryAccountBank.FIELD_SUB_STATUS: self._FIELD_SUB_STATUS,
            MonetaryAccountBank.FIELD_REASON: self._FIELD_REASON,
            MonetaryAccountBank.FIELD_REASON_DESCRIPTION:
                self._FIELD_REASON_DESCRIPTION,
        }
        MonetaryAccountBank.update(self._API_CONTEXT, update_map, self._USER_ID,
                                   monetary_account_id)

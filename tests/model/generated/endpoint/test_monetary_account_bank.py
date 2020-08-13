try:
    from secrets import token_hex
except ImportError:
    from os import urandom


    def token_hex():
        """ Function to replace import for Python < 3.6. """
        return urandom(16).hex()

from bunq.sdk.model.generated.endpoint import MonetaryAccountBank
from tests.bunq_test import BunqSdkTestCase


class TestMonetaryAccount(BunqSdkTestCase):
    """
    Tests:
        MonetaryAccountBank
    """

    _STATUS = 'CANCELLED'
    _SUB_STATUS = 'REDEMPTION_VOLUNTARY'
    _REASON = 'OTHER'
    _REASON_DESCRIPTION = 'Because this is a test'
    _CURRENCY = 'EUR'
    _MONETARY_ACCOUNT_PREFIX = 'Python_test'

    def test_create_new_monetary_account(self):
        """
        Tests the creation of a new monetary account. This account will be
        deleted after test exited with code 0.

        This test has no assertion as  of its testing to see if the code runs
        without errors
        """

        monetary_account_id = MonetaryAccountBank.create(
            self._CURRENCY,
            self._MONETARY_ACCOUNT_PREFIX + token_hex()
        ).value

        MonetaryAccountBank.update(monetary_account_id,
                                   status=self._STATUS,
                                   sub_status=self._SUB_STATUS,
                                   reason=self._REASON,
                                   reason_description=self._REASON_DESCRIPTION
                                   )

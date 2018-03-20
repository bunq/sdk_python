from bunq.sdk.context import BunqContext
from bunq.sdk.model.generated.endpoint import TabItemShop
from bunq.sdk.model.generated.endpoint import TabUsageSingle
from bunq.sdk.model.generated.object_ import Amount
from tests.bunq_test import BunqSdkTestCase
from tests.config import Config


class TestTabUsageSingle(BunqSdkTestCase):
    """
    Tests:
        TabUsageSingle
        TabItemShop
    """

    @classmethod
    def setUpClass(cls):
        cls._USER_ID = Config.get_user_id()
        cls._MONETARY_ACCOUNT_ID = Config.get_monetary_account_id_1()
        cls._CASH_REGISTER_ID = Config.get_cash_register_id()
        cls._AMOUNT_EUR = '0.02'
        cls._CURRENCY = 'EUR'
        cls._STATUS_OPEN = 'OPEN'
        cls._TAB_ITEM_DESCRIPTION = 'Super expensive python tea'
        cls._STATUS_WAITING = 'WAITING_FOR_PAYMENT'
        cls._TAB_DESCRIPTION = 'Pay the tab for Python test please.'
        BunqContext.load_api_context(cls._get_api_context())

    def test_create_and_update_tab(self):
        """
        Tests the creation of a Tab, adds a tab item to it and updates this tab

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        tab_uuid = TabUsageSingle.create(self._CASH_REGISTER_ID,
                                         self._TAB_DESCRIPTION,
                                         self._STATUS_OPEN,
                                         Amount(self._AMOUNT_EUR,
                                                self._CURRENCY)).value

        self._add_item_to_tab(tab_uuid)
        self._update_tab(tab_uuid)

    def _add_item_to_tab(self, tab_uuid):
        """
        :param tab_uuid:
        :type tab_uuid: str
        """

        TabItemShop.create(
            self._CASH_REGISTER_ID, tab_uuid,
            self._TAB_ITEM_DESCRIPTION
        )

    def _update_tab(self, tab_uuid):
        """
        :param tab_uuid:
        :type tab_uuid: str
        """

        TabUsageSingle.update(
            self._CASH_REGISTER_ID,
            tab_uuid
        )

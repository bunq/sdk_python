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
        cls._TAB_ITEM_FIELD_DESCRIPTION = 'Super expensive python tea'
        cls._STATUS_WAITING = 'WAITING_FOR_PAYMENT'
        cls._TAB_FIELD_DESCRIPTION = 'Pay the tab for Python test please.'
        cls._API_CONTEXT = cls._get_api_context()

    def test_create_and_update_tab(self):
        """
        Tests the creation of a Tab, adds a tab item to it and updates this tab

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        create_map = {
            TabUsageSingle.FIELD_STATUS: self._STATUS_OPEN,
            TabUsageSingle.FIELD_DESCRIPTION: self._TAB_FIELD_DESCRIPTION,
            TabUsageSingle.FIELD_AMOUNT_TOTAL: Amount(self._AMOUNT_EUR,
                                                      self._CURRENCY)
        }
        tab_uuid = TabUsageSingle.create(self._API_CONTEXT, create_map,
                                         self._USER_ID,
                                         self._MONETARY_ACCOUNT_ID,
                                         self._CASH_REGISTER_ID).value

        self._add_item_to_tab(tab_uuid)
        self._update_tab(tab_uuid)

    def _add_item_to_tab(self, tab_uuid):
        """
        :param tab_uuid:
        :type tab_uuid: str
        """

        tab_item_map = {
            TabItemShop.FIELD_AMOUNT: Amount(self._AMOUNT_EUR,
                                             self._CURRENCY),
            TabItemShop.FIELD_DESCRIPTION: self._TAB_ITEM_FIELD_DESCRIPTION,
        }
        TabItemShop.create(self._API_CONTEXT, tab_item_map, self._USER_ID,
                           self._MONETARY_ACCOUNT_ID,
                           self._CASH_REGISTER_ID,
                           tab_uuid)

    def _update_tab(self, tab_uuid):
        """
        :param tab_uuid:
        :type tab_uuid: str
        """

        update_map = {
            TabUsageSingle.FIELD_STATUS: self._STATUS_WAITING,
        }
        TabUsageSingle.update(self._API_CONTEXT, update_map, self._USER_ID,
                              self._MONETARY_ACCOUNT_ID, self._CASH_REGISTER_ID,
                              tab_uuid)

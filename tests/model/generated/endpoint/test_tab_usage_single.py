import unittest

from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.model.generated.endpoint import TabItemShop
from bunq.sdk.model.generated.endpoint import TabUsageSingle
from bunq.sdk.model.generated.object_ import Amount
from tests.bunq_test import BunqSdkTestCase


class TestTabUsageSingle(BunqSdkTestCase):
    """
    Tests:
        TabUsageSingle
        TabItemShop
    """

    _AMOUNT_EUR = '0.02'
    _CURRENCY = 'EUR'
    _STATUS_OPEN = 'OPEN'
    _STATUS_WAITING = 'WAITING_FOR_PAYMENT'
    _TAB_ITEM_DESCRIPTION = 'Super expensive python tea'
    _TAB_DESCRIPTION = 'Pay the tab for Python test please.'
    _ERROR_ONLY_USER_COMPANY_CAN_CREATE_TAB =\
        'Only user company can create/use cash registers.'

    def test_create_and_update_tab(self):
        """
        Tests the creation of a Tab, adds a tab item to it and updates this tab

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        if BunqContext.user_context().is_only_user_person_set():
            return unittest.skip(
                self._ERROR_ONLY_USER_COMPANY_CAN_CREATE_TAB
            )

        tab_uuid = TabUsageSingle.create(self._get_cash_register_id(),
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
            self._get_cash_register_id(), tab_uuid,
            self._TAB_ITEM_DESCRIPTION
        )

    def _update_tab(self, tab_uuid):
        """
        :param tab_uuid:
        :type tab_uuid: str
        """

        TabUsageSingle.update(
            self._get_cash_register_id(),
            tab_uuid
        )

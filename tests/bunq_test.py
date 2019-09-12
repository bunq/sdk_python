import os
import time
import unittest

from bunq.sdk.context import api_context
from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.util import util
from bunq.sdk.http.api_client import ApiClient
from bunq.sdk.exception.exception import BunqException
from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated import object_


class BunqSdkTestCase(unittest.TestCase):
    """
    :type _second_monetary_account: endpoint.MonetaryAccountBank
    :type _cash_register: endpoint.CashRegister
    """

    # Error constants.
    __ERROR_COULD_NOT_DETERMINE_USER = 'Could not determine user alias.'

    # Name of bunq config file
    _FILENAME_BUNQ_CONFIG = "/bunq-test.conf"

    # Device description used for python tests
    _DEVICE_DESCRIPTION = 'Python test device'

    _PATH_ATTACHMENT = 'tests/assets/'
    _READ_BYTES = "rb"
    _ATTACHMENT_PATH_IN = 'bunq_App_Icon_Square@4x.png'
    _CONTENT_TYPE = 'image/png'
    _ATTACHMENT_DESCRIPTION = 'SDK python test'
    _FIRST_INDEX = 0

    __SPENDING_MONEY_AMOUNT = '500'
    __CURRENCY_EUR = 'EUR'
    _POINTER_EMAIL = 'EMAIL'
    __SPENDING_MONEY_RECIPIENT = 'sugardaddy@bunq.com'
    __REQUEST_SPENDING_DESCRIPTION = 'sdk  python test, thanks daddy <3'

    __CASH_REGISTER_STATUS = 'PENDING_APPROVAL'
    __CASH_REGISTER_DESCRIPTION = 'python test cash register'

    __SECOND_MONETARY_ACCOUNT_DESCRIPTION = 'test account python'

    _EMAIL_BRAVO = 'bravo@bunq.com'

    __TIME_OUT_AUTO_ACCEPT_SPENDING_MONEY = 0.5

    _second_monetary_account = None
    _cash_register = None

    @classmethod
    def setUpClass(cls):
        BunqContext.load_api_context(cls._get_api_context())

    def setUp(self):
        self.__set_second_monetary_account()
        self.__request_spending_money()
        time.sleep(self.__TIME_OUT_AUTO_ACCEPT_SPENDING_MONEY)
        BunqContext.user_context().refresh_user_context()

    def __set_second_monetary_account(self):
        response = endpoint.MonetaryAccountBank.create(
            self.__CURRENCY_EUR,
            self.__SECOND_MONETARY_ACCOUNT_DESCRIPTION
        )

        self._second_monetary_account = endpoint.MonetaryAccountBank.get(
            response.value
        ).value

    def __request_spending_money(self):
        endpoint.RequestInquiry.create(
            object_.Amount(self.__SPENDING_MONEY_AMOUNT, self.__CURRENCY_EUR),
            object_.Pointer(
                self._POINTER_EMAIL,
                self.__SPENDING_MONEY_RECIPIENT
            ),
            self.__REQUEST_SPENDING_DESCRIPTION,
            False
        )
        endpoint.RequestInquiry.create(
            object_.Amount(self.__SPENDING_MONEY_AMOUNT, self.__CURRENCY_EUR),
            object_.Pointer(
                self._POINTER_EMAIL,
                self.__SPENDING_MONEY_RECIPIENT
            ),
            self.__REQUEST_SPENDING_DESCRIPTION,
            False,
            self._second_monetary_account.id_
        )

    def _get_cash_register_id(self):
        if self._cash_register is None:
            self._set_cash_register()

        return self._cash_register.id_

    @classmethod
    def _get_api_context(cls):
        """
        :rtype: api_context.ApiContext
        """

        return util.automatic_sandbox_install()

    def _get_pointer_bravo(self):
        """
        :rtype: object_.Pointer
        """

        return object_.Pointer(self._POINTER_EMAIL, self._EMAIL_BRAVO)

    def _get_alias_second_account(self):
        """
        :rtype: object_.Pointer
        """

        return self._second_monetary_account.alias[self._FIRST_INDEX]

    @staticmethod
    def _get_directory_test_root():
        return os.path.dirname(os.path.abspath(__file__))

    def _set_cash_register(self):
        attachment_uuid = endpoint.AttachmentPublic.create(
            self._attachment_contents,
            {
                ApiClient.HEADER_CONTENT_TYPE: self._CONTENT_TYPE,
                ApiClient.HEADER_ATTACHMENT_DESCRIPTION:
                    self._ATTACHMENT_DESCRIPTION,
            }
        )
        avatar_uuid = endpoint.Avatar.create(attachment_uuid.value)
        cash_register_id = endpoint.CashRegister.create(
            self.__CASH_REGISTER_DESCRIPTION,
            self.__CASH_REGISTER_STATUS,
            avatar_uuid.value
        )

        self._cash_register = endpoint.CashRegister.get(cash_register_id.value)

    @property
    def _attachment_contents(self):
        """
        :rtype: bytes
        """

        with open(
                self._get_directory_test_root() +
                self._PATH_ATTACHMENT +
                self._ATTACHMENT_PATH_IN,
                self._READ_BYTES
        ) as file:
            return file.read()

    @property
    def alias_first(self):
        """
        :rtype: Pointer
        """

        if BunqContext.user_context().is_only_user_company_set():
            return BunqContext.user_context().user_company.alias[
                self._FIRST_INDEX]

        if BunqContext.user_context().is_only_user_person_set():
            return BunqContext.user_context().user_person.alias[
                self._FIRST_INDEX]

        raise BunqException(self.__ERROR_COULD_NOT_DETERMINE_USER)

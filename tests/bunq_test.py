import os
import time
import unittest

from bunq.sdk import context, util
from bunq.sdk.client import ApiClient
from bunq.sdk.context import BunqContext
from bunq.sdk.exception import BunqException
from bunq.sdk.model.generated import endpoint, object_
from tests import config


class BunqSdkTestCase(unittest.TestCase):
    """
    :type _second_monetary_account: endpoint.MonetaryAccountBank
    :type _cash_register: endpoint.CashRegister

    """

    # Config values
    _API_KEY = config.Config.get_api_key()

    # Name of bunq config file
    _FILENAME_BUNQ_CONFIG = "/bunq-test.conf"

    # Device description used for python tests
    _DEVICE_DESCRIPTION = 'Python test device'

    _PATH_ATTACHMENT = '/assets/'
    _READ_BYTES = "rb"
    _ATTACHMENT_PATH_IN = 'bunq_App_Icon_Square@4x.png'
    _CONTENT_TYPE = 'image/png'
    _ATTACHMENT_DESCRIPTION = 'SDK python test'
    _FIRST_INDEX = 0

    _second_monetary_account = None
    _cash_register = None

    @classmethod
    def setUpClass(cls):
        BunqContext.load_api_context(cls._get_api_context())

    def setUp(self):
        self.__set_second_monetary_account()
        self.__request_spending_money()
        time.sleep(0.5)
        BunqContext.user_context().refresh_user_context()

    def __set_second_monetary_account(self):
        response = endpoint.MonetaryAccountBank.create(
            'EUR',
            'test account python'
        )

        self._second_monetary_account = endpoint.MonetaryAccountBank.get(
            response.value
        ).value

    def __request_spending_money(self):
        endpoint.RequestInquiry.create(
            object_.Amount('500', 'EUR'),
            object_.Pointer('EMAIL', 'sugardaddy@bunq.com'),
            'sdk  python test, thanks daddy <3 - OG',
            False
        )
        endpoint.RequestInquiry.create(
            object_.Amount('500', 'EUR'),
            object_.Pointer('EMAIL', 'sugardaddy@bunq.com'),
            'sdk  python test, thanks daddy <3 - OG',
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
        :rtype: context.ApiContext
        """

        util.automatic_sandbox_install('bunq-test.conf')

        return context.ApiContext.restore('bunq-test.conf')

    @staticmethod
    def _get_pointer_bravo():
        """
        :rtype: object_.Pointer
        """

        return object_.Pointer('EMAIL', 'bravo@bunq.com')

    def _get_alias_second_account(self):
        """
        :rtype: object_.Pointer
        """

        return self._second_monetary_account.alias[0]

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
            'python test cash register',
            'PENDING_APPROVAL',
            avatar_uuid.value
        )

        self._cash_register = endpoint.CashRegister.get(cash_register_id.value)

    @property
    def _attachment_contents(self):
        """
        :rtype: bytes
        """

        with open(self._get_directory_test_root() + self._PATH_ATTACHMENT + self._ATTACHMENT_PATH_IN,
                  self._READ_BYTES) as f:
            return f.read()

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

        raise BunqException('Could not determine user alias.')

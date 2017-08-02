from bunq.sdk.model.generated.endpoint import Payment
from bunq.sdk.model.generated.endpoint import PaymentChat
from bunq.sdk.model.generated.endpoint import ChatMessageText
from bunq.sdk.model.generated.object_ import Amount
from tests.bunq_test import BunqSdkTestCase
from tests.config import Config


class TestPayment(BunqSdkTestCase):
    """
    Tests:
        Payment
        PaymentChat
        ChatMessageText
    """

    @classmethod
    def setUpClass(cls):
        cls._PAYMENT_AMOUNT_IN_EUR = '0.01'
        cls._PAYMENT_CURRENCY = 'EUR'
        cls._FIELD_DESCRIPTION = 'Python unit test'
        cls._PAYMENT_CHAT_TEXT_MESSAGE = 'send from python test'
        cls._USER_ID = Config.get_user_id()
        cls._COUNTER_PARTY_OTHER_USER = Config.get_pointer_counter_party_other()
        cls._COUNTER_PARTY_SAME_USER = Config.get_pointer_counter_party_self()
        cls._MONETARY_ACCOUNT_ID = Config.get_monetary_account_id_1()
        cls._API_CONTEXT = cls.get_api_context()

    def test_payment_to_other_user(self):
        """
        Tests making a payment to another sandbox user

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        request_map = {
            Payment.FIELD_COUNTERPARTY_ALIAS: self._COUNTER_PARTY_OTHER_USER,
            Payment.FIELD_AMOUNT: Amount(self._PAYMENT_AMOUNT_IN_EUR,
                                         self._PAYMENT_CURRENCY),
            Payment.FIELD_DESCRIPTION: self._FIELD_DESCRIPTION,
        }
        Payment.create(self._API_CONTEXT, request_map, self._USER_ID,
                       self._MONETARY_ACCOUNT_ID)

    def test_payment_to_other_account(self):
        """
        Tests making a payment to another monetary account of the same user

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        request_map = {
            Payment.FIELD_COUNTERPARTY_ALIAS: self._COUNTER_PARTY_SAME_USER,
            Payment.FIELD_DESCRIPTION: self._FIELD_DESCRIPTION,
            Payment.FIELD_AMOUNT: Amount(self._PAYMENT_AMOUNT_IN_EUR,
                                         self._PAYMENT_CURRENCY),
        }
        Payment.create(self._API_CONTEXT, request_map, self._USER_ID,
                       self._MONETARY_ACCOUNT_ID)

    def test_payment_chat(self):
        """
        Tests sending a chat message in a newly created payment

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        request_map = {
            Payment.FIELD_COUNTERPARTY_ALIAS: self._COUNTER_PARTY_OTHER_USER,
            Payment.FIELD_AMOUNT: Amount(self._PAYMENT_AMOUNT_IN_EUR,
                                         self._PAYMENT_CURRENCY),
            Payment.FIELD_DESCRIPTION: self._FIELD_DESCRIPTION,
        }
        payment_id = Payment.create(self._API_CONTEXT, request_map,
                                    self._USER_ID, self._MONETARY_ACCOUNT_ID)

        chat_map = {}
        chat_id = PaymentChat.create(self._API_CONTEXT, chat_map, self._USER_ID,
                                     self._MONETARY_ACCOUNT_ID, payment_id)

        message_map = {
            ChatMessageText.FIELD_TEXT: self._PAYMENT_CHAT_TEXT_MESSAGE,
        }
        ChatMessageText.create(self._API_CONTEXT, message_map, self._USER_ID,
                               chat_id)

from bunq.sdk.context import BunqContext
from bunq.sdk.model.generated.endpoint import ChatMessageText
from bunq.sdk.model.generated.endpoint import Payment
from bunq.sdk.model.generated.endpoint import PaymentChat
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
        cls._PAYMENT_AMOUNT_EUR = '0.01'
        cls._PAYMENT_CURRENCY = 'EUR'
        cls._PAYMENT_DESCRIPTION = 'Python unit test'
        cls._PAYMENT_CHAT_TEXT_MESSAGE = 'send from python test'
        cls._USER_ID = Config.get_user_id()
        cls._COUNTER_PARTY_OTHER_USER = Config.get_pointer_counter_party_other()
        cls._COUNTER_PARTY_SAME_USER = Config.get_pointer_counter_party_self()
        cls._MONETARY_ACCOUNT_ID = Config.get_monetary_account_id_1()

        BunqContext.load_api_context(cls._get_api_context())

    def test_payment_to_other_user(self):
        """
        Tests making a payment to another sandbox user

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        Payment.create(
            Amount(self._PAYMENT_AMOUNT_EUR, self._PAYMENT_CURRENCY),
            self._COUNTER_PARTY_OTHER_USER,
            self._PAYMENT_DESCRIPTION
        )

    def test_payment_to_other_account(self):
        """
        Tests making a payment to another monetary account of the same user

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        Payment.create(
            Amount(self._PAYMENT_AMOUNT_EUR, self._PAYMENT_CURRENCY),
            self._COUNTER_PARTY_SAME_USER,
            self._PAYMENT_DESCRIPTION
        )

    def test_payment_chat(self):
        """
        Tests sending a chat message in a newly created payment

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        payment_id = Payment.create(
            Amount(self._PAYMENT_AMOUNT_EUR, self._PAYMENT_CURRENCY),
            self._COUNTER_PARTY_OTHER_USER,
            self._PAYMENT_DESCRIPTION
        ).value

        chat_id = PaymentChat.create(payment_id).value

        ChatMessageText.create(chat_id, self._PAYMENT_CHAT_TEXT_MESSAGE)

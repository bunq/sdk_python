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

    _PAYMENT_AMOUNT_EUR = '0.01'
    _PAYMENT_CURRENCY = 'EUR'
    _PAYMENT_DESCRIPTION = 'Python unit test'
    _PAYMENT_CHAT_TEXT_MESSAGE = 'send from python test'
    _USER_ID = Config.get_user_id()

    def test_payment_to_other_user(self):
        """
        Tests making a payment to another sandbox user

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        Payment.create(
            Amount(self._PAYMENT_AMOUNT_EUR, self._PAYMENT_CURRENCY),
            self._get_pointer_bravo(),
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
            self._get_alias_second_account(),
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
            self._get_pointer_bravo(),
            self._PAYMENT_DESCRIPTION
        ).value

        chat_id = PaymentChat.create(payment_id).value

        ChatMessageText.create(chat_id, self._PAYMENT_CHAT_TEXT_MESSAGE)

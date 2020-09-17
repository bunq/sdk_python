from typing import List

from bunq.sdk.model.generated.endpoint import Payment, PaymentBatch, BunqResponseInt, BunqResponsePaymentBatch
from bunq.sdk.model.generated.object_ import Amount, Pointer
from tests.bunq_test import BunqSdkTestCase


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

    _MAXIMUM_PAYMENT_IN_BATCH = 10

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

    def test_payment_batch(self):
        response_create = PaymentBatch.create(self.__create_payment_list())

        self.assertIsInstance(response_create, BunqResponseInt)
        self.assertIsNotNone(response_create)

        response_get = PaymentBatch.get(response_create.value)

        self.assertIsInstance(response_get, BunqResponsePaymentBatch)
        self.assertIsNotNone(response_get)
        self.assertFalse(response_get.value.is_all_field_none())

    def __create_payment_list(self) -> List[Payment]:
        all_payment = []

        while len(all_payment) < self._MAXIMUM_PAYMENT_IN_BATCH:
            all_payment.append(
                Payment(
                    Amount(self._PAYMENT_AMOUNT_EUR, self._PAYMENT_CURRENCY),
                    Pointer(self._POINTER_EMAIL, self._EMAIL_BRAVO),
                    self._PAYMENT_DESCRIPTION
                )
            )
        self.assertIsInstance(all_payment, List)
        self.assertIsInstance(all_payment[0], Payment)

        return all_payment

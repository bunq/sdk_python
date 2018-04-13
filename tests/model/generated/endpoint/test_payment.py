from typing import List

from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated import object_
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

        endpoint.Payment.create(
            object_.Amount(self._PAYMENT_AMOUNT_EUR, self._PAYMENT_CURRENCY),
            self._get_pointer_bravo(),
            self._PAYMENT_DESCRIPTION
        )

    def test_payment_to_other_account(self):
        """
        Tests making a payment to another monetary account of the same user

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        endpoint.Payment.create(
            object_.Amount(self._PAYMENT_AMOUNT_EUR, self._PAYMENT_CURRENCY),
            self._get_alias_second_account(),
            self._PAYMENT_DESCRIPTION
        )

    def test_payment_chat(self):
        """
        Tests sending a chat message in a newly created payment

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        payment_id = endpoint.Payment.create(
            object_.Amount(self._PAYMENT_AMOUNT_EUR, self._PAYMENT_CURRENCY),
            self._get_pointer_bravo(),
            self._PAYMENT_DESCRIPTION
        ).value

        chat_id = endpoint.PaymentChat.create(payment_id).value

        endpoint.ChatMessageText.create(chat_id, self._PAYMENT_CHAT_TEXT_MESSAGE)

    def test_payment_batch(self):
        response_create: endpoint.BunqResponseInt =\
            endpoint.PaymentBatch.create(
                self.__create_payment_list()
            )

        self.assertIsNotNone(response_create)

        response_get: endpoint.BunqResponsePaymentBatch =\
            endpoint.PaymentBatch.get(response_create.value)

        self.assertIsNotNone(response_get)
        self.assertFalse(response_get.value.is_all_field_none())

    def __create_payment_list(self) -> List[endpoint.Payment]:
        """
        :rtype: List[Payment]
        """

        all_payment: List[endpoint.Payment] = []

        while len(all_payment) < self._MAXIMUM_PAYMENT_IN_BATCH:
            all_payment.append(
                endpoint.Payment(
                    object_.Amount(
                        self._PAYMENT_AMOUNT_EUR,
                        self._PAYMENT_CURRENCY
                    ),
                    object_.Pointer(self._POINTER_EMAIL, self._EMAIL_BRAVO),
                    self._PAYMENT_DESCRIPTION
                )
            )

        return all_payment

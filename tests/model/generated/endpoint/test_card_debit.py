import random
import string

from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.model.generated.endpoint import Card
from bunq.sdk.model.generated.endpoint import CardDebit
from bunq.sdk.model.generated.endpoint import CardName
from bunq.sdk.model.generated.object_ import CardPinAssignment
from tests.bunq_test import BunqSdkTestCase


class TestCardDebit(BunqSdkTestCase):
    """
    Tests:
        Card
        CardDebit
        CardName
    """

    _CARD_PIN_CODE = '4045'
    _SECOND_LINE_LENGTH_MAXIMUM = 20
    _STRING_EMPTY = ''
    _PIN_CODE_ASSIGNMENT_TYPE_PRIMARY = 'PRIMARY'
    _CARD_TYPE_MAESTRO = 'MAESTRO'
    _PRODUCT_TYPE_MAESTRO_DEBIT = 'MAESTRO_DEBIT'

    def test_order_debit_card(self):
        """
        Tests ordering a new card and checks if the fields we have entered
        are indeed correct by retrieving the card from the card endpoint and
        checks this date against the data we have submitted
        """

        second_line = self.second_line_random
        pin_code_assignment = CardPinAssignment(
            self._PIN_CODE_ASSIGNMENT_TYPE_PRIMARY,
            self._CARD_PIN_CODE,
            BunqContext.user_context().primary_monetary_account.id_
        )
        card_debit = CardDebit.create(second_line,
                                      self.card_name_allowed,
                                      self._CARD_TYPE_MAESTRO,
                                      self.alias_first,
                                      self._PRODUCT_TYPE_MAESTRO_DEBIT,
                                      [pin_code_assignment]
                                      ).value
        card = Card.get(card_debit.id_).value

        self.assertEqual(self.card_name_allowed, card.name_on_card)
        self.assertEqual(second_line, card.second_line)
        self.assertEqual(card_debit.created, card.created)

    @property
    def card_name_allowed(self) -> str:
        return CardName.list().value[self._FIRST_INDEX].possible_card_name_array[self._FIRST_INDEX]

    @property
    def second_line_random(self) -> str:
        second_line_characters = []

        for _ in range(self._SECOND_LINE_LENGTH_MAXIMUM):
            next_char = random.choice(string.ascii_uppercase)
            second_line_characters.append(next_char)

        return self._STRING_EMPTY.join(second_line_characters)

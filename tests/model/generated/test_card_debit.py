import random
import string

from bunq.sdk.model.generated.endpoint import User
from bunq.sdk.model.generated.endpoint import CardName
from bunq.sdk.model.generated.endpoint import Card
from bunq.sdk.model.generated.endpoint import CardDebit
from bunq.sdk.model.generated.object_ import Pointer
from tests.bunq_test import BunqSdkTestCase
from tests.config import Config


class TestCardDebit(BunqSdkTestCase):
    """
    Tests:
        Card
        CardDebit
        CardName
    """

    @classmethod
    def setUpClass(cls):
        cls._CARD_PIN_CODE = '4045'
        cls._FIRST_INDEX = 0
        cls._SECOND_LINE_LENGTH_MAXIMUM = 20
        cls._STRING_EMPTY = ''
        cls._USER_ID = Config.get_user_id()
        cls._API_CONTEXT = cls._get_api_context()

    def test_order_debit_card(self):
        """
        Tests ordering a new card and checks if the fields we have entered
        are indeed correct by retrieving the card from the card endpoint and
        checks this date against the data we have submitted
        """

        second_line = self.second_line_random

        card_debit_map = {
            CardDebit.FIELD_NAME_ON_CARD: self.card_name_allowed,
            CardDebit.FIELD_ALIAS: self.alias_first,
            CardDebit.FIELD_PIN_CODE: self._CARD_PIN_CODE,
            CardDebit.FIELD_SECOND_LINE: second_line
        }
        card_debit = CardDebit.create(self._API_CONTEXT, card_debit_map,
                                      self._USER_ID).value
        card = Card.get(self._API_CONTEXT, self._USER_ID, card_debit.id_).value

        self.assertEqual(self.card_name_allowed, card.name_on_card)
        self.assertEqual(second_line, card.second_line)
        self.assertEqual(card_debit.created, card.created)

    @property
    def alias_first(self):
        """
        :rtype: Pointer
        """

        return User.list(self._API_CONTEXT).value[self._FIRST_INDEX] \
            .UserCompany.alias[self._FIRST_INDEX]

    @property
    def card_name_allowed(self):
        """
        :rtype: str
        """

        return CardName.list(self._API_CONTEXT, self._USER_ID).value[
            self._FIRST_INDEX].possible_card_name_array[self._FIRST_INDEX]

    @property
    def second_line_random(self):
        """
        :rtype: str
        """

        second_line_characters = []

        for _ in range(self._SECOND_LINE_LENGTH_MAXIMUM):
            next_char = random.choice(string.ascii_uppercase)
            second_line_characters.append(next_char)

        return self._STRING_EMPTY.join(second_line_characters)

import random
import string

from bunq.sdk.context import BunqContext
from bunq.sdk.exception import BunqException
from bunq.sdk.model.generated.endpoint import Card
from bunq.sdk.model.generated.endpoint import CardDebit
from bunq.sdk.model.generated.endpoint import CardName
from bunq.sdk.model.generated.object_ import CardPinAssignment
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
        cls._MONETARY_ACCOUNT_ID = Config.get_monetary_account_id_1()
        cls._PIN_CODE_ASSIGNMENT_TYPE_PRIMARY = 'PRIMARY'

        BunqContext.load_api_context(cls._get_api_context())

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
            self._MONETARY_ACCOUNT_ID
        )

        card_debit = CardDebit.create(second_line, self.card_name_allowed,
                                      self.alias_first, 'MAESTRO',
                                      [pin_code_assignment]).value
        card = Card.get(card_debit.id_).value

        self.assertEqual(self.card_name_allowed, card.name_on_card)
        self.assertEqual(second_line, card.second_line)
        self.assertEqual(card_debit.created, card.created)

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

    @property
    def card_name_allowed(self):
        """
        :rtype: str
        """

        return \
            CardName.list().value[self._FIRST_INDEX].possible_card_name_array[
                self._FIRST_INDEX]

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

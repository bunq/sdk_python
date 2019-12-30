from bunq import Pagination
from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.json import converter
from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated import object_
from tests.bunq_test import BunqSdkTestCase


class TestPaginationScenario(BunqSdkTestCase):
    """
    Tests:
        Pagination
    """

    @classmethod
    def setUpClass(cls):
        cls._PAYMENT_LISTING_PAGE_SIZE = 2
        cls._PAYMENT_REQUIRED_COUNT_MINIMUM = cls._PAYMENT_LISTING_PAGE_SIZE * 2
        cls._NUMBER_ZERO = 0
        cls._PAYMENT_AMOUNT_EUR = '0.01'
        cls._PAYMENT_CURRENCY = 'EUR'
        cls._PAYMENT_DESCRIPTION = 'Python test Payment'

        BunqContext.load_api_context(cls._get_api_context())

    def test_api_scenario_payment_listing_with_pagination(self):
        self._ensure_enough_payments()
        payments_expected = self._payments_required()
        pagination = Pagination()
        pagination.count = self._PAYMENT_LISTING_PAGE_SIZE

        response_latest = self._list_payments(pagination.url_params_count_only)
        pagination_latest = response_latest.pagination
        response_previous = self._list_payments(
            pagination_latest.url_params_previous_page
        )
        pagination_previous = response_previous.pagination
        response_previous_next = self._list_payments(
            pagination_previous.url_params_next_page
        )
        payments_previous = response_previous.value
        payments_previous_next = response_previous_next.value
        payments_actual = payments_previous_next + payments_previous
        payments_expected_serialized = converter.serialize(payments_expected)
        payments_actual_serialized = converter.serialize(payments_actual)

        self.assertEqual(payments_expected_serialized,
                         payments_actual_serialized)

    def _ensure_enough_payments(self):
        """
        :rtype: None
        """

        for _ in range(self._payment_missing_count):
            self._create_payment()

    @property
    def _payment_missing_count(self):
        """
        :rtype: int
        """

        return self._PAYMENT_REQUIRED_COUNT_MINIMUM - \
               len(self._payments_required())

    def _payments_required(self):
        """
        :rtype: list[endpoint.Payment]
        """

        pagination = Pagination()
        pagination.count = self._PAYMENT_REQUIRED_COUNT_MINIMUM

        return self._list_payments(pagination.url_params_count_only).value

    def _list_payments(self, params):
        """
        :type params: dict[str, str]

        :rtype BunqResponse[list[Payment]]
        """

        return endpoint.Payment.list(params=params)

    def _create_payment(self):
        """
        :rtype: None
        """

        endpoint.Payment.create(object_.Amount(self._PAYMENT_AMOUNT_EUR,
                                               self._PAYMENT_CURRENCY),
                                self._get_pointer_bravo(),
                                self._PAYMENT_DESCRIPTION)

from bunq import Pagination
from bunq.sdk.exception.bunq_exception import BunqException
from tests.bunq_test import BunqSdkTestCase


class TestPagination(BunqSdkTestCase):
    """
    Tests:
        Pagination
    """

    _PAGINATION_OLDER_ID_CUSTOM = 1
    _PAGINATION_NEWER_ID_CUSTOM = 2
    _PAGINATION_FUTURE_ID_CUSTOM = 3
    _PAGINATION_COUNT_CUSTOM = 5

    def test_get_url_params_count_only(self):
        pagination = self._create_pagination_with_all_properties_set()
        url_params_count_only_expected = {
            Pagination.PARAM_COUNT: str(self._PAGINATION_COUNT_CUSTOM),
        }

        self.assertEqual(url_params_count_only_expected,
                         pagination.url_params_count_only)

    def _create_pagination_with_all_properties_set(self):
        """
        :rtype: Pagination
        """

        pagination = Pagination()
        pagination.older_id = self._PAGINATION_OLDER_ID_CUSTOM
        pagination.newer_id = self._PAGINATION_NEWER_ID_CUSTOM
        pagination.future_id = self._PAGINATION_FUTURE_ID_CUSTOM
        pagination.count = self._PAGINATION_COUNT_CUSTOM

        return pagination

    def test_get_url_params_previous_page(self):
        pagination = self._create_pagination_with_all_properties_set()
        url_params_previous_page_expected = {
            Pagination.PARAM_COUNT: str(self._PAGINATION_COUNT_CUSTOM),
            Pagination.PARAM_OLDER_ID:
                str(self._PAGINATION_OLDER_ID_CUSTOM),
        }

        self.assertTrue(pagination.has_previous_page())
        self.assertEqual(url_params_previous_page_expected,
                         pagination.url_params_previous_page)

    def test_get_url_params_previous_page_no_count(self):
        pagination = self._create_pagination_with_all_properties_set()
        pagination.count = None
        url_params_previous_page_expected = {
            Pagination.PARAM_OLDER_ID:
                str(self._PAGINATION_OLDER_ID_CUSTOM),
        }

        self.assertTrue(pagination.has_previous_page())
        self.assertEqual(url_params_previous_page_expected,
                         pagination.url_params_previous_page)

    def test_get_url_params_next_page_newer(self):
        pagination = self._create_pagination_with_all_properties_set()
        url_params_next_page_expected = {
            Pagination.PARAM_COUNT: str(self._PAGINATION_COUNT_CUSTOM),
            Pagination.PARAM_NEWER_ID:
                str(self._PAGINATION_NEWER_ID_CUSTOM),
        }

        self.assertTrue(pagination.has_next_page_assured())
        self.assertEqual(url_params_next_page_expected,
                         pagination.url_params_next_page)

    def test_get_url_params_next_page_newer_no_count(self):
        pagination = self._create_pagination_with_all_properties_set()
        pagination.count = None
        url_params_next_page_expected = {
            Pagination.PARAM_NEWER_ID:
                str(self._PAGINATION_NEWER_ID_CUSTOM),
        }

        self.assertTrue(pagination.has_next_page_assured())
        self.assertEqual(url_params_next_page_expected,
                         pagination.url_params_next_page)

    def test_get_url_params_next_page_future(self):
        pagination = self._create_pagination_with_all_properties_set()
        pagination.newer_id = None
        url_params_next_page_expected = {
            Pagination.PARAM_COUNT: str(self._PAGINATION_COUNT_CUSTOM),
            Pagination.PARAM_NEWER_ID:
                str(self._PAGINATION_FUTURE_ID_CUSTOM),
        }

        self.assertFalse(pagination.has_next_page_assured())
        self.assertEqual(url_params_next_page_expected,
                         pagination.url_params_next_page)

    def test_get_url_params_next_page_future_no_count(self):
        pagination = self._create_pagination_with_all_properties_set()
        pagination.newer_id = None
        pagination.count = None
        url_params_next_page_expected = {
            Pagination.PARAM_NEWER_ID:
                str(self._PAGINATION_FUTURE_ID_CUSTOM),
        }

        self.assertFalse(pagination.has_next_page_assured())
        self.assertEqual(url_params_next_page_expected,
                         pagination.url_params_next_page)

    def test_get_url_params_prev_page_from_pagination_with_no_prev_page(self):
        pagination = self._create_pagination_with_all_properties_set()
        pagination.older_id = None

        def access_url_params_previous_page():
            _ = pagination.url_params_previous_page

        self.assertFalse(pagination.has_previous_page())
        self.assertRaises(BunqException,
                          access_url_params_previous_page)

    def test_get_url_params_next_page_from_pagination_with_no_next_page(self):
        pagination = self._create_pagination_with_all_properties_set()
        pagination.newer_id = None
        pagination.future_id = None

        def access_url_params_next_page():
            _ = pagination.url_params_next_page

        self.assertRaises(BunqException, access_url_params_next_page)

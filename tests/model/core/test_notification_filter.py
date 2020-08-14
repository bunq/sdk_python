from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.model.core.notification_filter_push_user_internal import NotificationFilterPushUserInternal
from bunq.sdk.model.core.notification_filter_url_monetary_account_internal import \
    NotificationFilterUrlMonetaryAccountInternal
from bunq.sdk.model.core.notification_filter_url_user_internal import NotificationFilterUrlUserInternal
from bunq.sdk.model.generated.object_ import NotificationFilterUrl, NotificationFilterPush
from tests.bunq_test import BunqSdkTestCase


class TestNotificationFilter(BunqSdkTestCase):
    _FILTER_CATEGORY_MUTATION = 'MUTATION'
    _FILTER_CALLBACK_URL = 'https://test.com/callback'

    def test_notification_filter_url_monetary_account(self):
        notification_filter = self.get_notification_filter_url()
        all_notification_filter = [notification_filter]

        all_created_notification_filter = NotificationFilterUrlMonetaryAccountInternal.create_with_list_response(
            self.get_primary_monetary_account().id_,
            all_notification_filter
        ).value

        self.assertEqual(1, len(all_created_notification_filter))

    def test_notification_filter_url_user(self):
        notification_filter = self.get_notification_filter_url()
        all_notification_filter = [notification_filter]

        all_created_notification_filter = NotificationFilterUrlUserInternal.create_with_list_response(
            all_notification_filter
        ).value

        self.assertEqual(1, len(all_created_notification_filter))

    def test_notification_filter_push_user(self):
        notification_filter = self.get_notification_filter_push()
        all_notification_filter = [notification_filter]

        all_created_notification_filter = NotificationFilterPushUserInternal.create_with_list_response(
            all_notification_filter
        ).value

        self.assertEqual(1, len(all_created_notification_filter))

    def test_notification_filter_clear(self):
        all_created_notification_filter_push_user = NotificationFilterPushUserInternal.create_with_list_response().value
        all_created_notification_filter_url_user = NotificationFilterUrlUserInternal.create_with_list_response().value
        all_created_notification_filter_url_monetary_account = \
            NotificationFilterUrlMonetaryAccountInternal.create_with_list_response().value

        self.assertFalse(all_created_notification_filter_push_user)
        self.assertFalse(all_created_notification_filter_url_user)
        self.assertFalse(all_created_notification_filter_url_monetary_account)

        self.assertEqual(0, len(NotificationFilterPushUserInternal.list().value))
        self.assertEqual(0, len(NotificationFilterUrlUserInternal.list().value))
        self.assertEqual(0, len(NotificationFilterUrlMonetaryAccountInternal.list().value))

    def get_notification_filter_url(self):
        return NotificationFilterUrl(self._FILTER_CATEGORY_MUTATION, self._FILTER_CALLBACK_URL)

    def get_notification_filter_push(self):
        return NotificationFilterPush(self._FILTER_CATEGORY_MUTATION)

    @staticmethod
    def get_primary_monetary_account():
        return BunqContext.user_context().primary_monetary_account

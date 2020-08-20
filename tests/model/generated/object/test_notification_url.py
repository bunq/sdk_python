import json
import os
from typing import Optional

from bunq.sdk.model.core.bunq_model import BunqModel
from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated import object_
from bunq.sdk.model.generated.endpoint import Payment, BunqMeTab, DraftPayment, MasterCardAction, MonetaryAccount, \
    MonetaryAccountBank, PaymentBatch, RequestInquiry, RequestResponse, SchedulePayment, ScheduleInstance, \
    ShareInviteMonetaryAccountInquiry, ShareInviteMonetaryAccountResponse
from bunq.sdk.model.generated.object_ import NotificationUrl
from tests import bunq_test


class TestNotificationUrl(bunq_test.BunqSdkTestCase):
    # Getter string constants
    _GETTER_PAYMENT = 'Payment'
    _GETTER_BUNQ_ME_TAB = 'BunqMeTab'
    _GETTER_CHAT_MESSAGE_ANNOUNCEMENT = 'ChatMessageAnnouncement'
    _GETTER_CHAT_MESSAGE = 'ChatMessage'
    _GETTER_DRAFT_PAYMENT = 'DraftPayment'
    _GETTER_MASTER_CARD_ACTION = 'MasterCardAction'
    _GETTER_MONETARY_ACCOUNT_BANK = 'MonetaryAccountBank'
    _GETTER_MONETARY_ACCOUNT = 'MonetaryAccount'
    _GETTER_PAYMENT_BATCH = 'PaymentBatch'
    _GETTER_REQUEST_INQUIRY = 'RequestInquiry'
    _GETTER_REQUEST_RESPONSE = 'RequestResponse'
    _GETTER_SCHEDULE_PAYMENT = 'ScheduledPayment'
    _GETTER_SCHEDULE_INSTANCE = 'ScheduledInstance'
    _GETTER_SHARE_INVITE_BANK_INQUIRY = 'ShareInviteBankInquiry'
    _GETTER_SHARE_INVITE_BANK_RESPONSE = 'ShareInviteBankResponse'

    # Model json paths constants.
    BASE_PATH_JSON_MODEL = '../../../assets/NotificationUrlJsons'
    JSON_PATH_MUTATION_MODEL = BASE_PATH_JSON_MODEL + '/Mutation.json'
    JSON_PATH_BUNQ_ME_TAB_MODEL = BASE_PATH_JSON_MODEL + '/BunqMeTab.json'
    JSON_PATH_CHAT_MESSAGE_ANNOUNCEMENT_MODEL = BASE_PATH_JSON_MODEL + '/ChatMessageAnnouncement.json'
    JSON_PATH_DRAFT_PAYMENT_MODEL = BASE_PATH_JSON_MODEL + '/DraftPayment.json'
    JSON_PATH_MASTER_CARD_ACTION_MODEL = BASE_PATH_JSON_MODEL + '/MasterCardAction.json'
    JSON_PATH_MONETARY_ACCOUNT_BANK_MODEL = BASE_PATH_JSON_MODEL + '/MonetaryAccountBank.json'
    JSON_PATH_PAYMENT_BATCH_MODEL = BASE_PATH_JSON_MODEL + '/PaymentBatch.json'
    JSON_PATH_REQUEST_INQUIRY_MODEL = BASE_PATH_JSON_MODEL + '/RequestInquiry.json'
    JSON_PATH_REQUEST_RESPONSE_MODEL = BASE_PATH_JSON_MODEL + '/RequestResponse.json'
    JSON_PATH_SCHEDULE_PAYMENT_MODEL = BASE_PATH_JSON_MODEL + '/ScheduledPayment.json'
    JSON_PATH_SCHEDULE_INSTANCE_MODEL = BASE_PATH_JSON_MODEL + '/ScheduledInstance.json'
    JSON_PATH_SHARE_INVITE_BANK_INQUIRY_MODEL = BASE_PATH_JSON_MODEL + '/ShareInviteBankInquiry.json'
    JSON_PATH_SHARE_INVITE_BANK_RESPONSE_MODEL = BASE_PATH_JSON_MODEL + '/ShareInviteBankResponse.json'

    # Model root key.
    _KEY_NOTIFICATION_URL_MODEL = 'NotificationUrl'

    # Model modules constants.
    _MODEL_MODULES = [
        object_,
        endpoint,
    ]

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    # File mode constants.
    _FILE_MODE_READ = 'r'

    def execute_notification_url_test(self,
                                      file_path: str,
                                      class_name: str,
                                      getter_name: str,
                                      sub_class_expected_object_name: str = None,
                                      sub_class_getter_name: str = None) -> None:
        notification_url = self.get_notification_url(file_path)
        self.assertIsNotNone(notification_url)
        self.assertIsNotNone(notification_url.object_)

        expected_model = getattr(notification_url.object_, getter_name)
        referenced_model = notification_url.object_.get_referenced_object()

        self.assertIsNotNone(expected_model)
        self.assertIsNotNone(referenced_model)
        self.assertTrue(self.is_model_reference(referenced_model, class_name))

        if sub_class_expected_object_name is not None:
            sub_class_model = getattr(referenced_model, sub_class_getter_name)

            self.assertIsNotNone(sub_class_model)
            self.assertTrue(isinstance(sub_class_model, self.get_model_type_or_none(sub_class_expected_object_name)))

    @classmethod
    def is_model_reference(cls, referenced_model: BunqModel, class_name: str) -> bool:
        model_type = cls.get_model_type_or_none(class_name)

        if model_type is None:
            return False

        return isinstance(referenced_model, model_type)

    @classmethod
    def get_model_type_or_none(cls, class_name: str) -> Optional[type]:
        for module_ in cls._MODEL_MODULES:
            if hasattr(module_, class_name):
                return getattr(module_, class_name)

        return None

    def get_notification_url(self, file_path: str) -> NotificationUrl:
        base_path = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(base_path, file_path))

        with open(file_path, self._FILE_MODE_READ) as f:
            json_string = f.read()
            json_object = json.loads(json_string)
            json_string = json.dumps(json_object[self._KEY_NOTIFICATION_URL_MODEL])

            self.assertTrue(self._KEY_NOTIFICATION_URL_MODEL in json_object)

            return object_.NotificationUrl.from_json(json_string)

    def test_mutation_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_MUTATION_MODEL,
            Payment.__name__,
            self._GETTER_PAYMENT
        )

    def test_bunq_me_tab_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_BUNQ_ME_TAB_MODEL,
            BunqMeTab.__name__,
            self._GETTER_BUNQ_ME_TAB
        )

    def test_draft_payment_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_DRAFT_PAYMENT_MODEL,
            DraftPayment.__name__,
            self._GETTER_DRAFT_PAYMENT
        )

    def test_mastercard_action(self):
        self.execute_notification_url_test(
            self.JSON_PATH_MASTER_CARD_ACTION_MODEL,
            MasterCardAction.__name__,
            self._GETTER_MASTER_CARD_ACTION
        )

    def test_monetary_account_bank_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_MONETARY_ACCOUNT_BANK_MODEL,
            MonetaryAccount.__name__,
            self._GETTER_MONETARY_ACCOUNT,
            MonetaryAccountBank.__name__,
            self._GETTER_MONETARY_ACCOUNT_BANK
        )

    def test_payment_batch_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_PAYMENT_BATCH_MODEL,
            PaymentBatch.__name__,
            self._GETTER_PAYMENT_BATCH
        )

    def test_request_inquiry_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_REQUEST_INQUIRY_MODEL,
            RequestInquiry.__name__,
            self._GETTER_REQUEST_INQUIRY
        )

    def test_request_response_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_REQUEST_RESPONSE_MODEL,
            RequestResponse.__name__,
            self._GETTER_REQUEST_RESPONSE
        )

    def test_scheduled_payment_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_SCHEDULE_PAYMENT_MODEL,
            SchedulePayment.__name__,
            self._GETTER_SCHEDULE_PAYMENT
        )

    def test_scheduled_instance_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_SCHEDULE_INSTANCE_MODEL,
            ScheduleInstance.__name__,
            self._GETTER_SCHEDULE_INSTANCE
        )

    def test_share_invite_bank_inquiry(self):
        self.execute_notification_url_test(
            self.JSON_PATH_SHARE_INVITE_BANK_INQUIRY_MODEL,
            ShareInviteMonetaryAccountInquiry.__name__,
            self._GETTER_SHARE_INVITE_BANK_INQUIRY
        )

    def test_share_invite_bank_response(self):
        self.execute_notification_url_test(
            self.JSON_PATH_SHARE_INVITE_BANK_RESPONSE_MODEL,
            ShareInviteMonetaryAccountResponse.__name__,
            self._GETTER_SHARE_INVITE_BANK_RESPONSE
        )

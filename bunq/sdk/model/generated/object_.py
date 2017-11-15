# -*- coding: utf-8 -*-
from bunq.sdk.model import core
from bunq.sdk import exception
from bunq.sdk.model.generated import endpoint


class InvoiceItemGroup(core.BunqModel):
    """
    :type type_: str
    :type type_description: str
    :type type_description_translated: str
    :type instance_description: str
    :type product_vat_exclusive: Amount
    :type product_vat_inclusive: Amount
    :type item: InvoiceItem
    """

    def __init__(self):
        self.type_ = None
        self.type_description = None
        self.type_description_translated = None
        self.instance_description = None
        self.product_vat_exclusive = None
        self.product_vat_inclusive = None
        self.item = None


class Amount(core.BunqModel):
    """
    :type value: str
    :type currency: str
    """

    def __init__(self, value, currency):
        """
        :type value: str
        :type currency: str
        """

        self.value = value
        self.currency = currency


class InvoiceItem(core.BunqModel):
    """
    :type billing_date: str
    :type type_description: str
    :type type_description_translated: str
    :type unit_vat_exclusive: Amount
    :type unit_vat_inclusive: Amount
    :type vat: float
    :type quantity: float
    :type total_vat_exclusive: Amount
    :type total_vat_inclusive: Amount
    """

    def __init__(self):
        self.billing_date = None
        self.type_description = None
        self.type_description_translated = None
        self.unit_vat_exclusive = None
        self.unit_vat_inclusive = None
        self.vat = None
        self.quantity = None
        self.total_vat_exclusive = None
        self.total_vat_inclusive = None


class LabelMonetaryAccount(core.BunqModel):
    """
    :type iban: str
    :type display_name: str
    :type avatar: Avatar
    :type label_user: LabelUser
    :type country: str
    :type bunq_me: MonetaryAccountReference
    :type is_light: bool
    :type swift_bic: str
    :type swift_account_number: str
    """

    def __init__(self):
        self.iban = None
        self.display_name = None
        self.avatar = None
        self.label_user = None
        self.country = None
        self.bunq_me = None
        self.is_light = None
        self.swift_bic = None
        self.swift_account_number = None


class Avatar(core.BunqModel):
    """
    :type uuid: str
    :type anchor_uuid: str
    :type image: list[Image]
    """

    def __init__(self, uuid):
        """
        :type uuid: str
        """

        self.uuid = uuid
        self.anchor_uuid = None
        self.image = None


class Image(core.BunqModel):
    """
    :type attachment_public_uuid: str
    :type content_type: str
    :type height: int
    :type width: int
    """

    def __init__(self):
        self.attachment_public_uuid = None
        self.content_type = None
        self.height = None
        self.width = None


class LabelUser(core.BunqModel):
    """
    :type uuid: str
    :type display_name: str
    :type country: str
    :type avatar: Avatar
    :type public_nick_name: str
    """

    def __init__(self, uuid, display_name, country):
        """
        :type uuid: str
        :type display_name: str
        :type country: str
        """

        self.uuid = uuid
        self.display_name = display_name
        self.country = country
        self.avatar = None
        self.public_nick_name = None


class Pointer(core.BunqModel):
    """
    :type type_: str
    :type value: str
    :type name: str
    """

    def __init__(self, type_, value):
        """
        :type type_: str
        :type value: str
        """

        self.type_ = type_
        self.value = value
        self.name = None


class Address(core.BunqModel):
    """
    :type street: str
    :type house_number: str
    :type po_box: str
    :type postal_code: str
    :type city: str
    :type country: str
    :type province: str
    """

    def __init__(self, street, house_number, postal_code, city, country):
        """
        :type street: str
        :type house_number: str
        :type postal_code: str
        :type city: str
        :type country: str
        """

        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.po_box = None
        self.province = None


class ChatMessageContent(core.BunqModel):
    """
    :type ChatMessageContentAnchorEvent: ChatMessageContentAnchorEvent
    :type ChatMessageContentAttachment: ChatMessageContentAttachment
    :type ChatMessageContentGeolocation: ChatMessageContentGeolocation
    :type ChatMessageContentStatusConversationTitle:
    ChatMessageContentStatusConversationTitle
    :type ChatMessageContentStatusConversation:
    ChatMessageContentStatusConversation
    :type ChatMessageContentStatusMembership: ChatMessageContentStatusMembership
    :type ChatMessageContentText: ChatMessageContentText
    """

    # Error constants.
    _ERROR_NULL_FIELDS = 'All fields of an extended model or object are null.'


    def __init__(self):
        self.ChatMessageContentAnchorEvent = None
        self.ChatMessageContentAttachment = None
        self.ChatMessageContentGeolocation = None
        self.ChatMessageContentStatusConversationTitle = None
        self.ChatMessageContentStatusConversation = None
        self.ChatMessageContentStatusMembership = None
        self.ChatMessageContentText = None

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self.ChatMessageContentAnchorEvent is not None:
            return self.ChatMessageContentAnchorEvent

        if self.ChatMessageContentAttachment is not None:
            return self.ChatMessageContentAttachment

        if self.ChatMessageContentGeolocation is not None:
            return self.ChatMessageContentGeolocation

        if self.ChatMessageContentStatusConversationTitle is not None:
            return self.ChatMessageContentStatusConversationTitle

        if self.ChatMessageContentStatusConversation is not None:
            return self.ChatMessageContentStatusConversation

        if self.ChatMessageContentStatusMembership is not None:
            return self.ChatMessageContentStatusMembership

        if self.ChatMessageContentText is not None:
            return self.ChatMessageContentText

        raise exception.BunqException(self._ERROR_NULL_FIELDS)


class ChatMessageContentAnchorEvent(core.BunqModel):
    """
    :type anchored_object: AnchoredObject
    """

    def __init__(self):
        self.anchored_object = None


class AnchoredObject(core.BunqModel):
    """
    :type CardDebit: endpoint.CardDebit
    :type CardPinChange: endpoint.CardPinChange
    :type CardResult: endpoint.CardResult
    :type DraftPayment: endpoint.DraftPayment
    :type IdealMerchantTransaction: endpoint.IdealMerchantTransaction
    :type Invoice: endpoint.Invoice
    :type Payment: endpoint.Payment
    :type PaymentBatch: endpoint.PaymentBatch
    :type PromotionDisplay: endpoint.PromotionDisplay
    :type RequestInquiryBatch: endpoint.RequestInquiryBatch
    :type RequestInquiry: endpoint.RequestInquiry
    :type RequestResponse: endpoint.RequestResponse
    :type ScheduledPaymentBatch: endpoint.SchedulePaymentBatch
    :type ScheduledPayment: endpoint.SchedulePayment
    :type ScheduledInstance: endpoint.ScheduleInstance
    :type ShareInviteBankInquiry: endpoint.ShareInviteBankInquiry
    :type ShareInviteBankResponse: endpoint.ShareInviteBankResponse
    :type UserCredentialPasswordIp: endpoint.UserCredentialPasswordIp
    """

    # Error constants.
    _ERROR_NULL_FIELDS = 'All fields of an extended model or object are null.'


    def __init__(self):
        self.CardDebit = None
        self.CardPinChange = None
        self.CardResult = None
        self.DraftPayment = None
        self.IdealMerchantTransaction = None
        self.Invoice = None
        self.Payment = None
        self.PaymentBatch = None
        self.PromotionDisplay = None
        self.RequestInquiryBatch = None
        self.RequestInquiry = None
        self.RequestResponse = None
        self.ScheduledPaymentBatch = None
        self.ScheduledPayment = None
        self.ScheduledInstance = None
        self.ShareInviteBankInquiry = None
        self.ShareInviteBankResponse = None
        self.UserCredentialPasswordIp = None

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self.CardDebit is not None:
            return self.CardDebit

        if self.CardPinChange is not None:
            return self.CardPinChange

        if self.CardResult is not None:
            return self.CardResult

        if self.DraftPayment is not None:
            return self.DraftPayment

        if self.IdealMerchantTransaction is not None:
            return self.IdealMerchantTransaction

        if self.Invoice is not None:
            return self.Invoice

        if self.Payment is not None:
            return self.Payment

        if self.PaymentBatch is not None:
            return self.PaymentBatch

        if self.PromotionDisplay is not None:
            return self.PromotionDisplay

        if self.RequestInquiryBatch is not None:
            return self.RequestInquiryBatch

        if self.RequestInquiry is not None:
            return self.RequestInquiry

        if self.RequestResponse is not None:
            return self.RequestResponse

        if self.ScheduledPaymentBatch is not None:
            return self.ScheduledPaymentBatch

        if self.ScheduledPayment is not None:
            return self.ScheduledPayment

        if self.ScheduledInstance is not None:
            return self.ScheduledInstance

        if self.ShareInviteBankInquiry is not None:
            return self.ShareInviteBankInquiry

        if self.ShareInviteBankResponse is not None:
            return self.ShareInviteBankResponse

        if self.UserCredentialPasswordIp is not None:
            return self.UserCredentialPasswordIp

        raise exception.BunqException(self._ERROR_NULL_FIELDS)


class CardLimit(core.BunqModel):
    """
    :type daily_limit: str
    :type currency: str
    :type type_: str
    :type id_: int
    """

    def __init__(self, daily_limit, currency, type_):
        """
        :type daily_limit: str
        :type currency: str
        :type type_: str
        """

        self.daily_limit = daily_limit
        self.currency = currency
        self.type_ = type_
        self.id_ = None


class CardCountryPermission(core.BunqModel):
    """
    :type country: str
    :type expiry_time: str
    :type id_: int
    """

    def __init__(self, country):
        """
        :type country: str
        """

        self.country = country
        self.expiry_time = None
        self.id_ = None


class CardPinAssignment(core.BunqModel):
    """
    :type type_: str
    :type pin_code: str
    :type monetary_account_id: str
    """

    def __init__(self, type_):
        """
        :type type_: str
        """

        self.type_ = type_
        self.pin_code = None
        self.monetary_account_id = None


class LabelCard(core.BunqModel):
    """
    :type uuid: str
    :type type_: str
    :type second_line: str
    :type expiry_date: str
    :type status: str
    :type label_user: LabelUser
    """

    def __init__(self):
        self.uuid = None
        self.type_ = None
        self.second_line = None
        self.expiry_date = None
        self.status = None
        self.label_user = None


class DraftPaymentResponse(core.BunqModel):
    """
    :type status: str
    :type user_alias_created: LabelUser
    """

    def __init__(self):
        self.status = None
        self.user_alias_created = None


class DraftPaymentEntry(core.BunqModel):
    """
    :type amount: Amount
    :type counterparty_alias: MonetaryAccountReference
    :type description: str
    :type merchant_reference: str
    :type attachment: list[AttachmentMonetaryAccountPayment]
    :type allow_bunqto: bool
    :type id_: int
    :type alias: MonetaryAccountReference
    :type type_: str
    """

    def __init__(self, amount, counterparty_alias, description):
        """
        :type amount: Amount
        :type counterparty_alias: MonetaryAccountReference
        :type description: str
        """

        self.amount = amount
        self.counterparty_alias = counterparty_alias
        self.description = description
        self.merchant_reference = None
        self.attachment = None
        self.allow_bunqto = None
        self.id_ = None
        self.alias = None
        self.type_ = None


class AttachmentMonetaryAccountPayment(core.BunqModel):
    """
    :type id_: int
    :type monetary_account_id: int
    """

    def __init__(self, id_):
        """
        :type id_: int
        """

        self.id_ = id_
        self.monetary_account_id = None


class DraftPaymentAnchorObject(core.BunqModel):
    """
    :type Payment: endpoint.Payment
    :type PaymentBatch: endpoint.PaymentBatch
    """

    # Error constants.
    _ERROR_NULL_FIELDS = 'All fields of an extended model or object are null.'


    def __init__(self):
        self.Payment = None
        self.PaymentBatch = None

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self.Payment is not None:
            return self.Payment

        if self.PaymentBatch is not None:
            return self.PaymentBatch

        raise exception.BunqException(self._ERROR_NULL_FIELDS)


class Geolocation(core.BunqModel):
    """
    :type latitude: float
    :type longitude: float
    :type altitude: float
    :type radius: float
    """

    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.altitude = None
        self.radius = None


class BunqId(core.BunqModel):
    """
    :type id_: int
    """

    def __init__(self, id_):
        """
        :type id_: int
        """

        self.id_ = id_


class Attachment(core.BunqModel):
    """
    :type description: str
    :type content_type: str
    """

    def __init__(self):
        self.description = None
        self.content_type = None


class SchedulePaymentEntry(core.BunqModel):
    """
    :type amount: Amount
    :type counterparty_alias: MonetaryAccountReference
    :type description: str
    :type attachment: list[AttachmentMonetaryAccountPayment]
    :type merchant_reference: str
    :type allow_bunqto: bool
    :type alias: MonetaryAccountReference
    """

    def __init__(self, amount, counterparty_alias, description):
        """
        :type amount: Amount
        :type counterparty_alias: MonetaryAccountReference
        :type description: str
        """

        self.amount = amount
        self.counterparty_alias = counterparty_alias
        self.description = description
        self.attachment = None
        self.merchant_reference = None
        self.allow_bunqto = None
        self.alias = None


class ScheduleAnchorObject(core.BunqModel):
    """
    :type Payment: endpoint.Payment
    :type PaymentBatch: endpoint.PaymentBatch
    """

    # Error constants.
    _ERROR_NULL_FIELDS = 'All fields of an extended model or object are null.'


    def __init__(self):
        self.Payment = None
        self.PaymentBatch = None

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self.Payment is not None:
            return self.Payment

        if self.PaymentBatch is not None:
            return self.PaymentBatch

        raise exception.BunqException(self._ERROR_NULL_FIELDS)


class Error(core.BunqModel):
    """
    :type error_description: str
    :type error_description_translated: str
    """

    def __init__(self):
        self.error_description = None
        self.error_description_translated = None


class ScheduleInstanceAnchorObject(core.BunqModel):
    """
    :type Payment: endpoint.Payment
    :type PaymentBatch: endpoint.PaymentBatch
    """

    # Error constants.
    _ERROR_NULL_FIELDS = 'All fields of an extended model or object are null.'


    def __init__(self):
        self.Payment = None
        self.PaymentBatch = None

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self.Payment is not None:
            return self.Payment

        if self.PaymentBatch is not None:
            return self.PaymentBatch

        raise exception.BunqException(self._ERROR_NULL_FIELDS)


class ShareDetail(core.BunqModel):
    """
    :type payment: ShareDetailPayment
    :type read_only: ShareDetailReadOnly
    :type draft_payment: ShareDetailDraftPayment
    """

    def __init__(self):
        self.payment = None
        self.read_only = None
        self.draft_payment = None


class ShareDetailPayment(core.BunqModel):
    """
    :type make_payments: bool
    :type make_draft_payments: bool
    :type view_balance: bool
    :type view_old_events: bool
    :type view_new_events: bool
    :type budget: BudgetRestriction
    """

    def __init__(self, make_payments, view_balance, view_old_events, view_new_events):
        """
        :type make_payments: bool
        :type view_balance: bool
        :type view_old_events: bool
        :type view_new_events: bool
        """

        self.make_payments = make_payments
        self.view_balance = view_balance
        self.view_old_events = view_old_events
        self.view_new_events = view_new_events
        self.make_draft_payments = None
        self.budget = None


class BudgetRestriction(core.BunqModel):
    """
    :type amount: Amount
    :type frequency: str
    """

    def __init__(self):
        self.amount = None
        self.frequency = None


class ShareDetailReadOnly(core.BunqModel):
    """
    :type view_balance: bool
    :type view_old_events: bool
    :type view_new_events: bool
    """

    def __init__(self, view_balance, view_old_events, view_new_events):
        """
        :type view_balance: bool
        :type view_old_events: bool
        :type view_new_events: bool
        """

        self.view_balance = view_balance
        self.view_old_events = view_old_events
        self.view_new_events = view_new_events


class ShareDetailDraftPayment(core.BunqModel):
    """
    :type make_draft_payments: bool
    :type view_balance: bool
    :type view_old_events: bool
    :type view_new_events: bool
    """

    def __init__(self, make_draft_payments, view_balance, view_old_events, view_new_events):
        """
        :type make_draft_payments: bool
        :type view_balance: bool
        :type view_old_events: bool
        :type view_new_events: bool
        """

        self.make_draft_payments = make_draft_payments
        self.view_balance = view_balance
        self.view_old_events = view_old_events
        self.view_new_events = view_new_events


class PermittedDevice(core.BunqModel):
    """
    :type description: str
    :type ip: str
    """

    def __init__(self):
        self.description = None
        self.ip = None


class ChatMessageContentAttachment(core.BunqModel):
    """
    :type attachment: Attachment
    """

    def __init__(self):
        self.attachment = None


class ChatMessageContentGeolocation(core.BunqModel):
    """
    :type geolocation: Geolocation
    """

    def __init__(self):
        self.geolocation = None


class ChatMessageContentStatusConversationTitle(core.BunqModel):
    """
    :type title: str
    """

    def __init__(self):
        self.title = None


class ChatMessageContentStatusConversation(core.BunqModel):
    """
    :type action: str
    """

    def __init__(self):
        self.action = None


class ChatMessageContentStatusMembership(core.BunqModel):
    """
    :type action: str
    :type member: LabelUser
    """

    def __init__(self):
        self.action = None
        self.member = None


class ChatMessageContentText(core.BunqModel):
    """
    :type text: str
    """

    def __init__(self):
        self.text = None


class BunqMeMerchantAvailable(core.BunqModel):
    """
    :type merchant_type: str
    :type available: bool
    """

    def __init__(self):
        self.merchant_type = None
        self.available = None


class CardMagStripePermission(core.BunqModel):
    """
    :type expiry_time: str
    """

    def __init__(self):
        self.expiry_time = None


class NotificationFilter(core.BunqModel):
    """
    :type notification_delivery_method: str
    :type notification_target: str
    :type category: str
    """

    def __init__(self, notification_delivery_method, notification_target, category):
        """
        :type notification_delivery_method: str
        :type notification_target: str
        :type category: str
        """

        self.notification_delivery_method = notification_delivery_method
        self.notification_target = notification_target
        self.category = category


class TabTextWaitingScreen(core.BunqModel):
    """
    :type language: str
    :type description: str
    """

    def __init__(self, language, description):
        """
        :type language: str
        :type description: str
        """

        self.language = language
        self.description = description


class TabVisibility(core.BunqModel):
    """
    :type cash_register_qr_code: bool
    :type tab_qr_code: bool
    :type location: Geolocation
    """

    def __init__(self, cash_register_qr_code, tab_qr_code):
        """
        :type cash_register_qr_code: bool
        :type tab_qr_code: bool
        """

        self.cash_register_qr_code = cash_register_qr_code
        self.tab_qr_code = tab_qr_code
        self.location = None


class AttachmentPublic(core.BunqModel):
    """
    :type uuid: str
    :type description: str
    :type content_type: str
    """

    def __init__(self):
        self.uuid = None
        self.description = None
        self.content_type = None


class AttachmentTab(core.BunqModel):
    """
    :type id_: int
    :type description: str
    :type content_type: str
    """

    def __init__(self):
        self.id_ = None
        self.description = None
        self.content_type = None


class Certificate(core.BunqModel):
    """
    :type certificate: str
    """

    def __init__(self, certificate):
        """
        :type certificate: str
        """

        self.certificate = certificate


class DraftShareInviteBankEntry(core.BunqModel):
    """
    :type share_detail: ShareDetail
    :type start_date: str
    :type end_date: str
    """

    def __init__(self, share_detail):
        """
        :type share_detail: ShareDetail
        """

        self.share_detail = share_detail
        self.start_date = None
        self.end_date = None


class MonetaryAccountProfileFill(core.BunqModel):
    """
    :type status: str
    :type balance_preferred: Amount
    :type balance_threshold_low: Amount
    :type method_fill: str
    :type issuer: Issuer
    """

    def __init__(self, status, balance_preferred, balance_threshold_low, method_fill):
        """
        :type status: str
        :type balance_preferred: Amount
        :type balance_threshold_low: Amount
        :type method_fill: str
        """

        self.status = status
        self.balance_preferred = balance_preferred
        self.balance_threshold_low = balance_threshold_low
        self.method_fill = method_fill
        self.issuer = None


class Issuer(core.BunqModel):
    """
    :type bic: str
    :type name: str
    """

    def __init__(self, bic):
        """
        :type bic: str
        """

        self.bic = bic
        self.name = None


class MonetaryAccountProfileDrain(core.BunqModel):
    """
    :type status: str
    :type balance_preferred: Amount
    :type balance_threshold_high: Amount
    :type savings_account_alias: MonetaryAccountReference
    """

    def __init__(self, status, balance_preferred, balance_threshold_high, savings_account_alias):
        """
        :type status: str
        :type balance_preferred: Amount
        :type balance_threshold_high: Amount
        :type savings_account_alias: MonetaryAccountReference
        """

        self.status = status
        self.balance_preferred = balance_preferred
        self.balance_threshold_high = balance_threshold_high
        self.savings_account_alias = savings_account_alias


class MonetaryAccountSetting(core.BunqModel):
    """
    :type color: str
    :type default_avatar_status: str
    :type restriction_chat: str
    """

    def __init__(self):
        self.color = None
        self.default_avatar_status = None
        self.restriction_chat = None


class NotificationUrl(core.BunqModel):
    """
    :type target_url: str
    :type category: str
    :type event_type: str
    :type object_: NotificationAnchorObject
    """

    def __init__(self):
        self.target_url = None
        self.category = None
        self.event_type = None
        self.object_ = None


class NotificationAnchorObject(core.BunqModel):
    """
    :type BunqMeTab: endpoint.BunqMeTab
    :type BunqMeTabResultInquiry: endpoint.BunqMeTabResultInquiry
    :type BunqMeTabResultResponse: endpoint.BunqMeTabResultResponse
    :type ChatMessageStatus: endpoint.ChatMessageStatus
    :type ChatMessageUser: endpoint.ChatMessageUser
    :type ChatMessageAnnouncement: endpoint.ChatMessageAnnouncement
    :type DraftPayment: endpoint.DraftPayment
    :type IdealMerchantTransaction: endpoint.IdealMerchantTransaction
    :type Invoice: endpoint.Invoice
    :type MasterCardAction: endpoint.MasterCardAction
    :type MonetaryAccountBank: endpoint.MonetaryAccountBank
    :type Payment: endpoint.Payment
    :type PaymentBatch: endpoint.PaymentBatch
    :type RequestInquiry: endpoint.RequestInquiry
    :type RequestInquiryBatch: endpoint.RequestInquiryBatch
    :type RequestResponse: endpoint.RequestResponse
    :type ShareInviteBankInquiry: endpoint.ShareInviteBankInquiry
    :type ShareInviteBankResponse: endpoint.ShareInviteBankResponse
    :type ScheduledPayment: endpoint.SchedulePayment
    :type ScheduledInstance: endpoint.ScheduleInstance
    :type TabResultInquiry: endpoint.TabResultInquiry
    :type TabResultResponse: endpoint.TabResultResponse
    :type UserPerson: endpoint.UserPerson
    :type UserCompany: endpoint.UserCompany
    """

    # Error constants.
    _ERROR_NULL_FIELDS = 'All fields of an extended model or object are null.'


    def __init__(self):
        self.BunqMeTab = None
        self.BunqMeTabResultInquiry = None
        self.BunqMeTabResultResponse = None
        self.ChatMessageStatus = None
        self.ChatMessageUser = None
        self.ChatMessageAnnouncement = None
        self.DraftPayment = None
        self.IdealMerchantTransaction = None
        self.Invoice = None
        self.MasterCardAction = None
        self.MonetaryAccountBank = None
        self.Payment = None
        self.PaymentBatch = None
        self.RequestInquiry = None
        self.RequestInquiryBatch = None
        self.RequestResponse = None
        self.ShareInviteBankInquiry = None
        self.ShareInviteBankResponse = None
        self.ScheduledPayment = None
        self.ScheduledInstance = None
        self.TabResultInquiry = None
        self.TabResultResponse = None
        self.UserPerson = None
        self.UserCompany = None

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self.BunqMeTab is not None:
            return self.BunqMeTab

        if self.BunqMeTabResultInquiry is not None:
            return self.BunqMeTabResultInquiry

        if self.BunqMeTabResultResponse is not None:
            return self.BunqMeTabResultResponse

        if self.ChatMessageStatus is not None:
            return self.ChatMessageStatus

        if self.ChatMessageUser is not None:
            return self.ChatMessageUser

        if self.ChatMessageAnnouncement is not None:
            return self.ChatMessageAnnouncement

        if self.DraftPayment is not None:
            return self.DraftPayment

        if self.IdealMerchantTransaction is not None:
            return self.IdealMerchantTransaction

        if self.Invoice is not None:
            return self.Invoice

        if self.MasterCardAction is not None:
            return self.MasterCardAction

        if self.MonetaryAccountBank is not None:
            return self.MonetaryAccountBank

        if self.Payment is not None:
            return self.Payment

        if self.PaymentBatch is not None:
            return self.PaymentBatch

        if self.RequestInquiry is not None:
            return self.RequestInquiry

        if self.RequestInquiryBatch is not None:
            return self.RequestInquiryBatch

        if self.RequestResponse is not None:
            return self.RequestResponse

        if self.ShareInviteBankInquiry is not None:
            return self.ShareInviteBankInquiry

        if self.ShareInviteBankResponse is not None:
            return self.ShareInviteBankResponse

        if self.ScheduledPayment is not None:
            return self.ScheduledPayment

        if self.ScheduledInstance is not None:
            return self.ScheduledInstance

        if self.TabResultInquiry is not None:
            return self.TabResultInquiry

        if self.TabResultResponse is not None:
            return self.TabResultResponse

        if self.UserPerson is not None:
            return self.UserPerson

        if self.UserCompany is not None:
            return self.UserCompany

        raise exception.BunqException(self._ERROR_NULL_FIELDS)


class TaxResident(core.BunqModel):
    """
    :type country: str
    :type tax_number: str
    """

    def __init__(self, country, tax_number):
        """
        :type country: str
        :type tax_number: str
        """

        self.country = country
        self.tax_number = tax_number


class Ubo(core.BunqModel):
    """
    :type name: str
    :type date_of_birth: str
    :type nationality: str
    """

    def __init__(self):
        self.name = None
        self.date_of_birth = None
        self.nationality = None


class MonetaryAccountReference(core.BunqModel):
    """
    :type pointer: Pointer
    :type label_monetary_account: LabelMonetaryAccount
    """

    # Error constants
    _ERROR_COULD_NOT_INSTANTIATE = 'Could not directly instantiate ' \
                                   'MonetaryAccountReference. Please use ' \
                                   'the class factory methods.'

    # Pointer type for creating pointer from LabelMonetaryAccount
    _POINTER_TYPE_IBAN = 'IBAN'

    def __init__(self):
        """
        :raise: TypeError always, to prevent instantiation via constructor.
        """

        self.pointer = None
        self.label_monetary_account = None

        raise TypeError(self._ERROR_COULD_NOT_INSTANTIATE)

    @classmethod
    def create_from_pointer(cls, pointer):
        """
        :type pointer: Pointer
        """

        instance = cls.__new__(cls)
        instance.pointer = pointer
        instance.label_monetary_account = LabelMonetaryAccount()
        instance.label_monetary_account.iban = pointer.value
        instance.label_monetary_account.display_name = pointer.name

        return instance

    @classmethod
    def create_from_label_monetary_account(cls, label_monetary_account):
        """
        :type label_monetary_account: LabelMonetaryAccount
        """

        instance = cls.__new__(cls)
        instance.label_monetary_account = label_monetary_account
        instance.pointer = Pointer(
            cls._POINTER_TYPE_IBAN,
            label_monetary_account.iban
        )
        instance.pointer.name = label_monetary_account.display_name

        return instance

# -*- coding: utf-8 -*-
from bunq.sdk import model


class InvoiceItemGroup(model.BunqModel):
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


class Amount(model.BunqModel):
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


class InvoiceItem(model.BunqModel):
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


class LabelMonetaryAccount(model.BunqModel):
    """
    :type iban: str
    :type display_name: str
    :type avatar: Avatar
    :type label_user: LabelUser
    :type country: str
    :type bunq_me: MonetaryAccountReference
    """

    def __init__(self):
        self.iban = None
        self.display_name = None
        self.avatar = None
        self.label_user = None
        self.country = None
        self.bunq_me = None


class Avatar(model.BunqModel):
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


class Image(model.BunqModel):
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


class LabelUser(model.BunqModel):
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


class Pointer(model.BunqModel):
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


class Address(model.BunqModel):
    """
    :type street: str
    :type house_number: str
    :type po_box: str
    :type postal_code: str
    :type city: str
    :type country: str
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


class BunqId(model.BunqModel):
    """
    :type id_: int
    """

    def __init__(self, id_):
        """
        :type id_: int
        """

        self.id_ = id_


class Attachment(model.BunqModel):
    """
    :type description: str
    :type content_type: str
    """

    def __init__(self):
        self.description = None
        self.content_type = None


class CardLimit(model.BunqModel):
    """
    :type daily_limit: str
    :type currency: str
    :type type_: str
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


class CardCountryPermission(model.BunqModel):
    """
    :type country: str
    :type expiry_time: str
    """

    def __init__(self, country):
        """
        :type country: str
        """

        self.country = country
        self.expiry_time = None


class CardMagStripePermission(model.BunqModel):
    """
    :type expiry_time: str
    """

    def __init__(self):
        self.expiry_time = None


class CardPinAssignment(model.BunqModel):
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


class Geolocation(model.BunqModel):
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


class NotificationFilter(model.BunqModel):
    """
    :type notification_delivery_method: str
    :type notification_target: str
    :type category: str
    """

    def __init__(self, notification_delivery_method, notification_target,
                 category):
        """
        :type notification_delivery_method: str
        :type notification_target: str
        :type category: str
        """

        self.notification_delivery_method = notification_delivery_method
        self.notification_target = notification_target
        self.category = category


class TabTextWaitingScreen(model.BunqModel):
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


class TabVisibility(model.BunqModel):
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


class AttachmentPublic(model.BunqModel):
    """
    :type uuid: str
    :type description: str
    :type content_type: str
    """

    def __init__(self):
        self.uuid = None
        self.description = None
        self.content_type = None


class AttachmentTab(model.BunqModel):
    """
    :type id_: int
    :type description: str
    :type content_type: str
    """

    def __init__(self):
        self.id_ = None
        self.description = None
        self.content_type = None


class Certificate(model.BunqModel):
    """
    :type certificate: str
    """

    def __init__(self, certificate):
        """
        :type certificate: str
        """

        self.certificate = certificate


class DraftShareInviteBankEntry(model.BunqModel):
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


class ShareDetail(model.BunqModel):
    """
    :type payment: ShareDetailPayment
    :type read_only: ShareDetailReadOnly
    :type draft_payment: ShareDetailDraftPayment
    """

    def __init__(self):
        self.payment = None
        self.read_only = None
        self.draft_payment = None


class ShareDetailPayment(model.BunqModel):
    """
    :type make_payments: bool
    :type make_draft_payments: bool
    :type view_balance: bool
    :type view_old_events: bool
    :type view_new_events: bool
    :type budget: BudgetRestriction
    """

    def __init__(self, make_payments, view_balance, view_old_events,
                 view_new_events):
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


class BudgetRestriction(model.BunqModel):
    """
    :type amount: Amount
    :type frequency: str
    """

    def __init__(self):
        self.amount = None
        self.frequency = None


class ShareDetailReadOnly(model.BunqModel):
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


class ShareDetailDraftPayment(model.BunqModel):
    """
    :type make_draft_payments: bool
    :type view_balance: bool
    :type view_old_events: bool
    :type view_new_events: bool
    """

    def __init__(self, make_draft_payments, view_balance, view_old_events,
                 view_new_events):
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


class MonetaryAccountProfileFill(model.BunqModel):
    """
    :type status: str
    :type balance_preferred: Amount
    :type balance_threshold_low: Amount
    :type method_fill: str
    :type issuer: Issuer
    """

    def __init__(self, status, balance_preferred, balance_threshold_low,
                 method_fill):
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


class Issuer(model.BunqModel):
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


class MonetaryAccountProfileDrain(model.BunqModel):
    """
    :type status: str
    :type balance_preferred: Amount
    :type balance_threshold_high: Amount
    :type savings_account_alias: MonetaryAccountReference
    """

    def __init__(self, status, balance_preferred, balance_threshold_high,
                 savings_account_alias):
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


class MonetaryAccountSetting(model.BunqModel):
    """
    :type color: str
    :type default_avatar_status: str
    :type restriction_chat: str
    """

    def __init__(self):
        self.color = None
        self.default_avatar_status = None
        self.restriction_chat = None


class AttachmentMonetaryAccountPayment(model.BunqModel):
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


class Error(model.BunqModel):
    """
    :type error_description: str
    :type error_description_translated: str
    """

    def __init__(self):
        self.error_description = None
        self.error_description_translated = None


class SchedulePaymentEntry(model.BunqModel):
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


class Schedule(model.BunqModel):
    """
    :type time_start: str
    :type time_end: str
    :type recurrence_unit: str
    :type recurrence_size: int
    :type status: str
    :type object_: model.BunqModel
    """

    def __init__(self, time_start, recurrence_unit, recurrence_size):
        """
        :type time_start: str
        :type recurrence_unit: str
        :type recurrence_size: int
        """

        self.time_start = time_start
        self.recurrence_unit = recurrence_unit
        self.recurrence_size = recurrence_size
        self.time_end = None
        self.status = None
        self.object_ = None


class Ubo(model.BunqModel):
    """
    :type name: str
    :type date_of_birth: str
    :type nationality: str
    """

    def __init__(self):
        self.name = None
        self.date_of_birth = None
        self.nationality = None


class PermittedDevice(model.BunqModel):
    """
    :type description: str
    :type ip: str
    """

    def __init__(self):
        self.description = None
        self.ip = None


class TaxResident(model.BunqModel):
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


class MonetaryAccountReference(model.BunqModel):
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

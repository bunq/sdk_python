# -*- coding: utf-8 -*-
from bunq.sdk.model import core
from bunq.sdk import exception
from bunq.sdk.model.generated import endpoint
from bunq.sdk.json import converter


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.type_ is not None:
            return False

        if self.type_description is not None:
            return False

        if self.type_description_translated is not None:
            return False

        if self.instance_description is not None:
            return False

        if self.product_vat_exclusive is not None:
            return False

        if self.product_vat_inclusive is not None:
            return False

        if self.item is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: InvoiceItemGroup
        """

        return converter.json_to_class(InvoiceItemGroup, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.value is not None:
            return False

        if self.currency is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Amount
        """

        return converter.json_to_class(Amount, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.billing_date is not None:
            return False

        if self.type_description is not None:
            return False

        if self.type_description_translated is not None:
            return False

        if self.unit_vat_exclusive is not None:
            return False

        if self.unit_vat_inclusive is not None:
            return False

        if self.vat is not None:
            return False

        if self.quantity is not None:
            return False

        if self.total_vat_exclusive is not None:
            return False

        if self.total_vat_inclusive is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: InvoiceItem
        """

        return converter.json_to_class(InvoiceItem, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.iban is not None:
            return False

        if self.display_name is not None:
            return False

        if self.avatar is not None:
            return False

        if self.label_user is not None:
            return False

        if self.country is not None:
            return False

        if self.bunq_me is not None:
            return False

        if self.is_light is not None:
            return False

        if self.swift_bic is not None:
            return False

        if self.swift_account_number is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: LabelMonetaryAccount
        """

        return converter.json_to_class(LabelMonetaryAccount, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.uuid is not None:
            return False

        if self.anchor_uuid is not None:
            return False

        if self.image is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Avatar
        """

        return converter.json_to_class(Avatar, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.attachment_public_uuid is not None:
            return False

        if self.content_type is not None:
            return False

        if self.height is not None:
            return False

        if self.width is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Image
        """

        return converter.json_to_class(Image, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.uuid is not None:
            return False

        if self.avatar is not None:
            return False

        if self.public_nick_name is not None:
            return False

        if self.display_name is not None:
            return False

        if self.country is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: LabelUser
        """

        return converter.json_to_class(LabelUser, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.type_ is not None:
            return False

        if self.value is not None:
            return False

        if self.name is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Pointer
        """

        return converter.json_to_class(Pointer, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.street is not None:
            return False

        if self.house_number is not None:
            return False

        if self.po_box is not None:
            return False

        if self.postal_code is not None:
            return False

        if self.city is not None:
            return False

        if self.country is not None:
            return False

        if self.province is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Address
        """

        return converter.json_to_class(Address, json_str)


class ChatMessageContent(core.BunqModel, core.AnchoredObjectInterface):
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
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."


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

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.ChatMessageContentAnchorEvent is not None:
            return False

        if self.ChatMessageContentAttachment is not None:
            return False

        if self.ChatMessageContentGeolocation is not None:
            return False

        if self.ChatMessageContentStatusConversationTitle is not None:
            return False

        if self.ChatMessageContentStatusConversation is not None:
            return False

        if self.ChatMessageContentStatusMembership is not None:
            return False

        if self.ChatMessageContentText is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageContent
        """

        return converter.json_to_class(ChatMessageContent, json_str)


class ChatMessageContentAnchorEvent(core.BunqModel):
    """
    :type anchored_object: AnchoredObject
    """

    def __init__(self):
        self.anchored_object = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.anchored_object is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageContentAnchorEvent
        """

        return converter.json_to_class(ChatMessageContentAnchorEvent, json_str)


class AnchoredObject(core.BunqModel, core.AnchoredObjectInterface):
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
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."


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

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.CardDebit is not None:
            return False

        if self.CardPinChange is not None:
            return False

        if self.CardResult is not None:
            return False

        if self.DraftPayment is not None:
            return False

        if self.IdealMerchantTransaction is not None:
            return False

        if self.Invoice is not None:
            return False

        if self.Payment is not None:
            return False

        if self.PaymentBatch is not None:
            return False

        if self.PromotionDisplay is not None:
            return False

        if self.RequestInquiryBatch is not None:
            return False

        if self.RequestInquiry is not None:
            return False

        if self.RequestResponse is not None:
            return False

        if self.ScheduledPaymentBatch is not None:
            return False

        if self.ScheduledPayment is not None:
            return False

        if self.ScheduledInstance is not None:
            return False

        if self.ShareInviteBankInquiry is not None:
            return False

        if self.ShareInviteBankResponse is not None:
            return False

        if self.UserCredentialPasswordIp is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AnchoredObject
        """

        return converter.json_to_class(AnchoredObject, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.id_ is not None:
            return False

        if self.daily_limit is not None:
            return False

        if self.currency is not None:
            return False

        if self.type_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardLimit
        """

        return converter.json_to_class(CardLimit, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.id_ is not None:
            return False

        if self.country is not None:
            return False

        if self.expiry_time is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardCountryPermission
        """

        return converter.json_to_class(CardCountryPermission, json_str)


class CardPinAssignment(core.BunqModel):
    """
    :type type_: str
    :type pin_code: str
    :type monetary_account_id: int
    """

    def __init__(self, type_, pin_code, monetary_account_id):
        """
        :type type_: str
        :type pin_code: str
        :type monetary_account_id: int
        """

        self.type_ = type_
        self.pin_code = pin_code
        self.monetary_account_id = monetary_account_id


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.type_ is not None:
            return False

        if self.monetary_account_id is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardPinAssignment
        """

        return converter.json_to_class(CardPinAssignment, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.uuid is not None:
            return False

        if self.type_ is not None:
            return False

        if self.second_line is not None:
            return False

        if self.expiry_date is not None:
            return False

        if self.status is not None:
            return False

        if self.label_user is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: LabelCard
        """

        return converter.json_to_class(LabelCard, json_str)


class DraftPaymentResponse(core.BunqModel):
    """
    :type status: str
    :type user_alias_created: LabelUser
    """

    def __init__(self):
        self.status = None
        self.user_alias_created = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.status is not None:
            return False

        if self.user_alias_created is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftPaymentResponse
        """

        return converter.json_to_class(DraftPaymentResponse, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.id_ is not None:
            return False

        if self.amount is not None:
            return False

        if self.alias is not None:
            return False

        if self.counterparty_alias is not None:
            return False

        if self.description is not None:
            return False

        if self.merchant_reference is not None:
            return False

        if self.type_ is not None:
            return False

        if self.attachment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftPaymentEntry
        """

        return converter.json_to_class(DraftPaymentEntry, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.id_ is not None:
            return False

        if self.monetary_account_id is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentMonetaryAccountPayment
        """

        return converter.json_to_class(AttachmentMonetaryAccountPayment, json_str)


class DraftPaymentAnchorObject(core.BunqModel, core.AnchoredObjectInterface):
    """
    :type Payment: endpoint.Payment
    :type PaymentBatch: endpoint.PaymentBatch
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."


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

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.Payment is not None:
            return False

        if self.PaymentBatch is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftPaymentAnchorObject
        """

        return converter.json_to_class(DraftPaymentAnchorObject, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.latitude is not None:
            return False

        if self.longitude is not None:
            return False

        if self.altitude is not None:
            return False

        if self.radius is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Geolocation
        """

        return converter.json_to_class(Geolocation, json_str)


class BunqId(core.BunqModel):
    """
    :type id_: int
    """

    def __init__(self, id_):
        """
        :type id_: int
        """

        self.id_ = id_


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BunqId
        """

        return converter.json_to_class(BunqId, json_str)


class Attachment(core.BunqModel):
    """
    :type description: str
    :type content_type: str
    """

    def __init__(self):
        self.description = None
        self.content_type = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.description is not None:
            return False

        if self.content_type is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Attachment
        """

        return converter.json_to_class(Attachment, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.amount is not None:
            return False

        if self.alias is not None:
            return False

        if self.counterparty_alias is not None:
            return False

        if self.description is not None:
            return False

        if self.attachment is not None:
            return False

        if self.merchant_reference is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: SchedulePaymentEntry
        """

        return converter.json_to_class(SchedulePaymentEntry, json_str)


class ScheduleAnchorObject(core.BunqModel, core.AnchoredObjectInterface):
    """
    :type Payment: endpoint.Payment
    :type PaymentBatch: endpoint.PaymentBatch
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."


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

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.Payment is not None:
            return False

        if self.PaymentBatch is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ScheduleAnchorObject
        """

        return converter.json_to_class(ScheduleAnchorObject, json_str)


class Error(core.BunqModel):
    """
    :type error_description: str
    :type error_description_translated: str
    """

    def __init__(self):
        self.error_description = None
        self.error_description_translated = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.error_description is not None:
            return False

        if self.error_description_translated is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Error
        """

        return converter.json_to_class(Error, json_str)


class ScheduleInstanceAnchorObject(core.BunqModel, core.AnchoredObjectInterface):
    """
    :type Payment: endpoint.Payment
    :type PaymentBatch: endpoint.PaymentBatch
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."


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

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.Payment is not None:
            return False

        if self.PaymentBatch is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ScheduleInstanceAnchorObject
        """

        return converter.json_to_class(ScheduleInstanceAnchorObject, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.payment is not None:
            return False

        if self.read_only is not None:
            return False

        if self.draft_payment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareDetail
        """

        return converter.json_to_class(ShareDetail, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.make_payments is not None:
            return False

        if self.make_draft_payments is not None:
            return False

        if self.view_balance is not None:
            return False

        if self.view_old_events is not None:
            return False

        if self.view_new_events is not None:
            return False

        if self.budget is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareDetailPayment
        """

        return converter.json_to_class(ShareDetailPayment, json_str)


class BudgetRestriction(core.BunqModel):
    """
    :type amount: Amount
    :type frequency: str
    """

    def __init__(self):
        self.amount = None
        self.frequency = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.amount is not None:
            return False

        if self.frequency is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BudgetRestriction
        """

        return converter.json_to_class(BudgetRestriction, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.view_balance is not None:
            return False

        if self.view_old_events is not None:
            return False

        if self.view_new_events is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareDetailReadOnly
        """

        return converter.json_to_class(ShareDetailReadOnly, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.make_draft_payments is not None:
            return False

        if self.view_balance is not None:
            return False

        if self.view_old_events is not None:
            return False

        if self.view_new_events is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareDetailDraftPayment
        """

        return converter.json_to_class(ShareDetailDraftPayment, json_str)


class PermittedDevice(core.BunqModel):
    """
    :type description: str
    :type ip: str
    """

    def __init__(self):
        self.description = None
        self.ip = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.description is not None:
            return False

        if self.ip is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: PermittedDevice
        """

        return converter.json_to_class(PermittedDevice, json_str)


class ChatMessageContentAttachment(core.BunqModel):
    """
    :type attachment: Attachment
    """

    def __init__(self):
        self.attachment = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.attachment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageContentAttachment
        """

        return converter.json_to_class(ChatMessageContentAttachment, json_str)


class ChatMessageContentGeolocation(core.BunqModel):
    """
    :type geolocation: Geolocation
    """

    def __init__(self):
        self.geolocation = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.geolocation is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageContentGeolocation
        """

        return converter.json_to_class(ChatMessageContentGeolocation, json_str)


class ChatMessageContentStatusConversationTitle(core.BunqModel):
    """
    :type title: str
    """

    def __init__(self):
        self.title = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.title is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageContentStatusConversationTitle
        """

        return converter.json_to_class(ChatMessageContentStatusConversationTitle, json_str)


class ChatMessageContentStatusConversation(core.BunqModel):
    """
    :type action: str
    """

    def __init__(self):
        self.action = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.action is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageContentStatusConversation
        """

        return converter.json_to_class(ChatMessageContentStatusConversation, json_str)


class ChatMessageContentStatusMembership(core.BunqModel):
    """
    :type action: str
    :type member: LabelUser
    """

    def __init__(self):
        self.action = None
        self.member = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.action is not None:
            return False

        if self.member is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageContentStatusMembership
        """

        return converter.json_to_class(ChatMessageContentStatusMembership, json_str)


class ChatMessageContentText(core.BunqModel):
    """
    :type text: str
    """

    def __init__(self):
        self.text = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.text is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageContentText
        """

        return converter.json_to_class(ChatMessageContentText, json_str)


class BunqMeMerchantAvailable(core.BunqModel):
    """
    :type merchant_type: str
    :type available: bool
    """

    def __init__(self):
        self.merchant_type = None
        self.available = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.merchant_type is not None:
            return False

        if self.available is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BunqMeMerchantAvailable
        """

        return converter.json_to_class(BunqMeMerchantAvailable, json_str)


class CardMagStripePermission(core.BunqModel):
    """
    :type expiry_time: str
    """

    def __init__(self):
        self.expiry_time = None


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.expiry_time is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardMagStripePermission
        """

        return converter.json_to_class(CardMagStripePermission, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.notification_delivery_method is not None:
            return False

        if self.notification_target is not None:
            return False

        if self.category is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: NotificationFilter
        """

        return converter.json_to_class(NotificationFilter, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.language is not None:
            return False

        if self.description is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabTextWaitingScreen
        """

        return converter.json_to_class(TabTextWaitingScreen, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.cash_register_qr_code is not None:
            return False

        if self.tab_qr_code is not None:
            return False

        if self.location is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabVisibility
        """

        return converter.json_to_class(TabVisibility, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.uuid is not None:
            return False

        if self.description is not None:
            return False

        if self.content_type is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentPublic
        """

        return converter.json_to_class(AttachmentPublic, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.id_ is not None:
            return False

        if self.description is not None:
            return False

        if self.content_type is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentTab
        """

        return converter.json_to_class(AttachmentTab, json_str)


class Certificate(core.BunqModel):
    """
    :type certificate: str
    """

    def __init__(self, certificate):
        """
        :type certificate: str
        """

        self.certificate = certificate


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.certificate is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Certificate
        """

        return converter.json_to_class(Certificate, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.share_detail is not None:
            return False

        if self.start_date is not None:
            return False

        if self.end_date is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftShareInviteBankEntry
        """

        return converter.json_to_class(DraftShareInviteBankEntry, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.status is not None:
            return False

        if self.balance_preferred is not None:
            return False

        if self.balance_threshold_low is not None:
            return False

        if self.method_fill is not None:
            return False

        if self.issuer is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccountProfileFill
        """

        return converter.json_to_class(MonetaryAccountProfileFill, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.bic is not None:
            return False

        if self.name is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Issuer
        """

        return converter.json_to_class(Issuer, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.status is not None:
            return False

        if self.balance_preferred is not None:
            return False

        if self.balance_threshold_high is not None:
            return False

        if self.savings_account_alias is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccountProfileDrain
        """

        return converter.json_to_class(MonetaryAccountProfileDrain, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.color is not None:
            return False

        if self.default_avatar_status is not None:
            return False

        if self.restriction_chat is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccountSetting
        """

        return converter.json_to_class(MonetaryAccountSetting, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.target_url is not None:
            return False

        if self.category is not None:
            return False

        if self.event_type is not None:
            return False

        if self.object_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: NotificationUrl
        """

        return converter.json_to_class(NotificationUrl, json_str)


class NotificationAnchorObject(core.BunqModel, core.AnchoredObjectInterface):
    """
    :type BunqMeFundraiserResult: endpoint.BunqMeFundraiserResult
    :type BunqMeTab: endpoint.BunqMeTab
    :type BunqMeTabResultInquiry: endpoint.BunqMeTabResultInquiry
    :type BunqMeTabResultResponse: endpoint.BunqMeTabResultResponse
    :type ChatMessage: endpoint.ChatMessage
    :type DraftPayment: endpoint.DraftPayment
    :type IdealMerchantTransaction: endpoint.IdealMerchantTransaction
    :type Invoice: endpoint.Invoice
    :type MasterCardAction: endpoint.MasterCardAction
    :type MonetaryAccount: endpoint.MonetaryAccount
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
    :type User: endpoint.User
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."


    def __init__(self):
        self.BunqMeFundraiserResult = None
        self.BunqMeTab = None
        self.BunqMeTabResultInquiry = None
        self.BunqMeTabResultResponse = None
        self.ChatMessage = None
        self.DraftPayment = None
        self.IdealMerchantTransaction = None
        self.Invoice = None
        self.MasterCardAction = None
        self.MonetaryAccount = None
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
        self.User = None

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self.BunqMeFundraiserResult is not None:
            return self.BunqMeFundraiserResult

        if self.BunqMeTab is not None:
            return self.BunqMeTab

        if self.BunqMeTabResultInquiry is not None:
            return self.BunqMeTabResultInquiry

        if self.BunqMeTabResultResponse is not None:
            return self.BunqMeTabResultResponse

        if self.ChatMessage is not None:
            return self.ChatMessage

        if self.DraftPayment is not None:
            return self.DraftPayment

        if self.IdealMerchantTransaction is not None:
            return self.IdealMerchantTransaction

        if self.Invoice is not None:
            return self.Invoice

        if self.MasterCardAction is not None:
            return self.MasterCardAction

        if self.MonetaryAccount is not None:
            return self.MonetaryAccount

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

        if self.User is not None:
            return self.User

        raise exception.BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.BunqMeFundraiserResult is not None:
            return False

        if self.BunqMeTab is not None:
            return False

        if self.BunqMeTabResultInquiry is not None:
            return False

        if self.BunqMeTabResultResponse is not None:
            return False

        if self.ChatMessage is not None:
            return False

        if self.DraftPayment is not None:
            return False

        if self.IdealMerchantTransaction is not None:
            return False

        if self.Invoice is not None:
            return False

        if self.MasterCardAction is not None:
            return False

        if self.MonetaryAccount is not None:
            return False

        if self.Payment is not None:
            return False

        if self.PaymentBatch is not None:
            return False

        if self.RequestInquiry is not None:
            return False

        if self.RequestInquiryBatch is not None:
            return False

        if self.RequestResponse is not None:
            return False

        if self.ShareInviteBankInquiry is not None:
            return False

        if self.ShareInviteBankResponse is not None:
            return False

        if self.ScheduledPayment is not None:
            return False

        if self.ScheduledInstance is not None:
            return False

        if self.TabResultInquiry is not None:
            return False

        if self.TabResultResponse is not None:
            return False

        if self.User is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: NotificationAnchorObject
        """

        return converter.json_to_class(NotificationAnchorObject, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.country is not None:
            return False

        if self.tax_number is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TaxResident
        """

        return converter.json_to_class(TaxResident, json_str)


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


    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.name is not None:
            return False

        if self.date_of_birth is not None:
            return False

        if self.nationality is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Ubo
        """

        return converter.json_to_class(Ubo, json_str)


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

# -*- coding: utf-8 -*-
from bunq.sdk import exception
from bunq.sdk.json import converter
from bunq.sdk.model import core
from bunq.sdk.model.generated import endpoint


class InvoiceItemGroup(core.BunqModel):
    """
    :param type_: The type of the invoice item group.
    :type type_: str
    :param type_description: The description of the type of the invoice item
    group.
    :type type_description: str
    :param type_description_translated: The translated description of the type
    of the invoice item group.
    :type type_description_translated: str
    :param instance_description: The identifier of the invoice item group.
    :type instance_description: str
    :param product_vat_exclusive: The unit item price excluding VAT.
    :type product_vat_exclusive: Amount
    :param product_vat_inclusive: The unit item price including VAT.
    :type product_vat_inclusive: Amount
    :param item: The invoice items in the group.
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
    :param value: The amount formatted to two decimal places.
    :type value: str
    :param currency: The currency of the amount. It is an ISO 4217 formatted
    currency code.
    :type currency: str
    """

    def __init__(self, value=None, currency=None):
        """
        :param value: The amount formatted to two decimal places.
        :type value: str
        :param currency: The currency of the amount. It is an ISO 4217 formatted
        currency code.
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
    :param billing_date: The billing date of the item.
    :type billing_date: str
    :param type_description: The price description.
    :type type_description: str
    :param type_description_translated: The translated price description.
    :type type_description_translated: str
    :param unit_vat_exclusive: The unit item price excluding VAT.
    :type unit_vat_exclusive: Amount
    :param unit_vat_inclusive: The unit item price including VAT.
    :type unit_vat_inclusive: Amount
    :param vat: The VAT tax fraction.
    :type vat: float
    :param quantity: The number of items priced.
    :type quantity: float
    :param total_vat_exclusive: The item price excluding VAT.
    :type total_vat_exclusive: Amount
    :param total_vat_inclusive: The item price including VAT.
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
    :param iban: The IBAN of the monetary account.
    :type iban: str
    :param display_name: The name to display with this monetary account.
    :type display_name: str
    :param avatar: The avatar of the monetary account.
    :type avatar: Avatar
    :param label_user: The user this monetary account belongs to.
    :type label_user: LabelUser
    :param country: The country of the user. Formatted as a ISO 3166-1 alpha-2
    country code.
    :type country: str
    :param bunq_me: Bunq.me pointer with type and value.
    :type bunq_me: MonetaryAccountReference
    :param is_light: Whether or not the monetary account is light.
    :type is_light: bool
    :param swift_bic: The BIC used for a SWIFT payment.
    :type swift_bic: str
    :param swift_account_number: The account number used for a SWIFT payment.
    May or may not be an IBAN.
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
    :param uuid: The public UUID of the avatar.
    :type uuid: str
    :param anchor_uuid: The public UUID of object this avatar is anchored to.
    :type anchor_uuid: str
    :param image: The actual image information of this avatar.
    :type image: list[Image]
    """

    def __init__(self, uuid=None):
        """
        :param uuid: The public UUID of the avatar.
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
    :param attachment_public_uuid: The public UUID of the public attachment
    containing the image.
    :type attachment_public_uuid: str
    :param content_type: The content-type as a MIME filetype.
    :type content_type: str
    :param height: The image height in pixels.
    :type height: int
    :param width: The image width in pixels.
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
    :param uuid: The public UUID of the label-user.
    :type uuid: str
    :param display_name: The name to be displayed for this user, as it was given
    on the request.
    :type display_name: str
    :param country: The country of the user. 000 stands for "unknown"
    :type country: str
    :param avatar: The current avatar of the user.
    :type avatar: Avatar
    :param public_nick_name: The current nickname of the user.
    :type public_nick_name: str
    """

    def __init__(self, uuid, display_name, country):
        """
        :param uuid: The public UUID of the label-user.
        :type uuid: str
        :param display_name: The name to be displayed for this user, as it was given
        on the request.
        :type display_name: str
        :param country: The country of the user
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
    :param type_: The alias type, can be: EMAIL|PHONE_NUMBER|IBAN.
    :type type_: str
    :param value: The alias value.
    :type value: str
    :param name: The alias name.
    :type name: str
    """

    def __init__(self, type_=None, value=None, name=None):
        """
        :param type_: The alias type, can be: EMAIL|PHONE_NUMBER|IBAN.
        :type type_: str
        :param value: The alias value. Phone number are formatted conform E.123
        without spaces (e.g., +314211234567).
        :type value: str
        :param name: The alias name. Only required for IBANs.
        :type name: str
        """

        self.type_ = type_
        self.value = value
        self.name = name

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
    :param street: The street.
    :type street: str
    :param house_number: The house number.
    :type house_number: str
    :param po_box: The PO box.
    :type po_box: str
    :param postal_code: The postal code.
    :type postal_code: str
    :param city: The city.
    :type city: str
    :param country: The country as an ISO 3166-1 alpha-2 country code..
    :type country: str
    :param province: The province according to local standard.
    :type province: str
    """

    def __init__(self, street=None, house_number=None, postal_code=None,
                 city=None, country=None, po_box=None):
        """
        :param street: The street.
        :type street: str
        :param house_number: The house number.
        :type house_number: str
        :param postal_code: The postal code.
        :type postal_code: str
        :param city: The city.
        :type city: str
        :param country: The country as an ISO 3166-1 alpha-2 country code.
        :type country: str
        :param po_box: The PO box.
        :type po_box: str
        """

        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.po_box = po_box
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


class RequestInquiryReference(core.BunqModel):
    """
    :param type_: The type of request inquiry. Can be RequestInquiry or
    RequestInquiryBatch.
    :type type_: str
    :param id_: The id of the request inquiry (batch).
    :type id_: int
    """

    def __init__(self):
        self.type_ = None
        self.id_ = None

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.type_ is not None:
            return False

        if self.id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RequestInquiryReference
        """

        return converter.json_to_class(RequestInquiryReference, json_str)


class ChatMessageContent(core.BunqModel, core.AnchoredObjectInterface):
    """
    :param ChatMessageContentAnchorEvent: 
    :type ChatMessageContentAnchorEvent: ChatMessageContentAnchorEvent
    :param ChatMessageContentAttachment: 
    :type ChatMessageContentAttachment: ChatMessageContentAttachment
    :param ChatMessageContentGeolocation: 
    :type ChatMessageContentGeolocation: ChatMessageContentGeolocation
    :param ChatMessageContentStatusConversationTitle: 
    :type ChatMessageContentStatusConversationTitle:
    ChatMessageContentStatusConversationTitle
    :param ChatMessageContentStatusConversation: 
    :type ChatMessageContentStatusConversation:
    ChatMessageContentStatusConversation
    :param ChatMessageContentStatusMembership: 
    :type ChatMessageContentStatusMembership: ChatMessageContentStatusMembership
    :param ChatMessageContentText: 
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
    :param anchored_object: An anchored object. Can be one of: CardDebit,
    CardPinChange, CardResult, DraftPayment, IdealMerchantTransaction, Invoice,
    Payment, PaymentBatch, PromotionDisplay, RequestInquiryBatch,
    RequestInquiry, RequestResponse, ScheduledPaymentBatch, ScheduledPayment,
    ScheduledRequestInquiryBatch, ScheduledRequestInquiry, ScheduledInstance,
    ShareInviteBankInquiry, ShareInviteBankResponse, UserCredentialPasswordIp
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
    :param CardDebit: 
    :type CardDebit: endpoint.CardDebit
    :param CardPinChange: 
    :type CardPinChange: endpoint.CardPinChange
    :param CardResult: 
    :type CardResult: endpoint.CardResult
    :param DraftPayment: 
    :type DraftPayment: endpoint.DraftPayment
    :param IdealMerchantTransaction: 
    :type IdealMerchantTransaction: endpoint.IdealMerchantTransaction
    :param Invoice: 
    :type Invoice: endpoint.Invoice
    :param Payment: 
    :type Payment: endpoint.Payment
    :param PaymentBatch: 
    :type PaymentBatch: endpoint.PaymentBatch
    :param PromotionDisplay: 
    :type PromotionDisplay: endpoint.PromotionDisplay
    :param RequestInquiryBatch: 
    :type RequestInquiryBatch: endpoint.RequestInquiryBatch
    :param RequestInquiry: 
    :type RequestInquiry: endpoint.RequestInquiry
    :param RequestResponse: 
    :type RequestResponse: endpoint.RequestResponse
    :param ScheduledPaymentBatch: 
    :type ScheduledPaymentBatch: endpoint.SchedulePaymentBatch
    :param ScheduledPayment: 
    :type ScheduledPayment: endpoint.SchedulePayment
    :param ScheduledInstance: 
    :type ScheduledInstance: endpoint.ScheduleInstance
    :param ShareInviteBankInquiry: 
    :type ShareInviteBankInquiry: endpoint.ShareInviteBankInquiry
    :param ShareInviteBankResponse: 
    :type ShareInviteBankResponse: endpoint.ShareInviteBankResponse
    :param UserCredentialPasswordIp: 
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
    :param daily_limit: The daily limit amount.
    :type daily_limit: str
    :param currency: Currency for the daily limit.
    :type currency: str
    :param type_: The type of transaction for the limit. Can be CARD_LIMIT_ATM,
    CARD_LIMIT_CONTACTLESS, CARD_LIMIT_DIPPING or CARD_LIMIT_POS_ICC.
    :type type_: str
    :param id_: The id of the card limit entry.
    :type id_: int
    """

    def __init__(self, daily_limit=None, currency=None, type_=None):
        """
        :param daily_limit: The daily limit amount.
        :type daily_limit: str
        :param currency: Currency for the daily limit.
        :type currency: str
        :param type_: The type of transaction for the limit. Can be CARD_LIMIT_ATM,
        CARD_LIMIT_CONTACTLESS, CARD_LIMIT_DIPPING or CARD_LIMIT_POS_ICC.
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
    :param country: The country to allow transactions in (e.g. NL, DE).
    :type country: str
    :param expiry_time: Expiry time of this rule.
    :type expiry_time: str
    :param id_: The id of the card country permission entry.
    :type id_: int
    """

    def __init__(self, country=None, expiry_time=None):
        """
        :param country: The country to allow transactions in (e.g. NL, DE).
        :type country: str
        :param expiry_time: Expiry time of this rule.
        :type expiry_time: str
        """

        self.country = country
        self.expiry_time = expiry_time
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
    :param type_: PIN type. Can be PRIMARY, SECONDARY or TERTIARY
    :type type_: str
    :param pin_code: The 4 digit PIN to be assigned to this account.
    :type pin_code: str
    :param monetary_account_id: The ID of the monetary account to assign to this
    pin for the card.
    :type monetary_account_id: int
    """

    def __init__(self, type_=None, pin_code=None, monetary_account_id=None):
        """
        :param type_: PIN type. Can be PRIMARY, SECONDARY or TERTIARY
        :type type_: str
        :param pin_code: The 4 digit PIN to be assigned to this account.
        :type pin_code: str
        :param monetary_account_id: The ID of the monetary account to assign to this
        pin for the card.
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
    :param uuid: The public UUID.
    :type uuid: str
    :param type_: The type of the card.
    :type type_: str
    :param second_line: The second line on the card.
    :type second_line: str
    :param expiry_date: The date this card will expire.
    :type expiry_date: str
    :param status: The status of the card.
    :type status: str
    :param label_user: The owner of this card.
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
    :param status: The status with which was responded.
    :type status: str
    :param user_alias_created: The user that responded to the DraftPayment.
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
    :param amount: The amount of the payment.
    :type amount: Amount
    :param counterparty_alias: The LabelMonetaryAccount containing the public
    information of the other (counterparty) side of the DraftPayment.
    :type counterparty_alias: MonetaryAccountReference
    :param description: The description for the DraftPayment. Maximum 140
    characters for DraftPayments to external IBANs, 9000 characters for
    DraftPayments to only other bunq MonetaryAccounts.
    :type description: str
    :param merchant_reference: Optional data to be included with the Payment
    specific to the merchant.
    :type merchant_reference: str
    :param attachment: The Attachments attached to the DraftPayment.
    :type attachment: list[AttachmentMonetaryAccountPayment]
    :param id_: The id of the draft payment entry.
    :type id_: int
    :param alias: The LabelMonetaryAccount containing the public information of
    'this' (party) side of the DraftPayment.
    :type alias: MonetaryAccountReference
    :param type_: The type of the draft payment entry.
    :type type_: str
    """

    def __init__(self, amount=None, counterparty_alias=None, description=None,
                 merchant_reference=None, attachment=None):
        """
        :param amount: The amount of the payment.
        :type amount: Amount
        :param counterparty_alias: The Alias of the party we are transferring the
        money to. Can be an Alias of type EMAIL or PHONE_NUMBER (for bunq
        MonetaryAccounts or bunq.to payments) or IBAN (for external bank account).
        :type counterparty_alias: MonetaryAccountReference
        :param description: The description for the DraftPayment. Maximum 140
        characters for DraftPayments to external IBANs, 9000 characters for
        DraftPayments to only other bunq MonetaryAccounts. Field is required but can
        be an empty string.
        :type description: str
        :param merchant_reference: Optional data to be included with the Payment
        specific to the merchant.
        :type merchant_reference: str
        :param attachment: The Attachments to attach to the DraftPayment.
        :type attachment: list[AttachmentMonetaryAccountPayment]
        """

        self.amount = amount
        self.counterparty_alias = counterparty_alias
        self.description = description
        self.merchant_reference = merchant_reference
        self.attachment = attachment
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
    :param id_: The id of the attached Attachment.
    :type id_: int
    :param monetary_account_id: The id of the MonetaryAccount this Attachment is
    attached from.
    :type monetary_account_id: int
    """

    def __init__(self, id_):
        """
        :param id_: The id of the Attachment to attach to the MonetaryAccount.
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

        return converter.json_to_class(AttachmentMonetaryAccountPayment,
                                       json_str)


class DraftPaymentAnchorObject(core.BunqModel, core.AnchoredObjectInterface):
    """
    :param Payment: 
    :type Payment: endpoint.Payment
    :param PaymentBatch: 
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
    :param latitude: The latitude for a geolocation restriction.
    :type latitude: float
    :param longitude: The longitude for a geolocation restriction.
    :type longitude: float
    :param altitude: The altitude for a geolocation restriction.
    :type altitude: float
    :param radius: The radius for a geolocation restriction.
    :type radius: float
    """

    def __init__(self, latitude=None, longitude=None, altitude=None,
                 radius=None):
        """
        :param latitude: The latitude for a geolocation restriction.
        :type latitude: str
        :param longitude: The longitude for a geolocation restriction.
        :type longitude: str
        :param altitude: The altitude for a geolocation restriction.
        :type altitude: str
        :param radius: The radius for a geolocation restriction.
        :type radius: str
        """

        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.radius = radius

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
    :param id_: An integer ID of an object. Unique per object type.
    :type id_: int
    """

    def __init__(self, id_=None):
        """
        :param id_: An integer ID of an object. Unique per object type.
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


class RequestReferenceSplitTheBillAnchorObject(core.BunqModel,
                                               core.AnchoredObjectInterface):
    """
    :param BillingInvoice: 
    :type BillingInvoice: endpoint.Invoice
    :param DraftPayment: 
    :type DraftPayment: endpoint.DraftPayment
    :param MasterCardAction: 
    :type MasterCardAction: endpoint.MasterCardAction
    :param Payment: 
    :type Payment: endpoint.Payment
    :param PaymentBatch: 
    :type PaymentBatch: endpoint.PaymentBatch
    :param RequestResponse: 
    :type RequestResponse: endpoint.RequestResponse
    :param ScheduleInstance: 
    :type ScheduleInstance: endpoint.ScheduleInstance
    :param TabResultResponse: 
    :type TabResultResponse: endpoint.TabResultResponse
    :param WhitelistResult: 
    :type WhitelistResult: endpoint.WhitelistResult
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    def __init__(self):
        self.BillingInvoice = None
        self.DraftPayment = None
        self.MasterCardAction = None
        self.Payment = None
        self.PaymentBatch = None
        self.RequestResponse = None
        self.ScheduleInstance = None
        self.TabResultResponse = None
        self.WhitelistResult = None

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self.BillingInvoice is not None:
            return self.BillingInvoice

        if self.DraftPayment is not None:
            return self.DraftPayment

        if self.MasterCardAction is not None:
            return self.MasterCardAction

        if self.Payment is not None:
            return self.Payment

        if self.PaymentBatch is not None:
            return self.PaymentBatch

        if self.RequestResponse is not None:
            return self.RequestResponse

        if self.ScheduleInstance is not None:
            return self.ScheduleInstance

        if self.TabResultResponse is not None:
            return self.TabResultResponse

        if self.WhitelistResult is not None:
            return self.WhitelistResult

        raise exception.BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.BillingInvoice is not None:
            return False

        if self.DraftPayment is not None:
            return False

        if self.MasterCardAction is not None:
            return False

        if self.Payment is not None:
            return False

        if self.PaymentBatch is not None:
            return False

        if self.RequestResponse is not None:
            return False

        if self.ScheduleInstance is not None:
            return False

        if self.TabResultResponse is not None:
            return False

        if self.WhitelistResult is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RequestReferenceSplitTheBillAnchorObject
        """

        return converter.json_to_class(RequestReferenceSplitTheBillAnchorObject,
                                       json_str)


class Attachment(core.BunqModel):
    """
    :param description: The description of the attachment.
    :type description: str
    :param content_type: The content type of the attachment's file.
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


class Error(core.BunqModel):
    """
    :param error_description: The error description (in English).
    :type error_description: str
    :param error_description_translated: The error description (in the user
    language).
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


class ScheduleAnchorObject(core.BunqModel, core.AnchoredObjectInterface):
    """
    :param Payment: 
    :type Payment: endpoint.Payment
    :param PaymentBatch: 
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


class ScheduleInstanceAnchorObject(core.BunqModel,
                                   core.AnchoredObjectInterface):
    """
    :param Payment: 
    :type Payment: endpoint.Payment
    :param PaymentBatch: 
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


class SchedulePaymentEntry(core.BunqModel):
    """
    :param amount: The Amount transferred by the Payment. Will be negative for
    outgoing Payments and positive for incoming Payments (relative to the
    MonetaryAccount indicated by monetary_account_id).
    :type amount: Amount
    :param counterparty_alias: The LabelMonetaryAccount containing the public
    information of the other (counterparty) side of the Payment.
    :type counterparty_alias: MonetaryAccountReference
    :param description: The description for the Payment. Maximum 140 characters
    for Payments to external IBANs, 9000 characters for Payments to only other
    bunq MonetaryAccounts.
    :type description: str
    :param attachment: The Attachments attached to the Payment.
    :type attachment: list[AttachmentMonetaryAccountPayment]
    :param merchant_reference: Optional data included with the Payment specific
    to the merchant.
    :type merchant_reference: str
    :param allow_bunqto: Whether or not sending a bunq.to payment is allowed.
    Mandatory for publicApi.
    :type allow_bunqto: bool
    :param alias: The LabelMonetaryAccount containing the public information of
    'this' (party) side of the Payment.
    :type alias: MonetaryAccountReference
    """

    def __init__(self, amount=None, counterparty_alias=None, description=None,
                 attachment=None, merchant_reference=None, allow_bunqto=None):
        """
        :param amount: The Amount to transfer with the Payment. Must be bigger 0 and
        smaller than the MonetaryAccount's balance.
        :type amount: Amount
        :param counterparty_alias: The Alias of the party we are transferring the
        money to. Can be an Alias of type EMAIL or PHONE (for bunq MonetaryAccounts)
        or IBAN (for external bank account).
        :type counterparty_alias: MonetaryAccountReference
        :param description: The description for the Payment. Maximum 140 characters
        for Payments to external IBANs, 9000 characters for Payments to only other
        bunq MonetaryAccounts. Field is required but can be an empty string.
        :type description: str
        :param attachment: The Attachments to attach to the Payment.
        :type attachment: list[BunqId]
        :param merchant_reference: Optional data to be included with the Payment
        specific to the merchant.
        :type merchant_reference: str
        :param allow_bunqto: Whether or not sending a bunq.to payment is allowed.
        Mandatory for publicApi.
        :type allow_bunqto: bool
        """

        self.amount = amount
        self.counterparty_alias = counterparty_alias
        self.description = description
        self.attachment = attachment
        self.merchant_reference = merchant_reference
        self.allow_bunqto = allow_bunqto
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


class ShareDetail(core.BunqModel):
    """
    :param payment: The share details for a payment share. In the response
    'payment' is replaced by 'ShareDetailPayment'.
    :type payment: ShareDetailPayment
    :param read_only: The share details for viewing a share. In the response
    'read_only' is replaced by 'ShareDetailReadOnly'.
    :type read_only: ShareDetailReadOnly
    :param draft_payment: The share details for a draft payment share. Remember
    to replace 'draft_payment' with 'ShareDetailDraftPayment' before sending a
    request.
    :type draft_payment: ShareDetailDraftPayment
    """

    def __init__(self, payment=None, read_only=None, draft_payment=None):
        """
        :param payment: The share details for a payment share. Remember to replace
        'payment' with 'ShareDetailPayment' before sending a request.
        :type payment: ShareDetailPayment
        :param read_only: The share details for viewing a share. Remember to replace
        'read_only' with 'ShareDetailReadOnly' before sending a request.
        :type read_only: ShareDetailReadOnly
        :param draft_payment: The share details for a draft payment share. Remember
        to replace 'draft_payment' with 'ShareDetailDraftPayment' before sending a
        request.
        :type draft_payment: ShareDetailDraftPayment
        """

        self.payment = payment
        self.read_only = read_only
        self.draft_payment = draft_payment

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
    :param make_payments: If set to true, the invited user will be able to make
    payments from the shared account.
    :type make_payments: bool
    :param make_draft_payments: If set to true, the invited user will be able to
    make draft payments from the shared account.
    :type make_draft_payments: bool
    :param view_balance: If set to true, the invited user will be able to view
    the account balance.
    :type view_balance: bool
    :param view_old_events: If set to true, the invited user will be able to
    view events from before the share was active.
    :type view_old_events: bool
    :param view_new_events: If set to true, the invited user will be able to
    view events starting from the time the share became active.
    :type view_new_events: bool
    :param budget: The budget restriction.
    :type budget: BudgetRestriction
    """

    def __init__(self, make_payments=None, view_balance=None,
                 view_old_events=None, view_new_events=None,
                 make_draft_payments=None, budget=None):
        """
        :param make_payments: If set to true, the invited user will be able to make
        payments from the shared account.
        :type make_payments: bool
        :param view_balance: If set to true, the invited user will be able to view
        the account balance.
        :type view_balance: bool
        :param view_old_events: If set to true, the invited user will be able to
        view events from before the share was active.
        :type view_old_events: bool
        :param view_new_events: If set to true, the invited user will be able to
        view events starting from the time the share became active.
        :type view_new_events: bool
        :param make_draft_payments: If set to true, the invited user will be able to
        make draft payments from the shared account.
        :type make_draft_payments: bool
        :param budget: The budget restriction.
        :type budget: BudgetRestriction
        """

        self.make_payments = make_payments
        self.view_balance = view_balance
        self.view_old_events = view_old_events
        self.view_new_events = view_new_events
        self.make_draft_payments = make_draft_payments
        self.budget = budget

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
    :param amount: The amount of the budget given to the invited user.
    :type amount: Amount
    :param frequency: The duration for a budget restriction. Valid values are
    DAILY, WEEKLY, MONTHLY, YEARLY.
    :type frequency: str
    """

    def __init__(self, amount=None, frequency=None):
        """
        :param amount: The amount of the budget given to the invited user.
        :type amount: Amount
        :param frequency: The duration for a budget restriction. Valid values are
        DAILY, WEEKLY, MONTHLY, YEARLY.
        :type frequency: str
        """

        self.amount = amount
        self.frequency = frequency

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
    :param view_balance: If set to true, the invited user will be able to view
    the account balance.
    :type view_balance: bool
    :param view_old_events: If set to true, the invited user will be able to
    view events from before the share was active.
    :type view_old_events: bool
    :param view_new_events: If set to true, the invited user will be able to
    view events starting from the time the share became active.
    :type view_new_events: bool
    """

    def __init__(self, view_balance=None, view_old_events=None,
                 view_new_events=None):
        """
        :param view_balance: If set to true, the invited user will be able to view
        the account balance.
        :type view_balance: bool
        :param view_old_events: If set to true, the invited user will be able to
        view events from before the share was active.
        :type view_old_events: bool
        :param view_new_events: If set to true, the invited user will be able to
        view events starting from the time the share became active.
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
    :param make_draft_payments: If set to true, the invited user will be able to
    make draft payments from the shared account.
    :type make_draft_payments: bool
    :param view_balance: If set to true, the invited user will be able to view
    the account balance.
    :type view_balance: bool
    :param view_old_events: If set to true, the invited user will be able to
    view events from before the share was active.
    :type view_old_events: bool
    :param view_new_events: If set to true, the invited user will be able to
    view events starting from the time the share became active.
    :type view_new_events: bool
    """

    def __init__(self, make_draft_payments=None, view_balance=None,
                 view_old_events=None, view_new_events=None):
        """
        :param make_draft_payments: If set to true, the invited user will be able to
        make draft payments from the shared account.
        :type make_draft_payments: bool
        :param view_balance: If set to true, the invited user will be able to view
        the account balance.
        :type view_balance: bool
        :param view_old_events: If set to true, the invited user will be able to
        view events from before the share was active.
        :type view_old_events: bool
        :param view_new_events: If set to true, the invited user will be able to
        view events starting from the time the share became active.
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
    :param description: The description of the device that may use the
    credential.
    :type description: str
    :param ip: The IP address of the device that may use the credential.
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
    :param attachment: An attachment.
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
    :param geolocation: A geolocation, using WGS 84 coordinates.
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
    :param title: The new title of a conversation.
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

        return converter.json_to_class(
            ChatMessageContentStatusConversationTitle, json_str)


class ChatMessageContentStatusConversation(core.BunqModel):
    """
    :param action: Action which occurred over a conversation. Always
    CONVERSATION_CREATED
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

        return converter.json_to_class(ChatMessageContentStatusConversation,
                                       json_str)


class ChatMessageContentStatusMembership(core.BunqModel):
    """
    :param action: Action which occurred over a member. Could be MEMBER_ADDED or
    MEMBER_REMOVED
    :type action: str
    :param member: The member over which the action has occurred.
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

        return converter.json_to_class(ChatMessageContentStatusMembership,
                                       json_str)


class ChatMessageContentText(core.BunqModel):
    """
    :param text: The text of the message.
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
    :param merchant_type: A merchant type supported by bunq.me.
    :type merchant_type: str
    :param available: Whether or not the merchant is available for the user.
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
    :param expiry_time: Expiry time of this rule.
    :type expiry_time: str
    """

    def __init__(self, expiry_time=None):
        """
        :param expiry_time: Expiry time of this rule.
        :type expiry_time: str
        """

        self.expiry_time = expiry_time

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
    :param notification_delivery_method: The delivery method via which
    notifications that match this notification filter will be delivered.
    Possible choices are PUSH for delivery via push notification and URL for
    delivery via URL callback.
    :type notification_delivery_method: str
    :param notification_target: The target of notifications that match this
    notification filter. For URL notification filters this is the URL to which
    the callback will be made. For PUSH notifications filters this should always
    be null.
    :type notification_target: str
    :param category: The notification category that will match this notification
    filter. Possible choices are BILLING, CARD_TRANSACTION_FAILED,
    CARD_TRANSACTION_SUCCESSFUL, CHAT, DRAFT_PAYMENT, IDEAL, SOFORT,
    MONETARY_ACCOUNT_PROFILE, MUTATION, PAYMENT, PROMOTION, REQUEST,
    SCHEDULE_RESULT, SCHEDULE_STATUS, SHARE, SUPPORT, TAB_RESULT, USER_APPROVAL.
    :type category: str
    """

    def __init__(self, notification_delivery_method=None,
                 notification_target=None, category=None):
        """
        :param notification_delivery_method: The delivery method via which
        notifications that match this notification filter will be delivered.
        Possible choices are PUSH for delivery via push notification and URL for
        delivery via URL callback.
        :type notification_delivery_method: str
        :param notification_target: The target of notifications that match this
        notification filter. For URL notification filters this is the URL to which
        the callback will be made. For PUSH notifications filters this should always
        be null.
        :type notification_target: str
        :param category: The notification category that will match this notification
        filter. Possible choices are BILLING, CARD_TRANSACTION_FAILED,
        CARD_TRANSACTION_SUCCESSFUL, CHAT, DRAFT_PAYMENT, IDEAL, SOFORT,
        MONETARY_ACCOUNT_PROFILE, MUTATION, PAYMENT, PROMOTION, REQUEST,
        SCHEDULE_RESULT, SCHEDULE_STATUS, SHARE, SUPPORT, TAB_RESULT, USER_APPROVAL.
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
    :param language: Language of tab text
    :type language: str
    :param description: Tab text
    :type description: str
    """

    def __init__(self, language=None, description=None):
        """
        :param language: Language of tab text
        :type language: str
        :param description: Tab text
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


class Certificate(core.BunqModel):
    """
    :param certificate: A single certificate in the chain in .PEM format.
    :type certificate: str
    """

    def __init__(self, certificate):
        """
        :param certificate: A single certificate in the chain in .PEM format.
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


class DraftShareInviteEntry(core.BunqModel):
    """
    :param share_detail: The share details. Only one of these objects is
    returned.
    :type share_detail: ShareDetail
    :param start_date: The start date of this share.
    :type start_date: str
    :param end_date: The expiration date of this share.
    :type end_date: str
    """

    def __init__(self, share_detail=None, start_date=None, end_date=None):
        """
        :param share_detail: The share details. Only one of these objects may be
        passed.
        :type share_detail: ShareDetail
        :param start_date: The start date of this share.
        :type start_date: str
        :param end_date: The expiration date of this share.
        :type end_date: str
        """

        self.share_detail = share_detail
        self.start_date = start_date
        self.end_date = end_date

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
        
        :rtype: DraftShareInviteEntry
        """

        return converter.json_to_class(DraftShareInviteEntry, json_str)


class MonetaryAccountProfileFill(core.BunqModel):
    """
    :param status: The status of the profile.
    :type status: str
    :param balance_preferred: The goal balance.
    :type balance_preferred: Amount
    :param balance_threshold_low: The low threshold balance.
    :type balance_threshold_low: Amount
    :param method_fill: The method used to fill the monetary account. Currently
    only iDEAL is supported, and it is the default one.
    :type method_fill: str
    :param issuer: The bank the fill is supposed to happen from, with BIC and
    bank name.
    :type issuer: Issuer
    """

    def __init__(self, status, balance_preferred, balance_threshold_low,
                 method_fill, issuer=None):
        """
        :param status: The status of the profile.
        :type status: str
        :param balance_preferred: The goal balance.
        :type balance_preferred: Amount
        :param balance_threshold_low: The low threshold balance.
        :type balance_threshold_low: Amount
        :param method_fill: The method used to fill the monetary account. Currently
        IDEAL and SOFORT is supported.
        :type method_fill: str
        :param issuer: The bank the fill is supposed to happen from, with BIC and
        bank name.
        :type issuer: Issuer
        """

        self.status = status
        self.balance_preferred = balance_preferred
        self.balance_threshold_low = balance_threshold_low
        self.method_fill = method_fill
        self.issuer = issuer

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
    :param bic: The BIC code.
    :type bic: str
    :param name: The name of the bank.
    :type name: str
    """

    def __init__(self, bic, name=None):
        """
        :param bic: The BIC code.
        :type bic: str
        :param name: The name of the bank.
        :type name: str
        """

        self.bic = bic
        self.name = name

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
    :param status: The status of the profile.
    :type status: str
    :param balance_preferred: The goal balance.
    :type balance_preferred: Amount
    :param balance_threshold_high: The high threshold balance.
    :type balance_threshold_high: Amount
    :param savings_account_alias: The savings monetary account.
    :type savings_account_alias: MonetaryAccountReference
    """

    def __init__(self, status, balance_preferred, balance_threshold_high,
                 savings_account_alias):
        """
        :param status: The status of the profile.
        :type status: str
        :param balance_preferred: The goal balance.
        :type balance_preferred: Amount
        :param balance_threshold_high: The high threshold balance.
        :type balance_threshold_high: Amount
        :param savings_account_alias: The savings monetary account.
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
    :param color: The color chosen for the MonetaryAccount.
    :type color: str
    :param default_avatar_status: The status of the avatar. Can be either
    AVATAR_DEFAULT, AVATAR_CUSTOM or AVATAR_UNDETERMINED.
    :type default_avatar_status: str
    :param restriction_chat: The chat restriction. Possible values are
    ALLOW_INCOMING or BLOCK_INCOMING
    :type restriction_chat: str
    """

    def __init__(self, color=None, default_avatar_status=None,
                 restriction_chat=None):
        """
        :param color: The color chosen for the MonetaryAccount in hexadecimal
        format.
        :type color: str
        :param default_avatar_status: The status of the avatar. Cannot be updated
        directly.
        :type default_avatar_status: str
        :param restriction_chat: The chat restriction. Possible values are
        ALLOW_INCOMING or BLOCK_INCOMING
        :type restriction_chat: str
        """

        self.color = color
        self.default_avatar_status = default_avatar_status
        self.restriction_chat = restriction_chat

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


class CoOwner(core.BunqModel):
    """
    :param alias: The Alias of the co-owner.
    :type alias: list[LabelUser]
    :param status: Can be: ACCEPTED, REJECTED, PENDING or REVOKED
    :type status: str
    """

    def __init__(self, alias):
        """
        :param alias: The users the account will be joint with.
        :type alias: MonetaryAccountReference
        """

        self.alias = alias
        self.status = None

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self.alias is not None:
            return False

        if self.status is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CoOwner
        """

        return converter.json_to_class(CoOwner, json_str)


class NotificationUrl(core.BunqModel):
    """
    :param target_url: 
    :type target_url: str
    :param category: 
    :type category: str
    :param event_type: 
    :type event_type: str
    :param object_: 
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
    :param BunqMeFundraiserResult: 
    :type BunqMeFundraiserResult: endpoint.BunqMeFundraiserResult
    :param BunqMeTab: 
    :type BunqMeTab: endpoint.BunqMeTab
    :param BunqMeTabResultInquiry: 
    :type BunqMeTabResultInquiry: endpoint.BunqMeTabResultInquiry
    :param BunqMeTabResultResponse: 
    :type BunqMeTabResultResponse: endpoint.BunqMeTabResultResponse
    :param ChatMessage: 
    :type ChatMessage: endpoint.ChatMessage
    :param DraftPayment: 
    :type DraftPayment: endpoint.DraftPayment
    :param IdealMerchantTransaction: 
    :type IdealMerchantTransaction: endpoint.IdealMerchantTransaction
    :param Invoice: 
    :type Invoice: endpoint.Invoice
    :param MasterCardAction: 
    :type MasterCardAction: endpoint.MasterCardAction
    :param MonetaryAccount: 
    :type MonetaryAccount: endpoint.MonetaryAccount
    :param Payment: 
    :type Payment: endpoint.Payment
    :param PaymentBatch: 
    :type PaymentBatch: endpoint.PaymentBatch
    :param RequestInquiry: 
    :type RequestInquiry: endpoint.RequestInquiry
    :param RequestInquiryBatch: 
    :type RequestInquiryBatch: endpoint.RequestInquiryBatch
    :param RequestResponse: 
    :type RequestResponse: endpoint.RequestResponse
    :param ShareInviteBankInquiry: 
    :type ShareInviteBankInquiry: endpoint.ShareInviteBankInquiry
    :param ShareInviteBankResponse: 
    :type ShareInviteBankResponse: endpoint.ShareInviteBankResponse
    :param ScheduledPayment: 
    :type ScheduledPayment: endpoint.SchedulePayment
    :param ScheduledInstance: 
    :type ScheduledInstance: endpoint.ScheduleInstance
    :param TabResultInquiry: 
    :type TabResultInquiry: endpoint.TabResultInquiry
    :param TabResultResponse: 
    :type TabResultResponse: endpoint.TabResultResponse
    :param User: 
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


class AttachmentPublic(core.BunqModel):
    """
    :param uuid: The uuid of the attachment.
    :type uuid: str
    :param description: The description of the attachment.
    :type description: str
    :param content_type: The content type of the attachment's file.
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


class TaxResident(core.BunqModel):
    """
    :param country: The country of the tax number.
    :type country: str
    :param tax_number: The tax number.
    :type tax_number: str
    """

    def __init__(self, country=None, tax_number=None):
        """
        :param country: The country of the tax number.
        :type country: str
        :param tax_number: The tax number.
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
    :param name: The name of the ultimate beneficiary owner.
    :type name: str
    :param date_of_birth: The date of birth of the ultimate beneficiary owner.
    :type date_of_birth: str
    :param nationality: The nationality of the ultimate beneficiary owner.
    :type nationality: str
    """

    def __init__(self, name=None, date_of_birth=None, nationality=None):
        """
        :param name: The name of the ultimate beneficiary owner.
        :type name: str
        :param date_of_birth: The date of birth of the ultimate beneficiary owner.
        Accepts ISO8601 date formats.
        :type date_of_birth: str
        :param nationality: The nationality of the ultimate beneficiary owner.
        Accepts ISO8601 date formats.
        :type nationality: str
        """

        self.name = name
        self.date_of_birth = date_of_birth
        self.nationality = nationality

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


class AttachmentTab(core.BunqModel):
    """
    :param id_: The id of the attachment.
    :type id_: int
    :param description: The description of the attachment.
    :type description: str
    :param content_type: The content type of the attachment's file.
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


class TabVisibility(core.BunqModel):
    """
    :param cash_register_qr_code: When true the tab will be linked to the ACTIVE
    cash registers QR code.
    :type cash_register_qr_code: bool
    :param tab_qr_code: When true the tab will be visible through its own QR
    code. Use ../tab/{tab-id}/qr-code-content to get the raw content of this QR
    code
    :type tab_qr_code: bool
    :param location: The location of the Tab in NearPay.
    :type location: Geolocation
    """

    def __init__(self, cash_register_qr_code=None, tab_qr_code=None,
                 location=None):
        """
        :param cash_register_qr_code: When true the Tab will be linked to the ACTIVE
        cash registers QR code. If no cash register QR code exists, one will be
        created.
        :type cash_register_qr_code: bool
        :param tab_qr_code: When true the Tab will be visible through its own QR
        code. Use ../tab/{tab-id}/qr-code-content to get the raw content of this QR
        code
        :type tab_qr_code: bool
        :param location: The location on which this tab will be made visible in
        NearPay. This location must overlap with the location of the CashRegister.
        If no location is provided the location of the CashRegister will be used.
        :type location: Geolocation
        """

        self.cash_register_qr_code = cash_register_qr_code
        self.tab_qr_code = tab_qr_code
        self.location = location

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

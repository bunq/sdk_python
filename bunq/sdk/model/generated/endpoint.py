# -*- coding: utf-8 -*-
from bunq.sdk import client
from bunq.sdk import context
from bunq.sdk import exception
from bunq.sdk import security
from bunq.sdk.json import converter
from bunq.sdk.model import core
from bunq.sdk.model.generated import object_


class Invoice(core.BunqModel):
    """
    Used to view a bunq invoice.
    
    :param _id_: The id of the invoice object.
    :type _id_: int
    :param _created: The timestamp of the invoice object's creation.
    :type _created: str
    :param _updated: The timestamp of the invoice object's last update.
    :type _updated: str
    :param _invoice_date: The invoice date.
    :type _invoice_date: str
    :param _invoice_number: The invoice number.
    :type _invoice_number: str
    :param _status: The invoice status.
    :type _status: str
    :param _group: The invoice item groups.
    :type _group: list[object_.InvoiceItemGroup]
    :param _total_vat_inclusive: The total discounted item price including VAT.
    :type _total_vat_inclusive: object_.Amount
    :param _total_vat_exclusive: The total discounted item price excluding VAT.
    :type _total_vat_exclusive: object_.Amount
    :param _total_vat: The VAT on the total discounted item price.
    :type _total_vat: object_.Amount
    :param _alias: The label that's displayed to the counterparty with the
    invoice. Includes user.
    :type _alias: object_.MonetaryAccountReference
    :param _address: The customer's address.
    :type _address: object_.Address
    :param _counterparty_alias: The label of the counterparty of the invoice.
    Includes user.
    :type _counterparty_alias: object_.MonetaryAccountReference
    :param _counterparty_address: The company's address.
    :type _counterparty_address: object_.Address
    :param _chamber_of_commerce_number: The company's chamber of commerce
    number.
    :type _chamber_of_commerce_number: str
    :param _vat_number: The company's chamber of commerce number.
    :type _vat_number: str
    :param _request_reference_split_the_bill: The reference to the object used
    for split the bill. Can be RequestInquiry or RequestInquiryBatch
    :type _request_reference_split_the_bill:
    list[object_.RequestInquiryReference]
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/invoice"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/invoice/{}"

    # Field constants.
    FIELD_STATUS = "status"
    FIELD_DESCRIPTION = "description"
    FIELD_EXTERNAL_URL = "external_url"

    # Object type.
    _OBJECT_TYPE_GET = "Invoice"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._invoice_date = None
        self._invoice_number = None
        self._status = None
        self._group = None
        self._total_vat_inclusive = None
        self._total_vat_exclusive = None
        self._total_vat = None
        self._alias = None
        self._address = None
        self._counterparty_alias = None
        self._counterparty_address = None
        self._chamber_of_commerce_number = None
        self._vat_number = None
        self._request_reference_split_the_bill = None

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInvoiceList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseInvoiceList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def get(cls, invoice_id, monetary_account_id=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type invoice_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInvoice
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     invoice_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseInvoice.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def invoice_date(self):
        """
        :rtype: str
        """

        return self._invoice_date

    @property
    def invoice_number(self):
        """
        :rtype: str
        """

        return self._invoice_number

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def group(self):
        """
        :rtype: list[object_.InvoiceItemGroup]
        """

        return self._group

    @property
    def total_vat_inclusive(self):
        """
        :rtype: object_.Amount
        """

        return self._total_vat_inclusive

    @property
    def total_vat_exclusive(self):
        """
        :rtype: object_.Amount
        """

        return self._total_vat_exclusive

    @property
    def total_vat(self):
        """
        :rtype: object_.Amount
        """

        return self._total_vat

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def address(self):
        """
        :rtype: object_.Address
        """

        return self._address

    @property
    def counterparty_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counterparty_alias

    @property
    def counterparty_address(self):
        """
        :rtype: object_.Address
        """

        return self._counterparty_address

    @property
    def chamber_of_commerce_number(self):
        """
        :rtype: str
        """

        return self._chamber_of_commerce_number

    @property
    def vat_number(self):
        """
        :rtype: str
        """

        return self._vat_number

    @property
    def request_reference_split_the_bill(self):
        """
        :rtype: list[object_.RequestInquiryReference]
        """

        return self._request_reference_split_the_bill

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._invoice_date is not None:
            return False

        if self._invoice_number is not None:
            return False

        if self._status is not None:
            return False

        if self._group is not None:
            return False

        if self._total_vat_inclusive is not None:
            return False

        if self._total_vat_exclusive is not None:
            return False

        if self._total_vat is not None:
            return False

        if self._alias is not None:
            return False

        if self._address is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._counterparty_address is not None:
            return False

        if self._chamber_of_commerce_number is not None:
            return False

        if self._vat_number is not None:
            return False

        if self._request_reference_split_the_bill is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Invoice
        """

        return converter.json_to_class(Invoice, json_str)


class InvoiceByUser(core.BunqModel):
    """
    Used to list bunq invoices by user.
    
    :param _id_: The id of the invoice object.
    :type _id_: int
    :param _created: The timestamp of the invoice object's creation.
    :type _created: str
    :param _updated: The timestamp of the invoice object's last update.
    :type _updated: str
    :param _invoice_date: The invoice date.
    :type _invoice_date: str
    :param _invoice_number: The invoice number.
    :type _invoice_number: str
    :param _status: The invoice status.
    :type _status: str
    :param _group: The invoice item groups.
    :type _group: list[object_.InvoiceItemGroup]
    :param _total_vat_inclusive: The total discounted item price including VAT.
    :type _total_vat_inclusive: object_.Amount
    :param _total_vat_exclusive: The total discounted item price excluding VAT.
    :type _total_vat_exclusive: object_.Amount
    :param _total_vat: The VAT on the total discounted item price.
    :type _total_vat: object_.Amount
    :param _alias: The label that's displayed to the counterparty with the
    invoice. Includes user.
    :type _alias: object_.MonetaryAccountReference
    :param _address: The customer's address.
    :type _address: object_.Address
    :param _counterparty_alias: The label of the counterparty of the invoice.
    Includes user.
    :type _counterparty_alias: object_.MonetaryAccountReference
    :param _counterparty_address: The company's address.
    :type _counterparty_address: object_.Address
    :param _chamber_of_commerce_number: The company's chamber of commerce
    number.
    :type _chamber_of_commerce_number: str
    :param _vat_number: The company's chamber of commerce number.
    :type _vat_number: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/invoice"
    _ENDPOINT_URL_READ = "user/{}/invoice/{}"

    # Object type.
    _OBJECT_TYPE_GET = "Invoice"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._invoice_date = None
        self._invoice_number = None
        self._status = None
        self._group = None
        self._total_vat_inclusive = None
        self._total_vat_exclusive = None
        self._total_vat = None
        self._alias = None
        self._address = None
        self._counterparty_alias = None
        self._counterparty_address = None
        self._chamber_of_commerce_number = None
        self._vat_number = None

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInvoiceByUserList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseInvoiceByUserList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def get(cls, invoice_by_user_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type invoice_by_user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInvoiceByUser
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     invoice_by_user_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseInvoiceByUser.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def invoice_date(self):
        """
        :rtype: str
        """

        return self._invoice_date

    @property
    def invoice_number(self):
        """
        :rtype: str
        """

        return self._invoice_number

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def group(self):
        """
        :rtype: list[object_.InvoiceItemGroup]
        """

        return self._group

    @property
    def total_vat_inclusive(self):
        """
        :rtype: object_.Amount
        """

        return self._total_vat_inclusive

    @property
    def total_vat_exclusive(self):
        """
        :rtype: object_.Amount
        """

        return self._total_vat_exclusive

    @property
    def total_vat(self):
        """
        :rtype: object_.Amount
        """

        return self._total_vat

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def address(self):
        """
        :rtype: object_.Address
        """

        return self._address

    @property
    def counterparty_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counterparty_alias

    @property
    def counterparty_address(self):
        """
        :rtype: object_.Address
        """

        return self._counterparty_address

    @property
    def chamber_of_commerce_number(self):
        """
        :rtype: str
        """

        return self._chamber_of_commerce_number

    @property
    def vat_number(self):
        """
        :rtype: str
        """

        return self._vat_number

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._invoice_date is not None:
            return False

        if self._invoice_number is not None:
            return False

        if self._status is not None:
            return False

        if self._group is not None:
            return False

        if self._total_vat_inclusive is not None:
            return False

        if self._total_vat_exclusive is not None:
            return False

        if self._total_vat is not None:
            return False

        if self._alias is not None:
            return False

        if self._address is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._counterparty_address is not None:
            return False

        if self._chamber_of_commerce_number is not None:
            return False

        if self._vat_number is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: InvoiceByUser
        """

        return converter.json_to_class(InvoiceByUser, json_str)


class ChatConversation(core.BunqModel, core.AnchoredObjectInterface):
    """
    Manages user's conversations.
    
    :param _SupportConversationExternal: 
    :type _SupportConversationExternal: ChatConversationSupportExternal
    :param _ChatConversationReference: 
    :type _ChatConversationReference: ChatConversationReference
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/chat-conversation"
    _ENDPOINT_URL_READ = "user/{}/chat-conversation/{}"

    # Object type.
    _OBJECT_TYPE_GET = "ChatConversation"

    def __init__(self):
        self._SupportConversationExternal = None
        self._ChatConversationReference = None

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseChatConversationList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseChatConversationList.cast_from_bunq_response(
            cls._from_json_list(response_raw)
        )

    @classmethod
    def get(cls, chat_conversation_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type chat_conversation_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseChatConversation
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     chat_conversation_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseChatConversation.cast_from_bunq_response(
            cls._from_json(response_raw)
        )

    @property
    def SupportConversationExternal(self):
        """
        :rtype: ChatConversationSupportExternal
        """

        return self._SupportConversationExternal

    @property
    def ChatConversationReference(self):
        """
        :rtype: ChatConversationReference
        """

        return self._ChatConversationReference

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self._SupportConversationExternal is not None:
            return self._SupportConversationExternal

        if self._ChatConversationReference is not None:
            return self._ChatConversationReference

        raise exception.BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._SupportConversationExternal is not None:
            return False

        if self._ChatConversationReference is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatConversation
        """

        return converter.json_to_class(ChatConversation, json_str)


class ChatConversationSupportExternal(core.BunqModel):
    """
    Manages user's support conversation.
    
    :param _id_: The id of this conversation.
    :type _id_: int
    :param _created: The timestamp of the support conversation's creation.
    :type _created: str
    :param _updated: The timestamp of the support conversation's last update.
    :type _updated: str
    :param _last_message: The last message posted to this conversation if any.
    :type _last_message: ChatMessage
    """

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._last_message = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def last_message(self):
        """
        :rtype: ChatMessage
        """

        return self._last_message

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._last_message is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatConversationSupportExternal
        """

        return converter.json_to_class(ChatConversationSupportExternal,
                                       json_str)


class ChatMessage(core.BunqModel, core.AnchoredObjectInterface):
    """
    Endpoint for retrieving the messages that are part of a conversation.
    
    :param _ChatMessageAnnouncement: 
    :type _ChatMessageAnnouncement: ChatMessageAnnouncement
    :param _ChatMessageStatus: 
    :type _ChatMessageStatus: ChatMessageStatus
    :param _ChatMessageUser: 
    :type _ChatMessageUser: ChatMessageUser
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/chat-conversation/{}/message"

    # Object type.
    _OBJECT_TYPE_GET = "ChatMessage"

    def __init__(self):
        self._ChatMessageAnnouncement = None
        self._ChatMessageStatus = None
        self._ChatMessageUser = None

    @classmethod
    def list(cls, chat_conversation_id, params=None, custom_headers=None):
        """
        Get all the messages that are part of a specific conversation.
        
        :type user_id: int
        :type chat_conversation_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseChatMessageList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(), chat_conversation_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseChatMessageList.cast_from_bunq_response(
            cls._from_json_list(response_raw)
        )

    @property
    def ChatMessageAnnouncement(self):
        """
        :rtype: ChatMessageAnnouncement
        """

        return self._ChatMessageAnnouncement

    @property
    def ChatMessageStatus(self):
        """
        :rtype: ChatMessageStatus
        """

        return self._ChatMessageStatus

    @property
    def ChatMessageUser(self):
        """
        :rtype: ChatMessageUser
        """

        return self._ChatMessageUser

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self._ChatMessageAnnouncement is not None:
            return self._ChatMessageAnnouncement

        if self._ChatMessageStatus is not None:
            return self._ChatMessageStatus

        if self._ChatMessageUser is not None:
            return self._ChatMessageUser

        raise exception.BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._ChatMessageAnnouncement is not None:
            return False

        if self._ChatMessageStatus is not None:
            return False

        if self._ChatMessageUser is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessage
        """

        return converter.json_to_class(ChatMessage, json_str)


class ChatMessageAnnouncement(core.BunqModel):
    """
    Endpoint for retrieving the messages that are part of a conversation.
    
    :param _id_: The id of the message.
    :type _id_: int
    :param _created: The timestamp when the message was created.
    :type _created: str
    :param _updated: The timestamp when the message was last updated.
    :type _updated: str
    :param _conversation_id: The id of the conversation this message belongs to.
    :type _conversation_id: int
    :param _creator: The user who initiated the action that caused this message
    to appear.
    :type _creator: object_.LabelUser
    :param _content: The content of this message.
    :type _content: object_.ChatMessageContent
    """

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._conversation_id = None
        self._creator = None
        self._content = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def conversation_id(self):
        """
        :rtype: int
        """

        return self._conversation_id

    @property
    def creator(self):
        """
        :rtype: object_.LabelUser
        """

        return self._creator

    @property
    def content(self):
        """
        :rtype: object_.ChatMessageContent
        """

        return self._content

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._conversation_id is not None:
            return False

        if self._creator is not None:
            return False

        if self._content is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageAnnouncement
        """

        return converter.json_to_class(ChatMessageAnnouncement, json_str)


class CardDebit(core.BunqModel):
    """
    With bunq it is possible to order debit cards that can then be connected
    with each one of the monetary accounts the user has access to (including
    connected accounts).
    
    :param _id_: The id of the card.
    :type _id_: int
    :param _created: The timestamp when the card was crated.
    :type _created: str
    :param _updated: The timestamp when the card was last updated.
    :type _updated: str
    :param _public_uuid: The public UUID of the card.
    :type _public_uuid: str
    :param _type_: The type of the card. Can be MAESTRO, MASTERCARD.
    :type _type_: str
    :param _sub_type: The sub_type of card.
    :type _sub_type: str
    :param _second_line: The second line of text on the card
    :type _second_line: str
    :param _name_on_card: The user's name as will be on the card
    :type _name_on_card: str
    :param _primary_account_number_four_digit: The last 4 digits of the PAN of
    the card.
    :type _primary_account_number_four_digit: str
    :param _status: The status to set for the card. After ordering the card it
    will be DEACTIVATED.
    :type _status: str
    :param _order_status: The order status of the card. After ordering the card
    it will be NEW_CARD_REQUEST_RECEIVED.
    :type _order_status: str
    :param _expiry_date: The expiry date of the card.
    :type _expiry_date: str
    :param _limit: The limits to define for the card (e.g. 25 EUR for
    CARD_LIMIT_CONTACTLESS).
    :type _limit: list[object_.CardLimit]
    :param _country_permission: The countries for which to grant (temporary)
    permissions to use the card.
    :type _country_permission: list[object_.CardCountryPermission]
    :param _label_monetary_account_ordered: The monetary account this card was
    ordered on and the label user that owns the card.
    :type _label_monetary_account_ordered: object_.MonetaryAccountReference
    :param _label_monetary_account_current: The monetary account that this card
    is currently linked to and the label user viewing it.
    :type _label_monetary_account_current: object_.MonetaryAccountReference
    :param _alias: The label for the user who requested the card.
    :type _alias: object_.LabelUser
    :param _pin_code_assignment: Array of Types, PINs, account IDs assigned to
    the card.
    :type _pin_code_assignment: list[object_.CardPinAssignment]
    :param _monetary_account_id_fallback: ID of the MA to be used as fallback
    for this card if insufficient balance. Fallback account is removed if not
    supplied.
    :type _monetary_account_id_fallback: int
    :param _country: The country that is domestic to the card. Defaults to
    country of residence of user.
    :type _country: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/card-debit"

    # Field constants.
    FIELD_SECOND_LINE = "second_line"
    FIELD_NAME_ON_CARD = "name_on_card"
    FIELD_ALIAS = "alias"
    FIELD_TYPE = "type"
    FIELD_PIN_CODE_ASSIGNMENT = "pin_code_assignment"
    FIELD_MONETARY_ACCOUNT_ID_FALLBACK = "monetary_account_id_fallback"

    # Object type.
    _OBJECT_TYPE_POST = "CardDebit"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._public_uuid = None
        self._type_ = None
        self._sub_type = None
        self._second_line = None
        self._name_on_card = None
        self._primary_account_number_four_digit = None
        self._status = None
        self._order_status = None
        self._expiry_date = None
        self._limit = None
        self._country_permission = None
        self._label_monetary_account_ordered = None
        self._label_monetary_account_current = None
        self._alias = None
        self._pin_code_assignment = None
        self._monetary_account_id_fallback = None
        self._country = None

    @classmethod
    def create(cls, second_line, name_on_card, alias=None, type_=None,
               pin_code_assignment=None, monetary_account_id_fallback=None,
               custom_headers=None):
        """
        Create a new debit card request.
        
        :type user_id: int
        :param second_line: The second line of text on the card, used as
        name/description for it. It can contain at most 17 characters and it can
        be empty.
        :type second_line: str
        :param name_on_card: The user's name as it will be on the card. Check
        'card-name' for the available card names for a user.
        :type name_on_card: str
        :param alias: The pointer to the monetary account that will be connected
        at first with the card. Its IBAN code is also the one that will be
        printed on the card itself. The pointer must be of type IBAN.
        :type alias: object_.Pointer
        :param type_: The type of card to order. Can be MAESTRO or MASTERCARD.
        :type type_: str
        :param pin_code_assignment: Array of Types, PINs, account IDs assigned
        to the card.
        :type pin_code_assignment: list[object_.CardPinAssignment]
        :param monetary_account_id_fallback: ID of the MA to be used as fallback
        for this card if insufficient balance. Fallback account is removed if
        not supplied.
        :type monetary_account_id_fallback: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardDebit
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_SECOND_LINE: second_line,
            cls.FIELD_NAME_ON_CARD: name_on_card,
            cls.FIELD_ALIAS: alias,
            cls.FIELD_TYPE: type_,
            cls.FIELD_PIN_CODE_ASSIGNMENT: pin_code_assignment,
            cls.FIELD_MONETARY_ACCOUNT_ID_FALLBACK: monetary_account_id_fallback
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        request_bytes = security.encrypt(cls._get_api_context(), request_bytes,
                                         custom_headers)
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseCardDebit.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_POST)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def public_uuid(self):
        """
        :rtype: str
        """

        return self._public_uuid

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def sub_type(self):
        """
        :rtype: str
        """

        return self._sub_type

    @property
    def second_line(self):
        """
        :rtype: str
        """

        return self._second_line

    @property
    def name_on_card(self):
        """
        :rtype: str
        """

        return self._name_on_card

    @property
    def primary_account_number_four_digit(self):
        """
        :rtype: str
        """

        return self._primary_account_number_four_digit

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def order_status(self):
        """
        :rtype: str
        """

        return self._order_status

    @property
    def expiry_date(self):
        """
        :rtype: str
        """

        return self._expiry_date

    @property
    def limit(self):
        """
        :rtype: list[object_.CardLimit]
        """

        return self._limit

    @property
    def country_permission(self):
        """
        :rtype: list[object_.CardCountryPermission]
        """

        return self._country_permission

    @property
    def label_monetary_account_ordered(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._label_monetary_account_ordered

    @property
    def label_monetary_account_current(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._label_monetary_account_current

    @property
    def alias(self):
        """
        :rtype: object_.LabelUser
        """

        return self._alias

    @property
    def pin_code_assignment(self):
        """
        :rtype: list[object_.CardPinAssignment]
        """

        return self._pin_code_assignment

    @property
    def monetary_account_id_fallback(self):
        """
        :rtype: int
        """

        return self._monetary_account_id_fallback

    @property
    def country(self):
        """
        :rtype: str
        """

        return self._country

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._public_uuid is not None:
            return False

        if self._type_ is not None:
            return False

        if self._sub_type is not None:
            return False

        if self._second_line is not None:
            return False

        if self._name_on_card is not None:
            return False

        if self._primary_account_number_four_digit is not None:
            return False

        if self._status is not None:
            return False

        if self._order_status is not None:
            return False

        if self._expiry_date is not None:
            return False

        if self._limit is not None:
            return False

        if self._country_permission is not None:
            return False

        if self._label_monetary_account_ordered is not None:
            return False

        if self._label_monetary_account_current is not None:
            return False

        if self._alias is not None:
            return False

        if self._pin_code_assignment is not None:
            return False

        if self._monetary_account_id_fallback is not None:
            return False

        if self._country is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardDebit
        """

        return converter.json_to_class(CardDebit, json_str)


class CardPinChange(core.BunqModel):
    """
    View for the pin change.
    
    :param _id_: The id of the pin change.
    :type _id_: int
    :param _label_card: The label of the card.
    :type _label_card: object_.LabelCard
    :param _label_monetary_account_current: The monetary account this card was
    ordered on and the label user that owns the card.
    :type _label_monetary_account_current: object_.MonetaryAccountReference
    :param _time_request: The request date of the pin change.
    :type _time_request: str
    :param _time_accept: The acceptance date of the pin change.
    :type _time_accept: str
    :param _status: The status of the pin change request, PIN_UPDATE_REQUESTED
    or PIN_UPDATE_ACCEPTED
    :type _status: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/card/{}/pin-change"
    _ENDPOINT_URL_READ = "user/{}/card/{}/pin-change/{}"

    # Object type.
    _OBJECT_TYPE_GET = "CardPinChange"

    def __init__(self):
        self._id_ = None
        self._label_card = None
        self._label_monetary_account_current = None
        self._time_request = None
        self._time_accept = None
        self._status = None

    @classmethod
    def list(cls, card_id, params=None, custom_headers=None):
        """
        :type user_id: int
        :type card_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardPinChangeList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(), card_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCardPinChangeList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def get(cls, card_id, card_pin_change_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type card_id: int
        :type card_pin_change_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardPinChange
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     card_id,
                                                     card_pin_change_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCardPinChange.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def label_card(self):
        """
        :rtype: object_.LabelCard
        """

        return self._label_card

    @property
    def label_monetary_account_current(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._label_monetary_account_current

    @property
    def time_request(self):
        """
        :rtype: str
        """

        return self._time_request

    @property
    def time_accept(self):
        """
        :rtype: str
        """

        return self._time_accept

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._label_card is not None:
            return False

        if self._label_monetary_account_current is not None:
            return False

        if self._time_request is not None:
            return False

        if self._time_accept is not None:
            return False

        if self._status is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardPinChange
        """

        return converter.json_to_class(CardPinChange, json_str)


class CardResult(core.BunqModel):
    """
    Endpoint for Card result requests (failed and successful transactions).
    
    :param _monetary_account_id: The id of the monetary account this card result
    links to.
    :type _monetary_account_id: int
    :param _card_id: The id of the card this card result links to.
    :type _card_id: int
    :param _amount_original: The original amount of the message.
    :type _amount_original: object_.Amount
    :param _amount_final: The final amount of the message to be booked to the
    account.
    :type _amount_final: object_.Amount
    :param _decision: Why the transaction was denied, if it was denied, or just
    ALLOWED.
    :type _decision: str
    :param _decision_description: Empty if allowed, otherwise a textual
    explanation of why it was denied.
    :type _decision_description: str
    :param _decision_description_translated: Empty if allowed, otherwise a
    textual explanation of why it was denied in user's language.
    :type _decision_description_translated: str
    :param _description: The description for this transaction to display.
    :type _description: str
    :param _message_type: The type of message that this card result is created
    for.
    :type _message_type: str
    :param _authorisation_type: The way the cardholder was authorised to the POS
    or ATM.
    :type _authorisation_type: str
    :param _city: The city where the message originates from.
    :type _city: str
    :param _alias: The monetary account label of the account that this result is
    created for.
    :type _alias: object_.MonetaryAccountReference
    :param _counterparty_alias: The monetary account label of the counterparty.
    :type _counterparty_alias: object_.MonetaryAccountReference
    :param _label_card: The label of the card.
    :type _label_card: object_.LabelCard
    :param _reservation_status: The status of the reservation if the transaction
    is a reservation.
    :type _reservation_status: str
    :param _reservation_expiry_time: The moment the reservation will expire.
    :type _reservation_expiry_time: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/card-result/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/card-result"

    # Object type.
    _OBJECT_TYPE_GET = "CardResult"

    def __init__(self):
        self._monetary_account_id = None
        self._card_id = None
        self._amount_original = None
        self._amount_final = None
        self._decision = None
        self._decision_description = None
        self._decision_description_translated = None
        self._description = None
        self._message_type = None
        self._authorisation_type = None
        self._city = None
        self._alias = None
        self._counterparty_alias = None
        self._label_card = None
        self._reservation_status = None
        self._reservation_expiry_time = None

    @classmethod
    def get(cls, card_result_id, monetary_account_id=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type card_result_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardResult
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     card_result_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCardResult.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardResultList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCardResultList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def card_id(self):
        """
        :rtype: int
        """

        return self._card_id

    @property
    def amount_original(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_original

    @property
    def amount_final(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_final

    @property
    def decision(self):
        """
        :rtype: str
        """

        return self._decision

    @property
    def decision_description(self):
        """
        :rtype: str
        """

        return self._decision_description

    @property
    def decision_description_translated(self):
        """
        :rtype: str
        """

        return self._decision_description_translated

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def message_type(self):
        """
        :rtype: str
        """

        return self._message_type

    @property
    def authorisation_type(self):
        """
        :rtype: str
        """

        return self._authorisation_type

    @property
    def city(self):
        """
        :rtype: str
        """

        return self._city

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def counterparty_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counterparty_alias

    @property
    def label_card(self):
        """
        :rtype: object_.LabelCard
        """

        return self._label_card

    @property
    def reservation_status(self):
        """
        :rtype: str
        """

        return self._reservation_status

    @property
    def reservation_expiry_time(self):
        """
        :rtype: str
        """

        return self._reservation_expiry_time

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._monetary_account_id is not None:
            return False

        if self._card_id is not None:
            return False

        if self._amount_original is not None:
            return False

        if self._amount_final is not None:
            return False

        if self._decision is not None:
            return False

        if self._decision_description is not None:
            return False

        if self._decision_description_translated is not None:
            return False

        if self._description is not None:
            return False

        if self._message_type is not None:
            return False

        if self._authorisation_type is not None:
            return False

        if self._city is not None:
            return False

        if self._alias is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._label_card is not None:
            return False

        if self._reservation_status is not None:
            return False

        if self._reservation_expiry_time is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardResult
        """

        return converter.json_to_class(CardResult, json_str)


class DraftPayment(core.BunqModel):
    """
    A DraftPayment is like a regular Payment, but it needs to be accepted by the
    sending party before the actual Payment is done.
    
    :param _id_: The id of the created DrafPayment.
    :type _id_: int
    :param _monetary_account_id: The id of the MonetaryAccount the DraftPayment
    applies to.
    :type _monetary_account_id: int
    :param _user_alias_created: The label of the User who created the
    DraftPayment.
    :type _user_alias_created: object_.LabelUser
    :param _responses: All responses to this draft payment.
    :type _responses: list[object_.DraftPaymentResponse]
    :param _status: The status of the DraftPayment.
    :type _status: str
    :param _type_: The type of the DraftPayment.
    :type _type_: str
    :param _entries: The entries in the DraftPayment.
    :type _entries: list[object_.DraftPaymentEntry]
    :param _object_: The Payment or PaymentBatch. This will only be present
    after the DraftPayment has been accepted.
    :type _object_: object_.DraftPaymentAnchorObject
    :param _request_reference_split_the_bill: The reference to the object used
    for split the bill. Can be RequestInquiry or RequestInquiryBatch
    :type _request_reference_split_the_bill:
    list[object_.RequestInquiryReference]
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/draft-payment"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/draft-payment/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/draft-payment"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/draft-payment/{}"

    # Field constants.
    FIELD_STATUS = "status"
    FIELD_ENTRIES = "entries"
    FIELD_PREVIOUS_UPDATED_TIMESTAMP = "previous_updated_timestamp"
    FIELD_NUMBER_OF_REQUIRED_ACCEPTS = "number_of_required_accepts"

    # Object type.
    _OBJECT_TYPE_GET = "DraftPayment"

    def __init__(self):
        self._id_ = None
        self._monetary_account_id = None
        self._user_alias_created = None
        self._responses = None
        self._status = None
        self._type_ = None
        self._entries = None
        self._object_ = None
        self._request_reference_split_the_bill = None

    @classmethod
    def create(cls, entries, number_of_required_accepts,
               monetary_account_id=None, status=None,
               previous_updated_timestamp=None, custom_headers=None):
        """
        Create a new DraftPayment.
        
        :type user_id: int
        :type monetary_account_id: int
        :param entries: The list of entries in the DraftPayment. Each entry will
        result in a payment when the DraftPayment is accepted.
        :type entries: list[object_.DraftPaymentEntry]
        :param number_of_required_accepts: The number of accepts that are
        required for the draft payment to receive status ACCEPTED. Currently
        only 1 is valid.
        :type number_of_required_accepts: int
        :param status: The status of the DraftPayment.
        :type status: str
        :param previous_updated_timestamp: The last updated_timestamp that you
        received for this DraftPayment. This needs to be provided to prevent
        race conditions.
        :type previous_updated_timestamp: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_STATUS: status,
            cls.FIELD_ENTRIES: entries,
            cls.FIELD_PREVIOUS_UPDATED_TIMESTAMP: previous_updated_timestamp,
            cls.FIELD_NUMBER_OF_REQUIRED_ACCEPTS: number_of_required_accepts
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, draft_payment_id, monetary_account_id=None, status=None,
               entries=None, previous_updated_timestamp=None,
               custom_headers=None):
        """
        Update a DraftPayment.
        
        :type user_id: int
        :type monetary_account_id: int
        :type draft_payment_id: int
        :param status: The status of the DraftPayment.
        :type status: str
        :param entries: The list of entries in the DraftPayment. Each entry will
        result in a payment when the DraftPayment is accepted.
        :type entries: list[object_.DraftPaymentEntry]
        :param previous_updated_timestamp: The last updated_timestamp that you
        received for this DraftPayment. This needs to be provided to prevent
        race conditions.
        :type previous_updated_timestamp: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status,
            cls.FIELD_ENTRIES: entries,
            cls.FIELD_PREVIOUS_UPDATED_TIMESTAMP: previous_updated_timestamp
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       draft_payment_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        Get a listing of all DraftPayments from a given MonetaryAccount.
        
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDraftPaymentList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseDraftPaymentList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def get(cls, draft_payment_id, monetary_account_id=None,
            custom_headers=None):
        """
        Get a specific DraftPayment.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type draft_payment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDraftPayment
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     draft_payment_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseDraftPayment.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def user_alias_created(self):
        """
        :rtype: object_.LabelUser
        """

        return self._user_alias_created

    @property
    def responses(self):
        """
        :rtype: list[object_.DraftPaymentResponse]
        """

        return self._responses

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def entries(self):
        """
        :rtype: list[object_.DraftPaymentEntry]
        """

        return self._entries

    @property
    def object_(self):
        """
        :rtype: object_.DraftPaymentAnchorObject
        """

        return self._object_

    @property
    def request_reference_split_the_bill(self):
        """
        :rtype: list[object_.RequestInquiryReference]
        """

        return self._request_reference_split_the_bill

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        if self._user_alias_created is not None:
            return False

        if self._responses is not None:
            return False

        if self._status is not None:
            return False

        if self._type_ is not None:
            return False

        if self._entries is not None:
            return False

        if self._object_ is not None:
            return False

        if self._request_reference_split_the_bill is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftPayment
        """

        return converter.json_to_class(DraftPayment, json_str)


class Payment(core.BunqModel):
    """
    Using Payment, you can send payments to bunq and non-bunq users from your
    bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases.
    When transferring money to other bunq MonetaryAccounts you can also refer to
    Attachments. These will be received by the counter-party as part of the
    Payment. You can also retrieve a single Payment or all executed Payments of
    a specific monetary account.
    
    :param _id_: The id of the created Payment.
    :type _id_: int
    :param _created: The timestamp when the Payment was done.
    :type _created: str
    :param _updated: The timestamp when the Payment was last updated (will be
    updated when chat messages are received).
    :type _updated: str
    :param _monetary_account_id: The id of the MonetaryAccount the Payment was
    made to or from (depending on whether this is an incoming or outgoing
    Payment).
    :type _monetary_account_id: int
    :param _amount: The Amount transferred by the Payment. Will be negative for
    outgoing Payments and positive for incoming Payments (relative to the
    MonetaryAccount indicated by monetary_account_id).
    :type _amount: object_.Amount
    :param _alias: The LabelMonetaryAccount containing the public information of
    'this' (party) side of the Payment.
    :type _alias: object_.MonetaryAccountReference
    :param _counterparty_alias: The LabelMonetaryAccount containing the public
    information of the other (counterparty) side of the Payment.
    :type _counterparty_alias: object_.MonetaryAccountReference
    :param _description: The description for the Payment. Maximum 140 characters
    for Payments to external IBANs, 9000 characters for Payments to only other
    bunq MonetaryAccounts.
    :type _description: str
    :param _type_: The type of Payment, can be BUNQ, EBA_SCT, EBA_SDD, IDEAL,
    SWIFT or FIS (card).
    :type _type_: str
    :param _sub_type: The sub-type of the Payment, can be PAYMENT, WITHDRAWAL,
    REVERSAL, REQUEST, BILLING, SCT, SDD or NLO.
    :type _sub_type: str
    :param _bunqto_status: The status of the bunq.to payment.
    :type _bunqto_status: str
    :param _bunqto_sub_status: The sub status of the bunq.to payment.
    :type _bunqto_sub_status: str
    :param _bunqto_share_url: The status of the bunq.to payment.
    :type _bunqto_share_url: str
    :param _bunqto_expiry: When bunq.to payment is about to expire.
    :type _bunqto_expiry: str
    :param _bunqto_time_responded: The timestamp of when the bunq.to payment was
    responded to.
    :type _bunqto_time_responded: str
    :param _attachment: The Attachments attached to the Payment.
    :type _attachment: list[object_.AttachmentMonetaryAccountPayment]
    :param _merchant_reference: Optional data included with the Payment specific
    to the merchant.
    :type _merchant_reference: str
    :param _batch_id: The id of the PaymentBatch if this Payment was part of
    one.
    :type _batch_id: int
    :param _scheduled_id: The id of the JobScheduled if the Payment was
    scheduled.
    :type _scheduled_id: int
    :param _address_shipping: A shipping Address provided with the Payment,
    currently unused.
    :type _address_shipping: object_.Address
    :param _address_billing: A billing Address provided with the Payment,
    currently unused.
    :type _address_billing: object_.Address
    :param _geolocation: The Geolocation where the Payment was done from.
    :type _geolocation: object_.Geolocation
    :param _allow_chat: Whether or not chat messages are allowed.
    :type _allow_chat: bool
    :param _request_reference_split_the_bill: The reference to the object used
    for split the bill. Can be RequestInquiry or RequestInquiryBatch
    :type _request_reference_split_the_bill:
    list[object_.RequestInquiryReference]
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/payment"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/payment/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/payment"

    # Field constants.
    FIELD_AMOUNT = "amount"
    FIELD_COUNTERPARTY_ALIAS = "counterparty_alias"
    FIELD_DESCRIPTION = "description"
    FIELD_ATTACHMENT = "attachment"
    FIELD_MERCHANT_REFERENCE = "merchant_reference"

    # Object type.
    _OBJECT_TYPE_GET = "Payment"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._monetary_account_id = None
        self._amount = None
        self._alias = None
        self._counterparty_alias = None
        self._description = None
        self._type_ = None
        self._sub_type = None
        self._bunqto_status = None
        self._bunqto_sub_status = None
        self._bunqto_share_url = None
        self._bunqto_expiry = None
        self._bunqto_time_responded = None
        self._attachment = None
        self._merchant_reference = None
        self._batch_id = None
        self._scheduled_id = None
        self._address_shipping = None
        self._address_billing = None
        self._geolocation = None
        self._allow_chat = None
        self._request_reference_split_the_bill = None

    @classmethod
    def create(cls, amount, counterparty_alias, description,
               monetary_account_id=None, attachment=None,
               merchant_reference=None, custom_headers=None):
        """
        Create a new Payment.
        
        :type user_id: int
        :type monetary_account_id: int
        :param amount: The Amount to transfer with the Payment. Must be bigger
        than 0 and smaller than the MonetaryAccount's balance.
        :type amount: object_.Amount
        :param counterparty_alias: The Alias of the party we are transferring
        the money to. Can be an Alias of type EMAIL or PHONE_NUMBER (for bunq
        MonetaryAccounts or bunq.to payments) or IBAN (for external bank
        account).
        :type counterparty_alias: object_.Pointer
        :param description: The description for the Payment. Maximum 140
        characters for Payments to external IBANs, 9000 characters for Payments
        to only other bunq MonetaryAccounts. Field is required but can be an
        empty string.
        :type description: str
        :param attachment: The Attachments to attach to the Payment.
        :type attachment: list[object_.AttachmentMonetaryAccountPayment]
        :param merchant_reference: Optional data to be included with the Payment
        specific to the merchant.
        :type merchant_reference: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_AMOUNT: amount,
            cls.FIELD_COUNTERPARTY_ALIAS: counterparty_alias,
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_ATTACHMENT: attachment,
            cls.FIELD_MERCHANT_REFERENCE: merchant_reference
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, payment_id, monetary_account_id=None, custom_headers=None):
        """
        Get a specific previous Payment.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type payment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponsePayment
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     payment_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponsePayment.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        Get a listing of all Payments performed on a given MonetaryAccount
        (incoming and outgoing).
        
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponsePaymentList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponsePaymentList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def amount(self):
        """
        :rtype: object_.Amount
        """

        return self._amount

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def counterparty_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counterparty_alias

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def sub_type(self):
        """
        :rtype: str
        """

        return self._sub_type

    @property
    def bunqto_status(self):
        """
        :rtype: str
        """

        return self._bunqto_status

    @property
    def bunqto_sub_status(self):
        """
        :rtype: str
        """

        return self._bunqto_sub_status

    @property
    def bunqto_share_url(self):
        """
        :rtype: str
        """

        return self._bunqto_share_url

    @property
    def bunqto_expiry(self):
        """
        :rtype: str
        """

        return self._bunqto_expiry

    @property
    def bunqto_time_responded(self):
        """
        :rtype: str
        """

        return self._bunqto_time_responded

    @property
    def attachment(self):
        """
        :rtype: list[object_.AttachmentMonetaryAccountPayment]
        """

        return self._attachment

    @property
    def merchant_reference(self):
        """
        :rtype: str
        """

        return self._merchant_reference

    @property
    def batch_id(self):
        """
        :rtype: int
        """

        return self._batch_id

    @property
    def scheduled_id(self):
        """
        :rtype: int
        """

        return self._scheduled_id

    @property
    def address_shipping(self):
        """
        :rtype: object_.Address
        """

        return self._address_shipping

    @property
    def address_billing(self):
        """
        :rtype: object_.Address
        """

        return self._address_billing

    @property
    def geolocation(self):
        """
        :rtype: object_.Geolocation
        """

        return self._geolocation

    @property
    def allow_chat(self):
        """
        :rtype: bool
        """

        return self._allow_chat

    @property
    def request_reference_split_the_bill(self):
        """
        :rtype: list[object_.RequestInquiryReference]
        """

        return self._request_reference_split_the_bill

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        if self._amount is not None:
            return False

        if self._alias is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._description is not None:
            return False

        if self._type_ is not None:
            return False

        if self._sub_type is not None:
            return False

        if self._bunqto_status is not None:
            return False

        if self._bunqto_sub_status is not None:
            return False

        if self._bunqto_share_url is not None:
            return False

        if self._bunqto_expiry is not None:
            return False

        if self._bunqto_time_responded is not None:
            return False

        if self._attachment is not None:
            return False

        if self._merchant_reference is not None:
            return False

        if self._batch_id is not None:
            return False

        if self._scheduled_id is not None:
            return False

        if self._address_shipping is not None:
            return False

        if self._address_billing is not None:
            return False

        if self._geolocation is not None:
            return False

        if self._allow_chat is not None:
            return False

        if self._request_reference_split_the_bill is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Payment
        """

        return converter.json_to_class(Payment, json_str)


class PaymentBatch(core.BunqModel):
    """
    Create a payment batch, or show the payment batches of a monetary account.
    
    :param _payments: The list of mutations that were made.
    :type _payments: list[Payment]
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/payment-batch"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/payment-batch/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/payment-batch/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/payment-batch"

    # Field constants.
    FIELD_PAYMENTS = "payments"

    # Object type.
    _OBJECT_TYPE_GET = "PaymentBatch"

    def __init__(self):
        self._payments = None

    @classmethod
    def create(cls, payments, monetary_account_id=None, custom_headers=None):
        """
        Create a payment batch by sending an array of single payment objects,
        that will become part of the batch.
        
        :type user_id: int
        :type monetary_account_id: int
        :param payments: The list of payments we want to send in a single batch.
        :type payments: list[Payment]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_PAYMENTS: payments
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, payment_batch_id, monetary_account_id=None,
               custom_headers=None):
        """
        Revoke a bunq.to payment batch. The status of all the payments will be
        set to REVOKED.
        
        :type user_id: int
        :type monetary_account_id: int
        :type payment_batch_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {

        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       payment_batch_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, payment_batch_id, monetary_account_id=None,
            custom_headers=None):
        """
        Return the details of a specific payment batch.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type payment_batch_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponsePaymentBatch
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     payment_batch_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponsePaymentBatch.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        Return all the payment batches for a monetary account.
        
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponsePaymentBatchList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponsePaymentBatchList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def payments(self):
        """
        :rtype: list[Payment]
        """

        return self._payments

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._payments is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: PaymentBatch
        """

        return converter.json_to_class(PaymentBatch, json_str)


class IdealMerchantTransaction(core.BunqModel):
    """
    View for requesting iDEAL transactions and polling their status.
    
    :param _monetary_account_id: The id of the monetary account this ideal
    merchant transaction links to.
    :type _monetary_account_id: int
    :param _alias: The alias of the monetary account to add money to.
    :type _alias: object_.MonetaryAccountReference
    :param _counterparty_alias: The alias of the monetary account the money
    comes from.
    :type _counterparty_alias: object_.MonetaryAccountReference
    :param _amount_guaranteed: In case of a successful transaction, the amount
    of money that will be transferred.
    :type _amount_guaranteed: object_.Amount
    :param _amount_requested: The requested amount of money to add.
    :type _amount_requested: object_.Amount
    :param _expiration: When the transaction will expire.
    :type _expiration: str
    :param _issuer: The BIC of the issuer.
    :type _issuer: str
    :param _issuer_name: The Name of the issuer.
    :type _issuer_name: str
    :param _issuer_authentication_url: The URL to visit to 
    :type _issuer_authentication_url: str
    :param _purchase_identifier: The 'purchase ID' of the iDEAL transaction.
    :type _purchase_identifier: str
    :param _status: The status of the transaction.
    :type _status: str
    :param _status_timestamp: When the status was last updated.
    :type _status_timestamp: str
    :param _transaction_identifier: The 'transaction ID' of the iDEAL
    transaction.
    :type _transaction_identifier: str
    :param _allow_chat: Whether or not chat messages are allowed.
    :type _allow_chat: bool
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/ideal-merchant-transaction"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/ideal-merchant-transaction/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/ideal-merchant-transaction"

    # Field constants.
    FIELD_AMOUNT_REQUESTED = "amount_requested"
    FIELD_ISSUER = "issuer"

    # Object type.
    _OBJECT_TYPE_GET = "IdealMerchantTransaction"

    def __init__(self):
        self._monetary_account_id = None
        self._alias = None
        self._counterparty_alias = None
        self._amount_guaranteed = None
        self._amount_requested = None
        self._expiration = None
        self._issuer = None
        self._issuer_name = None
        self._issuer_authentication_url = None
        self._purchase_identifier = None
        self._status = None
        self._status_timestamp = None
        self._transaction_identifier = None
        self._allow_chat = None

    @classmethod
    def create(cls, amount_requested, issuer, monetary_account_id=None,
               custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :param amount_requested: The requested amount of money to add.
        :type amount_requested: object_.Amount
        :param issuer: The BIC of the issuing bank to ask for money.
        :type issuer: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_AMOUNT_REQUESTED: amount_requested,
            cls.FIELD_ISSUER: issuer
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, ideal_merchant_transaction_id, monetary_account_id=None,
            custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type ideal_merchant_transaction_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseIdealMerchantTransaction
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     ideal_merchant_transaction_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseIdealMerchantTransaction.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseIdealMerchantTransactionList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseIdealMerchantTransactionList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def counterparty_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counterparty_alias

    @property
    def amount_guaranteed(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_guaranteed

    @property
    def amount_requested(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_requested

    @property
    def expiration(self):
        """
        :rtype: str
        """

        return self._expiration

    @property
    def issuer(self):
        """
        :rtype: str
        """

        return self._issuer

    @property
    def issuer_name(self):
        """
        :rtype: str
        """

        return self._issuer_name

    @property
    def issuer_authentication_url(self):
        """
        :rtype: str
        """

        return self._issuer_authentication_url

    @property
    def purchase_identifier(self):
        """
        :rtype: str
        """

        return self._purchase_identifier

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def status_timestamp(self):
        """
        :rtype: str
        """

        return self._status_timestamp

    @property
    def transaction_identifier(self):
        """
        :rtype: str
        """

        return self._transaction_identifier

    @property
    def allow_chat(self):
        """
        :rtype: bool
        """

        return self._allow_chat

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._monetary_account_id is not None:
            return False

        if self._alias is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._amount_guaranteed is not None:
            return False

        if self._amount_requested is not None:
            return False

        if self._expiration is not None:
            return False

        if self._issuer is not None:
            return False

        if self._issuer_name is not None:
            return False

        if self._issuer_authentication_url is not None:
            return False

        if self._purchase_identifier is not None:
            return False

        if self._status is not None:
            return False

        if self._status_timestamp is not None:
            return False

        if self._transaction_identifier is not None:
            return False

        if self._allow_chat is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: IdealMerchantTransaction
        """

        return converter.json_to_class(IdealMerchantTransaction, json_str)


class PromotionDisplay(core.BunqModel):
    """
    The public endpoint for retrieving and updating a promotion display model.
    
    :param _id_: The id of the promotion.
    :type _id_: int
    :param _counterparty_alias: The alias of the user you received the promotion
    from.
    :type _counterparty_alias: object_.MonetaryAccountReference
    :param _event_description: The event description of the promotion appearing
    on time line.
    :type _event_description: str
    :param _status: The status of the promotion. (CREATED, CLAIMED, EXPIRED,
    DISCARDED)
    :type _status: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/promotion-display/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/promotion-display/{}"

    # Field constants.
    FIELD_STATUS = "status"

    # Object type.
    _OBJECT_TYPE_GET = "PromotionDisplay"

    def __init__(self):
        self._id_ = None
        self._counterparty_alias = None
        self._event_description = None
        self._status = None

    @classmethod
    def get(cls, promotion_display_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type promotion_display_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponsePromotionDisplay
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     promotion_display_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponsePromotionDisplay.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, promotion_display_id, status=None, custom_headers=None):
        """
        :type user_id: int
        :type promotion_display_id: int
        :param status: The status of the promotion. User can set it to
        discarded.
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       promotion_display_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def counterparty_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counterparty_alias

    @property
    def event_description(self):
        """
        :rtype: str
        """

        return self._event_description

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._event_description is not None:
            return False

        if self._status is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: PromotionDisplay
        """

        return converter.json_to_class(PromotionDisplay, json_str)


class RequestInquiryBatch(core.BunqModel):
    """
    Create a batch of requests for payment, or show the request batches of a
    monetary account.
    
    :param _request_inquiries: The list of requests that were made.
    :type _request_inquiries: list[RequestInquiry]
    :param _total_amount_inquired: The total amount originally inquired for this
    batch.
    :type _total_amount_inquired: object_.Amount
    :param _reference_split_the_bill: The reference to the object used for split
    the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse
    and MasterCardAction
    :type _reference_split_the_bill:
    object_.RequestReferenceSplitTheBillAnchorObject
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/request-inquiry-batch"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/request-inquiry-batch/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/request-inquiry-batch/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/request-inquiry-batch"

    # Field constants.
    FIELD_REQUEST_INQUIRIES = "request_inquiries"
    FIELD_STATUS = "status"
    FIELD_TOTAL_AMOUNT_INQUIRED = "total_amount_inquired"
    FIELD_EVENT_ID = "event_id"

    # Object type.
    _OBJECT_TYPE_GET = "RequestInquiryBatch"

    def __init__(self):
        self._request_inquiries = None
        self._total_amount_inquired = None
        self._reference_split_the_bill = None

    @classmethod
    def create(cls, request_inquiries, total_amount_inquired,
               monetary_account_id=None, status=None, event_id=None,
               custom_headers=None):
        """
        Create a request batch by sending an array of single request objects,
        that will become part of the batch.
        
        :type user_id: int
        :type monetary_account_id: int
        :param request_inquiries: The list of request inquiries we want to send
        in 1 batch.
        :type request_inquiries: list[RequestInquiry]
        :param total_amount_inquired: The total amount originally inquired for
        this batch.
        :type total_amount_inquired: object_.Amount
        :param status: The status of the request.
        :type status: str
        :param event_id: The ID of the associated event if the request batch was
        made using 'split the bill'.
        :type event_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_REQUEST_INQUIRIES: request_inquiries,
            cls.FIELD_STATUS: status,
            cls.FIELD_TOTAL_AMOUNT_INQUIRED: total_amount_inquired,
            cls.FIELD_EVENT_ID: event_id
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, request_inquiry_batch_id, monetary_account_id=None,
               status=None, custom_headers=None):
        """
        Revoke a request batch. The status of all the requests will be set to
        REVOKED.
        
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_batch_id: int
        :param status: The status of the request.
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       request_inquiry_batch_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, request_inquiry_batch_id, monetary_account_id=None,
            custom_headers=None):
        """
        Return the details of a specific request batch.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_batch_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestInquiryBatch
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     request_inquiry_batch_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseRequestInquiryBatch.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        Return all the request batches for a monetary account.
        
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestInquiryBatchList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseRequestInquiryBatchList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def request_inquiries(self):
        """
        :rtype: list[RequestInquiry]
        """

        return self._request_inquiries

    @property
    def total_amount_inquired(self):
        """
        :rtype: object_.Amount
        """

        return self._total_amount_inquired

    @property
    def reference_split_the_bill(self):
        """
        :rtype: object_.RequestReferenceSplitTheBillAnchorObject
        """

        return self._reference_split_the_bill

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._request_inquiries is not None:
            return False

        if self._total_amount_inquired is not None:
            return False

        if self._reference_split_the_bill is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RequestInquiryBatch
        """

        return converter.json_to_class(RequestInquiryBatch, json_str)


class RequestInquiry(core.BunqModel):
    """
    RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative
    features that bunq offers. To request payment from another bunq account a
    new Request Inquiry is created. As with payments you can add attachments to
    a RFP. Requests for Payment are the foundation for a number of consumer
    features like 'Split the bill' and 'Request forwarding'. We invite you to
    invent your own based on the bunq api!
    
    :param _id_: The id of the created RequestInquiry.
    :type _id_: int
    :param _created: The timestamp of the payment request's creation.
    :type _created: str
    :param _updated: The timestamp of the payment request's last update.
    :type _updated: str
    :param _time_responded: The timestamp of when the payment request was
    responded to.
    :type _time_responded: str
    :param _time_expiry: The timestamp of when the payment request expired.
    :type _time_expiry: str
    :param _monetary_account_id: The id of the monetary account the request
    response applies to.
    :type _monetary_account_id: int
    :param _amount_inquired: The requested amount.
    :type _amount_inquired: object_.Amount
    :param _amount_responded: The responded amount.
    :type _amount_responded: object_.Amount
    :param _user_alias_created: The label that's displayed to the counterparty
    with the mutation. Includes user.
    :type _user_alias_created: object_.LabelUser
    :param _user_alias_revoked: The label that's displayed to the counterparty
    with the mutation. Includes user.
    :type _user_alias_revoked: object_.LabelUser
    :param _counterparty_alias: The LabelMonetaryAccount with the public
    information of the MonetaryAccount the money was requested from.
    :type _counterparty_alias: object_.MonetaryAccountReference
    :param _description: The description of the inquiry.
    :type _description: str
    :param _merchant_reference: The client's custom reference that was attached
    to the request and the mutation.
    :type _merchant_reference: str
    :param _attachment: The attachments attached to the payment.
    :type _attachment: list[object_.BunqId]
    :param _status: The status of the request.
    :type _status: str
    :param _batch_id: The id of the batch if the request was part of a batch.
    :type _batch_id: int
    :param _scheduled_id: The id of the scheduled job if the request was
    scheduled.
    :type _scheduled_id: int
    :param _minimum_age: The minimum age the user accepting the RequestInquiry
    must have.
    :type _minimum_age: int
    :param _require_address: Whether or not an address must be provided on
    accept.
    :type _require_address: str
    :param _bunqme_share_url: The url that points to the bunq.me request.
    :type _bunqme_share_url: str
    :param _redirect_url: The URL which the user is sent to after accepting or
    rejecting the Request.
    :type _redirect_url: str
    :param _address_shipping: The shipping address provided by the accepting
    user if an address was requested.
    :type _address_shipping: object_.Address
    :param _address_billing: The billing address provided by the accepting user
    if an address was requested.
    :type _address_billing: object_.Address
    :param _geolocation: The geolocation where the payment was done.
    :type _geolocation: object_.Geolocation
    :param _allow_chat: Whether or not chat messages are allowed.
    :type _allow_chat: bool
    :param _reference_split_the_bill: The reference to the object used for split
    the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse
    and MasterCardAction
    :type _reference_split_the_bill:
    object_.RequestReferenceSplitTheBillAnchorObject
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/request-inquiry"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/request-inquiry/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/request-inquiry"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/request-inquiry/{}"

    # Field constants.
    FIELD_AMOUNT_INQUIRED = "amount_inquired"
    FIELD_COUNTERPARTY_ALIAS = "counterparty_alias"
    FIELD_DESCRIPTION = "description"
    FIELD_ATTACHMENT = "attachment"
    FIELD_MERCHANT_REFERENCE = "merchant_reference"
    FIELD_STATUS = "status"
    FIELD_MINIMUM_AGE = "minimum_age"
    FIELD_REQUIRE_ADDRESS = "require_address"
    FIELD_WANT_TIP = "want_tip"
    FIELD_ALLOW_AMOUNT_LOWER = "allow_amount_lower"
    FIELD_ALLOW_AMOUNT_HIGHER = "allow_amount_higher"
    FIELD_ALLOW_BUNQME = "allow_bunqme"
    FIELD_REDIRECT_URL = "redirect_url"
    FIELD_EVENT_ID = "event_id"

    # Object type.
    _OBJECT_TYPE_PUT = "RequestInquiry"
    _OBJECT_TYPE_GET = "RequestInquiry"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._time_responded = None
        self._time_expiry = None
        self._monetary_account_id = None
        self._amount_inquired = None
        self._amount_responded = None
        self._user_alias_created = None
        self._user_alias_revoked = None
        self._counterparty_alias = None
        self._description = None
        self._merchant_reference = None
        self._attachment = None
        self._status = None
        self._batch_id = None
        self._scheduled_id = None
        self._minimum_age = None
        self._require_address = None
        self._bunqme_share_url = None
        self._redirect_url = None
        self._address_shipping = None
        self._address_billing = None
        self._geolocation = None
        self._allow_chat = None
        self._reference_split_the_bill = None

    @classmethod
    def create(cls, amount_inquired, counterparty_alias, description,
               allow_bunqme, monetary_account_id=None, attachment=None,
               merchant_reference=None, status=None, minimum_age=None,
               require_address=None, want_tip=None, allow_amount_lower=None,
               allow_amount_higher=None, redirect_url=None, event_id=None,
               custom_headers=None):
        """
        Create a new payment request.
        
        :type user_id: int
        :type monetary_account_id: int
        :param amount_inquired: The Amount requested to be paid by the person
        the RequestInquiry is sent to. Must be bigger than 0.
        :type amount_inquired: object_.Amount
        :param counterparty_alias: The Alias of the party we are requesting the
        money from. Can be an Alias of type EMAIL, PHONE_NUMBER or IBAN. In case
        the EMAIL or PHONE_NUMBER Alias does not refer to a bunq monetary
        account, 'allow_bunqme' needs to be 'true' in order to trigger the
        creation of a bunq.me request. Otherwise no request inquiry will be
        sent.
        :type counterparty_alias: object_.Pointer
        :param description: The description for the RequestInquiry. Maximum 9000
        characters. Field is required but can be an empty string.
        :type description: str
        :param allow_bunqme: Whether or not sending a bunq.me request is
        allowed.
        :type allow_bunqme: bool
        :param attachment: The Attachments to attach to the RequestInquiry.
        :type attachment: list[object_.BunqId]
        :param merchant_reference: Optional data to be included with the
        RequestInquiry specific to the merchant. Has to be unique for the same
        source MonetaryAccount.
        :type merchant_reference: str
        :param status: The status of the RequestInquiry. Ignored in POST
        requests but can be used for revoking (cancelling) the RequestInquiry by
        setting REVOKED with a PUT request.
        :type status: str
        :param minimum_age: The minimum age the user accepting the
        RequestInquiry must have. Defaults to not checking. If set, must be
        between 12 and 100 inclusive.
        :type minimum_age: int
        :param require_address: Whether a billing and shipping address must be
        provided when paying the request. Possible values are: BILLING,
        SHIPPING, BILLING_SHIPPING, NONE, OPTIONAL. Default is NONE.
        :type require_address: str
        :param want_tip: [DEPRECATED] Whether or not the accepting user can give
        an extra tip on top of the requested Amount. Defaults to false.
        :type want_tip: bool
        :param allow_amount_lower: [DEPRECATED] Whether or not the accepting
        user can choose to accept with a lower amount than requested. Defaults
        to false.
        :type allow_amount_lower: bool
        :param allow_amount_higher: [DEPRECATED] Whether or not the accepting
        user can choose to accept with a higher amount than requested. Defaults
        to false.
        :type allow_amount_higher: bool
        :param redirect_url: The URL which the user is sent to after accepting
        or rejecting the Request.
        :type redirect_url: str
        :param event_id: The ID of the associated event if the request was made
        using 'split the bill'.
        :type event_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_AMOUNT_INQUIRED: amount_inquired,
            cls.FIELD_COUNTERPARTY_ALIAS: counterparty_alias,
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_ATTACHMENT: attachment,
            cls.FIELD_MERCHANT_REFERENCE: merchant_reference,
            cls.FIELD_STATUS: status,
            cls.FIELD_MINIMUM_AGE: minimum_age,
            cls.FIELD_REQUIRE_ADDRESS: require_address,
            cls.FIELD_WANT_TIP: want_tip,
            cls.FIELD_ALLOW_AMOUNT_LOWER: allow_amount_lower,
            cls.FIELD_ALLOW_AMOUNT_HIGHER: allow_amount_higher,
            cls.FIELD_ALLOW_BUNQME: allow_bunqme,
            cls.FIELD_REDIRECT_URL: redirect_url,
            cls.FIELD_EVENT_ID: event_id
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, request_inquiry_id, monetary_account_id=None, status=None,
               custom_headers=None):
        """
        Revoke a request for payment, by updating the status to REVOKED.
        
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_id: int
        :param status: The status of the RequestInquiry. Ignored in POST
        requests but can be used for revoking (cancelling) the RequestInquiry by
        setting REVOKED with a PUT request.
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestInquiry
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       request_inquiry_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseRequestInquiry.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_PUT)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        Get all payment requests for a user's monetary account.
        
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestInquiryList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseRequestInquiryList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def get(cls, request_inquiry_id, monetary_account_id=None,
            custom_headers=None):
        """
        Get the details of a specific payment request, including its status.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestInquiry
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     request_inquiry_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseRequestInquiry.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def time_responded(self):
        """
        :rtype: str
        """

        return self._time_responded

    @property
    def time_expiry(self):
        """
        :rtype: str
        """

        return self._time_expiry

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def amount_inquired(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_inquired

    @property
    def amount_responded(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_responded

    @property
    def user_alias_created(self):
        """
        :rtype: object_.LabelUser
        """

        return self._user_alias_created

    @property
    def user_alias_revoked(self):
        """
        :rtype: object_.LabelUser
        """

        return self._user_alias_revoked

    @property
    def counterparty_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counterparty_alias

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def merchant_reference(self):
        """
        :rtype: str
        """

        return self._merchant_reference

    @property
    def attachment(self):
        """
        :rtype: list[object_.BunqId]
        """

        return self._attachment

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def batch_id(self):
        """
        :rtype: int
        """

        return self._batch_id

    @property
    def scheduled_id(self):
        """
        :rtype: int
        """

        return self._scheduled_id

    @property
    def minimum_age(self):
        """
        :rtype: int
        """

        return self._minimum_age

    @property
    def require_address(self):
        """
        :rtype: str
        """

        return self._require_address

    @property
    def bunqme_share_url(self):
        """
        :rtype: str
        """

        return self._bunqme_share_url

    @property
    def redirect_url(self):
        """
        :rtype: str
        """

        return self._redirect_url

    @property
    def address_shipping(self):
        """
        :rtype: object_.Address
        """

        return self._address_shipping

    @property
    def address_billing(self):
        """
        :rtype: object_.Address
        """

        return self._address_billing

    @property
    def geolocation(self):
        """
        :rtype: object_.Geolocation
        """

        return self._geolocation

    @property
    def allow_chat(self):
        """
        :rtype: bool
        """

        return self._allow_chat

    @property
    def reference_split_the_bill(self):
        """
        :rtype: object_.RequestReferenceSplitTheBillAnchorObject
        """

        return self._reference_split_the_bill

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._time_responded is not None:
            return False

        if self._time_expiry is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        if self._amount_inquired is not None:
            return False

        if self._amount_responded is not None:
            return False

        if self._user_alias_created is not None:
            return False

        if self._user_alias_revoked is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._description is not None:
            return False

        if self._merchant_reference is not None:
            return False

        if self._attachment is not None:
            return False

        if self._status is not None:
            return False

        if self._batch_id is not None:
            return False

        if self._scheduled_id is not None:
            return False

        if self._minimum_age is not None:
            return False

        if self._require_address is not None:
            return False

        if self._bunqme_share_url is not None:
            return False

        if self._redirect_url is not None:
            return False

        if self._address_shipping is not None:
            return False

        if self._address_billing is not None:
            return False

        if self._geolocation is not None:
            return False

        if self._allow_chat is not None:
            return False

        if self._reference_split_the_bill is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RequestInquiry
        """

        return converter.json_to_class(RequestInquiry, json_str)


class MasterCardAction(core.BunqModel):
    """
    MasterCard transaction view.
    
    :param _id_: The id of the MastercardAction.
    :type _id_: int
    :param _monetary_account_id: The id of the monetary account this action
    links to.
    :type _monetary_account_id: int
    :param _card_id: The id of the card this action links to.
    :type _card_id: int
    :param _amount_local: The amount of the transaction in local currency.
    :type _amount_local: object_.Amount
    :param _amount_billing: The amount of the transaction in the monetary
    account's currency.
    :type _amount_billing: object_.Amount
    :param _amount_original_local: The original amount in local currency.
    :type _amount_original_local: object_.Amount
    :param _amount_original_billing: The original amount in the monetary
    account's currency.
    :type _amount_original_billing: object_.Amount
    :param _amount_fee: The fee amount as charged by the merchant, if
    applicable.
    :type _amount_fee: object_.Amount
    :param _decision: Why the transaction was denied, if it was denied, or just
    ALLOWED.
    :type _decision: str
    :param _decision_description: Empty if allowed, otherwise a textual
    explanation of why it was denied.
    :type _decision_description: str
    :param _decision_description_translated: Empty if allowed, otherwise a
    textual explanation of why it was denied in user's language.
    :type _decision_description_translated: str
    :param _description: The description for this transaction to display.
    :type _description: str
    :param _authorisation_status: The status in the authorisation process.
    :type _authorisation_status: str
    :param _authorisation_type: The type of transaction that was delivered using
    the card.
    :type _authorisation_type: str
    :param _pan_entry_mode_user: The type of entry mode the user used. Can be
    'ATM', 'ICC', 'MAGNETIC_STRIPE' or 'E_COMMERCE'.
    :type _pan_entry_mode_user: str
    :param _city: The city where the message originates from as announced by the
    terminal.
    :type _city: str
    :param _alias: The monetary account label of the account that this action is
    created for.
    :type _alias: object_.MonetaryAccountReference
    :param _counterparty_alias: The monetary account label of the counterparty.
    :type _counterparty_alias: object_.MonetaryAccountReference
    :param _label_card: The label of the card.
    :type _label_card: object_.LabelCard
    :param _token_status: If this is a tokenisation action, this shows the
    status of the token.
    :type _token_status: str
    :param _reservation_expiry_time: If this is a reservation, the moment the
    reservation will expire.
    :type _reservation_expiry_time: str
    :param _applied_limit: The type of the limit applied to validate if this
    MasterCardAction was within the spending limits. The returned string matches
    the limit types as defined in the card endpoint.
    :type _applied_limit: str
    :param _allow_chat: Whether or not chat messages are allowed.
    :type _allow_chat: bool
    :param _eligible_whitelist_id: The whitelist id for this mastercard action
    or null.
    :type _eligible_whitelist_id: int
    :param _secure_code_id: The secure code id for this mastercard action or
    null.
    :type _secure_code_id: int
    :param _request_reference_split_the_bill: The reference to the object used
    for split the bill. Can be RequestInquiry or RequestInquiryBatch
    :type _request_reference_split_the_bill:
    list[object_.RequestInquiryReference]
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/mastercard-action/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/mastercard-action"

    # Object type.
    _OBJECT_TYPE_GET = "MasterCardAction"

    def __init__(self):
        self._id_ = None
        self._monetary_account_id = None
        self._card_id = None
        self._amount_local = None
        self._amount_billing = None
        self._amount_original_local = None
        self._amount_original_billing = None
        self._amount_fee = None
        self._decision = None
        self._decision_description = None
        self._decision_description_translated = None
        self._description = None
        self._authorisation_status = None
        self._authorisation_type = None
        self._pan_entry_mode_user = None
        self._city = None
        self._alias = None
        self._counterparty_alias = None
        self._label_card = None
        self._token_status = None
        self._reservation_expiry_time = None
        self._applied_limit = None
        self._allow_chat = None
        self._eligible_whitelist_id = None
        self._secure_code_id = None
        self._request_reference_split_the_bill = None

    @classmethod
    def get(cls, master_card_action_id, monetary_account_id=None,
            custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type master_card_action_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseMasterCardAction
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     master_card_action_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseMasterCardAction.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseMasterCardActionList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseMasterCardActionList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def card_id(self):
        """
        :rtype: int
        """

        return self._card_id

    @property
    def amount_local(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_local

    @property
    def amount_billing(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_billing

    @property
    def amount_original_local(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_original_local

    @property
    def amount_original_billing(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_original_billing

    @property
    def amount_fee(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_fee

    @property
    def decision(self):
        """
        :rtype: str
        """

        return self._decision

    @property
    def decision_description(self):
        """
        :rtype: str
        """

        return self._decision_description

    @property
    def decision_description_translated(self):
        """
        :rtype: str
        """

        return self._decision_description_translated

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def authorisation_status(self):
        """
        :rtype: str
        """

        return self._authorisation_status

    @property
    def authorisation_type(self):
        """
        :rtype: str
        """

        return self._authorisation_type

    @property
    def pan_entry_mode_user(self):
        """
        :rtype: str
        """

        return self._pan_entry_mode_user

    @property
    def city(self):
        """
        :rtype: str
        """

        return self._city

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def counterparty_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counterparty_alias

    @property
    def label_card(self):
        """
        :rtype: object_.LabelCard
        """

        return self._label_card

    @property
    def token_status(self):
        """
        :rtype: str
        """

        return self._token_status

    @property
    def reservation_expiry_time(self):
        """
        :rtype: str
        """

        return self._reservation_expiry_time

    @property
    def applied_limit(self):
        """
        :rtype: str
        """

        return self._applied_limit

    @property
    def allow_chat(self):
        """
        :rtype: bool
        """

        return self._allow_chat

    @property
    def eligible_whitelist_id(self):
        """
        :rtype: int
        """

        return self._eligible_whitelist_id

    @property
    def secure_code_id(self):
        """
        :rtype: int
        """

        return self._secure_code_id

    @property
    def request_reference_split_the_bill(self):
        """
        :rtype: list[object_.RequestInquiryReference]
        """

        return self._request_reference_split_the_bill

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        if self._card_id is not None:
            return False

        if self._amount_local is not None:
            return False

        if self._amount_billing is not None:
            return False

        if self._amount_original_local is not None:
            return False

        if self._amount_original_billing is not None:
            return False

        if self._amount_fee is not None:
            return False

        if self._decision is not None:
            return False

        if self._decision_description is not None:
            return False

        if self._decision_description_translated is not None:
            return False

        if self._description is not None:
            return False

        if self._authorisation_status is not None:
            return False

        if self._authorisation_type is not None:
            return False

        if self._pan_entry_mode_user is not None:
            return False

        if self._city is not None:
            return False

        if self._alias is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._label_card is not None:
            return False

        if self._token_status is not None:
            return False

        if self._reservation_expiry_time is not None:
            return False

        if self._applied_limit is not None:
            return False

        if self._allow_chat is not None:
            return False

        if self._eligible_whitelist_id is not None:
            return False

        if self._secure_code_id is not None:
            return False

        if self._request_reference_split_the_bill is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MasterCardAction
        """

        return converter.json_to_class(MasterCardAction, json_str)


class RequestResponse(core.BunqModel):
    """
    A RequestResponse is what a user on the other side of a RequestInquiry gets
    when he is sent one. So a RequestInquiry is the initiator and visible for
    the user that sent it and that wants to receive the money. A RequestResponse
    is what the other side sees, i.e. the user that pays the money to accept the
    request. The content is almost identical.
    
    :param _id_: The id of the Request Response.
    :type _id_: int
    :param _created: The timestamp when the Request Response was created.
    :type _created: str
    :param _updated: The timestamp when the Request Response was last updated
    (will be updated when chat messages are received).
    :type _updated: str
    :param _time_responded: The timestamp of when the RequestResponse was
    responded to.
    :type _time_responded: str
    :param _time_expiry: The timestamp of when the RequestResponse expired or
    will expire.
    :type _time_expiry: str
    :param _monetary_account_id: The id of the MonetaryAccount the
    RequestResponse was received on.
    :type _monetary_account_id: int
    :param _amount_inquired: The requested Amount.
    :type _amount_inquired: object_.Amount
    :param _amount_responded: The Amount the RequestResponse was accepted with.
    :type _amount_responded: object_.Amount
    :param _status: The status of the RequestResponse. Can be ACCEPTED, PENDING,
    REJECTED or REVOKED.
    :type _status: str
    :param _description: The description for the RequestResponse provided by the
    requesting party. Maximum 9000 characters.
    :type _description: str
    :param _alias: The LabelMonetaryAccount with the public information of the
    MonetaryAccount this RequestResponse was received on.
    :type _alias: object_.MonetaryAccountReference
    :param _counterparty_alias: The LabelMonetaryAccount with the public
    information of the MonetaryAccount that is requesting money with this
    RequestResponse.
    :type _counterparty_alias: object_.MonetaryAccountReference
    :param _attachment: The Attachments attached to the RequestResponse.
    :type _attachment: list[object_.Attachment]
    :param _minimum_age: The minimum age the user accepting the RequestResponse
    must have.
    :type _minimum_age: int
    :param _require_address: Whether or not an address must be provided on
    accept.
    :type _require_address: str
    :param _geolocation: The Geolocation where the RequestResponse was created.
    :type _geolocation: object_.Geolocation
    :param _type_: The type of the RequestInquiry. Can be DIRECT_DEBIT,
    DIRECT_DEBIT_B2B, IDEAL, SOFORT or INTERNAL.
    :type _type_: str
    :param _sub_type: The subtype of the RequestInquiry. Can be ONCE or
    RECURRING for DIRECT_DEBIT RequestInquiries and NONE for all other.
    :type _sub_type: str
    :param _redirect_url: The URL which the user is sent to after accepting or
    rejecting the Request.
    :type _redirect_url: str
    :param _address_billing: The billing address provided by the accepting user
    if an address was requested.
    :type _address_billing: object_.Address
    :param _address_shipping: The shipping address provided by the accepting
    user if an address was requested.
    :type _address_shipping: object_.Address
    :param _allow_chat: Whether or not chat messages are allowed.
    :type _allow_chat: bool
    :param _credit_scheme_identifier: The credit scheme id provided by the
    counterparty for DIRECT_DEBIT inquiries.
    :type _credit_scheme_identifier: str
    :param _mandate_identifier: The mandate id provided by the counterparty for
    DIRECT_DEBIT inquiries.
    :type _mandate_identifier: str
    :param _eligible_whitelist_id: The whitelist id for this action or null.
    :type _eligible_whitelist_id: int
    :param _request_reference_split_the_bill: The reference to the object used
    for split the bill. Can be RequestInquiry or RequestInquiryBatch
    :type _request_reference_split_the_bill:
    list[object_.RequestInquiryReference]
    """

    # Endpoint constants.
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/request-response/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/request-response"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/request-response/{}"

    # Field constants.
    FIELD_AMOUNT_RESPONDED = "amount_responded"
    FIELD_STATUS = "status"
    FIELD_ADDRESS_SHIPPING = "address_shipping"
    FIELD_ADDRESS_BILLING = "address_billing"

    # Object type.
    _OBJECT_TYPE_PUT = "RequestResponse"
    _OBJECT_TYPE_GET = "RequestResponse"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._time_responded = None
        self._time_expiry = None
        self._monetary_account_id = None
        self._amount_inquired = None
        self._amount_responded = None
        self._status = None
        self._description = None
        self._alias = None
        self._counterparty_alias = None
        self._attachment = None
        self._minimum_age = None
        self._require_address = None
        self._geolocation = None
        self._type_ = None
        self._sub_type = None
        self._redirect_url = None
        self._address_billing = None
        self._address_shipping = None
        self._allow_chat = None
        self._credit_scheme_identifier = None
        self._mandate_identifier = None
        self._eligible_whitelist_id = None
        self._request_reference_split_the_bill = None

    @classmethod
    def update(cls, request_response_id, monetary_account_id=None,
               amount_responded=None, status=None, address_shipping=None,
               address_billing=None, custom_headers=None):
        """
        Update the status to accept or reject the RequestResponse.
        
        :type user_id: int
        :type monetary_account_id: int
        :type request_response_id: int
        :param amount_responded: The Amount the user decides to pay.
        :type amount_responded: object_.Amount
        :param status: The responding status of the RequestResponse. Can be
        ACCEPTED or REJECTED.
        :type status: str
        :param address_shipping: The shipping Address to return to the user who
        created the RequestInquiry. Should only be provided if 'require_address'
        is set to SHIPPING, BILLING_SHIPPING or OPTIONAL.
        :type address_shipping: object_.Address
        :param address_billing: The billing Address to return to the user who
        created the RequestInquiry. Should only be provided if 'require_address'
        is set to BILLING, BILLING_SHIPPING or OPTIONAL.
        :type address_billing: object_.Address
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestResponse
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_AMOUNT_RESPONDED: amount_responded,
            cls.FIELD_STATUS: status,
            cls.FIELD_ADDRESS_SHIPPING: address_shipping,
            cls.FIELD_ADDRESS_BILLING: address_billing
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       request_response_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseRequestResponse.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_PUT)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        Get all RequestResponses for a MonetaryAccount.
        
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestResponseList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseRequestResponseList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def get(cls, request_response_id, monetary_account_id=None,
            custom_headers=None):
        """
        Get the details for a specific existing RequestResponse.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type request_response_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestResponse
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     request_response_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseRequestResponse.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def time_responded(self):
        """
        :rtype: str
        """

        return self._time_responded

    @property
    def time_expiry(self):
        """
        :rtype: str
        """

        return self._time_expiry

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def amount_inquired(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_inquired

    @property
    def amount_responded(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_responded

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def counterparty_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counterparty_alias

    @property
    def attachment(self):
        """
        :rtype: list[object_.Attachment]
        """

        return self._attachment

    @property
    def minimum_age(self):
        """
        :rtype: int
        """

        return self._minimum_age

    @property
    def require_address(self):
        """
        :rtype: str
        """

        return self._require_address

    @property
    def geolocation(self):
        """
        :rtype: object_.Geolocation
        """

        return self._geolocation

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def sub_type(self):
        """
        :rtype: str
        """

        return self._sub_type

    @property
    def redirect_url(self):
        """
        :rtype: str
        """

        return self._redirect_url

    @property
    def address_billing(self):
        """
        :rtype: object_.Address
        """

        return self._address_billing

    @property
    def address_shipping(self):
        """
        :rtype: object_.Address
        """

        return self._address_shipping

    @property
    def allow_chat(self):
        """
        :rtype: bool
        """

        return self._allow_chat

    @property
    def credit_scheme_identifier(self):
        """
        :rtype: str
        """

        return self._credit_scheme_identifier

    @property
    def mandate_identifier(self):
        """
        :rtype: str
        """

        return self._mandate_identifier

    @property
    def eligible_whitelist_id(self):
        """
        :rtype: int
        """

        return self._eligible_whitelist_id

    @property
    def request_reference_split_the_bill(self):
        """
        :rtype: list[object_.RequestInquiryReference]
        """

        return self._request_reference_split_the_bill

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._time_responded is not None:
            return False

        if self._time_expiry is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        if self._amount_inquired is not None:
            return False

        if self._amount_responded is not None:
            return False

        if self._status is not None:
            return False

        if self._description is not None:
            return False

        if self._alias is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._attachment is not None:
            return False

        if self._minimum_age is not None:
            return False

        if self._require_address is not None:
            return False

        if self._geolocation is not None:
            return False

        if self._type_ is not None:
            return False

        if self._sub_type is not None:
            return False

        if self._redirect_url is not None:
            return False

        if self._address_billing is not None:
            return False

        if self._address_shipping is not None:
            return False

        if self._allow_chat is not None:
            return False

        if self._credit_scheme_identifier is not None:
            return False

        if self._mandate_identifier is not None:
            return False

        if self._eligible_whitelist_id is not None:
            return False

        if self._request_reference_split_the_bill is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RequestResponse
        """

        return converter.json_to_class(RequestResponse, json_str)


class ScheduleInstance(core.BunqModel):
    """
    view for reading, updating and listing the scheduled instance.
    
    :param _state: The state of the scheduleInstance. (FINISHED_SUCCESSFULLY,
    RETRY, FAILED_USER_ERROR)
    :type _state: str
    :param _time_start: The schedule start time (UTC).
    :type _time_start: str
    :param _time_end: The schedule end time (UTC).
    :type _time_end: str
    :param _error_message: The message when the scheduled instance has run and
    failed due to user error.
    :type _error_message: list[object_.Error]
    :param _scheduled_object: The scheduled object. (Payment, PaymentBatch)
    :type _scheduled_object: object_.ScheduleAnchorObject
    :param _result_object: The result object of this schedule instance.
    (Payment, PaymentBatch)
    :type _result_object: object_.ScheduleInstanceAnchorObject
    :param _request_reference_split_the_bill: The reference to the object used
    for split the bill. Can be RequestInquiry or RequestInquiryBatch
    :type _request_reference_split_the_bill:
    list[object_.RequestInquiryReference]
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/schedule/{}/schedule-instance/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/schedule/{}/schedule-instance/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/schedule/{}/schedule-instance"

    # Field constants.
    FIELD_STATE = "state"

    # Object type.
    _OBJECT_TYPE_GET = "ScheduledInstance"

    def __init__(self):
        self._state = None
        self._time_start = None
        self._time_end = None
        self._error_message = None
        self._scheduled_object = None
        self._result_object = None
        self._request_reference_split_the_bill = None

    @classmethod
    def get(cls, schedule_id, schedule_instance_id, monetary_account_id=None,
            custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_id: int
        :type schedule_instance_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseScheduleInstance
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     schedule_id,
                                                     schedule_instance_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseScheduleInstance.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, schedule_id, schedule_instance_id, monetary_account_id=None,
               state=None, custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_id: int
        :type schedule_instance_id: int
        :param state: Change the state of the scheduleInstance from
        FAILED_USER_ERROR to RETRY.
        :type state: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATE: state
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       schedule_id,
                                                       schedule_instance_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, schedule_id, monetary_account_id=None, params=None,
             custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseScheduleInstanceList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            schedule_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseScheduleInstanceList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def state(self):
        """
        :rtype: str
        """

        return self._state

    @property
    def time_start(self):
        """
        :rtype: str
        """

        return self._time_start

    @property
    def time_end(self):
        """
        :rtype: str
        """

        return self._time_end

    @property
    def error_message(self):
        """
        :rtype: list[object_.Error]
        """

        return self._error_message

    @property
    def scheduled_object(self):
        """
        :rtype: object_.ScheduleAnchorObject
        """

        return self._scheduled_object

    @property
    def result_object(self):
        """
        :rtype: object_.ScheduleInstanceAnchorObject
        """

        return self._result_object

    @property
    def request_reference_split_the_bill(self):
        """
        :rtype: list[object_.RequestInquiryReference]
        """

        return self._request_reference_split_the_bill

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._state is not None:
            return False

        if self._time_start is not None:
            return False

        if self._time_end is not None:
            return False

        if self._error_message is not None:
            return False

        if self._scheduled_object is not None:
            return False

        if self._result_object is not None:
            return False

        if self._request_reference_split_the_bill is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ScheduleInstance
        """

        return converter.json_to_class(ScheduleInstance, json_str)


class TabResultResponse(core.BunqModel):
    """
    Used to view TabResultResponse objects belonging to a tab. A
    TabResultResponse is an object that holds details on a tab which has been
    paid from the provided monetary account.
    
    :param _tab: The Tab details.
    :type _tab: Tab
    :param _payment: The payment made for the Tab.
    :type _payment: Payment
    :param _request_reference_split_the_bill: The reference to the object used
    for split the bill. Can be RequestInquiry or RequestInquiryBatch
    :type _request_reference_split_the_bill:
    list[object_.RequestInquiryReference]
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/tab-result-response/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/tab-result-response"

    # Object type.
    _OBJECT_TYPE_GET = "TabResultResponse"

    def __init__(self):
        self._tab = None
        self._payment = None
        self._request_reference_split_the_bill = None

    @classmethod
    def get(cls, tab_result_response_id, monetary_account_id=None,
            custom_headers=None):
        """
        Used to view a single TabResultResponse belonging to a tab.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type tab_result_response_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabResultResponse
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     tab_result_response_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabResultResponse.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        Used to view a list of TabResultResponse objects belonging to a tab.
        
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabResultResponseList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabResultResponseList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def tab(self):
        """
        :rtype: Tab
        """

        return self._tab

    @property
    def payment(self):
        """
        :rtype: Payment
        """

        return self._payment

    @property
    def request_reference_split_the_bill(self):
        """
        :rtype: list[object_.RequestInquiryReference]
        """

        return self._request_reference_split_the_bill

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._tab is not None:
            return False

        if self._payment is not None:
            return False

        if self._request_reference_split_the_bill is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabResultResponse
        """

        return converter.json_to_class(TabResultResponse, json_str)


class Tab(core.BunqModel):
    """
    Used to read a single publicly visible tab.
    
    :param _uuid: The uuid of the tab.
    :type _uuid: str
    :param _alias: The label of the party that owns this tab.
    :type _alias: object_.MonetaryAccountReference
    :param _avatar: The avatar of this tab.
    :type _avatar: str
    :param _reference: The reference of the tab, as defined by the owner.
    :type _reference: str
    :param _description: The short description of the tab.
    :type _description: str
    :param _status: The status of the tab.
    :type _status: str
    :param _expiration: The moment when this tab expires.
    :type _expiration: str
    :param _amount_total: The total amount of the tab.
    :type _amount_total: object_.Amount
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "tab/{}"

    # Object type.
    _OBJECT_TYPE_GET = "Tab"

    def __init__(self):
        self._uuid = None
        self._alias = None
        self._avatar = None
        self._reference = None
        self._description = None
        self._status = None
        self._expiration = None
        self._amount_total = None

    @classmethod
    def get(cls, tab_uuid, custom_headers=None):
        """
        Get a publicly visible tab.
        
        :type api_context: context.ApiContext
        :type tab_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTab
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(tab_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTab.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def avatar(self):
        """
        :rtype: str
        """

        return self._avatar

    @property
    def reference(self):
        """
        :rtype: str
        """

        return self._reference

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def expiration(self):
        """
        :rtype: str
        """

        return self._expiration

    @property
    def amount_total(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_total

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._uuid is not None:
            return False

        if self._alias is not None:
            return False

        if self._avatar is not None:
            return False

        if self._reference is not None:
            return False

        if self._description is not None:
            return False

        if self._status is not None:
            return False

        if self._expiration is not None:
            return False

        if self._amount_total is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Tab
        """

        return converter.json_to_class(Tab, json_str)


class WhitelistResult(core.BunqModel):
    """
    Whitelist an SDD so that when one comes in, it is automatically accepted.
    
    :param _id_: The ID of the whitelist entry.
    :type _id_: int
    :param _monetary_account_paying_id: The account from which payments will be
    deducted when a transaction is matched with this whitelist.
    :type _monetary_account_paying_id: int
    :param _status: The status of the WhitelistResult.
    :type _status: str
    :param _whitelist: The corresponding whitelist.
    :type _whitelist: Whitelist
    :param _object_: The details of the external object the event was created
    for.
    :type _object_: core.BunqModel
    :param _request_reference_split_the_bill: The reference to the object used
    for split the bill. Can be RequestInquiry or RequestInquiryBatch
    :type _request_reference_split_the_bill:
    list[object_.RequestInquiryReference]
    """

    def __init__(self):
        self._id_ = None
        self._monetary_account_paying_id = None
        self._status = None
        self._whitelist = None
        self._object_ = None
        self._request_reference_split_the_bill = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def monetary_account_paying_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_paying_id

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def whitelist(self):
        """
        :rtype: Whitelist
        """

        return self._whitelist

    @property
    def object_(self):
        """
        :rtype: core.BunqModel
        """

        return self._object_

    @property
    def request_reference_split_the_bill(self):
        """
        :rtype: list[object_.RequestInquiryReference]
        """

        return self._request_reference_split_the_bill

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._monetary_account_paying_id is not None:
            return False

        if self._status is not None:
            return False

        if self._whitelist is not None:
            return False

        if self._object_ is not None:
            return False

        if self._request_reference_split_the_bill is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: WhitelistResult
        """

        return converter.json_to_class(WhitelistResult, json_str)


class Whitelist(core.BunqModel):
    """
    Whitelist a Request so that when one comes in, it is automatically accepted.
    """

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Whitelist
        """

        return converter.json_to_class(Whitelist, json_str)


class SchedulePaymentBatch(core.BunqModel):
    """
    Endpoint for schedule payment batches.
    
    :param _payments: The payment details.
    :type _payments: list[object_.SchedulePaymentEntry]
    :param _schedule: The schedule details.
    :type _schedule: Schedule
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/schedule-payment-batch"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/schedule-payment-batch/{}"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/schedule-payment-batch/{}"

    # Field constants.
    FIELD_PAYMENTS = "payments"
    FIELD_SCHEDULE = "schedule"

    def __init__(self):
        self._payments = None
        self._schedule = None

    @classmethod
    def create(cls, payments, schedule, monetary_account_id=None,
               custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :param payments: The payment details.
        :type payments: list[object_.SchedulePaymentEntry]
        :param schedule: The schedule details when creating a scheduled payment.
        :type schedule: Schedule
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_PAYMENTS: payments,
            cls.FIELD_SCHEDULE: schedule
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, schedule_payment_batch_id, monetary_account_id=None,
               payments=None, schedule=None, custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_payment_batch_id: int
        :param payments: The payment details.
        :type payments: list[object_.SchedulePaymentEntry]
        :param schedule: The schedule details when creating a scheduled payment.
        :type schedule: Schedule
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_PAYMENTS: payments,
            cls.FIELD_SCHEDULE: schedule
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       schedule_payment_batch_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def delete(cls, schedule_payment_batch_id, monetary_account_id=None,
               custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_payment_batch_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       schedule_payment_batch_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @property
    def payments(self):
        """
        :rtype: list[object_.SchedulePaymentEntry]
        """

        return self._payments

    @property
    def schedule(self):
        """
        :rtype: Schedule
        """

        return self._schedule

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._payments is not None:
            return False

        if self._schedule is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: SchedulePaymentBatch
        """

        return converter.json_to_class(SchedulePaymentBatch, json_str)


class Schedule(core.BunqModel):
    """
    view for reading the scheduled definitions.
    
    :param _time_start: The schedule start time (UTC).
    :type _time_start: str
    :param _time_end: The schedule end time (UTC).
    :type _time_end: str
    :param _recurrence_unit: The schedule recurrence unit, options: ONCE,
    HOURLY, DAILY, WEEKLY, MONTHLY, YEARLY
    :type _recurrence_unit: str
    :param _recurrence_size: The schedule recurrence size. For example size 4
    and unit WEEKLY means the recurrence is every 4 weeks.
    :type _recurrence_size: int
    :param _status: The schedule status, options: ACTIVE, FINISHED, CANCELLED.
    :type _status: str
    :param _object_: The scheduled object. (Payment, PaymentBatch)
    :type _object_: object_.ScheduleAnchorObject
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/schedule/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/schedule"

    # Field constants.
    FIELD_TIME_START = "time_start"
    FIELD_TIME_END = "time_end"
    FIELD_RECURRENCE_UNIT = "recurrence_unit"
    FIELD_RECURRENCE_SIZE = "recurrence_size"

    # Object type.
    _OBJECT_TYPE_GET = "Schedule"

    def __init__(self):
        self._time_start = None
        self._time_end = None
        self._recurrence_unit = None
        self._recurrence_size = None
        self._status = None
        self._object_ = None

    @classmethod
    def get(cls, schedule_id, monetary_account_id=None, custom_headers=None):
        """
        Get a specific schedule definition for a given monetary account.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseSchedule
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     schedule_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseSchedule.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        Get a collection of scheduled definition for a given monetary account.
        You can add the parameter type to filter the response. When
        type={SCHEDULE_DEFINITION_PAYMENT,SCHEDULE_DEFINITION_PAYMENT_BATCH} is
        provided only schedule definition object that relate to these
        definitions are returned.
        
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseScheduleList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseScheduleList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def time_start(self):
        """
        :rtype: str
        """

        return self._time_start

    @property
    def time_end(self):
        """
        :rtype: str
        """

        return self._time_end

    @property
    def recurrence_unit(self):
        """
        :rtype: str
        """

        return self._recurrence_unit

    @property
    def recurrence_size(self):
        """
        :rtype: int
        """

        return self._recurrence_size

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def object_(self):
        """
        :rtype: object_.ScheduleAnchorObject
        """

        return self._object_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._time_start is not None:
            return False

        if self._time_end is not None:
            return False

        if self._recurrence_unit is not None:
            return False

        if self._recurrence_size is not None:
            return False

        if self._status is not None:
            return False

        if self._object_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Schedule
        """

        return converter.json_to_class(Schedule, json_str)


class SchedulePayment(core.BunqModel):
    """
    Endpoint for schedule payments.
    
    :param _payment: The payment details.
    :type _payment: object_.SchedulePaymentEntry
    :param _schedule: The schedule details.
    :type _schedule: Schedule
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/schedule-payment"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/schedule-payment/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/schedule-payment/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/schedule-payment"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/schedule-payment/{}"

    # Field constants.
    FIELD_PAYMENT = "payment"
    FIELD_SCHEDULE = "schedule"

    # Object type.
    _OBJECT_TYPE_GET = "ScheduledPayment"

    def __init__(self):
        self._payment = None
        self._schedule = None

    @classmethod
    def create(cls, payment, schedule, monetary_account_id=None,
               custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :param payment: The payment details.
        :type payment: object_.SchedulePaymentEntry
        :param schedule: The schedule details when creating or updating a
        scheduled payment.
        :type schedule: Schedule
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_PAYMENT: payment,
            cls.FIELD_SCHEDULE: schedule
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def delete(cls, schedule_payment_id, monetary_account_id=None,
               custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_payment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       schedule_payment_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @classmethod
    def get(cls, schedule_payment_id, monetary_account_id=None,
            custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_payment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseSchedulePayment
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     schedule_payment_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseSchedulePayment.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseSchedulePaymentList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseSchedulePaymentList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, schedule_payment_id, monetary_account_id=None, payment=None,
               schedule=None, custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_payment_id: int
        :param payment: The payment details.
        :type payment: object_.SchedulePaymentEntry
        :param schedule: The schedule details when creating or updating a
        scheduled payment.
        :type schedule: Schedule
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_PAYMENT: payment,
            cls.FIELD_SCHEDULE: schedule
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       schedule_payment_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def payment(self):
        """
        :rtype: object_.SchedulePaymentEntry
        """

        return self._payment

    @property
    def schedule(self):
        """
        :rtype: Schedule
        """

        return self._schedule

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._payment is not None:
            return False

        if self._schedule is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: SchedulePayment
        """

        return converter.json_to_class(SchedulePayment, json_str)


class ShareInviteBankInquiry(core.BunqModel):
    """
    Used to share a monetary account with another bunq user, as in the 'Connect'
    feature in the bunq app. Allow the creation of share inquiries that, in the
    same way as request inquiries, can be revoked by the user creating them or
    accepted/rejected by the other party.
    
    :param _alias: The label of the monetary account that's being shared.
    :type _alias: object_.MonetaryAccountReference
    :param _user_alias_created: The user who created the share.
    :type _user_alias_created: object_.LabelUser
    :param _user_alias_revoked: The user who revoked the share.
    :type _user_alias_revoked: object_.LabelUser
    :param _counter_user_alias: The label of the user to share with.
    :type _counter_user_alias: object_.LabelUser
    :param _monetary_account_id: The id of the monetary account the share
    applies to.
    :type _monetary_account_id: int
    :param _draft_share_invite_bank_id: The id of the draft share invite bank.
    :type _draft_share_invite_bank_id: int
    :param _share_detail: The share details. Only one of these objects is
    returned.
    :type _share_detail: object_.ShareDetail
    :param _status: The status of the share. Can be PENDING, REVOKED (the user
    deletes the share inquiry before it's accepted), ACCEPTED, CANCELLED (the
    user deletes an active share) or CANCELLATION_PENDING,
    CANCELLATION_ACCEPTED, CANCELLATION_REJECTED (for canceling mutual connects)
    :type _status: str
    :param _share_type: The share type, either STANDARD or MUTUAL.
    :type _share_type: str
    :param _start_date: The start date of this share.
    :type _start_date: str
    :param _end_date: The expiration date of this share.
    :type _end_date: str
    :param _id_: The id of the newly created share invite.
    :type _id_: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/share-invite-bank-inquiry"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/share-invite-bank-inquiry/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/share-invite-bank-inquiry/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/share-invite-bank-inquiry"

    # Field constants.
    FIELD_COUNTER_USER_ALIAS = "counter_user_alias"
    FIELD_DRAFT_SHARE_INVITE_BANK_ID = "draft_share_invite_bank_id"
    FIELD_SHARE_DETAIL = "share_detail"
    FIELD_STATUS = "status"
    FIELD_SHARE_TYPE = "share_type"
    FIELD_START_DATE = "start_date"
    FIELD_END_DATE = "end_date"

    # Object type.
    _OBJECT_TYPE_GET = "ShareInviteBankInquiry"

    def __init__(self):
        self._alias = None
        self._user_alias_created = None
        self._user_alias_revoked = None
        self._counter_user_alias = None
        self._monetary_account_id = None
        self._draft_share_invite_bank_id = None
        self._share_detail = None
        self._status = None
        self._share_type = None
        self._start_date = None
        self._end_date = None
        self._id_ = None

    @classmethod
    def create(cls, counter_user_alias, share_detail, status,
               monetary_account_id=None, draft_share_invite_bank_id=None,
               share_type=None, start_date=None, end_date=None,
               custom_headers=None):
        """
        Create a new share inquiry for a monetary account, specifying the
        permission the other bunq user will have on it.
        
        :type user_id: int
        :type monetary_account_id: int
        :param counter_user_alias: The pointer of the user to share with.
        :type counter_user_alias: object_.Pointer
        :param share_detail: The share details. Only one of these objects may be
        passed.
        :type share_detail: object_.ShareDetail
        :param status: The status of the share. Can be PENDING, REVOKED (the
        user deletes the share inquiry before it's accepted), ACCEPTED,
        CANCELLED (the user deletes an active share) or CANCELLATION_PENDING,
        CANCELLATION_ACCEPTED, CANCELLATION_REJECTED (for canceling mutual
        connects).
        :type status: str
        :param draft_share_invite_bank_id: The id of the draft share invite
        bank.
        :type draft_share_invite_bank_id: int
        :param share_type: The share type, either STANDARD or MUTUAL.
        :type share_type: str
        :param start_date: The start date of this share.
        :type start_date: str
        :param end_date: The expiration date of this share.
        :type end_date: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_COUNTER_USER_ALIAS: counter_user_alias,
            cls.FIELD_DRAFT_SHARE_INVITE_BANK_ID: draft_share_invite_bank_id,
            cls.FIELD_SHARE_DETAIL: share_detail,
            cls.FIELD_STATUS: status,
            cls.FIELD_SHARE_TYPE: share_type,
            cls.FIELD_START_DATE: start_date,
            cls.FIELD_END_DATE: end_date
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, share_invite_bank_inquiry_id, monetary_account_id=None,
            custom_headers=None):
        """
        Get the details of a specific share inquiry.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type share_invite_bank_inquiry_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseShareInviteBankInquiry
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     share_invite_bank_inquiry_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseShareInviteBankInquiry.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, share_invite_bank_inquiry_id, monetary_account_id=None,
               share_detail=None, status=None, start_date=None, end_date=None,
               custom_headers=None):
        """
        Update the details of a share. This includes updating status (revoking
        or cancelling it), granted permission and validity period of this share.
        
        :type user_id: int
        :type monetary_account_id: int
        :type share_invite_bank_inquiry_id: int
        :param share_detail: The share details. Only one of these objects may be
        passed.
        :type share_detail: object_.ShareDetail
        :param status: The status of the share. Can be PENDING, REVOKED (the
        user deletes the share inquiry before it's accepted), ACCEPTED,
        CANCELLED (the user deletes an active share) or CANCELLATION_PENDING,
        CANCELLATION_ACCEPTED, CANCELLATION_REJECTED (for canceling mutual
        connects).
        :type status: str
        :param start_date: The start date of this share.
        :type start_date: str
        :param end_date: The expiration date of this share.
        :type end_date: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_SHARE_DETAIL: share_detail,
            cls.FIELD_STATUS: status,
            cls.FIELD_START_DATE: start_date,
            cls.FIELD_END_DATE: end_date
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       share_invite_bank_inquiry_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        Get a list with all the share inquiries for a monetary account, only if
        the requesting user has permission to change the details of the various
        ones.
        
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseShareInviteBankInquiryList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseShareInviteBankInquiryList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def user_alias_created(self):
        """
        :rtype: object_.LabelUser
        """

        return self._user_alias_created

    @property
    def user_alias_revoked(self):
        """
        :rtype: object_.LabelUser
        """

        return self._user_alias_revoked

    @property
    def counter_user_alias(self):
        """
        :rtype: object_.LabelUser
        """

        return self._counter_user_alias

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def draft_share_invite_bank_id(self):
        """
        :rtype: int
        """

        return self._draft_share_invite_bank_id

    @property
    def share_detail(self):
        """
        :rtype: object_.ShareDetail
        """

        return self._share_detail

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def share_type(self):
        """
        :rtype: str
        """

        return self._share_type

    @property
    def start_date(self):
        """
        :rtype: str
        """

        return self._start_date

    @property
    def end_date(self):
        """
        :rtype: str
        """

        return self._end_date

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._alias is not None:
            return False

        if self._user_alias_created is not None:
            return False

        if self._user_alias_revoked is not None:
            return False

        if self._counter_user_alias is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        if self._draft_share_invite_bank_id is not None:
            return False

        if self._share_detail is not None:
            return False

        if self._status is not None:
            return False

        if self._share_type is not None:
            return False

        if self._start_date is not None:
            return False

        if self._end_date is not None:
            return False

        if self._id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareInviteBankInquiry
        """

        return converter.json_to_class(ShareInviteBankInquiry, json_str)


class ShareInviteBankResponse(core.BunqModel):
    """
    Used to view or respond to shares a user was invited to. See
    'share-invite-bank-inquiry' for more information about the inquiring
    endpoint.
    
    :param _counter_alias: The monetary account and user who created the share.
    :type _counter_alias: object_.MonetaryAccountReference
    :param _user_alias_cancelled: The user who cancelled the share if it has
    been revoked or rejected.
    :type _user_alias_cancelled: object_.LabelUser
    :param _monetary_account_id: The id of the monetary account the ACCEPTED
    share applies to. null otherwise.
    :type _monetary_account_id: int
    :param _draft_share_invite_bank_id: The id of the draft share invite bank.
    :type _draft_share_invite_bank_id: int
    :param _share_detail: The share details.
    :type _share_detail: object_.ShareDetail
    :param _status: The status of the share. Can be PENDING, REVOKED (the user
    deletes the share inquiry before it's accepted), ACCEPTED, CANCELLED (the
    user deletes an active share) or CANCELLATION_PENDING,
    CANCELLATION_ACCEPTED, CANCELLATION_REJECTED (for canceling mutual connects)
    :type _status: str
    :param _share_type: The share type, either STANDARD or MUTUAL.
    :type _share_type: str
    :param _start_date: The start date of this share.
    :type _start_date: str
    :param _end_date: The expiration date of this share.
    :type _end_date: str
    :param _description: The description of this share. It is basically the
    monetary account description.
    :type _description: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/share-invite-bank-response/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/share-invite-bank-response/{}"
    _ENDPOINT_URL_LISTING = "user/{}/share-invite-bank-response"

    # Field constants.
    FIELD_STATUS = "status"

    # Object type.
    _OBJECT_TYPE_GET = "ShareInviteBankResponse"

    def __init__(self):
        self._counter_alias = None
        self._user_alias_cancelled = None
        self._monetary_account_id = None
        self._draft_share_invite_bank_id = None
        self._share_detail = None
        self._status = None
        self._share_type = None
        self._start_date = None
        self._end_date = None
        self._description = None

    @classmethod
    def get(cls, share_invite_bank_response_id, custom_headers=None):
        """
        Return the details of a specific share a user was invited to.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type share_invite_bank_response_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseShareInviteBankResponse
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     share_invite_bank_response_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseShareInviteBankResponse.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, share_invite_bank_response_id, status=None,
               custom_headers=None):
        """
        Accept or reject a share a user was invited to.
        
        :type user_id: int
        :type share_invite_bank_response_id: int
        :param status: The status of the share. Can be PENDING, REVOKED (the
        user deletes the share inquiry before it's accepted), ACCEPTED,
        CANCELLED (the user deletes an active share) or CANCELLATION_PENDING,
        CANCELLATION_ACCEPTED, CANCELLATION_REJECTED (for canceling mutual
        connects)
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       share_invite_bank_response_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Return all the shares a user was invited to.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseShareInviteBankResponseList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseShareInviteBankResponseList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def counter_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counter_alias

    @property
    def user_alias_cancelled(self):
        """
        :rtype: object_.LabelUser
        """

        return self._user_alias_cancelled

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def draft_share_invite_bank_id(self):
        """
        :rtype: int
        """

        return self._draft_share_invite_bank_id

    @property
    def share_detail(self):
        """
        :rtype: object_.ShareDetail
        """

        return self._share_detail

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def share_type(self):
        """
        :rtype: str
        """

        return self._share_type

    @property
    def start_date(self):
        """
        :rtype: str
        """

        return self._start_date

    @property
    def end_date(self):
        """
        :rtype: str
        """

        return self._end_date

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._counter_alias is not None:
            return False

        if self._user_alias_cancelled is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        if self._draft_share_invite_bank_id is not None:
            return False

        if self._share_detail is not None:
            return False

        if self._status is not None:
            return False

        if self._share_type is not None:
            return False

        if self._start_date is not None:
            return False

        if self._end_date is not None:
            return False

        if self._description is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareInviteBankResponse
        """

        return converter.json_to_class(ShareInviteBankResponse, json_str)


class UserCredentialPasswordIp(core.BunqModel):
    """
    Create a credential of a user for server authentication, or delete the
    credential of a user for server authentication.
    
    :param _id_: The id of the credential.
    :type _id_: int
    :param _created: The timestamp of the credential object's creation.
    :type _created: str
    :param _updated: The timestamp of the credential object's last update.
    :type _updated: str
    :param _status: The status of the credential.
    :type _status: str
    :param _expiry_time: When the status is PENDING_FIRST_USE: when the
    credential expires.
    :type _expiry_time: str
    :param _token_value: When the status is PENDING_FIRST_USE: the value of the
    token.
    :type _token_value: str
    :param _permitted_device: When the status is ACTIVE: the details of the
    device that may use the credential.
    :type _permitted_device: object_.PermittedDevice
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/credential-password-ip/{}"
    _ENDPOINT_URL_LISTING = "user/{}/credential-password-ip"

    # Object type.
    _OBJECT_TYPE_GET = "CredentialPasswordIp"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._status = None
        self._expiry_time = None
        self._token_value = None
        self._permitted_device = None

    @classmethod
    def get(cls, user_credential_password_ip_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type user_credential_password_ip_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserCredentialPasswordIp
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     user_credential_password_ip_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseUserCredentialPasswordIp.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserCredentialPasswordIpList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseUserCredentialPasswordIpList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def expiry_time(self):
        """
        :rtype: str
        """

        return self._expiry_time

    @property
    def token_value(self):
        """
        :rtype: str
        """

        return self._token_value

    @property
    def permitted_device(self):
        """
        :rtype: object_.PermittedDevice
        """

        return self._permitted_device

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._status is not None:
            return False

        if self._expiry_time is not None:
            return False

        if self._token_value is not None:
            return False

        if self._permitted_device is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: UserCredentialPasswordIp
        """

        return converter.json_to_class(UserCredentialPasswordIp, json_str)


class ChatMessageStatus(core.BunqModel):
    """
    Endpoint for retrieving the messages that are part of a conversation.
    
    :param _id_: The id of the message.
    :type _id_: int
    :param _created: The timestamp when the message was created.
    :type _created: str
    :param _updated: The timestamp when the message was last updated.
    :type _updated: str
    :param _conversation_id: The id of the conversation this message belongs to.
    :type _conversation_id: int
    :param _creator: The user who initiated the action that caused this message
    to appear.
    :type _creator: object_.LabelUser
    :param _content: The content of this message.
    :type _content: object_.ChatMessageContent
    """

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._conversation_id = None
        self._creator = None
        self._content = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def conversation_id(self):
        """
        :rtype: int
        """

        return self._conversation_id

    @property
    def creator(self):
        """
        :rtype: object_.LabelUser
        """

        return self._creator

    @property
    def content(self):
        """
        :rtype: object_.ChatMessageContent
        """

        return self._content

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._conversation_id is not None:
            return False

        if self._creator is not None:
            return False

        if self._content is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageStatus
        """

        return converter.json_to_class(ChatMessageStatus, json_str)


class ChatMessageUser(core.BunqModel):
    """
    Endpoint for retrieving the messages that are part of a conversation.
    
    :param _id_: The id of the message.
    :type _id_: int
    :param _created: The timestamp when the message was created.
    :type _created: str
    :param _updated: The timestamp when the message was last updated.
    :type _updated: str
    :param _conversation_id: The id of the conversation this message belongs to.
    :type _conversation_id: int
    :param _creator: The user who initiated the action that caused this message
    to appear.
    :type _creator: object_.LabelUser
    :param _displayed_sender: The user displayed as the sender of this message.
    :type _displayed_sender: object_.LabelUser
    :param _content: The content of this message.
    :type _content: object_.ChatMessageContent
    """

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._conversation_id = None
        self._creator = None
        self._displayed_sender = None
        self._content = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def conversation_id(self):
        """
        :rtype: int
        """

        return self._conversation_id

    @property
    def creator(self):
        """
        :rtype: object_.LabelUser
        """

        return self._creator

    @property
    def displayed_sender(self):
        """
        :rtype: object_.LabelUser
        """

        return self._displayed_sender

    @property
    def content(self):
        """
        :rtype: object_.ChatMessageContent
        """

        return self._content

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._conversation_id is not None:
            return False

        if self._creator is not None:
            return False

        if self._displayed_sender is not None:
            return False

        if self._content is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageUser
        """

        return converter.json_to_class(ChatMessageUser, json_str)


class ChatConversationReference(core.BunqModel):
    """
    Represents conversation references.
    
    :param _id_: The id of this conversation.
    :type _id_: int
    :param _created: The timestamp the conversation reference was created.
    :type _created: str
    :param _updated: The timestamp the conversation reference was last updated.
    :type _updated: str
    """

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatConversationReference
        """

        return converter.json_to_class(ChatConversationReference, json_str)


class ChatMessageAttachment(core.BunqModel):
    """
    Create new messages holding file attachments.
    
    :param _id_: The id of the newly created chat message.
    :type _id_: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/chat-conversation/{}/message-attachment"

    # Field constants.
    FIELD_ATTACHMENT = "attachment"

    def __init__(self):
        self._id_ = None

    @classmethod
    def create(cls, chat_conversation_id, attachment, custom_headers=None):
        """
        Create a new message holding a file attachment to a specific
        conversation.
        
        :type user_id: int
        :type chat_conversation_id: int
        :param attachment: The attachment contained in this message.
        :type attachment: object_.BunqId
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_ATTACHMENT: attachment
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       chat_conversation_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageAttachment
        """

        return converter.json_to_class(ChatMessageAttachment, json_str)


class ChatMessageText(core.BunqModel):
    """
    Endpoint for the type of chat message that carries text.
    
    :param _id_: The id of the newly created chat message.
    :type _id_: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/chat-conversation/{}/message-text"

    # Field constants.
    FIELD_TEXT = "text"

    def __init__(self):
        self._id_ = None

    @classmethod
    def create(cls, chat_conversation_id, text, custom_headers=None):
        """
        Add a new text message to a specific conversation.
        
        :type user_id: int
        :type chat_conversation_id: int
        :param text: The textual content of this message. Cannot be empty.
        :type text: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_TEXT: text
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       chat_conversation_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ChatMessageText
        """

        return converter.json_to_class(ChatMessageText, json_str)


class AttachmentConversationContent(core.BunqModel):
    """
    Fetch the raw content of an attachment with given ID. The raw content is the
    base64 of a file, without any JSON wrapping.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/chat-conversation/{}/attachment/{}/content"

    # Object type.
    _OBJECT_TYPE_GET = "AttachmentConversationContent"

    @classmethod
    def list(cls, chat_conversation_id, attachment_id, custom_headers=None):
        """
        Get the raw content of a specific attachment.
        
        :type user_id: int
        :type chat_conversation_id: int
        :type attachment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(), chat_conversation_id, attachment_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentConversationContent
        """

        return converter.json_to_class(AttachmentConversationContent, json_str)


class AttachmentPublicContent(core.BunqModel):
    """
    Fetch the raw content of a public attachment with given ID. The raw content
    is the binary representation of a file, without any JSON wrapping.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "attachment-public/{}/content"

    # Object type.
    _OBJECT_TYPE_GET = "AttachmentPublicContent"

    @classmethod
    def list(cls, attachment_public_uuid, custom_headers=None):
        """
        Get the raw content of a specific attachment.
        
        :type attachment_public_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(attachment_public_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentPublicContent
        """

        return converter.json_to_class(AttachmentPublicContent, json_str)


class AttachmentTabContent(core.BunqModel):
    """
    Fetch the raw content of a tab attachment with given ID. The raw content is
    the binary representation of a file, without any JSON wrapping.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/attachment-tab/{}/content"

    # Object type.
    _OBJECT_TYPE_GET = "AttachmentTabContent"

    @classmethod
    def list(cls, attachment_tab_id, monetary_account_id=None,
             custom_headers=None):
        """
        Get the raw content of a specific attachment.
        
        :type user_id: int
        :type monetary_account_id: int
        :type attachment_tab_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            attachment_tab_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentTabContent
        """

        return converter.json_to_class(AttachmentTabContent, json_str)


class TabAttachmentTabContent(core.BunqModel):
    """
    Fetch the raw content of a tab attachment with given ID. The raw content is
    the binary representation of a file, without any JSON wrapping.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "tab/{}/attachment/{}/content"

    # Object type.
    _OBJECT_TYPE_GET = "TabAttachmentTabContent"

    @classmethod
    def list(cls, tab_uuid, attachment_id, custom_headers=None):
        """
        Get the raw content of a specific attachment.
        
        :type tab_uuid: str
        :type attachment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(tab_uuid, attachment_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabAttachmentTabContent
        """

        return converter.json_to_class(TabAttachmentTabContent, json_str)


class AttachmentMonetaryAccount(core.BunqModel):
    """
    This call is used to upload an attachment that can be referenced to in
    payment requests and payments sent from a specific monetary account.
    Attachments supported are png, jpg and gif.
    
    :param _attachment: The attachment.
    :type _attachment: object_.Attachment
    :param _id_: The ID of the attachment created.
    :type _id_: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/attachment"

    def __init__(self):
        self._attachment = None
        self._id_ = None

    @classmethod
    def create(cls, request_bytes, monetary_account_id=None,
               custom_headers=None):
        """
        Create a new monetary account attachment. Create a POST request with a
        payload that contains the binary representation of the file, without any
        JSON wrapping. Make sure you define the MIME type (i.e. image/jpeg) in
        the Content-Type header. You are required to provide a description of
        the attachment using the X-Bunq-Attachment-Description header.
        
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def attachment(self):
        """
        :rtype: object_.Attachment
        """

        return self._attachment

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._attachment is not None:
            return False

        if self._id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentMonetaryAccount
        """

        return converter.json_to_class(AttachmentMonetaryAccount, json_str)


class AttachmentPublic(core.BunqModel):
    """
    This call is used to upload an attachment that can be referenced to as an
    avatar (through the Avatar endpoint) or in a tab sent. Attachments supported
    are png, jpg and gif.
    
    :param _uuid: The UUID of the attachment.
    :type _uuid: str
    :param _created: The timestamp of the attachment's creation.
    :type _created: str
    :param _updated: The timestamp of the attachment's last update.
    :type _updated: str
    :param _attachment: The attachment.
    :type _attachment: object_.Attachment
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "attachment-public"
    _ENDPOINT_URL_READ = "attachment-public/{}"

    # Object type.
    _OBJECT_TYPE_POST = "Uuid"
    _OBJECT_TYPE_GET = "AttachmentPublic"

    def __init__(self):
        self._uuid = None
        self._created = None
        self._updated = None
        self._attachment = None

    @classmethod
    def create(cls, request_bytes, custom_headers=None):
        """
        Create a new public attachment. Create a POST request with a payload
        that contains a binary representation of the file, without any JSON
        wrapping. Make sure you define the MIME type (i.e. image/jpeg, or
        image/png) in the Content-Type header. You are required to provide a
        description of the attachment using the X-Bunq-Attachment-Description
        header.
        
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_CREATE
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def get(cls, attachment_public_uuid, custom_headers=None):
        """
        Get a specific attachment's metadata through its UUID. The Content-Type
        header of the response will describe the MIME type of the attachment
        file.
        
        :type api_context: context.ApiContext
        :type attachment_public_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseAttachmentPublic
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(attachment_public_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseAttachmentPublic.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def attachment(self):
        """
        :rtype: object_.Attachment
        """

        return self._attachment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._uuid is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._attachment is not None:
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
    This call is used to upload an attachment that will be accessible only
    through tabs. This can be used for example to upload special promotions or
    other attachments. Attachments supported are png, jpg and gif.
    
    :param _id_: The id of the attachment.
    :type _id_: int
    :param _created: The timestamp of the attachment's creation.
    :type _created: str
    :param _updated: The timestamp of the attachment's last update.
    :type _updated: str
    :param _attachment: The attachment.
    :type _attachment: object_.Attachment
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/attachment-tab"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/attachment-tab/{}"

    # Object type.
    _OBJECT_TYPE_GET = "AttachmentTab"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._attachment = None

    @classmethod
    def create(cls, request_bytes, monetary_account_id=None,
               custom_headers=None):
        """
        Upload a new attachment to use with a tab, and to read its metadata.
        Create a POST request with a payload that contains the binary
        representation of the file, without any JSON wrapping. Make sure you
        define the MIME type (i.e. image/jpeg) in the Content-Type header. You
        are required to provide a description of the attachment using the
        X-Bunq-Attachment-Description header.
        
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, attachment_tab_id, monetary_account_id=None,
            custom_headers=None):
        """
        Get a specific attachment. The header of the response contains the
        content-type of the attachment.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type attachment_tab_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseAttachmentTab
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     attachment_tab_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseAttachmentTab.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def attachment(self):
        """
        :rtype: object_.Attachment
        """

        return self._attachment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._attachment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentTab
        """

        return converter.json_to_class(AttachmentTab, json_str)


class TabAttachmentTab(core.BunqModel):
    """
    This call is used to view an attachment that is linked to a tab.
    
    :param _id_: The id of the attachment.
    :type _id_: int
    :param _created: The timestamp of the attachment's creation.
    :type _created: str
    :param _updated: The timestamp of the attachment's last update.
    :type _updated: str
    :param _attachment: The attachment.
    :type _attachment: object_.Attachment
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "tab/{}/attachment/{}"

    # Object type.
    _OBJECT_TYPE_GET = "TabAttachmentTab"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._attachment = None

    @classmethod
    def get(cls, tab_uuid, tab_attachment_tab_id, custom_headers=None):
        """
        Get a specific attachment. The header of the response contains the
        content-type of the attachment.
        
        :type api_context: context.ApiContext
        :type tab_uuid: str
        :type tab_attachment_tab_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabAttachmentTab
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(tab_uuid,
                                                     tab_attachment_tab_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabAttachmentTab.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def attachment(self):
        """
        :rtype: object_.Attachment
        """

        return self._attachment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._attachment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabAttachmentTab
        """

        return converter.json_to_class(TabAttachmentTab, json_str)


class Avatar(core.BunqModel):
    """
    Avatars are public images used to represent you or your company. Avatars are
    used to represent users, monetary accounts and cash registers. Avatars
    cannot be deleted, only replaced. Avatars can be updated after uploading the
    image you would like to use through AttachmentPublic. Using the
    attachment_public_uuid which is returned you can update your Avatar. Avatars
    used for cash registers and company accounts will be reviewed by bunq.
    
    :param _uuid: The UUID of the created avatar.
    :type _uuid: str
    :param _image: The content type of the image.
    :type _image: list[object_.Image]
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "avatar"
    _ENDPOINT_URL_READ = "avatar/{}"

    # Field constants.
    FIELD_ATTACHMENT_PUBLIC_UUID = "attachment_public_uuid"

    # Object type.
    _OBJECT_TYPE_POST = "Uuid"
    _OBJECT_TYPE_GET = "Avatar"

    def __init__(self):
        self._uuid = None
        self._image = None

    @classmethod
    def create(cls, attachment_public_uuid, custom_headers=None):
        """
        :param attachment_public_uuid: The public UUID of the public attachment
        from which an avatar image must be created.
        :type attachment_public_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_ATTACHMENT_PUBLIC_UUID: attachment_public_uuid
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def get(cls, avatar_uuid, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type avatar_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseAvatar
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(avatar_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseAvatar.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

    @property
    def image(self):
        """
        :rtype: list[object_.Image]
        """

        return self._image

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._uuid is not None:
            return False

        if self._image is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Avatar
        """

        return converter.json_to_class(Avatar, json_str)


class BunqMeTab(core.BunqModel):
    """
    bunq.me tabs allows you to create a payment request and share the link
    through e-mail, chat, etc. Multiple persons are able to respond to the
    payment request and pay through bunq, iDeal or SOFORT.
    
    :param _id_: The id of the created bunq.me.
    :type _id_: int
    :param _created: The timestamp when the bunq.me was created.
    :type _created: str
    :param _updated: The timestamp when the bunq.me was last updated.
    :type _updated: str
    :param _time_expiry: The timestamp of when the bunq.me expired or will
    expire.
    :type _time_expiry: str
    :param _monetary_account_id: The id of the MonetaryAccount the bunq.me was
    sent from.
    :type _monetary_account_id: int
    :param _status: The status of the bunq.me. Can be WAITING_FOR_PAYMENT,
    CANCELLED or EXPIRED.
    :type _status: str
    :param _bunqme_tab_share_url: The url that points to the bunq.me page.
    :type _bunqme_tab_share_url: str
    :param _bunqme_tab_entry: The bunq.me entry containing the payment
    information.
    :type _bunqme_tab_entry: BunqMeTabEntry
    :param _result_inquiries: The list of bunq.me result Inquiries successfully
    made and paid.
    :type _result_inquiries: list[BunqMeTabResultInquiry]
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/bunqme-tab"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/bunqme-tab/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/bunqme-tab"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/bunqme-tab/{}"

    # Field constants.
    FIELD_BUNQME_TAB_ENTRY = "bunqme_tab_entry"
    FIELD_STATUS = "status"

    # Object type.
    _OBJECT_TYPE_GET = "BunqMeTab"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._time_expiry = None
        self._monetary_account_id = None
        self._status = None
        self._bunqme_tab_share_url = None
        self._bunqme_tab_entry = None
        self._result_inquiries = None

    @classmethod
    def create(cls, bunqme_tab_entry, monetary_account_id=None, status=None,
               custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :param bunqme_tab_entry: The bunq.me entry containing the payment
        information.
        :type bunqme_tab_entry: BunqMeTabEntry
        :param status: The status of the bunq.me. Ignored in POST requests but
        can be used for cancelling the bunq.me by setting status as CANCELLED
        with a PUT request.
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_BUNQME_TAB_ENTRY: bunqme_tab_entry,
            cls.FIELD_STATUS: status
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, bunq_me_tab_id, monetary_account_id=None, status=None,
               custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type bunq_me_tab_id: int
        :param status: The status of the bunq.me. Ignored in POST requests but
        can be used for cancelling the bunq.me by setting status as CANCELLED
        with a PUT request.
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       bunq_me_tab_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBunqMeTabList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseBunqMeTabList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def get(cls, bunq_me_tab_id, monetary_account_id=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type bunq_me_tab_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBunqMeTab
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     bunq_me_tab_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBunqMeTab.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def time_expiry(self):
        """
        :rtype: str
        """

        return self._time_expiry

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def bunqme_tab_share_url(self):
        """
        :rtype: str
        """

        return self._bunqme_tab_share_url

    @property
    def bunqme_tab_entry(self):
        """
        :rtype: BunqMeTabEntry
        """

        return self._bunqme_tab_entry

    @property
    def result_inquiries(self):
        """
        :rtype: list[BunqMeTabResultInquiry]
        """

        return self._result_inquiries

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._time_expiry is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        if self._status is not None:
            return False

        if self._bunqme_tab_share_url is not None:
            return False

        if self._bunqme_tab_entry is not None:
            return False

        if self._result_inquiries is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BunqMeTab
        """

        return converter.json_to_class(BunqMeTab, json_str)


class BunqMeTabEntry(core.BunqModel):
    """
    bunq.me tabs allows you to create a payment request and share the link
    through e-mail, chat, etc. Multiple persons are able to respond to the
    payment request and pay through bunq, iDeal or SOFORT.
    
    :param _uuid: The uuid of the bunq.me.
    :type _uuid: str
    :param _amount_inquired: The requested Amount.
    :type _amount_inquired: object_.Amount
    :param _alias: The LabelMonetaryAccount with the public information of the
    User and the MonetaryAccount that created the bunq.me link.
    :type _alias: object_.MonetaryAccountReference
    :param _description: The description for the bunq.me. Maximum 9000
    characters.
    :type _description: str
    :param _status: The status of the bunq.me. Can be WAITING_FOR_PAYMENT,
    CANCELLED or EXPIRED.
    :type _status: str
    :param _redirect_url: The URL which the user is sent to when a payment is
    completed.
    :type _redirect_url: str
    :param _merchant_available: List of available merchants.
    :type _merchant_available: list[object_.BunqMeMerchantAvailable]
    """

    # Field constants.
    FIELD_AMOUNT_INQUIRED = "amount_inquired"
    FIELD_DESCRIPTION = "description"
    FIELD_REDIRECT_URL = "redirect_url"

    def __init__(self):
        self._uuid = None
        self._amount_inquired = None
        self._alias = None
        self._description = None
        self._status = None
        self._redirect_url = None
        self._merchant_available = None

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

    @property
    def amount_inquired(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_inquired

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def redirect_url(self):
        """
        :rtype: str
        """

        return self._redirect_url

    @property
    def merchant_available(self):
        """
        :rtype: list[object_.BunqMeMerchantAvailable]
        """

        return self._merchant_available

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._uuid is not None:
            return False

        if self._amount_inquired is not None:
            return False

        if self._alias is not None:
            return False

        if self._description is not None:
            return False

        if self._status is not None:
            return False

        if self._redirect_url is not None:
            return False

        if self._merchant_available is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BunqMeTabEntry
        """

        return converter.json_to_class(BunqMeTabEntry, json_str)


class BunqMeTabResultInquiry(core.BunqModel):
    """
    Used to view bunq.me TabResultInquiry objects belonging to a tab. A
    TabResultInquiry is an object that holds details on both the tab and a
    single payment made for that tab.
    
    :param _payment: The payment made for the Tab.
    :type _payment: Payment
    :param _bunq_me_tab_id: The Id of the bunq.me tab that this
    BunqMeTabResultInquiry belongs to.
    :type _bunq_me_tab_id: int
    """

    def __init__(self):
        self._payment = None
        self._bunq_me_tab_id = None

    @property
    def payment(self):
        """
        :rtype: Payment
        """

        return self._payment

    @property
    def bunq_me_tab_id(self):
        """
        :rtype: int
        """

        return self._bunq_me_tab_id

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._payment is not None:
            return False

        if self._bunq_me_tab_id is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BunqMeTabResultInquiry
        """

        return converter.json_to_class(BunqMeTabResultInquiry, json_str)


class CardGeneratedCvc2(core.BunqModel):
    """
    Endpoint for generating and retrieving a new CVC2 code.
    
    :param _id_: The id of the cvc code.
    :type _id_: int
    :param _created: The timestamp of the cvc code's creation.
    :type _created: str
    :param _updated: The timestamp of the cvc code's last update.
    :type _updated: str
    :param _cvc2: The cvc2 code.
    :type _cvc2: str
    :param _status: The status of the cvc2. Can be AVAILABLE, USED, EXPIRED,
    BLOCKED.
    :type _status: str
    :param _expiry_time: Expiry time of the cvc2.
    :type _expiry_time: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/card/{}/generated-cvc2"
    _ENDPOINT_URL_READ = "user/{}/card/{}/generated-cvc2/{}"
    _ENDPOINT_URL_LISTING = "user/{}/card/{}/generated-cvc2"

    # Object type.
    _OBJECT_TYPE_GET = "CardGeneratedCvc2"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._cvc2 = None
        self._status = None
        self._expiry_time = None

    @classmethod
    def create(cls, card_id, custom_headers=None):
        """
        Generate a new CVC2 code for a card.
        
        :type user_id: int
        :type card_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {

        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        request_bytes = security.encrypt(cls._get_api_context(), request_bytes,
                                         custom_headers)
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       card_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, card_id, card_generated_cvc2_id, custom_headers=None):
        """
        Get the details for a specific generated CVC2 code.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type card_id: int
        :type card_generated_cvc2_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardGeneratedCvc2
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     card_id,
                                                     card_generated_cvc2_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCardGeneratedCvc2.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, card_id, params=None, custom_headers=None):
        """
        Get all generated CVC2 codes for a card.
        
        :type user_id: int
        :type card_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardGeneratedCvc2List
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(), card_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCardGeneratedCvc2List.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def cvc2(self):
        """
        :rtype: str
        """

        return self._cvc2

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def expiry_time(self):
        """
        :rtype: str
        """

        return self._expiry_time

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._cvc2 is not None:
            return False

        if self._status is not None:
            return False

        if self._expiry_time is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardGeneratedCvc2
        """

        return converter.json_to_class(CardGeneratedCvc2, json_str)


class CardName(core.BunqModel):
    """
    Endpoint for getting all the accepted card names for a user. As bunq do not
    allow total freedom in choosing the name that is going to be printed on the
    card, the following formats are accepted: Name Surname, N. Surname, N
    Surname or Surname.
    
    :param _possible_card_name_array: All possible variations (of suitable
    length) of user's legal name for the debit card.
    :type _possible_card_name_array: list[str]
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/card-name"

    # Object type.
    _OBJECT_TYPE_GET = "CardUserNameArray"

    def __init__(self):
        self._possible_card_name_array = None

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Return all the accepted card names for a specific user.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardNameList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCardNameList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def possible_card_name_array(self):
        """
        :rtype: list[str]
        """

        return self._possible_card_name_array

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._possible_card_name_array is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardName
        """

        return converter.json_to_class(CardName, json_str)


class CardReplace(core.BunqModel):
    """
    It is possible to order a card replacement with the bunq API.<br/><br/>You
    can order up to one free card replacement per year. Additional replacement
    requests will be billed.<br/><br/>The card replacement will have the same
    expiry date and the same pricing as the old card, but it will have a new
    card number. You can change the description and optional the PIN through the
    card replacement endpoint.
    
    :param _id_: The id of the new card.
    :type _id_: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/card/{}/replace"

    # Field constants.
    FIELD_PIN_CODE = "pin_code"
    FIELD_SECOND_LINE = "second_line"

    def __init__(self):
        self._id_ = None

    @classmethod
    def create(cls, card_id, pin_code=None, second_line=None,
               custom_headers=None):
        """
        Request a card replacement.
        
        :type user_id: int
        :type card_id: int
        :param pin_code: The plaintext pin code. Requests require encryption to
        be enabled.
        :type pin_code: str
        :param second_line: The second line on the card.
        :type second_line: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_PIN_CODE: pin_code,
            cls.FIELD_SECOND_LINE: second_line
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        request_bytes = security.encrypt(cls._get_api_context(), request_bytes,
                                         custom_headers)
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       card_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardReplace
        """

        return converter.json_to_class(CardReplace, json_str)


class Card(core.BunqModel):
    """
    Endpoint for retrieving details for the cards the user has access to.
    
    :param _id_: The id of the card.
    :type _id_: int
    :param _created: The timestamp of the card's creation.
    :type _created: str
    :param _updated: The timestamp of the card's last update.
    :type _updated: str
    :param _public_uuid: The public UUID of the card.
    :type _public_uuid: str
    :param _type_: The type of the card. Can be MAESTRO, MASTERCARD.
    :type _type_: str
    :param _sub_type: The sub-type of the card.
    :type _sub_type: str
    :param _second_line: The second line of text on the card
    :type _second_line: str
    :param _status: The status to set for the card. Can be ACTIVE, DEACTIVATED,
    LOST, STOLEN, CANCELLED, EXPIRED or PIN_TRIES_EXCEEDED.
    :type _status: str
    :param _sub_status: The sub-status of the card. Can be NONE or REPLACED.
    :type _sub_status: str
    :param _order_status: The order status of the card. Can be
    CARD_UPDATE_REQUESTED, CARD_UPDATE_SENT, CARD_UPDATE_ACCEPTED,
    ACCEPTED_FOR_PRODUCTION or DELIVERED_TO_CUSTOMER.
    :type _order_status: str
    :param _expiry_date: Expiry date of the card.
    :type _expiry_date: str
    :param _name_on_card: The user's name on the card.
    :type _name_on_card: str
    :param _primary_account_number_four_digit: The last 4 digits of the PAN of
    the card.
    :type _primary_account_number_four_digit: str
    :param _limit: The limits to define for the card, among
    CARD_LIMIT_CONTACTLESS, CARD_LIMIT_ATM, CARD_LIMIT_DIPPING and
    CARD_LIMIT_POS_ICC (e.g. 25 EUR for CARD_LIMIT_CONTACTLESS)
    :type _limit: list[object_.CardLimit]
    :param _mag_stripe_permission: The countries for which to grant (temporary)
    permissions to use the card.
    :type _mag_stripe_permission: object_.CardMagStripePermission
    :param _country_permission: The countries for which to grant (temporary)
    permissions to use the card.
    :type _country_permission: list[object_.CardCountryPermission]
    :param _label_monetary_account_ordered: The monetary account this card was
    ordered on and the label user that owns the card.
    :type _label_monetary_account_ordered: object_.MonetaryAccountReference
    :param _label_monetary_account_current: The monetary account that this card
    is currently linked to and the label user viewing it.
    :type _label_monetary_account_current: object_.MonetaryAccountReference
    :param _pin_code_assignment: Array of Types, PINs, account IDs assigned to
    the card.
    :type _pin_code_assignment: list[object_.CardPinAssignment]
    :param _monetary_account_id_fallback: ID of the MA to be used as fallback
    for this card if insufficient balance. Fallback account is removed if not
    supplied.
    :type _monetary_account_id_fallback: int
    :param _country: The country that is domestic to the card. Defaults to
    country of residence of user.
    :type _country: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_UPDATE = "user/{}/card/{}"
    _ENDPOINT_URL_READ = "user/{}/card/{}"
    _ENDPOINT_URL_LISTING = "user/{}/card"

    # Field constants.
    FIELD_PIN_CODE = "pin_code"
    FIELD_ACTIVATION_CODE = "activation_code"
    FIELD_STATUS = "status"
    FIELD_LIMIT = "limit"
    FIELD_MAG_STRIPE_PERMISSION = "mag_stripe_permission"
    FIELD_COUNTRY_PERMISSION = "country_permission"
    FIELD_MONETARY_ACCOUNT_CURRENT_ID = "monetary_account_current_id"
    FIELD_PIN_CODE_ASSIGNMENT = "pin_code_assignment"
    FIELD_MONETARY_ACCOUNT_ID_FALLBACK = "monetary_account_id_fallback"

    # Object type.
    _OBJECT_TYPE_PUT = "CardDebit"
    _OBJECT_TYPE_GET = "CardDebit"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._public_uuid = None
        self._type_ = None
        self._sub_type = None
        self._second_line = None
        self._status = None
        self._sub_status = None
        self._order_status = None
        self._expiry_date = None
        self._name_on_card = None
        self._primary_account_number_four_digit = None
        self._limit = None
        self._mag_stripe_permission = None
        self._country_permission = None
        self._label_monetary_account_ordered = None
        self._label_monetary_account_current = None
        self._pin_code_assignment = None
        self._monetary_account_id_fallback = None
        self._country = None

    @classmethod
    def update(cls, card_id, pin_code=None, activation_code=None, status=None,
               limit=None, mag_stripe_permission=None, country_permission=None,
               monetary_account_current_id=None, pin_code_assignment=None,
               monetary_account_id_fallback=None, custom_headers=None):
        """
        Update the card details. Allow to change pin code, status, limits,
        country permissions and the monetary account connected to the card. When
        the card has been received, it can be also activated through this
        endpoint.
        
        :type user_id: int
        :type card_id: int
        :param pin_code: The plaintext pin code. Requests require encryption to
        be enabled.
        :type pin_code: str
        :param activation_code: The activation code required to set status to
        ACTIVE initially. Can only set status to ACTIVE using activation code
        when order_status is ACCEPTED_FOR_PRODUCTION and status is DEACTIVATED.
        :type activation_code: str
        :param status: The status to set for the card. Can be ACTIVE,
        DEACTIVATED, LOST, STOLEN or CANCELLED, and can only be set to
        LOST/STOLEN/CANCELLED when order status is
        ACCEPTED_FOR_PRODUCTION/DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED.
        Can only be set to DEACTIVATED after initial activation, i.e.
        order_status is
        DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED.
        Mind that all the possible choices (apart from ACTIVE and DEACTIVATED)
        are permanent and cannot be changed after.
        :type status: str
        :param limit: The limits to define for the card, among
        CARD_LIMIT_CONTACTLESS, CARD_LIMIT_ATM, CARD_LIMIT_DIPPING and
        CARD_LIMIT_POS_ICC (e.g. 25 EUR for CARD_LIMIT_CONTACTLESS). All the
        limits must be provided on update.
        :type limit: list[object_.CardLimit]
        :param mag_stripe_permission: Whether or not it is allowed to use the
        mag stripe for the card.
        :type mag_stripe_permission: object_.CardMagStripePermission
        :param country_permission: The countries for which to grant (temporary)
        permissions to use the card.
        :type country_permission: list[object_.CardCountryPermission]
        :param monetary_account_current_id: The ID of the monetary account that
        card transactions will use.
        :type monetary_account_current_id: int
        :param pin_code_assignment: Array of Types, PINs, account IDs assigned
        to the card.
        :type pin_code_assignment: list[object_.CardPinAssignment]
        :param monetary_account_id_fallback: ID of the MA to be used as fallback
        for this card if insufficient balance. Fallback account is removed if
        not supplied.
        :type monetary_account_id_fallback: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCard
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_PIN_CODE: pin_code,
            cls.FIELD_ACTIVATION_CODE: activation_code,
            cls.FIELD_STATUS: status,
            cls.FIELD_LIMIT: limit,
            cls.FIELD_MAG_STRIPE_PERMISSION: mag_stripe_permission,
            cls.FIELD_COUNTRY_PERMISSION: country_permission,
            cls.FIELD_MONETARY_ACCOUNT_CURRENT_ID: monetary_account_current_id,
            cls.FIELD_PIN_CODE_ASSIGNMENT: pin_code_assignment,
            cls.FIELD_MONETARY_ACCOUNT_ID_FALLBACK: monetary_account_id_fallback
        }

        request_bytes = converter.class_to_json(request_map).encode()
        request_bytes = security.encrypt(cls._get_api_context(), request_bytes,
                                         custom_headers)
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       card_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseCard.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_PUT)
        )

    @classmethod
    def get(cls, card_id, custom_headers=None):
        """
        Return the details of a specific card.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type card_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCard
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     card_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCard.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Return all the cards available to the user.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCardList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def public_uuid(self):
        """
        :rtype: str
        """

        return self._public_uuid

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def sub_type(self):
        """
        :rtype: str
        """

        return self._sub_type

    @property
    def second_line(self):
        """
        :rtype: str
        """

        return self._second_line

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def sub_status(self):
        """
        :rtype: str
        """

        return self._sub_status

    @property
    def order_status(self):
        """
        :rtype: str
        """

        return self._order_status

    @property
    def expiry_date(self):
        """
        :rtype: str
        """

        return self._expiry_date

    @property
    def name_on_card(self):
        """
        :rtype: str
        """

        return self._name_on_card

    @property
    def primary_account_number_four_digit(self):
        """
        :rtype: str
        """

        return self._primary_account_number_four_digit

    @property
    def limit(self):
        """
        :rtype: list[object_.CardLimit]
        """

        return self._limit

    @property
    def mag_stripe_permission(self):
        """
        :rtype: object_.CardMagStripePermission
        """

        return self._mag_stripe_permission

    @property
    def country_permission(self):
        """
        :rtype: list[object_.CardCountryPermission]
        """

        return self._country_permission

    @property
    def label_monetary_account_ordered(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._label_monetary_account_ordered

    @property
    def label_monetary_account_current(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._label_monetary_account_current

    @property
    def pin_code_assignment(self):
        """
        :rtype: list[object_.CardPinAssignment]
        """

        return self._pin_code_assignment

    @property
    def monetary_account_id_fallback(self):
        """
        :rtype: int
        """

        return self._monetary_account_id_fallback

    @property
    def country(self):
        """
        :rtype: str
        """

        return self._country

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._public_uuid is not None:
            return False

        if self._type_ is not None:
            return False

        if self._sub_type is not None:
            return False

        if self._second_line is not None:
            return False

        if self._status is not None:
            return False

        if self._sub_status is not None:
            return False

        if self._order_status is not None:
            return False

        if self._expiry_date is not None:
            return False

        if self._name_on_card is not None:
            return False

        if self._primary_account_number_four_digit is not None:
            return False

        if self._limit is not None:
            return False

        if self._mag_stripe_permission is not None:
            return False

        if self._country_permission is not None:
            return False

        if self._label_monetary_account_ordered is not None:
            return False

        if self._label_monetary_account_current is not None:
            return False

        if self._pin_code_assignment is not None:
            return False

        if self._monetary_account_id_fallback is not None:
            return False

        if self._country is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Card
        """

        return converter.json_to_class(Card, json_str)


class CashRegisterQrCodeContent(core.BunqModel):
    """
    Show the raw contents of a QR code. First you need to created a QR code
    using ../cash-register/{id}/qr-code.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/qr-code/{}/content"

    # Object type.
    _OBJECT_TYPE_GET = "CashRegisterQrCodeContent"

    @classmethod
    def list(cls, cash_register_id, qr_code_id, monetary_account_id=None,
             custom_headers=None):
        """
        Show the raw contents of a QR code
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type qr_code_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            cash_register_id, qr_code_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CashRegisterQrCodeContent
        """

        return converter.json_to_class(CashRegisterQrCodeContent, json_str)


class CashRegisterQrCode(core.BunqModel):
    """
    Once your CashRegister has been activated you can create a QR code for it.
    The visibility of a tab can be modified to be linked to this QR code. If a
    user of the bunq app scans this QR code, the linked tab will be shown on his
    device.
    
    :param _id_: The id of the created QR code. Use this id to get the RAW
    content of the QR code with: ../qr-code/{id}/content
    :type _id_: int
    :param _created: The timestamp of the QR code's creation.
    :type _created: str
    :param _updated: The timestamp of the TokenQrCashRegister's last update.
    :type _updated: str
    :param _status: The status of this QR code. If the status is "ACTIVE" the QR
    code can be scanned to see the linked CashRegister and tab. If the status is
    "INACTIVE" the QR code does not link to a anything.
    :type _status: str
    :param _cash_register: The CashRegister that is linked to the token.
    :type _cash_register: CashRegister
    :param _tab_object: Holds the Tab object. Can be TabUsageSingle,
    TabUsageMultiple or null
    :type _tab_object: Tab
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register/{}/qr-code"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/cash-register/{}/qr-code/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/qr-code/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/qr-code"

    # Field constants.
    FIELD_STATUS = "status"

    # Object type.
    _OBJECT_TYPE_GET = "TokenQrCashRegister"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._status = None
        self._cash_register = None
        self._tab_object = None

    @classmethod
    def create(cls, cash_register_id, status, monetary_account_id=None,
               custom_headers=None):
        """
        Create a new QR code for this CashRegister. You can only have one ACTIVE
        CashRegister QR code at the time.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :param status: The status of the QR code. ACTIVE or INACTIVE. Only one
        QR code can be ACTIVE for a CashRegister at any time. Setting a QR code
        to ACTIVE will deactivate any other CashRegister QR codes.
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_STATUS: status
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, cash_register_id, cash_register_qr_code_id,
               monetary_account_id=None, status=None, custom_headers=None):
        """
        Modify a QR code in a given CashRegister. You can only have one ACTIVE
        CashRegister QR code at the time.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type cash_register_qr_code_id: int
        :param status: The status of the QR code. ACTIVE or INACTIVE. Only one
        QR code can be ACTIVE for a CashRegister at any time. Setting a QR code
        to ACTIVE will deactivate any other CashRegister QR codes.
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id,
                                                       cash_register_qr_code_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, cash_register_id, cash_register_qr_code_id,
            monetary_account_id=None, custom_headers=None):
        """
        Get the information of a specific QR code. To get the RAW content of the
        QR code use ../qr-code/{id}/content
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type cash_register_qr_code_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCashRegisterQrCode
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     cash_register_id,
                                                     cash_register_qr_code_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCashRegisterQrCode.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, cash_register_id, monetary_account_id=None, params=None,
             custom_headers=None):
        """
        Get a collection of QR code information from a given CashRegister
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCashRegisterQrCodeList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            cash_register_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCashRegisterQrCodeList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def cash_register(self):
        """
        :rtype: CashRegister
        """

        return self._cash_register

    @property
    def tab_object(self):
        """
        :rtype: Tab
        """

        return self._tab_object

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._status is not None:
            return False

        if self._cash_register is not None:
            return False

        if self._tab_object is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CashRegisterQrCode
        """

        return converter.json_to_class(CashRegisterQrCode, json_str)


class CashRegister(core.BunqModel):
    """
    CashRegisters are virtual points of sale. They have a specific name and
    avatar, and optionally, a location.<br/>With a CashRegister you can create a
    Tab and then use a QR code to receive payments.<br/>Check out our Quickstart
    example to learn how you can easily <a
    href="/api/1/page/usecase-tab-payment">create Tab
    payments</a>.<br/><br/>Notification filters can be set on a CashRegister to
    receive callbacks. For more information check the <a
    href="/api/1/page/callbacks">dedicated callbacks page</a>.
    
    :param _id_: The id of the created CashRegister.
    :type _id_: int
    :param _created: The timestamp of the CashRegister's creation.
    :type _created: str
    :param _updated: The timestamp of the CashRegister's last update.
    :type _updated: str
    :param _name: The name of the CashRegister.
    :type _name: str
    :param _status: The status of the CashRegister. Can be PENDING_APPROVAL,
    ACTIVE, DENIED or CLOSED.
    :type _status: str
    :param _avatar: The Avatar of the CashRegister.
    :type _avatar: object_.Avatar
    :param _location: The geolocation of the CashRegister. Can be null.
    :type _location: object_.Geolocation
    :param _notification_filters: The types of notifications that will result in
    a push notification or URL callback for this CashRegister.
    :type _notification_filters: list[object_.NotificationFilter]
    :param _tab_text_waiting_screen: The tab text for waiting screen of
    CashRegister.
    :type _tab_text_waiting_screen: list[object_.TabTextWaitingScreen]
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/cash-register/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register"

    # Field constants.
    FIELD_NAME = "name"
    FIELD_STATUS = "status"
    FIELD_AVATAR_UUID = "avatar_uuid"
    FIELD_LOCATION = "location"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"
    FIELD_TAB_TEXT_WAITING_SCREEN = "tab_text_waiting_screen"

    # Object type.
    _OBJECT_TYPE_GET = "CashRegister"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._name = None
        self._status = None
        self._avatar = None
        self._location = None
        self._notification_filters = None
        self._tab_text_waiting_screen = None

    @classmethod
    def create(cls, name, status, avatar_uuid, monetary_account_id=None,
               location=None, notification_filters=None,
               tab_text_waiting_screen=None, custom_headers=None):
        """
        Create a new CashRegister. Only an UserCompany can create a
        CashRegisters. They need to be created with status PENDING_APPROVAL, an
        bunq admin has to approve your CashRegister before you can use it. In
        the sandbox testing environment an CashRegister will be automatically
        approved immediately after creation.
        
        :type user_id: int
        :type monetary_account_id: int
        :param name: The name of the CashRegister. Must be unique for this
        MonetaryAccount.
        :type name: str
        :param status: The status of the CashRegister. Can only be created or
        updated with PENDING_APPROVAL or CLOSED.
        :type status: str
        :param avatar_uuid: The UUID of the avatar of the CashRegister. Use the
        calls /attachment-public and /avatar to create a new Avatar and get its
        UUID.
        :type avatar_uuid: str
        :param location: The geolocation of the CashRegister.
        :type location: object_.Geolocation
        :param notification_filters: The types of notifications that will result
        in a push notification or URL callback for this CashRegister.
        :type notification_filters: list[object_.NotificationFilter]
        :param tab_text_waiting_screen: The tab text for waiting screen of
        CashRegister.
        :type tab_text_waiting_screen: list[object_.TabTextWaitingScreen]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_NAME: name,
            cls.FIELD_STATUS: status,
            cls.FIELD_AVATAR_UUID: avatar_uuid,
            cls.FIELD_LOCATION: location,
            cls.FIELD_NOTIFICATION_FILTERS: notification_filters,
            cls.FIELD_TAB_TEXT_WAITING_SCREEN: tab_text_waiting_screen
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, cash_register_id, monetary_account_id=None,
            custom_headers=None):
        """
        Get a specific CashRegister.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCashRegister
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     cash_register_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCashRegister.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, cash_register_id, monetary_account_id=None, name=None,
               status=None, avatar_uuid=None, location=None,
               notification_filters=None, tab_text_waiting_screen=None,
               custom_headers=None):
        """
        Modify or close an existing CashRegister. You must set the status back
        to PENDING_APPROVAL if you modify the name, avatar or location of a
        CashRegister. To close a cash register put its status to CLOSED.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :param name: The name of the CashRegister. Must be unique for this
        MonetaryAccount.
        :type name: str
        :param status: The status of the CashRegister. Can only be created or
        updated with PENDING_APPROVAL or CLOSED.
        :type status: str
        :param avatar_uuid: The UUID of the avatar of the CashRegister. Use the
        calls /attachment-public and /avatar to create a new Avatar and get its
        UUID.
        :type avatar_uuid: str
        :param location: The geolocation of the CashRegister.
        :type location: object_.Geolocation
        :param notification_filters: The types of notifications that will result
        in a push notification or URL callback for this CashRegister.
        :type notification_filters: list[object_.NotificationFilter]
        :param tab_text_waiting_screen: The tab text for waiting screen of
        CashRegister.
        :type tab_text_waiting_screen: list[object_.TabTextWaitingScreen]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_NAME: name,
            cls.FIELD_STATUS: status,
            cls.FIELD_AVATAR_UUID: avatar_uuid,
            cls.FIELD_LOCATION: location,
            cls.FIELD_NOTIFICATION_FILTERS: notification_filters,
            cls.FIELD_TAB_TEXT_WAITING_SCREEN: tab_text_waiting_screen
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        Get a collection of CashRegister for a given user and monetary account.
        
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCashRegisterList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCashRegisterList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def name(self):
        """
        :rtype: str
        """

        return self._name

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def avatar(self):
        """
        :rtype: object_.Avatar
        """

        return self._avatar

    @property
    def location(self):
        """
        :rtype: object_.Geolocation
        """

        return self._location

    @property
    def notification_filters(self):
        """
        :rtype: list[object_.NotificationFilter]
        """

        return self._notification_filters

    @property
    def tab_text_waiting_screen(self):
        """
        :rtype: list[object_.TabTextWaitingScreen]
        """

        return self._tab_text_waiting_screen

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._name is not None:
            return False

        if self._status is not None:
            return False

        if self._avatar is not None:
            return False

        if self._location is not None:
            return False

        if self._notification_filters is not None:
            return False

        if self._tab_text_waiting_screen is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CashRegister
        """

        return converter.json_to_class(CashRegister, json_str)


class CertificatePinned(core.BunqModel):
    """
    This endpoint allow you to pin the certificate chains to your account. These
    certificate chains are used for SSL validation whenever a callback is
    initiated to one of your https callback urls.
    
    :param _certificate_chain: The certificate chain in .PEM format.
    Certificates are glued with newline characters.
    :type _certificate_chain: str
    :param _id_: The id generated for the pinned certificate chain.
    :type _id_: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/certificate-pinned"
    _ENDPOINT_URL_DELETE = "user/{}/certificate-pinned/{}"
    _ENDPOINT_URL_LISTING = "user/{}/certificate-pinned"
    _ENDPOINT_URL_READ = "user/{}/certificate-pinned/{}"

    # Field constants.
    FIELD_CERTIFICATE_CHAIN = "certificate_chain"

    # Object type.
    _OBJECT_TYPE_GET = "CertificatePinned"

    def __init__(self):
        self._certificate_chain = None
        self._id_ = None

    @classmethod
    def create(cls, certificate_chain, custom_headers=None):
        """
        Pin the certificate chain.
        
        :type user_id: int
        :param certificate_chain: The certificate chain in .PEM format.
        :type certificate_chain: list[object_.Certificate]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_CERTIFICATE_CHAIN: certificate_chain
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def delete(cls, certificate_pinned_id, custom_headers=None):
        """
        Remove the pinned certificate chain with the specific ID.
        
        :type user_id: int
        :type certificate_pinned_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(cls._determine_user_id(),
                                                       certificate_pinned_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        List all the pinned certificate chain for the given user.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCertificatePinnedList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCertificatePinnedList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def get(cls, certificate_pinned_id, custom_headers=None):
        """
        Get the pinned certificate chain with the specified ID.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type certificate_pinned_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCertificatePinned
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     certificate_pinned_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCertificatePinned.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def certificate_chain(self):
        """
        :rtype: str
        """

        return self._certificate_chain

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._certificate_chain is not None:
            return False

        if self._id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CertificatePinned
        """

        return converter.json_to_class(CertificatePinned, json_str)


class DeviceServer(core.BunqModel):
    """
    After having created an Installation you can now create a DeviceServer. A
    DeviceServer is needed to do a login call with session-server.
    
    :param _id_: The id of the DeviceServer as created on the server.
    :type _id_: int
    :param _created: The timestamp of the DeviceServer's creation.
    :type _created: str
    :param _updated: The timestamp of the DeviceServer's last update.
    :type _updated: str
    :param _description: The description of the DeviceServer.
    :type _description: str
    :param _ip: The ip address which was used to create the DeviceServer.
    :type _ip: str
    :param _status: The status of the DeviceServer. Can be ACTIVE, BLOCKED,
    NEEDS_CONFIRMATION or OBSOLETE.
    :type _status: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "device-server"
    _ENDPOINT_URL_READ = "device-server/{}"
    _ENDPOINT_URL_LISTING = "device-server"

    # Field constants.
    FIELD_DESCRIPTION = "description"
    FIELD_SECRET = "secret"
    FIELD_PERMITTED_IPS = "permitted_ips"

    # Object type.
    _OBJECT_TYPE_GET = "DeviceServer"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._description = None
        self._ip = None
        self._status = None

    @classmethod
    def create(cls, description, secret, permitted_ips=None,
               custom_headers=None):
        """
        Create a new DeviceServer providing the installation token in the header
        and signing the request with the private part of the key you used to
        create the installation. The API Key that you are using will be bound to
        the IP address of the DeviceServer which you have
        created.<br/><br/>Using a Wildcard API Key gives you the freedom to make
        API calls even if the IP address has changed after the POST
        device-server.<br/><br/>Find out more at this link <a
        href="https://bunq.com/en/apikey-dynamic-ip"
        target="_blank">https://bunq.com/en/apikey-dynamic-ip</a>.
        
        :param description: The description of the DeviceServer. This is only
        for your own reference when reading the DeviceServer again.
        :type description: str
        :param secret: The API key. You can request an API key in the bunq app.
        :type secret: str
        :param permitted_ips: An array of IPs (v4 or v6) this DeviceServer will
        be able to do calls from. These will be linked to the API key.
        :type permitted_ips: list[str]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_SECRET: secret,
            cls.FIELD_PERMITTED_IPS: permitted_ips
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, device_server_id, custom_headers=None):
        """
        Get one of your DeviceServers.
        
        :type api_context: context.ApiContext
        :type device_server_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDeviceServer
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(device_server_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseDeviceServer.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Get a collection of all the DeviceServers you have created.
        
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDeviceServerList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseDeviceServerList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def ip(self):
        """
        :rtype: str
        """

        return self._ip

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._description is not None:
            return False

        if self._ip is not None:
            return False

        if self._status is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DeviceServer
        """

        return converter.json_to_class(DeviceServer, json_str)


class Device(core.BunqModel, core.AnchoredObjectInterface):
    """
    Used to get a Device or a listing of Devices. Creating a DeviceServer should
    happen via /device-server
    
    :param _DeviceServer: 
    :type _DeviceServer: DeviceServer
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    # Endpoint constants.
    _ENDPOINT_URL_READ = "device/{}"
    _ENDPOINT_URL_LISTING = "device"

    # Object type.
    _OBJECT_TYPE_GET = "Device"

    def __init__(self):
        self._DeviceServer = None

    @classmethod
    def get(cls, device_id, custom_headers=None):
        """
        Get a single Device. A Device is either a DevicePhone or a DeviceServer.
        
        :type api_context: context.ApiContext
        :type device_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDevice
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(device_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseDevice.cast_from_bunq_response(
            cls._from_json(response_raw)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Get a collection of Devices. A Device is either a DevicePhone or a
        DeviceServer.
        
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDeviceList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseDeviceList.cast_from_bunq_response(
            cls._from_json_list(response_raw)
        )

    @property
    def DeviceServer(self):
        """
        :rtype: DeviceServer
        """

        return self._DeviceServer

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self._DeviceServer is not None:
            return self._DeviceServer

        raise exception.BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._DeviceServer is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Device
        """

        return converter.json_to_class(Device, json_str)


class DraftShareInviteApiKeyQrCodeContent(core.BunqModel):
    """
    This call returns the raw content of the QR code that links to this draft
    share invite. When a bunq user scans this QR code with the bunq app the
    draft share invite will be shown on his/her device.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/draft-share-invite-api-key/{}/qr-code-content"

    # Object type.
    _OBJECT_TYPE_GET = "DraftShareInviteApiKeyQrCodeContent"

    @classmethod
    def list(cls, draft_share_invite_api_key_id, custom_headers=None):
        """
        Returns the raw content of the QR code that links to this draft share
        invite. The raw content is the binary representation of a file, without
        any JSON wrapping.
        
        :type user_id: int
        :type draft_share_invite_api_key_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(), draft_share_invite_api_key_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftShareInviteApiKeyQrCodeContent
        """

        return converter.json_to_class(DraftShareInviteApiKeyQrCodeContent,
                                       json_str)


class DraftShareInviteApiKey(core.BunqModel):
    """
    Used to create a draft share invite for a user with another bunq user. The
    user that accepts the invite can share his MAs with the user that created
    the invite.
    
    :param _user_alias_created: The user who created the draft share invite.
    :type _user_alias_created: object_.LabelUser
    :param _status: The status of the draft share invite. Can be USED, CANCELLED
    and PENDING.
    :type _status: str
    :param _sub_status: The sub-status of the draft share invite. Can be NONE,
    ACCEPTED or REJECTED.
    :type _sub_status: str
    :param _expiration: The moment when this draft share invite expires.
    :type _expiration: str
    :param _draft_share_url: The URL redirecting user to the draft share invite
    in the app. Only works on mobile devices.
    :type _draft_share_url: str
    :param _api_key: The API key generated for this DraftShareInviteApiKey.
    :type _api_key: str
    :param _id_: The id of the newly created draft share invite.
    :type _id_: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/draft-share-invite-api-key"
    _ENDPOINT_URL_READ = "user/{}/draft-share-invite-api-key/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/draft-share-invite-api-key/{}"
    _ENDPOINT_URL_LISTING = "user/{}/draft-share-invite-api-key"

    # Field constants.
    FIELD_STATUS = "status"
    FIELD_SUB_STATUS = "sub_status"
    FIELD_EXPIRATION = "expiration"

    # Object type.
    _OBJECT_TYPE_GET = "DraftShareInviteApiKey"
    _OBJECT_TYPE_PUT = "DraftShareInviteApiKey"

    def __init__(self):
        self._user_alias_created = None
        self._status = None
        self._sub_status = None
        self._expiration = None
        self._draft_share_url = None
        self._api_key = None
        self._id_ = None

    @classmethod
    def create(cls, expiration, status=None, sub_status=None,
               custom_headers=None):
        """
        :type user_id: int
        :param expiration: The moment when this draft share invite expires.
        :type expiration: str
        :param status: The status of the draft share invite. Can be CANCELLED
        (the user cancels the draft share before it's used).
        :type status: str
        :param sub_status: The sub-status of the draft share invite. Can be
        NONE, ACCEPTED or REJECTED.
        :type sub_status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_STATUS: status,
            cls.FIELD_SUB_STATUS: sub_status,
            cls.FIELD_EXPIRATION: expiration
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, draft_share_invite_api_key_id, custom_headers=None):
        """
        Get the details of a specific draft of a share invite.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type draft_share_invite_api_key_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDraftShareInviteApiKey
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     draft_share_invite_api_key_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseDraftShareInviteApiKey.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, draft_share_invite_api_key_id, status=None, sub_status=None,
               expiration=None, custom_headers=None):
        """
        Update a draft share invite. When sending status CANCELLED it is
        possible to cancel the draft share invite.
        
        :type user_id: int
        :type draft_share_invite_api_key_id: int
        :param status: The status of the draft share invite. Can be CANCELLED
        (the user cancels the draft share before it's used).
        :type status: str
        :param sub_status: The sub-status of the draft share invite. Can be
        NONE, ACCEPTED or REJECTED.
        :type sub_status: str
        :param expiration: The moment when this draft share invite expires.
        :type expiration: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDraftShareInviteApiKey
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status,
            cls.FIELD_SUB_STATUS: sub_status,
            cls.FIELD_EXPIRATION: expiration
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       draft_share_invite_api_key_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseDraftShareInviteApiKey.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_PUT)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDraftShareInviteApiKeyList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseDraftShareInviteApiKeyList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def user_alias_created(self):
        """
        :rtype: object_.LabelUser
        """

        return self._user_alias_created

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def sub_status(self):
        """
        :rtype: str
        """

        return self._sub_status

    @property
    def expiration(self):
        """
        :rtype: str
        """

        return self._expiration

    @property
    def draft_share_url(self):
        """
        :rtype: str
        """

        return self._draft_share_url

    @property
    def api_key(self):
        """
        :rtype: str
        """

        return self._api_key

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._user_alias_created is not None:
            return False

        if self._status is not None:
            return False

        if self._sub_status is not None:
            return False

        if self._expiration is not None:
            return False

        if self._draft_share_url is not None:
            return False

        if self._api_key is not None:
            return False

        if self._id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftShareInviteApiKey
        """

        return converter.json_to_class(DraftShareInviteApiKey, json_str)


class DraftShareInviteBankQrCodeContent(core.BunqModel):
    """
    This call returns the raw content of the QR code that links to this draft
    share invite. When a bunq user scans this QR code with the bunq app the
    draft share invite will be shown on his/her device.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/draft-share-invite-bank/{}/qr-code-content"

    # Object type.
    _OBJECT_TYPE_GET = "DraftShareInviteBankQrCodeContent"

    @classmethod
    def list(cls, draft_share_invite_bank_id, custom_headers=None):
        """
        Returns the raw content of the QR code that links to this draft share
        invite. The raw content is the binary representation of a file, without
        any JSON wrapping.
        
        :type user_id: int
        :type draft_share_invite_bank_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(), draft_share_invite_bank_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftShareInviteBankQrCodeContent
        """

        return converter.json_to_class(DraftShareInviteBankQrCodeContent,
                                       json_str)


class DraftShareInviteBank(core.BunqModel):
    """
    Used to create a draft share invite for a monetary account with another bunq
    user, as in the 'Connect' feature in the bunq app. The user that accepts the
    invite can share one of their MonetaryAccounts with the user that created
    the invite.
    
    :param _user_alias_created: The user who created the draft share invite.
    :type _user_alias_created: object_.LabelUser
    :param _status: The status of the draft share invite. Can be USED, CANCELLED
    and PENDING.
    :type _status: str
    :param _expiration: The moment when this draft share invite expires.
    :type _expiration: str
    :param _share_invite_bank_response_id: The id of the share invite bank
    response this draft share belongs to.
    :type _share_invite_bank_response_id: int
    :param _draft_share_url: The URL redirecting user to the draft share invite
    in the app. Only works on mobile devices.
    :type _draft_share_url: str
    :param _draft_share_settings: The draft share invite details.
    :type _draft_share_settings: object_.DraftShareInviteEntry
    :param _id_: The id of the newly created draft share invite.
    :type _id_: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/draft-share-invite-bank"
    _ENDPOINT_URL_READ = "user/{}/draft-share-invite-bank/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/draft-share-invite-bank/{}"
    _ENDPOINT_URL_LISTING = "user/{}/draft-share-invite-bank"

    # Field constants.
    FIELD_STATUS = "status"
    FIELD_EXPIRATION = "expiration"
    FIELD_DRAFT_SHARE_SETTINGS = "draft_share_settings"

    # Object type.
    _OBJECT_TYPE_GET = "DraftShareInviteBank"

    def __init__(self):
        self._user_alias_created = None
        self._status = None
        self._expiration = None
        self._share_invite_bank_response_id = None
        self._draft_share_url = None
        self._draft_share_settings = None
        self._id_ = None

    @classmethod
    def create(cls, expiration, draft_share_settings, status=None,
               custom_headers=None):
        """
        :type user_id: int
        :param expiration: The moment when this draft share invite expires.
        :type expiration: str
        :param draft_share_settings: The draft share invite details.
        :type draft_share_settings: object_.DraftShareInviteEntry
        :param status: The status of the draft share invite. Can be CANCELLED
        (the user cancels the draft share before it's used).
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_STATUS: status,
            cls.FIELD_EXPIRATION: expiration,
            cls.FIELD_DRAFT_SHARE_SETTINGS: draft_share_settings
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, draft_share_invite_bank_id, custom_headers=None):
        """
        Get the details of a specific draft of a share invite.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type draft_share_invite_bank_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDraftShareInviteBank
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     draft_share_invite_bank_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseDraftShareInviteBank.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, draft_share_invite_bank_id, status=None, expiration=None,
               draft_share_settings=None, custom_headers=None):
        """
        Update a draft share invite. When sending status CANCELLED it is
        possible to cancel the draft share invite.
        
        :type user_id: int
        :type draft_share_invite_bank_id: int
        :param status: The status of the draft share invite. Can be CANCELLED
        (the user cancels the draft share before it's used).
        :type status: str
        :param expiration: The moment when this draft share invite expires.
        :type expiration: str
        :param draft_share_settings: The draft share invite details.
        :type draft_share_settings: object_.DraftShareInviteEntry
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status,
            cls.FIELD_EXPIRATION: expiration,
            cls.FIELD_DRAFT_SHARE_SETTINGS: draft_share_settings
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       draft_share_invite_bank_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDraftShareInviteBankList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseDraftShareInviteBankList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def user_alias_created(self):
        """
        :rtype: object_.LabelUser
        """

        return self._user_alias_created

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def expiration(self):
        """
        :rtype: str
        """

        return self._expiration

    @property
    def share_invite_bank_response_id(self):
        """
        :rtype: int
        """

        return self._share_invite_bank_response_id

    @property
    def draft_share_url(self):
        """
        :rtype: str
        """

        return self._draft_share_url

    @property
    def draft_share_settings(self):
        """
        :rtype: object_.DraftShareInviteEntry
        """

        return self._draft_share_settings

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._user_alias_created is not None:
            return False

        if self._status is not None:
            return False

        if self._expiration is not None:
            return False

        if self._share_invite_bank_response_id is not None:
            return False

        if self._draft_share_url is not None:
            return False

        if self._draft_share_settings is not None:
            return False

        if self._id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftShareInviteBank
        """

        return converter.json_to_class(DraftShareInviteBank, json_str)


class ExportAnnualOverviewContent(core.BunqModel):
    """
    Fetch the raw content of an annual overview. The annual overview is always
    in PDF format. Doc won't display the response of a request to get the
    content of an annual overview.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/export-annual-overview/{}/content"

    # Object type.
    _OBJECT_TYPE_GET = "ExportAnnualOverviewContent"

    @classmethod
    def list(cls, export_annual_overview_id, custom_headers=None):
        """
        Used to retrieve the raw content of an annual overview.
        
        :type user_id: int
        :type export_annual_overview_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(), export_annual_overview_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ExportAnnualOverviewContent
        """

        return converter.json_to_class(ExportAnnualOverviewContent, json_str)


class ExportAnnualOverview(core.BunqModel):
    """
    Used to create new and read existing annual overviews of all the user's
    monetary accounts. Once created, annual overviews can be downloaded in PDF
    format via the 'export-annual-overview/{id}/content' endpoint.
    
    :param _id_: The id of the annual overview as created on the server.
    :type _id_: int
    :param _created: The timestamp of the annual overview 's creation.
    :type _created: str
    :param _updated: The timestamp of the annual overview 's last update.
    :type _updated: str
    :param _year: The year for which the overview is.
    :type _year: int
    :param _alias_user: The user to which this annual overview belongs.
    :type _alias_user: object_.LabelUser
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/export-annual-overview"
    _ENDPOINT_URL_READ = "user/{}/export-annual-overview/{}"
    _ENDPOINT_URL_LISTING = "user/{}/export-annual-overview"

    # Field constants.
    FIELD_YEAR = "year"

    # Object type.
    _OBJECT_TYPE_GET = "ExportAnnualOverview"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._year = None
        self._alias_user = None

    @classmethod
    def create(cls, year, custom_headers=None):
        """
        Create a new annual overview for a specific year. An overview can be
        generated only for a past year.
        
        :type user_id: int
        :param year: The year for which the overview is.
        :type year: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_YEAR: year
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, export_annual_overview_id, custom_headers=None):
        """
        Get an annual overview for a user by its id.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type export_annual_overview_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseExportAnnualOverview
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     export_annual_overview_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseExportAnnualOverview.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        List all the annual overviews for a user.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseExportAnnualOverviewList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseExportAnnualOverviewList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def year(self):
        """
        :rtype: int
        """

        return self._year

    @property
    def alias_user(self):
        """
        :rtype: object_.LabelUser
        """

        return self._alias_user

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._year is not None:
            return False

        if self._alias_user is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ExportAnnualOverview
        """

        return converter.json_to_class(ExportAnnualOverview, json_str)


class CustomerStatementExportContent(core.BunqModel):
    """
    Fetch the raw content of a statement export. The returned file format could
    be MT940, CSV or PDF depending on the statement format specified during the
    statement creation. The doc won't display the response of a request to get
    the content of a statement export.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/customer-statement/{}/content"

    # Object type.
    _OBJECT_TYPE_GET = "CustomerStatementExportContent"

    @classmethod
    def list(cls, customer_statement_id, monetary_account_id=None,
             custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type customer_statement_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            customer_statement_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CustomerStatementExportContent
        """

        return converter.json_to_class(CustomerStatementExportContent, json_str)


class CustomerStatementExport(core.BunqModel):
    """
    Used to create new and read existing statement exports. Statement exports
    can be created in either CSV, MT940 or PDF file format.
    
    :param _id_: The id of the customer statement model.
    :type _id_: int
    :param _created: The timestamp of the statement model's creation.
    :type _created: str
    :param _updated: The timestamp of the statement model's last update.
    :type _updated: str
    :param _date_start: The date from when this statement shows transactions.
    :type _date_start: str
    :param _date_end: The date until which statement shows transactions.
    :type _date_end: str
    :param _status: The status of the export.
    :type _status: str
    :param _statement_number: MT940 Statement number. Unique per monetary
    account.
    :type _statement_number: int
    :param _statement_format: The format of statement.
    :type _statement_format: str
    :param _regional_format: The regional format of a CSV statement.
    :type _regional_format: str
    :param _alias_monetary_account: The monetary account for which this
    statement was created.
    :type _alias_monetary_account: object_.MonetaryAccountReference
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/customer-statement"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/customer-statement/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/customer-statement"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/customer-statement/{}"

    # Field constants.
    FIELD_STATEMENT_FORMAT = "statement_format"
    FIELD_DATE_START = "date_start"
    FIELD_DATE_END = "date_end"
    FIELD_REGIONAL_FORMAT = "regional_format"

    # Object type.
    _OBJECT_TYPE_GET = "CustomerStatementExport"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._date_start = None
        self._date_end = None
        self._status = None
        self._statement_number = None
        self._statement_format = None
        self._regional_format = None
        self._alias_monetary_account = None

    @classmethod
    def create(cls, statement_format, date_start, date_end,
               monetary_account_id=None, regional_format=None,
               custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :param statement_format: The format type of statement. Allowed values:
        MT940, CSV, PDF.
        :type statement_format: str
        :param date_start: The start date for making statements.
        :type date_start: str
        :param date_end: The end date for making statements.
        :type date_end: str
        :param regional_format: Required for CSV exports. The regional format of
        the statement, can be UK_US (comma-separated) or EUROPEAN
        (semicolon-separated).
        :type regional_format: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_STATEMENT_FORMAT: statement_format,
            cls.FIELD_DATE_START: date_start,
            cls.FIELD_DATE_END: date_end,
            cls.FIELD_REGIONAL_FORMAT: regional_format
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, customer_statement_export_id, monetary_account_id=None,
            custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type customer_statement_export_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCustomerStatementExport
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     customer_statement_export_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCustomerStatementExport.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, monetary_account_id=None, params=None, custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCustomerStatementExportList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCustomerStatementExportList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def delete(cls, customer_statement_export_id, monetary_account_id=None,
               custom_headers=None):
        """
        :type user_id: int
        :type monetary_account_id: int
        :type customer_statement_export_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       customer_statement_export_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def date_start(self):
        """
        :rtype: str
        """

        return self._date_start

    @property
    def date_end(self):
        """
        :rtype: str
        """

        return self._date_end

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def statement_number(self):
        """
        :rtype: int
        """

        return self._statement_number

    @property
    def statement_format(self):
        """
        :rtype: str
        """

        return self._statement_format

    @property
    def regional_format(self):
        """
        :rtype: str
        """

        return self._regional_format

    @property
    def alias_monetary_account(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias_monetary_account

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._date_start is not None:
            return False

        if self._date_end is not None:
            return False

        if self._status is not None:
            return False

        if self._statement_number is not None:
            return False

        if self._statement_format is not None:
            return False

        if self._regional_format is not None:
            return False

        if self._alias_monetary_account is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CustomerStatementExport
        """

        return converter.json_to_class(CustomerStatementExport, json_str)


class InstallationServerPublicKey(core.BunqModel):
    """
    Using /installation/_/server-public-key you can request the ServerPublicKey
    again. This is done by referring to the id of the Installation.
    
    :param _server_public_key: The server's public key for this Installation.
    :type _server_public_key: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "installation/{}/server-public-key"

    # Object type.
    _OBJECT_TYPE_GET = "ServerPublicKey"

    def __init__(self):
        self._server_public_key = None

    @classmethod
    def list(cls, installation_id, params=None, custom_headers=None):
        """
        Show the ServerPublicKey for this Installation.
        
        :type installation_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInstallationServerPublicKeyList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(installation_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseInstallationServerPublicKeyList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def server_public_key(self):
        """
        :rtype: str
        """

        return self._server_public_key

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._server_public_key is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: InstallationServerPublicKey
        """

        return converter.json_to_class(InstallationServerPublicKey, json_str)


class ShareInviteBankAmountUsed(core.BunqModel):
    """
    When you have connected your monetary account bank to a user, and given this
    user a (for example) daily budget of 10 EUR. If this users has used his
    entire budget or part of it, this call can be used to reset the amount he
    used to 0. The user can then spend the daily budget of 10 EUR again.
    """

    # Endpoint constants.
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/share-invite-bank-inquiry/{}/amount-used/{}"

    @classmethod
    def delete(cls, share_invite_bank_inquiry_id,
               share_invite_bank_amount_used_id, monetary_account_id=None,
               custom_headers=None):
        """
        Reset the available budget for a bank account share. To be called
        without any ID at the end of the path.
        
        :type user_id: int
        :type monetary_account_id: int
        :type share_invite_bank_inquiry_id: int
        :type share_invite_bank_amount_used_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       share_invite_bank_inquiry_id,
                                                       share_invite_bank_amount_used_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareInviteBankAmountUsed
        """

        return converter.json_to_class(ShareInviteBankAmountUsed, json_str)


class MonetaryAccountBank(core.BunqModel):
    """
    With MonetaryAccountBank you can create a new bank account, retrieve
    information regarding your existing MonetaryAccountBanks and update specific
    fields of an existing MonetaryAccountBank. Examples of fields that can be
    updated are the description, the daily limit and the avatar of the
    account.<br/><br/>Notification filters can be set on a monetary account
    level to receive callbacks. For more information check the <a
    href="/api/1/page/callbacks">dedicated callbacks page</a>.
    
    :param _id_: The id of the MonetaryAccountBank.
    :type _id_: int
    :param _created: The timestamp of the MonetaryAccountBank's creation.
    :type _created: str
    :param _updated: The timestamp of the MonetaryAccountBank's last update.
    :type _updated: str
    :param _avatar: The Avatar of the MonetaryAccountBank.
    :type _avatar: object_.Avatar
    :param _currency: The currency of the MonetaryAccountBank as an ISO 4217
    formatted currency code.
    :type _currency: str
    :param _description: The description of the MonetaryAccountBank. Defaults to
    'bunq account'.
    :type _description: str
    :param _daily_limit: The daily spending limit Amount of the
    MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the
    MonetaryAccountBank's currency. Limited to 10000 EUR.
    :type _daily_limit: object_.Amount
    :param _daily_spent: Total Amount of money spent today. Timezone aware.
    :type _daily_spent: object_.Amount
    :param _overdraft_limit: The maximum Amount the MonetaryAccountBank can be
    'in the red'.
    :type _overdraft_limit: object_.Amount
    :param _balance: The current balance Amount of the MonetaryAccountBank.
    :type _balance: object_.Amount
    :param _alias: The Aliases for the MonetaryAccountBank.
    :type _alias: list[object_.Pointer]
    :param _public_uuid: The MonetaryAccountBank's public UUID.
    :type _public_uuid: str
    :param _status: The status of the MonetaryAccountBank. Can be: ACTIVE,
    BLOCKED, CANCELLED or PENDING_REOPEN
    :type _status: str
    :param _sub_status: The sub-status of the MonetaryAccountBank providing
    extra information regarding the status. Will be NONE for ACTIVE or
    PENDING_REOPEN, COMPLETELY or ONLY_ACCEPTING_INCOMING for BLOCKED and
    REDEMPTION_INVOLUNTARY, REDEMPTION_VOLUNTARY or PERMANENT for CANCELLED.
    :type _sub_status: str
    :param _reason: The reason for voluntarily cancelling (closing) the
    MonetaryAccountBank, can only be OTHER.
    :type _reason: str
    :param _reason_description: The optional free-form reason for voluntarily
    cancelling (closing) the MonetaryAccountBank. Can be any user provided
    message.
    :type _reason_description: str
    :param _user_id: The id of the User who owns the MonetaryAccountBank.
    :type _user_id: int
    :param _monetary_account_profile: The profile of the account.
    :type _monetary_account_profile: MonetaryAccountProfile
    :param _notification_filters: The types of notifications that will result in
    a push notification or URL callback for this MonetaryAccountBank.
    :type _notification_filters: list[object_.NotificationFilter]
    :param _setting: The settings of the MonetaryAccountBank.
    :type _setting: object_.MonetaryAccountSetting
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account-bank"
    _ENDPOINT_URL_READ = "user/{}/monetary-account-bank/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account-bank/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account-bank"

    # Field constants.
    FIELD_CURRENCY = "currency"
    FIELD_DESCRIPTION = "description"
    FIELD_DAILY_LIMIT = "daily_limit"
    FIELD_AVATAR_UUID = "avatar_uuid"
    FIELD_STATUS = "status"
    FIELD_SUB_STATUS = "sub_status"
    FIELD_REASON = "reason"
    FIELD_REASON_DESCRIPTION = "reason_description"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"
    FIELD_SETTING = "setting"

    # Object type.
    _OBJECT_TYPE_GET = "MonetaryAccountBank"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._avatar = None
        self._currency = None
        self._description = None
        self._daily_limit = None
        self._daily_spent = None
        self._overdraft_limit = None
        self._balance = None
        self._alias = None
        self._public_uuid = None
        self._status = None
        self._sub_status = None
        self._reason = None
        self._reason_description = None
        self._user_id = None
        self._monetary_account_profile = None
        self._notification_filters = None
        self._setting = None

    @classmethod
    def create(cls, currency, description=None, daily_limit=None,
               avatar_uuid=None, status=None, sub_status=None, reason=None,
               reason_description=None, notification_filters=None, setting=None,
               custom_headers=None):
        """
        Create new MonetaryAccountBank.
        
        :type user_id: int
        :param currency: The currency of the MonetaryAccountBank as an ISO 4217
        formatted currency code.
        :type currency: str
        :param description: The description of the MonetaryAccountBank. Defaults
        to 'bunq account'.
        :type description: str
        :param daily_limit: The daily spending limit Amount of the
        MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the
        MonetaryAccountBank's currency. Limited to 10000 EUR.
        :type daily_limit: object_.Amount
        :param avatar_uuid: The UUID of the Avatar of the MonetaryAccountBank.
        :type avatar_uuid: str
        :param status: The status of the MonetaryAccountBank. Ignored in POST
        requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in
        PUT requests to cancel (close) or reopen the MonetaryAccountBank. When
        updating the status and/or sub_status no other fields can be updated in
        the same request (and vice versa).
        :type status: str
        :param sub_status: The sub-status of the MonetaryAccountBank providing
        extra information regarding the status. Should be ignored for POST
        requests. In case of PUT requests with status CANCELLED it can only be
        REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be
        NONE. When updating the status and/or sub_status no other fields can be
        updated in the same request (and vice versa).
        :type sub_status: str
        :param reason: The reason for voluntarily cancelling (closing) the
        MonetaryAccountBank, can only be OTHER. Should only be specified if
        updating the status to CANCELLED.
        :type reason: str
        :param reason_description: The optional free-form reason for voluntarily
        cancelling (closing) the MonetaryAccountBank. Can be any user provided
        message. Should only be specified if updating the status to CANCELLED.
        :type reason_description: str
        :param notification_filters: The types of notifications that will result
        in a push notification or URL callback for this MonetaryAccountBank.
        :type notification_filters: list[object_.NotificationFilter]
        :param setting: The settings of the MonetaryAccountBank.
        :type setting: object_.MonetaryAccountSetting
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_CURRENCY: currency,
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_DAILY_LIMIT: daily_limit,
            cls.FIELD_AVATAR_UUID: avatar_uuid,
            cls.FIELD_STATUS: status,
            cls.FIELD_SUB_STATUS: sub_status,
            cls.FIELD_REASON: reason,
            cls.FIELD_REASON_DESCRIPTION: reason_description,
            cls.FIELD_NOTIFICATION_FILTERS: notification_filters,
            cls.FIELD_SETTING: setting
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, monetary_account_bank_id, custom_headers=None):
        """
        Get a specific MonetaryAccountBank.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_bank_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseMonetaryAccountBank
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     monetary_account_bank_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseMonetaryAccountBank.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, monetary_account_bank_id, description=None,
               daily_limit=None, avatar_uuid=None, status=None, sub_status=None,
               reason=None, reason_description=None, notification_filters=None,
               setting=None, custom_headers=None):
        """
        Update a specific existing MonetaryAccountBank.
        
        :type user_id: int
        :type monetary_account_bank_id: int
        :param description: The description of the MonetaryAccountBank. Defaults
        to 'bunq account'.
        :type description: str
        :param daily_limit: The daily spending limit Amount of the
        MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the
        MonetaryAccountBank's currency. Limited to 10000 EUR.
        :type daily_limit: object_.Amount
        :param avatar_uuid: The UUID of the Avatar of the MonetaryAccountBank.
        :type avatar_uuid: str
        :param status: The status of the MonetaryAccountBank. Ignored in POST
        requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in
        PUT requests to cancel (close) or reopen the MonetaryAccountBank. When
        updating the status and/or sub_status no other fields can be updated in
        the same request (and vice versa).
        :type status: str
        :param sub_status: The sub-status of the MonetaryAccountBank providing
        extra information regarding the status. Should be ignored for POST
        requests. In case of PUT requests with status CANCELLED it can only be
        REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be
        NONE. When updating the status and/or sub_status no other fields can be
        updated in the same request (and vice versa).
        :type sub_status: str
        :param reason: The reason for voluntarily cancelling (closing) the
        MonetaryAccountBank, can only be OTHER. Should only be specified if
        updating the status to CANCELLED.
        :type reason: str
        :param reason_description: The optional free-form reason for voluntarily
        cancelling (closing) the MonetaryAccountBank. Can be any user provided
        message. Should only be specified if updating the status to CANCELLED.
        :type reason_description: str
        :param notification_filters: The types of notifications that will result
        in a push notification or URL callback for this MonetaryAccountBank.
        :type notification_filters: list[object_.NotificationFilter]
        :param setting: The settings of the MonetaryAccountBank.
        :type setting: object_.MonetaryAccountSetting
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_DAILY_LIMIT: daily_limit,
            cls.FIELD_AVATAR_UUID: avatar_uuid,
            cls.FIELD_STATUS: status,
            cls.FIELD_SUB_STATUS: sub_status,
            cls.FIELD_REASON: reason,
            cls.FIELD_REASON_DESCRIPTION: reason_description,
            cls.FIELD_NOTIFICATION_FILTERS: notification_filters,
            cls.FIELD_SETTING: setting
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       monetary_account_bank_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Gets a listing of all MonetaryAccountBanks of a given user.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseMonetaryAccountBankList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseMonetaryAccountBankList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def avatar(self):
        """
        :rtype: object_.Avatar
        """

        return self._avatar

    @property
    def currency(self):
        """
        :rtype: str
        """

        return self._currency

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def daily_limit(self):
        """
        :rtype: object_.Amount
        """

        return self._daily_limit

    @property
    def daily_spent(self):
        """
        :rtype: object_.Amount
        """

        return self._daily_spent

    @property
    def overdraft_limit(self):
        """
        :rtype: object_.Amount
        """

        return self._overdraft_limit

    @property
    def balance(self):
        """
        :rtype: object_.Amount
        """

        return self._balance

    @property
    def alias(self):
        """
        :rtype: list[object_.Pointer]
        """

        return self._alias

    @property
    def public_uuid(self):
        """
        :rtype: str
        """

        return self._public_uuid

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def sub_status(self):
        """
        :rtype: str
        """

        return self._sub_status

    @property
    def reason(self):
        """
        :rtype: str
        """

        return self._reason

    @property
    def reason_description(self):
        """
        :rtype: str
        """

        return self._reason_description

    @property
    def user_id(self):
        """
        :rtype: int
        """

        return self._user_id

    @property
    def monetary_account_profile(self):
        """
        :rtype: MonetaryAccountProfile
        """

        return self._monetary_account_profile

    @property
    def notification_filters(self):
        """
        :rtype: list[object_.NotificationFilter]
        """

        return self._notification_filters

    @property
    def setting(self):
        """
        :rtype: object_.MonetaryAccountSetting
        """

        return self._setting

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._avatar is not None:
            return False

        if self._currency is not None:
            return False

        if self._description is not None:
            return False

        if self._daily_limit is not None:
            return False

        if self._daily_spent is not None:
            return False

        if self._overdraft_limit is not None:
            return False

        if self._balance is not None:
            return False

        if self._alias is not None:
            return False

        if self._public_uuid is not None:
            return False

        if self._status is not None:
            return False

        if self._sub_status is not None:
            return False

        if self._reason is not None:
            return False

        if self._reason_description is not None:
            return False

        if self._user_id is not None:
            return False

        if self._monetary_account_profile is not None:
            return False

        if self._notification_filters is not None:
            return False

        if self._setting is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccountBank
        """

        return converter.json_to_class(MonetaryAccountBank, json_str)


class MonetaryAccountProfile(core.BunqModel):
    """
    Used to update and read up monetary account profiles, to keep the balance
    between specific thresholds.
    
    :param _profile_fill: The profile settings for triggering the fill of a
    monetary account.
    :type _profile_fill: object_.MonetaryAccountProfileFill
    :param _profile_drain: The profile settings for moving excesses to a savings
    account
    :type _profile_drain: object_.MonetaryAccountProfileDrain
    """

    # Field constants.
    FIELD_PROFILE_FILL = "profile_fill"
    FIELD_PROFILE_DRAIN = "profile_drain"

    def __init__(self):
        self._profile_fill = None
        self._profile_drain = None

    @property
    def profile_fill(self):
        """
        :rtype: object_.MonetaryAccountProfileFill
        """

        return self._profile_fill

    @property
    def profile_drain(self):
        """
        :rtype: object_.MonetaryAccountProfileDrain
        """

        return self._profile_drain

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._profile_fill is not None:
            return False

        if self._profile_drain is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccountProfile
        """

        return converter.json_to_class(MonetaryAccountProfile, json_str)


class MonetaryAccount(core.BunqModel, core.AnchoredObjectInterface):
    """
    Used to show the MonetaryAccounts that you can access. Currently the only
    MonetaryAccount type is MonetaryAccountBank. See also:
    monetary-account-bank.<br/><br/>Notification filters can be set on a
    monetary account level to receive callbacks. For more information check the
    <a href="/api/2/page/callbacks">dedicated callbacks page</a>.
    
    :param _MonetaryAccountBank: 
    :type _MonetaryAccountBank: MonetaryAccountBank
    :param _MonetaryAccountJoint: 
    :type _MonetaryAccountJoint: MonetaryAccountJoint
    :param _MonetaryAccountLight: 
    :type _MonetaryAccountLight: MonetaryAccountLight
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account"

    # Object type.
    _OBJECT_TYPE_GET = "MonetaryAccount"

    def __init__(self):
        self._MonetaryAccountBank = None
        self._MonetaryAccountJoint = None
        self._MonetaryAccountLight = None

    @classmethod
    def get(cls, monetary_account_id, custom_headers=None):
        """
        Get a specific MonetaryAccount.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseMonetaryAccount
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id))
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseMonetaryAccount.cast_from_bunq_response(
            cls._from_json(response_raw)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Get a collection of all your MonetaryAccounts.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseMonetaryAccountList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseMonetaryAccountList.cast_from_bunq_response(
            cls._from_json_list(response_raw)
        )

    @property
    def MonetaryAccountBank(self):
        """
        :rtype: MonetaryAccountBank
        """

        return self._MonetaryAccountBank

    @property
    def MonetaryAccountJoint(self):
        """
        :rtype: MonetaryAccountJoint
        """

        return self._MonetaryAccountJoint

    @property
    def MonetaryAccountLight(self):
        """
        :rtype: MonetaryAccountLight
        """

        return self._MonetaryAccountLight

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self._MonetaryAccountBank is not None:
            return self._MonetaryAccountBank

        if self._MonetaryAccountJoint is not None:
            return self._MonetaryAccountJoint

        if self._MonetaryAccountLight is not None:
            return self._MonetaryAccountLight

        raise exception.BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._MonetaryAccountBank is not None:
            return False

        if self._MonetaryAccountJoint is not None:
            return False

        if self._MonetaryAccountLight is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccount
        """

        return converter.json_to_class(MonetaryAccount, json_str)


class MonetaryAccountJoint(core.BunqModel):
    """
    The endpoint for joint monetary accounts.
    
    :param _id_: The id of the MonetaryAccountJoint.
    :type _id_: int
    :param _created: The timestamp of the MonetaryAccountJoint's creation.
    :type _created: str
    :param _updated: The timestamp of the MonetaryAccountJoint's last update.
    :type _updated: str
    :param _avatar: The Avatar of the MonetaryAccountJoint.
    :type _avatar: object_.Avatar
    :param _currency: The currency of the MonetaryAccountJoint as an ISO 4217
    formatted currency code.
    :type _currency: str
    :param _description: The description of the MonetaryAccountJoint. Defaults
    to 'bunq account'.
    :type _description: str
    :param _daily_limit: The daily spending limit Amount of the
    MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the
    MonetaryAccountJoint's currency. Limited to 10000 EUR.
    :type _daily_limit: object_.Amount
    :param _daily_spent: Total Amount of money spent today. Timezone aware.
    :type _daily_spent: object_.Amount
    :param _overdraft_limit: The maximum Amount the MonetaryAccountJoint can be
    'in the red'.
    :type _overdraft_limit: object_.Amount
    :param _balance: The current balance Amount of the MonetaryAccountJoint.
    :type _balance: object_.Amount
    :param _alias: The Aliases for the MonetaryAccountJoint.
    :type _alias: list[object_.Pointer]
    :param _public_uuid: The MonetaryAccountJoint's public UUID.
    :type _public_uuid: str
    :param _status: The status of the MonetaryAccountJoint. Can be: ACTIVE,
    BLOCKED, CANCELLED or PENDING_REOPEN
    :type _status: str
    :param _sub_status: The sub-status of the MonetaryAccountJoint providing
    extra information regarding the status. Will be NONE for ACTIVE or
    PENDING_REOPEN, COMPLETELY or ONLY_ACCEPTING_INCOMING for BLOCKED and
    REDEMPTION_INVOLUNTARY, REDEMPTION_VOLUNTARY or PERMANENT for CANCELLED.
    :type _sub_status: str
    :param _reason: The reason for voluntarily cancelling (closing) the
    MonetaryAccountJoint, can only be OTHER.
    :type _reason: str
    :param _reason_description: The optional free-form reason for voluntarily
    cancelling (closing) the MonetaryAccountJoint. Can be any user provided
    message.
    :type _reason_description: str
    :param _all_co_owner: The users the account will be joint with.
    :type _all_co_owner: list[object_.CoOwner]
    :param _user_id: The id of the User who owns the MonetaryAccountJoint.
    :type _user_id: int
    :param _monetary_account_profile: The profile of the account.
    :type _monetary_account_profile: MonetaryAccountProfile
    :param _notification_filters: The types of notifications that will result in
    a push notification or URL callback for this MonetaryAccountJoint.
    :type _notification_filters: list[object_.NotificationFilter]
    :param _setting: The settings of the MonetaryAccountJoint.
    :type _setting: object_.MonetaryAccountSetting
    """

    # Field constants.
    FIELD_CURRENCY = "currency"
    FIELD_DESCRIPTION = "description"
    FIELD_DAILY_LIMIT = "daily_limit"
    FIELD_OVERDRAFT_LIMIT = "overdraft_limit"
    FIELD_ALIAS = "alias"
    FIELD_AVATAR_UUID = "avatar_uuid"
    FIELD_STATUS = "status"
    FIELD_SUB_STATUS = "sub_status"
    FIELD_REASON = "reason"
    FIELD_REASON_DESCRIPTION = "reason_description"
    FIELD_ALL_CO_OWNER = "all_co_owner"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"
    FIELD_SETTING = "setting"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._avatar = None
        self._currency = None
        self._description = None
        self._daily_limit = None
        self._daily_spent = None
        self._overdraft_limit = None
        self._balance = None
        self._alias = None
        self._public_uuid = None
        self._status = None
        self._sub_status = None
        self._reason = None
        self._reason_description = None
        self._all_co_owner = None
        self._user_id = None
        self._monetary_account_profile = None
        self._notification_filters = None
        self._setting = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def avatar(self):
        """
        :rtype: object_.Avatar
        """

        return self._avatar

    @property
    def currency(self):
        """
        :rtype: str
        """

        return self._currency

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def daily_limit(self):
        """
        :rtype: object_.Amount
        """

        return self._daily_limit

    @property
    def daily_spent(self):
        """
        :rtype: object_.Amount
        """

        return self._daily_spent

    @property
    def overdraft_limit(self):
        """
        :rtype: object_.Amount
        """

        return self._overdraft_limit

    @property
    def balance(self):
        """
        :rtype: object_.Amount
        """

        return self._balance

    @property
    def alias(self):
        """
        :rtype: list[object_.Pointer]
        """

        return self._alias

    @property
    def public_uuid(self):
        """
        :rtype: str
        """

        return self._public_uuid

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def sub_status(self):
        """
        :rtype: str
        """

        return self._sub_status

    @property
    def reason(self):
        """
        :rtype: str
        """

        return self._reason

    @property
    def reason_description(self):
        """
        :rtype: str
        """

        return self._reason_description

    @property
    def all_co_owner(self):
        """
        :rtype: list[object_.CoOwner]
        """

        return self._all_co_owner

    @property
    def user_id(self):
        """
        :rtype: int
        """

        return self._user_id

    @property
    def monetary_account_profile(self):
        """
        :rtype: MonetaryAccountProfile
        """

        return self._monetary_account_profile

    @property
    def notification_filters(self):
        """
        :rtype: list[object_.NotificationFilter]
        """

        return self._notification_filters

    @property
    def setting(self):
        """
        :rtype: object_.MonetaryAccountSetting
        """

        return self._setting

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._avatar is not None:
            return False

        if self._currency is not None:
            return False

        if self._description is not None:
            return False

        if self._daily_limit is not None:
            return False

        if self._daily_spent is not None:
            return False

        if self._overdraft_limit is not None:
            return False

        if self._balance is not None:
            return False

        if self._alias is not None:
            return False

        if self._public_uuid is not None:
            return False

        if self._status is not None:
            return False

        if self._sub_status is not None:
            return False

        if self._reason is not None:
            return False

        if self._reason_description is not None:
            return False

        if self._all_co_owner is not None:
            return False

        if self._user_id is not None:
            return False

        if self._monetary_account_profile is not None:
            return False

        if self._notification_filters is not None:
            return False

        if self._setting is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccountJoint
        """

        return converter.json_to_class(MonetaryAccountJoint, json_str)


class MonetaryAccountLight(core.BunqModel):
    """
    With MonetaryAccountLight is a monetary account for bunq light users.
    Through this endpoint you can retrieve information regarding your existing
    MonetaryAccountLights and update specific fields of an existing
    MonetaryAccountLight. Examples of fields that can be updated are the
    description, the daily limit and the avatar of the account.
    
    :param _id_: The id of the MonetaryAccountLight.
    :type _id_: int
    :param _created: The timestamp of the MonetaryAccountLight's creation.
    :type _created: str
    :param _updated: The timestamp of the MonetaryAccountLight's last update.
    :type _updated: str
    :param _avatar: The Avatar of the MonetaryAccountLight.
    :type _avatar: object_.Avatar
    :param _currency: The currency of the MonetaryAccountLight as an ISO 4217
    formatted currency code.
    :type _currency: str
    :param _description: The description of the MonetaryAccountLight. Defaults
    to 'bunq account'.
    :type _description: str
    :param _daily_limit: The daily spending limit Amount of the
    MonetaryAccountLight. Defaults to 1000 EUR. Currency must match the
    MonetaryAccountLight's currency. Limited to 10000 EUR.
    :type _daily_limit: object_.Amount
    :param _daily_spent: Total Amount of money spent today. Timezone aware.
    :type _daily_spent: object_.Amount
    :param _balance: The current balance Amount of the MonetaryAccountLight.
    :type _balance: object_.Amount
    :param _alias: The Aliases for the MonetaryAccountLight.
    :type _alias: list[object_.Pointer]
    :param _public_uuid: The MonetaryAccountLight's public UUID.
    :type _public_uuid: str
    :param _status: The status of the MonetaryAccountLight. Can be: ACTIVE,
    BLOCKED, CANCELLED or PENDING_REOPEN
    :type _status: str
    :param _sub_status: The sub-status of the MonetaryAccountLight providing
    extra information regarding the status. Will be NONE for ACTIVE or
    PENDING_REOPEN, COMPLETELY or ONLY_ACCEPTING_INCOMING for BLOCKED and
    REDEMPTION_INVOLUNTARY, REDEMPTION_VOLUNTARY or PERMANENT for CANCELLED.
    :type _sub_status: str
    :param _reason: The reason for voluntarily cancelling (closing) the
    MonetaryAccountBank, can only be OTHER.
    :type _reason: str
    :param _reason_description: The optional free-form reason for voluntarily
    cancelling (closing) the MonetaryAccountBank. Can be any user provided
    message.
    :type _reason_description: str
    :param _user_id: The id of the User who owns the MonetaryAccountLight.
    :type _user_id: int
    :param _balance_maximum: The maximum balance Amount of the
    MonetaryAccountLight.
    :type _balance_maximum: object_.Amount
    :param _budget_month_used: The amount of the monthly budget used.
    :type _budget_month_used: object_.Amount
    :param _budget_month_maximum: The total amount of the monthly budget.
    :type _budget_month_maximum: object_.Amount
    :param _budget_year_used: The amount of the yearly budget used.
    :type _budget_year_used: object_.Amount
    :param _budget_year_maximum: The total amount of the yearly budget.
    :type _budget_year_maximum: object_.Amount
    :param _budget_withdrawal_year_used: The amount of the yearly withdrawal
    budget used.
    :type _budget_withdrawal_year_used: object_.Amount
    :param _budget_withdrawal_year_maximum: The total amount of the yearly
    withdrawal budget.
    :type _budget_withdrawal_year_maximum: object_.Amount
    :param _notification_filters: The types of notifications that will result in
    a push notification or URL callback for this MonetaryAccountLight.
    :type _notification_filters: list[object_.NotificationFilter]
    :param _setting: The settings of the MonetaryAccountLight.
    :type _setting: object_.MonetaryAccountSetting
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account-light"
    _ENDPOINT_URL_READ = "user/{}/monetary-account-light/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account-light/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account-light"

    # Field constants.
    FIELD_CURRENCY = "currency"
    FIELD_DESCRIPTION = "description"
    FIELD_DAILY_LIMIT = "daily_limit"
    FIELD_AVATAR_UUID = "avatar_uuid"
    FIELD_STATUS = "status"
    FIELD_SUB_STATUS = "sub_status"
    FIELD_REASON = "reason"
    FIELD_REASON_DESCRIPTION = "reason_description"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"
    FIELD_SETTING = "setting"

    # Object type.
    _OBJECT_TYPE_GET = "MonetaryAccountLight"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._avatar = None
        self._currency = None
        self._description = None
        self._daily_limit = None
        self._daily_spent = None
        self._balance = None
        self._alias = None
        self._public_uuid = None
        self._status = None
        self._sub_status = None
        self._reason = None
        self._reason_description = None
        self._user_id = None
        self._balance_maximum = None
        self._budget_month_used = None
        self._budget_month_maximum = None
        self._budget_year_used = None
        self._budget_year_maximum = None
        self._budget_withdrawal_year_used = None
        self._budget_withdrawal_year_maximum = None
        self._notification_filters = None
        self._setting = None

    @classmethod
    def create(cls, currency, description=None, daily_limit=None,
               avatar_uuid=None, status=None, sub_status=None, reason=None,
               reason_description=None, notification_filters=None, setting=None,
               custom_headers=None):
        """
        Create new MonetaryAccountLight.
        
        :type user_id: int
        :param currency: The currency of the MonetaryAccountLight as an ISO 4217
        formatted currency code.
        :type currency: str
        :param description: The description of the MonetaryAccountLight.
        Defaults to 'bunq account'.
        :type description: str
        :param daily_limit: The daily spending limit Amount of the
        MonetaryAccountLight. Defaults to 1000 EUR. Currency must match the
        MonetaryAccountLight's currency. Limited to 10000 EUR.
        :type daily_limit: object_.Amount
        :param avatar_uuid: The UUID of the Avatar of the MonetaryAccountLight.
        :type avatar_uuid: str
        :param status: The status of the MonetaryAccountLight. Ignored in POST
        requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in
        PUT requests to cancel (close) or reopen the MonetaryAccountLight. When
        updating the status and/or sub_status no other fields can be updated in
        the same request (and vice versa).
        :type status: str
        :param sub_status: The sub-status of the MonetaryAccountLight providing
        extra information regarding the status. Should be ignored for POST
        requests and can only be REDEMPTION_VOLUNTARY for PUT requests with
        status CANCELLED. When updating the status and/or sub_status no other
        fields can be updated in the same request (and vice versa).
        :type sub_status: str
        :param reason: The reason for voluntarily cancelling (closing) the
        MonetaryAccountBank, can only be OTHER. Should only be specified if
        updating the status to CANCELLED.
        :type reason: str
        :param reason_description: The optional free-form reason for voluntarily
        cancelling (closing) the MonetaryAccountBank. Can be any user provided
        message. Should only be specified if updating the status to CANCELLED.
        :type reason_description: str
        :param notification_filters: The types of notifications that will result
        in a push notification or URL callback for this MonetaryAccountLight.
        :type notification_filters: list[object_.NotificationFilter]
        :param setting: The settings of the MonetaryAccountLight.
        :type setting: object_.MonetaryAccountSetting
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_CURRENCY: currency,
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_DAILY_LIMIT: daily_limit,
            cls.FIELD_AVATAR_UUID: avatar_uuid,
            cls.FIELD_STATUS: status,
            cls.FIELD_SUB_STATUS: sub_status,
            cls.FIELD_REASON: reason,
            cls.FIELD_REASON_DESCRIPTION: reason_description,
            cls.FIELD_NOTIFICATION_FILTERS: notification_filters,
            cls.FIELD_SETTING: setting
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, monetary_account_light_id, custom_headers=None):
        """
        Get a specific MonetaryAccountLight.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_light_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseMonetaryAccountLight
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     monetary_account_light_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseMonetaryAccountLight.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, monetary_account_light_id, description=None,
               daily_limit=None, avatar_uuid=None, status=None, sub_status=None,
               reason=None, reason_description=None, notification_filters=None,
               setting=None, custom_headers=None):
        """
        Update a specific existing MonetaryAccountLight.
        
        :type user_id: int
        :type monetary_account_light_id: int
        :param description: The description of the MonetaryAccountLight.
        Defaults to 'bunq account'.
        :type description: str
        :param daily_limit: The daily spending limit Amount of the
        MonetaryAccountLight. Defaults to 1000 EUR. Currency must match the
        MonetaryAccountLight's currency. Limited to 10000 EUR.
        :type daily_limit: object_.Amount
        :param avatar_uuid: The UUID of the Avatar of the MonetaryAccountLight.
        :type avatar_uuid: str
        :param status: The status of the MonetaryAccountLight. Ignored in POST
        requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in
        PUT requests to cancel (close) or reopen the MonetaryAccountLight. When
        updating the status and/or sub_status no other fields can be updated in
        the same request (and vice versa).
        :type status: str
        :param sub_status: The sub-status of the MonetaryAccountLight providing
        extra information regarding the status. Should be ignored for POST
        requests and can only be REDEMPTION_VOLUNTARY for PUT requests with
        status CANCELLED. When updating the status and/or sub_status no other
        fields can be updated in the same request (and vice versa).
        :type sub_status: str
        :param reason: The reason for voluntarily cancelling (closing) the
        MonetaryAccountBank, can only be OTHER. Should only be specified if
        updating the status to CANCELLED.
        :type reason: str
        :param reason_description: The optional free-form reason for voluntarily
        cancelling (closing) the MonetaryAccountBank. Can be any user provided
        message. Should only be specified if updating the status to CANCELLED.
        :type reason_description: str
        :param notification_filters: The types of notifications that will result
        in a push notification or URL callback for this MonetaryAccountLight.
        :type notification_filters: list[object_.NotificationFilter]
        :param setting: The settings of the MonetaryAccountLight.
        :type setting: object_.MonetaryAccountSetting
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_DAILY_LIMIT: daily_limit,
            cls.FIELD_AVATAR_UUID: avatar_uuid,
            cls.FIELD_STATUS: status,
            cls.FIELD_SUB_STATUS: sub_status,
            cls.FIELD_REASON: reason,
            cls.FIELD_REASON_DESCRIPTION: reason_description,
            cls.FIELD_NOTIFICATION_FILTERS: notification_filters,
            cls.FIELD_SETTING: setting
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       monetary_account_light_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Gets a listing of all MonetaryAccountLights of a given user.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseMonetaryAccountLightList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseMonetaryAccountLightList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def avatar(self):
        """
        :rtype: object_.Avatar
        """

        return self._avatar

    @property
    def currency(self):
        """
        :rtype: str
        """

        return self._currency

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def daily_limit(self):
        """
        :rtype: object_.Amount
        """

        return self._daily_limit

    @property
    def daily_spent(self):
        """
        :rtype: object_.Amount
        """

        return self._daily_spent

    @property
    def balance(self):
        """
        :rtype: object_.Amount
        """

        return self._balance

    @property
    def alias(self):
        """
        :rtype: list[object_.Pointer]
        """

        return self._alias

    @property
    def public_uuid(self):
        """
        :rtype: str
        """

        return self._public_uuid

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def sub_status(self):
        """
        :rtype: str
        """

        return self._sub_status

    @property
    def reason(self):
        """
        :rtype: str
        """

        return self._reason

    @property
    def reason_description(self):
        """
        :rtype: str
        """

        return self._reason_description

    @property
    def user_id(self):
        """
        :rtype: int
        """

        return self._user_id

    @property
    def balance_maximum(self):
        """
        :rtype: object_.Amount
        """

        return self._balance_maximum

    @property
    def budget_month_used(self):
        """
        :rtype: object_.Amount
        """

        return self._budget_month_used

    @property
    def budget_month_maximum(self):
        """
        :rtype: object_.Amount
        """

        return self._budget_month_maximum

    @property
    def budget_year_used(self):
        """
        :rtype: object_.Amount
        """

        return self._budget_year_used

    @property
    def budget_year_maximum(self):
        """
        :rtype: object_.Amount
        """

        return self._budget_year_maximum

    @property
    def budget_withdrawal_year_used(self):
        """
        :rtype: object_.Amount
        """

        return self._budget_withdrawal_year_used

    @property
    def budget_withdrawal_year_maximum(self):
        """
        :rtype: object_.Amount
        """

        return self._budget_withdrawal_year_maximum

    @property
    def notification_filters(self):
        """
        :rtype: list[object_.NotificationFilter]
        """

        return self._notification_filters

    @property
    def setting(self):
        """
        :rtype: object_.MonetaryAccountSetting
        """

        return self._setting

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._avatar is not None:
            return False

        if self._currency is not None:
            return False

        if self._description is not None:
            return False

        if self._daily_limit is not None:
            return False

        if self._daily_spent is not None:
            return False

        if self._balance is not None:
            return False

        if self._alias is not None:
            return False

        if self._public_uuid is not None:
            return False

        if self._status is not None:
            return False

        if self._sub_status is not None:
            return False

        if self._reason is not None:
            return False

        if self._reason_description is not None:
            return False

        if self._user_id is not None:
            return False

        if self._balance_maximum is not None:
            return False

        if self._budget_month_used is not None:
            return False

        if self._budget_month_maximum is not None:
            return False

        if self._budget_year_used is not None:
            return False

        if self._budget_year_maximum is not None:
            return False

        if self._budget_withdrawal_year_used is not None:
            return False

        if self._budget_withdrawal_year_maximum is not None:
            return False

        if self._notification_filters is not None:
            return False

        if self._setting is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccountLight
        """

        return converter.json_to_class(MonetaryAccountLight, json_str)


class BunqMeFundraiserResult(core.BunqModel):
    """
    bunq.me fundraiser result containing all payments.
    
    :param _id_: The id of the bunq.me.
    :type _id_: int
    :param _created: The timestamp when the bunq.me was created.
    :type _created: str
    :param _updated: The timestamp when the bunq.me was last updated.
    :type _updated: str
    :param _bunqme_fundraiser_profile: The bunq.me fundraiser profile.
    :type _bunqme_fundraiser_profile: BunqMeFundraiserProfile
    :param _payments: The list of payments, paid to the bunq.me fundraiser
    profile.
    :type _payments: list[Payment]
    """

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._bunqme_fundraiser_profile = None
        self._payments = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def bunqme_fundraiser_profile(self):
        """
        :rtype: BunqMeFundraiserProfile
        """

        return self._bunqme_fundraiser_profile

    @property
    def payments(self):
        """
        :rtype: list[Payment]
        """

        return self._payments

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._bunqme_fundraiser_profile is not None:
            return False

        if self._payments is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BunqMeFundraiserResult
        """

        return converter.json_to_class(BunqMeFundraiserResult, json_str)


class BunqMeFundraiserProfile(core.BunqModel):
    """
    bunq.me public profile of the user.
    
    :param _color: The color chosen for the bunq.me fundraiser profile in
    hexadecimal format.
    :type _color: str
    :param _alias: The LabelMonetaryAccount with the public information of the
    User and the MonetaryAccount that created the bunq.me fundraiser profile.
    :type _alias: object_.MonetaryAccountReference
    :param _description: The description of the bunq.me fundraiser profile.
    :type _description: str
    :param _attachment: The attachments attached to the fundraiser profile.
    :type _attachment: list[object_.AttachmentPublic]
    :param _pointer: The pointer (url) which will be used to access the bunq.me
    fundraiser profile.
    :type _pointer: object_.MonetaryAccountReference
    :param _status: The status of the bunq.me fundraiser profile, can be ACTIVE
    or DEACTIVATED.
    :type _status: str
    :param _redirect_url: The URL which the user is sent to when a payment is
    completed.
    :type _redirect_url: str
    """

    # Field constants.
    FIELD_POINTER = "pointer"

    def __init__(self):
        self._color = None
        self._alias = None
        self._description = None
        self._attachment = None
        self._pointer = None
        self._status = None
        self._redirect_url = None

    @property
    def color(self):
        """
        :rtype: str
        """

        return self._color

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def attachment(self):
        """
        :rtype: list[object_.AttachmentPublic]
        """

        return self._attachment

    @property
    def pointer(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._pointer

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def redirect_url(self):
        """
        :rtype: str
        """

        return self._redirect_url

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._color is not None:
            return False

        if self._alias is not None:
            return False

        if self._description is not None:
            return False

        if self._attachment is not None:
            return False

        if self._pointer is not None:
            return False

        if self._status is not None:
            return False

        if self._redirect_url is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BunqMeFundraiserProfile
        """

        return converter.json_to_class(BunqMeFundraiserProfile, json_str)


class BunqMeTabResultResponse(core.BunqModel):
    """
    Used to view bunq.me TabResultResponse objects belonging to a tab. A
    TabResultResponse is an object that holds details on a tab which has been
    paid from the provided monetary account.
    
    :param _payment: The payment made for the bunq.me tab.
    :type _payment: Payment
    """

    def __init__(self):
        self._payment = None

    @property
    def payment(self):
        """
        :rtype: Payment
        """

        return self._payment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._payment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BunqMeTabResultResponse
        """

        return converter.json_to_class(BunqMeTabResultResponse, json_str)


class TabResultInquiry(core.BunqModel):
    """
    Used to view TabResultInquiry objects belonging to a tab. A TabResultInquiry
    is an object that holds details on both the tab and a single payment made
    for that tab.
    
    :param _tab: The Tab details.
    :type _tab: Tab
    :param _payment: The payment made for the Tab.
    :type _payment: Payment
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-result-inquiry/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-result-inquiry"

    # Object type.
    _OBJECT_TYPE_GET = "TabResultInquiry"

    def __init__(self):
        self._tab = None
        self._payment = None

    @classmethod
    def get(cls, cash_register_id, tab_uuid, tab_result_inquiry_id,
            monetary_account_id=None, custom_headers=None):
        """
        Used to view a single TabResultInquiry belonging to a tab.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type tab_result_inquiry_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabResultInquiry
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     cash_register_id, tab_uuid,
                                                     tab_result_inquiry_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabResultInquiry.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, cash_register_id, tab_uuid, monetary_account_id=None,
             params=None, custom_headers=None):
        """
        Used to view a list of TabResultInquiry objects belonging to a tab.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabResultInquiryList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            cash_register_id, tab_uuid)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabResultInquiryList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def tab(self):
        """
        :rtype: Tab
        """

        return self._tab

    @property
    def payment(self):
        """
        :rtype: Payment
        """

        return self._payment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._tab is not None:
            return False

        if self._payment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabResultInquiry
        """

        return converter.json_to_class(TabResultInquiry, json_str)


class User(core.BunqModel, core.AnchoredObjectInterface):
    """
    Using this call you can retrieve information of the user you are logged in
    as. This includes your user id, which is referred to in endpoints.
    
    :param _UserLight: 
    :type _UserLight: UserLight
    :param _UserPerson: 
    :type _UserPerson: UserPerson
    :param _UserCompany: 
    :type _UserCompany: UserCompany
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}"
    _ENDPOINT_URL_LISTING = "user"

    # Object type.
    _OBJECT_TYPE_GET = "User"

    def __init__(self):
        self._UserLight = None
        self._UserPerson = None
        self._UserCompany = None

    @classmethod
    def get(cls, custom_headers=None):
        """
        Get a specific user.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUser
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseUser.cast_from_bunq_response(
            cls._from_json(response_raw)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Get a collection of all available users.
        
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseUserList.cast_from_bunq_response(
            cls._from_json_list(response_raw)
        )

    @property
    def UserLight(self):
        """
        :rtype: UserLight
        """

        return self._UserLight

    @property
    def UserPerson(self):
        """
        :rtype: UserPerson
        """

        return self._UserPerson

    @property
    def UserCompany(self):
        """
        :rtype: UserCompany
        """

        return self._UserCompany

    def get_referenced_object(self):
        """
        :rtype: core.BunqModel
        :raise: BunqException
        """

        if self._UserLight is not None:
            return self._UserLight

        if self._UserPerson is not None:
            return self._UserPerson

        if self._UserCompany is not None:
            return self._UserCompany

        raise exception.BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._UserLight is not None:
            return False

        if self._UserPerson is not None:
            return False

        if self._UserCompany is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: User
        """

        return converter.json_to_class(User, json_str)


class UserLight(core.BunqModel):
    """
    Show the authenticated user, if it is a light user.
    
    :param _id_: The id of the user.
    :type _id_: int
    :param _created: The timestamp of the user object's creation.
    :type _created: str
    :param _updated: The timestamp of the user object's last update.
    :type _updated: str
    :param _public_uuid: The user's public UUID.
    :type _public_uuid: str
    :param _first_name: The user's first name.
    :type _first_name: str
    :param _middle_name: The user's middle name.
    :type _middle_name: str
    :param _last_name: The user's last name.
    :type _last_name: str
    :param _legal_name: The user's legal name.
    :type _legal_name: str
    :param _display_name: The display name for the user.
    :type _display_name: str
    :param _public_nick_name: The public nick name for the user.
    :type _public_nick_name: str
    :param _alias: The aliases of the user.
    :type _alias: list[object_.Pointer]
    :param _social_security_number: The user's social security number.
    :type _social_security_number: str
    :param _tax_resident: The user's tax residence numbers for different
    countries.
    :type _tax_resident: list[object_.TaxResident]
    :param _document_type: The type of identification document the user
    registered with.
    :type _document_type: str
    :param _document_number: The identification document number the user
    registered with.
    :type _document_number: str
    :param _document_country_of_issuance: The country which issued the
    identification document the user registered with.
    :type _document_country_of_issuance: str
    :param _address_main: The user's main address.
    :type _address_main: object_.Address
    :param _address_postal: The user's postal address.
    :type _address_postal: object_.Address
    :param _date_of_birth: The user's date of birth. Accepts ISO8601 date
    formats.
    :type _date_of_birth: str
    :param _place_of_birth: The user's place of birth.
    :type _place_of_birth: str
    :param _country_of_birth: The user's country of birth. Formatted as a SO
    3166-1 alpha-2 country code.
    :type _country_of_birth: str
    :param _nationality: The user's nationality. Formatted as a SO 3166-1
    alpha-2 country code.
    :type _nationality: str
    :param _language: The user's preferred language. Formatted as a ISO 639-1
    language code plus a ISO 3166-1 alpha-2 country code, seperated by an
    underscore.
    :type _language: str
    :param _region: The user's preferred region. Formatted as a ISO 639-1
    language code plus a ISO 3166-1 alpha-2 country code, seperated by an
    underscore.
    :type _region: str
    :param _gender: The user's gender. Can be MALE, FEMALE or UNKNOWN.
    :type _gender: str
    :param _avatar: The user's avatar.
    :type _avatar: object_.Avatar
    :param _version_terms_of_service: The version of the terms of service
    accepted by the user.
    :type _version_terms_of_service: str
    :param _status: The user status. The user status. Can be: ACTIVE, BLOCKED,
    SIGNUP, DENIED or ABORTED.
    :type _status: str
    :param _sub_status: The user sub-status. Can be: NONE, FACE_RESET, APPROVAL,
    APPROVAL_PARENT, AWAITING_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or
    SUBMIT.
    :type _sub_status: str
    :param _session_timeout: The setting for the session timeout of the user in
    seconds.
    :type _session_timeout: int
    :param _daily_limit_without_confirmation_login: The amount the user can pay
    in the session without asking for credentials.
    :type _daily_limit_without_confirmation_login: object_.Amount
    :param _notification_filters: The types of notifications that will result in
    a push notification or URL callback for this UserLight.
    :type _notification_filters: list[object_.NotificationFilter]
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user-light/{}"

    # Field constants.
    FIELD_FIRST_NAME = "first_name"
    FIELD_MIDDLE_NAME = "middle_name"
    FIELD_LAST_NAME = "last_name"
    FIELD_PUBLIC_NICK_NAME = "public_nick_name"
    FIELD_ADDRESS_MAIN = "address_main"
    FIELD_ADDRESS_POSTAL = "address_postal"
    FIELD_AVATAR_UUID = "avatar_uuid"
    FIELD_SOCIAL_SECURITY_NUMBER = "social_security_number"
    FIELD_TAX_RESIDENT = "tax_resident"
    FIELD_DOCUMENT_TYPE = "document_type"
    FIELD_DOCUMENT_NUMBER = "document_number"
    FIELD_DOCUMENT_COUNTRY_OF_ISSUANCE = "document_country_of_issuance"
    FIELD_DOCUMENT_FRONT_ATTACHMENT_ID = "document_front_attachment_id"
    FIELD_DOCUMENT_BACK_ATTACHMENT_ID = "document_back_attachment_id"
    FIELD_DATE_OF_BIRTH = "date_of_birth"
    FIELD_PLACE_OF_BIRTH = "place_of_birth"
    FIELD_COUNTRY_OF_BIRTH = "country_of_birth"
    FIELD_NATIONALITY = "nationality"
    FIELD_LANGUAGE = "language"
    FIELD_REGION = "region"
    FIELD_GENDER = "gender"
    FIELD_STATUS = "status"
    FIELD_SUB_STATUS = "sub_status"
    FIELD_LEGAL_GUARDIAN_ALIAS = "legal_guardian_alias"
    FIELD_SESSION_TIMEOUT = "session_timeout"
    FIELD_DAILY_LIMIT_WITHOUT_CONFIRMATION_LOGIN = "daily_limit_without_confirmation_login"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"

    # Object type.
    _OBJECT_TYPE_GET = "UserPerson"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._public_uuid = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._legal_name = None
        self._display_name = None
        self._public_nick_name = None
        self._alias = None
        self._social_security_number = None
        self._tax_resident = None
        self._document_type = None
        self._document_number = None
        self._document_country_of_issuance = None
        self._address_main = None
        self._address_postal = None
        self._date_of_birth = None
        self._place_of_birth = None
        self._country_of_birth = None
        self._nationality = None
        self._language = None
        self._region = None
        self._gender = None
        self._avatar = None
        self._version_terms_of_service = None
        self._status = None
        self._sub_status = None
        self._session_timeout = None
        self._daily_limit_without_confirmation_login = None
        self._notification_filters = None

    @classmethod
    def get(cls, user_light_id, custom_headers=None):
        """
        Get a specific bunq light user.
        
        :type api_context: context.ApiContext
        :type user_light_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserLight
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_light_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseUserLight.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def public_uuid(self):
        """
        :rtype: str
        """

        return self._public_uuid

    @property
    def first_name(self):
        """
        :rtype: str
        """

        return self._first_name

    @property
    def middle_name(self):
        """
        :rtype: str
        """

        return self._middle_name

    @property
    def last_name(self):
        """
        :rtype: str
        """

        return self._last_name

    @property
    def legal_name(self):
        """
        :rtype: str
        """

        return self._legal_name

    @property
    def display_name(self):
        """
        :rtype: str
        """

        return self._display_name

    @property
    def public_nick_name(self):
        """
        :rtype: str
        """

        return self._public_nick_name

    @property
    def alias(self):
        """
        :rtype: list[object_.Pointer]
        """

        return self._alias

    @property
    def social_security_number(self):
        """
        :rtype: str
        """

        return self._social_security_number

    @property
    def tax_resident(self):
        """
        :rtype: list[object_.TaxResident]
        """

        return self._tax_resident

    @property
    def document_type(self):
        """
        :rtype: str
        """

        return self._document_type

    @property
    def document_number(self):
        """
        :rtype: str
        """

        return self._document_number

    @property
    def document_country_of_issuance(self):
        """
        :rtype: str
        """

        return self._document_country_of_issuance

    @property
    def address_main(self):
        """
        :rtype: object_.Address
        """

        return self._address_main

    @property
    def address_postal(self):
        """
        :rtype: object_.Address
        """

        return self._address_postal

    @property
    def date_of_birth(self):
        """
        :rtype: str
        """

        return self._date_of_birth

    @property
    def place_of_birth(self):
        """
        :rtype: str
        """

        return self._place_of_birth

    @property
    def country_of_birth(self):
        """
        :rtype: str
        """

        return self._country_of_birth

    @property
    def nationality(self):
        """
        :rtype: str
        """

        return self._nationality

    @property
    def language(self):
        """
        :rtype: str
        """

        return self._language

    @property
    def region(self):
        """
        :rtype: str
        """

        return self._region

    @property
    def gender(self):
        """
        :rtype: str
        """

        return self._gender

    @property
    def avatar(self):
        """
        :rtype: object_.Avatar
        """

        return self._avatar

    @property
    def version_terms_of_service(self):
        """
        :rtype: str
        """

        return self._version_terms_of_service

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def sub_status(self):
        """
        :rtype: str
        """

        return self._sub_status

    @property
    def session_timeout(self):
        """
        :rtype: int
        """

        return self._session_timeout

    @property
    def daily_limit_without_confirmation_login(self):
        """
        :rtype: object_.Amount
        """

        return self._daily_limit_without_confirmation_login

    @property
    def notification_filters(self):
        """
        :rtype: list[object_.NotificationFilter]
        """

        return self._notification_filters

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._public_uuid is not None:
            return False

        if self._first_name is not None:
            return False

        if self._middle_name is not None:
            return False

        if self._last_name is not None:
            return False

        if self._legal_name is not None:
            return False

        if self._display_name is not None:
            return False

        if self._public_nick_name is not None:
            return False

        if self._alias is not None:
            return False

        if self._social_security_number is not None:
            return False

        if self._tax_resident is not None:
            return False

        if self._document_type is not None:
            return False

        if self._document_number is not None:
            return False

        if self._document_country_of_issuance is not None:
            return False

        if self._address_main is not None:
            return False

        if self._address_postal is not None:
            return False

        if self._date_of_birth is not None:
            return False

        if self._place_of_birth is not None:
            return False

        if self._country_of_birth is not None:
            return False

        if self._nationality is not None:
            return False

        if self._language is not None:
            return False

        if self._region is not None:
            return False

        if self._gender is not None:
            return False

        if self._avatar is not None:
            return False

        if self._version_terms_of_service is not None:
            return False

        if self._status is not None:
            return False

        if self._sub_status is not None:
            return False

        if self._session_timeout is not None:
            return False

        if self._daily_limit_without_confirmation_login is not None:
            return False

        if self._notification_filters is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: UserLight
        """

        return converter.json_to_class(UserLight, json_str)


class UserPerson(core.BunqModel):
    """
    With UserPerson you can retrieve information regarding the authenticated
    UserPerson and update specific fields.<br/><br/>Notification filters can be
    set on a UserPerson level to receive callbacks. For more information check
    the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
    
    :param _id_: The id of the modified person object.
    :type _id_: int
    :param _created: The timestamp of the person object's creation.
    :type _created: str
    :param _updated: The timestamp of the person object's last update.
    :type _updated: str
    :param _public_uuid: The person's public UUID.
    :type _public_uuid: str
    :param _first_name: The person's first name.
    :type _first_name: str
    :param _middle_name: The person's middle name.
    :type _middle_name: str
    :param _last_name: The person's last name.
    :type _last_name: str
    :param _legal_name: The person's legal name.
    :type _legal_name: str
    :param _display_name: The display name for the person.
    :type _display_name: str
    :param _public_nick_name: The public nick name for the person.
    :type _public_nick_name: str
    :param _alias: The aliases of the user.
    :type _alias: list[object_.Pointer]
    :param _tax_resident: The user's tax residence numbers for different
    countries.
    :type _tax_resident: list[object_.TaxResident]
    :param _document_type: The type of identification document the person
    registered with.
    :type _document_type: str
    :param _document_number: The identification document number the person
    registered with.
    :type _document_number: str
    :param _document_country_of_issuance: The country which issued the
    identification document the person registered with.
    :type _document_country_of_issuance: str
    :param _address_main: The person's main address.
    :type _address_main: object_.Address
    :param _address_postal: The person's postal address.
    :type _address_postal: object_.Address
    :param _date_of_birth: The person's date of birth. Accepts ISO8601 date
    formats.
    :type _date_of_birth: str
    :param _place_of_birth: The person's place of birth.
    :type _place_of_birth: str
    :param _country_of_birth: The person's country of birth. Formatted as a SO
    3166-1 alpha-2 country code.
    :type _country_of_birth: str
    :param _nationality: The person's nationality. Formatted as a SO 3166-1
    alpha-2 country code.
    :type _nationality: str
    :param _language: The person's preferred language. Formatted as a ISO 639-1
    language code plus a ISO 3166-1 alpha-2 country code, seperated by an
    underscore.
    :type _language: str
    :param _region: The person's preferred region. Formatted as a ISO 639-1
    language code plus a ISO 3166-1 alpha-2 country code, seperated by an
    underscore.
    :type _region: str
    :param _gender: The person's gender. Can be MALE, FEMALE or UNKNOWN.
    :type _gender: str
    :param _avatar: The user's avatar.
    :type _avatar: object_.Avatar
    :param _version_terms_of_service: The version of the terms of service
    accepted by the user.
    :type _version_terms_of_service: str
    :param _status: The user status. The user status. Can be: ACTIVE, BLOCKED,
    SIGNUP, RECOVERY, DENIED or ABORTED.
    :type _status: str
    :param _sub_status: The user sub-status. Can be: NONE, FACE_RESET, APPROVAL,
    APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or
    SUBMIT.
    :type _sub_status: str
    :param _session_timeout: The setting for the session timeout of the user in
    seconds.
    :type _session_timeout: int
    :param _daily_limit_without_confirmation_login: The amount the user can pay
    in the session without asking for credentials.
    :type _daily_limit_without_confirmation_login: object_.Amount
    :param _notification_filters: The types of notifications that will result in
    a push notification or URL callback for this UserPerson.
    :type _notification_filters: list[object_.NotificationFilter]
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user-person/{}"
    _ENDPOINT_URL_UPDATE = "user-person/{}"

    # Field constants.
    FIELD_FIRST_NAME = "first_name"
    FIELD_MIDDLE_NAME = "middle_name"
    FIELD_LAST_NAME = "last_name"
    FIELD_PUBLIC_NICK_NAME = "public_nick_name"
    FIELD_ADDRESS_MAIN = "address_main"
    FIELD_ADDRESS_POSTAL = "address_postal"
    FIELD_AVATAR_UUID = "avatar_uuid"
    FIELD_TAX_RESIDENT = "tax_resident"
    FIELD_DOCUMENT_TYPE = "document_type"
    FIELD_DOCUMENT_NUMBER = "document_number"
    FIELD_DOCUMENT_COUNTRY_OF_ISSUANCE = "document_country_of_issuance"
    FIELD_DOCUMENT_FRONT_ATTACHMENT_ID = "document_front_attachment_id"
    FIELD_DOCUMENT_BACK_ATTACHMENT_ID = "document_back_attachment_id"
    FIELD_DATE_OF_BIRTH = "date_of_birth"
    FIELD_PLACE_OF_BIRTH = "place_of_birth"
    FIELD_COUNTRY_OF_BIRTH = "country_of_birth"
    FIELD_NATIONALITY = "nationality"
    FIELD_LANGUAGE = "language"
    FIELD_REGION = "region"
    FIELD_GENDER = "gender"
    FIELD_STATUS = "status"
    FIELD_SUB_STATUS = "sub_status"
    FIELD_LEGAL_GUARDIAN_ALIAS = "legal_guardian_alias"
    FIELD_SESSION_TIMEOUT = "session_timeout"
    FIELD_CARD_IDS = "card_ids"
    FIELD_CARD_LIMITS = "card_limits"
    FIELD_DAILY_LIMIT_WITHOUT_CONFIRMATION_LOGIN = "daily_limit_without_confirmation_login"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"

    # Object type.
    _OBJECT_TYPE_GET = "UserPerson"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._public_uuid = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._legal_name = None
        self._display_name = None
        self._public_nick_name = None
        self._alias = None
        self._tax_resident = None
        self._document_type = None
        self._document_number = None
        self._document_country_of_issuance = None
        self._address_main = None
        self._address_postal = None
        self._date_of_birth = None
        self._place_of_birth = None
        self._country_of_birth = None
        self._nationality = None
        self._language = None
        self._region = None
        self._gender = None
        self._avatar = None
        self._version_terms_of_service = None
        self._status = None
        self._sub_status = None
        self._session_timeout = None
        self._daily_limit_without_confirmation_login = None
        self._notification_filters = None

    @classmethod
    def get(cls, custom_headers=None):
        """
        Get a specific person.
        
        :type api_context: context.ApiContext
        :type user_person_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserPerson
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseUserPerson.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, first_name=None, middle_name=None, last_name=None,
               public_nick_name=None, address_main=None, address_postal=None,
               avatar_uuid=None, tax_resident=None, document_type=None,
               document_number=None, document_country_of_issuance=None,
               document_front_attachment_id=None,
               document_back_attachment_id=None, date_of_birth=None,
               place_of_birth=None, country_of_birth=None, nationality=None,
               language=None, region=None, gender=None, status=None,
               sub_status=None, legal_guardian_alias=None, session_timeout=None,
               card_ids=None, card_limits=None,
               daily_limit_without_confirmation_login=None,
               notification_filters=None, custom_headers=None):
        """
        Modify a specific person object's data.
        
        :type user_person_id: int
        :param first_name: The person's first name.
        :type first_name: str
        :param middle_name: The person's middle name.
        :type middle_name: str
        :param last_name: The person's last name.
        :type last_name: str
        :param public_nick_name: The person's public nick name.
        :type public_nick_name: str
        :param address_main: The user's main address.
        :type address_main: object_.Address
        :param address_postal: The person's postal address.
        :type address_postal: object_.Address
        :param avatar_uuid: The public UUID of the user's avatar.
        :type avatar_uuid: str
        :param tax_resident: The user's tax residence numbers for different
        countries.
        :type tax_resident: list[object_.TaxResident]
        :param document_type: The type of identification document the person
        registered with.
        :type document_type: str
        :param document_number: The identification document number the person
        registered with.
        :type document_number: str
        :param document_country_of_issuance: The country which issued the
        identification document the person registered with.
        :type document_country_of_issuance: str
        :param document_front_attachment_id: The reference to the uploaded
        picture/scan of the front side of the identification document.
        :type document_front_attachment_id: int
        :param document_back_attachment_id: The reference to the uploaded
        picture/scan of the back side of the identification document.
        :type document_back_attachment_id: int
        :param date_of_birth: The person's date of birth. Accepts ISO8601 date
        formats.
        :type date_of_birth: str
        :param place_of_birth: The person's place of birth.
        :type place_of_birth: str
        :param country_of_birth: The person's country of birth. Formatted as a
        SO 3166-1 alpha-2 country code.
        :type country_of_birth: str
        :param nationality: The person's nationality. Formatted as a SO 3166-1
        alpha-2 country code.
        :type nationality: str
        :param language: The person's preferred language. Formatted as a ISO
        639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by
        an underscore.
        :type language: str
        :param region: The person's preferred region. Formatted as a ISO 639-1
        language code plus a ISO 3166-1 alpha-2 country code, seperated by an
        underscore.
        :type region: str
        :param gender: The person's gender. Can be: MALE, FEMALE and UNKNOWN.
        :type gender: str
        :param status: The user status. You are not allowed to update the status
        via PUT.
        :type status: str
        :param sub_status: The user sub-status. Can be updated to SUBMIT if
        status is RECOVERY.
        :type sub_status: str
        :param legal_guardian_alias: The legal guardian of the user. Required
        for minors.
        :type legal_guardian_alias: object_.Pointer
        :param session_timeout: The setting for the session timeout of the user
        in seconds.
        :type session_timeout: int
        :param card_ids: Card ids used for centralized card limits.
        :type card_ids: list[object_.BunqId]
        :param card_limits: The centralized limits for user's cards.
        :type card_limits: list[object_.CardLimit]
        :param daily_limit_without_confirmation_login: The amount the user can
        pay in the session without asking for credentials.
        :type daily_limit_without_confirmation_login: object_.Amount
        :param notification_filters: The types of notifications that will result
        in a push notification or URL callback for this UserPerson.
        :type notification_filters: list[object_.NotificationFilter]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_FIRST_NAME: first_name,
            cls.FIELD_MIDDLE_NAME: middle_name,
            cls.FIELD_LAST_NAME: last_name,
            cls.FIELD_PUBLIC_NICK_NAME: public_nick_name,
            cls.FIELD_ADDRESS_MAIN: address_main,
            cls.FIELD_ADDRESS_POSTAL: address_postal,
            cls.FIELD_AVATAR_UUID: avatar_uuid,
            cls.FIELD_TAX_RESIDENT: tax_resident,
            cls.FIELD_DOCUMENT_TYPE: document_type,
            cls.FIELD_DOCUMENT_NUMBER: document_number,
            cls.FIELD_DOCUMENT_COUNTRY_OF_ISSUANCE: document_country_of_issuance,
            cls.FIELD_DOCUMENT_FRONT_ATTACHMENT_ID: document_front_attachment_id,
            cls.FIELD_DOCUMENT_BACK_ATTACHMENT_ID: document_back_attachment_id,
            cls.FIELD_DATE_OF_BIRTH: date_of_birth,
            cls.FIELD_PLACE_OF_BIRTH: place_of_birth,
            cls.FIELD_COUNTRY_OF_BIRTH: country_of_birth,
            cls.FIELD_NATIONALITY: nationality,
            cls.FIELD_LANGUAGE: language,
            cls.FIELD_REGION: region,
            cls.FIELD_GENDER: gender,
            cls.FIELD_STATUS: status,
            cls.FIELD_SUB_STATUS: sub_status,
            cls.FIELD_LEGAL_GUARDIAN_ALIAS: legal_guardian_alias,
            cls.FIELD_SESSION_TIMEOUT: session_timeout,
            cls.FIELD_CARD_IDS: card_ids,
            cls.FIELD_CARD_LIMITS: card_limits,
            cls.FIELD_DAILY_LIMIT_WITHOUT_CONFIRMATION_LOGIN: daily_limit_without_confirmation_login,
            cls.FIELD_NOTIFICATION_FILTERS: notification_filters
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id())
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def public_uuid(self):
        """
        :rtype: str
        """

        return self._public_uuid

    @property
    def first_name(self):
        """
        :rtype: str
        """

        return self._first_name

    @property
    def middle_name(self):
        """
        :rtype: str
        """

        return self._middle_name

    @property
    def last_name(self):
        """
        :rtype: str
        """

        return self._last_name

    @property
    def legal_name(self):
        """
        :rtype: str
        """

        return self._legal_name

    @property
    def display_name(self):
        """
        :rtype: str
        """

        return self._display_name

    @property
    def public_nick_name(self):
        """
        :rtype: str
        """

        return self._public_nick_name

    @property
    def alias(self):
        """
        :rtype: list[object_.Pointer]
        """

        return self._alias

    @property
    def tax_resident(self):
        """
        :rtype: list[object_.TaxResident]
        """

        return self._tax_resident

    @property
    def document_type(self):
        """
        :rtype: str
        """

        return self._document_type

    @property
    def document_number(self):
        """
        :rtype: str
        """

        return self._document_number

    @property
    def document_country_of_issuance(self):
        """
        :rtype: str
        """

        return self._document_country_of_issuance

    @property
    def address_main(self):
        """
        :rtype: object_.Address
        """

        return self._address_main

    @property
    def address_postal(self):
        """
        :rtype: object_.Address
        """

        return self._address_postal

    @property
    def date_of_birth(self):
        """
        :rtype: str
        """

        return self._date_of_birth

    @property
    def place_of_birth(self):
        """
        :rtype: str
        """

        return self._place_of_birth

    @property
    def country_of_birth(self):
        """
        :rtype: str
        """

        return self._country_of_birth

    @property
    def nationality(self):
        """
        :rtype: str
        """

        return self._nationality

    @property
    def language(self):
        """
        :rtype: str
        """

        return self._language

    @property
    def region(self):
        """
        :rtype: str
        """

        return self._region

    @property
    def gender(self):
        """
        :rtype: str
        """

        return self._gender

    @property
    def avatar(self):
        """
        :rtype: object_.Avatar
        """

        return self._avatar

    @property
    def version_terms_of_service(self):
        """
        :rtype: str
        """

        return self._version_terms_of_service

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def sub_status(self):
        """
        :rtype: str
        """

        return self._sub_status

    @property
    def session_timeout(self):
        """
        :rtype: int
        """

        return self._session_timeout

    @property
    def daily_limit_without_confirmation_login(self):
        """
        :rtype: object_.Amount
        """

        return self._daily_limit_without_confirmation_login

    @property
    def notification_filters(self):
        """
        :rtype: list[object_.NotificationFilter]
        """

        return self._notification_filters

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._public_uuid is not None:
            return False

        if self._first_name is not None:
            return False

        if self._middle_name is not None:
            return False

        if self._last_name is not None:
            return False

        if self._legal_name is not None:
            return False

        if self._display_name is not None:
            return False

        if self._public_nick_name is not None:
            return False

        if self._alias is not None:
            return False

        if self._tax_resident is not None:
            return False

        if self._document_type is not None:
            return False

        if self._document_number is not None:
            return False

        if self._document_country_of_issuance is not None:
            return False

        if self._address_main is not None:
            return False

        if self._address_postal is not None:
            return False

        if self._date_of_birth is not None:
            return False

        if self._place_of_birth is not None:
            return False

        if self._country_of_birth is not None:
            return False

        if self._nationality is not None:
            return False

        if self._language is not None:
            return False

        if self._region is not None:
            return False

        if self._gender is not None:
            return False

        if self._avatar is not None:
            return False

        if self._version_terms_of_service is not None:
            return False

        if self._status is not None:
            return False

        if self._sub_status is not None:
            return False

        if self._session_timeout is not None:
            return False

        if self._daily_limit_without_confirmation_login is not None:
            return False

        if self._notification_filters is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: UserPerson
        """

        return converter.json_to_class(UserPerson, json_str)


class UserCompany(core.BunqModel):
    """
    With UserCompany you can retrieve information regarding the authenticated
    UserCompany and update specific fields.<br/><br/>Notification filters can be
    set on a UserCompany level to receive callbacks. For more information check
    the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
    
    :param _id_: The id of the modified company.
    :type _id_: int
    :param _created: The timestamp of the company object's creation.
    :type _created: str
    :param _updated: The timestamp of the company object's last update.
    :type _updated: str
    :param _public_uuid: The company's public UUID.
    :type _public_uuid: str
    :param _name: The company name.
    :type _name: str
    :param _display_name: The company's display name.
    :type _display_name: str
    :param _public_nick_name: The company's public nick name.
    :type _public_nick_name: str
    :param _alias: The aliases of the account.
    :type _alias: list[object_.Pointer]
    :param _chamber_of_commerce_number: The company's chamber of commerce
    number.
    :type _chamber_of_commerce_number: str
    :param _type_of_business_entity: The type of business entity.
    :type _type_of_business_entity: str
    :param _sector_of_industry: The sector of industry.
    :type _sector_of_industry: str
    :param _counter_bank_iban: The company's other bank account IBAN, through
    which we verify it.
    :type _counter_bank_iban: str
    :param _avatar: The company's avatar.
    :type _avatar: object_.Avatar
    :param _address_main: The company's main address.
    :type _address_main: object_.Address
    :param _address_postal: The company's postal address.
    :type _address_postal: object_.Address
    :param _version_terms_of_service: The version of the terms of service
    accepted by the user.
    :type _version_terms_of_service: str
    :param _director_alias: The existing bunq user alias for the company's
    director.
    :type _director_alias: object_.LabelUser
    :param _language: The person's preferred language. Formatted as a ISO 639-1
    language code plus a ISO 3166-1 alpha-2 country code, seperated by an
    underscore.
    :type _language: str
    :param _country: The country as an ISO 3166-1 alpha-2 country code..
    :type _country: str
    :param _region: The person's preferred region. Formatted as a ISO 639-1
    language code plus a ISO 3166-1 alpha-2 country code, seperated by an
    underscore.
    :type _region: str
    :param _ubo: The names of the company's ultimate beneficiary owners. Minimum
    zero, maximum four.
    :type _ubo: list[object_.Ubo]
    :param _status: The user status. Can be: ACTIVE, SIGNUP, RECOVERY.
    :type _status: str
    :param _sub_status: The user sub-status. Can be: NONE, FACE_RESET, APPROVAL,
    APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or
    SUBMIT.
    :type _sub_status: str
    :param _session_timeout: The setting for the session timeout of the company
    in seconds.
    :type _session_timeout: int
    :param _card_ids: Card ids used for centralized card limits.
    :type _card_ids: list[object_.BunqId]
    :param _card_limits: The centralized limits for user's cards.
    :type _card_limits: list[object_.CardLimit]
    :param _daily_limit_without_confirmation_login: The amount the company can
    pay in the session without asking for credentials.
    :type _daily_limit_without_confirmation_login: object_.Amount
    :param _notification_filters: The types of notifications that will result in
    a push notification or URL callback for this UserCompany.
    :type _notification_filters: list[object_.NotificationFilter]
    :param _customer: The customer profile of the company.
    :type _customer: Customer
    :param _customer_limit: The customer limits of the company.
    :type _customer_limit: CustomerLimit
    :param _billing_contract: The subscription of the company.
    :type _billing_contract: list[BillingContractSubscription]
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user-company/{}"
    _ENDPOINT_URL_UPDATE = "user-company/{}"

    # Field constants.
    FIELD_NAME = "name"
    FIELD_PUBLIC_NICK_NAME = "public_nick_name"
    FIELD_AVATAR_UUID = "avatar_uuid"
    FIELD_ADDRESS_MAIN = "address_main"
    FIELD_ADDRESS_POSTAL = "address_postal"
    FIELD_LANGUAGE = "language"
    FIELD_REGION = "region"
    FIELD_COUNTRY = "country"
    FIELD_UBO = "ubo"
    FIELD_CHAMBER_OF_COMMERCE_NUMBER = "chamber_of_commerce_number"
    FIELD_STATUS = "status"
    FIELD_SUB_STATUS = "sub_status"
    FIELD_SESSION_TIMEOUT = "session_timeout"
    FIELD_DAILY_LIMIT_WITHOUT_CONFIRMATION_LOGIN = "daily_limit_without_confirmation_login"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"

    # Object type.
    _OBJECT_TYPE_GET = "UserCompany"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._public_uuid = None
        self._name = None
        self._display_name = None
        self._public_nick_name = None
        self._alias = None
        self._chamber_of_commerce_number = None
        self._type_of_business_entity = None
        self._sector_of_industry = None
        self._counter_bank_iban = None
        self._avatar = None
        self._address_main = None
        self._address_postal = None
        self._version_terms_of_service = None
        self._director_alias = None
        self._language = None
        self._country = None
        self._region = None
        self._ubo = None
        self._status = None
        self._sub_status = None
        self._session_timeout = None
        self._card_ids = None
        self._card_limits = None
        self._daily_limit_without_confirmation_login = None
        self._notification_filters = None
        self._customer = None
        self._customer_limit = None
        self._billing_contract = None

    @classmethod
    def get(cls, custom_headers=None):
        """
        Get a specific company.
        
        :type api_context: context.ApiContext
        :type user_company_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserCompany
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseUserCompany.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, name=None, public_nick_name=None, avatar_uuid=None,
               address_main=None, address_postal=None, language=None,
               region=None, country=None, ubo=None,
               chamber_of_commerce_number=None, status=None, sub_status=None,
               session_timeout=None,
               daily_limit_without_confirmation_login=None,
               notification_filters=None, custom_headers=None):
        """
        Modify a specific company's data.
        
        :type user_company_id: int
        :param name: The company name.
        :type name: str
        :param public_nick_name: The company's nick name.
        :type public_nick_name: str
        :param avatar_uuid: The public UUID of the company's avatar.
        :type avatar_uuid: str
        :param address_main: The user's main address.
        :type address_main: object_.Address
        :param address_postal: The company's postal address.
        :type address_postal: object_.Address
        :param language: The person's preferred language. Formatted as a ISO
        639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by
        an underscore.
        :type language: str
        :param region: The person's preferred region. Formatted as a ISO 639-1
        language code plus a ISO 3166-1 alpha-2 country code, seperated by an
        underscore.
        :type region: str
        :param country: The country where the company is registered.
        :type country: str
        :param ubo: The names and birth dates of the company's ultimate
        beneficiary owners. Minimum zero, maximum four.
        :type ubo: list[object_.Ubo]
        :param chamber_of_commerce_number: The company's chamber of commerce
        number.
        :type chamber_of_commerce_number: str
        :param status: The user status. Can be: ACTIVE, SIGNUP, RECOVERY.
        :type status: str
        :param sub_status: The user sub-status. Can be: NONE, FACE_RESET,
        APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT,
        COUNTER_IBAN, IDEAL or SUBMIT.
        :type sub_status: str
        :param session_timeout: The setting for the session timeout of the
        company in seconds.
        :type session_timeout: int
        :param daily_limit_without_confirmation_login: The amount the company
        can pay in the session without asking for credentials.
        :type daily_limit_without_confirmation_login: object_.Amount
        :param notification_filters: The types of notifications that will result
        in a push notification or URL callback for this UserCompany.
        :type notification_filters: list[object_.NotificationFilter]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_NAME: name,
            cls.FIELD_PUBLIC_NICK_NAME: public_nick_name,
            cls.FIELD_AVATAR_UUID: avatar_uuid,
            cls.FIELD_ADDRESS_MAIN: address_main,
            cls.FIELD_ADDRESS_POSTAL: address_postal,
            cls.FIELD_LANGUAGE: language,
            cls.FIELD_REGION: region,
            cls.FIELD_COUNTRY: country,
            cls.FIELD_UBO: ubo,
            cls.FIELD_CHAMBER_OF_COMMERCE_NUMBER: chamber_of_commerce_number,
            cls.FIELD_STATUS: status,
            cls.FIELD_SUB_STATUS: sub_status,
            cls.FIELD_SESSION_TIMEOUT: session_timeout,
            cls.FIELD_DAILY_LIMIT_WITHOUT_CONFIRMATION_LOGIN: daily_limit_without_confirmation_login,
            cls.FIELD_NOTIFICATION_FILTERS: notification_filters
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id())
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def public_uuid(self):
        """
        :rtype: str
        """

        return self._public_uuid

    @property
    def name(self):
        """
        :rtype: str
        """

        return self._name

    @property
    def display_name(self):
        """
        :rtype: str
        """

        return self._display_name

    @property
    def public_nick_name(self):
        """
        :rtype: str
        """

        return self._public_nick_name

    @property
    def alias(self):
        """
        :rtype: list[object_.Pointer]
        """

        return self._alias

    @property
    def chamber_of_commerce_number(self):
        """
        :rtype: str
        """

        return self._chamber_of_commerce_number

    @property
    def type_of_business_entity(self):
        """
        :rtype: str
        """

        return self._type_of_business_entity

    @property
    def sector_of_industry(self):
        """
        :rtype: str
        """

        return self._sector_of_industry

    @property
    def counter_bank_iban(self):
        """
        :rtype: str
        """

        return self._counter_bank_iban

    @property
    def avatar(self):
        """
        :rtype: object_.Avatar
        """

        return self._avatar

    @property
    def address_main(self):
        """
        :rtype: object_.Address
        """

        return self._address_main

    @property
    def address_postal(self):
        """
        :rtype: object_.Address
        """

        return self._address_postal

    @property
    def version_terms_of_service(self):
        """
        :rtype: str
        """

        return self._version_terms_of_service

    @property
    def director_alias(self):
        """
        :rtype: object_.LabelUser
        """

        return self._director_alias

    @property
    def language(self):
        """
        :rtype: str
        """

        return self._language

    @property
    def country(self):
        """
        :rtype: str
        """

        return self._country

    @property
    def region(self):
        """
        :rtype: str
        """

        return self._region

    @property
    def ubo(self):
        """
        :rtype: list[object_.Ubo]
        """

        return self._ubo

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def sub_status(self):
        """
        :rtype: str
        """

        return self._sub_status

    @property
    def session_timeout(self):
        """
        :rtype: int
        """

        return self._session_timeout

    @property
    def card_ids(self):
        """
        :rtype: list[object_.BunqId]
        """

        return self._card_ids

    @property
    def card_limits(self):
        """
        :rtype: list[object_.CardLimit]
        """

        return self._card_limits

    @property
    def daily_limit_without_confirmation_login(self):
        """
        :rtype: object_.Amount
        """

        return self._daily_limit_without_confirmation_login

    @property
    def notification_filters(self):
        """
        :rtype: list[object_.NotificationFilter]
        """

        return self._notification_filters

    @property
    def customer(self):
        """
        :rtype: Customer
        """

        return self._customer

    @property
    def customer_limit(self):
        """
        :rtype: CustomerLimit
        """

        return self._customer_limit

    @property
    def billing_contract(self):
        """
        :rtype: list[BillingContractSubscription]
        """

        return self._billing_contract

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._public_uuid is not None:
            return False

        if self._name is not None:
            return False

        if self._display_name is not None:
            return False

        if self._public_nick_name is not None:
            return False

        if self._alias is not None:
            return False

        if self._chamber_of_commerce_number is not None:
            return False

        if self._type_of_business_entity is not None:
            return False

        if self._sector_of_industry is not None:
            return False

        if self._counter_bank_iban is not None:
            return False

        if self._avatar is not None:
            return False

        if self._address_main is not None:
            return False

        if self._address_postal is not None:
            return False

        if self._version_terms_of_service is not None:
            return False

        if self._director_alias is not None:
            return False

        if self._language is not None:
            return False

        if self._country is not None:
            return False

        if self._region is not None:
            return False

        if self._ubo is not None:
            return False

        if self._status is not None:
            return False

        if self._sub_status is not None:
            return False

        if self._session_timeout is not None:
            return False

        if self._card_ids is not None:
            return False

        if self._card_limits is not None:
            return False

        if self._daily_limit_without_confirmation_login is not None:
            return False

        if self._notification_filters is not None:
            return False

        if self._customer is not None:
            return False

        if self._customer_limit is not None:
            return False

        if self._billing_contract is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: UserCompany
        """

        return converter.json_to_class(UserCompany, json_str)


class Customer(core.BunqModel):
    """
    Used to view a customer.
    
    :param _id_: The id of the customer.
    :type _id_: int
    :param _created: The timestamp of the customer object's creation.
    :type _created: str
    :param _updated: The timestamp of the customer object's last update.
    :type _updated: str
    :param _billing_account_id: The primary billing account account's id.
    :type _billing_account_id: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/customer"
    _ENDPOINT_URL_READ = "user/{}/customer/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/customer/{}"

    # Field constants.
    FIELD_BILLING_ACCOUNT_ID = "billing_account_id"

    # Object type.
    _OBJECT_TYPE_GET = "Customer"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._billing_account_id = None

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCustomerList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCustomerList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def get(cls, customer_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type customer_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCustomer
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     customer_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCustomer.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, customer_id, billing_account_id=None, custom_headers=None):
        """
        :type user_id: int
        :type customer_id: int
        :param billing_account_id: The primary billing account account's id.
        :type billing_account_id: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_BILLING_ACCOUNT_ID: billing_account_id
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       customer_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def billing_account_id(self):
        """
        :rtype: str
        """

        return self._billing_account_id

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._billing_account_id is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Customer
        """

        return converter.json_to_class(Customer, json_str)


class CustomerLimit(core.BunqModel):
    """
    Show the limits for the authenticated user.
    
    :param _limit_monetary_account: The limit of monetary accounts.
    :type _limit_monetary_account: int
    :param _limit_card_debit_maestro: The limit of Maestro cards.
    :type _limit_card_debit_maestro: int
    :param _limit_card_debit_mastercard: The limit of MasterCard cards.
    :type _limit_card_debit_mastercard: int
    :param _limit_card_debit_wildcard: The limit of wildcards, e.g. Maestro or
    MasterCard cards.
    :type _limit_card_debit_wildcard: int
    :param _limit_card_debit_replacement: The limit of free replacement cards.
    :type _limit_card_debit_replacement: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/limit"

    # Object type.
    _OBJECT_TYPE_GET = "CustomerLimit"

    def __init__(self):
        self._limit_monetary_account = None
        self._limit_card_debit_maestro = None
        self._limit_card_debit_mastercard = None
        self._limit_card_debit_wildcard = None
        self._limit_card_debit_replacement = None

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Get all limits for the authenticated user.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCustomerLimitList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCustomerLimitList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def limit_monetary_account(self):
        """
        :rtype: int
        """

        return self._limit_monetary_account

    @property
    def limit_card_debit_maestro(self):
        """
        :rtype: int
        """

        return self._limit_card_debit_maestro

    @property
    def limit_card_debit_mastercard(self):
        """
        :rtype: int
        """

        return self._limit_card_debit_mastercard

    @property
    def limit_card_debit_wildcard(self):
        """
        :rtype: int
        """

        return self._limit_card_debit_wildcard

    @property
    def limit_card_debit_replacement(self):
        """
        :rtype: int
        """

        return self._limit_card_debit_replacement

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._limit_monetary_account is not None:
            return False

        if self._limit_card_debit_maestro is not None:
            return False

        if self._limit_card_debit_mastercard is not None:
            return False

        if self._limit_card_debit_wildcard is not None:
            return False

        if self._limit_card_debit_replacement is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CustomerLimit
        """

        return converter.json_to_class(CustomerLimit, json_str)


class BillingContractSubscription(core.BunqModel):
    """
    Show the subscription billing contract for the authenticated user.
    
    :param _id_: The id of the billing contract.
    :type _id_: int
    :param _created: The timestamp when the billing contract was made.
    :type _created: str
    :param _updated: The timestamp when the billing contract was last updated.
    :type _updated: str
    :param _contract_date_start: The date from when the billing contract is
    valid.
    :type _contract_date_start: str
    :param _contract_date_end: The date until when the billing contract is
    valid.
    :type _contract_date_end: str
    :param _contract_version: The version of the billing contract.
    :type _contract_version: int
    :param _subscription_type: The subscription type of the user. Can be one of
    PERSON_SUPER_LIGHT_V1, PERSON_LIGHT_V1, PERSON_MORE_V1, PERSON_FREE_V1,
    PERSON_PREMIUM_V1, COMPANY_V1, or COMPANY_V2.
    :type _subscription_type: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/billing-contract-subscription"
    _ENDPOINT_URL_LISTING = "user/{}/billing-contract-subscription"

    # Field constants.
    FIELD_SUBSCRIPTION_TYPE = "subscription_type"

    # Object type.
    _OBJECT_TYPE_GET = "BillingContractSubscription"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._contract_date_start = None
        self._contract_date_end = None
        self._contract_version = None
        self._subscription_type = None

    @classmethod
    def create(cls, subscription_type, custom_headers=None):
        """
        :type user_id: int
        :param subscription_type: The subscription type of the user. Can be one
        of PERSON_LIGHT_V1, PERSON_MORE_V1, PERSON_FREE_V1, PERSON_PREMIUM_V1,
        COMPANY_V1, or COMPANY_V2.
        :type subscription_type: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_SUBSCRIPTION_TYPE: subscription_type
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Get all subscription billing contract for the authenticated user.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBillingContractSubscriptionList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseBillingContractSubscriptionList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def contract_date_start(self):
        """
        :rtype: str
        """

        return self._contract_date_start

    @property
    def contract_date_end(self):
        """
        :rtype: str
        """

        return self._contract_date_end

    @property
    def contract_version(self):
        """
        :rtype: int
        """

        return self._contract_version

    @property
    def subscription_type(self):
        """
        :rtype: str
        """

        return self._subscription_type

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._contract_date_start is not None:
            return False

        if self._contract_date_end is not None:
            return False

        if self._contract_version is not None:
            return False

        if self._subscription_type is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BillingContractSubscription
        """

        return converter.json_to_class(BillingContractSubscription, json_str)


class PaymentChat(core.BunqModel):
    """
    Manage the chat connected to a payment.
    
    :param _id_: The id of the chat conversation.
    :type _id_: int
    :param _created: The timestamp when the chat was created.
    :type _created: str
    :param _updated: The timestamp when the chat was last updated.
    :type _updated: str
    :param _unread_message_count: The total number of unread messages in this
    conversation.
    :type _unread_message_count: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/payment/{}/chat"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/payment/{}/chat/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/payment/{}/chat"

    # Field constants.
    FIELD_LAST_READ_MESSAGE_ID = "last_read_message_id"

    # Object type.
    _OBJECT_TYPE_GET = "ChatConversationPayment"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._unread_message_count = None

    @classmethod
    def create(cls, payment_id, monetary_account_id=None,
               last_read_message_id=None, custom_headers=None):
        """
        Create a chat for a specific payment.
        
        :type user_id: int
        :type monetary_account_id: int
        :type payment_id: int
        :param last_read_message_id: The id of the last read message.
        :type last_read_message_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_LAST_READ_MESSAGE_ID: last_read_message_id
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       payment_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, payment_id, payment_chat_id, monetary_account_id=None,
               last_read_message_id=None, custom_headers=None):
        """
        Update the last read message in the chat of a specific payment.
        
        :type user_id: int
        :type monetary_account_id: int
        :type payment_id: int
        :type payment_chat_id: int
        :param last_read_message_id: The id of the last read message.
        :type last_read_message_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_LAST_READ_MESSAGE_ID: last_read_message_id
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       payment_id,
                                                       payment_chat_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, payment_id, monetary_account_id=None, params=None,
             custom_headers=None):
        """
        Get the chat for a specific payment.
        
        :type user_id: int
        :type monetary_account_id: int
        :type payment_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponsePaymentChatList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id), payment_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponsePaymentChatList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def unread_message_count(self):
        """
        :rtype: int
        """

        return self._unread_message_count

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._unread_message_count is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: PaymentChat
        """

        return converter.json_to_class(PaymentChat, json_str)


class PermittedIp(core.BunqModel):
    """
    Manage the IPs which may be used for a credential of a user for server
    authentication.
    
    :param _ip: The IP address.
    :type _ip: str
    :param _status: The status of the IP. May be "ACTIVE" or "INACTIVE". It is
    only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs
    will be billed.
    :type _status: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/credential-password-ip/{}/ip/{}"
    _ENDPOINT_URL_CREATE = "user/{}/credential-password-ip/{}/ip"
    _ENDPOINT_URL_LISTING = "user/{}/credential-password-ip/{}/ip"
    _ENDPOINT_URL_UPDATE = "user/{}/credential-password-ip/{}/ip/{}"

    # Field constants.
    FIELD_IP = "ip"
    FIELD_STATUS = "status"

    # Object type.
    _OBJECT_TYPE_GET = "PermittedIp"

    def __init__(self):
        self._ip = None
        self._status = None

    @classmethod
    def get(cls, credential_password_ip_id, permitted_ip_id,
            custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type credential_password_ip_id: int
        :type permitted_ip_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponsePermittedIp
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     credential_password_ip_id,
                                                     permitted_ip_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponsePermittedIp.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def create(cls, credential_password_ip_id, ip, status=None,
               custom_headers=None):
        """
        :type user_id: int
        :type credential_password_ip_id: int
        :param ip: The IP address.
        :type ip: str
        :param status: The status of the IP. May be "ACTIVE" or "INACTIVE". It
        is only possible to make requests from "ACTIVE" IP addresses. Only
        "ACTIVE" IPs will be billed.
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_IP: ip,
            cls.FIELD_STATUS: status
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       credential_password_ip_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, credential_password_ip_id, params=None, custom_headers=None):
        """
        :type user_id: int
        :type credential_password_ip_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponsePermittedIpList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(), credential_password_ip_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponsePermittedIpList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def update(cls, credential_password_ip_id, permitted_ip_id, status=None,
               custom_headers=None):
        """
        :type user_id: int
        :type credential_password_ip_id: int
        :type permitted_ip_id: int
        :param status: The status of the IP. May be "ACTIVE" or "INACTIVE". It
        is only possible to make requests from "ACTIVE" IP addresses. Only
        "ACTIVE" IPs will be billed.
        :type status: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       credential_password_ip_id,
                                                       permitted_ip_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def ip(self):
        """
        :rtype: str
        """

        return self._ip

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._ip is not None:
            return False

        if self._status is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: PermittedIp
        """

        return converter.json_to_class(PermittedIp, json_str)


class RequestInquiryChat(core.BunqModel):
    """
    Manage the chat connected to a request inquiry. In the same way a request
    inquiry and a request response are created together, so that each side of
    the interaction can work on a different object, also a request inquiry chat
    and a request response chat are created at the same time. See
    'request-response-chat' for the chat endpoint for the responding user.
    
    :param _id_: The id of the newly created chat conversation.
    :type _id_: int
    :param _created: The timestamp when the chat was created.
    :type _created: str
    :param _updated: The timestamp when the chat was last updated.
    :type _updated: str
    :param _unread_message_count: The total number of messages in this
    conversation.
    :type _unread_message_count: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/request-inquiry/{}/chat"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/request-inquiry/{}/chat/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/request-inquiry/{}/chat"

    # Field constants.
    FIELD_LAST_READ_MESSAGE_ID = "last_read_message_id"

    # Object type.
    _OBJECT_TYPE_GET = "RequestInquiryChat"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._unread_message_count = None

    @classmethod
    def create(cls, request_inquiry_id, monetary_account_id=None,
               last_read_message_id=None, custom_headers=None):
        """
        Create a chat for a specific request inquiry.
        
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_id: int
        :param last_read_message_id: The id of the last read message.
        :type last_read_message_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_LAST_READ_MESSAGE_ID: last_read_message_id
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       request_inquiry_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, request_inquiry_id, request_inquiry_chat_id,
               monetary_account_id=None, last_read_message_id=None,
               custom_headers=None):
        """
        Update the last read message in the chat of a specific request inquiry.
        
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_id: int
        :type request_inquiry_chat_id: int
        :param last_read_message_id: The id of the last read message.
        :type last_read_message_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_LAST_READ_MESSAGE_ID: last_read_message_id
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       request_inquiry_id,
                                                       request_inquiry_chat_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, request_inquiry_id, monetary_account_id=None, params=None,
             custom_headers=None):
        """
        Get the chat for a specific request inquiry.
        
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestInquiryChatList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            request_inquiry_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseRequestInquiryChatList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def unread_message_count(self):
        """
        :rtype: int
        """

        return self._unread_message_count

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._unread_message_count is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RequestInquiryChat
        """

        return converter.json_to_class(RequestInquiryChat, json_str)


class RequestResponseChat(core.BunqModel):
    """
    Manage the chat connected to a request response. In the same way a request
    inquiry and a request response are created together, so that each side of
    the interaction can work on a different object, also a request inquiry chat
    and a request response chat are created at the same time. See
    'request-inquiry-chat' for the chat endpoint for the inquiring user.
    
    :param _id_: The id of the newly created chat conversation.
    :type _id_: int
    :param _created: The timestamp when the chat was created.
    :type _created: str
    :param _updated: The timestamp when the chat was last updated.
    :type _updated: str
    :param _unread_message_count: The total number of messages in this
    conversation.
    :type _unread_message_count: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/request-response/{}/chat"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/request-response/{}/chat/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/request-response/{}/chat"

    # Field constants.
    FIELD_LAST_READ_MESSAGE_ID = "last_read_message_id"

    # Object type.
    _OBJECT_TYPE_GET = "RequestResponseChat"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._unread_message_count = None

    @classmethod
    def create(cls, request_response_id, monetary_account_id=None,
               last_read_message_id=None, custom_headers=None):
        """
        Create a chat for a specific request response.
        
        :type user_id: int
        :type monetary_account_id: int
        :type request_response_id: int
        :param last_read_message_id: The id of the last read message.
        :type last_read_message_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_LAST_READ_MESSAGE_ID: last_read_message_id
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       request_response_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, request_response_id, request_response_chat_id,
               monetary_account_id=None, last_read_message_id=None,
               custom_headers=None):
        """
        Update the last read message in the chat of a specific request response.
        
        :type user_id: int
        :type monetary_account_id: int
        :type request_response_id: int
        :type request_response_chat_id: int
        :param last_read_message_id: The id of the last read message.
        :type last_read_message_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_LAST_READ_MESSAGE_ID: last_read_message_id
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       request_response_id,
                                                       request_response_chat_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, request_response_id, monetary_account_id=None, params=None,
             custom_headers=None):
        """
        Get the chat for a specific request response.
        
        :type user_id: int
        :type monetary_account_id: int
        :type request_response_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestResponseChatList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            request_response_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseRequestResponseChatList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def unread_message_count(self):
        """
        :rtype: int
        """

        return self._unread_message_count

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._unread_message_count is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RequestResponseChat
        """

        return converter.json_to_class(RequestResponseChat, json_str)


class SandboxUser(core.BunqModel):
    """
    Used to create a sandbox user.
    
    :param _api_key: The API key of the newly created sandbox user.
    :type _api_key: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "sandbox-user"

    # Object type.
    _OBJECT_TYPE_POST = "ApiKey"

    def __init__(self):
        self._api_key = None

    @classmethod
    def create(cls, custom_headers=None):
        """
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseSandboxUser
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {

        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseSandboxUser.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_POST)
        )

    @property
    def api_key(self):
        """
        :rtype: str
        """

        return self._api_key

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._api_key is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: SandboxUser
        """

        return converter.json_to_class(SandboxUser, json_str)


class ScheduleUser(core.BunqModel):
    """
    view for reading the scheduled definitions.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/schedule"

    # Object type.
    _OBJECT_TYPE_GET = "ScheduleUser"

    @classmethod
    def list(cls, params=None, custom_headers=None):
        """
        Get a collection of scheduled definition for all accessible monetary
        accounts of the user. You can add the parameter type to filter the
        response. When
        type={SCHEDULE_DEFINITION_PAYMENT,SCHEDULE_DEFINITION_PAYMENT_BATCH} is
        provided only schedule definition object that relate to these
        definitions are returned.
        
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseScheduleUserList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id())
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseScheduleUserList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ScheduleUser
        """

        return converter.json_to_class(ScheduleUser, json_str)


class Session(core.BunqModel):
    """
    Endpoint for operations over the current session.
    """

    # Endpoint constants.
    _ENDPOINT_URL_DELETE = "session/{}"

    @classmethod
    def delete(cls, session_id, custom_headers=None):
        """
        Deletes the current session.
        
        :type session_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(session_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Session
        """

        return converter.json_to_class(Session, json_str)


class TabItemShopBatch(core.BunqModel):
    """
    Create a batch of tab items.
    
    :param _tab_items: The list of tab items in the batch.
    :type _tab_items: list[TabItemShop]
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item-batch"

    # Field constants.
    FIELD_TAB_ITEMS = "tab_items"

    def __init__(self):
        self._tab_items = None

    @classmethod
    def create(cls, cash_register_id, tab_uuid, tab_items,
               monetary_account_id=None, custom_headers=None):
        """
        Create tab items as a batch.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :param tab_items: The list of tab items we want to create in a single
        batch. Limited to 50 items per batch.
        :type tab_items: list[TabItemShop]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_TAB_ITEMS: tab_items
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id,
                                                       tab_uuid)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def tab_items(self):
        """
        :rtype: list[TabItemShop]
        """

        return self._tab_items

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._tab_items is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabItemShopBatch
        """

        return converter.json_to_class(TabItemShopBatch, json_str)


class TabItemShop(core.BunqModel):
    """
    After you’ve created a Tab using /tab-usage-single or /tab-usage-multiple
    you can add items and attachments using tab-item. You can only add or modify
    TabItems of a Tab which status is OPEN. The amount of the TabItems will not
    influence the total_amount of the corresponding Tab. However, if you've
    created any TabItems for a Tab the sum of the amounts of these items must be
    equal to the total_amount of the Tab when you change its status to
    PAYABLE/WAITING_FOR_PAYMENT.
    
    :param _id_: The id of the created TabItem.
    :type _id_: int
    :param _description: The TabItem's brief description.
    :type _description: str
    :param _ean_code: The TabItem's EAN code.
    :type _ean_code: str
    :param _avatar_attachment: A struct with an AttachmentPublic UUID that used
    as an avatar for the TabItem.
    :type _avatar_attachment: object_.AttachmentPublic
    :param _tab_attachment: A list of AttachmentTab attached to the TabItem.
    :type _tab_attachment: list[object_.AttachmentTab]
    :param _quantity: The quantity of the TabItem.
    :type _quantity: float
    :param _amount: The money amount of the TabItem.
    :type _amount: object_.Amount
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item/{}"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item/{}"

    # Field constants.
    FIELD_DESCRIPTION = "description"
    FIELD_EAN_CODE = "ean_code"
    FIELD_AVATAR_ATTACHMENT_UUID = "avatar_attachment_uuid"
    FIELD_TAB_ATTACHMENT = "tab_attachment"
    FIELD_QUANTITY = "quantity"
    FIELD_AMOUNT = "amount"

    # Object type.
    _OBJECT_TYPE_GET = "TabItem"

    def __init__(self):
        self._id_ = None
        self._description = None
        self._ean_code = None
        self._avatar_attachment = None
        self._tab_attachment = None
        self._quantity = None
        self._amount = None

    @classmethod
    def create(cls, cash_register_id, tab_uuid, description,
               monetary_account_id=None, ean_code=None,
               avatar_attachment_uuid=None, tab_attachment=None, quantity=None,
               amount=None, custom_headers=None):
        """
        Create a new TabItem for a given Tab.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :param description: The TabItem's brief description. Can't be empty and
        must be no longer than 100 characters
        :type description: str
        :param ean_code: The TabItem's EAN code.
        :type ean_code: str
        :param avatar_attachment_uuid: An AttachmentPublic UUID that used as an
        avatar for the TabItem.
        :type avatar_attachment_uuid: str
        :param tab_attachment: A list of AttachmentTab attached to the TabItem.
        :type tab_attachment: list[int]
        :param quantity: The quantity of the TabItem. Formatted as a number
        containing up to 15 digits, up to 15 decimals and using a dot.
        :type quantity: str
        :param amount: The money amount of the TabItem. Will not change the
        value of the corresponding Tab.
        :type amount: object_.Amount
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_EAN_CODE: ean_code,
            cls.FIELD_AVATAR_ATTACHMENT_UUID: avatar_attachment_uuid,
            cls.FIELD_TAB_ATTACHMENT: tab_attachment,
            cls.FIELD_QUANTITY: quantity,
            cls.FIELD_AMOUNT: amount
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id,
                                                       tab_uuid)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, cash_register_id, tab_uuid, tab_item_shop_id,
               monetary_account_id=None, description=None, ean_code=None,
               avatar_attachment_uuid=None, tab_attachment=None, quantity=None,
               amount=None, custom_headers=None):
        """
        Modify a TabItem from a given Tab.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type tab_item_shop_id: int
        :param description: The TabItem's brief description. Can't be empty and
        must be no longer than 100 characters
        :type description: str
        :param ean_code: The TabItem's EAN code.
        :type ean_code: str
        :param avatar_attachment_uuid: An AttachmentPublic UUID that used as an
        avatar for the TabItem.
        :type avatar_attachment_uuid: str
        :param tab_attachment: A list of AttachmentTab attached to the TabItem.
        :type tab_attachment: list[int]
        :param quantity: The quantity of the TabItem. Formatted as a number
        containing up to 15 digits, up to 15 decimals and using a dot.
        :type quantity: str
        :param amount: The money amount of the TabItem. Will not change the
        value of the corresponding Tab.
        :type amount: object_.Amount
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_EAN_CODE: ean_code,
            cls.FIELD_AVATAR_ATTACHMENT_UUID: avatar_attachment_uuid,
            cls.FIELD_TAB_ATTACHMENT: tab_attachment,
            cls.FIELD_QUANTITY: quantity,
            cls.FIELD_AMOUNT: amount
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id,
                                                       tab_uuid,
                                                       tab_item_shop_id)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def delete(cls, cash_register_id, tab_uuid, tab_item_shop_id,
               monetary_account_id=None, custom_headers=None):
        """
        Delete a specific TabItem from a Tab.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type tab_item_shop_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id,
                                                       tab_uuid,
                                                       tab_item_shop_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @classmethod
    def list(cls, cash_register_id, tab_uuid, monetary_account_id=None,
             params=None, custom_headers=None):
        """
        Get a collection of TabItems from a given Tab.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabItemShopList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            cash_register_id, tab_uuid)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabItemShopList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def get(cls, cash_register_id, tab_uuid, tab_item_shop_id,
            monetary_account_id=None, custom_headers=None):
        """
        Get a specific TabItem from a given Tab.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type tab_item_shop_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabItemShop
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     cash_register_id, tab_uuid,
                                                     tab_item_shop_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabItemShop.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def ean_code(self):
        """
        :rtype: str
        """

        return self._ean_code

    @property
    def avatar_attachment(self):
        """
        :rtype: object_.AttachmentPublic
        """

        return self._avatar_attachment

    @property
    def tab_attachment(self):
        """
        :rtype: list[object_.AttachmentTab]
        """

        return self._tab_attachment

    @property
    def quantity(self):
        """
        :rtype: float
        """

        return self._quantity

    @property
    def amount(self):
        """
        :rtype: object_.Amount
        """

        return self._amount

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._description is not None:
            return False

        if self._ean_code is not None:
            return False

        if self._avatar_attachment is not None:
            return False

        if self._tab_attachment is not None:
            return False

        if self._quantity is not None:
            return False

        if self._amount is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabItemShop
        """

        return converter.json_to_class(TabItemShop, json_str)


class TabQrCodeContent(core.BunqModel):
    """
    This call returns the raw content of the QR code that links to this Tab.
    When a bunq user scans this QR code with the bunq app the Tab will be shown
    on his/her device.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/qr-code-content"

    # Object type.
    _OBJECT_TYPE_GET = "TabQrCodeContent"

    @classmethod
    def list(cls, cash_register_id, tab_uuid, monetary_account_id=None,
             custom_headers=None):
        """
        Returns the raw content of the QR code that links to this Tab. The raw
        content is the binary representation of a file, without any JSON
        wrapping.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            cash_register_id, tab_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabQrCodeContent
        """

        return converter.json_to_class(TabQrCodeContent, json_str)


class TabUsageMultiple(core.BunqModel):
    """
    TabUsageMultiple is a Tab that can be paid by multiple users. Just like the
    TabUsageSingle it is created with the status OPEN, the visibility can be
    defined in the visibility object and TabItems can be added as long as the
    status is OPEN. When you change the status to PAYABLE any bunq user can use
    the tab to make a payment to your account. After an user has paid your
    TabUsageMultiple the status will not change, it will stay PAYABLE. For
    example: you can create a TabUsageMultiple with require_address set to true.
    Now show the QR code of this Tab on your webshop, and any bunq user can
    instantly pay and order something from your webshop.
    
    :param _uuid: The uuid of the created TabUsageMultiple.
    :type _uuid: str
    :param _created: The timestamp of the Tab's creation.
    :type _created: str
    :param _updated: The timestamp of the Tab's last update.
    :type _updated: str
    :param _description: The description of the TabUsageMultiple. Maximum 9000
    characters.
    :type _description: str
    :param _status: The status of the Tab. Can be OPEN, PAYABLE or CLOSED.
    :type _status: str
    :param _amount_total: The total amount of the Tab.
    :type _amount_total: object_.Amount
    :param _qr_code_token: The token used to redirect mobile devices directly to
    the bunq app. Because they can't scan a QR code.
    :type _qr_code_token: str
    :param _tab_url: The URL redirecting user to the tab payment in the bunq
    app. Only works on mobile devices.
    :type _tab_url: str
    :param _visibility: The visibility of a Tab. A Tab can be visible trough
    NearPay, the QR code of the CashRegister and its own QR code.
    :type _visibility: object_.TabVisibility
    :param _minimum_age: The minimum age of the user paying the Tab.
    :type _minimum_age: bool
    :param _require_address: Whether or not an billing and shipping address must
    be provided when paying the Tab.
    :type _require_address: str
    :param _redirect_url: The URL which the user is sent to after paying the
    Tab.
    :type _redirect_url: str
    :param _expiration: The moment when this Tab expires.
    :type _expiration: str
    :param _alias: The alias of the party that owns this tab.
    :type _alias: object_.MonetaryAccountReference
    :param _cash_register_location: The location of the cash register that
    created this tab.
    :type _cash_register_location: object_.Geolocation
    :param _tab_item: The tab items of this tab.
    :type _tab_item: list[TabItem]
    :param _tab_attachment: An array of attachments that describe the tab.
    Viewable through the GET /tab/{tabid}/attachment/{attachmentid}/content
    endpoint.
    :type _tab_attachment: list[object_.BunqId]
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-multiple"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-multiple/{}"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-multiple/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-multiple/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-multiple"

    # Field constants.
    FIELD_DESCRIPTION = "description"
    FIELD_STATUS = "status"
    FIELD_AMOUNT_TOTAL = "amount_total"
    FIELD_ALLOW_AMOUNT_HIGHER = "allow_amount_higher"
    FIELD_ALLOW_AMOUNT_LOWER = "allow_amount_lower"
    FIELD_WANT_TIP = "want_tip"
    FIELD_MINIMUM_AGE = "minimum_age"
    FIELD_REQUIRE_ADDRESS = "require_address"
    FIELD_REDIRECT_URL = "redirect_url"
    FIELD_VISIBILITY = "visibility"
    FIELD_EXPIRATION = "expiration"
    FIELD_TAB_ATTACHMENT = "tab_attachment"

    # Object type.
    _OBJECT_TYPE_POST = "Uuid"
    _OBJECT_TYPE_PUT = "Uuid"
    _OBJECT_TYPE_GET = "TabUsageMultiple"

    def __init__(self):
        self._uuid = None
        self._created = None
        self._updated = None
        self._description = None
        self._status = None
        self._amount_total = None
        self._qr_code_token = None
        self._tab_url = None
        self._visibility = None
        self._minimum_age = None
        self._require_address = None
        self._redirect_url = None
        self._expiration = None
        self._alias = None
        self._cash_register_location = None
        self._tab_item = None
        self._tab_attachment = None

    @classmethod
    def create(cls, cash_register_id, description, status, amount_total,
               monetary_account_id=None, allow_amount_higher=None,
               allow_amount_lower=None, want_tip=None, minimum_age=None,
               require_address=None, redirect_url=None, visibility=None,
               expiration=None, tab_attachment=None, custom_headers=None):
        """
        Create a TabUsageMultiple. On creation the status must be set to OPEN
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :param description: The description of the TabUsageMultiple. Maximum
        9000 characters. Field is required but can be an empty string.
        :type description: str
        :param status: The status of the TabUsageMultiple. On creation the
        status must be set to OPEN. You can change the status from OPEN to
        PAYABLE. If the TabUsageMultiple gets paid the status will remain
        PAYABLE.
        :type status: str
        :param amount_total: The total amount of the Tab. Must be a positive
        amount. As long as the tab has the status OPEN you can change the total
        amount. This amount is not affected by the amounts of the TabItems.
        However, if you've created any TabItems for a Tab the sum of the amounts
        of these items must be equal to the total_amount of the Tab when you
        change its status to PAYABLE
        :type amount_total: object_.Amount
        :param allow_amount_higher: [DEPRECATED] Whether or not a higher amount
        can be paid.
        :type allow_amount_higher: bool
        :param allow_amount_lower: [DEPRECATED] Whether or not a lower amount
        can be paid.
        :type allow_amount_lower: bool
        :param want_tip: [DEPRECATED] Whether or not the user paying the Tab
        should be asked if he wants to give a tip. When want_tip is set to true,
        allow_amount_higher must also be set to true and allow_amount_lower must
        be false.
        :type want_tip: bool
        :param minimum_age: The minimum age of the user paying the Tab.
        :type minimum_age: int
        :param require_address: Whether a billing and shipping address must be
        provided when paying the Tab. Possible values are: BILLING, SHIPPING,
        BILLING_SHIPPING, NONE, OPTIONAL. Default is NONE.
        :type require_address: str
        :param redirect_url: The URL which the user is sent to after paying the
        Tab.
        :type redirect_url: str
        :param visibility: The visibility of a Tab. A Tab can be visible trough
        NearPay, the QR code of the CashRegister and its own QR code.
        :type visibility: object_.TabVisibility
        :param expiration: The moment when this Tab expires. Can be at most 365
        days into the future.
        :type expiration: str
        :param tab_attachment: An array of attachments that describe the tab.
        Uploaded through the POST /user/{userid}/attachment-tab endpoint.
        :type tab_attachment: list[object_.BunqId]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_STATUS: status,
            cls.FIELD_AMOUNT_TOTAL: amount_total,
            cls.FIELD_ALLOW_AMOUNT_HIGHER: allow_amount_higher,
            cls.FIELD_ALLOW_AMOUNT_LOWER: allow_amount_lower,
            cls.FIELD_WANT_TIP: want_tip,
            cls.FIELD_MINIMUM_AGE: minimum_age,
            cls.FIELD_REQUIRE_ADDRESS: require_address,
            cls.FIELD_REDIRECT_URL: redirect_url,
            cls.FIELD_VISIBILITY: visibility,
            cls.FIELD_EXPIRATION: expiration,
            cls.FIELD_TAB_ATTACHMENT: tab_attachment
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def update(cls, cash_register_id, tab_usage_multiple_uuid,
               monetary_account_id=None, status=None, amount_total=None,
               visibility=None, expiration=None, tab_attachment=None,
               custom_headers=None):
        """
        Modify a specific TabUsageMultiple. You can change the amount_total,
        status and visibility. Once you change the status to PAYABLE the
        TabUsageMultiple will expire after a year (default). If you've created
        any TabItems for a Tab the sum of the amounts of these items must be
        equal to the total_amount of the Tab when you change its status to
        PAYABLE.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_usage_multiple_uuid: str
        :param status: The status of the TabUsageMultiple. On creation the
        status must be set to OPEN. You can change the status from OPEN to
        PAYABLE. If the TabUsageMultiple gets paid the status will remain
        PAYABLE.
        :type status: str
        :param amount_total: The total amount of the Tab. Must be a positive
        amount. As long as the tab has the status OPEN you can change the total
        amount. This amount is not affected by the amounts of the TabItems.
        However, if you've created any TabItems for a Tab the sum of the amounts
        of these items must be equal to the total_amount of the Tab when you
        change its status to PAYABLE
        :type amount_total: object_.Amount
        :param visibility: The visibility of a Tab. A Tab can be visible trough
        NearPay, the QR code of the CashRegister and its own QR code.
        :type visibility: object_.TabVisibility
        :param expiration: The moment when this Tab expires. Can be at most 365
        days into the future.
        :type expiration: str
        :param tab_attachment: An array of attachments that describe the tab.
        Uploaded through the POST /user/{userid}/attachment-tab endpoint.
        :type tab_attachment: list[object_.BunqId]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status,
            cls.FIELD_AMOUNT_TOTAL: amount_total,
            cls.FIELD_VISIBILITY: visibility,
            cls.FIELD_EXPIRATION: expiration,
            cls.FIELD_TAB_ATTACHMENT: tab_attachment
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id,
                                                       tab_usage_multiple_uuid)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def delete(cls, cash_register_id, tab_usage_multiple_uuid,
               monetary_account_id=None, custom_headers=None):
        """
        Close a specific TabUsageMultiple.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_usage_multiple_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id,
                                                       tab_usage_multiple_uuid)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @classmethod
    def get(cls, cash_register_id, tab_usage_multiple_uuid,
            monetary_account_id=None, custom_headers=None):
        """
        Get a specific TabUsageMultiple.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_usage_multiple_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabUsageMultiple
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     cash_register_id,
                                                     tab_usage_multiple_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabUsageMultiple.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, cash_register_id, monetary_account_id=None, params=None,
             custom_headers=None):
        """
        Get a collection of TabUsageMultiple.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabUsageMultipleList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            cash_register_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabUsageMultipleList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def amount_total(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_total

    @property
    def qr_code_token(self):
        """
        :rtype: str
        """

        return self._qr_code_token

    @property
    def tab_url(self):
        """
        :rtype: str
        """

        return self._tab_url

    @property
    def visibility(self):
        """
        :rtype: object_.TabVisibility
        """

        return self._visibility

    @property
    def minimum_age(self):
        """
        :rtype: bool
        """

        return self._minimum_age

    @property
    def require_address(self):
        """
        :rtype: str
        """

        return self._require_address

    @property
    def redirect_url(self):
        """
        :rtype: str
        """

        return self._redirect_url

    @property
    def expiration(self):
        """
        :rtype: str
        """

        return self._expiration

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def cash_register_location(self):
        """
        :rtype: object_.Geolocation
        """

        return self._cash_register_location

    @property
    def tab_item(self):
        """
        :rtype: list[TabItem]
        """

        return self._tab_item

    @property
    def tab_attachment(self):
        """
        :rtype: list[object_.BunqId]
        """

        return self._tab_attachment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._uuid is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._description is not None:
            return False

        if self._status is not None:
            return False

        if self._amount_total is not None:
            return False

        if self._qr_code_token is not None:
            return False

        if self._tab_url is not None:
            return False

        if self._visibility is not None:
            return False

        if self._minimum_age is not None:
            return False

        if self._require_address is not None:
            return False

        if self._redirect_url is not None:
            return False

        if self._expiration is not None:
            return False

        if self._alias is not None:
            return False

        if self._cash_register_location is not None:
            return False

        if self._tab_item is not None:
            return False

        if self._tab_attachment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabUsageMultiple
        """

        return converter.json_to_class(TabUsageMultiple, json_str)


class TabItem(core.BunqModel):
    """
    Used to get items on a tab.
    
    :param _id_: The id of the tab item.
    :type _id_: int
    :param _description: The item's brief description.
    :type _description: str
    :param _ean_code: The item's EAN code.
    :type _ean_code: str
    :param _avatar_attachment: A struct with an AttachmentPublic UUID that used
    as an avatar for the TabItem.
    :type _avatar_attachment: object_.AttachmentPublic
    :param _tab_attachment: A list of AttachmentTab attached to the TabItem.
    :type _tab_attachment: list[object_.AttachmentTab]
    :param _quantity: The quantity of the item. Formatted as a number containing
    up to 15 digits, up to 15 decimals and using a dot.
    :type _quantity: str
    :param _amount: The money amount of the item.
    :type _amount: object_.Amount
    """

    def __init__(self):
        self._id_ = None
        self._description = None
        self._ean_code = None
        self._avatar_attachment = None
        self._tab_attachment = None
        self._quantity = None
        self._amount = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def ean_code(self):
        """
        :rtype: str
        """

        return self._ean_code

    @property
    def avatar_attachment(self):
        """
        :rtype: object_.AttachmentPublic
        """

        return self._avatar_attachment

    @property
    def tab_attachment(self):
        """
        :rtype: list[object_.AttachmentTab]
        """

        return self._tab_attachment

    @property
    def quantity(self):
        """
        :rtype: str
        """

        return self._quantity

    @property
    def amount(self):
        """
        :rtype: object_.Amount
        """

        return self._amount

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._description is not None:
            return False

        if self._ean_code is not None:
            return False

        if self._avatar_attachment is not None:
            return False

        if self._tab_attachment is not None:
            return False

        if self._quantity is not None:
            return False

        if self._amount is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabItem
        """

        return converter.json_to_class(TabItem, json_str)


class TabUsageSingle(core.BunqModel):
    """
    TabUsageSingle is a Tab that can be paid once. The TabUsageSingle is created
    with the status OPEN. Optionally you can add TabItems to the tab using
    /tab/_/tab-item, TabItems don't affect the total amount of the Tab. However,
    if you've created any TabItems for a Tab the sum of the amounts of these
    items must be equal to the total_amount of the Tab when you change its
    status to WAITING_FOR_PAYMENT. By setting the visibility object a
    TabUsageSingle with the status OPEN or WAITING_FOR_PAYMENT can be made
    visible to customers. As soon as a customer pays the TabUsageSingle its
    status changes to PAID, and it can't be paid again.
    
    :param _uuid: The uuid of the created TabUsageSingle.
    :type _uuid: str
    :param _created: The timestamp of the Tab's creation.
    :type _created: str
    :param _updated: The timestamp of the Tab's last update.
    :type _updated: str
    :param _merchant_reference: The merchant reference of the Tab, as defined by
    the owner.
    :type _merchant_reference: str
    :param _description: The description of the TabUsageMultiple. Maximum 9000
    characters.
    :type _description: str
    :param _status: The status of the Tab. Can be OPEN, WAITING_FOR_PAYMENT,
    PAID or CANCELED.
    :type _status: str
    :param _amount_total: The total amount of the Tab.
    :type _amount_total: object_.Amount
    :param _amount_paid: The amount that has been paid for this Tab.
    :type _amount_paid: object_.Amount
    :param _qr_code_token: The token used to redirect mobile devices directly to
    the bunq app. Because they can't scan a QR code.
    :type _qr_code_token: str
    :param _tab_url: The URL redirecting user to the tab payment in the bunq
    app. Only works on mobile devices.
    :type _tab_url: str
    :param _visibility: The visibility of a Tab. A Tab can be visible trough
    NearPay, the QR code of the CashRegister and its own QR code.
    :type _visibility: object_.TabVisibility
    :param _minimum_age: The minimum age of the user paying the Tab.
    :type _minimum_age: bool
    :param _require_address: Whether or not an billing and shipping address must
    be provided when paying the Tab.
    :type _require_address: str
    :param _redirect_url: The URL which the user is sent to after paying the
    Tab.
    :type _redirect_url: str
    :param _expiration: The moment when this Tab expires.
    :type _expiration: str
    :param _alias: The alias of the party that owns this tab.
    :type _alias: object_.MonetaryAccountReference
    :param _cash_register_location: The location of the cash register that
    created this tab.
    :type _cash_register_location: object_.Geolocation
    :param _tab_item: The tab items of this tab.
    :type _tab_item: list[TabItem]
    :param _tab_attachment: An array of attachments that describe the tab.
    Uploaded through the POST /user/{userid}/attachment-tab endpoint.
    :type _tab_attachment: list[object_.BunqId]
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-single"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-single/{}"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-single/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-single/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-single"

    # Field constants.
    FIELD_MERCHANT_REFERENCE = "merchant_reference"
    FIELD_DESCRIPTION = "description"
    FIELD_STATUS = "status"
    FIELD_AMOUNT_TOTAL = "amount_total"
    FIELD_ALLOW_AMOUNT_HIGHER = "allow_amount_higher"
    FIELD_ALLOW_AMOUNT_LOWER = "allow_amount_lower"
    FIELD_WANT_TIP = "want_tip"
    FIELD_MINIMUM_AGE = "minimum_age"
    FIELD_REQUIRE_ADDRESS = "require_address"
    FIELD_REDIRECT_URL = "redirect_url"
    FIELD_VISIBILITY = "visibility"
    FIELD_EXPIRATION = "expiration"
    FIELD_TAB_ATTACHMENT = "tab_attachment"

    # Object type.
    _OBJECT_TYPE_POST = "Uuid"
    _OBJECT_TYPE_PUT = "Uuid"
    _OBJECT_TYPE_GET = "TabUsageSingle"

    def __init__(self):
        self._uuid = None
        self._created = None
        self._updated = None
        self._merchant_reference = None
        self._description = None
        self._status = None
        self._amount_total = None
        self._amount_paid = None
        self._qr_code_token = None
        self._tab_url = None
        self._visibility = None
        self._minimum_age = None
        self._require_address = None
        self._redirect_url = None
        self._expiration = None
        self._alias = None
        self._cash_register_location = None
        self._tab_item = None
        self._tab_attachment = None

    @classmethod
    def create(cls, cash_register_id, description, status, amount_total,
               monetary_account_id=None, merchant_reference=None,
               allow_amount_higher=None, allow_amount_lower=None, want_tip=None,
               minimum_age=None, require_address=None, redirect_url=None,
               visibility=None, expiration=None, tab_attachment=None,
               custom_headers=None):
        """
        Create a TabUsageSingle. The initial status must be OPEN
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :param description: The description of the Tab. Maximum 9000 characters.
        Field is required but can be an empty string.
        :type description: str
        :param status: The status of the Tab. On creation the status must be set
        to OPEN. You can change the status from OPEN to WAITING_FOR_PAYMENT.
        :type status: str
        :param amount_total: The total amount of the Tab. Must be a positive
        amount. As long as the tab has the status OPEN you can change the total
        amount. This amount is not affected by the amounts of the TabItems.
        However, if you've created any TabItems for a Tab the sum of the amounts
        of these items must be equal to the total_amount of the Tab when you
        change its status to WAITING_FOR_PAYMENT.
        :type amount_total: object_.Amount
        :param merchant_reference: The reference of the Tab, as defined by the
        owner. This reference will be set for any payment that is generated by
        this tab. Must be unique among all the owner's tabs for the used
        monetary account.
        :type merchant_reference: str
        :param allow_amount_higher: [DEPRECATED] Whether or not a higher amount
        can be paid.
        :type allow_amount_higher: bool
        :param allow_amount_lower: [DEPRECATED] Whether or not a lower amount
        can be paid.
        :type allow_amount_lower: bool
        :param want_tip: [DEPRECATED] Whether or not the user paying the Tab
        should be asked if he wants to give a tip. When want_tip is set to true,
        allow_amount_higher must also be set to true and allow_amount_lower must
        be false.
        :type want_tip: bool
        :param minimum_age: The minimum age of the user paying the Tab.
        :type minimum_age: int
        :param require_address: Whether a billing and shipping address must be
        provided when paying the Tab. Possible values are: BILLING, SHIPPING,
        BILLING_SHIPPING, NONE, OPTIONAL. Default is NONE.
        :type require_address: str
        :param redirect_url: The URL which the user is sent to after paying the
        Tab.
        :type redirect_url: str
        :param visibility: The visibility of a Tab. A Tab can be visible trough
        NearPay, the QR code of the CashRegister and its own QR code.
        :type visibility: object_.TabVisibility
        :param expiration: The moment when this Tab expires. Can be at most 1
        hour into the future.
        :type expiration: str
        :param tab_attachment: An array of attachments that describe the tab.
        Uploaded through the POST /user/{userid}/attachment-tab endpoint.
        :type tab_attachment: list[object_.BunqId]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_MERCHANT_REFERENCE: merchant_reference,
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_STATUS: status,
            cls.FIELD_AMOUNT_TOTAL: amount_total,
            cls.FIELD_ALLOW_AMOUNT_HIGHER: allow_amount_higher,
            cls.FIELD_ALLOW_AMOUNT_LOWER: allow_amount_lower,
            cls.FIELD_WANT_TIP: want_tip,
            cls.FIELD_MINIMUM_AGE: minimum_age,
            cls.FIELD_REQUIRE_ADDRESS: require_address,
            cls.FIELD_REDIRECT_URL: redirect_url,
            cls.FIELD_VISIBILITY: visibility,
            cls.FIELD_EXPIRATION: expiration,
            cls.FIELD_TAB_ATTACHMENT: tab_attachment
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id)
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def update(cls, cash_register_id, tab_usage_single_uuid,
               monetary_account_id=None, status=None, amount_total=None,
               visibility=None, expiration=None, tab_attachment=None,
               custom_headers=None):
        """
        Modify a specific TabUsageSingle. You can change the amount_total,
        status and visibility. Once you change the status to WAITING_FOR_PAYMENT
        the TabUsageSingle will expire after 5 minutes (default) or up to 1 hour
        if a different expiration is provided.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_usage_single_uuid: str
        :param status: The status of the Tab. On creation the status must be set
        to OPEN. You can change the status from OPEN to WAITING_FOR_PAYMENT.
        :type status: str
        :param amount_total: The total amount of the Tab. Must be a positive
        amount. As long as the tab has the status OPEN you can change the total
        amount. This amount is not affected by the amounts of the TabItems.
        However, if you've created any TabItems for a Tab the sum of the amounts
        of these items must be equal to the total_amount of the Tab when you
        change its status to WAITING_FOR_PAYMENT.
        :type amount_total: object_.Amount
        :param visibility: The visibility of a Tab. A Tab can be visible trough
        NearPay, the QR code of the CashRegister and its own QR code.
        :type visibility: object_.TabVisibility
        :param expiration: The moment when this Tab expires. Can be at most 1
        hour into the future.
        :type expiration: str
        :param tab_attachment: An array of attachments that describe the tab.
        Uploaded through the POST /user/{userid}/attachment-tab endpoint.
        :type tab_attachment: list[object_.BunqId]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())

        request_map = {
            cls.FIELD_STATUS: status,
            cls.FIELD_AMOUNT_TOTAL: amount_total,
            cls.FIELD_VISIBILITY: visibility,
            cls.FIELD_EXPIRATION: expiration,
            cls.FIELD_TAB_ATTACHMENT: tab_attachment
        }

        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id,
                                                       tab_usage_single_uuid)
        response_raw = api_client.put(endpoint_url, request_bytes,
                                      custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def delete(cls, cash_register_id, tab_usage_single_uuid,
               monetary_account_id=None, custom_headers=None):
        """
        Cancel a specific TabUsageSingle.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_usage_single_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(
                                                           monetary_account_id),
                                                       cash_register_id,
                                                       tab_usage_single_uuid)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @classmethod
    def get(cls, cash_register_id, tab_usage_single_uuid,
            monetary_account_id=None, custom_headers=None):
        """
        Get a specific TabUsageSingle.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_usage_single_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabUsageSingle
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_READ.format(cls._determine_user_id(),
                                                     cls._determine_monetary_account_id(
                                                         monetary_account_id),
                                                     cash_register_id,
                                                     tab_usage_single_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabUsageSingle.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_GET)
        )

    @classmethod
    def list(cls, cash_register_id, monetary_account_id=None, params=None,
             custom_headers=None):
        """
        Get a collection of TabUsageSingle.
        
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabUsageSingleList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(cls._get_api_context())
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(
            cls._determine_user_id(),
            cls._determine_monetary_account_id(monetary_account_id),
            cash_register_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabUsageSingleList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE_GET)
        )

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def merchant_reference(self):
        """
        :rtype: str
        """

        return self._merchant_reference

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def amount_total(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_total

    @property
    def amount_paid(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_paid

    @property
    def qr_code_token(self):
        """
        :rtype: str
        """

        return self._qr_code_token

    @property
    def tab_url(self):
        """
        :rtype: str
        """

        return self._tab_url

    @property
    def visibility(self):
        """
        :rtype: object_.TabVisibility
        """

        return self._visibility

    @property
    def minimum_age(self):
        """
        :rtype: bool
        """

        return self._minimum_age

    @property
    def require_address(self):
        """
        :rtype: str
        """

        return self._require_address

    @property
    def redirect_url(self):
        """
        :rtype: str
        """

        return self._redirect_url

    @property
    def expiration(self):
        """
        :rtype: str
        """

        return self._expiration

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def cash_register_location(self):
        """
        :rtype: object_.Geolocation
        """

        return self._cash_register_location

    @property
    def tab_item(self):
        """
        :rtype: list[TabItem]
        """

        return self._tab_item

    @property
    def tab_attachment(self):
        """
        :rtype: list[object_.BunqId]
        """

        return self._tab_attachment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._uuid is not None:
            return False

        if self._created is not None:
            return False

        if self._updated is not None:
            return False

        if self._merchant_reference is not None:
            return False

        if self._description is not None:
            return False

        if self._status is not None:
            return False

        if self._amount_total is not None:
            return False

        if self._amount_paid is not None:
            return False

        if self._qr_code_token is not None:
            return False

        if self._tab_url is not None:
            return False

        if self._visibility is not None:
            return False

        if self._minimum_age is not None:
            return False

        if self._require_address is not None:
            return False

        if self._redirect_url is not None:
            return False

        if self._expiration is not None:
            return False

        if self._alias is not None:
            return False

        if self._cash_register_location is not None:
            return False

        if self._tab_item is not None:
            return False

        if self._tab_attachment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabUsageSingle
        """

        return converter.json_to_class(TabUsageSingle, json_str)


class TokenQrRequestIdeal(core.BunqModel):
    """
    Using this call you create a request for payment from an external token
    provided with an ideal transaction. Make sure your iDEAL payments are
    compliant with the iDEAL standards, by following the following manual: <a
    href="https://www.bunq.com/files/media/legal/en/20170315_ideal_standards_en.pdf">https://www.bunq.com/files/media/legal/en/20170315_ideal_standards_en.pdf</a>.
    It's very important to keep these points in mind when you are using the
    endpoint to make iDEAL payments from your application.
    
    :param _id_: The id of the RequestResponse.
    :type _id_: int
    :param _time_responded: The timestamp of when the RequestResponse was
    responded to.
    :type _time_responded: str
    :param _time_expiry: The timestamp of when the RequestResponse expired or
    will expire.
    :type _time_expiry: str
    :param _monetary_account_id: The id of the MonetaryAccount the
    RequestResponse was received on.
    :type _monetary_account_id: int
    :param _amount_inquired: The requested Amount.
    :type _amount_inquired: object_.Amount
    :param _amount_responded: The Amount the RequestResponse was accepted with.
    :type _amount_responded: object_.Amount
    :param _alias: The LabelMonetaryAccount with the public information of the
    MonetaryAccount this RequestResponse was received on.
    :type _alias: object_.MonetaryAccountReference
    :param _counterparty_alias: The LabelMonetaryAccount with the public
    information of the MonetaryAccount that is requesting money with this
    RequestResponse.
    :type _counterparty_alias: object_.MonetaryAccountReference
    :param _description: The description for the RequestResponse provided by the
    requesting party. Maximum 9000 characters.
    :type _description: str
    :param _attachment: The Attachments attached to the RequestResponse.
    :type _attachment: list[object_.Attachment]
    :param _status: The status of the created RequestResponse. Can only be
    PENDING.
    :type _status: str
    :param _minimum_age: The minimum age the user accepting the RequestResponse
    must have.
    :type _minimum_age: int
    :param _require_address: Whether or not an address must be provided on
    accept.
    :type _require_address: str
    :param _address_shipping: The shipping address provided by the accepting
    user if an address was requested.
    :type _address_shipping: object_.Address
    :param _address_billing: The billing address provided by the accepting user
    if an address was requested.
    :type _address_billing: object_.Address
    :param _geolocation: The Geolocation where the RequestResponse was created.
    :type _geolocation: object_.Geolocation
    :param _redirect_url: The URL which the user is sent to after accepting or
    rejecting the Request.
    :type _redirect_url: str
    :param _type_: The type of the RequestResponse. Can be only be IDEAL.
    :type _type_: str
    :param _sub_type: The subtype of the RequestResponse. Can be only be NONE.
    :type _sub_type: str
    :param _allow_chat: Whether or not chat messages are allowed.
    :type _allow_chat: bool
    :param _eligible_whitelist_id: The whitelist id for this action or null.
    :type _eligible_whitelist_id: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/token-qr-request-ideal"

    # Field constants.
    FIELD_TOKEN = "token"

    # Object type.
    _OBJECT_TYPE_POST = "RequestResponse"

    def __init__(self):
        self._id_ = None
        self._time_responded = None
        self._time_expiry = None
        self._monetary_account_id = None
        self._amount_inquired = None
        self._amount_responded = None
        self._alias = None
        self._counterparty_alias = None
        self._description = None
        self._attachment = None
        self._status = None
        self._minimum_age = None
        self._require_address = None
        self._address_shipping = None
        self._address_billing = None
        self._geolocation = None
        self._redirect_url = None
        self._type_ = None
        self._sub_type = None
        self._allow_chat = None
        self._eligible_whitelist_id = None

    @classmethod
    def create(cls, token, custom_headers=None):
        """
        Create a request from an ideal transaction.
        
        :type user_id: int
        :param token: The token passed from a site or read from a QR code.
        :type token: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTokenQrRequestIdeal
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_TOKEN: token
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseTokenQrRequestIdeal.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_POST)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def time_responded(self):
        """
        :rtype: str
        """

        return self._time_responded

    @property
    def time_expiry(self):
        """
        :rtype: str
        """

        return self._time_expiry

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def amount_inquired(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_inquired

    @property
    def amount_responded(self):
        """
        :rtype: object_.Amount
        """

        return self._amount_responded

    @property
    def alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._alias

    @property
    def counterparty_alias(self):
        """
        :rtype: object_.MonetaryAccountReference
        """

        return self._counterparty_alias

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def attachment(self):
        """
        :rtype: list[object_.Attachment]
        """

        return self._attachment

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def minimum_age(self):
        """
        :rtype: int
        """

        return self._minimum_age

    @property
    def require_address(self):
        """
        :rtype: str
        """

        return self._require_address

    @property
    def address_shipping(self):
        """
        :rtype: object_.Address
        """

        return self._address_shipping

    @property
    def address_billing(self):
        """
        :rtype: object_.Address
        """

        return self._address_billing

    @property
    def geolocation(self):
        """
        :rtype: object_.Geolocation
        """

        return self._geolocation

    @property
    def redirect_url(self):
        """
        :rtype: str
        """

        return self._redirect_url

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def sub_type(self):
        """
        :rtype: str
        """

        return self._sub_type

    @property
    def allow_chat(self):
        """
        :rtype: bool
        """

        return self._allow_chat

    @property
    def eligible_whitelist_id(self):
        """
        :rtype: int
        """

        return self._eligible_whitelist_id

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._time_responded is not None:
            return False

        if self._time_expiry is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        if self._amount_inquired is not None:
            return False

        if self._amount_responded is not None:
            return False

        if self._alias is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._description is not None:
            return False

        if self._attachment is not None:
            return False

        if self._status is not None:
            return False

        if self._minimum_age is not None:
            return False

        if self._require_address is not None:
            return False

        if self._address_shipping is not None:
            return False

        if self._address_billing is not None:
            return False

        if self._geolocation is not None:
            return False

        if self._redirect_url is not None:
            return False

        if self._type_ is not None:
            return False

        if self._sub_type is not None:
            return False

        if self._allow_chat is not None:
            return False

        if self._eligible_whitelist_id is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TokenQrRequestIdeal
        """

        return converter.json_to_class(TokenQrRequestIdeal, json_str)


class TokenQrRequestSofort(core.BunqModel):
    """
    Using this call you can create a SOFORT Request assigned to your User by
    providing the Token of the request.
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/token-qr-request-sofort"

    # Field constants.
    FIELD_TOKEN = "token"

    # Object type.
    _OBJECT_TYPE_POST = "RequestResponse"

    @classmethod
    def create(cls, token, custom_headers=None):
        """
        Create a request from an SOFORT transaction.
        
        :type user_id: int
        :param token: The token passed from a site or read from a QR code.
        :type token: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTokenQrRequestSofort
        """

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_TOKEN: token
        }

        api_client = client.ApiClient(cls._get_api_context())
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseTokenQrRequestSofort.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE_POST)
        )

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TokenQrRequestSofort
        """

        return converter.json_to_class(TokenQrRequestSofort, json_str)


class BunqResponseInvoiceList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[Invoice]
        """

        return super().value


class BunqResponseInvoice(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: Invoice
        """

        return super().value


class BunqResponseInvoiceByUserList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[InvoiceByUser]
        """

        return super().value


class BunqResponseInvoiceByUser(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: InvoiceByUser
        """

        return super().value


class BunqResponseChatConversationList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[ChatConversation]
        """

        return super().value


class BunqResponseChatConversation(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: ChatConversation
        """

        return super().value


class BunqResponseChatMessageList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[ChatMessage]
        """

        return super().value


class BunqResponseCardDebit(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: CardDebit
        """

        return super().value


class BunqResponseCardPinChangeList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[CardPinChange]
        """

        return super().value


class BunqResponseCardPinChange(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: CardPinChange
        """

        return super().value


class BunqResponseCardResult(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: CardResult
        """

        return super().value


class BunqResponseCardResultList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[CardResult]
        """

        return super().value


class BunqResponseInt(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: int
        """

        return super().value


class BunqResponseDraftPaymentList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[DraftPayment]
        """

        return super().value


class BunqResponseDraftPayment(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: DraftPayment
        """

        return super().value


class BunqResponsePayment(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: Payment
        """

        return super().value


class BunqResponsePaymentList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[Payment]
        """

        return super().value


class BunqResponsePaymentBatch(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: PaymentBatch
        """

        return super().value


class BunqResponsePaymentBatchList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[PaymentBatch]
        """

        return super().value


class BunqResponseIdealMerchantTransaction(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: IdealMerchantTransaction
        """

        return super().value


class BunqResponseIdealMerchantTransactionList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[IdealMerchantTransaction]
        """

        return super().value


class BunqResponsePromotionDisplay(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: PromotionDisplay
        """

        return super().value


class BunqResponseRequestInquiryBatch(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: RequestInquiryBatch
        """

        return super().value


class BunqResponseRequestInquiryBatchList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[RequestInquiryBatch]
        """

        return super().value


class BunqResponseRequestInquiry(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: RequestInquiry
        """

        return super().value


class BunqResponseRequestInquiryList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[RequestInquiry]
        """

        return super().value


class BunqResponseMasterCardAction(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: MasterCardAction
        """

        return super().value


class BunqResponseMasterCardActionList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[MasterCardAction]
        """

        return super().value


class BunqResponseRequestResponse(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: RequestResponse
        """

        return super().value


class BunqResponseRequestResponseList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[RequestResponse]
        """

        return super().value


class BunqResponseScheduleInstance(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: ScheduleInstance
        """

        return super().value


class BunqResponseScheduleInstanceList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[ScheduleInstance]
        """

        return super().value


class BunqResponseTabResultResponse(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: TabResultResponse
        """

        return super().value


class BunqResponseTabResultResponseList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[TabResultResponse]
        """

        return super().value


class BunqResponseTab(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: Tab
        """

        return super().value


class BunqResponseNone(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: None
        """

        return super().value


class BunqResponseSchedule(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: Schedule
        """

        return super().value


class BunqResponseScheduleList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[Schedule]
        """

        return super().value


class BunqResponseSchedulePayment(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: SchedulePayment
        """

        return super().value


class BunqResponseSchedulePaymentList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[SchedulePayment]
        """

        return super().value


class BunqResponseShareInviteBankInquiry(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: ShareInviteBankInquiry
        """

        return super().value


class BunqResponseShareInviteBankInquiryList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[ShareInviteBankInquiry]
        """

        return super().value


class BunqResponseShareInviteBankResponse(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: ShareInviteBankResponse
        """

        return super().value


class BunqResponseShareInviteBankResponseList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[ShareInviteBankResponse]
        """

        return super().value


class BunqResponseUserCredentialPasswordIp(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: UserCredentialPasswordIp
        """

        return super().value


class BunqResponseUserCredentialPasswordIpList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[UserCredentialPasswordIp]
        """

        return super().value


class BunqResponseBytes(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: bytes
        """

        return super().value


class BunqResponseStr(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: str
        """

        return super().value


class BunqResponseAttachmentPublic(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: AttachmentPublic
        """

        return super().value


class BunqResponseAttachmentTab(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: AttachmentTab
        """

        return super().value


class BunqResponseTabAttachmentTab(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: TabAttachmentTab
        """

        return super().value


class BunqResponseAvatar(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: Avatar
        """

        return super().value


class BunqResponseBunqMeTabList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[BunqMeTab]
        """

        return super().value


class BunqResponseBunqMeTab(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: BunqMeTab
        """

        return super().value


class BunqResponseCardGeneratedCvc2(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: CardGeneratedCvc2
        """

        return super().value


class BunqResponseCardGeneratedCvc2List(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[CardGeneratedCvc2]
        """

        return super().value


class BunqResponseCardNameList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[CardName]
        """

        return super().value


class BunqResponseCard(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: Card
        """

        return super().value


class BunqResponseCardList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[Card]
        """

        return super().value


class BunqResponseCashRegisterQrCode(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: CashRegisterQrCode
        """

        return super().value


class BunqResponseCashRegisterQrCodeList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[CashRegisterQrCode]
        """

        return super().value


class BunqResponseCashRegister(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: CashRegister
        """

        return super().value


class BunqResponseCashRegisterList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[CashRegister]
        """

        return super().value


class BunqResponseCertificatePinnedList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[CertificatePinned]
        """

        return super().value


class BunqResponseCertificatePinned(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: CertificatePinned
        """

        return super().value


class BunqResponseDeviceServer(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: DeviceServer
        """

        return super().value


class BunqResponseDeviceServerList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[DeviceServer]
        """

        return super().value


class BunqResponseDevice(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: Device
        """

        return super().value


class BunqResponseDeviceList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[Device]
        """

        return super().value


class BunqResponseDraftShareInviteApiKey(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: DraftShareInviteApiKey
        """

        return super().value


class BunqResponseDraftShareInviteApiKeyList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[DraftShareInviteApiKey]
        """

        return super().value


class BunqResponseDraftShareInviteBank(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: DraftShareInviteBank
        """

        return super().value


class BunqResponseDraftShareInviteBankList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[DraftShareInviteBank]
        """

        return super().value


class BunqResponseExportAnnualOverview(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: ExportAnnualOverview
        """

        return super().value


class BunqResponseExportAnnualOverviewList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[ExportAnnualOverview]
        """

        return super().value


class BunqResponseCustomerStatementExport(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: CustomerStatementExport
        """

        return super().value


class BunqResponseCustomerStatementExportList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[CustomerStatementExport]
        """

        return super().value


class BunqResponseInstallationServerPublicKeyList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[InstallationServerPublicKey]
        """

        return super().value


class BunqResponseMonetaryAccountBank(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: MonetaryAccountBank
        """

        return super().value


class BunqResponseMonetaryAccountBankList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[MonetaryAccountBank]
        """

        return super().value


class BunqResponseMonetaryAccount(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: MonetaryAccount
        """

        return super().value


class BunqResponseMonetaryAccountList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[MonetaryAccount]
        """

        return super().value


class BunqResponseMonetaryAccountLight(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: MonetaryAccountLight
        """

        return super().value


class BunqResponseMonetaryAccountLightList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[MonetaryAccountLight]
        """

        return super().value


class BunqResponseTabResultInquiry(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: TabResultInquiry
        """

        return super().value


class BunqResponseTabResultInquiryList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[TabResultInquiry]
        """

        return super().value


class BunqResponseUser(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: User
        """

        return super().value


class BunqResponseUserList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[User]
        """

        return super().value


class BunqResponseUserLight(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: UserLight
        """

        return super().value


class BunqResponseUserPerson(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: UserPerson
        """

        return super().value


class BunqResponseUserCompany(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: UserCompany
        """

        return super().value


class BunqResponseCustomerList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[Customer]
        """

        return super().value


class BunqResponseCustomer(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: Customer
        """

        return super().value


class BunqResponseCustomerLimitList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[CustomerLimit]
        """

        return super().value


class BunqResponseBillingContractSubscriptionList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[BillingContractSubscription]
        """

        return super().value


class BunqResponsePaymentChatList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[PaymentChat]
        """

        return super().value


class BunqResponsePermittedIp(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: PermittedIp
        """

        return super().value


class BunqResponsePermittedIpList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[PermittedIp]
        """

        return super().value


class BunqResponseRequestInquiryChatList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[RequestInquiryChat]
        """

        return super().value


class BunqResponseRequestResponseChatList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[RequestResponseChat]
        """

        return super().value


class BunqResponseSandboxUser(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: SandboxUser
        """

        return super().value


class BunqResponseScheduleUserList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[ScheduleUser]
        """

        return super().value


class BunqResponseTabItemShopList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[TabItemShop]
        """

        return super().value


class BunqResponseTabItemShop(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: TabItemShop
        """

        return super().value


class BunqResponseTabUsageMultiple(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: TabUsageMultiple
        """

        return super().value


class BunqResponseTabUsageMultipleList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[TabUsageMultiple]
        """

        return super().value


class BunqResponseTabUsageSingle(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: TabUsageSingle
        """

        return super().value


class BunqResponseTabUsageSingleList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[TabUsageSingle]
        """

        return super().value


class BunqResponseTokenQrRequestIdeal(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: TokenQrRequestIdeal
        """

        return super().value


class BunqResponseTokenQrRequestSofort(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: TokenQrRequestSofort
        """

        return super().value

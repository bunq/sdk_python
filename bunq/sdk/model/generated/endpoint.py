# -*- coding: utf-8 -*-
from bunq.sdk import client
from bunq.sdk import context
from bunq.sdk import security
from bunq.sdk.json import converter
from bunq.sdk.model import core
from bunq.sdk.model.generated import object_


class Invoice(core.BunqModel):
    """
    Used to view a bunq invoice.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _invoice_date: str
    :type _invoice_number: str
    :type _status: str
    :type _group: list[object_.InvoiceItemGroup]
    :type _total_vat_inclusive: object_.Amount
    :type _total_vat_exclusive: object_.Amount
    :type _total_vat: object_.Amount
    :type _alias: object_.MonetaryAccountReference
    :type _address: object_.Address
    :type _counterparty_alias: object_.MonetaryAccountReference
    :type _counterparty_address: object_.Address
    :type _chamber_of_commerce_number: str
    :type _vat_number: str
    """

    # Field constants.
    FIELD_STATUS = "status"
    FIELD_DESCRIPTION = "description"
    FIELD_EXTERNAL_URL = "external_url"

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/invoice"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/invoice/{}"

    # Object type.
    _OBJECT_TYPE = "Invoice"

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
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseInvoiceList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, invoice_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, invoice_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseInvoice.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class InvoiceByUser(core.BunqModel):
    """
    Used to list bunq invoices by user.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _invoice_date: str
    :type _invoice_number: str
    :type _status: str
    :type _group: list[object_.InvoiceItemGroup]
    :type _total_vat_inclusive: object_.Amount
    :type _total_vat_exclusive: object_.Amount
    :type _total_vat: object_.Amount
    :type _alias: object_.MonetaryAccountReference
    :type _address: object_.Address
    :type _counterparty_alias: object_.MonetaryAccountReference
    :type _counterparty_address: object_.Address
    :type _chamber_of_commerce_number: str
    :type _vat_number: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/invoice"
    _ENDPOINT_URL_READ = "user/{}/invoice/{}"

    # Object type.
    _OBJECT_TYPE = "Invoice"

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
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInvoiceByUserList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseInvoiceByUserList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, invoice_by_user_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type invoice_by_user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInvoiceByUser
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, invoice_by_user_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseInvoiceByUser.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class ChatConversation(core.BunqModel):
    """
    Manages user's conversations.
    
    :type _SupportConversationExternal: ChatConversationSupportExternal
    :type _ChatConversationReference: ChatConversationReference
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/chat-conversation"
    _ENDPOINT_URL_READ = "user/{}/chat-conversation/{}"

    # Object type.
    _OBJECT_TYPE = "ChatConversation"

    def __init__(self):
        self._SupportConversationExternal = None
        self._ChatConversationReference = None

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseChatConversationList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseChatConversationList.cast_from_bunq_response(
            cls._from_json_list(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, chat_conversation_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type chat_conversation_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseChatConversation
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, chat_conversation_id)
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


class ChatConversationSupportExternal(core.BunqModel):
    """
    Manages user's support conversation.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _last_message: ChatMessage
    """

    # Object type.
    _OBJECT_TYPE = "SupportConversationExternal"

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


class ChatMessage(core.BunqModel):
    """
    Endpoint for retrieving the messages that are part of a conversation.
    
    :type _ChatMessageAnnouncement: ChatMessageAnnouncement
    :type _ChatMessageStatus: ChatMessageStatus
    :type _ChatMessageUser: ChatMessageUser
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/chat-conversation/{}/message"

    # Object type.
    _OBJECT_TYPE = "ChatMessage"

    def __init__(self):
        self._ChatMessageAnnouncement = None
        self._ChatMessageStatus = None
        self._ChatMessageUser = None

    @classmethod
    def list(cls, api_context, user_id, chat_conversation_id, params=None, custom_headers=None):
        """
        Get all the messages that are part of a specific conversation.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, chat_conversation_id)
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


class ChatMessageAnnouncement(core.BunqModel):
    """
    Endpoint for retrieving the messages that are part of a conversation.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _conversation_id: int
    :type _creator: object_.LabelUser
    :type _content: object_.ChatMessageContent
    """

    # Object type.
    _OBJECT_TYPE = "ChatMessageUser"

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


class CardDebit(core.BunqModel):
    """
    With bunq it is possible to order debit cards that can then be connected
    with each one of the monetary accounts the user has access to (including
    connected accounts).
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _public_uuid: str
    :type _type_: str
    :type _second_line: str
    :type _name_on_card: str
    :type _primary_account_number_four_digit: str
    :type _status: str
    :type _order_status: str
    :type _expiry_date: str
    :type _limit: list[object_.CardLimit]
    :type _country_permission: list[object_.CardCountryPermission]
    :type _label_monetary_account_ordered: object_.MonetaryAccountReference
    :type _label_monetary_account_current: object_.MonetaryAccountReference
    :type _alias: object_.LabelUser
    :type _pin_code_assignment: list[object_.CardPinAssignment]
    :type _monetary_account_id_fallback: int
    """

    # Field constants.
    FIELD_SECOND_LINE = "second_line"
    FIELD_NAME_ON_CARD = "name_on_card"
    FIELD_PIN_CODE = "pin_code"
    FIELD_ALIAS = "alias"
    FIELD_TYPE = "type"
    FIELD_PIN_CODE_ASSIGNMENT = "pin_code_assignment"
    FIELD_MONETARY_ACCOUNT_ID_FALLBACK = "monetary_account_id_fallback"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/card-debit"

    # Object type.
    _OBJECT_TYPE = "CardDebit"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._public_uuid = None
        self._type_ = None
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

    @classmethod
    def create(cls, api_context, request_map, user_id, custom_headers=None):
        """
        Create a new debit card request.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardDebit
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        request_bytes = security.encrypt(api_context, request_bytes, custom_headers)
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseCardDebit.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class CardPinChange(core.BunqModel):
    """
    View for the pin change.
    
    :type _id_: int
    :type _label_card: object_.LabelCard
    :type _label_monetary_account_current: object_.MonetaryAccountReference
    :type _time_request: str
    :type _time_accept: str
    :type _status: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/card/{}/pin-change"
    _ENDPOINT_URL_READ = "user/{}/card/{}/pin-change/{}"

    # Object type.
    _OBJECT_TYPE = "CardPinChange"

    def __init__(self):
        self._id_ = None
        self._label_card = None
        self._label_monetary_account_current = None
        self._time_request = None
        self._time_accept = None
        self._status = None

    @classmethod
    def list(cls, api_context, user_id, card_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, card_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCardPinChangeList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, card_id, card_pin_change_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, card_id, card_pin_change_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCardPinChange.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class CardResult(core.BunqModel):
    """
    Endpoint for Card result requests (failed and successful transactions).
    
    :type _monetary_account_id: int
    :type _card_id: int
    :type _amount_original: object_.Amount
    :type _amount_final: object_.Amount
    :type _decision: str
    :type _decision_description: str
    :type _decision_description_translated: str
    :type _description: str
    :type _message_type: str
    :type _authorisation_type: str
    :type _city: str
    :type _alias: object_.MonetaryAccountReference
    :type _counterparty_alias: object_.MonetaryAccountReference
    :type _label_card: object_.LabelCard
    :type _reservation_status: str
    :type _reservation_expiry_time: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/card-result/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/card-result"

    # Object type.
    _OBJECT_TYPE = "CardResult"

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
    def get(cls, api_context, user_id, monetary_account_id, card_result_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, card_result_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCardResult.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCardResultList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class DraftPayment(core.BunqModel):
    """
    A DraftPayment is like a regular Payment, but it needs to be accepted by the
    sending party before the actual Payment is done.
    
    :type _id_: int
    :type _monetary_account_id: int
    :type _user_alias_created: object_.LabelUser
    :type _responses: list[object_.DraftPaymentResponse]
    :type _status: str
    :type _type_: str
    :type _entries: list[object_.DraftPaymentEntry]
    :type _object_: core.BunqModel
    """

    # Field constants.
    FIELD_STATUS = "status"
    FIELD_ENTRIES = "entries"
    FIELD_PREVIOUS_UPDATED_TIMESTAMP = "previous_updated_timestamp"
    FIELD_NUMBER_OF_REQUIRED_ACCEPTS = "number_of_required_accepts"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/draft-payment"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/draft-payment/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/draft-payment"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/draft-payment/{}"

    # Object type.
    _OBJECT_TYPE = "DraftPayment"

    def __init__(self):
        self._id_ = None
        self._monetary_account_id = None
        self._user_alias_created = None
        self._responses = None
        self._status = None
        self._type_ = None
        self._entries = None
        self._object_ = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        Create a new DraftPayment.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, draft_payment_id, custom_headers=None):
        """
        Update a DraftPayment.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type draft_payment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, draft_payment_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        Get a listing of all DraftPayments from a given MonetaryAccount.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseDraftPaymentList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, draft_payment_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, draft_payment_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseDraftPayment.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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
        :rtype: core.BunqModel
        """

        return self._object_


class IdealMerchantTransaction(core.BunqModel):
    """
    View for requesting iDEAL transactions and polling their status.
    
    :type _monetary_account_id: int
    :type _alias: object_.MonetaryAccountReference
    :type _counterparty_alias: object_.MonetaryAccountReference
    :type _amount_guaranteed: object_.Amount
    :type _amount_requested: object_.Amount
    :type _expiration: str
    :type _issuer: str
    :type _issuer_name: str
    :type _issuer_authentication_url: str
    :type _purchase_identifier: str
    :type _status: str
    :type _status_timestamp: str
    :type _transaction_identifier: str
    :type _allow_chat: bool
    """

    # Field constants.
    FIELD_AMOUNT_REQUESTED = "amount_requested"
    FIELD_ISSUER = "issuer"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/ideal-merchant-transaction"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/ideal-merchant-transaction/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/ideal-merchant-transaction"

    # Object type.
    _OBJECT_TYPE = "IdealMerchantTransaction"

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
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, ideal_merchant_transaction_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, ideal_merchant_transaction_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseIdealMerchantTransaction.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseIdealMerchantTransactionList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class Payment(core.BunqModel):
    """
    Using Payment, you can send payments to bunq and non-bunq users from your
    bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases.
    When transferring money to other bunq MonetaryAccounts you can also refer to
    Attachments. These will be received by the counter-party as part of the
    Payment. You can also retrieve a single Payment or all executed Payments of
    a specific monetary account.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _monetary_account_id: int
    :type _amount: object_.Amount
    :type _alias: object_.MonetaryAccountReference
    :type _counterparty_alias: object_.MonetaryAccountReference
    :type _description: str
    :type _type_: str
    :type _sub_type: str
    :type _bunqto_status: str
    :type _bunqto_sub_status: str
    :type _bunqto_share_url: str
    :type _bunqto_expiry: str
    :type _bunqto_time_responded: str
    :type _attachment: list[object_.AttachmentMonetaryAccountPayment]
    :type _merchant_reference: str
    :type _batch_id: int
    :type _scheduled_id: int
    :type _address_shipping: object_.Address
    :type _address_billing: object_.Address
    :type _geolocation: object_.Geolocation
    :type _allow_chat: bool
    """

    # Field constants.
    FIELD_AMOUNT = "amount"
    FIELD_COUNTERPARTY_ALIAS = "counterparty_alias"
    FIELD_DESCRIPTION = "description"
    FIELD_ATTACHMENT = "attachment"
    FIELD_MERCHANT_REFERENCE = "merchant_reference"
    FIELD_ALLOW_BUNQTO = "allow_bunqto"
    FIELD_BUNQTO_STATUS = "bunqto_status"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/payment"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/payment/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/payment"

    # Object type.
    _OBJECT_TYPE = "Payment"

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

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        Create a new Payment.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, payment_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, payment_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponsePayment.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        Get a listing of all Payments performed on a given MonetaryAccount
        (incoming and outgoing).
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponsePaymentList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class PaymentBatch(core.BunqModel):
    """
    Create a payment batch, or show the payment batches of a monetary account.
    
    :type _payments: list[Payment]
    """

    # Field constants.
    FIELD_PAYMENTS = "payments"
    FIELD_BUNQTO_STATUS = "bunqto_status"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/payment-batch"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/payment-batch/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/payment-batch/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/payment-batch"

    # Object type.
    _OBJECT_TYPE = "PaymentBatch"

    def __init__(self):
        self._payments = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        Create a payment batch by sending an array of single payment objects,
        that will become part of the batch.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, payment_batch_id, custom_headers=None):
        """
        Revoke a bunq.to payment batch. The status of all the payments will be
        set to REVOKED.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type payment_batch_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, payment_batch_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, payment_batch_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, payment_batch_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponsePaymentBatch.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        Return all the payment batches for a monetary account.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponsePaymentBatchList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @property
    def payments(self):
        """
        :rtype: list[Payment]
        """

        return self._payments


class PromotionDisplay(core.BunqModel):
    """
    The public endpoint for retrieving and updating a promotion display model.
    
    :type _id_: int
    :type _counterparty_alias: object_.MonetaryAccountReference
    :type _event_description: str
    :type _status: str
    """

    # Field constants.
    FIELD_STATUS = "status"

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/promotion-display/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/promotion-display/{}"

    # Object type.
    _OBJECT_TYPE = "PromotionDisplay"

    def __init__(self):
        self._id_ = None
        self._counterparty_alias = None
        self._event_description = None
        self._status = None

    @classmethod
    def get(cls, api_context, user_id, promotion_display_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type promotion_display_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponsePromotionDisplay
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, promotion_display_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponsePromotionDisplay.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, promotion_display_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type promotion_display_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, promotion_display_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

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


class RequestInquiryBatch(core.BunqModel):
    """
    Create a batch of requests for payment, or show the request batches of a
    monetary account.
    
    :type _request_inquiries: list[RequestInquiry]
    :type _total_amount_inquired: object_.Amount
    """

    # Field constants.
    FIELD_REQUEST_INQUIRIES = "request_inquiries"
    FIELD_STATUS = "status"
    FIELD_TOTAL_AMOUNT_INQUIRED = "total_amount_inquired"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/request-inquiry-batch"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/request-inquiry-batch/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/request-inquiry-batch/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/request-inquiry-batch"

    # Object type.
    _OBJECT_TYPE = "RequestInquiryBatch"

    def __init__(self):
        self._request_inquiries = None
        self._total_amount_inquired = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        Create a request batch by sending an array of single request objects,
        that will become part of the batch.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, request_inquiry_batch_id, custom_headers=None):
        """
        Revoke a request batch. The status of all the requests will be set to
        REVOKED.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_batch_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, request_inquiry_batch_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, request_inquiry_batch_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, request_inquiry_batch_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseRequestInquiryBatch.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        Return all the request batches for a monetary account.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseRequestInquiryBatchList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class RequestInquiry(core.BunqModel):
    """
    RequestInquiry, aka 'RFP' (Request for Payment), is one of the innovative
    features that bunq offers. To request payment from another bunq account a
    new Request Inquiry is created. As with payments you can add attachments to
    a RFP. Requests for Payment are the foundation for a number of consumer
    features like 'Split the bill' and 'Request forwarding'. We invite you to
    invent your own based on the bunq api!
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _time_responded: str
    :type _time_expiry: str
    :type _monetary_account_id: int
    :type _amount_inquired: object_.Amount
    :type _amount_responded: object_.Amount
    :type _user_alias_created: object_.LabelUser
    :type _user_alias_revoked: object_.LabelUser
    :type _counterparty_alias: object_.MonetaryAccountReference
    :type _description: str
    :type _merchant_reference: str
    :type _attachment: list[object_.BunqId]
    :type _status: str
    :type _batch_id: int
    :type _scheduled_id: int
    :type _minimum_age: int
    :type _require_address: str
    :type _bunqme_share_url: str
    :type _redirect_url: str
    :type _address_shipping: object_.Address
    :type _address_billing: object_.Address
    :type _geolocation: object_.Geolocation
    :type _allow_chat: bool
    """

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

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/request-inquiry"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/request-inquiry/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/request-inquiry"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/request-inquiry/{}"

    # Object type.
    _OBJECT_TYPE = "RequestInquiry"

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

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        Create a new payment request.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, request_inquiry_id, custom_headers=None):
        """
        Revoke a request for payment, by updating the status to REVOKED.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestInquiry
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, request_inquiry_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseRequestInquiry.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        Get all payment requests for a user's monetary account.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseRequestInquiryList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, request_inquiry_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, request_inquiry_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseRequestInquiry.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class RequestResponse(core.BunqModel):
    """
    A RequestResponse is what a user on the other side of a RequestInquiry gets
    when he is sent one. So a RequestInquiry is the initiator and visible for
    the user that sent it and that wants to receive the money. A RequestResponse
    is what the other side sees, i.e. the user that pays the money to accept the
    request. The content is almost identical.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _time_responded: str
    :type _time_expiry: str
    :type _monetary_account_id: int
    :type _amount_inquired: object_.Amount
    :type _amount_responded: object_.Amount
    :type _status: str
    :type _description: str
    :type _alias: object_.MonetaryAccountReference
    :type _counterparty_alias: object_.MonetaryAccountReference
    :type _attachment: list[object_.Attachment]
    :type _minimum_age: int
    :type _require_address: str
    :type _geolocation: object_.Geolocation
    :type _type_: str
    :type _sub_type: str
    :type _redirect_url: str
    :type _address_billing: object_.Address
    :type _address_shipping: object_.Address
    :type _allow_chat: bool
    :type _credit_scheme_identifier: str
    :type _mandate_identifier: str
    :type _eligible_whitelist_id: int
    """

    # Field constants.
    FIELD_AMOUNT_RESPONDED = "amount_responded"
    FIELD_STATUS = "status"
    FIELD_ADDRESS_SHIPPING = "address_shipping"
    FIELD_ADDRESS_BILLING = "address_billing"

    # Endpoint constants.
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/request-response/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/request-response"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/request-response/{}"

    # Object type.
    _OBJECT_TYPE = "RequestResponse"

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

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, request_response_id, custom_headers=None):
        """
        Update the status to accept or reject the RequestResponse.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type request_response_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestResponse
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, request_response_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseRequestResponse.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        Get all RequestResponses for a MonetaryAccount.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseRequestResponseList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, request_response_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, request_response_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseRequestResponse.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class SchedulePaymentBatch(core.BunqModel):
    """
    Endpoint for schedule payment batches.
    
    :type _payments: list[object_.SchedulePaymentEntry]
    :type _schedule: object_.Schedule
    """

    # Field constants.
    FIELD_PAYMENTS = "payments"
    FIELD_SCHEDULE = "schedule"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/schedule-payment-batch"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/schedule-payment-batch/{}"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/schedule-payment-batch/{}"

    # Object type.
    _OBJECT_TYPE = "SchedulePaymentBatch"

    def __init__(self):
        self._payments = None
        self._schedule = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, schedule_payment_batch_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_payment_batch_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, schedule_payment_batch_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def delete(cls, api_context, user_id, monetary_account_id, schedule_payment_batch_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_payment_batch_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(user_id, monetary_account_id, schedule_payment_batch_id)
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
        :rtype: object_.Schedule
        """

        return self._schedule


class SchedulePayment(core.BunqModel):
    """
    Endpoint for schedule payments.
    
    :type _payment: object_.SchedulePaymentEntry
    :type _schedule: object_.Schedule
    """

    # Field constants.
    FIELD_PAYMENT = "payment"
    FIELD_SCHEDULE = "schedule"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/schedule-payment"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/schedule-payment/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/schedule-payment/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/schedule-payment"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/schedule-payment/{}"

    # Object type.
    _OBJECT_TYPE = "SchedulePayment"

    def __init__(self):
        self._payment = None
        self._schedule = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def delete(cls, api_context, user_id, monetary_account_id, schedule_payment_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_payment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(user_id, monetary_account_id, schedule_payment_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, schedule_payment_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, schedule_payment_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseSchedulePayment.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseSchedulePaymentList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, schedule_payment_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_payment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, schedule_payment_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

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
        :rtype: object_.Schedule
        """

        return self._schedule


class ScheduleInstance(core.BunqModel):
    """
    view for reading, updating and listing the scheduled instance.
    
    :type _state: str
    :type _time_start: str
    :type _time_end: str
    :type _error_message: list[object_.Error]
    :type _scheduled_object: core.BunqModel
    :type _result_object: core.BunqModel
    """

    # Field constants.
    FIELD_STATE = "state"

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/schedule/{}/schedule-instance/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/schedule/{}/schedule-instance/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/schedule/{}/schedule-instance"

    # Object type.
    _OBJECT_TYPE = "ScheduleInstance"

    def __init__(self):
        self._state = None
        self._time_start = None
        self._time_end = None
        self._error_message = None
        self._scheduled_object = None
        self._result_object = None

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, schedule_id, schedule_instance_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, schedule_id, schedule_instance_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseScheduleInstance.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, schedule_id, schedule_instance_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type schedule_id: int
        :type schedule_instance_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, schedule_id, schedule_instance_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, schedule_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, schedule_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseScheduleInstanceList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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
        :rtype: core.BunqModel
        """

        return self._scheduled_object

    @property
    def result_object(self):
        """
        :rtype: core.BunqModel
        """

        return self._result_object


class ShareInviteBankInquiry(core.BunqModel):
    """
    Used to share a monetary account with another bunq user, as in the 'Connect'
    feature in the bunq app. Allow the creation of share inquiries that, in the
    same way as request inquiries, can be revoked by the user creating them or
    accepted/rejected by the other party.
    
    :type _alias: object_.MonetaryAccountReference
    :type _user_alias_created: object_.LabelUser
    :type _user_alias_revoked: object_.LabelUser
    :type _counter_user_alias: object_.LabelUser
    :type _monetary_account_id: int
    :type _draft_share_invite_bank_id: int
    :type _share_detail: object_.ShareDetail
    :type _status: str
    :type _start_date: str
    :type _end_date: str
    :type _id_: int
    """

    # Field constants.
    FIELD_COUNTER_USER_ALIAS = "counter_user_alias"
    FIELD_DRAFT_SHARE_INVITE_BANK_ID = "draft_share_invite_bank_id"
    FIELD_SHARE_DETAIL = "share_detail"
    FIELD_STATUS = "status"
    FIELD_START_DATE = "start_date"
    FIELD_END_DATE = "end_date"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/share-invite-bank-inquiry"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/share-invite-bank-inquiry/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/share-invite-bank-inquiry/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/share-invite-bank-inquiry"

    # Object type.
    _OBJECT_TYPE = "ShareInviteBankInquiry"

    def __init__(self):
        self._alias = None
        self._user_alias_created = None
        self._user_alias_revoked = None
        self._counter_user_alias = None
        self._monetary_account_id = None
        self._draft_share_invite_bank_id = None
        self._share_detail = None
        self._status = None
        self._start_date = None
        self._end_date = None
        self._id_ = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        Create a new share inquiry for a monetary account, specifying the
        permission the other bunq user will have on it.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, share_invite_bank_inquiry_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, share_invite_bank_inquiry_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseShareInviteBankInquiry.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, share_invite_bank_inquiry_id, custom_headers=None):
        """
        Update the details of a share. This includes updating status (revoking
        or cancelling it), granted permission and validity period of this share.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type share_invite_bank_inquiry_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseShareInviteBankInquiry
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, share_invite_bank_inquiry_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseShareInviteBankInquiry.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        Get a list with all the share inquiries for a monetary account, only if
        the requesting user has permission to change the details of the various
        ones.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseShareInviteBankInquiryList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class ShareInviteBankResponse(core.BunqModel):
    """
    Used to view or respond to shares a user was invited to. See
    'share-invite-bank-inquiry' for more information about the inquiring
    endpoint.
    
    :type _counter_alias: object_.MonetaryAccountReference
    :type _user_alias_cancelled: object_.LabelUser
    :type _monetary_account_id: int
    :type _draft_share_invite_bank_id: int
    :type _share_detail: object_.ShareDetail
    :type _status: str
    :type _start_date: str
    :type _end_date: str
    :type _description: str
    """

    # Field constants.
    FIELD_STATUS = "status"

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/share-invite-bank-response/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/share-invite-bank-response/{}"
    _ENDPOINT_URL_LISTING = "user/{}/share-invite-bank-response"

    # Object type.
    _OBJECT_TYPE = "ShareInviteBankResponse"

    def __init__(self):
        self._counter_alias = None
        self._user_alias_cancelled = None
        self._monetary_account_id = None
        self._draft_share_invite_bank_id = None
        self._share_detail = None
        self._status = None
        self._start_date = None
        self._end_date = None
        self._description = None

    @classmethod
    def get(cls, api_context, user_id, share_invite_bank_response_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, share_invite_bank_response_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseShareInviteBankResponse.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, share_invite_bank_response_id, custom_headers=None):
        """
        Accept or reject a share a user was invited to.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type share_invite_bank_response_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseShareInviteBankResponse
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, share_invite_bank_response_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseShareInviteBankResponse.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        Return all the shares a user was invited to.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseShareInviteBankResponseList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseShareInviteBankResponseList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class UserCredentialPasswordIp(core.BunqModel):
    """
    Create a credential of a user for server authentication, or delete the
    credential of a user for server authentication.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _status: str
    :type _expiry_time: str
    :type _token_value: str
    :type _permitted_device: object_.PermittedDevice
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/credential-password-ip/{}"
    _ENDPOINT_URL_LISTING = "user/{}/credential-password-ip"

    # Object type.
    _OBJECT_TYPE = "CredentialPasswordIp"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._status = None
        self._expiry_time = None
        self._token_value = None
        self._permitted_device = None

    @classmethod
    def get(cls, api_context, user_id, user_credential_password_ip_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type user_credential_password_ip_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserCredentialPasswordIp
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, user_credential_password_ip_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseUserCredentialPasswordIp.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserCredentialPasswordIpList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseUserCredentialPasswordIpList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class ChatMessageStatus(core.BunqModel):
    """
    Endpoint for retrieving the messages that are part of a conversation.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _conversation_id: int
    :type _creator: object_.LabelUser
    :type _content: object_.ChatMessageContent
    """

    # Object type.
    _OBJECT_TYPE = "ChatMessageUser"

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


class ChatMessageUser(core.BunqModel):
    """
    Endpoint for retrieving the messages that are part of a conversation.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _conversation_id: int
    :type _creator: object_.LabelUser
    :type _displayed_sender: object_.LabelUser
    :type _content: object_.ChatMessageContent
    """

    # Object type.
    _OBJECT_TYPE = "ChatMessageUser"

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


class ChatConversationReference(core.BunqModel):
    """
    Represents conversation references.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    """

    # Object type.
    _OBJECT_TYPE = "SupportConversationReference"

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


class ChatMessageAttachment(core.BunqModel):
    """
    Create new messages holding file attachments.
    
    :type _id_: int
    """

    # Field constants.
    FIELD_CLIENT_MESSAGE_UUID = "client_message_uuid"
    FIELD_ATTACHMENT = "attachment"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/chat-conversation/{}/message-attachment"

    # Object type.
    _OBJECT_TYPE = "Id"

    def __init__(self):
        self._id_ = None

    @classmethod
    def create(cls, api_context, request_map, user_id, chat_conversation_id, custom_headers=None):
        """
        Create a new message holding a file attachment to a specific
        conversation.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type chat_conversation_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, chat_conversation_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_


class ChatMessageText(core.BunqModel):
    """
    Endpoint for the type of chat message that carries text.
    
    :type _id_: int
    """

    # Field constants.
    FIELD_CLIENT_MESSAGE_UUID = "client_message_uuid"
    FIELD_TEXT = "text"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/chat-conversation/{}/message-text"

    # Object type.
    _OBJECT_TYPE = "Id"

    def __init__(self):
        self._id_ = None

    @classmethod
    def create(cls, api_context, request_map, user_id, chat_conversation_id, custom_headers=None):
        """
        Add a new text message to a specific conversation.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type chat_conversation_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, chat_conversation_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_


class AttachmentConversationContent(core.BunqModel):
    """
    Fetch the raw content of an attachment with given ID. The raw content is the
    base64 of a file, without any JSON wrapping.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/chat-conversation/{}/attachment/{}/content"

    # Object type.
    _OBJECT_TYPE = "AttachmentConversationContent"

    @classmethod
    def list(cls, api_context, user_id, chat_conversation_id, attachment_id, custom_headers=None):
        """
        Get the raw content of a specific attachment.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type chat_conversation_id: int
        :type attachment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, chat_conversation_id, attachment_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )


class AttachmentPublicContent(core.BunqModel):
    """
    Fetch the raw content of a public attachment with given ID. The raw content
    is the binary representation of a file, without any JSON wrapping.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "attachment-public/{}/content"

    # Object type.
    _OBJECT_TYPE = "AttachmentPublicContent"

    @classmethod
    def list(cls, api_context, attachment_public_uuid, custom_headers=None):
        """
        Get the raw content of a specific attachment.
        
        :type api_context: context.ApiContext
        :type attachment_public_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(attachment_public_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )


class AttachmentTabContent(core.BunqModel):
    """
    Fetch the raw content of a tab attachment with given ID. The raw content is
    the binary representation of a file, without any JSON wrapping.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/attachment-tab/{}/content"

    # Object type.
    _OBJECT_TYPE = "AttachmentTabContent"

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, attachment_tab_id, custom_headers=None):
        """
        Get the raw content of a specific attachment.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type attachment_tab_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, attachment_tab_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )


class TabAttachmentTabContent(core.BunqModel):
    """
    Fetch the raw content of a tab attachment with given ID. The raw content is
    the binary representation of a file, without any JSON wrapping.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "tab/{}/attachment/{}/content"

    # Object type.
    _OBJECT_TYPE = "TabAttachmentTabContent"

    @classmethod
    def list(cls, api_context, tab_uuid, attachment_id, custom_headers=None):
        """
        Get the raw content of a specific attachment.
        
        :type api_context: context.ApiContext
        :type tab_uuid: str
        :type attachment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(tab_uuid, attachment_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )


class AttachmentMonetaryAccount(core.BunqModel):
    """
    This call is used to upload an attachment that can be referenced to in
    payment requests and payments sent from a specific monetary account.
    Attachments supported are png, jpg and gif.
    
    :type _attachment: object_.Attachment
    :type _id_: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/attachment"

    # Object type.
    _OBJECT_TYPE = "AttachmentMonetaryAccount"

    def __init__(self):
        self._attachment = None
        self._id_ = None

    @classmethod
    def create(cls, api_context, request_bytes, user_id, monetary_account_id, custom_headers=None):
        """
        Create a new monetary account attachment. Create a POST request with a
        payload that contains the binary representation of the file, without any
        JSON wrapping. Make sure you define the MIME type (i.e. image/jpeg) in
        the Content-Type header. You are required to provide a description of
        the attachment using the X-Bunq-Attachment-Description header.
        
        :type api_context: context.ApiContext
        :type request_bytes: bytes
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

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


class AttachmentPublic(core.BunqModel):
    """
    This call is used to upload an attachment that can be referenced to as an
    avatar (through the Avatar endpoint) or in a tab sent. Attachments supported
    are png, jpg and gif.
    
    :type _uuid: str
    :type _created: str
    :type _updated: str
    :type _attachment: object_.Attachment
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "attachment-public"
    _ENDPOINT_URL_READ = "attachment-public/{}"

    # Object type.
    _OBJECT_TYPE = "AttachmentPublic"

    def __init__(self):
        self._uuid = None
        self._created = None
        self._updated = None
        self._attachment = None

    @classmethod
    def create(cls, api_context, request_bytes, custom_headers=None):
        """
        Create a new public attachment. Create a POST request with a payload
        that contains a binary representation of the file, without any JSON
        wrapping. Make sure you define the MIME type (i.e. image/jpeg, or
        image/png) in the Content-Type header. You are required to provide a
        description of the attachment using the X-Bunq-Attachment-Description
        header.
        
        :type api_context: context.ApiContext
        :type request_bytes: bytes
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_CREATE
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def get(cls, api_context, attachment_public_uuid, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(attachment_public_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseAttachmentPublic.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class AttachmentTab(core.BunqModel):
    """
    This call is used to upload an attachment that will be accessible only
    through tabs. This can be used for example to upload special promotions or
    other attachments. Attachments supported are png, jpg and gif.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _attachment: object_.Attachment
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/attachment-tab"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/attachment-tab/{}"

    # Object type.
    _OBJECT_TYPE = "AttachmentTab"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._attachment = None

    @classmethod
    def create(cls, api_context, request_bytes, user_id, monetary_account_id, custom_headers=None):
        """
        Upload a new attachment to use with a tab, and to read its metadata.
        Create a POST request with a payload that contains the binary
        representation of the file, without any JSON wrapping. Make sure you
        define the MIME type (i.e. image/jpeg) in the Content-Type header. You
        are required to provide a description of the attachment using the
        X-Bunq-Attachment-Description header.
        
        :type api_context: context.ApiContext
        :type request_bytes: bytes
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, attachment_tab_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, attachment_tab_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseAttachmentTab.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class TabAttachmentTab(core.BunqModel):
    """
    This call is used to view an attachment that is linked to a tab.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _attachment: object_.Attachment
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "tab/{}/attachment/{}"

    # Object type.
    _OBJECT_TYPE = "TabAttachmentTab"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._attachment = None

    @classmethod
    def get(cls, api_context, tab_uuid, tab_attachment_tab_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(tab_uuid, tab_attachment_tab_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabAttachmentTab.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class Avatar(core.BunqModel):
    """
    Avatars are public images used to represent you or your company. Avatars are
    used to represent users, monetary accounts and cash registers. Avatars
    cannot be deleted, only replaced. Avatars can be updated after uploading the
    image you would like to use through AttachmentPublic. Using the
    attachment_public_uuid which is returned you can update your Avatar. Avatars
    used for cash registers and company accounts will be reviewed by bunq.
    
    :type _uuid: str
    :type _image: list[object_.Image]
    """

    # Field constants.
    FIELD_ATTACHMENT_PUBLIC_UUID = "attachment_public_uuid"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "avatar"
    _ENDPOINT_URL_READ = "avatar/{}"

    # Object type.
    _OBJECT_TYPE = "Avatar"

    def __init__(self):
        self._uuid = None
        self._image = None

    @classmethod
    def create(cls, api_context, request_map, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def get(cls, api_context, avatar_uuid, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type avatar_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseAvatar
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(avatar_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseAvatar.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class BunqMeTab(core.BunqModel):
    """
    bunq.me tabs allows you to create a payment request and share the link
    through e-mail, chat, etc. Multiple persons are able to respond to the
    payment request and pay through bunq, iDeal or SOFORT.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _time_expiry: str
    :type _monetary_account_id: int
    :type _status: str
    :type _bunqme_tab_share_url: str
    :type _bunqme_tab_entry: BunqMeTabEntry
    :type _result_inquiries: list[BunqMeTabResultInquiry]
    """

    # Field constants.
    FIELD_BUNQME_TAB_ENTRY = "bunqme_tab_entry"
    FIELD_STATUS = "status"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/bunqme-tab"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/bunqme-tab/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/bunqme-tab"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/bunqme-tab/{}"

    # Object type.
    _OBJECT_TYPE = "BunqMeTab"

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
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, bunq_me_tab_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type bunq_me_tab_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBunqMeTab
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, bunq_me_tab_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseBunqMeTab.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseBunqMeTabList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, bunq_me_tab_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, bunq_me_tab_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBunqMeTab.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class BunqMeTabEntry(core.BunqModel):
    """
    bunq.me tabs allows you to create a payment request and share the link
    through e-mail, chat, etc. Multiple persons are able to respond to the
    payment request and pay through bunq, iDeal or SOFORT.
    
    :type _uuid: str
    :type _amount_inquired: object_.Amount
    :type _alias: object_.MonetaryAccountReference
    :type _description: str
    :type _status: str
    :type _redirect_url: str
    :type _merchant_available: list[object_.BunqMeMerchantAvailable]
    """

    # Field constants.
    FIELD_AMOUNT_INQUIRED = "amount_inquired"
    FIELD_DESCRIPTION = "description"
    FIELD_REDIRECT_URL = "redirect_url"

    # Object type.
    _OBJECT_TYPE = "BunqMeTab"

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


class BunqMeTabResultInquiry(core.BunqModel):
    """
    Used to view bunq.me TabResultInquiry objects belonging to a tab. A
    TabResultInquiry is an object that holds details on both the tab and a
    single payment made for that tab.
    
    :type _payment: Payment
    """

    # Object type.
    _OBJECT_TYPE = "BunqMeTabResultInquiry"

    def __init__(self):
        self._payment = None



    @property
    def payment(self):
        """
        :rtype: Payment
        """

        return self._payment


class CardGeneratedCvc2(core.BunqModel):
    """
    Endpoint for generating and retrieving a new CVC2 code.
    
    :type _cvc2: str
    :type _status: str
    :type _expiry_time: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/card/{}/generated-cvc2"
    _ENDPOINT_URL_READ = "user/{}/card/{}/generated-cvc2/{}"
    _ENDPOINT_URL_LISTING = "user/{}/card/{}/generated-cvc2"

    # Object type.
    _OBJECT_TYPE = "CardGeneratedCvc2"

    def __init__(self):
        self._cvc2 = None
        self._status = None
        self._expiry_time = None

    @classmethod
    def create(cls, api_context, request_map, user_id, card_id, custom_headers=None):
        """
        Generate a new CVC2 code for a card.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type card_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardGeneratedCvc2
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        request_bytes = security.encrypt(api_context, request_bytes, custom_headers)
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, card_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseCardGeneratedCvc2.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, card_id, card_generated_cvc2_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, card_id, card_generated_cvc2_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCardGeneratedCvc2.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, card_id, params=None, custom_headers=None):
        """
        Get all generated CVC2 codes for a card.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, card_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCardGeneratedCvc2List.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

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


class CardName(core.BunqModel):
    """
    Endpoint for getting all the accepted card names for a user. As bunq do not
    allow total freedom in choosing the name that is going to be printed on the
    card, the following formats are accepted: Name Surname, N. Surname, N
    Surname or Surname.
    
    :type _possible_card_name_array: list[str]
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/card-name"

    # Object type.
    _OBJECT_TYPE = "CardUserNameArray"

    def __init__(self):
        self._possible_card_name_array = None

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        Return all the accepted card names for a specific user.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardNameList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCardNameList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @property
    def possible_card_name_array(self):
        """
        :rtype: list[str]
        """

        return self._possible_card_name_array


class CardReplace(core.BunqModel):
    """
    It is possible to order a card replacement with the bunq API.<br/><br/>You
    can order up to three free card replacements per year. Additional
    replacement requests will be billed.<br/><br/>The card replacement will have
    the same expiry date and the same pricing as the old card, but it will have
    a new card number. You can change the description and PIN through the card
    replacement endpoint.
    
    :type _id_: int
    """

    # Field constants.
    FIELD_PIN_CODE = "pin_code"
    FIELD_SECOND_LINE = "second_line"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/card/{}/replace"

    # Object type.
    _OBJECT_TYPE = "CardReplace"

    def __init__(self):
        self._id_ = None

    @classmethod
    def create(cls, api_context, request_map, user_id, card_id, custom_headers=None):
        """
        Request a card replacement.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type card_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        request_bytes = security.encrypt(api_context, request_bytes, custom_headers)
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, card_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_


class Card(core.BunqModel):
    """
    Endpoint for retrieving details for the cards the user has access to.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _public_uuid: str
    :type _type_: str
    :type _second_line: str
    :type _status: str
    :type _sub_status: str
    :type _order_status: str
    :type _expiry_date: str
    :type _name_on_card: str
    :type _primary_account_number_four_digit: str
    :type _limit: list[object_.CardLimit]
    :type _mag_stripe_permission: object_.CardMagStripePermission
    :type _country_permission: list[object_.CardCountryPermission]
    :type _label_monetary_account_ordered: object_.MonetaryAccountReference
    :type _label_monetary_account_current: object_.MonetaryAccountReference
    :type _pin_code_assignment: list[object_.CardPinAssignment]
    :type _monetary_account_id_fallback: int
    """

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

    # Endpoint constants.
    _ENDPOINT_URL_UPDATE = "user/{}/card/{}"
    _ENDPOINT_URL_READ = "user/{}/card/{}"
    _ENDPOINT_URL_LISTING = "user/{}/card"

    # Object type.
    _OBJECT_TYPE = "CardDebit"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._public_uuid = None
        self._type_ = None
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

    @classmethod
    def update(cls, api_context, request_map, user_id, card_id, custom_headers=None):
        """
        Update the card details. Allow to change pin code, status, limits,
        country permissions and the monetary account connected to the card. When
        the card has been received, it can be also activated through this
        endpoint.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type card_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCard
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        request_bytes = security.encrypt(api_context, request_bytes, custom_headers)
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, card_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseCard.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, card_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, card_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCard.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        Return all the cards available to the user.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCardList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCardList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class CashRegisterQrCodeContent(core.BunqModel):
    """
    Show the raw contents of a QR code. First you need to created a QR code
    using ../cash-register/{id}/qr-code.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/qr-code/{}/content"

    # Object type.
    _OBJECT_TYPE = "CashRegisterQrCodeContent"

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, cash_register_id, qr_code_id, custom_headers=None):
        """
        Show the raw contents of a QR code
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type qr_code_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, cash_register_id, qr_code_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )


class CashRegisterQrCode(core.BunqModel):
    """
    Once your CashRegister has been activated you can create a QR code for it.
    The visibility of a tab can be modified to be linked to this QR code. If a
    user of the bunq app scans this QR code, the linked tab will be shown on his
    device.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _status: str
    :type _cash_register: CashRegister
    :type _tab_object: Tab
    """

    # Field constants.
    FIELD_STATUS = "status"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register/{}/qr-code"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/cash-register/{}/qr-code/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/qr-code/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/qr-code"

    # Object type.
    _OBJECT_TYPE = "TokenQrCashRegister"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._status = None
        self._cash_register = None
        self._tab_object = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, cash_register_id, custom_headers=None):
        """
        Create a new QR code for this CashRegister. You can only have one ACTIVE
        CashRegister QR code at the time.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id, cash_register_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, cash_register_id, cash_register_qr_code_id, custom_headers=None):
        """
        Modify a QR code in a given CashRegister. You can only have one ACTIVE
        CashRegister QR code at the time.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type cash_register_qr_code_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, cash_register_id, cash_register_qr_code_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, cash_register_id, cash_register_qr_code_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, cash_register_id, cash_register_qr_code_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCashRegisterQrCode.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, cash_register_id, params=None, custom_headers=None):
        """
        Get a collection of QR code information from a given CashRegister
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, cash_register_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCashRegisterQrCodeList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _name: str
    :type _status: str
    :type _avatar: object_.Avatar
    :type _location: object_.Geolocation
    :type _notification_filters: list[object_.NotificationFilter]
    :type _tab_text_waiting_screen: list[object_.TabTextWaitingScreen]
    """

    # Field constants.
    FIELD_NAME = "name"
    FIELD_STATUS = "status"
    FIELD_AVATAR_UUID = "avatar_uuid"
    FIELD_LOCATION = "location"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"
    FIELD_TAB_TEXT_WAITING_SCREEN = "tab_text_waiting_screen"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/cash-register/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register"

    # Object type.
    _OBJECT_TYPE = "CashRegister"

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
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        Create a new CashRegister. Only an UserCompany can create a
        CashRegisters. They need to be created with status PENDING_APPROVAL, an
        bunq admin has to approve your CashRegister before you can use it. In
        the sandbox testing environment an CashRegister will be automatically
        approved immediately after creation.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, cash_register_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, cash_register_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCashRegister.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, cash_register_id, custom_headers=None):
        """
        Modify or close an existing CashRegister. You must set the status back
        to PENDING_APPROVAL if you modify the name, avatar or location of a
        CashRegister. To close a cash register put its status to CLOSED.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, cash_register_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        Get a collection of CashRegister for a given user and monetary account.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCashRegisterList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class Tab(core.BunqModel):
    """
    Once your CashRegister has been activated you can use it to create Tabs. A
    Tab is a template for a payment. In contrast to requests a Tab is not
    pointed towards a specific user. Any user can pay the Tab as long as it is
    made visible by you. The creation of a Tab happens with /tab-usage-single or
    /tab-usage-multiple. A TabUsageSingle is a Tab that can be paid once. A
    TabUsageMultiple is a Tab that can be paid multiple times by different
    users.
    
    :type _TabUsageSingle: TabUsageSingle
    :type _TabUsageMultiple: TabUsageMultiple
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/tab/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab"

    # Object type.
    _OBJECT_TYPE = "Tab"

    def __init__(self):
        self._TabUsageSingle = None
        self._TabUsageMultiple = None

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_uuid, custom_headers=None):
        """
        Get a specific tab. This returns a TabUsageSingle or TabUsageMultiple.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTab
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, cash_register_id, tab_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTab.cast_from_bunq_response(
            cls._from_json(response_raw)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, cash_register_id, params=None, custom_headers=None):
        """
        Get a collection of tabs.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTabList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, cash_register_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabList.cast_from_bunq_response(
            cls._from_json_list(response_raw)
        )

    @property
    def TabUsageSingle(self):
        """
        :rtype: TabUsageSingle
        """

        return self._TabUsageSingle

    @property
    def TabUsageMultiple(self):
        """
        :rtype: TabUsageMultiple
        """

        return self._TabUsageMultiple


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
    
    :type _uuid: str
    :type _created: str
    :type _updated: str
    :type _merchant_reference: str
    :type _description: str
    :type _status: str
    :type _amount_total: object_.Amount
    :type _amount_paid: object_.Amount
    :type _qr_code_token: str
    :type _tab_url: str
    :type _visibility: object_.TabVisibility
    :type _minimum_age: bool
    :type _require_address: str
    :type _redirect_url: str
    :type _expiration: str
    :type _alias: object_.MonetaryAccountReference
    :type _cash_register_location: object_.Geolocation
    :type _tab_item: list[TabItem]
    :type _tab_attachment: list[object_.BunqId]
    """

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

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-single"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-single/{}"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-single/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-single/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-single"

    # Object type.
    _OBJECT_TYPE = "TabUsageSingle"

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
    def create(cls, api_context, request_map, user_id, monetary_account_id, cash_register_id, custom_headers=None):
        """
        Create a TabUsageSingle. The initial status must be OPEN
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id, cash_register_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, cash_register_id, tab_usage_single_uuid, custom_headers=None):
        """
        Modify a specific TabUsageSingle. You can change the amount_total,
        status and visibility. Once you change the status to WAITING_FOR_PAYMENT
        the TabUsageSingle will expire after 5 minutes (default) or up to 1 hour
        if a different expiration is provided.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_usage_single_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, cash_register_id, tab_usage_single_uuid)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def delete(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_usage_single_uuid, custom_headers=None):
        """
        Cancel a specific TabUsageSingle. This request returns an empty
        response.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_usage_single_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(user_id, monetary_account_id, cash_register_id, tab_usage_single_uuid)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_usage_single_uuid, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, cash_register_id, tab_usage_single_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabUsageSingle.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, cash_register_id, params=None, custom_headers=None):
        """
        Get a collection of TabUsageSingle.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, cash_register_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabUsageSingleList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class TabItem(core.BunqModel):
    """
    Used to get items on a tab.
    
    :type _id_: int
    :type _description: str
    :type _ean_code: str
    :type _avatar_attachment: object_.AttachmentPublic
    :type _tab_attachment: list[object_.AttachmentTab]
    :type _quantity: str
    :type _amount: object_.Amount
    """

    # Object type.
    _OBJECT_TYPE = "TabItem"

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
    
    :type _uuid: str
    :type _created: str
    :type _updated: str
    :type _description: str
    :type _status: str
    :type _amount_total: object_.Amount
    :type _qr_code_token: str
    :type _tab_url: str
    :type _visibility: object_.TabVisibility
    :type _minimum_age: bool
    :type _require_address: str
    :type _redirect_url: str
    :type _expiration: str
    :type _alias: object_.MonetaryAccountReference
    :type _cash_register_location: object_.Geolocation
    :type _tab_item: list[TabItem]
    :type _tab_attachment: list[object_.BunqId]
    """

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

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-multiple"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-multiple/{}"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-multiple/{}"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-multiple/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab-usage-multiple"

    # Object type.
    _OBJECT_TYPE = "TabUsageMultiple"

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
    def create(cls, api_context, request_map, user_id, monetary_account_id, cash_register_id, custom_headers=None):
        """
        Create a TabUsageMultiple. On creation the status must be set to OPEN
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id, cash_register_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, cash_register_id, tab_usage_multiple_uuid, custom_headers=None):
        """
        Modify a specific TabUsageMultiple. You can change the amount_total,
        status and visibility. Once you change the status to PAYABLE the
        TabUsageMultiple will expire after a year (default). If you've created
        any TabItems for a Tab the sum of the amounts of these items must be
        equal to the total_amount of the Tab when you change its status to
        PAYABLE.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_usage_multiple_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseStr
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, cash_register_id, tab_usage_multiple_uuid)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseStr.cast_from_bunq_response(
            cls._process_for_uuid(response_raw)
        )

    @classmethod
    def delete(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_usage_multiple_uuid, custom_headers=None):
        """
        Close a specific TabUsageMultiple. This request returns an empty
        response.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_usage_multiple_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(user_id, monetary_account_id, cash_register_id, tab_usage_multiple_uuid)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_usage_multiple_uuid, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, cash_register_id, tab_usage_multiple_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabUsageMultiple.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, cash_register_id, params=None, custom_headers=None):
        """
        Get a collection of TabUsageMultiple.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, cash_register_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabUsageMultipleList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class CertificatePinned(core.BunqModel):
    """
    This endpoint allow you to pin the certificate chains to your account. These
    certificate chains are used for SSL validation whenever a callback is
    initiated to one of your https callback urls.
    
    :type _certificate_chain: str
    :type _id_: int
    """

    # Field constants.
    FIELD_CERTIFICATE_CHAIN = "certificate_chain"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/certificate-pinned"
    _ENDPOINT_URL_DELETE = "user/{}/certificate-pinned/{}"
    _ENDPOINT_URL_LISTING = "user/{}/certificate-pinned"
    _ENDPOINT_URL_READ = "user/{}/certificate-pinned/{}"

    # Object type.
    _OBJECT_TYPE = "CertificatePinned"

    def __init__(self):
        self._certificate_chain = None
        self._id_ = None

    @classmethod
    def create(cls, api_context, request_map, user_id, custom_headers=None):
        """
        Pin the certificate chain.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def delete(cls, api_context, user_id, certificate_pinned_id, custom_headers=None):
        """
        Remove the pinned certificate chain with the specific ID.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type certificate_pinned_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(user_id, certificate_pinned_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        List all the pinned certificate chain for the given user.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCertificatePinnedList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCertificatePinnedList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, certificate_pinned_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, certificate_pinned_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCertificatePinned.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class DeviceServer(core.BunqModel):
    """
    After having created an Installation you can now create a DeviceServer. A
    DeviceServer is needed to do a login call with session-server.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _description: str
    :type _ip: str
    :type _status: str
    """

    # Field constants.
    FIELD_DESCRIPTION = "description"
    FIELD_SECRET = "secret"
    FIELD_PERMITTED_IPS = "permitted_ips"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "device-server"
    _ENDPOINT_URL_READ = "device-server/{}"
    _ENDPOINT_URL_LISTING = "device-server"

    # Object type.
    _OBJECT_TYPE = "DeviceServer"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._description = None
        self._ip = None
        self._status = None

    @classmethod
    def create(cls, api_context, request_map, custom_headers=None):
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
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, device_server_id, custom_headers=None):
        """
        Get one of your DeviceServers.
        
        :type api_context: context.ApiContext
        :type device_server_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDeviceServer
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(device_server_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseDeviceServer.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, params=None, custom_headers=None):
        """
        Get a collection of all the DeviceServers you have created.
        
        :type api_context: context.ApiContext
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDeviceServerList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseDeviceServerList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class Device(core.BunqModel):
    """
    Used to get a Device or a listing of Devices. Creating a DeviceServer should
    happen via /device-server
    
    :type _DevicePhone: DevicePhone
    :type _DeviceServer: DeviceServer
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "device/{}"
    _ENDPOINT_URL_LISTING = "device"

    # Object type.
    _OBJECT_TYPE = "Device"

    def __init__(self):
        self._DevicePhone = None
        self._DeviceServer = None

    @classmethod
    def get(cls, api_context, device_id, custom_headers=None):
        """
        Get a single Device. A Device is either a DevicePhone or a DeviceServer.
        
        :type api_context: context.ApiContext
        :type device_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDevice
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(device_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseDevice.cast_from_bunq_response(
            cls._from_json(response_raw)
        )

    @classmethod
    def list(cls, api_context, params=None, custom_headers=None):
        """
        Get a collection of Devices. A Device is either a DevicePhone or a
        DeviceServer.
        
        :type api_context: context.ApiContext
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDeviceList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseDeviceList.cast_from_bunq_response(
            cls._from_json_list(response_raw)
        )

    @property
    def DevicePhone(self):
        """
        :rtype: DevicePhone
        """

        return self._DevicePhone

    @property
    def DeviceServer(self):
        """
        :rtype: DeviceServer
        """

        return self._DeviceServer


class DevicePhone(core.BunqModel):
    """
    Used to register a device. This is the only unsigned/verified request.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _description: str
    :type _phone_number: str
    :type _os: str
    :type _status: str
    """

    # Field constants.
    FIELD_DESCRIPTION = "description"
    FIELD_PHONE_NUMBER = "phone_number"
    FIELD_REMOVE_OLD_DEVICES = "remove_old_devices"

    # Object type.
    _OBJECT_TYPE = "DevicePhone"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._description = None
        self._phone_number = None
        self._os = None
        self._status = None



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
    def phone_number(self):
        """
        :rtype: str
        """

        return self._phone_number

    @property
    def os(self):
        """
        :rtype: str
        """

        return self._os

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status


class DraftShareInviteBankQrCodeContent(core.BunqModel):
    """
    This call returns the raw content of the QR code that links to this draft
    share invite. When a bunq user scans this QR code with the bunq app the
    draft share invite will be shown on his/her device.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/draft-share-invite-bank/{}/qr-code-content"

    # Object type.
    _OBJECT_TYPE = "DraftShareInviteBankQrCodeContent"

    @classmethod
    def list(cls, api_context, user_id, draft_share_invite_bank_id, custom_headers=None):
        """
        Returns the raw content of the QR code that links to this draft share
        invite. The raw content is the binary representation of a file, without
        any JSON wrapping.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type draft_share_invite_bank_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, draft_share_invite_bank_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )


class DraftShareInviteBank(core.BunqModel):
    """
    Used to create a draft share invite for a monetary account with another bunq
    user, as in the 'Connect' feature in the bunq app. The user that accepts the
    invite can share one of their MonetaryAccounts with the user that created
    the invite.
    
    :type _user_alias_created: object_.LabelUser
    :type _status: str
    :type _expiration: str
    :type _share_invite_bank_response_id: int
    :type _draft_share_url: str
    :type _draft_share_settings: object_.DraftShareInviteBankEntry
    :type _id_: int
    """

    # Field constants.
    FIELD_STATUS = "status"
    FIELD_EXPIRATION = "expiration"
    FIELD_DRAFT_SHARE_SETTINGS = "draft_share_settings"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/draft-share-invite-bank"
    _ENDPOINT_URL_READ = "user/{}/draft-share-invite-bank/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/draft-share-invite-bank/{}"
    _ENDPOINT_URL_LISTING = "user/{}/draft-share-invite-bank"

    # Object type.
    _OBJECT_TYPE = "DraftShareInviteBank"

    def __init__(self):
        self._user_alias_created = None
        self._status = None
        self._expiration = None
        self._share_invite_bank_response_id = None
        self._draft_share_url = None
        self._draft_share_settings = None
        self._id_ = None

    @classmethod
    def create(cls, api_context, request_map, user_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, draft_share_invite_bank_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, draft_share_invite_bank_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseDraftShareInviteBank.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, draft_share_invite_bank_id, custom_headers=None):
        """
        Update a draft share invite. When sending status CANCELLED it is
        possible to cancel the draft share invite.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type draft_share_invite_bank_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDraftShareInviteBank
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, draft_share_invite_bank_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseDraftShareInviteBank.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseDraftShareInviteBankList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseDraftShareInviteBankList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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
        :rtype: object_.DraftShareInviteBankEntry
        """

        return self._draft_share_settings

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_


class ExportAnnualOverviewContent(core.BunqModel):
    """
    Fetch the raw content of an annual overview. The annual overview is always
    in PDF format. Doc won't display the response of a request to get the
    content of an annual overview.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/export-annual-overview/{}/content"

    # Object type.
    _OBJECT_TYPE = "ExportAnnualOverviewContent"

    @classmethod
    def list(cls, api_context, user_id, export_annual_overview_id, custom_headers=None):
        """
        Used to retrieve the raw content of an annual overview.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type export_annual_overview_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, export_annual_overview_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )


class ExportAnnualOverview(core.BunqModel):
    """
    Used to create new and read existing annual overviews of all the user's
    monetary accounts. Once created, annual overviews can be downloaded in PDF
    format via the 'export-annual-overview/{id}/content' endpoint.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _year: int
    :type _alias_user: object_.LabelUser
    """

    # Field constants.
    FIELD_YEAR = "year"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/export-annual-overview"
    _ENDPOINT_URL_READ = "user/{}/export-annual-overview/{}"
    _ENDPOINT_URL_LISTING = "user/{}/export-annual-overview"

    # Object type.
    _OBJECT_TYPE = "ExportAnnualOverview"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._year = None
        self._alias_user = None

    @classmethod
    def create(cls, api_context, request_map, user_id, custom_headers=None):
        """
        Create a new annual overview for a specific year. An overview can be
        generated only for a past year.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, export_annual_overview_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, export_annual_overview_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseExportAnnualOverview.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        List all the annual overviews for a user.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseExportAnnualOverviewList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseExportAnnualOverviewList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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
    _OBJECT_TYPE = "CustomerStatementExportContent"

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, customer_statement_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type customer_statement_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, customer_statement_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )


class CustomerStatementExport(core.BunqModel):
    """
    Used to create new and read existing statement exports. Statement exports
    can be created in either CSV, MT940 or PDF file format.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _date_start: str
    :type _date_end: str
    :type _status: str
    :type _statement_number: int
    :type _statement_format: str
    :type _regional_format: str
    :type _alias_monetary_account: object_.MonetaryAccountReference
    """

    # Field constants.
    FIELD_STATEMENT_FORMAT = "statement_format"
    FIELD_DATE_START = "date_start"
    FIELD_DATE_END = "date_end"
    FIELD_REGIONAL_FORMAT = "regional_format"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/customer-statement"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/customer-statement/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/customer-statement"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/customer-statement/{}"

    # Object type.
    _OBJECT_TYPE = "CustomerStatementExport"

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
    def create(cls, api_context, request_map, user_id, monetary_account_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, customer_statement_export_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, customer_statement_export_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCustomerStatementExport.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCustomerStatementExportList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def delete(cls, api_context, user_id, monetary_account_id, customer_statement_export_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type customer_statement_export_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(user_id, monetary_account_id, customer_statement_export_id)
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


class InstallationServerPublicKey(core.BunqModel):
    """
    Using /installation/_/server-public-key you can request the ServerPublicKey
    again. This is done by referring to the id of the Installation.
    
    :type _server_public_key: str
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "installation/{}/server-public-key"

    # Object type.
    _OBJECT_TYPE = "ServerPublicKey"

    def __init__(self):
        self._server_public_key = None

    @classmethod
    def list(cls, api_context, installation_id, params=None, custom_headers=None):
        """
        Show the ServerPublicKey for this Installation.
        
        :type api_context: context.ApiContext
        :type installation_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInstallationServerPublicKeyList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(installation_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseInstallationServerPublicKeyList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @property
    def server_public_key(self):
        """
        :rtype: str
        """

        return self._server_public_key


class ShareInviteBankAmountUsed(core.BunqModel):
    """
    When you have connected your monetary account bank to a user, and given this
    user a (for example) daily budget of 10 EUR. If this users has used his
    entire budget or part of it, this call can be used to reset the amount he
    used to 0. The user can then spend the daily budget of 10 EUR again.
    """

    # Endpoint constants.
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/share-invite-bank-inquiry/{}/amount-used/{}"

    # Object type.
    _OBJECT_TYPE = "ShareInviteBankAmountUsed"

    @classmethod
    def delete(cls, api_context, user_id, monetary_account_id, share_invite_bank_inquiry_id, share_invite_bank_amount_used_id, custom_headers=None):
        """
        Reset the available budget for a bank account share. To be called
        without any ID at the end of the path.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type share_invite_bank_inquiry_id: int
        :type share_invite_bank_amount_used_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(user_id, monetary_account_id, share_invite_bank_inquiry_id, share_invite_bank_amount_used_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )


class MonetaryAccountBank(core.BunqModel):
    """
    With MonetaryAccountBank you can create a new bank account, retrieve
    information regarding your existing MonetaryAccountBanks and update specific
    fields of an existing MonetaryAccountBank. Examples of fields that can be
    updated are the description, the daily limit and the avatar of the
    account.<br/><br/>Notification filters can be set on a monetary account
    level to receive callbacks. For more information check the <a
    href="/api/1/page/callbacks">dedicated callbacks page</a>.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _avatar: object_.Avatar
    :type _currency: str
    :type _description: str
    :type _daily_limit: object_.Amount
    :type _daily_spent: object_.Amount
    :type _overdraft_limit: object_.Amount
    :type _balance: object_.Amount
    :type _alias: list[object_.Pointer]
    :type _public_uuid: str
    :type _status: str
    :type _sub_status: str
    :type _reason: str
    :type _reason_description: str
    :type _user_id: int
    :type _monetary_account_profile: MonetaryAccountProfile
    :type _notification_filters: list[object_.NotificationFilter]
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
    FIELD_SHARE = "share"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"
    FIELD_SETTING = "setting"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account-bank"
    _ENDPOINT_URL_READ = "user/{}/monetary-account-bank/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account-bank/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account-bank"

    # Object type.
    _OBJECT_TYPE = "MonetaryAccountBank"

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
    def create(cls, api_context, request_map, user_id, custom_headers=None):
        """
        Create new MonetaryAccountBank.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_bank_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_bank_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseMonetaryAccountBank.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_bank_id, custom_headers=None):
        """
        Update a specific existing MonetaryAccountBank.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_bank_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_bank_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        Gets a listing of all MonetaryAccountBanks of a given user.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseMonetaryAccountBankList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseMonetaryAccountBankList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class MonetaryAccountProfile(core.BunqModel):
    """
    Used to update and read up monetary account profiles, to keep the balance
    between specific thresholds.
    
    :type _profile_fill: object_.MonetaryAccountProfileFill
    :type _profile_drain: object_.MonetaryAccountProfileDrain
    """

    # Field constants.
    FIELD_PROFILE_FILL = "profile_fill"
    FIELD_PROFILE_DRAIN = "profile_drain"

    # Object type.
    _OBJECT_TYPE = "MonetaryAccountProfile"

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


class MonetaryAccount(core.BunqModel):
    """
    Used to show the MonetaryAccounts that you can access. Currently the only
    MonetaryAccount type is MonetaryAccountBank. See also:
    monetary-account-bank.<br/><br/>Notification filters can be set on a
    monetary account level to receive callbacks. For more information check the
    <a href="/api/2/page/callbacks">dedicated callbacks page</a>.
    
    :type _MonetaryAccountBank: MonetaryAccountBank
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account"

    # Object type.
    _OBJECT_TYPE = "MonetaryAccount"

    def __init__(self):
        self._MonetaryAccountBank = None

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseMonetaryAccount.cast_from_bunq_response(
            cls._from_json(response_raw)
        )

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        Get a collection of all your MonetaryAccounts.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseMonetaryAccountList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
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


class PaymentChat(core.BunqModel):
    """
    Manage the chat connected to a payment.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _unread_message_count: int
    """

    # Field constants.
    FIELD_LAST_READ_MESSAGE_ID = "last_read_message_id"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/payment/{}/chat"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/payment/{}/chat/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/payment/{}/chat"

    # Object type.
    _OBJECT_TYPE = "ChatConversationPayment"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._unread_message_count = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, payment_id, custom_headers=None):
        """
        Create a chat for a specific payment.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type payment_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id, payment_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, payment_id, payment_chat_id, custom_headers=None):
        """
        Update the last read message in the chat of a specific payment.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type payment_id: int
        :type payment_chat_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponsePaymentChat
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, payment_id, payment_chat_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponsePaymentChat.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, payment_id, params=None, custom_headers=None):
        """
        Get the chat for a specific payment.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, payment_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponsePaymentChatList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class PermittedIp(core.BunqModel):
    """
    Manage the IPs which may be used for a credential of a user for server
    authentication.
    
    :type _ip: str
    :type _status: str
    """

    # Field constants.
    FIELD_IP = "ip"
    FIELD_STATUS = "status"

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/credential-password-ip/{}/ip/{}"
    _ENDPOINT_URL_CREATE = "user/{}/credential-password-ip/{}/ip"
    _ENDPOINT_URL_LISTING = "user/{}/credential-password-ip/{}/ip"
    _ENDPOINT_URL_UPDATE = "user/{}/credential-password-ip/{}/ip/{}"

    # Object type.
    _OBJECT_TYPE = "PermittedIp"

    def __init__(self):
        self._ip = None
        self._status = None

    @classmethod
    def get(cls, api_context, user_id, credential_password_ip_id, permitted_ip_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, credential_password_ip_id, permitted_ip_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponsePermittedIp.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def create(cls, api_context, request_map, user_id, credential_password_ip_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type credential_password_ip_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, credential_password_ip_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def list(cls, api_context, user_id, credential_password_ip_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, credential_password_ip_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponsePermittedIpList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, credential_password_ip_id, permitted_ip_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type credential_password_ip_id: int
        :type permitted_ip_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, credential_password_ip_id, permitted_ip_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

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


class RequestInquiryChat(core.BunqModel):
    """
    Manage the chat connected to a request inquiry. In the same way a request
    inquiry and a request response are created together, so that each side of
    the interaction can work on a different object, also a request inquiry chat
    and a request response chat are created at the same time. See
    'request-response-chat' for the chat endpoint for the responding user.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _unread_message_count: int
    """

    # Field constants.
    FIELD_LAST_READ_MESSAGE_ID = "last_read_message_id"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/request-inquiry/{}/chat"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/request-inquiry/{}/chat/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/request-inquiry/{}/chat"

    # Object type.
    _OBJECT_TYPE = "RequestInquiryChat"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._unread_message_count = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, request_inquiry_id, custom_headers=None):
        """
        Create a chat for a specific request inquiry.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id, request_inquiry_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, request_inquiry_id, request_inquiry_chat_id, custom_headers=None):
        """
        Update the last read message in the chat of a specific request inquiry.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type request_inquiry_id: int
        :type request_inquiry_chat_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestInquiryChat
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, request_inquiry_id, request_inquiry_chat_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseRequestInquiryChat.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, request_inquiry_id, params=None, custom_headers=None):
        """
        Get the chat for a specific request inquiry.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, request_inquiry_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseRequestInquiryChatList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class RequestResponseChat(core.BunqModel):
    """
    Manage the chat connected to a request response. In the same way a request
    inquiry and a request response are created together, so that each side of
    the interaction can work on a different object, also a request inquiry chat
    and a request response chat are created at the same time. See
    'request-inquiry-chat' for the chat endpoint for the inquiring user.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _unread_message_count: int
    """

    # Field constants.
    FIELD_LAST_READ_MESSAGE_ID = "last_read_message_id"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/request-response/{}/chat"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/request-response/{}/chat/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/request-response/{}/chat"

    # Object type.
    _OBJECT_TYPE = "RequestResponseChat"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._unread_message_count = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, request_response_id, custom_headers=None):
        """
        Create a chat for a specific request response.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type request_response_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id, request_response_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, request_response_id, request_response_chat_id, custom_headers=None):
        """
        Update the last read message in the chat of a specific request response.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type request_response_id: int
        :type request_response_chat_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseRequestResponseChat
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, request_response_id, request_response_chat_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseRequestResponseChat.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, request_response_id, params=None, custom_headers=None):
        """
        Get the chat for a specific request response.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, request_response_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseRequestResponseChatList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class Schedule(core.BunqModel):
    """
    view for reading the scheduled definitions.
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/schedule/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/schedule"

    # Object type.
    _OBJECT_TYPE = "Schedule"

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, schedule_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, schedule_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseSchedule.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        Get a collection of scheduled definition for a given monetary account.
        You can add the parameter type to filter the response. When
        type={SCHEDULE_DEFINITION_PAYMENT,SCHEDULE_DEFINITION_PAYMENT_BATCH} is
        provided only schedule definition object that relate to these
        definitions are returned.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseScheduleList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )


class ScheduleUser(core.BunqModel):
    """
    view for reading the scheduled definitions.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/schedule"

    # Object type.
    _OBJECT_TYPE = "ScheduleUser"

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        Get a collection of scheduled definition for all accessible monetary
        accounts of the user. You can add the parameter type to filter the
        response. When
        type={SCHEDULE_DEFINITION_PAYMENT,SCHEDULE_DEFINITION_PAYMENT_BATCH} is
        provided only schedule definition object that relate to these
        definitions are returned.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseScheduleUserList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseScheduleUserList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )


class Session(core.BunqModel):
    """
    Endpoint for operations over the current session.
    """

    # Endpoint constants.
    _ENDPOINT_URL_DELETE = "session/{}"

    # Object type.
    _OBJECT_TYPE = "Session"

    @classmethod
    def delete(cls, api_context, session_id, custom_headers=None):
        """
        Deletes the current session. No response is returned for this request.
        
        :type api_context: context.ApiContext
        :type session_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseNone
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(session_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )


class TabItemShopBatch(core.BunqModel):
    """
    Create a batch of tab items.
    
    :type _tab_items: list[TabItemShop]
    """

    # Field constants.
    FIELD_TAB_ITEMS = "tab_items"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item-batch"

    # Object type.
    _OBJECT_TYPE = "TabItemShopBatch"

    def __init__(self):
        self._tab_items = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, cash_register_id, tab_uuid, custom_headers=None):
        """
        Create tab items as a batch.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id, cash_register_id, tab_uuid)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @property
    def tab_items(self):
        """
        :rtype: list[TabItemShop]
        """

        return self._tab_items


class TabItemShop(core.BunqModel):
    """
    After you’ve created a Tab using /tab-usage-single or /tab-usage-multiple
    you can add items and attachments using tab-item. You can only add or modify
    TabItems of a Tab which status is OPEN. The amount of the TabItems will not
    influence the total_amount of the corresponding Tab. However, if you've
    created any TabItems for a Tab the sum of the amounts of these items must be
    equal to the total_amount of the Tab when you change its status to
    PAYABLE/WAITING_FOR_PAYMENT.
    
    :type _id_: int
    :type _description: str
    :type _ean_code: str
    :type _avatar_attachment: object_.AttachmentPublic
    :type _tab_attachment: list[object_.AttachmentTab]
    :type _quantity: float
    :type _amount: object_.Amount
    """

    # Field constants.
    FIELD_DESCRIPTION = "description"
    FIELD_EAN_CODE = "ean_code"
    FIELD_AVATAR_ATTACHMENT_UUID = "avatar_attachment_uuid"
    FIELD_TAB_ATTACHMENT = "tab_attachment"
    FIELD_QUANTITY = "quantity"
    FIELD_AMOUNT = "amount"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item"
    _ENDPOINT_URL_UPDATE = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item/{}"
    _ENDPOINT_URL_DELETE = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item"
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-item/{}"

    # Object type.
    _OBJECT_TYPE = "TabItem"

    def __init__(self):
        self._id_ = None
        self._description = None
        self._ean_code = None
        self._avatar_attachment = None
        self._tab_attachment = None
        self._quantity = None
        self._amount = None

    @classmethod
    def create(cls, api_context, request_map, user_id, monetary_account_id, cash_register_id, tab_uuid, custom_headers=None):
        """
        Create a new TabItem for a given Tab.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id, monetary_account_id, cash_register_id, tab_uuid)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, monetary_account_id, cash_register_id, tab_uuid, tab_item_shop_id, custom_headers=None):
        """
        Modify a TabItem from a given Tab.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type tab_item_shop_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, monetary_account_id, cash_register_id, tab_uuid, tab_item_shop_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

    @classmethod
    def delete(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_uuid, tab_item_shop_id, custom_headers=None):
        """
        Delete a specific TabItem from a Tab. This request returns an empty
        response.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_DELETE.format(user_id, monetary_account_id, cash_register_id, tab_uuid, tab_item_shop_id)
        response_raw = api_client.delete(endpoint_url, custom_headers)

        return BunqResponseNone.cast_from_bunq_response(
            client.BunqResponse(None, response_raw.headers)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_uuid, params=None, custom_headers=None):
        """
        Get a collection of TabItems from a given Tab.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, cash_register_id, tab_uuid)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabItemShopList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_uuid, tab_item_shop_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, cash_register_id, tab_uuid, tab_item_shop_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabItemShop.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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


class TabResultInquiry(core.BunqModel):
    """
    Used to view TabResultInquiry objects belonging to a tab. A TabResultInquiry
    is an object that holds details on both the tab and a single payment made
    for that tab.
    
    :type _tab: Tab
    :type _payment: Payment
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-result-inquiry/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/tab-result-inquiry"

    # Object type.
    _OBJECT_TYPE = "TabResultInquiry"

    def __init__(self):
        self._tab = None
        self._payment = None

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_uuid, tab_result_inquiry_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, cash_register_id, tab_uuid, tab_result_inquiry_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabResultInquiry.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_uuid, params=None, custom_headers=None):
        """
        Used to view a list of TabResultInquiry objects belonging to a tab.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, cash_register_id, tab_uuid)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabResultInquiryList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class TabResultResponse(core.BunqModel):
    """
    Used to view TabResultResponse objects belonging to a tab. A
    TabResultResponse is an object that holds details on a tab which has been
    paid from the provided monetary account.
    
    :type _tab: Tab
    :type _payment: Payment
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}/monetary-account/{}/tab-result-response/{}"
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/tab-result-response"

    # Object type.
    _OBJECT_TYPE = "TabResultResponse"

    def __init__(self):
        self._tab = None
        self._payment = None

    @classmethod
    def get(cls, api_context, user_id, monetary_account_id, tab_result_response_id, custom_headers=None):
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, monetary_account_id, tab_result_response_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseTabResultResponse.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, params=None, custom_headers=None):
        """
        Used to view a list of TabResultResponse objects belonging to a tab.
        
        :type api_context: context.ApiContext
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

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseTabResultResponseList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class TabQrCodeContent(core.BunqModel):
    """
    This call returns the raw content of the QR code that links to this Tab.
    When a bunq user scans this QR code with the bunq app the Tab will be shown
    on his/her device.
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/monetary-account/{}/cash-register/{}/tab/{}/qr-code-content"

    # Object type.
    _OBJECT_TYPE = "TabQrCodeContent"

    @classmethod
    def list(cls, api_context, user_id, monetary_account_id, cash_register_id, tab_uuid, custom_headers=None):
        """
        Returns the raw content of the QR code that links to this Tab. The raw
        content is the binary representation of a file, without any JSON
        wrapping.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type monetary_account_id: int
        :type cash_register_id: int
        :type tab_uuid: str
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBytes
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id, monetary_account_id, cash_register_id, tab_uuid)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseBytes.cast_from_bunq_response(
            client.BunqResponse(response_raw.body_bytes, response_raw.headers)
        )


class TokenQrRequestIdeal(core.BunqModel):
    """
    Using this call you create a request for payment from an external token
    provided with an ideal transaction. Make sure your iDEAL payments are
    compliant with the iDEAL standards, by following the following manual: <a
    href="https://www.bunq.com/files/media/legal/en/20170315_ideal_standards_en.pdf">https://www.bunq.com/files/media/legal/en/20170315_ideal_standards_en.pdf</a>.
    It's very important to keep these points in mind when you are using the
    endpoint to make iDEAL payments from your application.
    
    :type _time_responded: str
    :type _time_expiry: str
    :type _monetary_account_id: int
    :type _amount_inquired: object_.Amount
    :type _amount_responded: object_.Amount
    :type _alias: object_.MonetaryAccountReference
    :type _counterparty_alias: object_.MonetaryAccountReference
    :type _description: str
    :type _attachment: list[object_.Attachment]
    :type _status: str
    :type _minimum_age: int
    :type _require_address: str
    :type _address_shipping: object_.Address
    :type _address_billing: object_.Address
    :type _geolocation: object_.Geolocation
    :type _redirect_url: str
    :type _type_: str
    :type _sub_type: str
    :type _allow_chat: bool
    :type _eligible_whitelist_id: int
    """

    # Field constants.
    FIELD_TOKEN = "token"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/token-qr-request-ideal"

    # Object type.
    _OBJECT_TYPE = "TokenQrRequestIdeal"

    def __init__(self):
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
    def create(cls, api_context, request_map, user_id, custom_headers=None):
        """
        Create a request from an ideal transaction.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseTokenQrRequestIdeal
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseTokenQrRequestIdeal.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

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


class UserCompany(core.BunqModel):
    """
    With UserCompany you can retrieve information regarding the authenticated
    UserCompany and update specific fields.<br/><br/>Notification filters can be
    set on a UserCompany level to receive callbacks. For more information check
    the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _public_uuid: str
    :type _name: str
    :type _display_name: str
    :type _public_nick_name: str
    :type _alias: list[object_.Pointer]
    :type _chamber_of_commerce_number: str
    :type _type_of_business_entity: str
    :type _sector_of_industry: str
    :type _counter_bank_iban: str
    :type _avatar: object_.Avatar
    :type _address_main: object_.Address
    :type _address_postal: object_.Address
    :type _version_terms_of_service: str
    :type _director_alias: object_.LabelUser
    :type _language: str
    :type _country: str
    :type _region: str
    :type _ubo: list[object_.Ubo]
    :type _status: str
    :type _sub_status: str
    :type _session_timeout: int
    :type _daily_limit_without_confirmation_login: object_.Amount
    :type _notification_filters: list[object_.NotificationFilter]
    :type _customer: Customer
    :type _customer_limit: CustomerLimit
    :type _billing_contract: list[BillingContractSubscription]
    """

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
    FIELD_COUNTER_BANK_IBAN = "counter_bank_iban"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user-company/{}"
    _ENDPOINT_URL_UPDATE = "user-company/{}"

    # Object type.
    _OBJECT_TYPE = "UserCompany"

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
        self._daily_limit_without_confirmation_login = None
        self._notification_filters = None
        self._customer = None
        self._customer_limit = None
        self._billing_contract = None

    @classmethod
    def get(cls, api_context, user_company_id, custom_headers=None):
        """
        Get a specific company.
        
        :type api_context: context.ApiContext
        :type user_company_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserCompany
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_company_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseUserCompany.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_company_id, custom_headers=None):
        """
        Modify a specific company's data.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_company_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_company_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

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


class Customer(core.BunqModel):
    """
    Used to view a customer.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _billing_account_id: str
    """

    # Field constants.
    FIELD_BILLING_ACCOUNT_ID = "billing_account_id"

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/customer"
    _ENDPOINT_URL_READ = "user/{}/customer/{}"
    _ENDPOINT_URL_UPDATE = "user/{}/customer/{}"

    # Object type.
    _OBJECT_TYPE = "Customer"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._billing_account_id = None

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCustomerList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCustomerList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def get(cls, api_context, user_id, customer_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type user_id: int
        :type customer_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCustomer
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id, customer_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseCustomer.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_id, customer_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type customer_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_id, customer_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

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


class CustomerLimit(core.BunqModel):
    """
    Show the limits for the authenticated user.
    
    :type _limit_monetary_account: int
    :type _limit_card_debit_maestro: int
    :type _limit_card_debit_mastercard: int
    :type _limit_card_debit_replacement: int
    """

    # Endpoint constants.
    _ENDPOINT_URL_LISTING = "user/{}/limit"

    # Object type.
    _OBJECT_TYPE = "CustomerLimit"

    def __init__(self):
        self._limit_monetary_account = None
        self._limit_card_debit_maestro = None
        self._limit_card_debit_mastercard = None
        self._limit_card_debit_replacement = None

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        Get all limits for the authenticated user.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseCustomerLimitList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseCustomerLimitList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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
    def limit_card_debit_replacement(self):
        """
        :rtype: int
        """

        return self._limit_card_debit_replacement


class BillingContractSubscription(core.BunqModel):
    """
    Show the subscription billing contract for the authenticated user.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _contract_date_start: str
    :type _contract_date_end: str
    :type _contract_version: int
    :type _subscription_type: str
    """

    # Field constants.
    FIELD_SUBSCRIPTION_TYPE = "subscription_type"

    # Endpoint constants.
    _ENDPOINT_URL_CREATE = "user/{}/billing-contract-subscription"
    _ENDPOINT_URL_LISTING = "user/{}/billing-contract-subscription"

    # Object type.
    _OBJECT_TYPE = "BillingContractSubscription"

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._contract_date_start = None
        self._contract_date_end = None
        self._contract_version = None
        self._subscription_type = None

    @classmethod
    def create(cls, api_context, request_map, user_id, custom_headers=None):
        """
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBillingContractSubscription
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(user_id)
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return BunqResponseBillingContractSubscription.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def list(cls, api_context, user_id, params=None, custom_headers=None):
        """
        Get all subscription billing contract for the authenticated user.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseBillingContractSubscriptionList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_LISTING.format(user_id)
        response_raw = api_client.get(endpoint_url, params, custom_headers)

        return BunqResponseBillingContractSubscriptionList.cast_from_bunq_response(
            cls._from_json_list(response_raw, cls._OBJECT_TYPE)
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


class UserPerson(core.BunqModel):
    """
    With UserPerson you can retrieve information regarding the authenticated
    UserPerson and update specific fields.<br/><br/>Notification filters can be
    set on a UserPerson level to receive callbacks. For more information check
    the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _public_uuid: str
    :type _first_name: str
    :type _middle_name: str
    :type _last_name: str
    :type _legal_name: str
    :type _display_name: str
    :type _public_nick_name: str
    :type _alias: list[object_.Pointer]
    :type _tax_resident: list[object_.TaxResident]
    :type _document_type: str
    :type _document_number: str
    :type _document_country_of_issuance: str
    :type _address_main: object_.Address
    :type _address_postal: object_.Address
    :type _date_of_birth: str
    :type _place_of_birth: str
    :type _country_of_birth: str
    :type _nationality: str
    :type _language: str
    :type _region: str
    :type _gender: str
    :type _avatar: object_.Avatar
    :type _version_terms_of_service: str
    :type _status: str
    :type _sub_status: str
    :type _session_timeout: int
    :type _daily_limit_without_confirmation_login: object_.Amount
    :type _notification_filters: list[object_.NotificationFilter]
    """

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
    FIELD_DAILY_LIMIT_WITHOUT_CONFIRMATION_LOGIN = "daily_limit_without_confirmation_login"
    FIELD_COUNTER_BANK_IBAN = "counter_bank_iban"
    FIELD_NOTIFICATION_FILTERS = "notification_filters"

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user-person/{}"
    _ENDPOINT_URL_UPDATE = "user-person/{}"

    # Object type.
    _OBJECT_TYPE = "UserPerson"

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
    def get(cls, api_context, user_person_id, custom_headers=None):
        """
        Get a specific person.
        
        :type api_context: context.ApiContext
        :type user_person_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserPerson
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_person_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseUserPerson.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
        )

    @classmethod
    def update(cls, api_context, request_map, user_person_id, custom_headers=None):
        """
        Modify a specific person object's data.
        
        :type api_context: context.ApiContext
        :type request_map: dict[str, object]
        :type user_person_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseInt
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_UPDATE.format(user_person_id)
        response_raw = api_client.put(endpoint_url, request_bytes, custom_headers)

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


class User(core.BunqModel):
    """
    Using this call you can retrieve information of the user you are logged in
    as. This includes your user id, which is referred to in endpoints.
    
    :type _UserLight: UserLight
    :type _UserPerson: UserPerson
    :type _UserCompany: UserCompany
    """

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user/{}"
    _ENDPOINT_URL_LISTING = "user"

    # Object type.
    _OBJECT_TYPE = "User"

    def __init__(self):
        self._UserLight = None
        self._UserPerson = None
        self._UserCompany = None

    @classmethod
    def get(cls, api_context, user_id, custom_headers=None):
        """
        Get a specific user.
        
        :type api_context: context.ApiContext
        :type user_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUser
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseUser.cast_from_bunq_response(
            cls._from_json(response_raw)
        )

    @classmethod
    def list(cls, api_context, params=None, custom_headers=None):
        """
        Get a collection of all available users.
        
        :type api_context: context.ApiContext
        :type params: dict[str, str]|None
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserList
        """

        if params is None:
            params = {}

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
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


class UserLight(core.BunqModel):
    """
    Show the authenticated user, if it is a light user.
    
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _public_uuid: str
    :type _first_name: str
    :type _middle_name: str
    :type _last_name: str
    :type _legal_name: str
    :type _display_name: str
    :type _public_nick_name: str
    :type _alias: list[object_.Pointer]
    :type _social_security_number: str
    :type _tax_resident: list[object_.TaxResident]
    :type _document_type: str
    :type _document_number: str
    :type _document_country_of_issuance: str
    :type _address_main: object_.Address
    :type _address_postal: object_.Address
    :type _date_of_birth: str
    :type _place_of_birth: str
    :type _country_of_birth: str
    :type _nationality: str
    :type _language: str
    :type _region: str
    :type _gender: str
    :type _avatar: object_.Avatar
    :type _version_terms_of_service: str
    :type _status: str
    :type _sub_status: str
    :type _session_timeout: int
    :type _daily_limit_without_confirmation_login: object_.Amount
    :type _notification_filters: list[object_.NotificationFilter]
    """

    # Field constants.
    FIELD_FIRST_NAME = "first_name"
    FIELD_MIDDLE_NAME = "middle_name"
    FIELD_LAST_NAME = "last_name"
    FIELD_PUBLIC_NICK_NAME = "public_nick_name"
    FIELD_COUNTER_BANK_IBAN = "counter_bank_iban"
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

    # Endpoint constants.
    _ENDPOINT_URL_READ = "user-light/{}"

    # Object type.
    _OBJECT_TYPE = "UserPerson"

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
    def get(cls, api_context, user_light_id, custom_headers=None):
        """
        Get a specific bunq light user.
        
        :type api_context: context.ApiContext
        :type user_light_id: int
        :type custom_headers: dict[str, str]|None
        
        :rtype: BunqResponseUserLight
        """

        if custom_headers is None:
            custom_headers = {}

        api_client = client.ApiClient(api_context)
        endpoint_url = cls._ENDPOINT_URL_READ.format(user_light_id)
        response_raw = api_client.get(endpoint_url, {}, custom_headers)

        return BunqResponseUserLight.cast_from_bunq_response(
            cls._from_json(response_raw, cls._OBJECT_TYPE)
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

    
class BunqResponseNone(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: None
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

    
class BunqResponseBunqMeTab(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: BunqMeTab
        """
 
        return super().value

    
class BunqResponseBunqMeTabList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[BunqMeTab]
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

    
class BunqResponseTab(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: Tab
        """
 
        return super().value

    
class BunqResponseTabList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[Tab]
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

    
class BunqResponsePaymentChat(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: PaymentChat
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

    
class BunqResponseRequestInquiryChat(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: RequestInquiryChat
        """
 
        return super().value

    
class BunqResponseRequestInquiryChatList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[RequestInquiryChat]
        """
 
        return super().value

    
class BunqResponseRequestResponseChat(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: RequestResponseChat
        """
 
        return super().value

    
class BunqResponseRequestResponseChatList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[RequestResponseChat]
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

    
class BunqResponseTokenQrRequestIdeal(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: TokenQrRequestIdeal
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

    
class BunqResponseBillingContractSubscription(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: BillingContractSubscription
        """
 
        return super().value

    
class BunqResponseBillingContractSubscriptionList(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: list[BillingContractSubscription]
        """
 
        return super().value

    
class BunqResponseUserPerson(client.BunqResponse):
    @property
    def value(self):
        """
        :rtype: UserPerson
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


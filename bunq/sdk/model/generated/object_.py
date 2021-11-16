# -*- coding: utf-8 -*-
from bunq.sdk.exception.bunq_exception import BunqException
from bunq.sdk.json import converter
from bunq.sdk.model.core.anchor_object_interface import AnchorObjectInterface
from bunq.sdk.model.core.bunq_model import BunqModel
from bunq.sdk.model.generated import endpoint


class Amount(BunqModel):
    """
    :param _value: The amount formatted to two decimal places.
    :type _value: str
    :param _currency: The currency of the amount. It is an ISO 4217 formatted
    currency code.
    :type _currency: str
    """

    _value = None
    _currency = None
    _value_field_for_request = None
    _currency_field_for_request = None

    def __init__(self, value=None, currency=None):
        """
        :param value: The amount formatted to two decimal places.
        :type value: str
        :param currency: The currency of the amount. It is an ISO 4217 formatted
        currency code.
        :type currency: str
        """

        self._value_field_for_request = value
        self._currency_field_for_request = currency

    @property
    def value(self):
        """
        :rtype: str
        """

        return self._value

    @property
    def currency(self):
        """
        :rtype: str
        """

        return self._currency

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._value is not None:
            return False

        if self._currency is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Amount
        """

        return converter.json_to_class(Amount, json_str)


class InvoiceItemGroup(BunqModel):
    """
    :param _type_: The type of the invoice item group.
    :type _type_: str
    :param _type_description: The description of the type of the invoice item
    group.
    :type _type_description: str
    :param _type_description_translated: The translated description of the type
    of the invoice item group.
    :type _type_description_translated: str
    :param _instance_description: The identifier of the invoice item group.
    :type _instance_description: str
    :param _product_vat_exclusive: The unit item price excluding VAT.
    :type _product_vat_exclusive: Amount
    :param _product_vat_inclusive: The unit item price including VAT.
    :type _product_vat_inclusive: Amount
    :param _item: The invoice items in the group.
    :type _item: list[InvoiceItem]
    """

    _type_ = None
    _type_description = None
    _type_description_translated = None
    _instance_description = None
    _product_vat_exclusive = None
    _product_vat_inclusive = None
    _item = None

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def type_description(self):
        """
        :rtype: str
        """

        return self._type_description

    @property
    def type_description_translated(self):
        """
        :rtype: str
        """

        return self._type_description_translated

    @property
    def instance_description(self):
        """
        :rtype: str
        """

        return self._instance_description

    @property
    def product_vat_exclusive(self):
        """
        :rtype: Amount
        """

        return self._product_vat_exclusive

    @property
    def product_vat_inclusive(self):
        """
        :rtype: Amount
        """

        return self._product_vat_inclusive

    @property
    def item(self):
        """
        :rtype: list[InvoiceItem]
        """

        return self._item

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._type_ is not None:
            return False

        if self._type_description is not None:
            return False

        if self._type_description_translated is not None:
            return False

        if self._instance_description is not None:
            return False

        if self._product_vat_exclusive is not None:
            return False

        if self._product_vat_inclusive is not None:
            return False

        if self._item is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: InvoiceItemGroup
        """

        return converter.json_to_class(InvoiceItemGroup, json_str)


class InvoiceItem(BunqModel):
    """
    :param _billing_date: The billing date of the item.
    :type _billing_date: str
    :param _type_description: The price description.
    :type _type_description: str
    :param _type_description_translated: The translated price description.
    :type _type_description_translated: str
    :param _unit_vat_exclusive: The unit item price excluding VAT.
    :type _unit_vat_exclusive: Amount
    :param _unit_vat_inclusive: The unit item price including VAT.
    :type _unit_vat_inclusive: Amount
    :param _vat: The VAT tax fraction.
    :type _vat: float
    :param _quantity: The number of items priced.
    :type _quantity: float
    :param _total_vat_exclusive: The item price excluding VAT.
    :type _total_vat_exclusive: Amount
    :param _total_vat_inclusive: The item price including VAT.
    :type _total_vat_inclusive: Amount
    """

    _billing_date = None
    _type_description = None
    _type_description_translated = None
    _unit_vat_exclusive = None
    _unit_vat_inclusive = None
    _vat = None
    _quantity = None
    _total_vat_exclusive = None
    _total_vat_inclusive = None

    @property
    def billing_date(self):
        """
        :rtype: str
        """

        return self._billing_date

    @property
    def type_description(self):
        """
        :rtype: str
        """

        return self._type_description

    @property
    def type_description_translated(self):
        """
        :rtype: str
        """

        return self._type_description_translated

    @property
    def unit_vat_exclusive(self):
        """
        :rtype: Amount
        """

        return self._unit_vat_exclusive

    @property
    def unit_vat_inclusive(self):
        """
        :rtype: Amount
        """

        return self._unit_vat_inclusive

    @property
    def vat(self):
        """
        :rtype: float
        """

        return self._vat

    @property
    def quantity(self):
        """
        :rtype: float
        """

        return self._quantity

    @property
    def total_vat_exclusive(self):
        """
        :rtype: Amount
        """

        return self._total_vat_exclusive

    @property
    def total_vat_inclusive(self):
        """
        :rtype: Amount
        """

        return self._total_vat_inclusive

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._billing_date is not None:
            return False

        if self._type_description is not None:
            return False

        if self._type_description_translated is not None:
            return False

        if self._unit_vat_exclusive is not None:
            return False

        if self._unit_vat_inclusive is not None:
            return False

        if self._vat is not None:
            return False

        if self._quantity is not None:
            return False

        if self._total_vat_exclusive is not None:
            return False

        if self._total_vat_inclusive is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: InvoiceItem
        """

        return converter.json_to_class(InvoiceItem, json_str)


class LabelMonetaryAccount(BunqModel):
    """
    :param _iban: The IBAN of the monetary account.
    :type _iban: str
    :param _display_name: The name to display with this monetary account.
    :type _display_name: str
    :param _avatar: The avatar of the monetary account.
    :type _avatar: Avatar
    :param _label_user: The user this monetary account belongs to.
    :type _label_user: LabelUser
    :param _country: The country of the user. Formatted as a ISO 3166-1 alpha-2
    country code.
    :type _country: str
    :param _bunq_me: Bunq.me pointer with type and value.
    :type _bunq_me: MonetaryAccountReference
    :param _is_light: Whether or not the monetary account is light.
    :type _is_light: bool
    :param _swift_bic: The BIC used for a SWIFT payment.
    :type _swift_bic: str
    :param _swift_account_number: The account number used for a SWIFT payment.
    May or may not be an IBAN.
    :type _swift_account_number: str
    :param _transferwise_account_number: The account number used for a
    Transferwise payment. May or may not be an IBAN.
    :type _transferwise_account_number: str
    :param _transferwise_bank_code: The bank code used for a Transferwise
    payment. May or may not be a BIC.
    :type _transferwise_bank_code: str
    :param _merchant_category_code: The merchant category code.
    :type _merchant_category_code: str
    """

    _iban = None
    _display_name = None
    _avatar = None
    _label_user = None
    _country = None
    _bunq_me = None
    _is_light = None
    _swift_bic = None
    _swift_account_number = None
    _transferwise_account_number = None
    _transferwise_bank_code = None
    _merchant_category_code = None

    @property
    def iban(self):
        """
        :rtype: str
        """

        return self._iban

    @property
    def display_name(self):
        """
        :rtype: str
        """

        return self._display_name

    @property
    def avatar(self):
        """
        :rtype: Avatar
        """

        return self._avatar

    @property
    def label_user(self):
        """
        :rtype: LabelUser
        """

        return self._label_user

    @property
    def country(self):
        """
        :rtype: str
        """

        return self._country

    @property
    def bunq_me(self):
        """
        :rtype: MonetaryAccountReference
        """

        return self._bunq_me

    @property
    def is_light(self):
        """
        :rtype: bool
        """

        return self._is_light

    @property
    def swift_bic(self):
        """
        :rtype: str
        """

        return self._swift_bic

    @property
    def swift_account_number(self):
        """
        :rtype: str
        """

        return self._swift_account_number

    @property
    def transferwise_account_number(self):
        """
        :rtype: str
        """

        return self._transferwise_account_number

    @property
    def transferwise_bank_code(self):
        """
        :rtype: str
        """

        return self._transferwise_bank_code

    @property
    def merchant_category_code(self):
        """
        :rtype: str
        """

        return self._merchant_category_code

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._iban is not None:
            return False

        if self._display_name is not None:
            return False

        if self._avatar is not None:
            return False

        if self._label_user is not None:
            return False

        if self._country is not None:
            return False

        if self._bunq_me is not None:
            return False

        if self._is_light is not None:
            return False

        if self._swift_bic is not None:
            return False

        if self._swift_account_number is not None:
            return False

        if self._transferwise_account_number is not None:
            return False

        if self._transferwise_bank_code is not None:
            return False

        if self._merchant_category_code is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: LabelMonetaryAccount
        """

        return converter.json_to_class(LabelMonetaryAccount, json_str)


class Avatar(BunqModel):
    """
    :param _uuid: The public UUID of the avatar.
    :type _uuid: str
    :param _anchor_uuid: The public UUID of object this avatar is anchored to.
    :type _anchor_uuid: str
    :param _image: The actual image information of this avatar.
    :type _image: list[Image]
    """

    _uuid = None
    _anchor_uuid = None
    _image = None
    _uuid_field_for_request = None

    def __init__(self, uuid=None):
        """
        :param uuid: The public UUID of the avatar.
        :type uuid: str
        """

        self._uuid_field_for_request = uuid

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

    @property
    def anchor_uuid(self):
        """
        :rtype: str
        """

        return self._anchor_uuid

    @property
    def image(self):
        """
        :rtype: list[Image]
        """

        return self._image

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._uuid is not None:
            return False

        if self._anchor_uuid is not None:
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


class Image(BunqModel):
    """
    :param _attachment_public_uuid: The public UUID of the public attachment
    containing the image.
    :type _attachment_public_uuid: str
    :param _content_type: The content-type as a MIME filetype.
    :type _content_type: str
    :param _height: The image height in pixels.
    :type _height: int
    :param _width: The image width in pixels.
    :type _width: int
    """

    _attachment_public_uuid = None
    _content_type = None
    _height = None
    _width = None

    @property
    def attachment_public_uuid(self):
        """
        :rtype: str
        """

        return self._attachment_public_uuid

    @property
    def content_type(self):
        """
        :rtype: str
        """

        return self._content_type

    @property
    def height(self):
        """
        :rtype: int
        """

        return self._height

    @property
    def width(self):
        """
        :rtype: int
        """

        return self._width

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._attachment_public_uuid is not None:
            return False

        if self._content_type is not None:
            return False

        if self._height is not None:
            return False

        if self._width is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Image
        """

        return converter.json_to_class(Image, json_str)


class LabelUser(BunqModel):
    """
    :param _uuid: The public UUID of the label-user.
    :type _uuid: str
    :param _display_name: The name to be displayed for this user, as it was
    given on the request.
    :type _display_name: str
    :param _country: The country of the user. 000 stands for "unknown"
    :type _country: str
    :param _avatar: The current avatar of the user.
    :type _avatar: Avatar
    :param _public_nick_name: The current nickname of the user.
    :type _public_nick_name: str
    """

    _uuid = None
    _avatar = None
    _public_nick_name = None
    _display_name = None
    _country = None
    _uuid_field_for_request = None
    _display_name_field_for_request = None
    _country_field_for_request = None

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

        self._uuid_field_for_request = uuid
        self._display_name_field_for_request = display_name
        self._country_field_for_request = country

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

    @property
    def avatar(self):
        """
        :rtype: Avatar
        """

        return self._avatar

    @property
    def public_nick_name(self):
        """
        :rtype: str
        """

        return self._public_nick_name

    @property
    def display_name(self):
        """
        :rtype: str
        """

        return self._display_name

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

        if self._uuid is not None:
            return False

        if self._avatar is not None:
            return False

        if self._public_nick_name is not None:
            return False

        if self._display_name is not None:
            return False

        if self._country is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: LabelUser
        """

        return converter.json_to_class(LabelUser, json_str)


class Pointer(BunqModel):
    """
    :param _type_: The alias type, can be: EMAIL|PHONE_NUMBER|IBAN.
    :type _type_: str
    :param _value: The alias value.
    :type _value: str
    :param _name: The alias name.
    :type _name: str
    """

    _type_ = None
    _value = None
    _name = None
    _type__field_for_request = None
    _value_field_for_request = None
    _name_field_for_request = None

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

        self._type__field_for_request = type_
        self._value_field_for_request = value
        self._name_field_for_request = name

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def value(self):
        """
        :rtype: str
        """

        return self._value

    @property
    def name(self):
        """
        :rtype: str
        """

        return self._name

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._type_ is not None:
            return False

        if self._value is not None:
            return False

        if self._name is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Pointer
        """

        return converter.json_to_class(Pointer, json_str)


class Address(BunqModel):
    """
    :param _street: The street.
    :type _street: str
    :param _house_number: The house number.
    :type _house_number: str
    :param _po_box: The PO box.
    :type _po_box: str
    :param _postal_code: The postal code.
    :type _postal_code: str
    :param _city: The city.
    :type _city: str
    :param _country: The country as an ISO 3166-1 alpha-2 country code.
    :type _country: str
    :param _extra: The apartment, building or other extra information for
    addresses.
    :type _extra: str
    :param _mailbox_name: The name on the mailbox (only used for Postal
    addresses).
    :type _mailbox_name: str
    :param _province: The province according to local standard.
    :type _province: str
    """

    _street = None
    _house_number = None
    _po_box = None
    _postal_code = None
    _city = None
    _country = None
    _province = None
    _extra = None
    _mailbox_name = None
    _street_field_for_request = None
    _house_number_field_for_request = None
    _po_box_field_for_request = None
    _postal_code_field_for_request = None
    _city_field_for_request = None
    _country_field_for_request = None
    _extra_field_for_request = None
    _mailbox_name_field_for_request = None

    def __init__(self, street=None, house_number=None, postal_code=None, city=None, country=None, po_box=None,
                 extra=None, mailbox_name=None):
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
        :param extra: The apartment, building or other extra information for
        addresses.
        :type extra: str
        :param mailbox_name: The name on the mailbox (only used for Postal
        addresses).
        :type mailbox_name: str
        """

        self._street_field_for_request = street
        self._house_number_field_for_request = house_number
        self._postal_code_field_for_request = postal_code
        self._city_field_for_request = city
        self._country_field_for_request = country
        self._po_box_field_for_request = po_box
        self._extra_field_for_request = extra
        self._mailbox_name_field_for_request = mailbox_name

    @property
    def street(self):
        """
        :rtype: str
        """

        return self._street

    @property
    def house_number(self):
        """
        :rtype: str
        """

        return self._house_number

    @property
    def po_box(self):
        """
        :rtype: str
        """

        return self._po_box

    @property
    def postal_code(self):
        """
        :rtype: str
        """

        return self._postal_code

    @property
    def city(self):
        """
        :rtype: str
        """

        return self._city

    @property
    def country(self):
        """
        :rtype: str
        """

        return self._country

    @property
    def province(self):
        """
        :rtype: str
        """

        return self._province

    @property
    def extra(self):
        """
        :rtype: str
        """

        return self._extra

    @property
    def mailbox_name(self):
        """
        :rtype: str
        """

        return self._mailbox_name

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._street is not None:
            return False

        if self._house_number is not None:
            return False

        if self._po_box is not None:
            return False

        if self._postal_code is not None:
            return False

        if self._city is not None:
            return False

        if self._country is not None:
            return False

        if self._province is not None:
            return False

        if self._extra is not None:
            return False

        if self._mailbox_name is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Address
        """

        return converter.json_to_class(Address, json_str)


class RequestInquiryReference(BunqModel):
    """
    :param _type_: The type of request inquiry. Can be RequestInquiry or
    RequestInquiryBatch.
    :type _type_: str
    :param _id_: The id of the request inquiry (batch).
    :type _id_: int
    """

    _type_ = None
    _id_ = None

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

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

        if self._type_ is not None:
            return False

        if self._id_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RequestInquiryReference
        """

        return converter.json_to_class(RequestInquiryReference, json_str)


class Attachment(BunqModel):
    """
    :param _description: The description of the attachment.
    :type _description: str
    :param _content_type: The content type of the attachment's file.
    :type _content_type: str
    """

    _description = None
    _content_type = None

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def content_type(self):
        """
        :rtype: str
        """

        return self._content_type

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._description is not None:
            return False

        if self._content_type is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Attachment
        """

        return converter.json_to_class(Attachment, json_str)


class AttachmentMonetaryAccountPayment(BunqModel):
    """
    :param _id_: The id of the attached Attachment.
    :type _id_: int
    :param _monetary_account_id: The id of the MonetaryAccount this Attachment
    is attached from.
    :type _monetary_account_id: int
    """

    _id_ = None
    _monetary_account_id = None
    _id__field_for_request = None

    def __init__(self, id_):
        """
        :param id_: The id of the Attachment to attach to the MonetaryAccount.
        :type id_: int
        """

        self._id__field_for_request = id_

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

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentMonetaryAccountPayment
        """

        return converter.json_to_class(AttachmentMonetaryAccountPayment, json_str)


class Geolocation(BunqModel):
    """
    :param _latitude: The latitude for a geolocation restriction.
    :type _latitude: float
    :param _longitude: The longitude for a geolocation restriction.
    :type _longitude: float
    :param _altitude: The altitude for a geolocation restriction.
    :type _altitude: float
    :param _radius: The radius for a geolocation restriction.
    :type _radius: float
    """

    _latitude = None
    _longitude = None
    _altitude = None
    _radius = None
    _latitude_field_for_request = None
    _longitude_field_for_request = None
    _altitude_field_for_request = None
    _radius_field_for_request = None

    def __init__(self, latitude=None, longitude=None, altitude=None, radius=None):
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

        self._latitude_field_for_request = latitude
        self._longitude_field_for_request = longitude
        self._altitude_field_for_request = altitude
        self._radius_field_for_request = radius

    @property
    def latitude(self):
        """
        :rtype: float
        """

        return self._latitude

    @property
    def longitude(self):
        """
        :rtype: float
        """

        return self._longitude

    @property
    def altitude(self):
        """
        :rtype: float
        """

        return self._altitude

    @property
    def radius(self):
        """
        :rtype: float
        """

        return self._radius

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._latitude is not None:
            return False

        if self._longitude is not None:
            return False

        if self._altitude is not None:
            return False

        if self._radius is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Geolocation
        """

        return converter.json_to_class(Geolocation, json_str)


class AttachmentPublic(BunqModel):
    """
    :param _uuid: The uuid of the attachment.
    :type _uuid: str
    :param _description: The description of the attachment.
    :type _description: str
    :param _content_type: The content type of the attachment's file.
    :type _content_type: str
    """

    _uuid = None
    _description = None
    _content_type = None

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

    @property
    def description(self):
        """
        :rtype: str
        """

        return self._description

    @property
    def content_type(self):
        """
        :rtype: str
        """

        return self._content_type

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._uuid is not None:
            return False

        if self._description is not None:
            return False

        if self._content_type is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentPublic
        """

        return converter.json_to_class(AttachmentPublic, json_str)


class BunqMeMerchantAvailable(BunqModel):
    """
    :param _merchant_type: A merchant type supported by bunq.me.
    :type _merchant_type: str
    :param _available: Whether or not the merchant is available for the user.
    :type _available: bool
    """

    _merchant_type = None
    _available = None

    @property
    def merchant_type(self):
        """
        :rtype: str
        """

        return self._merchant_type

    @property
    def available(self):
        """
        :rtype: bool
        """

        return self._available

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._merchant_type is not None:
            return False

        if self._available is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BunqMeMerchantAvailable
        """

        return converter.json_to_class(BunqMeMerchantAvailable, json_str)


class BunqId(BunqModel):
    """
    :param _id_: An integer ID of an object. Unique per object type.
    :type _id_: int
    """

    _id_ = None
    _id__field_for_request = None

    def __init__(self, id_=None):
        """
        :param id_: An integer ID of an object. Unique per object type.
        :type id_: int
        """

        self._id__field_for_request = id_

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
        
        :rtype: BunqId
        """

        return converter.json_to_class(BunqId, json_str)


class CardBatchEntry(BunqModel):
    """
    :param _id_: The ID of the card that needs to be updated.
    :type _id_: int
    :param _status: The status to set for the card. Can be ACTIVE, DEACTIVATED,
    LOST, STOLEN or CANCELLED, and can only be set to LOST/STOLEN/CANCELLED when
    order status is
    ACCEPTED_FOR_PRODUCTION/DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED.
    Can only be set to DEACTIVATED after initial activation, i.e. order_status
    is
    DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED.
    Mind that all the possible choices (apart from ACTIVE and DEACTIVATED) are
    permanent and cannot be changed after.
    :type _status: str
    :param _card_limit: The spending limit for the card.
    :type _card_limit: Amount
    :param _card_limit_atm: The ATM spending limit for the card.
    :type _card_limit_atm: Amount
    :param _country_permission: The countries for which to grant (temporary)
    permissions to use the card.
    :type _country_permission: list[CardCountryPermission]
    :param _monetary_account_id_fallback: ID of the MA to be used as fallback
    for this card if insufficient balance. Fallback account is removed if not
    supplied.
    :type _monetary_account_id_fallback: int
    """

    _id__field_for_request = None
    _status_field_for_request = None
    _card_limit_field_for_request = None
    _card_limit_atm_field_for_request = None
    _country_permission_field_for_request = None
    _monetary_account_id_fallback_field_for_request = None

    def __init__(self, id_, status=None, card_limit=None, card_limit_atm=None, country_permission=None,
                 monetary_account_id_fallback=None):
        """
        :param id_: The ID of the card that needs to be updated.
        :type id_: int
        :param status: The status to set for the card. Can be ACTIVE, DEACTIVATED,
        LOST, STOLEN or CANCELLED, and can only be set to LOST/STOLEN/CANCELLED when
        order status is
        ACCEPTED_FOR_PRODUCTION/DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED.
        Can only be set to DEACTIVATED after initial activation, i.e. order_status
        is
        DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED.
        Mind that all the possible choices (apart from ACTIVE and DEACTIVATED) are
        permanent and cannot be changed after.
        :type status: str
        :param card_limit: The spending limit for the card.
        :type card_limit: Amount
        :param card_limit_atm: The ATM spending limit for the card.
        :type card_limit_atm: Amount
        :param country_permission: The countries for which to grant (temporary)
        permissions to use the card.
        :type country_permission: list[CardCountryPermission]
        :param monetary_account_id_fallback: ID of the MA to be used as fallback for
        this card if insufficient balance. Fallback account is removed if not
        supplied.
        :type monetary_account_id_fallback: int
        """

        self._id__field_for_request = id_
        self._status_field_for_request = status
        self._card_limit_field_for_request = card_limit
        self._card_limit_atm_field_for_request = card_limit_atm
        self._country_permission_field_for_request = country_permission
        self._monetary_account_id_fallback_field_for_request = monetary_account_id_fallback

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardBatchEntry
        """

        return converter.json_to_class(CardBatchEntry, json_str)


class CardCountryPermission(BunqModel):
    """
    :param _country: The country to allow transactions in (e.g. NL, DE).
    :type _country: str
    :param _expiry_time: Expiry time of this rule.
    :type _expiry_time: str
    :param _id_: The id of the card country permission entry.
    :type _id_: int
    """

    _id_ = None
    _country = None
    _expiry_time = None
    _country_field_for_request = None
    _expiry_time_field_for_request = None

    def __init__(self, country=None, expiry_time=None):
        """
        :param country: The country to allow transactions in (e.g. NL, DE).
        :type country: str
        :param expiry_time: Expiry time of this rule.
        :type expiry_time: str
        """

        self._country_field_for_request = country
        self._expiry_time_field_for_request = expiry_time

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def country(self):
        """
        :rtype: str
        """

        return self._country

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

        if self._country is not None:
            return False

        if self._expiry_time is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardCountryPermission
        """

        return converter.json_to_class(CardCountryPermission, json_str)


class CardPinAssignment(BunqModel):
    """
    :param _type_: PIN type. Can be PRIMARY, SECONDARY or TERTIARY
    :type _type_: str
    :param _pin_code: The 4 digit PIN to be assigned to this account.
    :type _pin_code: str
    :param _monetary_account_id: The ID of the monetary account to assign to
    this pin for the card.
    :type _monetary_account_id: int
    """

    _type_ = None
    _monetary_account_id = None
    _type__field_for_request = None
    _pin_code_field_for_request = None
    _monetary_account_id_field_for_request = None

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

        self._type__field_for_request = type_
        self._pin_code_field_for_request = pin_code
        self._monetary_account_id_field_for_request = monetary_account_id

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._type_ is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardPinAssignment
        """

        return converter.json_to_class(CardPinAssignment, json_str)


class CardPrimaryAccountNumber(BunqModel):
    """
    :param _id_: The ID for this Virtual PAN.
    :type _id_: int
    :param _description: The description for this PAN.
    :type _description: str
    :param _status: The status for this PAN, only for Online Cards.
    :type _status: str
    :param _monetary_account_id: The ID of the monetary account to assign to
    this PAN, only for Online Cards.
    :type _monetary_account_id: int
    :param _uuid: The UUID for this Virtual PAN.
    :type _uuid: str
    :param _four_digit: The last four digits of the PAN.
    :type _four_digit: str
    """

    _id_ = None
    _uuid = None
    _description = None
    _status = None
    _monetary_account_id = None
    _four_digit = None
    _id__field_for_request = None
    _description_field_for_request = None
    _status_field_for_request = None
    _monetary_account_id_field_for_request = None

    def __init__(self, id_=None, description=None, status=None, monetary_account_id=None):
        """
        :param id_: The ID for this PAN.
        :type id_: int
        :param description: The description for this PAN.
        :type description: str
        :param status: The status for this PAN, only for Online Cards.
        :type status: str
        :param monetary_account_id: The ID of the monetary account to assign to this
        PAN, only for Online Cards.
        :type monetary_account_id: int
        """

        self._id__field_for_request = id_
        self._description_field_for_request = description
        self._status_field_for_request = status
        self._monetary_account_id_field_for_request = monetary_account_id

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

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
    def monetary_account_id(self):
        """
        :rtype: int
        """

        return self._monetary_account_id

    @property
    def four_digit(self):
        """
        :rtype: str
        """

        return self._four_digit

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._uuid is not None:
            return False

        if self._description is not None:
            return False

        if self._status is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        if self._four_digit is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CardPrimaryAccountNumber
        """

        return converter.json_to_class(CardPrimaryAccountNumber, json_str)


class TabTextWaitingScreen(BunqModel):
    """
    :param _language: Language of tab text
    :type _language: str
    :param _description: Tab text
    :type _description: str
    """

    _language = None
    _description = None
    _language_field_for_request = None
    _description_field_for_request = None

    def __init__(self, language=None, description=None):
        """
        :param language: Language of tab text
        :type language: str
        :param description: Tab text
        :type description: str
        """

        self._language_field_for_request = language
        self._description_field_for_request = description

    @property
    def language(self):
        """
        :rtype: str
        """

        return self._language

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

        if self._language is not None:
            return False

        if self._description is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabTextWaitingScreen
        """

        return converter.json_to_class(TabTextWaitingScreen, json_str)


class TabVisibility(BunqModel):
    """
    :param _cash_register_qr_code: When true the tab will be linked to the
    ACTIVE cash registers QR code.
    :type _cash_register_qr_code: bool
    :param _tab_qr_code: When true the tab will be visible through its own QR
    code. Use ../tab/{tab-id}/qr-code-content to get the raw content of this QR
    code
    :type _tab_qr_code: bool
    :param _location: The location of the Tab in NearPay.
    :type _location: Geolocation
    """

    _cash_register_qr_code = None
    _tab_qr_code = None
    _location = None
    _cash_register_qr_code_field_for_request = None
    _tab_qr_code_field_for_request = None
    _location_field_for_request = None

    def __init__(self, cash_register_qr_code=None, tab_qr_code=None, location=None):
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

        self._cash_register_qr_code_field_for_request = cash_register_qr_code
        self._tab_qr_code_field_for_request = tab_qr_code
        self._location_field_for_request = location

    @property
    def cash_register_qr_code(self):
        """
        :rtype: bool
        """

        return self._cash_register_qr_code

    @property
    def tab_qr_code(self):
        """
        :rtype: bool
        """

        return self._tab_qr_code

    @property
    def location(self):
        """
        :rtype: Geolocation
        """

        return self._location

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._cash_register_qr_code is not None:
            return False

        if self._tab_qr_code is not None:
            return False

        if self._location is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TabVisibility
        """

        return converter.json_to_class(TabVisibility, json_str)


class AttachmentTab(BunqModel):
    """
    :param _id_: The id of the attachment.
    :type _id_: int
    :param _description: The description of the attachment.
    :type _description: str
    :param _content_type: The content type of the attachment's file.
    :type _content_type: str
    """

    _id_ = None
    _description = None
    _content_type = None

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
    def content_type(self):
        """
        :rtype: str
        """

        return self._content_type

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._description is not None:
            return False

        if self._content_type is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AttachmentTab
        """

        return converter.json_to_class(AttachmentTab, json_str)


class Certificate(BunqModel):
    """
    :param _certificate: A single certificate in the chain in .PEM format.
    :type _certificate: str
    """

    _certificate = None
    _certificate_field_for_request = None

    def __init__(self, certificate):
        """
        :param certificate: A single certificate in the chain in .PEM format.
        :type certificate: str
        """

        self._certificate_field_for_request = certificate

    @property
    def certificate(self):
        """
        :rtype: str
        """

        return self._certificate

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._certificate is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Certificate
        """

        return converter.json_to_class(Certificate, json_str)


class Ubo(BunqModel):
    """
    :param _name: The name of the ultimate beneficiary owner.
    :type _name: str
    :param _date_of_birth: The date of birth of the ultimate beneficiary owner.
    :type _date_of_birth: str
    :param _nationality: The nationality of the ultimate beneficiary owner.
    :type _nationality: str
    """

    _name = None
    _date_of_birth = None
    _nationality = None
    _name_field_for_request = None
    _date_of_birth_field_for_request = None
    _nationality_field_for_request = None

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

        self._name_field_for_request = name
        self._date_of_birth_field_for_request = date_of_birth
        self._nationality_field_for_request = nationality

    @property
    def name(self):
        """
        :rtype: str
        """

        return self._name

    @property
    def date_of_birth(self):
        """
        :rtype: str
        """

        return self._date_of_birth

    @property
    def nationality(self):
        """
        :rtype: str
        """

        return self._nationality

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._name is not None:
            return False

        if self._date_of_birth is not None:
            return False

        if self._nationality is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Ubo
        """

        return converter.json_to_class(Ubo, json_str)


class NotificationFilter(BunqModel):
    """
    :param _notification_delivery_method: The delivery method via which
    notifications that match this notification filter will be delivered.
    Possible choices are PUSH for delivery via push notification and URL for
    delivery via URL callback.
    :type _notification_delivery_method: str
    :param _notification_target: The target of notifications that match this
    notification filter. For URL notification filters this is the URL to which
    the callback will be made. For PUSH notifications filters this should always
    be null.
    :type _notification_target: str
    :param _category: The notification category that will match this
    notification filter. Possible choices are BILLING, CARD_TRANSACTION_FAILED,
    CARD_TRANSACTION_SUCCESSFUL, CHAT, DRAFT_PAYMENT, IDEAL, SOFORT,
    MONETARY_ACCOUNT_PROFILE, MUTATION, PAYMENT, PROMOTION, REQUEST,
    SCHEDULE_RESULT, SCHEDULE_STATUS, SHARE, SUPPORT, TAB_RESULT, USER_APPROVAL.
    :type _category: str
    """

    _notification_delivery_method = None
    _notification_target = None
    _category = None
    _notification_delivery_method_field_for_request = None
    _notification_target_field_for_request = None
    _category_field_for_request = None

    def __init__(self, notification_delivery_method=None, notification_target=None, category=None):
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

        self._notification_delivery_method_field_for_request = notification_delivery_method
        self._notification_target_field_for_request = notification_target
        self._category_field_for_request = category

    @property
    def notification_delivery_method(self):
        """
        :rtype: str
        """

        return self._notification_delivery_method

    @property
    def notification_target(self):
        """
        :rtype: str
        """

        return self._notification_target

    @property
    def category(self):
        """
        :rtype: str
        """

        return self._category

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._notification_delivery_method is not None:
            return False

        if self._notification_target is not None:
            return False

        if self._category is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: NotificationFilter
        """

        return converter.json_to_class(NotificationFilter, json_str)


class DraftPaymentResponse(BunqModel):
    """
    :param _status: The status with which was responded.
    :type _status: str
    :param _user_alias_created: The user that responded to the DraftPayment.
    :type _user_alias_created: LabelUser
    """

    _status = None
    _user_alias_created = None

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def user_alias_created(self):
        """
        :rtype: LabelUser
        """

        return self._user_alias_created

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._status is not None:
            return False

        if self._user_alias_created is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftPaymentResponse
        """

        return converter.json_to_class(DraftPaymentResponse, json_str)


class DraftPaymentEntry(BunqModel):
    """
    :param _amount: The amount of the payment.
    :type _amount: Amount
    :param _counterparty_alias: The LabelMonetaryAccount containing the public
    information of the other (counterparty) side of the DraftPayment.
    :type _counterparty_alias: MonetaryAccountReference
    :param _description: The description for the DraftPayment. Maximum 140
    characters for DraftPayments to external IBANs, 9000 characters for
    DraftPayments to only other bunq MonetaryAccounts.
    :type _description: str
    :param _merchant_reference: Optional data to be included with the Payment
    specific to the merchant.
    :type _merchant_reference: str
    :param _attachment: The Attachments attached to the DraftPayment.
    :type _attachment: list[AttachmentMonetaryAccountPayment]
    :param _id_: The id of the draft payment entry.
    :type _id_: int
    :param _alias: The LabelMonetaryAccount containing the public information of
    'this' (party) side of the DraftPayment.
    :type _alias: MonetaryAccountReference
    :param _type_: The type of the draft payment entry.
    :type _type_: str
    """

    _id_ = None
    _amount = None
    _alias = None
    _counterparty_alias = None
    _description = None
    _merchant_reference = None
    _type_ = None
    _attachment = None
    _amount_field_for_request = None
    _counterparty_alias_field_for_request = None
    _description_field_for_request = None
    _merchant_reference_field_for_request = None
    _attachment_field_for_request = None

    def __init__(self, amount=None, counterparty_alias=None, description=None, merchant_reference=None,
                 attachment=None):
        """
        :param amount: The amount of the payment.
        :type amount: Amount
        :param counterparty_alias: The Alias of the party we are transferring the
        money to. Can be an Alias of type EMAIL or PHONE_NUMBER (for bunq
        MonetaryAccounts or bunq.to payments) or IBAN (for external bank account).
        :type counterparty_alias: Pointer
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

        self._amount_field_for_request = amount
        self._counterparty_alias_field_for_request = counterparty_alias
        self._description_field_for_request = description
        self._merchant_reference_field_for_request = merchant_reference
        self._attachment_field_for_request = attachment

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def amount(self):
        """
        :rtype: Amount
        """

        return self._amount

    @property
    def alias(self):
        """
        :rtype: MonetaryAccountReference
        """

        return self._alias

    @property
    def counterparty_alias(self):
        """
        :rtype: MonetaryAccountReference
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
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def attachment(self):
        """
        :rtype: list[AttachmentMonetaryAccountPayment]
        """

        return self._attachment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._amount is not None:
            return False

        if self._alias is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._description is not None:
            return False

        if self._merchant_reference is not None:
            return False

        if self._type_ is not None:
            return False

        if self._attachment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftPaymentEntry
        """

        return converter.json_to_class(DraftPaymentEntry, json_str)


class DraftPaymentAnchorObject(BunqModel, AnchorObjectInterface):
    """
    :param _Payment: 
    :type _Payment: endpoint.Payment
    :param _PaymentBatch: 
    :type _PaymentBatch: endpoint.PaymentBatch
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    _Payment = None
    _PaymentBatch = None

    @property
    def Payment(self):
        """
        :rtype: endpoint.Payment
        """

        return self._Payment

    @property
    def PaymentBatch(self):
        """
        :rtype: endpoint.PaymentBatch
        """

        return self._PaymentBatch

    def get_referenced_object(self):
        """
        :rtype: BunqModel
        :raise: BunqException
        """

        if self._Payment is not None:
            return self._Payment

        if self._PaymentBatch is not None:
            return self._PaymentBatch

        raise BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._Payment is not None:
            return False

        if self._PaymentBatch is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftPaymentAnchorObject
        """

        return converter.json_to_class(DraftPaymentAnchorObject, json_str)


class PaymentBatchAnchoredPayment(BunqModel):
    """
    :param _Payment: 
    :type _Payment: list[endpoint.Payment]
    """

    _Payment = None

    @property
    def Payment(self):
        """
        :rtype: list[endpoint.Payment]
        """

        return self._Payment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._Payment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: PaymentBatchAnchoredPayment
        """

        return converter.json_to_class(PaymentBatchAnchoredPayment, json_str)


class ScheduleAnchorObject(BunqModel, AnchorObjectInterface):
    """
    :param _Payment: 
    :type _Payment: endpoint.Payment
    :param _PaymentBatch: 
    :type _PaymentBatch: endpoint.PaymentBatch
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    _Payment = None
    _PaymentBatch = None

    @property
    def Payment(self):
        """
        :rtype: endpoint.Payment
        """

        return self._Payment

    @property
    def PaymentBatch(self):
        """
        :rtype: endpoint.PaymentBatch
        """

        return self._PaymentBatch

    def get_referenced_object(self):
        """
        :rtype: BunqModel
        :raise: BunqException
        """

        if self._Payment is not None:
            return self._Payment

        if self._PaymentBatch is not None:
            return self._PaymentBatch

        raise BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._Payment is not None:
            return False

        if self._PaymentBatch is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ScheduleAnchorObject
        """

        return converter.json_to_class(ScheduleAnchorObject, json_str)


class DraftShareInviteEntry(BunqModel):
    """
    :param _share_detail: The share details. Only one of these objects is
    returned.
    :type _share_detail: ShareDetail
    :param _start_date: The start date of this share.
    :type _start_date: str
    :param _end_date: The expiration date of this share.
    :type _end_date: str
    """

    _share_detail = None
    _start_date = None
    _end_date = None
    _share_detail_field_for_request = None
    _start_date_field_for_request = None
    _end_date_field_for_request = None

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

        self._share_detail_field_for_request = share_detail
        self._start_date_field_for_request = start_date
        self._end_date_field_for_request = end_date

    @property
    def share_detail(self):
        """
        :rtype: ShareDetail
        """

        return self._share_detail

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

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._share_detail is not None:
            return False

        if self._start_date is not None:
            return False

        if self._end_date is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: DraftShareInviteEntry
        """

        return converter.json_to_class(DraftShareInviteEntry, json_str)


class ShareDetail(BunqModel):
    """
    :param _payment: The share details for a payment share. In the response
    'payment' is replaced by 'ShareDetailPayment'.
    :type _payment: ShareDetailPayment
    :param _read_only: The share details for viewing a share. In the response
    'read_only' is replaced by 'ShareDetailReadOnly'.
    :type _read_only: ShareDetailReadOnly
    :param _draft_payment: The share details for a draft payment share. In the
    response 'draft_payment' is replaced by 'ShareDetailDraftPayment'.
    :type _draft_payment: ShareDetailDraftPayment
    """

    _payment = None
    _read_only = None
    _draft_payment = None
    _payment_field_for_request = None
    _read_only_field_for_request = None
    _draft_payment_field_for_request = None

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

        self._payment_field_for_request = payment
        self._read_only_field_for_request = read_only
        self._draft_payment_field_for_request = draft_payment

    @property
    def payment(self):
        """
        :rtype: ShareDetailPayment
        """

        return self._payment

    @property
    def read_only(self):
        """
        :rtype: ShareDetailReadOnly
        """

        return self._read_only

    @property
    def draft_payment(self):
        """
        :rtype: ShareDetailDraftPayment
        """

        return self._draft_payment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._payment is not None:
            return False

        if self._read_only is not None:
            return False

        if self._draft_payment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareDetail
        """

        return converter.json_to_class(ShareDetail, json_str)


class ShareDetailPayment(BunqModel):
    """
    :param _make_payments: If set to true, the invited user will be able to make
    payments from the shared account.
    :type _make_payments: bool
    :param _make_draft_payments: If set to true, the invited user will be able
    to make draft payments from the shared account.
    :type _make_draft_payments: bool
    :param _view_balance: If set to true, the invited user will be able to view
    the account balance.
    :type _view_balance: bool
    :param _view_old_events: If set to true, the invited user will be able to
    view events from before the share was active.
    :type _view_old_events: bool
    :param _view_new_events: If set to true, the invited user will be able to
    view events starting from the time the share became active.
    :type _view_new_events: bool
    :param _budget: The budget restriction.
    :type _budget: BudgetRestriction
    """

    _make_payments = None
    _make_draft_payments = None
    _view_balance = None
    _view_old_events = None
    _view_new_events = None
    _budget = None
    _make_payments_field_for_request = None
    _make_draft_payments_field_for_request = None
    _view_balance_field_for_request = None
    _view_old_events_field_for_request = None
    _view_new_events_field_for_request = None
    _budget_field_for_request = None

    def __init__(self, make_payments=None, view_balance=None, view_old_events=None, view_new_events=None,
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

        self._make_payments_field_for_request = make_payments
        self._view_balance_field_for_request = view_balance
        self._view_old_events_field_for_request = view_old_events
        self._view_new_events_field_for_request = view_new_events
        self._make_draft_payments_field_for_request = make_draft_payments
        self._budget_field_for_request = budget

    @property
    def make_payments(self):
        """
        :rtype: bool
        """

        return self._make_payments

    @property
    def make_draft_payments(self):
        """
        :rtype: bool
        """

        return self._make_draft_payments

    @property
    def view_balance(self):
        """
        :rtype: bool
        """

        return self._view_balance

    @property
    def view_old_events(self):
        """
        :rtype: bool
        """

        return self._view_old_events

    @property
    def view_new_events(self):
        """
        :rtype: bool
        """

        return self._view_new_events

    @property
    def budget(self):
        """
        :rtype: BudgetRestriction
        """

        return self._budget

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._make_payments is not None:
            return False

        if self._make_draft_payments is not None:
            return False

        if self._view_balance is not None:
            return False

        if self._view_old_events is not None:
            return False

        if self._view_new_events is not None:
            return False

        if self._budget is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareDetailPayment
        """

        return converter.json_to_class(ShareDetailPayment, json_str)


class BudgetRestriction(BunqModel):
    """
    :param _amount: The amount of the budget given to the invited user.
    :type _amount: Amount
    :param _frequency: The duration for a budget restriction. Valid values are
    DAILY, WEEKLY, MONTHLY, YEARLY.
    :type _frequency: str
    """

    _amount = None
    _frequency = None
    _amount_field_for_request = None
    _frequency_field_for_request = None

    def __init__(self, amount=None, frequency=None):
        """
        :param amount: The amount of the budget given to the invited user.
        :type amount: Amount
        :param frequency: The duration for a budget restriction. Valid values are
        DAILY, WEEKLY, MONTHLY, YEARLY.
        :type frequency: str
        """

        self._amount_field_for_request = amount
        self._frequency_field_for_request = frequency

    @property
    def amount(self):
        """
        :rtype: Amount
        """

        return self._amount

    @property
    def frequency(self):
        """
        :rtype: str
        """

        return self._frequency

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._amount is not None:
            return False

        if self._frequency is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: BudgetRestriction
        """

        return converter.json_to_class(BudgetRestriction, json_str)


class ShareDetailReadOnly(BunqModel):
    """
    :param _view_balance: If set to true, the invited user will be able to view
    the account balance.
    :type _view_balance: bool
    :param _view_old_events: If set to true, the invited user will be able to
    view events from before the share was active.
    :type _view_old_events: bool
    :param _view_new_events: If set to true, the invited user will be able to
    view events starting from the time the share became active.
    :type _view_new_events: bool
    """

    _view_balance = None
    _view_old_events = None
    _view_new_events = None
    _view_balance_field_for_request = None
    _view_old_events_field_for_request = None
    _view_new_events_field_for_request = None

    def __init__(self, view_balance=None, view_old_events=None, view_new_events=None):
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

        self._view_balance_field_for_request = view_balance
        self._view_old_events_field_for_request = view_old_events
        self._view_new_events_field_for_request = view_new_events

    @property
    def view_balance(self):
        """
        :rtype: bool
        """

        return self._view_balance

    @property
    def view_old_events(self):
        """
        :rtype: bool
        """

        return self._view_old_events

    @property
    def view_new_events(self):
        """
        :rtype: bool
        """

        return self._view_new_events

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._view_balance is not None:
            return False

        if self._view_old_events is not None:
            return False

        if self._view_new_events is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareDetailReadOnly
        """

        return converter.json_to_class(ShareDetailReadOnly, json_str)


class ShareDetailDraftPayment(BunqModel):
    """
    :param _make_draft_payments: If set to true, the invited user will be able
    to make draft payments from the shared account.
    :type _make_draft_payments: bool
    :param _view_balance: If set to true, the invited user will be able to view
    the account balance.
    :type _view_balance: bool
    :param _view_old_events: If set to true, the invited user will be able to
    view events from before the share was active.
    :type _view_old_events: bool
    :param _view_new_events: If set to true, the invited user will be able to
    view events starting from the time the share became active.
    :type _view_new_events: bool
    """

    _make_draft_payments = None
    _view_balance = None
    _view_old_events = None
    _view_new_events = None
    _make_draft_payments_field_for_request = None
    _view_balance_field_for_request = None
    _view_old_events_field_for_request = None
    _view_new_events_field_for_request = None

    def __init__(self, make_draft_payments=None, view_balance=None, view_old_events=None, view_new_events=None):
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

        self._make_draft_payments_field_for_request = make_draft_payments
        self._view_balance_field_for_request = view_balance
        self._view_old_events_field_for_request = view_old_events
        self._view_new_events_field_for_request = view_new_events

    @property
    def make_draft_payments(self):
        """
        :rtype: bool
        """

        return self._make_draft_payments

    @property
    def view_balance(self):
        """
        :rtype: bool
        """

        return self._view_balance

    @property
    def view_old_events(self):
        """
        :rtype: bool
        """

        return self._view_old_events

    @property
    def view_new_events(self):
        """
        :rtype: bool
        """

        return self._view_new_events

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._make_draft_payments is not None:
            return False

        if self._view_balance is not None:
            return False

        if self._view_old_events is not None:
            return False

        if self._view_new_events is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ShareDetailDraftPayment
        """

        return converter.json_to_class(ShareDetailDraftPayment, json_str)


class EventObject(BunqModel, AnchorObjectInterface):
    """
    :param _BunqMeTab: 
    :type _BunqMeTab: endpoint.BunqMeTab
    :param _BunqMeTabResultResponse: 
    :type _BunqMeTabResultResponse: endpoint.BunqMeTabResultResponse
    :param _BunqMeFundraiserResult: 
    :type _BunqMeFundraiserResult: endpoint.BunqMeFundraiserResult
    :param _Card: 
    :type _Card: endpoint.Card
    :param _CardDebit: 
    :type _CardDebit: endpoint.CardDebit
    :param _DraftPayment: 
    :type _DraftPayment: endpoint.DraftPayment
    :param _FeatureAnnouncement: 
    :type _FeatureAnnouncement: endpoint.FeatureAnnouncement
    :param _IdealMerchantTransaction: 
    :type _IdealMerchantTransaction: endpoint.IdealMerchantTransaction
    :param _Invoice: 
    :type _Invoice: endpoint.Invoice
    :param _ScheduledPayment: 
    :type _ScheduledPayment: endpoint.SchedulePayment
    :param _ScheduledPaymentBatch: 
    :type _ScheduledPaymentBatch: endpoint.SchedulePaymentBatch
    :param _ScheduledInstance: 
    :type _ScheduledInstance: endpoint.ScheduleInstance
    :param _MasterCardAction: 
    :type _MasterCardAction: endpoint.MasterCardAction
    :param _BankSwitchServiceNetherlandsIncomingPayment: 
    :type _BankSwitchServiceNetherlandsIncomingPayment:
    endpoint.BankSwitchServiceNetherlandsIncomingPayment
    :param _Payment: 
    :type _Payment: endpoint.Payment
    :param _PaymentBatch: 
    :type _PaymentBatch: endpoint.PaymentBatch
    :param _RequestInquiryBatch: 
    :type _RequestInquiryBatch: endpoint.RequestInquiryBatch
    :param _RequestInquiry: 
    :type _RequestInquiry: endpoint.RequestInquiry
    :param _RequestResponse: 
    :type _RequestResponse: endpoint.RequestResponse
    :param _RewardRecipient: 
    :type _RewardRecipient: endpoint.RewardRecipient
    :param _RewardSender: 
    :type _RewardSender: endpoint.RewardSender
    :param _ShareInviteBankInquiryBatch: 
    :type _ShareInviteBankInquiryBatch: endpoint.ShareInviteBankInquiryBatch
    :param _ShareInviteBankInquiry: 
    :type _ShareInviteBankInquiry: endpoint.ShareInviteMonetaryAccountInquiry
    :param _ShareInviteBankResponse: 
    :type _ShareInviteBankResponse: endpoint.ShareInviteMonetaryAccountResponse
    :param _SofortMerchantTransaction: 
    :type _SofortMerchantTransaction: endpoint.SofortMerchantTransaction
    :param _TabResultInquiry: 
    :type _TabResultInquiry: endpoint.TabResultInquiry
    :param _TabResultResponse: 
    :type _TabResultResponse: endpoint.TabResultResponse
    :param _TransferwisePayment: 
    :type _TransferwisePayment: endpoint.TransferwiseTransfer
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    _BunqMeTab = None
    _BunqMeTabResultResponse = None
    _BunqMeFundraiserResult = None
    _Card = None
    _CardDebit = None
    _DraftPayment = None
    _FeatureAnnouncement = None
    _IdealMerchantTransaction = None
    _Invoice = None
    _ScheduledPayment = None
    _ScheduledPaymentBatch = None
    _ScheduledInstance = None
    _MasterCardAction = None
    _BankSwitchServiceNetherlandsIncomingPayment = None
    _Payment = None
    _PaymentBatch = None
    _RequestInquiryBatch = None
    _RequestInquiry = None
    _RequestResponse = None
    _RewardRecipient = None
    _RewardSender = None
    _ShareInviteBankInquiryBatch = None
    _ShareInviteBankInquiry = None
    _ShareInviteBankResponse = None
    _SofortMerchantTransaction = None
    _TabResultInquiry = None
    _TabResultResponse = None
    _TransferwisePayment = None

    @property
    def BunqMeTab(self):
        """
        :rtype: endpoint.BunqMeTab
        """

        return self._BunqMeTab

    @property
    def BunqMeTabResultResponse(self):
        """
        :rtype: endpoint.BunqMeTabResultResponse
        """

        return self._BunqMeTabResultResponse

    @property
    def BunqMeFundraiserResult(self):
        """
        :rtype: endpoint.BunqMeFundraiserResult
        """

        return self._BunqMeFundraiserResult

    @property
    def Card(self):
        """
        :rtype: endpoint.Card
        """

        return self._Card

    @property
    def CardDebit(self):
        """
        :rtype: endpoint.CardDebit
        """

        return self._CardDebit

    @property
    def DraftPayment(self):
        """
        :rtype: endpoint.DraftPayment
        """

        return self._DraftPayment

    @property
    def FeatureAnnouncement(self):
        """
        :rtype: endpoint.FeatureAnnouncement
        """

        return self._FeatureAnnouncement

    @property
    def IdealMerchantTransaction(self):
        """
        :rtype: endpoint.IdealMerchantTransaction
        """

        return self._IdealMerchantTransaction

    @property
    def Invoice(self):
        """
        :rtype: endpoint.Invoice
        """

        return self._Invoice

    @property
    def ScheduledPayment(self):
        """
        :rtype: endpoint.SchedulePayment
        """

        return self._ScheduledPayment

    @property
    def ScheduledPaymentBatch(self):
        """
        :rtype: endpoint.SchedulePaymentBatch
        """

        return self._ScheduledPaymentBatch

    @property
    def ScheduledInstance(self):
        """
        :rtype: endpoint.ScheduleInstance
        """

        return self._ScheduledInstance

    @property
    def MasterCardAction(self):
        """
        :rtype: endpoint.MasterCardAction
        """

        return self._MasterCardAction

    @property
    def BankSwitchServiceNetherlandsIncomingPayment(self):
        """
        :rtype: endpoint.BankSwitchServiceNetherlandsIncomingPayment
        """

        return self._BankSwitchServiceNetherlandsIncomingPayment

    @property
    def Payment(self):
        """
        :rtype: endpoint.Payment
        """

        return self._Payment

    @property
    def PaymentBatch(self):
        """
        :rtype: endpoint.PaymentBatch
        """

        return self._PaymentBatch

    @property
    def RequestInquiryBatch(self):
        """
        :rtype: endpoint.RequestInquiryBatch
        """

        return self._RequestInquiryBatch

    @property
    def RequestInquiry(self):
        """
        :rtype: endpoint.RequestInquiry
        """

        return self._RequestInquiry

    @property
    def RequestResponse(self):
        """
        :rtype: endpoint.RequestResponse
        """

        return self._RequestResponse

    @property
    def RewardRecipient(self):
        """
        :rtype: endpoint.RewardRecipient
        """

        return self._RewardRecipient

    @property
    def RewardSender(self):
        """
        :rtype: endpoint.RewardSender
        """

        return self._RewardSender

    @property
    def ShareInviteBankInquiryBatch(self):
        """
        :rtype: endpoint.ShareInviteBankInquiryBatch
        """

        return self._ShareInviteBankInquiryBatch

    @property
    def ShareInviteBankInquiry(self):
        """
        :rtype: endpoint.ShareInviteMonetaryAccountInquiry
        """

        return self._ShareInviteBankInquiry

    @property
    def ShareInviteBankResponse(self):
        """
        :rtype: endpoint.ShareInviteMonetaryAccountResponse
        """

        return self._ShareInviteBankResponse

    @property
    def SofortMerchantTransaction(self):
        """
        :rtype: endpoint.SofortMerchantTransaction
        """

        return self._SofortMerchantTransaction

    @property
    def TabResultInquiry(self):
        """
        :rtype: endpoint.TabResultInquiry
        """

        return self._TabResultInquiry

    @property
    def TabResultResponse(self):
        """
        :rtype: endpoint.TabResultResponse
        """

        return self._TabResultResponse

    @property
    def TransferwisePayment(self):
        """
        :rtype: endpoint.TransferwiseTransfer
        """

        return self._TransferwisePayment

    def get_referenced_object(self):
        """
        :rtype: BunqModel
        :raise: BunqException
        """

        if self._BunqMeTab is not None:
            return self._BunqMeTab

        if self._BunqMeTabResultResponse is not None:
            return self._BunqMeTabResultResponse

        if self._BunqMeFundraiserResult is not None:
            return self._BunqMeFundraiserResult

        if self._Card is not None:
            return self._Card

        if self._CardDebit is not None:
            return self._CardDebit

        if self._DraftPayment is not None:
            return self._DraftPayment

        if self._FeatureAnnouncement is not None:
            return self._FeatureAnnouncement

        if self._IdealMerchantTransaction is not None:
            return self._IdealMerchantTransaction

        if self._Invoice is not None:
            return self._Invoice

        if self._ScheduledPayment is not None:
            return self._ScheduledPayment

        if self._ScheduledPaymentBatch is not None:
            return self._ScheduledPaymentBatch

        if self._ScheduledInstance is not None:
            return self._ScheduledInstance

        if self._MasterCardAction is not None:
            return self._MasterCardAction

        if self._BankSwitchServiceNetherlandsIncomingPayment is not None:
            return self._BankSwitchServiceNetherlandsIncomingPayment

        if self._Payment is not None:
            return self._Payment

        if self._PaymentBatch is not None:
            return self._PaymentBatch

        if self._RequestInquiryBatch is not None:
            return self._RequestInquiryBatch

        if self._RequestInquiry is not None:
            return self._RequestInquiry

        if self._RequestResponse is not None:
            return self._RequestResponse

        if self._RewardRecipient is not None:
            return self._RewardRecipient

        if self._RewardSender is not None:
            return self._RewardSender

        if self._ShareInviteBankInquiryBatch is not None:
            return self._ShareInviteBankInquiryBatch

        if self._ShareInviteBankInquiry is not None:
            return self._ShareInviteBankInquiry

        if self._ShareInviteBankResponse is not None:
            return self._ShareInviteBankResponse

        if self._SofortMerchantTransaction is not None:
            return self._SofortMerchantTransaction

        if self._TabResultInquiry is not None:
            return self._TabResultInquiry

        if self._TabResultResponse is not None:
            return self._TabResultResponse

        if self._TransferwisePayment is not None:
            return self._TransferwisePayment

        raise BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._BunqMeTab is not None:
            return False

        if self._BunqMeTabResultResponse is not None:
            return False

        if self._BunqMeFundraiserResult is not None:
            return False

        if self._Card is not None:
            return False

        if self._CardDebit is not None:
            return False

        if self._DraftPayment is not None:
            return False

        if self._FeatureAnnouncement is not None:
            return False

        if self._IdealMerchantTransaction is not None:
            return False

        if self._Invoice is not None:
            return False

        if self._ScheduledPayment is not None:
            return False

        if self._ScheduledPaymentBatch is not None:
            return False

        if self._ScheduledInstance is not None:
            return False

        if self._MasterCardAction is not None:
            return False

        if self._BankSwitchServiceNetherlandsIncomingPayment is not None:
            return False

        if self._Payment is not None:
            return False

        if self._PaymentBatch is not None:
            return False

        if self._RequestInquiryBatch is not None:
            return False

        if self._RequestInquiry is not None:
            return False

        if self._RequestResponse is not None:
            return False

        if self._RewardRecipient is not None:
            return False

        if self._RewardSender is not None:
            return False

        if self._ShareInviteBankInquiryBatch is not None:
            return False

        if self._ShareInviteBankInquiry is not None:
            return False

        if self._ShareInviteBankResponse is not None:
            return False

        if self._SofortMerchantTransaction is not None:
            return False

        if self._TabResultInquiry is not None:
            return False

        if self._TabResultResponse is not None:
            return False

        if self._TransferwisePayment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: EventObject
        """

        return converter.json_to_class(EventObject, json_str)


class SchedulePaymentEntry(BunqModel):
    """
    :param _amount: The Amount transferred by the Payment. Will be negative for
    outgoing Payments and positive for incoming Payments (relative to the
    MonetaryAccount indicated by monetary_account_id).
    :type _amount: Amount
    :param _counterparty_alias: The LabelMonetaryAccount containing the public
    information of the other (counterparty) side of the Payment.
    :type _counterparty_alias: MonetaryAccountReference
    :param _description: The description for the Payment. Maximum 140 characters
    for Payments to external IBANs, 9000 characters for Payments to only other
    bunq MonetaryAccounts.
    :type _description: str
    :param _attachment: The Attachments attached to the Payment.
    :type _attachment: list[AttachmentMonetaryAccountPayment]
    :param _merchant_reference: Optional data included with the Payment specific
    to the merchant.
    :type _merchant_reference: str
    :param _allow_bunqto: Whether or not sending a bunq.to payment is allowed.
    :type _allow_bunqto: bool
    :param _alias: The LabelMonetaryAccount containing the public information of
    'this' (party) side of the Payment.
    :type _alias: MonetaryAccountReference
    """

    _amount = None
    _alias = None
    _counterparty_alias = None
    _description = None
    _attachment = None
    _merchant_reference = None
    _amount_field_for_request = None
    _counterparty_alias_field_for_request = None
    _description_field_for_request = None
    _attachment_field_for_request = None
    _merchant_reference_field_for_request = None
    _allow_bunqto_field_for_request = None

    def __init__(self, amount=None, counterparty_alias=None, description=None, attachment=None, merchant_reference=None,
                 allow_bunqto=None):
        """
        :param amount: The Amount to transfer with the Payment. Must be bigger 0 and
        smaller than the MonetaryAccount's balance.
        :type amount: Amount
        :param counterparty_alias: The Alias of the party we are transferring the
        money to. Can be an Alias of type EMAIL or PHONE (for bunq MonetaryAccounts)
        or IBAN (for external bank account).
        :type counterparty_alias: Pointer
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
        :type allow_bunqto: bool
        """

        self._amount_field_for_request = amount
        self._counterparty_alias_field_for_request = counterparty_alias
        self._description_field_for_request = description
        self._attachment_field_for_request = attachment
        self._merchant_reference_field_for_request = merchant_reference
        self._allow_bunqto_field_for_request = allow_bunqto

    @property
    def amount(self):
        """
        :rtype: Amount
        """

        return self._amount

    @property
    def alias(self):
        """
        :rtype: MonetaryAccountReference
        """

        return self._alias

    @property
    def counterparty_alias(self):
        """
        :rtype: MonetaryAccountReference
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
        :rtype: list[AttachmentMonetaryAccountPayment]
        """

        return self._attachment

    @property
    def merchant_reference(self):
        """
        :rtype: str
        """

        return self._merchant_reference

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._amount is not None:
            return False

        if self._alias is not None:
            return False

        if self._counterparty_alias is not None:
            return False

        if self._description is not None:
            return False

        if self._attachment is not None:
            return False

        if self._merchant_reference is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: SchedulePaymentEntry
        """

        return converter.json_to_class(SchedulePaymentEntry, json_str)


class Error(BunqModel):
    """
    :param _error_description: The error description (in English).
    :type _error_description: str
    :param _error_description_translated: The error description (in the user
    language).
    :type _error_description_translated: str
    """

    _error_description = None
    _error_description_translated = None

    @property
    def error_description(self):
        """
        :rtype: str
        """

        return self._error_description

    @property
    def error_description_translated(self):
        """
        :rtype: str
        """

        return self._error_description_translated

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._error_description is not None:
            return False

        if self._error_description_translated is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Error
        """

        return converter.json_to_class(Error, json_str)


class ScheduleInstanceAnchorObject(BunqModel, AnchorObjectInterface):
    """
    :param _Payment: 
    :type _Payment: endpoint.Payment
    :param _PaymentBatch: 
    :type _PaymentBatch: endpoint.PaymentBatch
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    _Payment = None
    _PaymentBatch = None

    @property
    def Payment(self):
        """
        :rtype: endpoint.Payment
        """

        return self._Payment

    @property
    def PaymentBatch(self):
        """
        :rtype: endpoint.PaymentBatch
        """

        return self._PaymentBatch

    def get_referenced_object(self):
        """
        :rtype: BunqModel
        :raise: BunqException
        """

        if self._Payment is not None:
            return self._Payment

        if self._PaymentBatch is not None:
            return self._PaymentBatch

        raise BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._Payment is not None:
            return False

        if self._PaymentBatch is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: ScheduleInstanceAnchorObject
        """

        return converter.json_to_class(ScheduleInstanceAnchorObject, json_str)


class LabelCard(BunqModel):
    """
    :param _uuid: The public UUID.
    :type _uuid: str
    :param _type_: The type of the card.
    :type _type_: str
    :param _second_line: The second line on the card.
    :type _second_line: str
    :param _expiry_date: The date this card will expire.
    :type _expiry_date: str
    :param _status: The status of the card.
    :type _status: str
    :param _label_user: The owner of this card.
    :type _label_user: LabelUser
    """

    _uuid = None
    _type_ = None
    _second_line = None
    _expiry_date = None
    _status = None
    _label_user = None

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

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
    def expiry_date(self):
        """
        :rtype: str
        """

        return self._expiry_date

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def label_user(self):
        """
        :rtype: LabelUser
        """

        return self._label_user

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._uuid is not None:
            return False

        if self._type_ is not None:
            return False

        if self._second_line is not None:
            return False

        if self._expiry_date is not None:
            return False

        if self._status is not None:
            return False

        if self._label_user is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: LabelCard
        """

        return converter.json_to_class(LabelCard, json_str)


class RequestReferenceSplitTheBillAnchorObject(BunqModel, AnchorObjectInterface):
    """
    :param _BillingInvoice: 
    :type _BillingInvoice: endpoint.Invoice
    :param _DraftPayment: 
    :type _DraftPayment: endpoint.DraftPayment
    :param _MasterCardAction: 
    :type _MasterCardAction: endpoint.MasterCardAction
    :param _Payment: 
    :type _Payment: endpoint.Payment
    :param _PaymentBatch: 
    :type _PaymentBatch: endpoint.PaymentBatch
    :param _RequestResponse: 
    :type _RequestResponse: endpoint.RequestResponse
    :param _ScheduleInstance: 
    :type _ScheduleInstance: endpoint.ScheduleInstance
    :param _TabResultResponse: 
    :type _TabResultResponse: endpoint.TabResultResponse
    :param _WhitelistResult: 
    :type _WhitelistResult: endpoint.WhitelistResult
    :param _TransferwisePayment: 
    :type _TransferwisePayment: endpoint.TransferwiseTransfer
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    _BillingInvoice = None
    _DraftPayment = None
    _MasterCardAction = None
    _Payment = None
    _PaymentBatch = None
    _RequestResponse = None
    _ScheduleInstance = None
    _TabResultResponse = None
    _WhitelistResult = None
    _TransferwisePayment = None

    @property
    def BillingInvoice(self):
        """
        :rtype: endpoint.Invoice
        """

        return self._BillingInvoice

    @property
    def DraftPayment(self):
        """
        :rtype: endpoint.DraftPayment
        """

        return self._DraftPayment

    @property
    def MasterCardAction(self):
        """
        :rtype: endpoint.MasterCardAction
        """

        return self._MasterCardAction

    @property
    def Payment(self):
        """
        :rtype: endpoint.Payment
        """

        return self._Payment

    @property
    def PaymentBatch(self):
        """
        :rtype: endpoint.PaymentBatch
        """

        return self._PaymentBatch

    @property
    def RequestResponse(self):
        """
        :rtype: endpoint.RequestResponse
        """

        return self._RequestResponse

    @property
    def ScheduleInstance(self):
        """
        :rtype: endpoint.ScheduleInstance
        """

        return self._ScheduleInstance

    @property
    def TabResultResponse(self):
        """
        :rtype: endpoint.TabResultResponse
        """

        return self._TabResultResponse

    @property
    def WhitelistResult(self):
        """
        :rtype: endpoint.WhitelistResult
        """

        return self._WhitelistResult

    @property
    def TransferwisePayment(self):
        """
        :rtype: endpoint.TransferwiseTransfer
        """

        return self._TransferwisePayment

    def get_referenced_object(self):
        """
        :rtype: BunqModel
        :raise: BunqException
        """

        if self._BillingInvoice is not None:
            return self._BillingInvoice

        if self._DraftPayment is not None:
            return self._DraftPayment

        if self._MasterCardAction is not None:
            return self._MasterCardAction

        if self._Payment is not None:
            return self._Payment

        if self._PaymentBatch is not None:
            return self._PaymentBatch

        if self._RequestResponse is not None:
            return self._RequestResponse

        if self._ScheduleInstance is not None:
            return self._ScheduleInstance

        if self._TabResultResponse is not None:
            return self._TabResultResponse

        if self._WhitelistResult is not None:
            return self._WhitelistResult

        if self._TransferwisePayment is not None:
            return self._TransferwisePayment

        raise BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._BillingInvoice is not None:
            return False

        if self._DraftPayment is not None:
            return False

        if self._MasterCardAction is not None:
            return False

        if self._Payment is not None:
            return False

        if self._PaymentBatch is not None:
            return False

        if self._RequestResponse is not None:
            return False

        if self._ScheduleInstance is not None:
            return False

        if self._TabResultResponse is not None:
            return False

        if self._WhitelistResult is not None:
            return False

        if self._TransferwisePayment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RequestReferenceSplitTheBillAnchorObject
        """

        return converter.json_to_class(RequestReferenceSplitTheBillAnchorObject, json_str)


class WhitelistResultViewAnchoredObject(BunqModel):
    """
    :param _id_: The ID of the whitelist entry.
    :type _id_: int
    :param _requestResponse: The RequestResponse object
    :type _requestResponse: endpoint.RequestResponse
    :param _draftPayment: The DraftPayment object
    :type _draftPayment: endpoint.DraftPayment
    """

    _id_ = None
    _requestResponse = None
    _draftPayment = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def requestResponse(self):
        """
        :rtype: endpoint.RequestResponse
        """

        return self._requestResponse

    @property
    def draftPayment(self):
        """
        :rtype: endpoint.DraftPayment
        """

        return self._draftPayment

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._requestResponse is not None:
            return False

        if self._draftPayment is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: WhitelistResultViewAnchoredObject
        """

        return converter.json_to_class(WhitelistResultViewAnchoredObject, json_str)


class MonetaryAccountProfileFill(BunqModel):
    """
    :param _status: The status of the profile.
    :type _status: str
    :param _balance_preferred: The goal balance.
    :type _balance_preferred: Amount
    :param _balance_threshold_low: The low threshold balance.
    :type _balance_threshold_low: Amount
    :param _method_fill: The method used to fill the monetary account. Currently
    only iDEAL is supported, and it is the default one.
    :type _method_fill: str
    :param _issuer: The bank the fill is supposed to happen from, with BIC and
    bank name.
    :type _issuer: Issuer
    """

    _status = None
    _balance_preferred = None
    _balance_threshold_low = None
    _method_fill = None
    _issuer = None
    _status_field_for_request = None
    _balance_preferred_field_for_request = None
    _balance_threshold_low_field_for_request = None
    _method_fill_field_for_request = None
    _issuer_field_for_request = None

    def __init__(self, status, balance_preferred, balance_threshold_low, method_fill, issuer=None):
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

        self._status_field_for_request = status
        self._balance_preferred_field_for_request = balance_preferred
        self._balance_threshold_low_field_for_request = balance_threshold_low
        self._method_fill_field_for_request = method_fill
        self._issuer_field_for_request = issuer

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def balance_preferred(self):
        """
        :rtype: Amount
        """

        return self._balance_preferred

    @property
    def balance_threshold_low(self):
        """
        :rtype: Amount
        """

        return self._balance_threshold_low

    @property
    def method_fill(self):
        """
        :rtype: str
        """

        return self._method_fill

    @property
    def issuer(self):
        """
        :rtype: Issuer
        """

        return self._issuer

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._status is not None:
            return False

        if self._balance_preferred is not None:
            return False

        if self._balance_threshold_low is not None:
            return False

        if self._method_fill is not None:
            return False

        if self._issuer is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccountProfileFill
        """

        return converter.json_to_class(MonetaryAccountProfileFill, json_str)


class Issuer(BunqModel):
    """
    :param _bic: The BIC code.
    :type _bic: str
    :param _name: The name of the bank.
    :type _name: str
    """

    _bic = None
    _name = None
    _bic_field_for_request = None
    _name_field_for_request = None

    def __init__(self, bic, name=None):
        """
        :param bic: The BIC code.
        :type bic: str
        :param name: The name of the bank.
        :type name: str
        """

        self._bic_field_for_request = bic
        self._name_field_for_request = name

    @property
    def bic(self):
        """
        :rtype: str
        """

        return self._bic

    @property
    def name(self):
        """
        :rtype: str
        """

        return self._name

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._bic is not None:
            return False

        if self._name is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: Issuer
        """

        return converter.json_to_class(Issuer, json_str)


class MonetaryAccountProfileDrain(BunqModel):
    """
    :param _status: The status of the profile.
    :type _status: str
    :param _balance_preferred: The goal balance.
    :type _balance_preferred: Amount
    :param _balance_threshold_high: The high threshold balance.
    :type _balance_threshold_high: Amount
    :param _savings_account_alias: The savings monetary account.
    :type _savings_account_alias: MonetaryAccountReference
    """

    _status = None
    _balance_preferred = None
    _balance_threshold_high = None
    _savings_account_alias = None
    _status_field_for_request = None
    _balance_preferred_field_for_request = None
    _balance_threshold_high_field_for_request = None
    _savings_account_alias_field_for_request = None

    def __init__(self, status, balance_preferred, balance_threshold_high, savings_account_alias):
        """
        :param status: The status of the profile.
        :type status: str
        :param balance_preferred: The goal balance.
        :type balance_preferred: Amount
        :param balance_threshold_high: The high threshold balance.
        :type balance_threshold_high: Amount
        :param savings_account_alias: The savings monetary account.
        :type savings_account_alias: Pointer
        """

        self._status_field_for_request = status
        self._balance_preferred_field_for_request = balance_preferred
        self._balance_threshold_high_field_for_request = balance_threshold_high
        self._savings_account_alias_field_for_request = savings_account_alias

    @property
    def status(self):
        """
        :rtype: str
        """

        return self._status

    @property
    def balance_preferred(self):
        """
        :rtype: Amount
        """

        return self._balance_preferred

    @property
    def balance_threshold_high(self):
        """
        :rtype: Amount
        """

        return self._balance_threshold_high

    @property
    def savings_account_alias(self):
        """
        :rtype: MonetaryAccountReference
        """

        return self._savings_account_alias

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._status is not None:
            return False

        if self._balance_preferred is not None:
            return False

        if self._balance_threshold_high is not None:
            return False

        if self._savings_account_alias is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccountProfileDrain
        """

        return converter.json_to_class(MonetaryAccountProfileDrain, json_str)


class MonetaryAccountSetting(BunqModel):
    """
    :param _color: The color chosen for the MonetaryAccount.
    :type _color: str
    :param _icon: The icon chosen for the MonetaryAccount.
    :type _icon: str
    :param _default_avatar_status: The status of the avatar. Can be either
    AVATAR_DEFAULT, AVATAR_CUSTOM or AVATAR_UNDETERMINED.
    :type _default_avatar_status: str
    :param _restriction_chat: The chat restriction. Possible values are
    ALLOW_INCOMING or BLOCK_INCOMING
    :type _restriction_chat: str
    """

    _color = None
    _icon = None
    _default_avatar_status = None
    _restriction_chat = None
    _color_field_for_request = None
    _icon_field_for_request = None
    _default_avatar_status_field_for_request = None
    _restriction_chat_field_for_request = None

    def __init__(self, color=None, icon=None, default_avatar_status=None, restriction_chat=None):
        """
        :param color: The color chosen for the MonetaryAccount in hexadecimal
        format.
        :type color: str
        :param icon: The icon chosen for the MonetaryAccount.
        :type icon: str
        :param default_avatar_status: The status of the avatar. Cannot be updated
        directly.
        :type default_avatar_status: str
        :param restriction_chat: The chat restriction. Possible values are
        ALLOW_INCOMING or BLOCK_INCOMING
        :type restriction_chat: str
        """

        self._color_field_for_request = color
        self._icon_field_for_request = icon
        self._default_avatar_status_field_for_request = default_avatar_status
        self._restriction_chat_field_for_request = restriction_chat

    @property
    def color(self):
        """
        :rtype: str
        """

        return self._color

    @property
    def icon(self):
        """
        :rtype: str
        """

        return self._icon

    @property
    def default_avatar_status(self):
        """
        :rtype: str
        """

        return self._default_avatar_status

    @property
    def restriction_chat(self):
        """
        :rtype: str
        """

        return self._restriction_chat

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._color is not None:
            return False

        if self._icon is not None:
            return False

        if self._default_avatar_status is not None:
            return False

        if self._restriction_chat is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: MonetaryAccountSetting
        """

        return converter.json_to_class(MonetaryAccountSetting, json_str)


class CoOwner(BunqModel):
    """
    :param _alias: The Alias of the co-owner.
    :type _alias: LabelUser
    :param _status: Can be: ACCEPTED, REJECTED, PENDING or REVOKED
    :type _status: str
    """

    _alias = None
    _status = None
    _alias_field_for_request = None

    def __init__(self, alias):
        """
        :param alias: The users the account will be joint with.
        :type alias: Pointer
        """

        self._alias_field_for_request = alias

    @property
    def alias(self):
        """
        :rtype: LabelUser
        """

        return self._alias

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

        if self._alias is not None:
            return False

        if self._status is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: CoOwner
        """

        return converter.json_to_class(CoOwner, json_str)


class NotificationFilterPush(BunqModel):
    """
    :param _category: The notification category that will match this
    notification filter.
    :type _category: str
    """

    _category = None
    _category_field_for_request = None

    def __init__(self, category=None):
        """
        :param category: The notification category that will match this notification
        filter.
        :type category: str
        """

        self._category_field_for_request = category

    @property
    def category(self):
        """
        :rtype: str
        """

        return self._category

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._category is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: NotificationFilterPush
        """

        return converter.json_to_class(NotificationFilterPush, json_str)


class NotificationFilterUrl(BunqModel):
    """
    :param _category: The notification category that will match this
    notification filter.
    :type _category: str
    :param _notification_target: The URL to which the callback should be made.
    :type _notification_target: str
    :param _id_: The id of the NotificationFilterUrl.
    :type _id_: int
    :param _created: The timestamp of the NotificationFilterUrl's creation.
    :type _created: str
    :param _updated: The timestamp of the NotificationFilterUrl's last update.
    :type _updated: str
    """

    _id_ = None
    _created = None
    _updated = None
    _category = None
    _notification_target = None
    _category_field_for_request = None
    _notification_target_field_for_request = None

    def __init__(self, category=None, notification_target=None):
        """
        :param category: The notification category that will match this notification
        filter.
        :type category: str
        :param notification_target: The URL to which the callback should be made.
        :type notification_target: str
        """

        self._category_field_for_request = category
        self._notification_target_field_for_request = notification_target

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
    def category(self):
        """
        :rtype: str
        """

        return self._category

    @property
    def notification_target(self):
        """
        :rtype: str
        """

        return self._notification_target

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

        if self._category is not None:
            return False

        if self._notification_target is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: NotificationFilterUrl
        """

        return converter.json_to_class(NotificationFilterUrl, json_str)


class NotificationUrl(BunqModel):
    """
    :param _target_url: 
    :type _target_url: str
    :param _category: 
    :type _category: str
    :param _event_type: 
    :type _event_type: str
    :param _object_: 
    :type _object_: NotificationAnchorObject
    """

    _target_url = None
    _category = None
    _event_type = None
    _object_ = None

    @property
    def target_url(self):
        """
        :rtype: str
        """

        return self._target_url

    @property
    def category(self):
        """
        :rtype: str
        """

        return self._category

    @property
    def event_type(self):
        """
        :rtype: str
        """

        return self._event_type

    @property
    def object_(self):
        """
        :rtype: NotificationAnchorObject
        """

        return self._object_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._target_url is not None:
            return False

        if self._category is not None:
            return False

        if self._event_type is not None:
            return False

        if self._object_ is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: NotificationUrl
        """

        return converter.json_to_class(NotificationUrl, json_str)


class NotificationAnchorObject(BunqModel, AnchorObjectInterface):
    """
    :param _BunqMeFundraiserResult: 
    :type _BunqMeFundraiserResult: endpoint.BunqMeFundraiserResult
    :param _BunqMeTab: 
    :type _BunqMeTab: endpoint.BunqMeTab
    :param _BunqMeTabResultInquiry: 
    :type _BunqMeTabResultInquiry: endpoint.BunqMeTabResultInquiry
    :param _BunqMeTabResultResponse: 
    :type _BunqMeTabResultResponse: endpoint.BunqMeTabResultResponse
    :param _ChatMessage: 
    :type _ChatMessage: endpoint.ChatMessage
    :param _DraftPayment: 
    :type _DraftPayment: endpoint.DraftPayment
    :param _IdealMerchantTransaction: 
    :type _IdealMerchantTransaction: endpoint.IdealMerchantTransaction
    :param _Invoice: 
    :type _Invoice: endpoint.Invoice
    :param _MasterCardAction: 
    :type _MasterCardAction: endpoint.MasterCardAction
    :param _MonetaryAccount: 
    :type _MonetaryAccount: endpoint.MonetaryAccount
    :param _Payment: 
    :type _Payment: endpoint.Payment
    :param _PaymentBatch: 
    :type _PaymentBatch: endpoint.PaymentBatch
    :param _RequestInquiry: 
    :type _RequestInquiry: endpoint.RequestInquiry
    :param _RequestInquiryBatch: 
    :type _RequestInquiryBatch: endpoint.RequestInquiryBatch
    :param _RequestResponse: 
    :type _RequestResponse: endpoint.RequestResponse
    :param _ShareInviteBankInquiry: 
    :type _ShareInviteBankInquiry: endpoint.ShareInviteMonetaryAccountInquiry
    :param _ShareInviteBankResponse: 
    :type _ShareInviteBankResponse: endpoint.ShareInviteMonetaryAccountResponse
    :param _ScheduledPayment: 
    :type _ScheduledPayment: endpoint.SchedulePayment
    :param _ScheduledInstance: 
    :type _ScheduledInstance: endpoint.ScheduleInstance
    :param _TabResultInquiry: 
    :type _TabResultInquiry: endpoint.TabResultInquiry
    :param _TabResultResponse: 
    :type _TabResultResponse: endpoint.TabResultResponse
    :param _User: 
    :type _User: endpoint.User
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    _BunqMeFundraiserResult = None
    _BunqMeTab = None
    _BunqMeTabResultInquiry = None
    _BunqMeTabResultResponse = None
    _ChatMessage = None
    _DraftPayment = None
    _IdealMerchantTransaction = None
    _Invoice = None
    _MasterCardAction = None
    _MonetaryAccount = None
    _Payment = None
    _PaymentBatch = None
    _RequestInquiry = None
    _RequestInquiryBatch = None
    _RequestResponse = None
    _ShareInviteBankInquiry = None
    _ShareInviteBankResponse = None
    _ScheduledPayment = None
    _ScheduledInstance = None
    _TabResultInquiry = None
    _TabResultResponse = None
    _User = None

    @property
    def BunqMeFundraiserResult(self):
        """
        :rtype: endpoint.BunqMeFundraiserResult
        """

        return self._BunqMeFundraiserResult

    @property
    def BunqMeTab(self):
        """
        :rtype: endpoint.BunqMeTab
        """

        return self._BunqMeTab

    @property
    def BunqMeTabResultInquiry(self):
        """
        :rtype: endpoint.BunqMeTabResultInquiry
        """

        return self._BunqMeTabResultInquiry

    @property
    def BunqMeTabResultResponse(self):
        """
        :rtype: endpoint.BunqMeTabResultResponse
        """

        return self._BunqMeTabResultResponse

    @property
    def ChatMessage(self):
        """
        :rtype: endpoint.ChatMessage
        """

        return self._ChatMessage

    @property
    def DraftPayment(self):
        """
        :rtype: endpoint.DraftPayment
        """

        return self._DraftPayment

    @property
    def IdealMerchantTransaction(self):
        """
        :rtype: endpoint.IdealMerchantTransaction
        """

        return self._IdealMerchantTransaction

    @property
    def Invoice(self):
        """
        :rtype: endpoint.Invoice
        """

        return self._Invoice

    @property
    def MasterCardAction(self):
        """
        :rtype: endpoint.MasterCardAction
        """

        return self._MasterCardAction

    @property
    def MonetaryAccount(self):
        """
        :rtype: endpoint.MonetaryAccount
        """

        return self._MonetaryAccount

    @property
    def Payment(self):
        """
        :rtype: endpoint.Payment
        """

        return self._Payment

    @property
    def PaymentBatch(self):
        """
        :rtype: endpoint.PaymentBatch
        """

        return self._PaymentBatch

    @property
    def RequestInquiry(self):
        """
        :rtype: endpoint.RequestInquiry
        """

        return self._RequestInquiry

    @property
    def RequestInquiryBatch(self):
        """
        :rtype: endpoint.RequestInquiryBatch
        """

        return self._RequestInquiryBatch

    @property
    def RequestResponse(self):
        """
        :rtype: endpoint.RequestResponse
        """

        return self._RequestResponse

    @property
    def ShareInviteBankInquiry(self):
        """
        :rtype: endpoint.ShareInviteMonetaryAccountInquiry
        """

        return self._ShareInviteBankInquiry

    @property
    def ShareInviteBankResponse(self):
        """
        :rtype: endpoint.ShareInviteMonetaryAccountResponse
        """

        return self._ShareInviteBankResponse

    @property
    def ScheduledPayment(self):
        """
        :rtype: endpoint.SchedulePayment
        """

        return self._ScheduledPayment

    @property
    def ScheduledInstance(self):
        """
        :rtype: endpoint.ScheduleInstance
        """

        return self._ScheduledInstance

    @property
    def TabResultInquiry(self):
        """
        :rtype: endpoint.TabResultInquiry
        """

        return self._TabResultInquiry

    @property
    def TabResultResponse(self):
        """
        :rtype: endpoint.TabResultResponse
        """

        return self._TabResultResponse

    @property
    def User(self):
        """
        :rtype: endpoint.User
        """

        return self._User

    def get_referenced_object(self):
        """
        :rtype: BunqModel
        :raise: BunqException
        """

        if self._BunqMeFundraiserResult is not None:
            return self._BunqMeFundraiserResult

        if self._BunqMeTab is not None:
            return self._BunqMeTab

        if self._BunqMeTabResultInquiry is not None:
            return self._BunqMeTabResultInquiry

        if self._BunqMeTabResultResponse is not None:
            return self._BunqMeTabResultResponse

        if self._ChatMessage is not None:
            return self._ChatMessage

        if self._DraftPayment is not None:
            return self._DraftPayment

        if self._IdealMerchantTransaction is not None:
            return self._IdealMerchantTransaction

        if self._Invoice is not None:
            return self._Invoice

        if self._MasterCardAction is not None:
            return self._MasterCardAction

        if self._MonetaryAccount is not None:
            return self._MonetaryAccount

        if self._Payment is not None:
            return self._Payment

        if self._PaymentBatch is not None:
            return self._PaymentBatch

        if self._RequestInquiry is not None:
            return self._RequestInquiry

        if self._RequestInquiryBatch is not None:
            return self._RequestInquiryBatch

        if self._RequestResponse is not None:
            return self._RequestResponse

        if self._ShareInviteBankInquiry is not None:
            return self._ShareInviteBankInquiry

        if self._ShareInviteBankResponse is not None:
            return self._ShareInviteBankResponse

        if self._ScheduledPayment is not None:
            return self._ScheduledPayment

        if self._ScheduledInstance is not None:
            return self._ScheduledInstance

        if self._TabResultInquiry is not None:
            return self._TabResultInquiry

        if self._TabResultResponse is not None:
            return self._TabResultResponse

        if self._User is not None:
            return self._User

        raise BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._BunqMeFundraiserResult is not None:
            return False

        if self._BunqMeTab is not None:
            return False

        if self._BunqMeTabResultInquiry is not None:
            return False

        if self._BunqMeTabResultResponse is not None:
            return False

        if self._ChatMessage is not None:
            return False

        if self._DraftPayment is not None:
            return False

        if self._IdealMerchantTransaction is not None:
            return False

        if self._Invoice is not None:
            return False

        if self._MasterCardAction is not None:
            return False

        if self._MonetaryAccount is not None:
            return False

        if self._Payment is not None:
            return False

        if self._PaymentBatch is not None:
            return False

        if self._RequestInquiry is not None:
            return False

        if self._RequestInquiryBatch is not None:
            return False

        if self._RequestResponse is not None:
            return False

        if self._ShareInviteBankInquiry is not None:
            return False

        if self._ShareInviteBankResponse is not None:
            return False

        if self._ScheduledPayment is not None:
            return False

        if self._ScheduledInstance is not None:
            return False

        if self._TabResultInquiry is not None:
            return False

        if self._TabResultResponse is not None:
            return False

        if self._User is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: NotificationAnchorObject
        """

        return converter.json_to_class(NotificationAnchorObject, json_str)


class TaxResident(BunqModel):
    """
    :param _country: The country of the tax number.
    :type _country: str
    :param _tax_number: The tax number.
    :type _tax_number: str
    :param _status: The status of the tax number. Either CONFIRMED or
    UNCONFIRMED.
    :type _status: str
    """

    _country = None
    _tax_number = None
    _status = None
    _country_field_for_request = None
    _tax_number_field_for_request = None
    _status_field_for_request = None

    def __init__(self, country=None, tax_number=None, status=None):
        """
        :param country: The country of the tax number.
        :type country: str
        :param tax_number: The tax number.
        :type tax_number: str
        :param status: The status of the tax number. Either CONFIRMED or
        UNCONFIRMED.
        :type status: str
        """

        self._country_field_for_request = country
        self._tax_number_field_for_request = tax_number
        self._status_field_for_request = status

    @property
    def country(self):
        """
        :rtype: str
        """

        return self._country

    @property
    def tax_number(self):
        """
        :rtype: str
        """

        return self._tax_number

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

        if self._country is not None:
            return False

        if self._tax_number is not None:
            return False

        if self._status is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TaxResident
        """

        return converter.json_to_class(TaxResident, json_str)


class UserApiKeyAnchoredUser(BunqModel, AnchorObjectInterface):
    """
    :param _UserPerson: 
    :type _UserPerson: endpoint.UserPerson
    :param _UserCompany: 
    :type _UserCompany: endpoint.UserCompany
    :param _UserPaymentServiceProvider: 
    :type _UserPaymentServiceProvider: endpoint.UserPaymentServiceProvider
    """

    # Error constants.
    _ERROR_NULL_FIELDS = "All fields of an extended model or object are null."

    _UserPerson = None
    _UserCompany = None
    _UserPaymentServiceProvider = None

    @property
    def UserPerson(self):
        """
        :rtype: endpoint.UserPerson
        """

        return self._UserPerson

    @property
    def UserCompany(self):
        """
        :rtype: endpoint.UserCompany
        """

        return self._UserCompany

    @property
    def UserPaymentServiceProvider(self):
        """
        :rtype: endpoint.UserPaymentServiceProvider
        """

        return self._UserPaymentServiceProvider

    def get_referenced_object(self):
        """
        :rtype: BunqModel
        :raise: BunqException
        """

        if self._UserPerson is not None:
            return self._UserPerson

        if self._UserCompany is not None:
            return self._UserCompany

        if self._UserPaymentServiceProvider is not None:
            return self._UserPaymentServiceProvider

        raise BunqException(self._ERROR_NULL_FIELDS)

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._UserPerson is not None:
            return False

        if self._UserCompany is not None:
            return False

        if self._UserPaymentServiceProvider is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: UserApiKeyAnchoredUser
        """

        return converter.json_to_class(UserApiKeyAnchoredUser, json_str)


class OauthCallbackUrl(BunqModel):
    """
    :param _id_: The id of the callback URL.
    :type _id_: int
    :param _created: The timestamp of the callback URL's creation.
    :type _created: str
    :param _updated: The timestamp of the callback URL's last update.
    :type _updated: str
    :param _url: The Callback URL.
    :type _url: str
    """

    _id_ = None
    _created = None
    _updated = None
    _url = None

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
    def url(self):
        """
        :rtype: str
        """

        return self._url

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

        if self._url is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: OauthCallbackUrl
        """

        return converter.json_to_class(OauthCallbackUrl, json_str)


class PermittedDevice(BunqModel):
    """
    :param _description: The description of the device that may use the
    credential.
    :type _description: str
    :param _ip: The IP address of the device that may use the credential.
    :type _ip: str
    """

    _description = None
    _ip = None

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

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._description is not None:
            return False

        if self._ip is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: PermittedDevice
        """

        return converter.json_to_class(PermittedDevice, json_str)


class TransferwiseRequirementField(BunqModel):
    """
    :param _key: The name of the required field.
    :type _key: str
    :param _value: The value of the required field.
    :type _value: str
    :param _name: The descriptive label of the field.
    :type _name: str
    :param _group: The field group.
    :type _group: TransferwiseRequirementFieldGroup
    """

    _name = None
    _group = None
    _key_field_for_request = None
    _value_field_for_request = None

    def __init__(self, key=None, value=None):
        """
        :param key: The name of the required field.
        :type key: str
        :param value: The value of the required field.
        :type value: str
        """

        self._key_field_for_request = key
        self._value_field_for_request = value

    @property
    def name(self):
        """
        :rtype: str
        """

        return self._name

    @property
    def group(self):
        """
        :rtype: TransferwiseRequirementFieldGroup
        """

        return self._group

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._name is not None:
            return False

        if self._group is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TransferwiseRequirementField
        """

        return converter.json_to_class(TransferwiseRequirementField, json_str)


class TransferwiseRequirementFieldGroup(BunqModel):
    """
    :param _key: The key of the field. This is the value to send as input.
    :type _key: str
    :param _type_: The field's input type: "text", "select" or "radio".
    :type _type_: str
    :param _name: The field name.
    :type _name: str
    :param _refresh_requirements_on_change: Indicates that any changes in this
    field affect the requirements, if this field is changed, the requirements
    endpoint must be called again to recheck if there are any additional
    requirements.
    :type _refresh_requirements_on_change: bool
    :param _required: Whether or not the field is required.
    :type _required: bool
    :param _display_format: Formatting mask to guide user input.
    :type _display_format: str
    :param _example: An example value for this field.
    :type _example: str
    :param _min_length: The minimum length of the field's value.
    :type _min_length: str
    :param _max_length: The maximum length of the field's value.
    :type _max_length: str
    :param _validation_regexp: A regular expression which may be used to
    validate the user input.
    :type _validation_regexp: str
    :param _validation_async: Details of an endpoint which may be used to
    validate the user input.
    :type _validation_async: TransferwiseRequirementFieldGroupValidationAsync
    :param _values_allowed: Shows which values are allowed for fields of type
    "select" or "radio".
    :type _values_allowed: TransferwiseRequirementFieldGroupValuesAllowed
    """

    _key = None
    _type_ = None
    _name = None
    _refresh_requirements_on_change = None
    _required = None
    _display_format = None
    _example = None
    _min_length = None
    _max_length = None
    _validation_regexp = None
    _validation_async = None
    _values_allowed = None

    @property
    def key(self):
        """
        :rtype: str
        """

        return self._key

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def name(self):
        """
        :rtype: str
        """

        return self._name

    @property
    def refresh_requirements_on_change(self):
        """
        :rtype: bool
        """

        return self._refresh_requirements_on_change

    @property
    def required(self):
        """
        :rtype: bool
        """

        return self._required

    @property
    def display_format(self):
        """
        :rtype: str
        """

        return self._display_format

    @property
    def example(self):
        """
        :rtype: str
        """

        return self._example

    @property
    def min_length(self):
        """
        :rtype: str
        """

        return self._min_length

    @property
    def max_length(self):
        """
        :rtype: str
        """

        return self._max_length

    @property
    def validation_regexp(self):
        """
        :rtype: str
        """

        return self._validation_regexp

    @property
    def validation_async(self):
        """
        :rtype: TransferwiseRequirementFieldGroupValidationAsync
        """

        return self._validation_async

    @property
    def values_allowed(self):
        """
        :rtype: TransferwiseRequirementFieldGroupValuesAllowed
        """

        return self._values_allowed

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._key is not None:
            return False

        if self._type_ is not None:
            return False

        if self._name is not None:
            return False

        if self._refresh_requirements_on_change is not None:
            return False

        if self._required is not None:
            return False

        if self._display_format is not None:
            return False

        if self._example is not None:
            return False

        if self._min_length is not None:
            return False

        if self._max_length is not None:
            return False

        if self._validation_regexp is not None:
            return False

        if self._validation_async is not None:
            return False

        if self._values_allowed is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TransferwiseRequirementFieldGroup
        """

        return converter.json_to_class(TransferwiseRequirementFieldGroup, json_str)


class TransferwiseRequirementFieldGroupValidationAsync(BunqModel):
    """
    :param _url: The url to be used to validate user input.
    :type _url: str
    :param _params: The parameters to send when validating user input.
    :type _params: TransferwiseRequirementFieldGroupValidationAsyncParams
    """

    _url = None
    _params = None

    @property
    def url(self):
        """
        :rtype: str
        """

        return self._url

    @property
    def params(self):
        """
        :rtype: TransferwiseRequirementFieldGroupValidationAsyncParams
        """

        return self._params

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._url is not None:
            return False

        if self._params is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TransferwiseRequirementFieldGroupValidationAsync
        """

        return converter.json_to_class(TransferwiseRequirementFieldGroupValidationAsync, json_str)


class TransferwiseRequirementFieldGroupValidationAsyncParams(BunqModel):
    """
    :param _key: The parameter key.
    :type _key: str
    :param _parameter_name: The parameter label.
    :type _parameter_name: str
    :param _required: Shows whether the parameter is required or not.
    :type _required: bool
    """

    _key = None
    _parameter_name = None
    _required = None

    @property
    def key(self):
        """
        :rtype: str
        """

        return self._key

    @property
    def parameter_name(self):
        """
        :rtype: str
        """

        return self._parameter_name

    @property
    def required(self):
        """
        :rtype: bool
        """

        return self._required

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._key is not None:
            return False

        if self._parameter_name is not None:
            return False

        if self._required is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TransferwiseRequirementFieldGroupValidationAsyncParams
        """

        return converter.json_to_class(TransferwiseRequirementFieldGroupValidationAsyncParams, json_str)


class TransferwiseRequirementFieldGroupValuesAllowed(BunqModel):
    """
    :param _key: The key.
    :type _key: str
    :param _name: The label.
    :type _name: str
    """

    _key = None
    _name = None

    @property
    def key(self):
        """
        :rtype: str
        """

        return self._key

    @property
    def name(self):
        """
        :rtype: str
        """

        return self._name

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._key is not None:
            return False

        if self._name is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: TransferwiseRequirementFieldGroupValuesAllowed
        """

        return converter.json_to_class(TransferwiseRequirementFieldGroupValuesAllowed, json_str)


class AllocationItem(BunqModel):
    """
    :param _alias: The Alias of the party we are allocating money for.
    :type _alias: Pointer
    :param _type_: The type of the AllocationItem.
    :type _type_: str
    :param _amount: The Amount of the AllocationItem.
    :type _amount: Amount
    :param _share_ratio: The share ratio of the AllocationItem.
    :type _share_ratio: int
    :param _membership: The membership.
    :type _membership: endpoint.RegistryMembership
    """

    _type_ = None
    _membership = None
    _amount = None
    _share_ratio = None
    _alias_field_for_request = None
    _type__field_for_request = None
    _amount_field_for_request = None
    _share_ratio_field_for_request = None

    def __init__(self, alias=None, type_=None, amount=None, share_ratio=None):
        """
        :param alias: The Alias of the party we are allocating money for.
        :type alias: Pointer
        :param type_: The type of the AllocationItem.
        :type type_: str
        :param amount: The Amount of the AllocationItem.
        :type amount: Amount
        :param share_ratio: The share ratio of the AllocationItem.
        :type share_ratio: int
        """

        self._alias_field_for_request = alias
        self._type__field_for_request = type_
        self._amount_field_for_request = amount
        self._share_ratio_field_for_request = share_ratio

    @property
    def type_(self):
        """
        :rtype: str
        """

        return self._type_

    @property
    def membership(self):
        """
        :rtype: endpoint.RegistryMembership
        """

        return self._membership

    @property
    def amount(self):
        """
        :rtype: Amount
        """

        return self._amount

    @property
    def share_ratio(self):
        """
        :rtype: int
        """

        return self._share_ratio

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._type_ is not None:
            return False

        if self._membership is not None:
            return False

        if self._amount is not None:
            return False

        if self._share_ratio is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: AllocationItem
        """

        return converter.json_to_class(AllocationItem, json_str)


class RegistryEntryAttachment(BunqModel):
    """
    :param _id_: The id of the attachment.
    :type _id_: int
    :param _monetary_account_id: The id of the monetary account to which the
    attachment belongs.
    :type _monetary_account_id: int
    """

    _id_ = None
    _monetary_account_id = None
    _id__field_for_request = None

    def __init__(self, id_=None):
        """
        :param id_: The id of the attachment we are attaching.
        :type id_: int
        """

        self._id__field_for_request = id_

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

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._id_ is not None:
            return False

        if self._monetary_account_id is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RegistryEntryAttachment
        """

        return converter.json_to_class(RegistryEntryAttachment, json_str)


class RegistryEntryReference(BunqModel):
    """
    :param _type_: The object type that will be linked to the RegistryEntry.
    :type _type_: str
    :param _id_: The ID of the object that will be used for the RegistryEntry.
    :type _id_: int
    """

    _type__field_for_request = None
    _id__field_for_request = None

    def __init__(self, type_=None, id_=None):
        """
        :param type_: The object type that will be linked to the RegistryEntry.
        :type type_: str
        :param id_: The ID of the object that will be used for the RegistryEntry.
        :type id_: int
        """

        self._type__field_for_request = type_
        self._id__field_for_request = id_

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RegistryEntryReference
        """

        return converter.json_to_class(RegistryEntryReference, json_str)


class RegistrySettlementItem(BunqModel):
    """
    :param _amount: The amount of the RegistrySettlementItem.
    :type _amount: Amount
    :param _membership_paying: The membership of the user that has to pay.
    :type _membership_paying: endpoint.RegistryMembership
    :param _membership_receiving: The membership of the user that will receive
    money.
    :type _membership_receiving: endpoint.RegistryMembership
    :param _paying_user_alias: The LabelMonetaryAccount of the user that has to
    pay the request.
    :type _paying_user_alias: MonetaryAccountReference
    :param _receiving_user_alias: The LabelMonetaryAccount of the user that will
    receive the amount.
    :type _receiving_user_alias: MonetaryAccountReference
    """

    _amount = None
    _membership_paying = None
    _membership_receiving = None
    _paying_user_alias = None
    _receiving_user_alias = None

    @property
    def amount(self):
        """
        :rtype: Amount
        """

        return self._amount

    @property
    def membership_paying(self):
        """
        :rtype: endpoint.RegistryMembership
        """

        return self._membership_paying

    @property
    def membership_receiving(self):
        """
        :rtype: endpoint.RegistryMembership
        """

        return self._membership_receiving

    @property
    def paying_user_alias(self):
        """
        :rtype: MonetaryAccountReference
        """

        return self._paying_user_alias

    @property
    def receiving_user_alias(self):
        """
        :rtype: MonetaryAccountReference
        """

        return self._receiving_user_alias

    def is_all_field_none(self):
        """
        :rtype: bool
        """

        if self._amount is not None:
            return False

        if self._membership_paying is not None:
            return False

        if self._membership_receiving is not None:
            return False

        if self._paying_user_alias is not None:
            return False

        if self._receiving_user_alias is not None:
            return False

        return True

    @staticmethod
    def from_json(json_str):
        """
        :type json_str: str
        
        :rtype: RegistrySettlementItem
        """

        return converter.json_to_class(RegistrySettlementItem, json_str)


class MonetaryAccountReference(BunqModel):
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
        instance.label_monetary_account._iban = pointer.value
        instance.label_monetary_account._display_name = pointer.name

        return instance

    @classmethod
    def create_from_label_monetary_account(cls, label_monetary_account):
        """
        :type label_monetary_account: LabelMonetaryAccount
        """

        instance = cls.__new__(cls)
        instance.label_monetary_account = label_monetary_account
        instance.pointer = Pointer()
        instance.pointer._name = label_monetary_account.display_name
        instance.pointer._type_ = cls._POINTER_TYPE_IBAN
        instance.pointer._value = label_monetary_account.iban

        return instance

    def is_all_field_none(self):
        return False

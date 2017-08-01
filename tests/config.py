import json
import os

from bunq.sdk.model.generated.object_ import Pointer


class Config:
    _FIELD_IP_ADDRESS_ALLOWED = "ipAddress"
    _FIELD_COUNTER_PARTY_OTHER = "CounterPartyOther"
    _FIELD_COUNTER_PARTY_SELF = "CounterPartySelf"
    _FIELD_TYPE = "Type"
    _FIELD_ALIAS = "Alias"
    _FIELD_TAB_USAGE = "TabUsageSingleTest"
    _FIELD_CASH_REGISTER_ID = "CASH_REGISTER_ID"
    _FIELD_MONETARY_ACCOUNT_ID_1 = "MA_ID"
    _FIELD_MONETARY_ACCOUNT_ID_2 = "MA_ID2"
    _FIELD_USER_ID = "USER_ID"
    _FIELD_API_KEY = "API_KEY"
    _FIELD_ATTACHMENT_PUBLIC = "AttachmentPublicTest"
    _FIELD_ATTACHMENT_PATH_IN = "PATH_IN"
    _FIELD_ATTACHMENT_DESCRIPTION = "DESCRIPTION"
    _FIELD_ATTACHMENT_CONTENT_TYPE = "CONTENT_TYPE"

    @classmethod
    def get_attachment_content_type(cls):
        """
        :rtype: str
        """

        return cls._get_config_file()[cls._FIELD_ATTACHMENT_PUBLIC][
            cls._FIELD_ATTACHMENT_CONTENT_TYPE]

    @classmethod
    def get_attachment_description(cls):
        """
        :rtype: str
        """

        return cls._get_config_file()[cls._FIELD_ATTACHMENT_PUBLIC][
            cls._FIELD_ATTACHMENT_DESCRIPTION]

    @classmethod
    def get_attachment_path_in(cls):
        """
        :rtype: str
        """

        return cls._get_config_file()[cls._FIELD_ATTACHMENT_PUBLIC][
            cls._FIELD_ATTACHMENT_PATH_IN]

    @classmethod
    def get_api_key(cls):
        """
        :rtype: str
        """

        return cls._get_config_file()[cls._FIELD_API_KEY]

    @classmethod
    def get_user_id(cls):
        """
        :rtype: int
        """

        return int(cls._get_config_file()[cls._FIELD_USER_ID])

    @classmethod
    def get_monetary_account_id_2(cls):
        """
        :rtype: int
        """

        return int(cls._get_config_file()[cls._FIELD_MONETARY_ACCOUNT_ID_2])

    @classmethod
    def get_monetary_account_id_1(cls):
        """
        :rtype: int
        """

        return int(cls._get_config_file()[cls._FIELD_MONETARY_ACCOUNT_ID_1])

    @classmethod
    def get_cash_register_id(cls):
        """
        :rtype str
        """

        return cls._get_config_file()[cls._FIELD_TAB_USAGE][
            cls._FIELD_CASH_REGISTER_ID]

    @classmethod
    def get_pointer_counter_party_self(cls):
        """
        :rtype: Pointer
        """

        type_ = cls._get_config_file()[cls._FIELD_COUNTER_PARTY_SELF][
            cls._FIELD_TYPE]
        alias = cls._get_config_file()[cls._FIELD_COUNTER_PARTY_SELF][
            cls._FIELD_ALIAS]

        return Pointer(type_, alias)

    @classmethod
    def get_pointer_counter_party_other(cls):
        """
        :rtype: Pointer
        """

        type_ = cls._get_config_file()[cls._FIELD_COUNTER_PARTY_OTHER][
            cls._FIELD_TYPE]
        alias = cls._get_config_file()[cls._FIELD_COUNTER_PARTY_OTHER][
            cls._FIELD_ALIAS]

        return Pointer(type_, alias)

    @classmethod
    def get_ip_address(cls):
        """
        :rtype: str
        """

        return cls._get_config_file()[cls._FIELD_IP_ADDRESS_ALLOWED]

    @classmethod
    def _get_config_file(cls):
        """
        :rtype:  json.load
        """

        file_path = os.path.dirname(os.path.realpath(__file__))
        with open(file_path + "/assets/config.json", "r") as f:
            return json.load(f)

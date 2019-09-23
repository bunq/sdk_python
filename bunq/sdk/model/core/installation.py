from abc import ABC

from bunq.sdk.http.api_client import ApiClient
from bunq.sdk.json import converter
from bunq.sdk.model.core.bunq_model import BunqModel


class Installation(BunqModel, ABC):
    """
    :type _id_: Id
    :type _token: SessionToken
    :type _server_public_key: PublicKeyServer
    """

    # Endpoint name.
    _ENDPOINT_URL_POST = "installation"

    # Field constants.
    FIELD_CLIENT_PUBLIC_KEY = "client_public_key"

    def __init__(self):
        self._id_ = None
        self._token = None
        self._server_public_key = None

    @property
    def id_(self):
        """
        :rtype: Id
        """

        return self._id_

    @property
    def token(self):
        """
        :rtype: SessionToken
        """

        return self._token

    @property
    def server_public_key(self):
        """
        :rtype: PublicKeyServer
        """

        return self._server_public_key

    @classmethod
    def create(cls, api_context, public_key_string):
        """
        :type api_context: ApiContext
        :type public_key_string: str

        :rtype: BunqResponse[Installation]
        """

        api_client = ApiClient(api_context)
        body_bytes = cls.generate_request_body_bytes(
            public_key_string
        )
        response_raw = api_client.post(cls._ENDPOINT_URL_POST, body_bytes, {})

        return cls._from_json_array_nested(response_raw)

    @classmethod
    def generate_request_body_bytes(cls, public_key_string):
        """
        :type public_key_string: str

        :rtype: bytes
        """

        return converter.class_to_json(
            {
                cls.FIELD_CLIENT_PUBLIC_KEY: public_key_string,
            }
        ).encode()

    def is_all_field_none(self):
        if self.id_ is not None:
            return False

        if self.token is not None:
            return False

        if self.server_public_key is not None:
            return False

        return True

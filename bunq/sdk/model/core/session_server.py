from abc import ABC

from bunq.sdk.exception.bunq_exception import BunqException
from bunq.sdk.http.api_client import ApiClient
from bunq.sdk.json import converter
from bunq.sdk.model.core.bunq_model import BunqModel


class SessionServer(BunqModel, ABC):
    """
    :type _id_: Id
    :type _token: SessionToken
    :type _user_person: bunq.sdk.model.generated.UserPerson
    :type _user_company: bunq.sdk.model.generated.UserCompany
    :type _user_api_key: bunq.sdk.model.generated.UserApiKey
    """

    # Endpoint name.
    _ENDPOINT_URL_POST = "session-server"

    # Field constants
    FIELD_SECRET = "secret"

    # Error constants
    _ERROR_ALL_FIELD_IS_NULL = 'All fields are null'

    def __init__(self):
        self._id_ = None
        self._token = None
        self._user_person = None
        self._user_company = None
        self._user_api_key = None

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
    def user_person(self):
        """
        :rtype: bunq.sdk.model.generated.UserPerson
        """

        return self._user_person

    @property
    def user_company(self):
        """
        :rtype: bunq.sdk.model.generated.UserCompany
        """

        return self._user_company

    @property
    def user_api_key(self):
        """
        :rtype: bunq.sdk.model.generated.UserApiKey
        """

        return self._user_api_key

    @classmethod
    def create(cls, api_context):
        """
        :type api_context: ApiContext

        :rtype: BunqResponse[SessionServer]
        """

        api_client = ApiClient(api_context)
        body_bytes = cls.generate_request_body_bytes(api_context.api_key)
        response_raw = api_client.post(cls._ENDPOINT_URL_POST, body_bytes, {})

        return cls._from_json_array_nested(response_raw)

    @classmethod
    def generate_request_body_bytes(cls, secret):
        """
        :type secret: str

        :rtype: bytes
        """

        return converter.class_to_json({cls.FIELD_SECRET: secret}).encode()

    def is_all_field_none(self):
        if self.id_ is not None:
            return False

        if self.token is not None:
            return False

        if self.user_person is not None:
            return False

        if self.user_company is not None:
            return False

        if self.user_api_key is not None:
            return False

        return True

    def get_referenced_user(self):
        """
        :rtype: BunqModel
        """

        if self._user_person is not None:
            return self._user_person

        if self._user_company is not None:
            return self._user_company

        if self._user_api_key is not None:
            return self._user_api_key

        raise BunqException(self._ERROR_ALL_FIELD_IS_NULL)

import datetime

import aenum
from Cryptodome.PublicKey import RSA

from bunq.sdk import model
from bunq.sdk import security
from bunq.sdk.json import converter
from bunq.sdk.model import generated


class ApiEnvironmentType(aenum.AutoNumberEnum):
    """
    :type PRODUCTION: ApiEnvironmentType
    :type SANDBOX: ApiEnvironmentType
    :type uri_base: str
    """

    PRODUCTION = 'https://api.bunq.com/v1/'
    SANDBOX = 'https://sandbox.public.api.bunq.com/v1/'

    def __init__(self, uri_base):
        """
        :type uri_base: str
        """

        self._uri_base = uri_base

    @property
    def uri_base(self):
        """
        :rtype: str
        """

        return self._uri_base


class ApiContext(object):
    """
    :type _environment_type: ApiEnvironmentType
    :type _api_key: str
    :type _session_context: SessionContext
    :type _installation_context: InstallationContext
    """

    # File mode for saving and restoring the context
    _FILE_MODE_WRITE = 'w'
    _FILE_MODE_READ = 'r'

    # Minimum time to session expiry not requiring session reset
    _TIME_TO_SESSION_EXPIRY_MINIMUM_SECONDS = 30

    # Dummy ID to pass to Session endpoint
    _SESSION_ID_DUMMY = 0

    # Default path to the file storing serialized API context
    _PATH_API_CONTEXT_DEFAULT = 'bunq.conf'

    def __init__(self, environment_type, api_key, device_description,
                 permitted_ips=None):
        """
        :type environment_type: ApiEnvironmentType
        :type api_key: str
        :type device_description: str
        :type permitted_ips: list[str]|None
        """

        if permitted_ips is None:
            permitted_ips = []

        self._environment_type = environment_type
        self._api_key = api_key
        self._installation_context = None
        self._session_context = None
        self._initialize(device_description, permitted_ips)

    def _initialize(self, device_description, permitted_ips):
        """
        :type device_description: str
        :type permitted_ips: list[str]

        :rtype: None
        """

        self._initialize_installation()
        self._register_device(device_description, permitted_ips)
        self._initialize_session()

    def _initialize_installation(self):
        """
        :rtype: None
        """

        private_key_client = security.generate_rsa_private_key()
        installation = model.Installation.create(
            self,
            security.public_key_to_string(private_key_client.publickey())
        ).value
        token = installation.token.token
        public_key_server_string = \
            installation.server_public_key.server_public_key
        public_key_server = RSA.import_key(public_key_server_string)

        self._installation_context = InstallationContext(
            token,
            private_key_client,
            public_key_server
        )

    def _register_device(self, device_description,
                         permitted_ips):
        """
        :type device_description: str
        :type permitted_ips: list[]

        :rtype: None
        """

        generated.DeviceServer.create(
            self,
            {
                generated.DeviceServer.FIELD_DESCRIPTION: device_description,
                generated.DeviceServer.FIELD_SECRET: self.api_key,
                generated.DeviceServer.FIELD_PERMITTED_IPS: permitted_ips,
            }
        )

    def _initialize_session(self):
        """
        :rtype: None
        """

        session_server = model.SessionServer.create(self).value
        token = session_server.token.token
        expiry_time = self._get_expiry_timestamp(session_server)

        self._session_context = SessionContext(token, expiry_time)

    @classmethod
    def _get_expiry_timestamp(cls, session_server):
        """
        :type session_server: model.SessionServer

        :rtype: datetime.datetime
        """

        timeout_seconds = cls._get_session_timeout_seconds(session_server)
        time_now = datetime.datetime.now()

        return time_now + datetime.timedelta(seconds=timeout_seconds)

    @classmethod
    def _get_session_timeout_seconds(cls, session_server):
        """
        :type session_server: model.SessionServer

        :rtype: int
        """

        if session_server.user_company is not None:
            return session_server.user_company.session_timeout
        else:
            return session_server.user_person.session_timeout

    def ensure_session_active(self):
        if self.session_context is None:
            return

        time_now = datetime.datetime.now()
        time_to_expiry = self.session_context.expiry_time - time_now
        time_to_expiry_minimum = datetime.timedelta(
            seconds=self._TIME_TO_SESSION_EXPIRY_MINIMUM_SECONDS
        )

        if time_to_expiry < time_to_expiry_minimum:
            self.reset_session()

    def reset_session(self):
        """
        Closes the current session and opens a new one.

        :rtype: None
        """

        self._drop_session_context()
        self._initialize_session()

    def _drop_session_context(self):
        """
        :rtype: None
        """

        self._session_context = None

    def close_session(self):
        """
        Closes the current session.

        :rtype: None
        """

        self._delete_session()
        self._drop_session_context()

    def _delete_session(self):
        """
        :rtype: None
        """

        generated.Session.delete(self, self._SESSION_ID_DUMMY)

    @property
    def environment_type(self):
        """
        :rtype: ApiEnvironmentType
        """

        return self._environment_type

    @property
    def api_key(self):
        """
        :rtype: str
        """

        return self._api_key

    @property
    def token(self):
        """
        :rtype: str
        """

        if self._session_context is not None:
            return self.session_context.token
        elif self._installation_context is not None:
            return self.installation_context.token
        else:
            return None

    @property
    def installation_context(self):
        """
        :rtype: InstallationContext
        """

        return self._installation_context

    @property
    def session_context(self):
        """
        :rtype: SessionContext
        """

        return self._session_context

    def save(self, path=None):
        """
        :type path: str

        :rtype: None
        """

        if path is None:
            path = self._PATH_API_CONTEXT_DEFAULT

        with open(path, self._FILE_MODE_WRITE) as file_:
            file_.write(self.to_json())

    def to_json(self):
        """
        Serializes an ApiContext to JSON string.

        :rtype: str
        """

        return converter.class_to_json(self)

    @classmethod
    def restore(cls, path=None):
        """
        :type path: str

        :rtype: ApiContext
        """

        if path is None:
            path = cls._PATH_API_CONTEXT_DEFAULT

        with open(path, cls._FILE_MODE_READ) as file_:
            return cls.from_json(file_.read())
        
    @classmethod
    def from_json(cls, json_str):
        """
        Creates an ApiContext instance from JSON string.

        :type json_str: str

        :rtype: ApiContext
        """

        return converter.json_to_class(ApiContext, json_str)

    def __eq__(self, other):
        return (self.token == other.token and
                self.api_key == other.api_key and
                self.environment_type == other.environment_type)


class InstallationContext(object):
    """
    :type _token: str
    :type _private_key_client: RSA.RsaKey
    :type _public_key_server: RSA.RsaKey
    """

    def __init__(self, token, private_key_client, public_key_server):
        """
        :type token: str
        :type private_key_client: RSA.RsaKey
        :type public_key_server: RSA.RsaKey
        """

        self._token = token
        self._private_key_client = private_key_client
        self._public_key_server = public_key_server

    @property
    def token(self):
        """
        :rtype: str
        """

        return self._token

    @property
    def private_key_client(self):
        """
        :rtype: RSA.RsaKey
        """

        return self._private_key_client

    @property
    def public_key_server(self):
        """
        :rtype: RSA.RsaKey
        """

        return self._public_key_server


class SessionContext(object):
    """
    :type _token: str
    :type _expiry_time: datetime.datetime
    """

    def __init__(self, token, expiry_time):
        """
        :type token: str
        :type expiry_time: datetime.datetime
        """

        self._token = token
        self._expiry_time = expiry_time

    @property
    def token(self):
        """
        :rtype: str
        """

        return self._token

    @property
    def expiry_time(self):
        """
        :rtype: datetime.datetime
        """

        return self._expiry_time

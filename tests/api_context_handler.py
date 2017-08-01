from tests.config import Config
from bunq.sdk.context import ApiContext
from bunq.sdk.context import ApiEnvironmentType
from bunq.sdk.model.generated import endpoint
from bunq.sdk.exception import ApiException


class ApiContextHandler:
    # Config values
    _API_KEY = Config.get_api_key()
    _BUNQ_CONFIG_FILE = "bunq-test.conf"
    _DEVICE_DESCRIPTION = 'Python test device'

    @classmethod
    def get_api_context(cls):
        """
        Calls IsSessionActive to check if the session token is still active
        and returns the ApiContext.

        :rtype: ApiContext
        """

        if cls._is_session_active():
            return ApiContext.restore(cls._BUNQ_CONFIG_FILE)
        else:
            api_context = ApiContext(ApiEnvironmentType.SANDBOX, cls._API_KEY,
                                     cls._DEVICE_DESCRIPTION, [])
            api_context.save(cls._BUNQ_CONFIG_FILE)

            return api_context

    @classmethod
    def _is_session_active(cls):
        """
        Catches ApiExceptoin if the session is inactive.
        Catches BunqEception if the conf file does not exist.

        :rtype: bool
        :return: True If exception is not called, otherwise False.

        """
        try:
            api_context = ApiContext.restore(cls._BUNQ_CONFIG_FILE)
            endpoint.User.list(api_context)

            return True
        except ApiException:
            return False
        except FileNotFoundError:
            return False

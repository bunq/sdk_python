import os
import unittest

from tests.config import Config
from bunq.sdk.context import ApiContext
from bunq.sdk.context import ApiEnvironmentType
from bunq.sdk.model.generated import endpoint
from bunq.sdk.exception import ApiException


class BunqSdkTestCase(unittest.TestCase):
    # Config values
    _API_KEY = Config.get_api_key()

    # Name of bunq config file
    _FILENAME_BUNQ_CONFIG = "/bunq-test.conf"

    # Device description used for python tests
    _DEVICE_DESCRIPTION = 'Python test device'

    @classmethod
    def _get_api_context(cls):
        """
        Calls IsSessionActive to check if the session token is still active
        and returns the ApiContext.

        Catches ApiException if the session is inactive.
        Catches BunqException if the conf file does not exist.

        :rtype: ApiContext
        """

        filename_bunq_config_full = (cls._get_directory_test_root() +
                                     cls._FILENAME_BUNQ_CONFIG)

        try:
            api_context = ApiContext.restore(filename_bunq_config_full)
            endpoint.User.list(api_context)
        except (ApiException, FileNotFoundError):
            api_context = ApiContext(ApiEnvironmentType.SANDBOX, cls._API_KEY,
                                     cls._DEVICE_DESCRIPTION, [])

        api_context.save(filename_bunq_config_full)

        return api_context

    @staticmethod
    def _get_directory_test_root():
        return os.path.dirname(os.path.abspath(__file__))

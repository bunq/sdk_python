import os
import unittest

from bunq import ApiEnvironmentType
from bunq.sdk.context.api_context import ApiContext
from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.json import converter
from bunq.sdk.model.generated.endpoint import OauthClient
from tests.bunq_test import BunqSdkTestCase


class TestPsd2Context(unittest.TestCase):
    """
    Tests:
        Psd2Context
    """

    _FILE_TEST_CONFIGURATION = '/assets/bunq-psd2-test.conf'
    _FILE_TEST_OAUTH = '/assets/bunq-oauth-psd2-test.conf'

    _FILE_TEST_CERTIFICATE = '/assets/cert.pem'
    _FILE_TEST_CERTIFICATE_CHAIN = '/assets/cert.pem'
    _FILE_TEST_PRIVATE_KEY = '/assets/key.pem'

    _TEST_DEVICE_DESCRIPTION = 'PSD2TestDevice'

    @classmethod
    def setUpClass(cls) -> None:
        cls._FILE_MODE_READ = ApiContext._FILE_MODE_READ
        cls._FILE_TEST_CONFIGURATION_PATH_FULL = (
                BunqSdkTestCase._get_directory_test_root() +
                cls._FILE_TEST_CONFIGURATION)
        cls._FILE_TEST_OAUTH_PATH_FULL = (
                BunqSdkTestCase._get_directory_test_root() +
                cls._FILE_TEST_OAUTH)
        cls._FILE_TEST_CERTIFICATE_PATH_FULL = (
                BunqSdkTestCase._get_directory_test_root() +
                cls._FILE_TEST_CERTIFICATE)
        cls._FILE_TEST_CERTIFICATE_CHAIN_PATH_FULL = (
                BunqSdkTestCase._get_directory_test_root() +
                cls._FILE_TEST_CERTIFICATE_CHAIN)
        cls._FILE_TEST_PRIVATE_KEY_PATH_FULL = (
                BunqSdkTestCase._get_directory_test_root() +
                cls._FILE_TEST_PRIVATE_KEY)
        cls.setup_test_data()

    @classmethod
    def setup_test_data(cls) -> None:
        if not os.path.isfile(cls._FILE_TEST_CONFIGURATION_PATH_FULL):
            try:
                BunqContext.load_api_context(cls._create_api_context())
            except FileNotFoundError:
                return

        api_context = ApiContext.restore(cls._FILE_TEST_CONFIGURATION_PATH_FULL)
        BunqContext.load_api_context(api_context)

    def test_create_psd2_context(self) -> None:
        if os.path.isfile(self._FILE_TEST_CONFIGURATION_PATH_FULL):
            return

        try:
            api_context = self._create_api_context()
            BunqContext.load_api_context(api_context)

            self.assertTrue(os.path.isfile(self._FILE_TEST_CONFIGURATION_PATH_FULL))

        except AssertionError:
            raise AssertionError

    def test_create_oauth_client(self) -> None:
        if os.path.isfile(self._FILE_TEST_OAUTH_PATH_FULL):
            return

        try:
            client_id = OauthClient.create().value
            oauth_client = OauthClient.get(client_id).value

            self.assertIsNotNone(oauth_client)

            serialized_client = converter.class_to_json(oauth_client)

            file = open(self._FILE_TEST_OAUTH_PATH_FULL, ApiContext._FILE_MODE_WRITE)
            file.write(serialized_client)
            file.close()

            self.assertTrue(os.path.isfile(self._FILE_TEST_OAUTH_PATH_FULL))

        except AssertionError:
            raise AssertionError

    @classmethod
    def _create_api_context(cls) -> ApiContext:
        with open(cls._FILE_TEST_CERTIFICATE_PATH_FULL, cls._FILE_MODE_READ) as file_:
            certificate = file_.read()

        with open(cls._FILE_TEST_PRIVATE_KEY_PATH_FULL, cls._FILE_MODE_READ) as file_:
            private_key = file_.read()

        with open(cls._FILE_TEST_CERTIFICATE_PATH_FULL, cls._FILE_MODE_READ) as file_:
            all_certificate_chain = file_.read()

        api_context = ApiContext.create_for_psd2(
            ApiEnvironmentType.SANDBOX,
            certificate,
            private_key,
            [all_certificate_chain],
            cls._TEST_DEVICE_DESCRIPTION
        )

        api_context.save(cls._FILE_TEST_CONFIGURATION_PATH_FULL)

        return api_context

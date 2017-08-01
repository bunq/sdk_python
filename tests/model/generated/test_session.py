import unittest
import time

from bunq.sdk.model.generated import Session
from tests.api_context_handler import ApiContextHandler
from tests.config import Config


class TestSession(unittest.TestCase):
    """
    Tests:
        Session
    """

    @classmethod
    def setUpClass(cls):
        cls._SESSION_ID = 0
        cls._API_KEY = Config.get_api_key()
        cls._BUNQ_CONFIG_FILE = "bunq-test.conf"
        cls._DEVICE_DESCRIPTION = 'Python test device'
        cls._API_CONTEXT = ApiContextHandler.get_api_context()

    def test_session_delete(self):
        """
        Tests the deletion and resetting of the current active session

        This test has no assertion as of its testing to see if the code runs
        without errors.

        Notes
        -----
            time.sleep() is needed  as of you can only make 1 POST call to
            Session endpoint per second.
        """

        Session.delete(self._API_CONTEXT, self._SESSION_ID)
        time.sleep(2)
        self._API_CONTEXT.reset_session()
        self._API_CONTEXT.save(self._BUNQ_CONFIG_FILE)

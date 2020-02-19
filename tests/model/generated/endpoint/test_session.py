import time

from bunq.sdk.context.bunq_context import BunqContext
from bunq.sdk.model.generated.endpoint import Session
from tests.bunq_test import BunqSdkTestCase


class TestSession(BunqSdkTestCase):
    """
    Tests:
        Session
    """

    _SESSION_ID = 0
    _BUNQ_CONFIG_FILE = "bunq-test.conf"
    _DEVICE_DESCRIPTION = 'Python test device'

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

        Session.delete(self._SESSION_ID)
        time.sleep(2)
        BunqContext.api_context().reset_session()
        BunqContext.api_context().save(self._BUNQ_CONFIG_FILE)

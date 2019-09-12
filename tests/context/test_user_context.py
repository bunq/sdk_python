from tests.bunq_test import BunqSdkTestCase


class TestUserContext(BunqSdkTestCase):
    """
    Tests:
        UserContext
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._API_CONTEXT = cls._get_api_context()

    def test_build_user_context(self):
        """ Test """


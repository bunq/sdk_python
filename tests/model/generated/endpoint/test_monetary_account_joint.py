import os

from bunq.sdk.model.generated.endpoint import MonetaryAccountJoint
from tests.bunq_test import BunqSdkTestCase


class TestMonetaryAccountJoint(BunqSdkTestCase):
    """
    Tests:
        - MonetaryAccountJoint
        - CoOwner
    """

    _BASE_PATH_JSON_MODEL = '../../../assets/ResponseJsons'
    _MONETARY_ACCOUNT_JOINT_JSON = '/MonetaryAccountJoint.json'
    _FILE_MODE_READ = 'r'

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_monetary_account_joint_parser(self):
        """
        """

        base_path = os.path.dirname(__file__)
        file_path = os.path.abspath(
            os.path.join(base_path,
                         self._BASE_PATH_JSON_MODEL +
                         self._MONETARY_ACCOUNT_JOINT_JSON
                         )
        )

        with open(file_path, self._FILE_MODE_READ) as f:
            json_string = f.read()

        joint_account = MonetaryAccountJoint.from_json(json_string)

        self.assertIsInstance(joint_account, MonetaryAccountJoint)
        self.assertIsNotNone(joint_account)
        self.assertIsNotNone(joint_account.all_co_owner)

        for co_owner in joint_account.all_co_owner:
            self.assertIsNotNone(co_owner.alias)

import unittest
from datetime import datetime
from datetime import timedelta

from bunq.sdk.model.generated.object_ import ShareDetailReadOnly
from bunq.sdk.model.generated.object_ import ShareDetail
from bunq.sdk.model.generated.object_ import DraftShareInviteBankEntry
from bunq.sdk.model.generated.endpoint import DraftShareInviteBank
from bunq.sdk.model.generated.endpoint import DraftShareInviteBankQrCodeContent
from tests.api_context_handler import ApiContextHandler
from tests.config import Config


class TestDraftShareInvite(unittest.TestCase):
    """
    Tests:
        DraftShareInviteBankEntry
        DraftShareInviteBankQrCodeContent
    """

    @classmethod
    def setUpClass(cls):
        cls._OUT_PUT_FILE_PATH = 'connectQr.png'
        cls._WRITE_BYTES = 'wb'
        cls._EXPIRATION_ADDED_TIME = 1
        cls._USER_ID = Config.get_user_id()
        cls._API_CONTEXT = ApiContextHandler.get_api_context()

    def test_draft_share_invite_bank(self):
        """
        Tests the creation of a connect and retrieves the QR code bound to
        this connect.

        This test has no assertion as of its testing to see if the code runs
        without errors
        """

        read_only = ShareDetailReadOnly(True, True, True)
        share_detail = ShareDetail()
        share_detail.read_only = read_only
        share_settings = DraftShareInviteBankEntry(share_detail)
        draft_map = {
            DraftShareInviteBank.FIELD_DRAFT_SHARE_SETTINGS: share_settings,
            DraftShareInviteBank.FIELD_EXPIRATION: self.expiration_date
        }
        draft_id = DraftShareInviteBank.create(self._API_CONTEXT, draft_map,
                                               self._USER_ID)

        connect_qr = DraftShareInviteBankQrCodeContent.list(self._API_CONTEXT,
                                                            self._USER_ID,
                                                            draft_id,)

        with open(self._OUT_PUT_FILE_PATH, self._WRITE_BYTES) as f:
            f.write(connect_qr)

    @property
    def expiration_date(self):
        """
        :rtype: str
        """

        date = datetime.utcnow() + timedelta(hours=self._EXPIRATION_ADDED_TIME)

        return date.isoformat()

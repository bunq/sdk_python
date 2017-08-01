import unittest

from tests.api_context_handler import ApiContextHandler
from tests.config import Config
from bunq.sdk.model.generated.endpoint import AttachmentPublic
from bunq.sdk.model.generated.endpoint import AttachmentPublicContent
from bunq.sdk.client import ApiClient


class TestAttachmentPublic(unittest.TestCase):
    """
    Tests:
        AttachmentPublic
        AttachmentPublicContent
    """

    @classmethod
    def setUpClass(cls):
        # config values
        cls._PATH_TO_ATTACHMENT = '/Users/khellemun/bunq/sdk_python/tests/' \
                                  'assets'
        cls._READ_BYTES = "rb"
        cls._CONTENT_TYPE = Config.get_attachment_content_type()
        cls._ATTACHMENT_DESCRIPTION = Config.get_attachment_description()
        cls._ATTACHMENT_PATH_IN = Config.get_attachment_path_in()
        cls._API_CONTEXT = ApiContextHandler.get_api_context()

    def test_file_upload_and_retrieval(self):
        """
        Tests uploading an attachment, retrieves it and compare them to see
        if the uploaded attachment is indeed the attachment we are getting
        back.
        """

        custom_headers = {
            ApiClient.HEADER_CONTENT_TYPE: self._CONTENT_TYPE,
            ApiClient.HEADER_ATTACHMENT_DESCRIPTION:
                self._ATTACHMENT_DESCRIPTION,
        }

        attachment_uuid = AttachmentPublic.create(self._API_CONTEXT,
                                                  self.attachment_contents,
                                                  custom_headers)

        contents_from_response = AttachmentPublicContent.list(self._API_CONTEXT,
                                                              attachment_uuid)

        self.assertEqual(self.attachment_contents, contents_from_response)

    @property
    def attachment_contents(self):
        """
        :rtype: bytes
        """

        with open(self._PATH_TO_ATTACHMENT + self._ATTACHMENT_PATH_IN,
                  self._READ_BYTES) as f:
            return f.read()

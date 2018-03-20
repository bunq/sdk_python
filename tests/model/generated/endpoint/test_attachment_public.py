from bunq.sdk.client import ApiClient
from bunq.sdk.context import BunqContext
from bunq.sdk.model.generated.endpoint import AttachmentPublic
from bunq.sdk.model.generated.endpoint import AttachmentPublicContent
from tests.bunq_test import BunqSdkTestCase
from tests.config import Config


class TestAttachmentPublic(BunqSdkTestCase):
    """
    Tests:
        AttachmentPublic
        AttachmentPublicContent
    """

    @classmethod
    def setUpClass(cls):
        # config values
        cls._PATH_ATTACHMENT = cls._get_directory_test_root() + '/assets/'
        cls._READ_BYTES = "rb"
        cls._CONTENT_TYPE = Config.get_attachment_content_type()
        cls._ATTACHMENT_DESCRIPTION = Config.get_attachment_description()
        cls._ATTACHMENT_PATH_IN = Config.get_attachment_path_in()

        BunqContext.load_api_context(cls._get_api_context())

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

        attachment_uuid = AttachmentPublic.create(self.attachment_contents,
                                                  custom_headers).value

        contents_from_response = AttachmentPublicContent.list(
            attachment_uuid).value

        self.assertEqual(self.attachment_contents, contents_from_response)

    @property
    def attachment_contents(self):
        """
        :rtype: bytes
        """

        with open(self._PATH_ATTACHMENT + self._ATTACHMENT_PATH_IN,
                  self._READ_BYTES) as f:
            return f.read()

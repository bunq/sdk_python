from typing import AnyStr

from bunq.sdk.http.api_client import ApiClient
from bunq.sdk.model.generated.endpoint import AttachmentPublicContent, AttachmentPublic
from tests.bunq_test import BunqSdkTestCase


class TestAttachmentPublic(BunqSdkTestCase):
    """
    Tests:
        AttachmentPublic
        AttachmentPublicContent
    """

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

        attachment_uuid = AttachmentPublic.create(self.attachment_contents, custom_headers).value
        contents_from_response = AttachmentPublicContent.list(attachment_uuid).value

        self.assertEqual(self.attachment_contents, contents_from_response)

    @property
    def attachment_contents(self) -> AnyStr:
        with open(self._PATH_ATTACHMENT + self._ATTACHMENT_PATH_IN, self._READ_BYTES) as f:
            return f.read()

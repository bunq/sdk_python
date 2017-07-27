#!/usr/bin/env python3

import errno
import os

from bunq.sdk import client
from bunq.sdk import context
from bunq.sdk.model import generated

_CONTENT_TYPE_IMAGE_JPEG = 'image/jpeg'
_DESCRIPTION_TEST_JPG_ATTACHMENT = 'A test JPG attachment.'
_PATH_ATTACHMENT_IN = 'assets/attachment.jpg'
_MODE_READ_BINARY = 'rb'
_PATH_ATTACHMENT_OUT = 'tmp/attachment_out.jpg'
_MODE_WRITE_BINARY = 'wb'


def run():
    api_context = context.ApiContext.restore()
    custom_headers = {
        client.ApiClient.HEADER_CONTENT_TYPE: _CONTENT_TYPE_IMAGE_JPEG,
        client.ApiClient.HEADER_ATTACHMENT_DESCRIPTION:
            _DESCRIPTION_TEST_JPG_ATTACHMENT,
    }

    attachment_bytes = read_attachment_in_bytes()
    attachment_uuid = generated.AttachmentPublic.create(
        api_context,
        attachment_bytes,
        custom_headers
    )
    attachment_bytes2 = generated.AttachmentPublicContent.list(
        api_context,
        attachment_uuid
    )

    if not os.path.exists(os.path.dirname(_PATH_ATTACHMENT_OUT)):
        try:
            os.makedirs(os.path.dirname(_PATH_ATTACHMENT_OUT))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    write_attachment_out_bytes(attachment_bytes2)


def read_attachment_in_bytes():
    """
    :rtype: bytes
    """

    with open(_PATH_ATTACHMENT_IN, _MODE_READ_BINARY) as attachment_file:
        return attachment_file.read()


def write_attachment_out_bytes(bytes_):
    """
    :type bytes_: bytes
    """

    with open(_PATH_ATTACHMENT_OUT, _MODE_WRITE_BINARY) as attachment_file2:
        attachment_file2.write(bytes_)

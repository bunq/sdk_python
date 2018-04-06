import json
import socket

import requests

from bunq.sdk.context import ApiContext, ApiEnvironmentType
from bunq.sdk.exception import BunqException
from bunq.sdk.model.generated import endpoint

_ERROR_COULD_NOT_CREATE_NEW_SANDBOX_USER = "Could not create new sandbox" \
                                           " user."


def automatic_sandbox_install(file_path=None):
    """
    :type file_path: str
    """

    sandbox_user = __generate_new_sandbox_user()
    ApiContext(
        ApiEnvironmentType.SANDBOX,
        sandbox_user.api_key,
        socket.gethostname()
    ).save(file_path)


def __generate_new_sandbox_user():
    """
    :rtype: endpoint.SandboxUser
    """

    url = "https://sandbox.public.api.bunq.com/v1/sandbox-user"

    headers = {
        'x-bunq-client-request-id': "uniqueness-is-required",
        'cache-control': "no-cache",
        'x-bunq-geolocation': "0 0 0 0 NL",
        'x-bunq-language': "en_US",
        'x-bunq-region': "en_US",
    }

    response = requests.request("POST", url, headers=headers)

    if response.status_code is 200:
        response_json = json.loads(response.text)
        return endpoint.SandboxUser.from_json(
            json.dumps(response_json["Response"][0]["ApiKey"]))

    raise BunqException(_ERROR_COULD_NOT_CREATE_NEW_SANDBOX_USER)

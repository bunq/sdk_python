from bunq.sdk.model.generated.endpoint import DeviceServer
from bunq.sdk.model.generated.endpoint import BunqResponseInt
from bunq.sdk import client
from bunq.sdk.json import converter
from bunq.sdk.exception import BunqException


class DeviceServerInternal(DeviceServer):
    _ERROR_API_CONTEXT_IS_NULL = 'ApiContext should not be None,' \
                                 ' use the generated class instead.'

    @classmethod
    def create(cls, description, secret, permitted_ips=None,
               custom_headers=None, api_context=None):
        """
        Create a new DeviceServer providing the installation token in the header
        and signing the request with the private part of the key you used to
        create the installation. The API Key that you are using will be bound to
        the IP address of the DeviceServer which you have
        created.<br/><br/>Using a Wildcard API Key gives you the freedom to make
        API calls even if the IP address has changed after the POST
        device-server.<br/><br/>Find out more at this link <a
        href="https://bunq.com/en/apikey-dynamic-ip"
        target="_blank">https://bunq.com/en/apikey-dynamic-ip</a>.

        :param description: The description of the DeviceServer. This is only
        for your own reference when reading the DeviceServer again.
        :type description: str
        :param secret: The API key. You can request an API key in the bunq app.
        :type secret: str
        :param permitted_ips: An array of IPs (v4 or v6) this DeviceServer will
        be able to do calls from. These will be linked to the API key.
        :type permitted_ips: list[str]
        :type custom_headers: dict[str, str]|None
        :type api_context: context.ApiContext

        :rtype: BunqResponseInt
        """

        if api_context is None:
            raise BunqException(cls._ERROR_API_CONTEXT_IS_NULL)

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_DESCRIPTION: description,
            cls.FIELD_SECRET: secret,
            cls.FIELD_PERMITTED_IPS: permitted_ips
        }

        api_client = client.ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE
        response_raw = api_client.post(endpoint_url, request_bytes,
                                       custom_headers)

        return BunqResponseInt.cast_from_bunq_response(
            cls._process_for_id(response_raw)
        )

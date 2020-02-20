from __future__ import annotations

import json
import typing

from bunq.sdk.http.api_client import ApiClient
from bunq.sdk.json import converter
from bunq.sdk.model.generated.endpoint import PaymentServiceProviderCredential, UserCredentialPasswordIp

if typing.TYPE_CHECKING:
    from bunq.sdk.context.api_context import ApiContext


class PaymentServiceProviderCredentialInternal(PaymentServiceProviderCredential):
    @classmethod
    def create_with_api_context(cls,
                                client_payment_service_provider_certificate: str,
                                client_payment_service_provider_certificate_chain: str,
                                client_public_key_signature: str,
                                api_context: ApiContext,
                                all_custom_header=None) -> UserCredentialPasswordIp:
        request_map = {
            cls.FIELD_CLIENT_PAYMENT_SERVICE_PROVIDER_CERTIFICATE: client_payment_service_provider_certificate,
            cls.FIELD_CLIENT_PAYMENT_SERVICE_PROVIDER_CERTIFICATE_CHAIN: client_payment_service_provider_certificate_chain,
            cls.FIELD_CLIENT_PUBLIC_KEY_SIGNATURE: client_public_key_signature
        }

        if all_custom_header is None:
            all_custom_header = {}

        api_client = ApiClient(api_context)
        request_bytes = converter.class_to_json(request_map).encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE
        response_raw = api_client.post(endpoint_url, request_bytes, all_custom_header)

        response_body = converter.json_to_class(dict, response_raw.body_bytes.decode())
        response_body_dict = converter.deserialize(cls, response_body[cls._FIELD_RESPONSE])[0]

        return UserCredentialPasswordIp.from_json(json.dumps(response_body_dict[cls._OBJECT_TYPE_GET]))

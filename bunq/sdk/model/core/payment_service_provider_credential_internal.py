from __future__ import annotations

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

        return UserCredentialPasswordIp.from_json(response_raw.body_bytes.decode())

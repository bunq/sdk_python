from typing import Type, Dict

from bunq import InstallationContext
from bunq.sdk.json import converter
from bunq.sdk.security import security


class InstallationContextAdapter(converter.JsonAdapter):
    # Attribute/Field constants
    _ATTRIBUTE_TOKEN = '_token'
    _FIELD_TOKEN = 'token'

    _ATTRIBUTE_PRIVATE_KEY_CLIENT = '_private_key_client'
    _FIELD_PRIVATE_KEY_CLIENT = 'private_key_client'

    _ATTRIBUTE_PUBLIC_KEY_CLIENT = '_public_key_client'
    _FIELD_PUBLIC_KEY_CLIENT = 'public_key_client'

    _ATTRIBUTE_PUBLIC_KEY_SERVER = '_public_key_server'
    _FIELD_PUBLIC_KEY_SERVER = 'public_key_server'

    @classmethod
    def deserialize(cls,
                    target_class: Type[InstallationContext],
                    obj: Dict) -> InstallationContext:
        installation_context = target_class.__new__(target_class)
        private_key_client = security.rsa_key_from_string(
            obj[cls._FIELD_PRIVATE_KEY_CLIENT]
        )
        public_key_client = security.rsa_key_from_string(
            obj[cls._FIELD_PUBLIC_KEY_CLIENT]
        )
        public_key_server = security.rsa_key_from_string(
            obj[cls._FIELD_PUBLIC_KEY_SERVER]
        )
        installation_context.__dict__ = {
            cls._ATTRIBUTE_TOKEN: obj[cls._FIELD_TOKEN],
            cls._ATTRIBUTE_PRIVATE_KEY_CLIENT: private_key_client,
            cls._ATTRIBUTE_PUBLIC_KEY_CLIENT: public_key_client,
            cls._ATTRIBUTE_PUBLIC_KEY_SERVER: public_key_server,
        }

        return installation_context

    @classmethod
    def serialize(cls, installation_context: InstallationContext) -> Dict:
        return {
            cls._FIELD_TOKEN: installation_context.token,
            cls._FIELD_PUBLIC_KEY_CLIENT: security.public_key_to_string(
                installation_context.private_key_client.publickey()
            ),
            cls._FIELD_PRIVATE_KEY_CLIENT: security.private_key_to_string(
                installation_context.private_key_client
            ),
            cls._FIELD_PUBLIC_KEY_SERVER: security.public_key_to_string(
                installation_context.public_key_server
            ),
        }

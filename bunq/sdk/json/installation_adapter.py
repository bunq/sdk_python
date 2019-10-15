from typing import Type, List

from bunq.sdk.json import converter
from bunq.sdk.model.core.id import Id
from bunq.sdk.model.core.installation import Installation
from bunq.sdk.model.core.public_key_server import PublicKeyServer
from bunq.sdk.model.core.session_token import SessionToken


class InstallationAdapter(converter.JsonAdapter):
    # Id constants
    _ATTRIBUTE_ID = '_id_'
    _INDEX_ID = 0
    _FIELD_ID = 'Id'

    # Token constants
    _ATTRIBUTE_TOKEN = '_token'
    _INDEX_TOKEN = 1
    _FIELD_TOKEN = 'Token'

    # Server Public Key constants
    _ATTRIBUTE_SERVER_PUBLIC_KEY = '_server_public_key'
    _INDEX_SERVER_PUBLIC_KEY = 2
    _FIELD_SERVER_PUBLIC_KEY = 'ServerPublicKey'

    @classmethod
    def deserialize(cls,
                    target_class: Type[Installation],
                    array: List) -> Installation:
        installation = target_class.__new__(target_class)
        server_public_key_wrapped = array[cls._INDEX_SERVER_PUBLIC_KEY]
        installation.__dict__ = {
            cls._ATTRIBUTE_ID: converter.deserialize(
                Id,
                array[cls._INDEX_ID][cls._FIELD_ID]
            ),
            cls._ATTRIBUTE_TOKEN: converter.deserialize(
                SessionToken,
                array[cls._INDEX_TOKEN][cls._FIELD_TOKEN]
            ),
            cls._ATTRIBUTE_SERVER_PUBLIC_KEY: converter.deserialize(
                PublicKeyServer,
                server_public_key_wrapped[cls._FIELD_SERVER_PUBLIC_KEY]
            ),
        }

        return installation

    @classmethod
    def serialize(cls, installation: Installation) -> List:
        return [
            {cls._FIELD_ID: converter.serialize(installation.id_)},
            {cls._FIELD_TOKEN: converter.serialize(installation.token)},
            {cls._FIELD_SERVER_PUBLIC_KEY: converter.serialize(installation.server_public_key), },
        ]

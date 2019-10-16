from Cryptodome.PublicKey import RSA
from Cryptodome.PublicKey.RSA import RsaKey


class InstallationContext:
    """
    :type _token: str
    :type _private_key_client: RSA.RsaKey
    :type _public_key_server: RSA.RsaKey
    """

    def __init__(self,
                 token: str,
                 private_key_client: RsaKey,
                 public_key_server: RsaKey) -> None:
        self._token = token
        self._private_key_client = private_key_client
        self._public_key_server = public_key_server

    @property
    def token(self) -> str:
        return self._token

    @property
    def private_key_client(self) -> RsaKey:
        return self._private_key_client

    @property
    def public_key_server(self) -> RsaKey:
        return self._public_key_server

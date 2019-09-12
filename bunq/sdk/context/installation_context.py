from Cryptodome.PublicKey import RSA


class InstallationContext(object):
    """
    :type _token: str
    :type _private_key_client: RSA.RsaKey
    :type _public_key_server: RSA.RsaKey
    """

    def __init__(self, token, private_key_client, public_key_server):
        """
        :type token: str
        :type private_key_client: RSA.RsaKey
        :type public_key_server: RSA.RsaKey
        """

        self._token = token
        self._private_key_client = private_key_client
        self._public_key_server = public_key_server

    @property
    def token(self):
        """
        :rtype: str
        """

        return self._token

    @property
    def private_key_client(self):
        """
        :rtype: RSA.RsaKey
        """

        return self._private_key_client

    @property
    def public_key_server(self):
        """
        :rtype: RSA.RsaKey
        """

        return self._public_key_server

from bunq.sdk.model.core.bunq_model import BunqModel


class PublicKeyServer(BunqModel):
    """
    :type _server_public_key: str
    """

    def __init__(self):
        self._server_public_key = None

    @property
    def server_public_key(self):
        """
        :rtype: str
        """

        return self._server_public_key

    def is_all_field_none(self):
        if self.server_public_key is not None:
            return False

        return True

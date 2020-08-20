import aenum


class OauthGrantType(aenum.AutoNumberEnum):
    """
    :type AUTHORIZATION_CODE: str
    :type grant_type: str
    """

    AUTHORIZATION_CODE = 'authorization_code'

    def __init__(self, grant_type: str) -> None:
        self._grant_type = grant_type

    @property
    def grant_type(self) -> str:
        return self.grant_type

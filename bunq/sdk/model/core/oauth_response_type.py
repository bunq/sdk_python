import aenum


class OauthResponseType(aenum.AutoNumberEnum):
    """
    :type CODE: str
    :type response_type: str
    """

    CODE = 'code'

    def __init__(self, response_type: str) -> None:
        self._response_type = response_type

    @property
    def response_type(self) -> str:
        return self._response_type

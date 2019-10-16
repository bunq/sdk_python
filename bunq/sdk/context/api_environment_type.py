import aenum


class ApiEnvironmentType(aenum.AutoNumberEnum):
    """
    :type PRODUCTION: ApiEnvironmentType
    :type SANDBOX: ApiEnvironmentType
    :type uri_base: str
    """

    PRODUCTION = 'https://api.bunq.com/v1/'
    SANDBOX = 'https://public-api.sandbox.bunq.com/v1/'

    def __init__(self, uri_base: str) -> None:
        self._uri_base = uri_base

    @property
    def uri_base(self) -> str:
        return self._uri_base

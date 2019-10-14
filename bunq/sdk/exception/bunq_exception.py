class BunqException(Exception):
    def __init__(self, message: str) -> None:
        """

        :param message:
        """

        super(BunqException, self).__init__(message)

class BunqException(Exception):
    def __init__(self, message: str) -> None:
        super(BunqException, self).__init__(message)

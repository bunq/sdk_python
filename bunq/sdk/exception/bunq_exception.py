class BunqException(Exception):
    def __init__(self, message):
        super(BunqException, self).__init__(message)

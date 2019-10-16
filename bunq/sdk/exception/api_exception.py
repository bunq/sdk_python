class ApiException(Exception):
    def __init__(self,
                 message: str,
                 response_code: int,
                 response_id: str) -> None:
        self._response_id = response_id
        self._message = message
        self._response_code = response_code

        super(ApiException, self).__init__(message)

    @property
    def message(self) -> str:
        return self._message

    @property
    def response_code(self) -> int:
        return self._response_code

    @property
    def response_id(self) -> str:
        return self._response_id

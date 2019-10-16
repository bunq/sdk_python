import datetime


class SessionContext:
    """
    :type _token: str
    :type _expiry_time: datetime.datetime
    :type _user_id: int
    """

    def __init__(self,
                 token: str,
                 expiry_time: datetime.datetime,
                 user_id: int) -> None:
        self._token = token
        self._expiry_time = expiry_time
        self._user_id = user_id

    @property
    def token(self) -> str:
        return self._token

    @property
    def expiry_time(self) -> datetime.datetime:
        return self._expiry_time

    @property
    def user_id(self) -> int:
        return self._user_id

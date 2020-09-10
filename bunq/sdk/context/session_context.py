import datetime

from bunq.sdk.model.core.session_server import SessionServer


class SessionContext:
    def __init__(self, session_server: SessionServer) -> None:
        self._token = session_server.token.token
        self._expiry_time = self._get_expiry_timestamp(session_server)
        self._user_id = session_server.get_referenced_user().id_
        self._user = session_server.get_referenced_user()

    @property
    def token(self) -> str:
        return self._token

    @property
    def expiry_time(self) -> datetime.datetime:
        return self._expiry_time

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def user(self):
        return self._user

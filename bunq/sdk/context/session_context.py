import datetime


class SessionContext(object):
    """
    :type _token: str
    :type _expiry_time: datetime.datetime
    :type _user_id: int
    """

    def __init__(self, token, expiry_time, user_id):
        """
        :type token: str
        :type expiry_time: datetime.datetime
        """

        self._token = token
        self._expiry_time = expiry_time
        self._user_id = user_id

    @property
    def token(self):
        """
        :rtype: str
        """

        return self._token

    @property
    def expiry_time(self):
        """
        :rtype: datetime.datetime
        """

        return self._expiry_time

    @property
    def user_id(self):
        return self._user_id

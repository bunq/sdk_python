from bunq.sdk.exception.exception import BunqException
from bunq.sdk.model import core
from bunq.sdk.model.generated import endpoint


class UserContext(object):
    _ERROR_UNEXPECTED_USER_INSTANCE = '"{}" is unexpected user instance.'
    _ERROR_NO_ACTIVE_MONETARY_ACCOUNT_FOUND = \
        'No active monetary account found.'
    _STATUS_ACTIVE = 'ACTIVE'

    def __init__(self, user_id):
        """
        :type user_id: int
        """

        self._user_id = user_id
        self._user_person = None
        self._user_company = None
        self._user_api_key = None
        self._primary_monetary_account = None

        self._set_user(self.__get_user_object())

    @staticmethod
    def __get_user_object():
        """
        :rtype: core.BunqModel
        """

        return endpoint.User.list().value[0].get_referenced_object()

    def _set_user(self, user):
        if isinstance(user, endpoint.UserPerson):
            self._user_person = user

        elif isinstance(user, endpoint.UserCompany):
            self._user_company = user

        elif isinstance(user, endpoint.UserApiKey):
            self._user_api_key = user

        else:
            raise BunqException(
                self._ERROR_UNEXPECTED_USER_INSTANCE.format(user.__class__))

    def init_main_monetary_account(self):
        all_monetary_account = endpoint.MonetaryAccountBank.list().value

        for account in all_monetary_account:
            if account.status == self._STATUS_ACTIVE:
                self._primary_monetary_account = account

                return

        raise BunqException(self._ERROR_NO_ACTIVE_MONETARY_ACCOUNT_FOUND)

    @property
    def user_id(self):
        return self._user_id

    def is_only_user_person_set(self):
        """
        :rtype: bool
        """

        return self._user_person is not None \
            and self._user_company is None \
            and self._user_api_key is None

    def is_only_user_company_set(self):
        """
        :rtype: bool
        """

        return self._user_company is not None \
            and self._user_person is None \
            and self._user_api_key is None

    def is_only_user_api_key_set(self):
        """
        :rtype: bool
        """

        return self._user_api_key is not None \
            and self._user_company is None \
            and self._user_person is None

    def is_all_user_type_set(self):
        """
        :rtype: bool
        """

        return self._user_company is not None \
            and self._user_person is not None \
            and self._user_api_key is not None

    def refresh_user_context(self):
        """
        """

        self._set_user(self.__get_user_object())
        self.init_main_monetary_account()

    @property
    def user_company(self):
        """
        :rtype: endpoint.UserCompany
        """

        return self._user_company

    @property
    def user_person(self):
        """
        :rtype: endpoint.UserPerson
        """

        return self._user_person

    @property
    def user_api_key(self):
        """
        :rtype: endpoint.UserApiKey
        """

        return self._user_api_key

    @property
    def primary_monetary_account(self):
        """
        :rtype: endpoint.MonetaryAccountBank
        """

        return self._primary_monetary_account

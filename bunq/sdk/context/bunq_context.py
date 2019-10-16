from bunq.sdk.context.api_context import ApiContext
from bunq.sdk.context.user_context import UserContext
from bunq.sdk.exception.bunq_exception import BunqException


class BunqContext:
    _ERROR_CLASS_SHOULD_NOT_BE_INITIALIZED = 'This class should not be instantiated'
    _ERROR_API_CONTEXT_HAS_NOT_BEEN_LOADED = 'ApiContext has not been loaded. Please load ApiContext in BunqContext'
    _ERROR_USER_CONTEXT_HAS_NOT_BEEN_LOADED = 'UserContext has not been loaded, please load this by loading ApiContext.'

    _api_context = None
    _user_context = None

    def __init__(self) -> None:
        raise TypeError(self._ERROR_CLASS_SHOULD_NOT_BE_INITIALIZED)

    @classmethod
    def load_api_context(cls, api_context: ApiContext) -> None:
        cls._api_context = api_context
        cls._user_context = UserContext(api_context.session_context.user_id)
        cls._user_context.init_main_monetary_account()

    @classmethod
    def api_context(cls) -> ApiContext:
        if cls._api_context is not None:
            return cls._api_context

        raise BunqException(cls._ERROR_API_CONTEXT_HAS_NOT_BEEN_LOADED)

    @classmethod
    def user_context(cls) -> UserContext:
        if cls._user_context is not None:
            return cls._user_context

        raise BunqException(cls._ERROR_USER_CONTEXT_HAS_NOT_BEEN_LOADED)

    @classmethod
    def update_api_context(cls, api_context: ApiContext) -> None:
        cls._api_context = api_context

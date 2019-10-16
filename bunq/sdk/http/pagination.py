from typing import Dict

from bunq.sdk.exception.bunq_exception import BunqException


class Pagination:
    """
    :type older_id: int|None
    :type newer_id: int|None
    :type future_id: int|None
    :type count: int|None
    """

    # Error constants
    _ERROR_NO_PREVIOUS_PAGE = 'Could not generate previous page URL params: there is no previous page.'
    _ERROR_NO_NEXT_PAGE = 'Could not generate next page URL params: there is no next page.'

    # URL Param constants
    PARAM_OLDER_ID = 'older_id'
    PARAM_NEWER_ID = 'newer_id'
    PARAM_COUNT = 'count'

    def __init__(self) -> None:
        self.older_id = None
        self.newer_id = None
        self.future_id = None
        self.count = None

    @property
    def url_params_previous_page(self) -> Dict[str, str]:
        self.assert_has_previous_page()

        params = {self.PARAM_OLDER_ID: str(self.older_id)}
        self._add_count_to_params_if_needed(params)

        return params

    def assert_has_previous_page(self) -> None:
        """

        :raise: BunqException
        """

        if not self.has_previous_page():
            raise BunqException(self._ERROR_NO_PREVIOUS_PAGE)

    def has_previous_page(self) -> bool:
        return self.older_id is not None

    @property
    def url_params_count_only(self) -> Dict[str, str]:
        params = {}
        self._add_count_to_params_if_needed(params)

        return params

    def _add_count_to_params_if_needed(self, params: Dict[str, str]) -> None:
        if self.count is not None:
            params[self.PARAM_COUNT] = str(self.count)

    def has_next_page_assured(self) -> bool:
        return self.newer_id is not None

    @property
    def url_params_next_page(self) -> Dict[str, str]:
        self.assert_has_next_page()

        params = {self.PARAM_NEWER_ID: str(self._next_id)}
        self._add_count_to_params_if_needed(params)

        return params

    def assert_has_next_page(self) -> None:
        """

        :raise: BunqException
        """

        if self._next_id is None:
            raise BunqException(self._ERROR_NO_NEXT_PAGE)

    @property
    def _next_id(self) -> int:
        if self.has_next_page_assured():
            return self.newer_id

        return self.future_id

from abc import ABC

from bunq.sdk.model.core.bunq_model import BunqModel


class Uuid(BunqModel, ABC):
    """
    :type _uuid: str
    """

    def __init__(self):
        self._uuid = None

    @property
    def uuid(self):
        """
        :rtype: str
        """

        return self._uuid

    def is_all_field_none(self):
        if self.uuid is not None:
            return False

        return True

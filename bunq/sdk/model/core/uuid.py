from bunq.sdk.model.core.bunq_model import BunqModel


class Uuid(BunqModel):
    """
    :type _uuid: str
    """

    def __init__(self) -> None:
        self._uuid = None

    @property
    def uuid(self) -> str:
        return self._uuid

    def is_all_field_none(self) -> bool:
        if self.uuid is not None:
            return False

        return True

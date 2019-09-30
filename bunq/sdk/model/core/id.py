from bunq.sdk.model.core.bunq_model import BunqModel


class Id(BunqModel):
    """
    :type _id_: int
    """

    def __init__(self):
        self._id_ = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    def is_all_field_none(self):
        if self.id_ is not None:
            return False

        return True

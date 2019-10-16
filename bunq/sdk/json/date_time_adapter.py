import datetime
from typing import Type

from bunq.sdk.json import converter


class DateTimeAdapter(converter.JsonAdapter):
    # bunq timestamp format
    _FORMAT_TIMESTAMP = '%Y-%m-%d %H:%M:%S.%f'

    @classmethod
    def deserialize(cls,
                    target_class: Type[datetime.datetime],
                    string: str) -> datetime.datetime:
        return target_class.strptime(string, cls._FORMAT_TIMESTAMP)

    @classmethod
    def serialize(cls, timestamp: datetime.datetime) -> str:
        return timestamp.strftime(cls._FORMAT_TIMESTAMP)

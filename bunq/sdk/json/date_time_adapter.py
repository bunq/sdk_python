import datetime

from bunq.sdk.json import converter


class DateTimeAdapter(converter.JsonAdapter):
    # bunq timestamp format
    _FORMAT_TIMESTAMP = '%Y-%m-%d %H:%M:%S.%f'

    @classmethod
    def deserialize(cls, target_class, string):
        """
        :type target_class: datetime.datetime|type
        :type string: str

        :rtype: datetime.datetime
        """

        return target_class.strptime(string, cls._FORMAT_TIMESTAMP)

    @classmethod
    def serialize(cls, timestamp):
        """
        :type timestamp: datetime.datetime

        :rtype: dict
        """

        return timestamp.strftime(cls._FORMAT_TIMESTAMP)



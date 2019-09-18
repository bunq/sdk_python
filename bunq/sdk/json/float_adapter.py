from bunq.sdk.json import converter


class FloatAdapter(converter.JsonAdapter):
    # Precision to round the floats to before outputting them
    _PRECISION_FLOAT = 2

    @classmethod
    def deserialize(cls, target_class, string):
        """
        :type target_class: float|type
        :type string: str

        :rtype: float
        """

        _ = target_class

        return float(string)

    @classmethod
    def serialize(cls, number):
        """
        :type number: float

        :rtype: str
        """

        return str(round(number, cls._PRECISION_FLOAT))


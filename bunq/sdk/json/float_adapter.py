from typing import Type

from bunq.sdk.json import converter


class FloatAdapter(converter.JsonAdapter):
    # Precision to round the floats to before outputting them
    _PRECISION_FLOAT = 2

    @classmethod
    def deserialize(cls,
                    target_class: Type[float],
                    string: str) -> float:
        _ = target_class

        return float(string)

    @classmethod
    def serialize(cls, number: float) -> str:
        return str(round(number, cls._PRECISION_FLOAT))

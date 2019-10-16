from typing import Type, Dict

from bunq.sdk.json import converter
from bunq.sdk.model.generated.object_ import Geolocation


class GeolocationAdapter(converter.JsonAdapter):
    # Field constants
    _FIELD_LATITUDE = 'latitude'
    _FIELD_LONGITUDE = 'longitude'
    _FIELD_ALTITUDE = 'altitude'
    _FIELD_RADIUS = 'radius'

    @classmethod
    def can_deserialize(cls) -> bool:
        return False

    @classmethod
    def deserialize(cls,
                    target_class: Type[float],
                    obj: Dict) -> None:
        """

        :raise: NotImplementedError
        """

        raise NotImplementedError()

    @classmethod
    def serialize(cls, geolocation: Geolocation) -> Dict:
        obj = {}

        cls.add_if_not_none(obj, cls._FIELD_LATITUDE, geolocation.latitude)
        cls.add_if_not_none(obj, cls._FIELD_LONGITUDE, geolocation.longitude)
        cls.add_if_not_none(obj, cls._FIELD_ALTITUDE, geolocation.altitude)
        cls.add_if_not_none(obj, cls._FIELD_RADIUS, geolocation.radius)

        return obj

    @classmethod
    def add_if_not_none(cls,
                        dict_: Dict[str, str],
                        key: str,
                        value: float) -> None:
        if value is not None:
            dict_[key] = str(value)

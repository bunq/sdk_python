from bunq.sdk.json import converter
from bunq.sdk.model.generated import object_


class GeolocationAdapter(converter.JsonAdapter):
    # Field constants
    _FIELD_LATITUDE = 'latitude'
    _FIELD_LONGITUDE = 'longitude'
    _FIELD_ALTITUDE = 'altitude'
    _FIELD_RADIUS = 'radius'

    @classmethod
    def can_deserialize(cls):
        """
        :rtype: bool
        """

        return False

    @classmethod
    def deserialize(cls, target_class, obj):
        """
        :type target_class: float|type
        :type obj: dict

        :raise: NotImplementedError
        """

        raise NotImplementedError()

    @classmethod
    def serialize(cls, geolocation):
        """
        :type geolocation: object_.Geolocation

        :rtype: dict
        """

        obj = {}

        cls.add_if_not_none(obj, cls._FIELD_LATITUDE, geolocation.latitude)
        cls.add_if_not_none(obj, cls._FIELD_LONGITUDE, geolocation.longitude)
        cls.add_if_not_none(obj, cls._FIELD_ALTITUDE, geolocation.altitude)
        cls.add_if_not_none(obj, cls._FIELD_RADIUS, geolocation.radius)

        return obj

    @classmethod
    def add_if_not_none(cls, dict_, key, value):
        """
        :type dict_: dict[str, str]
        :type key: str
        :type value: float

        :rtype: None
        """

        if value is not None:
            dict_[key] = str(value)

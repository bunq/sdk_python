from bunq.sdk.context.api_environment_type import ApiEnvironmentType
from bunq.sdk.json import converter


class ApiEnvironmentTypeAdapter(converter.JsonAdapter):
    @classmethod
    def deserialize(cls, target_class, name):
        """
        :type target_class: ApiEnvironmentType|type
        :type name: str

        :rtype: context.ApiEnvironmentType
        """

        return ApiEnvironmentType[name]

    @classmethod
    def serialize(cls, api_environment_type):
        """
        :type api_environment_type: ApiEnvironmentType

        :rtype: str
        """

        return api_environment_type.name

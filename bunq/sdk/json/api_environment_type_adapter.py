from bunq.sdk.context import api_context
from bunq.sdk.json import converter


class ApiEnvironmentTypeAdapter(converter.JsonAdapter):
    @classmethod
    def deserialize(cls, target_class, name):
        """
        :type target_class: api_context.ApiEnvironmentType|type
        :type name: str

        :rtype: context.ApiEnvironmentType
        """

        _ = target_class

        return api_context.ApiEnvironmentType[name]

    @classmethod
    def serialize(cls, api_environment_type):
        """
        :type api_environment_type: api_context.ApiEnvironmentType

        :rtype: str
        """

        return api_environment_type.name

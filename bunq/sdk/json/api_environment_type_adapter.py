from typing import Type

from bunq.sdk.context.api_environment_type import ApiEnvironmentType
from bunq.sdk.json import converter


class ApiEnvironmentTypeAdapter(converter.JsonAdapter):
    @classmethod
    def deserialize(cls,
                    target_class: Type[ApiEnvironmentType],
                    name: str) -> ApiEnvironmentType:
        return ApiEnvironmentType[name]

    @classmethod
    def serialize(cls, api_environment_type: ApiEnvironmentType) -> str:
        return api_environment_type.name

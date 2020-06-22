from typing import Type

from bunq.sdk.context.api_environment_type import ApiEnvironmentType
from bunq.sdk.context.installation_context import InstallationContext
from bunq.sdk.http.pagination import Pagination
from bunq.sdk.json import converter
from bunq.sdk.model.core.anchor_object_interface import AnchorObjectInterface
from bunq.sdk.util.type_alias import T


def initialize_converter() -> None:
    import datetime
    import inspect

    from bunq.sdk.http import api_client
    from bunq.sdk.context import api_context
    from bunq.sdk.json import converter
    from bunq.sdk.model.generated import object_
    from bunq.sdk.model.generated import endpoint
    from bunq.sdk.model.core.installation import Installation
    from bunq.sdk.model.core.session_server import SessionServer
    from bunq.sdk.json.installation_adapter import InstallationAdapter
    from bunq.sdk.json.session_server_adapter import SessionServerAdapter
    from bunq.sdk.json.installation_context_adapter import InstallationContextAdapter
    from bunq.sdk.json.api_environment_type_adapter import ApiEnvironmentTypeAdapter
    from bunq.sdk.json.float_adapter import FloatAdapter
    from bunq.sdk.json.geolocation_adapter import GeolocationAdapter
    from bunq.sdk.json.monetary_account_reference_adapter import MonetaryAccountReferenceAdapter
    from bunq.sdk.json.share_detail_adapter import ShareDetailAdapter
    from bunq.sdk.json.date_time_adapter import DateTimeAdapter
    from bunq.sdk.json.pagination_adapter import PaginationAdapter
    from bunq.sdk.json.anchor_object_adapter import AnchorObjectAdapter

    converter.register_adapter(Installation, InstallationAdapter)
    converter.register_adapter(SessionServer, SessionServerAdapter)
    converter.register_adapter(InstallationContext, InstallationContextAdapter)
    converter.register_adapter(ApiEnvironmentType, ApiEnvironmentTypeAdapter)
    converter.register_adapter(float, FloatAdapter)
    converter.register_adapter(object_.Geolocation, GeolocationAdapter)
    converter.register_adapter(object_.MonetaryAccountReference, MonetaryAccountReferenceAdapter)
    converter.register_adapter(object_.ShareDetail, ShareDetailAdapter)
    converter.register_adapter(datetime.datetime, DateTimeAdapter)
    converter.register_adapter(Pagination, PaginationAdapter)

    def register_anchor_adapter(class_to_register: Type[T]) -> None:
        if issubclass(class_to_register, AnchorObjectInterface):
            converter.register_adapter(class_to_register, AnchorObjectAdapter)

    def get_class(class_string_to_get: str) -> Type[T]:
        if hasattr(object_, class_string_to_get):
            return getattr(object_, class_string_to_get)

        if hasattr(endpoint, class_string_to_get):
            return getattr(endpoint, class_string_to_get)

    for class_string in list(dir(object_) + dir(endpoint)):
        class_ = get_class(class_string)

        if not inspect.isclass(class_):
            continue

        register_anchor_adapter(class_)


converter.set_initializer_function(initialize_converter)

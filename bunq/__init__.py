from bunq.sdk.json import converter


def initialize_converter():
    """
    :rtype: None
    """

    import datetime
    import inspect

    from bunq.sdk import client
    from bunq.sdk import context
    from bunq.sdk.model import core
    from bunq.sdk.json import adapters
    from bunq.sdk.json import converter
    from bunq.sdk.model.generated import object_
    from bunq.sdk.model.generated import endpoint

    converter.register_adapter(core.Installation, adapters.InstallationAdapter)
    converter.register_adapter(
        core.SessionServer,
        adapters.SessionServerAdapter
    )
    converter.register_adapter(
        context.InstallationContext,
        adapters.InstallationContextAdapter
    )
    converter.register_adapter(
        context.ApiEnvironmentType,
        adapters.ApiEnvironmentTypeAdapter
    )
    converter.register_adapter(float, adapters.FloatAdapter)
    converter.register_adapter(object_.Geolocation, adapters.GeolocationAdapter)
    converter.register_adapter(
        object_.MonetaryAccountReference,
        adapters.MonetaryAccountReferenceAdapter
    )
    converter.register_adapter(object_.ShareDetail, adapters.ShareDetailAdapter)
    converter.register_adapter(datetime.datetime, adapters.DateTimeAdapter)
    converter.register_adapter(client.Pagination, adapters.PaginationAdapter)

    def register_anchor_adapter(class_to_regsiter):
        if issubclass(class_to_regsiter, core.AnchoredObjectInterface):
            converter.register_adapter(
                class_to_regsiter,
                adapters.AnchoredObjectModelAdapter
            )

    def get_class(class_string_to_get):
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

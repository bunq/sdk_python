from bunq.sdk.json import converter


def initialize_converter():
    """
    :rtype: None
    """

    import datetime

    from bunq.sdk import client
    from bunq.sdk import context
    from bunq.sdk.model import core
    from bunq.sdk.json import adapters
    from bunq.sdk.json import converter
    from bunq.sdk.model.generated import object_
    from bunq.sdk.model.generated import endpoint
    import inspect

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
    # converter.register_adapter(core.AnchoredObjectInterface,
    #                            adapters.AnchoredObjectModelAdapter)

    for class_string in dir(object_):
        class_ = getattr(object_, class_string)

        if not inspect.isclass(class_):
            continue

        if issubclass(class_, core.AnchoredObjectInterface):
            converter.register_adapter(
                class_,
                adapters.AnchoredObjectModelAdapter
            )

    for class_string in dir(endpoint):
        class_ = getattr(endpoint, class_string)

        if not inspect.isclass(class_):
            continue

        if issubclass(class_, core.AnchoredObjectInterface):
            converter.register_adapter(
                class_,
                adapters.AnchoredObjectModelAdapter
            )


converter.set_initializer_function(initialize_converter)

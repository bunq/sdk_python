from bunq.sdk.json import converter


def create_converter_initializer():
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

    is_initialized = False

    if not is_initialized:
        converter.register_adapter(core.Installation,
                                   adapters.InstallationAdapter)
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
        converter.register_adapter(
            object_.Geolocation,
            adapters.GeolocationAdapter
        )
        converter.register_adapter(
            object_.MonetaryAccountReference,
            adapters.MonetaryAccountReferenceAdapter
        )
        converter.register_adapter(object_.ShareDetail,
                                   adapters.ShareDetailAdapter)
        converter.register_adapter(datetime.datetime,
                                   adapters.DateTimeAdapter)
        converter.register_adapter(client.Pagination,
                                   adapters.PaginationAdapter)
        is_initialized = True

    yield is_initialized

converter.set_initializer(create_converter_initializer())

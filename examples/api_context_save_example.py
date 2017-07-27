#!/usr/bin/env python3

from bunq.sdk import context
from bunq.sdk.json import converter


def run():
    ctx = context.ApiContext(
        context.ApiEnvironmentType.SANDBOX,
        '###YOUR_API_KEY###',  # Put your API key here
        'test device python'
    )

    ctx.save()
    ctx_restored = context.ApiContext.restore()
    print('Is original context equal the one saved and restored?:',
          converter.class_to_json(ctx) == converter.class_to_json(ctx_restored))

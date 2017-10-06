#!/usr/bin/env python3

from bunq.sdk import context
from bunq.sdk.model.generated import endpoint


def run():
    api_context = context.ApiContext.restore()
    users = endpoint.User.list(api_context).value
    api_context.save()

    for user in users:
        print(user.to_json())

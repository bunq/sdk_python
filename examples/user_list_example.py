#!/usr/bin/env python3

from bunq.sdk import context
from bunq.sdk.model import generated


def run():
    api_context = context.ApiContext.restore()
    users = generated.User.list(api_context)
    api_context.save()

    for user in users:
        print(user.UserCompany.to_json())

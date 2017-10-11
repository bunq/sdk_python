#!/usr/bin/env python3

from bunq.sdk import context
from bunq.sdk.model.generated import endpoint

_USER_ITEM_ID = 0  # Put your user ID here
_MONETARY_ACCOUNT_ITEM_ID = 0  # Put your monetary account ID here


def run():
    api_context = context.ApiContext.restore()
    monetary_account = endpoint.MonetaryAccountBank.get(
        api_context,
        _USER_ITEM_ID,
        _MONETARY_ACCOUNT_ITEM_ID
    )
    print(monetary_account.value.to_json())

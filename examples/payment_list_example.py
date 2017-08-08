#!/usr/bin/env python3

from bunq.sdk import context
from bunq.sdk.model import generated

_USER_ITEM_ID = 0  # Put your user ID here
_MONETARY_ACCOUNT_ITEM_ID = 0  # Put your monetary account ID here


def run():
    api_context = context.ApiContext.restore()
    payments = generated.Payment.list(
        api_context,
        _USER_ITEM_ID,
        _MONETARY_ACCOUNT_ITEM_ID,
    ).value

    for payment in payments:
        print(payment.id_)

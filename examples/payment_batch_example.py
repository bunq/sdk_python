#!/usr/bin/env python3

from bunq.sdk import context
from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated import object_

_PAYMENT_AMOUNT = '0.01'
_PAYMENT_CURRENCY = 'EUR'
_COUNTERPARTY_POINTER_TYPE = 'EMAIL'
_COUNTERPARTY_EMAIL = 'bravo@bunq.com'  # Put your counterparty email here
_PAYMENT_DESCRIPTION = 'This is a generated payment batch!'
_USER_ITEM_ID = 0  # Put your user ID here
_MONETARY_ACCOUNT_ITEM_ID = 0  # Put your monetary account ID here


def run():
    api_context = context.ApiContext.restore()
    request_map = {
        endpoint.PaymentBatch.FIELD_PAYMENTS: [
            {
                endpoint.Payment.FIELD_AMOUNT: object_.Amount(
                    _PAYMENT_AMOUNT,
                    _PAYMENT_CURRENCY),
                endpoint.Payment.FIELD_COUNTERPARTY_ALIAS: object_.Pointer(
                    _COUNTERPARTY_POINTER_TYPE,
                    _COUNTERPARTY_EMAIL
                ),
                endpoint.Payment.FIELD_DESCRIPTION: _PAYMENT_DESCRIPTION,
            }
        ]
    }

    payment_id = endpoint.PaymentBatch.create(
        api_context,
        request_map,
        _USER_ITEM_ID,
        _MONETARY_ACCOUNT_ITEM_ID
    ).value

    print(
        endpoint.PaymentBatch.get(
            api_context,
            _USER_ITEM_ID,
            _MONETARY_ACCOUNT_ITEM_ID,
            payment_id
        ).value.to_json()
    )

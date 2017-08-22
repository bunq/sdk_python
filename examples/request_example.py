#!/usr/bin/env python3

from bunq.sdk import context
from bunq.sdk.model import generated
from bunq.sdk.model.generated import object_

_REQUEST_AMOUNT = '0.01'
_REQUEST_CURRENCY = 'EUR'
_COUNTERPARTY_POINTER_TYPE = 'EMAIL'
_COUNTERPARTY_EMAIL = 'bravo@bunq.com'
_REQUEST_DESCRIPTION = 'This is a generated request!'
_USER_ITEM_ID = 0  # Put your user ID here
_MONETARY_ACCOUNT_ITEM_ID = 0  # Put your monetary account ID here
_STATUS_REVOKED = 'REVOKED'


def run():
    api_context = context.ApiContext.restore()
    request_map = {
        generated.RequestInquiry.FIELD_AMOUNT_INQUIRED: object_.Amount(
            _REQUEST_AMOUNT,
            _REQUEST_CURRENCY
        ),
        generated.RequestInquiry.FIELD_COUNTERPARTY_ALIAS: object_.Pointer(
            _COUNTERPARTY_POINTER_TYPE,
            _COUNTERPARTY_EMAIL
        ),
        generated.RequestInquiry.FIELD_DESCRIPTION: _REQUEST_DESCRIPTION,
        generated.RequestInquiry.FIELD_ALLOW_BUNQME: True,
    }
    request_id = generated.RequestInquiry.create(
        api_context,
        request_map,
        _USER_ITEM_ID,
        _MONETARY_ACCOUNT_ITEM_ID
    ).value
    print(
        generated.RequestInquiry.get(
            api_context,
            _USER_ITEM_ID,
            _MONETARY_ACCOUNT_ITEM_ID,
            request_id
        ).value.to_json()
    )

    request_update_map = {
        generated.RequestInquiry.FIELD_STATUS: _STATUS_REVOKED,
    }
    print(
        generated.RequestInquiry.update(
            api_context,
            request_update_map,
            _USER_ITEM_ID,
            _MONETARY_ACCOUNT_ITEM_ID,
            request_id
        ).value.to_json()
    )

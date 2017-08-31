#!/usr/bin/env python3

from bunq.sdk import client
from bunq.sdk import context
from bunq.sdk.model import generated

# Console messages
_MESSAGE_LATEST_PAGE_IDS = 'Latest page IDs:'
_MESSAGE_SECOND_LATEST_PAGE_IDS = 'Second latest page IDs:'

# Size of page of payments to list
_PAGE_SIZE = 3

_USER_ITEM_ID = 0  # Put your user ID here
_MONETARY_ACCOUNT_ITEM_ID = 0  # Put your monetary account ID here


def run():
    api_context = context.ApiContext.restore()
    pagination = client.Pagination()
    pagination.count = _PAGE_SIZE
    payments_response = generated.Payment.list(
        api_context,
        _USER_ITEM_ID,
        _MONETARY_ACCOUNT_ITEM_ID,
        pagination.url_params_count_only
    )

    print(_MESSAGE_LATEST_PAGE_IDS)

    for payment in payments_response.value:
        print(payment.id_)

    payments_response_previous = generated.Payment.list(
        api_context,
        _USER_ITEM_ID,
        _MONETARY_ACCOUNT_ITEM_ID,
        payments_response.pagination.url_params_previous_page
    )

    print(_MESSAGE_SECOND_LATEST_PAGE_IDS)

    for payment in payments_response_previous.value:
        print(payment.id_)

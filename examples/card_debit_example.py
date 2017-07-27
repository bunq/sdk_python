#!/usr/bin/env python3

import random
import string

from bunq.sdk import context
from bunq.sdk.model import generated
from bunq.sdk.model.generated import object_

# Empty string to join the random values of second string
_STRING_EMPTY = ''

# Example constants
_POINTER_TYPE_EMAIL = 'EMAIL'
_EMAIL_YOUR_COMPANY = 'COMPANY_EMAIL_HERE'  # Put your company email here
_NAME_YOUR_COMPANY = 'COMPANY_NAME_HERE'  # Put your company name here
_USER_ITEM_ID = 0  # Put your user ID here
_PIN_CODE = '9922'
_POINTER_NAME_TEST = 'test pointer'
_SECOND_LINE_LENGTH_MAXIMUM = 20


def run():
    api_context = context.ApiContext.restore()
    pointer = object_.Pointer(_POINTER_TYPE_EMAIL, _EMAIL_YOUR_COMPANY)
    pointer.name = _POINTER_NAME_TEST
    request_map = {
        generated.CardDebit.FIELD_ALIAS: pointer,
        generated.CardDebit.FIELD_NAME_ON_CARD: _NAME_YOUR_COMPANY,
        generated.CardDebit.FIELD_PIN_CODE: _PIN_CODE,
        generated.CardDebit.FIELD_SECOND_LINE: _make_second_line()
    }

    print(generated.CardDebit.create(api_context, request_map,
                                     _USER_ITEM_ID).to_json())


def _make_second_line():
    second_line_characters = []

    for _ in range(_SECOND_LINE_LENGTH_MAXIMUM):
        next_char = random.choice(string.ascii_uppercase)
        second_line_characters.append(next_char)

    return _STRING_EMPTY.join(second_line_characters)

#!/usr/bin/env python3
import datetime

from bunq.sdk import context
from bunq.sdk.model import generated

# Desired format of customer statement
_CUSTOMER_STATEMENT_FORMAT = 'PDF'

# Number of days in a week
_DAYS_IN_WEEK = 7

# Date format required for customer statement export endpoint
_FORMAT_DATE = '%Y-%m-%d'

# Index of the very first item in an array
_INDEX_FIRST = 0


def run():
    api_context = context.ApiContext.restore()
    user_id = generated.User.list(api_context).value[_INDEX_FIRST]\
        .UserCompany.id_
    monetary_account_id = generated.MonetaryAccountBank.list(
        api_context,
        user_id
    ).value[_INDEX_FIRST].id_

    date_start = datetime.datetime.now()
    date_start -= datetime.timedelta(_DAYS_IN_WEEK)
    date_end = datetime.datetime.now()
    customer_statement_map = {
        generated.CustomerStatementExport.FIELD_STATEMENT_FORMAT:
            _CUSTOMER_STATEMENT_FORMAT,
        generated.CustomerStatementExport.FIELD_DATE_START: date_start.strftime(
            _FORMAT_DATE
        ),
        generated.CustomerStatementExport.FIELD_DATE_END: date_end.strftime(
            _FORMAT_DATE
        ),
    }
    customer_statement_id = generated.CustomerStatementExport.create(
        api_context,
        customer_statement_map,
        user_id,
        monetary_account_id
    ).value
    generated.CustomerStatementExport.delete(
        api_context,
        user_id,
        monetary_account_id,
        customer_statement_id
    )

    api_context.save()

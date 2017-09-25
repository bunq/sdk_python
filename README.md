# bunq Python SDK

## Introduction
Hi developers!

Welcome to the bunq Python SDK! 👨‍💻

We're very happy to introduce yet another unique product: complete banking SDKs! 
Now you can build even bigger and better apps and integrate them with your bank of the free! 🌈

Before you dive into this brand new SDK, please consider:
- Checking out our new developer’s page [https://bunq.com/en/developer](https://bunq.com/en/developer) 🙌  
- Grabbing your production API key from the bunq app or asking our support for a Sandbox API key 🗝
- Visiting [together.bunq.com](https://together.bunq.com) where you can share your creations,
questions and experience 🎤

Give us your feedback, create pull requests, build your very own bunq apps and most importantly:
have fun! 💪

This SDK is in **beta**. We cannot guarantee constant availability or stability. 
Thanks to your feedback we will make improvements on it.

## Installation
``pip install bunq_sdk --upgrade``

## Usage

### Creating an API context
In order to start making calls with the bunq API, you must first register your API key and device,
and create a session. In the SDKs, we group these actions and call it "creating an API context". The
context can be created by using the following code snippet:

```
apiContext = context.ApiContext(ENVIRONMENT_TYPE, API_KEY,
  DEVICE_DESCRIPTION);
apiContext.save(API_CONTEXT_FILE_PATH);
```

#### Example
See [`api_context_save_example.py`](./examples/api_context_save_example.py)

The API context can then be saved with:

#### Safety considerations
The file storing the context details (i.e. `bunq.conf`) is a key to your account. Anyone having
access to it is able to perform any Public API actions with your account. Therefore, we recommend
choosing a truly safe place to store it.

### Making API calls
There is a class for each endpoint. Each class has functions for each supported action. These
actions can be `create`, `get`, `update`, `delete` and `list`.

Sometimes API calls have dependencies, for instance `MonetaryAccount`. Making changes to a monetary
account always also needs a reference to a `User`. These dependencies are required as arguments when
performing API calls. Take a look at [doc.bunq.com](https://doc.bunq.com) for the full
documentation.

#### Creating objects
Creating objects through the API requires an `ApiContext`, a `requestMap` and identifiers of all
dependencies (such as User ID required for accessing a Monetary Account). Optionally, custom headers
can be passed to requests.


```
request_map = {
    generated.Payment.FIELD_AMOUNT: object_.Amount(
        _PAYMENT_AMOUNT,
        _PAYMENT_CURRENCY
    ),
    generated.Payment.FIELD_COUNTERPARTY_ALIAS: object_.Pointer(
        _COUNTERPARTY_POINTER_TYPE,
        _COUNTERPARTY_EMAIL
    ),
    generated.Payment.FIELD_DESCRIPTION: _PAYMENT_DESCRIPTION,
}

payment_id = generated.Payment.create(
    api_context,
    request_map,
    _USER_ITEM_ID,
    _MONETARY_ACCOUNT_ITEM_ID
)
```

##### Example
See [`PaymentExample.py`](./examples/payment_example.py)

#### Reading objects
Reading objects through the API requires an `ApiContext`, identifiers of all dependencies (such as
User ID required for accessing a Monetary Account), and the identifier of the object to read (ID or
UUID) Optionally, custom headers can be passed to requests.

This type of calls always returns a model.

```
monetary_account = generated.MonetaryAccountBank.get(
    api_context,
    _USER_ITEM_ID,
    _MONETARY_ACCOUNT_ITEM_ID
)
```

##### Example
See [`MonetaryAccountExample.py`](./examples/monetary_account_example.py)

#### Updating objects
Updating objects through the API goes the same way as creating objects, except that also the object to update identifier 
(ID or UUID) is needed.

```
request_update_map = {
    generated.RequestInquiry.FIELD_STATUS: _STATUS_REVOKED,
}
generated.RequestInquiry.update(
    api_context,
    request_update_map,
    _USER_ITEM_ID,
    _MONETARY_ACCOUNT_ITEM_ID,
    request_id
).to_json()
```

##### Example
See [`RequestExample.py`](./examples/request_example.py)

#### Deleting objects
Deleting objects through the API requires an `ApiContext`, identifiers of all dependencies (such as User ID required for
accessing a Monetary Account), and the identifier of the object to delete (ID or UUID) Optionally, custom headers can be
passed to requests.

```
generated.CustomerStatementExport.delete(apiContext, userId, monetaryAccountId, customerStatementId);
```

##### Example
See [`CustomerStatementExportExample.py`](./examples/customer_statement_export_example.py)

#### Listing objects
Listing objects through the API requires an `ApiContext` and identifiers of all dependencies (such as User ID required
for accessing a Monetary Account). Optionally, custom headers can be passed to requests.

```
users = generated.User.list(api_context)
```

##### Example
See [`UserListExample.py`](./examples/user_list_example.py)

## Running Samples
In order to make the experience of getting into bunq Python SDK smoother, we
have bundled it with example use cases (located under `/examples`).

To run an example, please do the following:
1. In your IDE, open the example you are interested in and adjust the constants,
such as `_API_KEY` or `_USER_ID`, to hold your data.
2. In your terminal, go to the root of bunq SDK project:

```shell
$ cd /path/to/bunq/sdk/
```
3. In the terminal, run:

```shell
$ python3 run.py examples/<something_example.py>
```
   Replace `<something_example.py>` with the name of the example you would like
   to run. If you wish to run the example with python 2, also replace
   `python3` with `python`.

In order for examples to run, you would need a valid context file (`bunq.conf`)
to be present in the bunq SDK project root directory. The file can either copied
from somewhere else (e.g. tests) or created by running the following command
in your bunq SDK project root directory:

```shell
$ python3 run.py examples/api_context_save_example.py
```

Please do not forget to set the `_API_KEY` constant in
`api_context_save_example.py` to your actual API key before running the sample!

## Running Tests

Information regarding the test cases can be found in the [README.md](./tests/README.md)
located in [test](/tests)

## Exceptions
The SDK can raise multiple exceptions. For an overview of these exceptions please
take a look at [EXCEPTIONS.md](./EXCEPTIONS.md)

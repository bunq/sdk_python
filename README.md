# bunq Python SDK

## Introduction
Hi developers!

Welcome to the bunq Python SDK! 👨‍💻

We're very happy to introduce yet another unique product: complete banking SDKs! 
Now you can build even bigger and better apps and integrate them with your bank of the free! 🌈

Before you dive into this brand new SDK, please consider:
- Checking out our new developer’s page [https://bunq.com/en/developer](https://bunq.com/en/developer) 🙌  
- Grabbing your production API key from the bunq app or generate a Sandbox API key using [Tinker](https://www.bunq.com/developer) 🗝
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
apiContext.save(API_CONTEXT_FILE_PATH)
context.BunqContext.loadApiContext(apiContext)
```

This code snippet, except for `context.BunqContext.loadApiContext(apiContext)` should be called once per API key. 

#### Example

See [`tinker/setup_context`](https://github.com/bunq/tinker_python/blob/2182b8be276fda921657ad22cfe0b8b48a585ccf/tinker/libs/bunq_lib.py#L44-L59)

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
payment_id = endpoint.Payment.create(
	amount=Amount(amount_string, self._CURRENCY_EURL),
    counterparty_alias=Pointer(self._POINTER_TYPE_EMAIL, recipient),
    description=description
    )
```

##### Example
See [`tinker/make_payment`](https://github.com/bunq/tinker_python/blob/2182b8be276fda921657ad22cfe0b8b48a585ccf/tinker/libs/bunq_lib.py#L140-L151)

#### Reading objects
Reading objects through the API requires an `ApiContext`, identifiers of all dependencies (such as
User ID required for accessing a Monetary Account), and the identifier of the object to read (ID or
UUID) Optionally, custom headers can be passed to requests.

This type of calls always returns a model.

```
monetary_account = generated.MonetaryAccountBank.get(
    _MONETARY_ACCOUNT_ITEM_ID
)
```

##### Example
See [`tinker/list_all_payment`](https://github.com/bunq/tinker_python/blob/2182b8be276fda921657ad22cfe0b8b48a585ccf/tinker/libs/bunq_lib.py#L85-L103)

#### Updating objects
Updating objects through the API goes the same way as creating objects, except that also the object to update identifier 
(ID or UUID) is needed.

```
endpoint.Card.update(
	card_id=int(card_id),
	monetary_account_current_id=int(account_id)
	)
```

##### Example
See [`tinker/update_card`](https://github.com/bunq/tinker_python/blob/2182b8be276fda921657ad22cfe0b8b48a585ccf/tinker/libs/bunq_lib.py#L167-L174)

#### Deleting objects
Deleting objects through the API requires an `ApiContext`, identifiers of all dependencies (such as User ID required for
accessing a Monetary Account), and the identifier of the object to delete (ID or UUID) Optionally, custom headers can be
passed to requests.

```
Session.delete(self._SESSION_ID)
```

##### Example


#### Listing objects
Listing objects through the API requires an `ApiContext` and identifiers of all dependencies (such as User ID required
for accessing a Monetary Account). Optionally, custom headers can be passed to requests.

```
users = generated.User.list(api_context)
```

##### Example
See [`UserListExample.py`](./examples/user_list_example.py)

## Running Samples
To get an indication on how the SDK works you can use the python tinker which is located at https://github.com/bunq/tinker_python

## Running Tests

Information regarding the test cases can be found in the [README.md](./tests/README.md)
located in [test](/tests)

## Exceptions
The SDK can raise multiple exceptions. For an overview of these exceptions please
take a look at [EXCEPTIONS.md](./bunq/sdk/exception/EXCEPTIONS.md)

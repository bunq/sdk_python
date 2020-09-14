# bunq Python SDK

## Introduction
Hi developers!

Welcome to the bunq Python SDK! 👨‍💻

We're very happy to introduce yet another unique product: complete banking SDKs! 
Now you can build even bigger and better apps and integrate them with your bank of the free! 🌈

Before you dive into this brand new SDK, please consider:
- Learning how bunq works and what objects you will work with by reading [the intro to our API](https://github.com/bunq/doc/blob/develop/README.md) 🤓
- Checking out [our developer portal](https://developer.bunq.com/) 🙌  
- Grabbing your Production API key from [our developer portal](https://developer.bunq.com/) or the bunq app 🗝
- Generating a Sandbox API key using [our developer portal](https://developer.bunq.com/) or [Tinker](https://www.bunq.com/developer) 🗝
- Visiting [our forum](https://together.bunq.com/t/api) where you can share your creations,
questions and experience 🎤

Give us your feedback, create pull requests, build your very own bunq apps and most importantly:
have fun! 💪

This SDK is in **beta**. We cannot guarantee constant availability or stability. 
Thanks to your feedback we will make improvements on it.

## Installation
    pip install bunq_sdk --upgrade

## Usage

### Creating an API context
In order to start making calls with the bunq API, you must first register your API key and device,
and create a session. In the SDKs, we group these actions and call it "creating an API context". The
context can be created by using the following code snippet:


    apiContext = ApiContext.create(ENVIRONMENT_TYPE, API_KEY, DEVICE_DESCRIPTION)
    apiContext.save(API_CONTEXT_FILE_PATH)


**Please note**: initialising your application is a heavy task and it is recommended to do it only once per device.

    apiContext = ApiContext.restore(self.API_CONTEXT_FILE_PATH)
    BunqContext.loadApiContext(apiContext)

After saving the context, you can restore it at any time: 

#### Example

See [`tinker/setup_context`](https://github.com/bunq/tinker_python/blob/2182b8be276fda921657ad22cfe0b8b48a585ccf/tinker/libs/bunq_lib.py#L44-L59)

#### PSD2
It is possible to create an ApiContext as PSD2 Service Provider. Although this might seem a complex task, we wrote some 
helper implementations to get you started. You need to create a certificate and private key to get you started. 
Our sandbox environment currently accepts all certificates, if these criteria are met:

- Up to 64 characters
- PISP and/or AISP used in the end.

Make sure you have your unique eIDAS certificate number and certificates ready when you want to perform these tasks on 
our production environment.

Creating a PSD2 context is very easy:

    apiContext = ApiContext.create_for_psd2(ENVIRONMENT_TYPE, CERTIFICATE, PRIVATE_KEY, CERTIFICATE_CHAIN, DEVICE_DESCRIPTION)

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

    payment_id = Payment.create(
        amount=Amount(amount_string, self._CURRENCY_EURL),
        counterparty_alias=Pointer(self._POINTER_TYPE_EMAIL, recipient),
        description=description
    )

##### Example
See [`tinker/make_payment`](https://github.com/bunq/tinker_python/blob/2182b8be276fda921657ad22cfe0b8b48a585ccf/tinker/libs/bunq_lib.py#L140-L151)

#### Reading objects
Reading objects through the API requires an `ApiContext`, identifiers of all dependencies (such as
User ID required for accessing a Monetary Account), and the identifier of the object to read (ID or
UUID) Optionally, custom headers can be passed to requests.

This type of calls always returns a model.

    monetary_account = generated.MonetaryAccountBank.get(
        _MONETARY_ACCOUNT_ITEM_ID
    )

##### Example
See [`tinker/list_all_payment`](https://github.com/bunq/tinker_python/blob/2182b8be276fda921657ad22cfe0b8b48a585ccf/tinker/libs/bunq_lib.py#L85-L103)

#### Updating objects
Updating objects through the API goes the same way as creating objects, except that also the object to update identifier 
(ID or UUID) is needed.

    Card.update(
        card_id=int(card_id),
        monetary_account_current_id=int(account_id)
    )

##### Example
See [`tinker/update_card`](https://github.com/bunq/tinker_python/blob/2182b8be276fda921657ad22cfe0b8b48a585ccf/tinker/libs/bunq_lib.py#L167-L174)

#### Deleting objects
Deleting objects through the API requires an `ApiContext`, identifiers of all dependencies (such as User ID required for
accessing a Monetary Account), and the identifier of the object to delete (ID or UUID) Optionally, custom headers can be
passed to requests.

    Session.delete(self._SESSION_ID)

##### Example

#### Listing objects
Listing objects through the API requires an `ApiContext` and identifiers of all dependencies (such as User ID required
for accessing a Monetary Account). Optionally, custom headers can be passed to requests.

    users = User.list(api_context)

##### Example
See [`UserListExample.py`](./examples/user_list_example.py)

## Running Samples
To get an indication on how the SDK works you can use the python tinker which is located at https://github.com/bunq/tinker_python

## Running Tests

Information regarding the test cases can be found in the [README.md](./tests/README.md)
located in [test](/tests).

## Exceptions
The SDK can raise multiple exceptions. For an overview of these exceptions please
take a look at [EXCEPTIONS.md](./bunq/sdk/exception/EXCEPTIONS.md).

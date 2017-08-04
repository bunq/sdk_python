# bunq Python SDK
Version 0.9.0 **BETA**

## Introduction
Hi developers!


Welcome to the bunq Python SDK integration tests. Currently we are not
targeting the 100% test coverage, but rather want to be certain that the most
common scenarios can run without any errors.


## Scenarios 

These are the scenarios that are currently being tested:
* Create installation, session-server and device server
* Create a new MonetaryAccount
* Create a tab
* Update the tab
* Create attachment and avatar
* Request money from first MA to second MA
* Accept the request
* Make a transaction from first MA to second MA
* Create connect gr code
* Make a payment to another sandbox user
* Send a chat message in a recent payment
* Delete the current session
* Order a card with a second line

Besides these scenarios, some code of ApiContext, ApiClient and the JSON module 
are also tested :thumbs_up:.

## Configuration

To run the tests you must first setup the test configuration JSON. The example
of a configuration file is located at `tests/assets/config.example.json`. In
order to make use of the configuration file, please copy the example to the same
directory, fill in your sandbox user data and rename the copy to config.json.

## Execution

You can run the tests via command line: 

```
python -m unittest discover -s tests/model/generated
```  

or via PyCharm, but first you must configure PyCharm by doing the following:
* Got to preferences --> tools --> Python integrated tools and change default
test runner to `unittests`.
* Configure your Python interpreter to an supported Python version. Python 3 is
recommended.

Afterwards you can right click on the tests folders and should be able to run
the tests cases form the IDE.

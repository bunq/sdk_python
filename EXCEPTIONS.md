## Exceptions
When you make a request via the SDK, there is a chance of request failing
due to various reasons. When such a failure happens, an exception
corresponding to the error occurred is raised.


----
#### Possible Exceptions
* `BadRequestException` If the request returns with status code `400`
* `UnauthorizedException` If the request returns with status code `401`
* `ForbiddenException` If the request returns with status code `403`
* `NotFoundException` If the request returns with status code `404`
* `MethodNotAllowedException` If the request returns with status code `405`
* `TooManyRequestsException` If the request returns with status code `429`
* `PleaseContactBunqException` If the request returns with status code `500`.
If you get this exception, please contact us preferably via the support chat in the bunq app.
* `UnknownApiErrorException` If none of the above mentioned exceptions are raised,
this exception will be raised instead.

For more information regarding these errors, please take a look on the documentation
page here: https://doc.bunq.com/api/1/page/errors

---
#### Base exception
All the exceptions have the same base exception which looks like this:
```python
class ApiException(Exception):
    def __init__(self, message, response_code):
        pass
        
    @property
    def message(self):
        """
        :rtype: str
        """

        return self._message

    @property
    def response_code(self):
        """
        :rtype: int
        """

        return self._response_code
```
This means that each exception will have the response code and the error message 
related to the specific exception that has been raised.

---
#### Exception handling
Because we raise different exceptions for each error, you can catch an error
if you expect it to be raised.

```python
from bunq.sdk.exception import BadRequestException
from bunq.sdk.context import ApiEnvironmentType, ApiContext

API_KEY = "Some invalid API key"
DESCRIPTION = "This wil raise a BadRequestException"

try:
    # Make a call that might raise an exception
    ApiContext(ApiEnvironmentType.SANDBOX, API_KEY, DESCRIPTION)
except BadRequestException as error:
    # Do something if exception is raised
    print(error.response_code)
    print(error.message) # or just print(error)
```

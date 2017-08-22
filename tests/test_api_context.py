import os

from bunq.sdk.context import ApiContext
from bunq.sdk.json import converter
from tests.bunq_test import BunqSdkTestCase


class TestApiContext(BunqSdkTestCase):
    """
    Tests:
        ApiContext
    """

    _TMP_FILE_PATH = '/context-save-test.conf'

    @classmethod
    def setUpClass(cls):
        cls._FILE_MODE_READ = ApiContext._FILE_MODE_READ
        cls._API_CONTEXT = cls._get_api_context()
        cls._TMP_FILE_PATH_FULL = (cls._get_directory_test_root() +
                                   cls._TMP_FILE_PATH)

    def test_api_context_save(self):
        """
        Converts an ApiContext to JSON data, saves the same ApiContext to a
        temporary file, and compares whether the JSON data is equal to the
        data in the file.

        Removes the temporary file before assertion.
        """

        context_json = converter.class_to_json(self._API_CONTEXT)

        self._API_CONTEXT.save(self._TMP_FILE_PATH_FULL)

        with open(self._TMP_FILE_PATH_FULL, self._FILE_MODE_READ) as file_:
            context_retrieved = file_.read()

        os.remove(self._TMP_FILE_PATH_FULL)

        self.assertEqual(context_retrieved, context_json)

    def test_api_context_restore(self):
        """
        Saves an ApiContext to a temporary file, restores an ApiContext from
        that file, and compares whether the api_keys, tokens, and environment
        types are equal in the ApiContext and the restored ApiContext.

        Removes the temporary file before assertion.
        """

        self._API_CONTEXT.save(self._TMP_FILE_PATH_FULL)
        api_context_restored = ApiContext.restore(self._TMP_FILE_PATH_FULL)

        os.remove(self._TMP_FILE_PATH_FULL)

        self.assertEqual(api_context_restored, self._API_CONTEXT)

    def test_api_context_save_json(self):
        """
        Converts an ApiContext to JSON data, saves the ApiContext using the
        ApiContext.save() function with the to_JSON flag set to True, and
        compares whether the JSON data equals the returned JSON data from the
        ApiContext.save() function.
        """

        context_json = converter.class_to_json(self._API_CONTEXT)
        context_saved = self._API_CONTEXT.to_json()

        self.assertEqual(context_saved, context_json)

    def test_api_context_restore_json(self):
        """
        Saves an ApiContext with the ApiContext.save() function with the
        to_JSON flag set to True, restores an ApiContext from the JSON data
        returned from the ApiContext.save() function, and checks that the
        api_key, token, and environment type variables of the restored
        ApiContext are equal to the respective variables in the original
        ApiContext.
        """

        context_json = self._API_CONTEXT.to_json()
        api_context_restored = self._API_CONTEXT.from_json(context_json)

        self.assertEqual(api_context_restored, self._API_CONTEXT)

from __future__ import annotations

from typing import List, Dict

from bunq.sdk.http.api_client import ApiClient
from bunq.sdk.http.bunq_response import BunqResponse
from bunq.sdk.json import converter
from bunq.sdk.model.generated.endpoint import NotificationFilterUrlMonetaryAccount
from bunq.sdk.model.generated.object_ import NotificationFilterUrl


class NotificationFilterUrlMonetaryAccountInternal(NotificationFilterUrlMonetaryAccount):
    @classmethod
    def create_with_list_response(cls,
                                  monetary_account_id: int = None,
                                  all_notification_filter: List[NotificationFilterUrl] = None,
                                  custom_headers: Dict[str, str] = None
                                  ) -> BunqResponse[List[NotificationFilterUrl]]:
        if all_notification_filter is None:
            all_notification_filter = []

        if custom_headers is None:
            custom_headers = {}

        request_map = {
            cls.FIELD_NOTIFICATION_FILTERS: all_notification_filter
        }
        request_map_string = converter.class_to_json(request_map)
        request_map_string = cls._remove_field_for_request(request_map_string)

        api_client = ApiClient(cls._get_api_context())
        request_bytes = request_map_string.encode()
        endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id(),
                                                       cls._determine_monetary_account_id(monetary_account_id))
        response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)

        return NotificationFilterUrl._from_json_list(response_raw, cls._OBJECT_TYPE_GET)

from typing import Dict, Type, Optional

from bunq.sdk.json import converter
from bunq.sdk.model.generated import object_
from bunq.sdk.model.generated.object_ import ShareDetail


class ShareDetailAdapter(converter.JsonAdapter):
    # Attribute/Field constants
    _ATTRIBUTE_PAYMENT = 'payment'
    _FIELD_PAYMENT = 'ShareDetailPayment'

    _ATTRIBUTE_READ_ONLY = 'read_only'
    _FIELD_READ_ONLY = 'ShareDetailReadOnly'

    _ATTRIBUTE_DRAFT_PAYMENT = 'draft_payment'
    _FIELD_DRAFT_PAYMENT = 'ShareDetailDraftPayment'

    @classmethod
    def deserialize(cls,
                    target_class: Type[ShareDetail],
                    obj: Dict) -> ShareDetail:
        """
        :type target_class: object_.ShareDetail|type
        :type obj: dict

        :rtype: object_.ShareDetail
        """

        share_detail = target_class.__new__(target_class)
        share_detail.__dict__ = {
            cls._ATTRIBUTE_PAYMENT: converter.deserialize(
                object_.ShareDetailPayment,
                cls._get_field_or_none(cls._FIELD_DRAFT_PAYMENT, obj)
            ),
            cls._ATTRIBUTE_READ_ONLY: converter.deserialize(
                object_.ShareDetailReadOnly,
                cls._get_field_or_none(cls._FIELD_READ_ONLY, obj)
            ),
            cls._ATTRIBUTE_DRAFT_PAYMENT: converter.deserialize(
                object_.ShareDetailDraftPayment,
                cls._get_field_or_none(cls._FIELD_DRAFT_PAYMENT, obj)
            ),
        }

        return share_detail

    @staticmethod
    def _get_field_or_none(field: str, obj: Dict) -> Optional[Dict]:
        return obj[field] if field in obj else None

    @classmethod
    def serialize(cls, share_detail: ShareDetail) -> Dict:
        return {
            cls._FIELD_PAYMENT: converter.serialize(
                share_detail._payment_field_for_request),
            cls._FIELD_READ_ONLY: converter.serialize(
                share_detail._read_only_field_for_request),
            cls._FIELD_DRAFT_PAYMENT: converter.serialize(
                share_detail._draft_payment
            ),
        }

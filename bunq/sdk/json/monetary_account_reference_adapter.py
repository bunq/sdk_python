from typing import Type, Dict

from bunq.sdk.json import converter
from bunq.sdk.model.generated import object_
from bunq.sdk.model.generated.object_ import MonetaryAccountReference


class MonetaryAccountReferenceAdapter(converter.JsonAdapter):
    @classmethod
    def deserialize(cls,
                    target_class: Type[MonetaryAccountReference],
                    obj: Dict) -> MonetaryAccountReference:
        label_monetary_account = converter.deserialize(
            object_.LabelMonetaryAccount,
            obj
        )

        return target_class.create_from_label_monetary_account(label_monetary_account)

    @classmethod
    def serialize(cls, monetary_account_reference: MonetaryAccountReference) -> Dict:
        return converter.serialize(monetary_account_reference.pointer)

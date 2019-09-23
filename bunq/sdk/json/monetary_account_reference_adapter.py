from bunq.sdk.json import converter
from bunq.sdk.model.generated import object_


class MonetaryAccountReferenceAdapter(converter.JsonAdapter):
    @classmethod
    def deserialize(cls, target_class, obj):
        """
        :type target_class: object_.MonetaryAccountReference|type
        :type obj: dict

        :rtype: object_.MonetaryAccountReference
        """

        label_monetary_account = converter.deserialize(
            object_.LabelMonetaryAccount,
            obj
        )

        return target_class.create_from_label_monetary_account(label_monetary_account)

    @classmethod
    def serialize(cls, monetary_account_reference):
        """
        :type monetary_account_reference: object_.MonetaryAccountReference

        :rtype: dict
        """

        return converter.serialize(monetary_account_reference.pointer)

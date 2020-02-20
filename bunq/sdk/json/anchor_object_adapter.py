from __future__ import annotations

from bunq import AnchorObjectInterface
from bunq.sdk.exception.bunq_exception import BunqException
from bunq.sdk.json import converter
from bunq.sdk.model.core.bunq_model import BunqModel
from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated import object_
from bunq.sdk.util.type_alias import JsonValue
from bunq.sdk.util.type_alias import T


class AnchorObjectAdapter(converter.JsonAdapter):
    __ERROR_MODEL_NOT_FOUND = '{} is not in endpoint nor object.'

    __STRING_FORMAT_UNDERSCORE = '_'

    _override_field_map = {
        'ScheduledPayment': 'SchedulePayment',
        'ScheduledInstance': 'ScheduleInstance',
        'ShareInviteBankInquiry': 'ShareInviteMonetaryAccountInquiry',
        'ShareInviteBankResponse': 'ShareInviteMonetaryAccountResponse'
    }

    @classmethod
    def deserialize(cls,
                    cls_target: Type[T],
                    obj_raw: JsonValue) -> T:
        model_ = super()._deserialize_default(cls_target, obj_raw)

        if isinstance(model_, AnchorObjectInterface) and model_.is_all_field_none():
            for field in model_.__dict__:
                object_class = cls._get_object_class(field)
                contents = super()._deserialize_default(object_class, obj_raw)

                if contents.is_all_field_none():
                    setattr(model_, field, None)
                else:
                    setattr(model_, field, contents)

        return model_

    @classmethod
    def can_serialize(cls) -> bool:
        return False

    @classmethod
    def _get_object_class(cls, class_name: str) -> BunqModel:
        class_name = class_name.lstrip(cls.__STRING_FORMAT_UNDERSCORE)

        if class_name in cls._override_field_map:
            class_name = cls._override_field_map[class_name]

        try:
            return getattr(endpoint, class_name)
        except AttributeError:
            pass

        try:
            return getattr(object_, class_name)
        except AttributeError:
            pass

        raise BunqException(cls.__ERROR_MODEL_NOT_FOUND.format(class_name))

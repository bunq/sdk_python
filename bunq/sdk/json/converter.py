import inspect
import json
import re
import sys
import warnings

from bunq.sdk import exception

# Indentation size we use for the serialized JSON output
_JSON_INDENT = 4


class JsonAdapter(object):
    # Error constants
    _ERROR_COULD_NOT_FIND_CLASS = 'Could not find class: {}'

    # Maps to store custom serializers and deserializers
    _custom_serializers = {}
    _custom_deserializers = {}

    # Initializer
    _initializer = None

    # Warning for when a key from raw object is unknown
    _WARNING_KEY_UNKNOWN = '[bunq SDK beta] Key "{}" in "{}" is unknown.'

    # Overlapping key names to be suffixed by and underscore
    _KEYS_OVERLAPPING = {'id', 'type', 'object'}

    # Suffix to strip from the keys during serialization
    _SUFFIX_KEY_OVERLAPPING = '_'
    _PREFIX_KEY_PROTECTED = '_'

    # Constants to fetch param types from the docstrings
    _TEMPLATE_PATTERN_PARAM_TYPES = \
        ':type (_?{}):[\s\n\r]+([\w.]+)(?:\[([\w.]+)\])?'
    _PATTERN_PARAM_NAME_TYPED_ANY = ':type (\w+):'
    _SUBMATCH_INDEX_NAME = 1
    _SUBMATCH_INDEX_TYPE_MAIN = 2
    _SUBMATCH_INDEX_TYPE_SUB = 3

    # List of builtin type names
    _TYPE_NAMES_BUILTIN = {'int', 'bool', 'float', 'str', 'list', 'dict',
                           'bytes', 'unicode'}

    # Delimiter between modules in class paths
    _DELIMITER_MODULE = '.'

    # List of byte-array type names
    _TYPE_NAMES_BYTES = {'bytes', 'unicode'}

    @classmethod
    def set_initializer(cls, initializer):
        """
        :type initializer: Generator[bool, None, None]
        """

        cls._initializer = initializer

    @classmethod
    def register_custom_adapter(cls, target_class, adapter):
        """
        :type target_class: type
        :type adapter: JsonAdapter|type

        :rtype: None
        """

        class_name = target_class.__name__

        if adapter.can_serialize():
            cls._custom_serializers[class_name] = adapter

        if adapter.can_deserialize():
            cls._custom_deserializers[class_name] = adapter

    @classmethod
    def _get_serializer(cls, cls_for):
        """
        :type cls_for: type

        :rtype: JsonAdapter
        """

        if cls_for.__name__ in cls._custom_serializers:
            return cls._custom_serializers[cls_for.__name__]

        return JsonAdapter

    @classmethod
    def _get_deserializer(cls, cls_for):
        """
        :type cls_for: type

        :rtype: JsonAdapter
        """

        if cls_for.__name__ in cls._custom_deserializers:
            return cls._custom_deserializers[cls_for.__name__]

        return JsonAdapter

    @classmethod
    def can_deserialize(cls):
        """
        :rtype: bool
        """

        return True

    @classmethod
    def deserialize(cls, cls_target, obj_raw):
        """
        :type cls_target: T|type
        :type obj_raw: int|str|bool|float|list|dict|None

        :rtype: T
        """

        cls._initialize()
        deserializer = cls._get_deserializer(cls_target)

        if deserializer == cls:
            return cls._deserialize_default(cls_target, obj_raw)
        else:
            return deserializer.deserialize(cls_target, obj_raw)

    @classmethod
    def _initialize(cls):
        """
        :rtype: None
        """

        next(cls._initializer, None)

    @classmethod
    def _deserialize_default(cls, cls_target, obj_raw):
        """
        :type cls_target: T|type
        :type obj_raw: int|str|bool|float|list|dict|None

        :rtype: T
        """

        if cls._is_deserialized(cls_target, obj_raw):
            return obj_raw
        elif type(obj_raw) == dict:
            return cls._deserialize_dict(cls_target, obj_raw)
        else:
            return cls_target(obj_raw)

    @classmethod
    def _is_deserialized(cls, cls_target, obj):
        """
        :type cls_target: type
        :type obj: int|str|bool|float|bytes|unicode|list|dict|object

        :rtype: bool
        """

        if cls_target is None:
            return True

        if cls_target in {list, dict}:
            return True

        if cls._is_bytes_type(cls_target):
            return True

        if obj is None:
            return True

        if type(obj) in {list, cls_target}:
            return True

        return False

    @classmethod
    def _deserialize_dict(cls, cls_target, dict_):
        """
        :type cls_target: T|type
        :type dict_: dict

        :rtype: T
        """

        instance = cls_target.__new__(cls_target)
        dict_deserialized = cls._deserialize_dict_attributes(cls_target, dict_)
        instance.__dict__ = cls._fill_default_values(cls_target,
                                                     dict_deserialized)

        return instance

    @classmethod
    def _deserialize_dict_attributes(cls, cls_context, dict_):
        """
        :type cls_context: type
        :type dict_: dict

        :rtype: dict
        """

        dict_deserialized = {}

        for key in dict_.keys():
            key_deserialized = cls._deserialize_key(key)
            value_specs = cls._get_value_specs(cls_context, key_deserialized)

            if value_specs is not None:
                dict_deserialized[value_specs.name] = cls._deserialize_value(
                    value_specs.types,
                    dict_[key]
                )
            else:
                cls._warn_key_unknown(cls_context, key)

        return dict_deserialized

    @classmethod
    def _deserialize_key(cls, key):
        """
        :type key: str

        :rtype: str
        """

        if key in cls._KEYS_OVERLAPPING:
            return key + cls._SUFFIX_KEY_OVERLAPPING

        return key

    @classmethod
    def _get_value_specs(cls, cls_in, attribute_name):
        """
        :type cls_in: type
        :type attribute_name: str

        :rtype: ValueSpecs
        """

        if cls_in in {dict, list}:
            return ValueSpecs(None, ValueTypes(None, None))
        else:
            return cls._fetch_attribute_specs_from_doc(cls_in, attribute_name)

    @classmethod
    def _fetch_attribute_specs_from_doc(cls, cls_in, attribute_name):
        """
        :type cls_in: type
        :type attribute_name: str

        :rtype: ValueSpecs
        """

        pattern = cls._TEMPLATE_PATTERN_PARAM_TYPES.format(attribute_name)
        match = re.search(pattern, cls_in.__doc__)

        if match is not None:
            return ValueSpecs(
                cls._fetch_name(match),
                ValueTypes(
                    cls._fetch_type_main(cls_in, match),
                    cls._fetch_type_sub(cls_in, match)
                )
            )
        else:
            return None

    @classmethod
    def _fetch_name(cls, match):
        """
        :type match: _sre.SRE_Match

        :rtype: str
        """

        return match.group(cls._SUBMATCH_INDEX_NAME)

    @classmethod
    def _fetch_type_main(cls, cls_in, match):
        """
        :type cls_in: type
        :type match: _sre.SRE_Match

        :rtype: type
        """

        return cls._str_to_type(
            cls_in,
            match.group(cls._SUBMATCH_INDEX_TYPE_MAIN)
        )

    @classmethod
    def _fetch_type_sub(cls, cls_in, match):
        """
        :type cls_in: type
        :type match: _sre.SRE_Match

        :rtype: type
        """

        if match.group(cls._SUBMATCH_INDEX_TYPE_SUB):
            return cls._str_to_type(
                cls_in,
                match.group(cls._SUBMATCH_INDEX_TYPE_SUB)
            )
        else:
            return None

    @classmethod
    def _str_to_type(cls, context_class, string):
        """
        :type context_class: type
        :type string: str

        :rtype: type
        """

        if string in cls._TYPE_NAMES_BUILTIN:
            return eval(string)

        module_ = sys.modules[context_class.__module__]

        if hasattr(module_, string):
            return getattr(module_, string)

        return cls._str_to_type_from_member_module(module_, string)

    @classmethod
    def _str_to_type_from_member_module(cls, module_, string):
        """
        :type module_: module
        :type string: str

        :rtype: type
        :raise: BunqException when could not find the class for the string.
        """

        module_name_short, class_name = string.split(cls._DELIMITER_MODULE)
        members = inspect.getmembers(module_, inspect.ismodule)

        for name, module_member in members:
            if module_name_short == name:
                return getattr(module_member, class_name)

        error_message = cls._ERROR_COULD_NOT_FIND_CLASS.format(string)

        raise exception.BunqException(error_message)

    @classmethod
    def _deserialize_value(cls, types, value):
        """
        :type types: ValueTypes
        :type value: int|str|bool|float|bytes|unicode|list|dict

        :rtype: int|str|bool|float|bytes|unicode|list|dict|object
        """

        if types.main == list and value is not None:
            return cls._deserialize_list(types.sub, value)
        else:
            return cls.deserialize(types.main, value)

    @classmethod
    def _deserialize_list(cls, type_item, list_):
        """
        :type type_item: T|type
        :type list_: list

        :rtype: list[T]
        """

        list_deserialized = []

        for item in list_:
            item_deserialized = cls.deserialize(type_item, item)
            list_deserialized.append(item_deserialized)

        return list_deserialized

    @classmethod
    def _warn_key_unknown(cls, cls_context, key):
        """
        :type cls_context: type
        :type key: str

        :rtype: None
        """

        context_name = cls_context.__name__
        warnings.warn(cls._WARNING_KEY_UNKNOWN.format(key, context_name))

    @classmethod
    def _fill_default_values(cls, cls_context, dict_):
        """
        :type cls_context: type
        :type dict_: dict

        :rtype: dict
        """

        dict_with_default_values = dict(dict_)
        params = re.findall(cls._PATTERN_PARAM_NAME_TYPED_ANY,
                            cls_context.__doc__)

        for param in params:
            if param not in dict_with_default_values:
                dict_with_default_values[param] = None

        return dict_with_default_values

    @classmethod
    def can_serialize(cls):
        """
        :rtype: bool
        """

        return True

    @classmethod
    def serialize(cls, obj):
        """
        :type obj: int|str|bool|float|bytes|unicode|list|dict|object

        :rtype: int|str|bool|list|dict
        """

        cls._initialize()
        serializer = cls._get_serializer(type(obj))

        if serializer == cls:
            return cls._serialize_default(obj)
        else:
            return serializer.serialize(obj)

    @classmethod
    def _serialize_default(cls, obj):
        """
        :type obj: int|str|bool|float|bytes|unicode|list|dict|object

        :rtype: int|str|bool|list|dict
        """

        if obj is None or cls._is_primitive(obj):
            return obj
        elif cls._is_bytes(obj):
            return obj.decode()
        elif type(obj) == list:
            return cls._serialize_list(obj)
        else:
            dict_ = cls._get_obj_raw(obj)

            return cls._serialize_dict(dict_)

    @classmethod
    def _is_primitive(cls, obj):
        """
        :type obj: int|str|bool|float|bytes|unicode|list|dict|object

        :rtype: bool
        """

        return cls._is_type_primitive(type(obj))

    @classmethod
    def _is_type_primitive(cls, type_):
        """
        :type type_: type

        :rtype: bool
        """

        return type_ in {int, str, bool, float}

    @classmethod
    def _is_bytes(cls, obj):
        """
        :type obj: int|str|bool|float|bytes|unicode|list|dict|object

        :rtype: bool
        """

        return cls._is_bytes_type(type(obj))

    @classmethod
    def _is_bytes_type(cls, type_):
        """
        :type type_: type

        :rtype: bool
        """

        return type_.__name__ in cls._TYPE_NAMES_BYTES

    @classmethod
    def _serialize_list(cls, list_):
        """
        :type list_: list

        :rtype: list
        """

        list_serialized = []

        for item in list_:
            item_serialized = cls.serialize(item)
            list_serialized.append(item_serialized)

        return list_serialized

    @classmethod
    def _get_obj_raw(cls, obj):
        """
        :type obj: int|str|bool|float|bytes|unicode|list|dict|object

        :rtype: dict
        """

        return obj if type(obj) == dict else obj.__dict__

    @classmethod
    def _serialize_dict(cls, dict_):
        """
        :type dict_ dict

        :rtype: dict
        """

        obj_serialized = {}

        for key in dict_.keys():
            item_serialized = cls.serialize(dict_[key])

            if item_serialized is not None:
                key = key.rstrip(cls._SUFFIX_KEY_OVERLAPPING)
                key = key.lstrip(cls._PREFIX_KEY_PROTECTED)
                obj_serialized[key] = item_serialized

        return obj_serialized


class ValueTypes(object):
    """
    :type _main: type|None
    :type _sub: type|None
    """

    def __init__(self, main, sub):
        """
        :type main: type|None
        :type sub: type|None
        """

        self._main = main
        self._sub = sub

    @property
    def main(self):
        """
        :rtype: type|None
        """

        return self._main

    @property
    def sub(self):
        """
        :rtype: type|None
        """

        return self._sub


class ValueSpecs(object):
    """
    :type _name: str|None
    :type _types: ValueTypes|None
    """

    def __init__(self, name, types):
        """
        :type name: str|None
        :type types: ValueTypes|None
        """

        self._name = name
        self._types = types

    @property
    def name(self):
        """
        :rtype: str|None
        """

        return self._name

    @property
    def types(self):
        """
        :rtype: ValueTypes|None
        """

        return self._types


def set_initializer_function(initializer_function):
    """
    :type initializer_function: callable
    """

    JsonAdapter.set_initializer(create_initializer(initializer_function))


def create_initializer(initializer_function):
    """
    :type initializer_function: callable

    :rtype: bool
    """

    is_disposed = False

    if not is_disposed:
        initializer_function()
        is_disposed = True

    yield is_disposed


def register_adapter(target_class, adapter):
    """
    :type target_class: type
    :type adapter: JsonAdapter|type

    :rtype: None
    """

    JsonAdapter.register_custom_adapter(target_class, adapter)


def json_to_class(cls, json_str):
    """
    :type cls: T|type
    :type json_str: str

    :rtype: T
    """

    obj_raw = json.loads(json_str)

    return deserialize(cls, obj_raw)


def deserialize(cls, obj_raw):
    """
    :type cls: T|type
    :type obj_raw: int|str|bool|float|list|dict|None

    :rtype: T
    """

    return JsonAdapter.deserialize(cls, obj_raw)


def class_to_json(obj):
    """
    :type obj: int|str|bool|float|bytes|unicode|list|dict|object

    :rtype: int|str|bool|list|dict
    """

    obj_raw = serialize(obj)

    return json.dumps(obj_raw, indent=_JSON_INDENT, sort_keys=True)


def serialize(obj_cls):
    """
    :type obj_cls: int|str|bool|float|bytes|unicode|list|dict|object

    :rtype: int|str|bool|list|dict
    """

    return JsonAdapter.serialize(obj_cls)

from __future__ import annotations

from collections.abc import Callable
from string import Formatter as StringFormatter
from typing import Any


# we only need string.Formatter for calling its parse() method, which returns `_string.formatter_parser(string)`.
_stringformatter = StringFormatter()
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_yield_from_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = yield from mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = yield from mutants[mutant_name](*call_args, **call_kwargs)
    return result


def _identity(obj):
    return obj


class Formatter:
    def xǁFormatterǁ__init____mutmut_orig(
        self,
        mapping: dict[str, Callable[[], Any]],
        formatting: dict[str, Callable[[Any, str], Any]] | None = None,
    ):
        super().__init__()
        self.mapping: dict[str, Callable[[], Any]] = mapping
        self.formatting: dict[str, Callable[[Any, str], Any]] = formatting or {}
        self.cache: dict[str, Any] = {}
    def xǁFormatterǁ__init____mutmut_1(
        self,
        mapping: dict[str, Callable[[], Any]],
        formatting: dict[str, Callable[[Any, str], Any]] | None = None,
    ):
        super().__init__()
        self.mapping: dict[str, Callable[[], Any]] = None
        self.formatting: dict[str, Callable[[Any, str], Any]] = formatting or {}
        self.cache: dict[str, Any] = {}
    def xǁFormatterǁ__init____mutmut_2(
        self,
        mapping: dict[str, Callable[[], Any]],
        formatting: dict[str, Callable[[Any, str], Any]] | None = None,
    ):
        super().__init__()
        self.mapping: dict[str, Callable[[], Any]] = mapping
        self.formatting: dict[str, Callable[[Any, str], Any]] = None
        self.cache: dict[str, Any] = {}
    def xǁFormatterǁ__init____mutmut_3(
        self,
        mapping: dict[str, Callable[[], Any]],
        formatting: dict[str, Callable[[Any, str], Any]] | None = None,
    ):
        super().__init__()
        self.mapping: dict[str, Callable[[], Any]] = mapping
        self.formatting: dict[str, Callable[[Any, str], Any]] = formatting and {}
        self.cache: dict[str, Any] = {}
    def xǁFormatterǁ__init____mutmut_4(
        self,
        mapping: dict[str, Callable[[], Any]],
        formatting: dict[str, Callable[[Any, str], Any]] | None = None,
    ):
        super().__init__()
        self.mapping: dict[str, Callable[[], Any]] = mapping
        self.formatting: dict[str, Callable[[Any, str], Any]] = formatting or {}
        self.cache: dict[str, Any] = None
    
    xǁFormatterǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFormatterǁ__init____mutmut_1': xǁFormatterǁ__init____mutmut_1, 
        'xǁFormatterǁ__init____mutmut_2': xǁFormatterǁ__init____mutmut_2, 
        'xǁFormatterǁ__init____mutmut_3': xǁFormatterǁ__init____mutmut_3, 
        'xǁFormatterǁ__init____mutmut_4': xǁFormatterǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFormatterǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁFormatterǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁFormatterǁ__init____mutmut_orig)
    xǁFormatterǁ__init____mutmut_orig.__name__ = 'xǁFormatterǁ__init__'

    def xǁFormatterǁ_get_value__mutmut_orig(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_1(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_2(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(None, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_3(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, None)

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_4(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_5(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, )

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_6(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_7(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name not in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_8(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = None
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_9(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = None
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_10(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = None

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_11(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is not None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_12(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = None

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_13(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(None, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_14(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, None)

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_15(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get("")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_16(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, )

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_17(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "XXXX")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_18(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec or field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_19(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name not in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_20(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](None, format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_21(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, None)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_22(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](format_spec)
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value

    def xǁFormatterǁ_get_value__mutmut_23(self, field_name: str, format_spec: str | None, defaults: dict[str, str]) -> Any:
        if field_name not in self.mapping:
            return defaults.get(field_name, f"{{{field_name}}}" if not format_spec else f"{{{field_name}:{format_spec}}}")

        if field_name in self.cache:
            value = self.cache[field_name]
        else:
            value = self.mapping[field_name]()
            self.cache[field_name] = value

        if value is None:
            value = defaults.get(field_name, "")

        if format_spec and field_name in self.formatting:
            # noinspection PyBroadException
            try:
                return self.formatting[field_name](value, )
            except Exception:
                return f"{{{field_name}:{format_spec}}}"

        return value
    
    xǁFormatterǁ_get_value__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFormatterǁ_get_value__mutmut_1': xǁFormatterǁ_get_value__mutmut_1, 
        'xǁFormatterǁ_get_value__mutmut_2': xǁFormatterǁ_get_value__mutmut_2, 
        'xǁFormatterǁ_get_value__mutmut_3': xǁFormatterǁ_get_value__mutmut_3, 
        'xǁFormatterǁ_get_value__mutmut_4': xǁFormatterǁ_get_value__mutmut_4, 
        'xǁFormatterǁ_get_value__mutmut_5': xǁFormatterǁ_get_value__mutmut_5, 
        'xǁFormatterǁ_get_value__mutmut_6': xǁFormatterǁ_get_value__mutmut_6, 
        'xǁFormatterǁ_get_value__mutmut_7': xǁFormatterǁ_get_value__mutmut_7, 
        'xǁFormatterǁ_get_value__mutmut_8': xǁFormatterǁ_get_value__mutmut_8, 
        'xǁFormatterǁ_get_value__mutmut_9': xǁFormatterǁ_get_value__mutmut_9, 
        'xǁFormatterǁ_get_value__mutmut_10': xǁFormatterǁ_get_value__mutmut_10, 
        'xǁFormatterǁ_get_value__mutmut_11': xǁFormatterǁ_get_value__mutmut_11, 
        'xǁFormatterǁ_get_value__mutmut_12': xǁFormatterǁ_get_value__mutmut_12, 
        'xǁFormatterǁ_get_value__mutmut_13': xǁFormatterǁ_get_value__mutmut_13, 
        'xǁFormatterǁ_get_value__mutmut_14': xǁFormatterǁ_get_value__mutmut_14, 
        'xǁFormatterǁ_get_value__mutmut_15': xǁFormatterǁ_get_value__mutmut_15, 
        'xǁFormatterǁ_get_value__mutmut_16': xǁFormatterǁ_get_value__mutmut_16, 
        'xǁFormatterǁ_get_value__mutmut_17': xǁFormatterǁ_get_value__mutmut_17, 
        'xǁFormatterǁ_get_value__mutmut_18': xǁFormatterǁ_get_value__mutmut_18, 
        'xǁFormatterǁ_get_value__mutmut_19': xǁFormatterǁ_get_value__mutmut_19, 
        'xǁFormatterǁ_get_value__mutmut_20': xǁFormatterǁ_get_value__mutmut_20, 
        'xǁFormatterǁ_get_value__mutmut_21': xǁFormatterǁ_get_value__mutmut_21, 
        'xǁFormatterǁ_get_value__mutmut_22': xǁFormatterǁ_get_value__mutmut_22, 
        'xǁFormatterǁ_get_value__mutmut_23': xǁFormatterǁ_get_value__mutmut_23
    }
    
    def _get_value(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFormatterǁ_get_value__mutmut_orig"), object.__getattribute__(self, "xǁFormatterǁ_get_value__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_value.__signature__ = _mutmut_signature(xǁFormatterǁ_get_value__mutmut_orig)
    xǁFormatterǁ_get_value__mutmut_orig.__name__ = 'xǁFormatterǁ_get_value'

    def xǁFormatterǁ_format__mutmut_orig(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, defaults)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_1(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = None

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, defaults)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_2(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(None):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, defaults)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_3(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(None)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, defaults)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_4(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is not None:
                continue

            value = self._get_value(field_name, format_spec, defaults)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_5(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                break

            value = self._get_value(field_name, format_spec, defaults)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_6(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = None
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_7(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(None, format_spec, defaults)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_8(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, None, defaults)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_9(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, None)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_10(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(format_spec, defaults)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_11(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, defaults)
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_12(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, )
            result.append(mapper(str(value)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_13(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, defaults)
            result.append(None)

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_14(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, defaults)
            result.append(mapper(None))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_15(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, defaults)
            result.append(mapper(str(None)))

        return "".join(result)

    def xǁFormatterǁ_format__mutmut_16(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, defaults)
            result.append(mapper(str(value)))

        return "".join(None)

    def xǁFormatterǁ_format__mutmut_17(self, string: str, mapper: Callable[[str], str], defaults: dict[str, str]) -> str:
        result = []

        for literal_text, field_name, format_spec, _conversion in _stringformatter.parse(string):
            if literal_text:
                result.append(literal_text)

            if field_name is None:
                continue

            value = self._get_value(field_name, format_spec, defaults)
            result.append(mapper(str(value)))

        return "XXXX".join(result)
    
    xǁFormatterǁ_format__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFormatterǁ_format__mutmut_1': xǁFormatterǁ_format__mutmut_1, 
        'xǁFormatterǁ_format__mutmut_2': xǁFormatterǁ_format__mutmut_2, 
        'xǁFormatterǁ_format__mutmut_3': xǁFormatterǁ_format__mutmut_3, 
        'xǁFormatterǁ_format__mutmut_4': xǁFormatterǁ_format__mutmut_4, 
        'xǁFormatterǁ_format__mutmut_5': xǁFormatterǁ_format__mutmut_5, 
        'xǁFormatterǁ_format__mutmut_6': xǁFormatterǁ_format__mutmut_6, 
        'xǁFormatterǁ_format__mutmut_7': xǁFormatterǁ_format__mutmut_7, 
        'xǁFormatterǁ_format__mutmut_8': xǁFormatterǁ_format__mutmut_8, 
        'xǁFormatterǁ_format__mutmut_9': xǁFormatterǁ_format__mutmut_9, 
        'xǁFormatterǁ_format__mutmut_10': xǁFormatterǁ_format__mutmut_10, 
        'xǁFormatterǁ_format__mutmut_11': xǁFormatterǁ_format__mutmut_11, 
        'xǁFormatterǁ_format__mutmut_12': xǁFormatterǁ_format__mutmut_12, 
        'xǁFormatterǁ_format__mutmut_13': xǁFormatterǁ_format__mutmut_13, 
        'xǁFormatterǁ_format__mutmut_14': xǁFormatterǁ_format__mutmut_14, 
        'xǁFormatterǁ_format__mutmut_15': xǁFormatterǁ_format__mutmut_15, 
        'xǁFormatterǁ_format__mutmut_16': xǁFormatterǁ_format__mutmut_16, 
        'xǁFormatterǁ_format__mutmut_17': xǁFormatterǁ_format__mutmut_17
    }
    
    def _format(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFormatterǁ_format__mutmut_orig"), object.__getattribute__(self, "xǁFormatterǁ_format__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _format.__signature__ = _mutmut_signature(xǁFormatterǁ_format__mutmut_orig)
    xǁFormatterǁ_format__mutmut_orig.__name__ = 'xǁFormatterǁ_format'

    def xǁFormatterǁformat__mutmut_orig(self, string: str, defaults: dict[str, str] | None = None) -> str:
        return self._format(string, _identity, defaults or {})

    def xǁFormatterǁformat__mutmut_1(self, string: str, defaults: dict[str, str] | None = None) -> str:
        return self._format(None, _identity, defaults or {})

    def xǁFormatterǁformat__mutmut_2(self, string: str, defaults: dict[str, str] | None = None) -> str:
        return self._format(string, None, defaults or {})

    def xǁFormatterǁformat__mutmut_3(self, string: str, defaults: dict[str, str] | None = None) -> str:
        return self._format(string, _identity, None)

    def xǁFormatterǁformat__mutmut_4(self, string: str, defaults: dict[str, str] | None = None) -> str:
        return self._format(_identity, defaults or {})

    def xǁFormatterǁformat__mutmut_5(self, string: str, defaults: dict[str, str] | None = None) -> str:
        return self._format(string, defaults or {})

    def xǁFormatterǁformat__mutmut_6(self, string: str, defaults: dict[str, str] | None = None) -> str:
        return self._format(string, _identity, )

    def xǁFormatterǁformat__mutmut_7(self, string: str, defaults: dict[str, str] | None = None) -> str:
        return self._format(string, _identity, defaults and {})
    
    xǁFormatterǁformat__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFormatterǁformat__mutmut_1': xǁFormatterǁformat__mutmut_1, 
        'xǁFormatterǁformat__mutmut_2': xǁFormatterǁformat__mutmut_2, 
        'xǁFormatterǁformat__mutmut_3': xǁFormatterǁformat__mutmut_3, 
        'xǁFormatterǁformat__mutmut_4': xǁFormatterǁformat__mutmut_4, 
        'xǁFormatterǁformat__mutmut_5': xǁFormatterǁformat__mutmut_5, 
        'xǁFormatterǁformat__mutmut_6': xǁFormatterǁformat__mutmut_6, 
        'xǁFormatterǁformat__mutmut_7': xǁFormatterǁformat__mutmut_7
    }
    
    def format(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFormatterǁformat__mutmut_orig"), object.__getattribute__(self, "xǁFormatterǁformat__mutmut_mutants"), args, kwargs, self)
        return result 
    
    format.__signature__ = _mutmut_signature(xǁFormatterǁformat__mutmut_orig)
    xǁFormatterǁformat__mutmut_orig.__name__ = 'xǁFormatterǁformat'

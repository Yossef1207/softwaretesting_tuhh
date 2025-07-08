from __future__ import annotations

import re
from typing import Any, Generic, TypeVar


_BOOLEAN_TRUE = "yes", "1", "true", "on"
_BOOLEAN_FALSE = "no", "0", "false", "off"

_FILESIZE_RE = re.compile(r"^(?P<size>\d+(\.\d+)?)(?P<modifier>[km])?b?$", re.IGNORECASE)
_FILESIZE_UNITS = {
    "k": 2**10,
    "m": 2**20,
}

_KEYVALUE_RE = re.compile(r"^(?P<key>[^=\s]+)\s*=\s*(?P<value>.*)$")
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


def x_boolean__mutmut_orig(value: str) -> bool:
    if value.lower() not in _BOOLEAN_TRUE + _BOOLEAN_FALSE:
        raise ValueError(f"{value} is not one of {{{', '.join(_BOOLEAN_TRUE + _BOOLEAN_FALSE)}}}")

    return value.lower() in _BOOLEAN_TRUE


def x_boolean__mutmut_1(value: str) -> bool:
    if value.upper() not in _BOOLEAN_TRUE + _BOOLEAN_FALSE:
        raise ValueError(f"{value} is not one of {{{', '.join(_BOOLEAN_TRUE + _BOOLEAN_FALSE)}}}")

    return value.lower() in _BOOLEAN_TRUE


def x_boolean__mutmut_2(value: str) -> bool:
    if value.lower() in _BOOLEAN_TRUE + _BOOLEAN_FALSE:
        raise ValueError(f"{value} is not one of {{{', '.join(_BOOLEAN_TRUE + _BOOLEAN_FALSE)}}}")

    return value.lower() in _BOOLEAN_TRUE


def x_boolean__mutmut_3(value: str) -> bool:
    if value.lower() not in _BOOLEAN_TRUE - _BOOLEAN_FALSE:
        raise ValueError(f"{value} is not one of {{{', '.join(_BOOLEAN_TRUE + _BOOLEAN_FALSE)}}}")

    return value.lower() in _BOOLEAN_TRUE


def x_boolean__mutmut_4(value: str) -> bool:
    if value.lower() not in _BOOLEAN_TRUE + _BOOLEAN_FALSE:
        raise ValueError(None)

    return value.lower() in _BOOLEAN_TRUE


def x_boolean__mutmut_5(value: str) -> bool:
    if value.lower() not in _BOOLEAN_TRUE + _BOOLEAN_FALSE:
        raise ValueError(f"{value} is not one of {{{', '.join(None)}}}")

    return value.lower() in _BOOLEAN_TRUE


def x_boolean__mutmut_6(value: str) -> bool:
    if value.lower() not in _BOOLEAN_TRUE + _BOOLEAN_FALSE:
        raise ValueError(f"{value} is not one of {{{'XX, XX'.join(_BOOLEAN_TRUE + _BOOLEAN_FALSE)}}}")

    return value.lower() in _BOOLEAN_TRUE


def x_boolean__mutmut_7(value: str) -> bool:
    if value.lower() not in _BOOLEAN_TRUE + _BOOLEAN_FALSE:
        raise ValueError(f"{value} is not one of {{{', '.join(_BOOLEAN_TRUE - _BOOLEAN_FALSE)}}}")

    return value.lower() in _BOOLEAN_TRUE


def x_boolean__mutmut_8(value: str) -> bool:
    if value.lower() not in _BOOLEAN_TRUE + _BOOLEAN_FALSE:
        raise ValueError(f"{value} is not one of {{{', '.join(_BOOLEAN_TRUE + _BOOLEAN_FALSE)}}}")

    return value.upper() in _BOOLEAN_TRUE


def x_boolean__mutmut_9(value: str) -> bool:
    if value.lower() not in _BOOLEAN_TRUE + _BOOLEAN_FALSE:
        raise ValueError(f"{value} is not one of {{{', '.join(_BOOLEAN_TRUE + _BOOLEAN_FALSE)}}}")

    return value.lower() not in _BOOLEAN_TRUE

x_boolean__mutmut_mutants : ClassVar[MutantDict] = {
'x_boolean__mutmut_1': x_boolean__mutmut_1, 
    'x_boolean__mutmut_2': x_boolean__mutmut_2, 
    'x_boolean__mutmut_3': x_boolean__mutmut_3, 
    'x_boolean__mutmut_4': x_boolean__mutmut_4, 
    'x_boolean__mutmut_5': x_boolean__mutmut_5, 
    'x_boolean__mutmut_6': x_boolean__mutmut_6, 
    'x_boolean__mutmut_7': x_boolean__mutmut_7, 
    'x_boolean__mutmut_8': x_boolean__mutmut_8, 
    'x_boolean__mutmut_9': x_boolean__mutmut_9
}

def boolean(*args, **kwargs):
    result = _mutmut_trampoline(x_boolean__mutmut_orig, x_boolean__mutmut_mutants, args, kwargs)
    return result 

boolean.__signature__ = _mutmut_signature(x_boolean__mutmut_orig)
x_boolean__mutmut_orig.__name__ = 'x_boolean'


def x_comma_list__mutmut_orig(values: str) -> list[str]:
    return [val.strip() for val in values.split(",")]


def x_comma_list__mutmut_1(values: str) -> list[str]:
    return [val.strip() for val in values.split(None)]


def x_comma_list__mutmut_2(values: str) -> list[str]:
    return [val.strip() for val in values.rsplit(",")]


def x_comma_list__mutmut_3(values: str) -> list[str]:
    return [val.strip() for val in values.split("XX,XX")]

x_comma_list__mutmut_mutants : ClassVar[MutantDict] = {
'x_comma_list__mutmut_1': x_comma_list__mutmut_1, 
    'x_comma_list__mutmut_2': x_comma_list__mutmut_2, 
    'x_comma_list__mutmut_3': x_comma_list__mutmut_3
}

def comma_list(*args, **kwargs):
    result = _mutmut_trampoline(x_comma_list__mutmut_orig, x_comma_list__mutmut_mutants, args, kwargs)
    return result 

comma_list.__signature__ = _mutmut_signature(x_comma_list__mutmut_orig)
x_comma_list__mutmut_orig.__name__ = 'x_comma_list'


# noinspection PyPep8Naming
class comma_list_filter:
    def xǁcomma_list_filterǁ__init____mutmut_orig(self, acceptable: list[str], unique: bool = False):
        self.acceptable = tuple(acceptable)
        self.unique = unique
    def xǁcomma_list_filterǁ__init____mutmut_1(self, acceptable: list[str], unique: bool = True):
        self.acceptable = tuple(acceptable)
        self.unique = unique
    def xǁcomma_list_filterǁ__init____mutmut_2(self, acceptable: list[str], unique: bool = False):
        self.acceptable = None
        self.unique = unique
    def xǁcomma_list_filterǁ__init____mutmut_3(self, acceptable: list[str], unique: bool = False):
        self.acceptable = tuple(None)
        self.unique = unique
    def xǁcomma_list_filterǁ__init____mutmut_4(self, acceptable: list[str], unique: bool = False):
        self.acceptable = tuple(acceptable)
        self.unique = None
    
    xǁcomma_list_filterǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁcomma_list_filterǁ__init____mutmut_1': xǁcomma_list_filterǁ__init____mutmut_1, 
        'xǁcomma_list_filterǁ__init____mutmut_2': xǁcomma_list_filterǁ__init____mutmut_2, 
        'xǁcomma_list_filterǁ__init____mutmut_3': xǁcomma_list_filterǁ__init____mutmut_3, 
        'xǁcomma_list_filterǁ__init____mutmut_4': xǁcomma_list_filterǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁcomma_list_filterǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁcomma_list_filterǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁcomma_list_filterǁ__init____mutmut_orig)
    xǁcomma_list_filterǁ__init____mutmut_orig.__name__ = 'xǁcomma_list_filterǁ__init__'

    def xǁcomma_list_filterǁ__call____mutmut_orig(self, values: str) -> list[str]:
        res = [item for item in comma_list(values) if item in self.acceptable]
        return sorted(set(res)) if self.unique else res

    def xǁcomma_list_filterǁ__call____mutmut_1(self, values: str) -> list[str]:
        res = None
        return sorted(set(res)) if self.unique else res

    def xǁcomma_list_filterǁ__call____mutmut_2(self, values: str) -> list[str]:
        res = [item for item in comma_list(None) if item in self.acceptable]
        return sorted(set(res)) if self.unique else res

    def xǁcomma_list_filterǁ__call____mutmut_3(self, values: str) -> list[str]:
        res = [item for item in comma_list(values) if item not in self.acceptable]
        return sorted(set(res)) if self.unique else res

    def xǁcomma_list_filterǁ__call____mutmut_4(self, values: str) -> list[str]:
        res = [item for item in comma_list(values) if item in self.acceptable]
        return sorted(None) if self.unique else res

    def xǁcomma_list_filterǁ__call____mutmut_5(self, values: str) -> list[str]:
        res = [item for item in comma_list(values) if item in self.acceptable]
        return sorted(set(None)) if self.unique else res
    
    xǁcomma_list_filterǁ__call____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁcomma_list_filterǁ__call____mutmut_1': xǁcomma_list_filterǁ__call____mutmut_1, 
        'xǁcomma_list_filterǁ__call____mutmut_2': xǁcomma_list_filterǁ__call____mutmut_2, 
        'xǁcomma_list_filterǁ__call____mutmut_3': xǁcomma_list_filterǁ__call____mutmut_3, 
        'xǁcomma_list_filterǁ__call____mutmut_4': xǁcomma_list_filterǁ__call____mutmut_4, 
        'xǁcomma_list_filterǁ__call____mutmut_5': xǁcomma_list_filterǁ__call____mutmut_5
    }
    
    def __call__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁcomma_list_filterǁ__call____mutmut_orig"), object.__getattribute__(self, "xǁcomma_list_filterǁ__call____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __call__.__signature__ = _mutmut_signature(xǁcomma_list_filterǁ__call____mutmut_orig)
    xǁcomma_list_filterǁ__call____mutmut_orig.__name__ = 'xǁcomma_list_filterǁ__call__'

    def xǁcomma_list_filterǁ__hash____mutmut_orig(self):
        return hash((self.acceptable, self.unique))

    def xǁcomma_list_filterǁ__hash____mutmut_1(self):
        return hash(None)
    
    xǁcomma_list_filterǁ__hash____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁcomma_list_filterǁ__hash____mutmut_1': xǁcomma_list_filterǁ__hash____mutmut_1
    }
    
    def __hash__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁcomma_list_filterǁ__hash____mutmut_orig"), object.__getattribute__(self, "xǁcomma_list_filterǁ__hash____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __hash__.__signature__ = _mutmut_signature(xǁcomma_list_filterǁ__hash____mutmut_orig)
    xǁcomma_list_filterǁ__hash____mutmut_orig.__name__ = 'xǁcomma_list_filterǁ__hash__'


def x_filesize__mutmut_orig(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_1(value: str) -> int:
    match = None
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_2(value: str) -> int:
    match = _FILESIZE_RE.match(None)
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_3(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_4(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError(None)

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_5(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("XXInvalid file size formatXX")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_6(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_7(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("INVALID FILE SIZE FORMAT")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_8(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = None
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_9(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(None)
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_10(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["XXsizeXX"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_11(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["SIZE"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_12(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["Size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_13(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size = _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_14(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size /= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_15(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get(None, 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_16(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), None)

    return num(int, ge=1)(size)


def x_filesize__mutmut_17(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get(1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_18(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), )

    return num(int, ge=1)(size)


def x_filesize__mutmut_19(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").upper(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_20(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["XXmodifierXX"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_21(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["MODIFIER"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_22(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["Modifier"] or "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_23(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] and "").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_24(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "XXXX").lower(), 1)

    return num(int, ge=1)(size)


def x_filesize__mutmut_25(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 2)

    return num(int, ge=1)(size)


def x_filesize__mutmut_26(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=1)(None)


def x_filesize__mutmut_27(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(None, ge=1)(size)


def x_filesize__mutmut_28(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=None)(size)


def x_filesize__mutmut_29(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(ge=1)(size)


def x_filesize__mutmut_30(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, )(size)


def x_filesize__mutmut_31(value: str) -> int:
    match = _FILESIZE_RE.match(value.strip())
    if not match:
        raise ValueError("Invalid file size format")

    size = float(match["size"])
    size *= _FILESIZE_UNITS.get((match["modifier"] or "").lower(), 1)

    return num(int, ge=2)(size)

x_filesize__mutmut_mutants : ClassVar[MutantDict] = {
'x_filesize__mutmut_1': x_filesize__mutmut_1, 
    'x_filesize__mutmut_2': x_filesize__mutmut_2, 
    'x_filesize__mutmut_3': x_filesize__mutmut_3, 
    'x_filesize__mutmut_4': x_filesize__mutmut_4, 
    'x_filesize__mutmut_5': x_filesize__mutmut_5, 
    'x_filesize__mutmut_6': x_filesize__mutmut_6, 
    'x_filesize__mutmut_7': x_filesize__mutmut_7, 
    'x_filesize__mutmut_8': x_filesize__mutmut_8, 
    'x_filesize__mutmut_9': x_filesize__mutmut_9, 
    'x_filesize__mutmut_10': x_filesize__mutmut_10, 
    'x_filesize__mutmut_11': x_filesize__mutmut_11, 
    'x_filesize__mutmut_12': x_filesize__mutmut_12, 
    'x_filesize__mutmut_13': x_filesize__mutmut_13, 
    'x_filesize__mutmut_14': x_filesize__mutmut_14, 
    'x_filesize__mutmut_15': x_filesize__mutmut_15, 
    'x_filesize__mutmut_16': x_filesize__mutmut_16, 
    'x_filesize__mutmut_17': x_filesize__mutmut_17, 
    'x_filesize__mutmut_18': x_filesize__mutmut_18, 
    'x_filesize__mutmut_19': x_filesize__mutmut_19, 
    'x_filesize__mutmut_20': x_filesize__mutmut_20, 
    'x_filesize__mutmut_21': x_filesize__mutmut_21, 
    'x_filesize__mutmut_22': x_filesize__mutmut_22, 
    'x_filesize__mutmut_23': x_filesize__mutmut_23, 
    'x_filesize__mutmut_24': x_filesize__mutmut_24, 
    'x_filesize__mutmut_25': x_filesize__mutmut_25, 
    'x_filesize__mutmut_26': x_filesize__mutmut_26, 
    'x_filesize__mutmut_27': x_filesize__mutmut_27, 
    'x_filesize__mutmut_28': x_filesize__mutmut_28, 
    'x_filesize__mutmut_29': x_filesize__mutmut_29, 
    'x_filesize__mutmut_30': x_filesize__mutmut_30, 
    'x_filesize__mutmut_31': x_filesize__mutmut_31
}

def filesize(*args, **kwargs):
    result = _mutmut_trampoline(x_filesize__mutmut_orig, x_filesize__mutmut_mutants, args, kwargs)
    return result 

filesize.__signature__ = _mutmut_signature(x_filesize__mutmut_orig)
x_filesize__mutmut_orig.__name__ = 'x_filesize'


def x_keyvalue__mutmut_orig(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError("Invalid key=value format")

    return match["key"], match["value"]


def x_keyvalue__mutmut_1(value: str) -> tuple[str, str]:
    match = None
    if not match:
        raise ValueError("Invalid key=value format")

    return match["key"], match["value"]


def x_keyvalue__mutmut_2(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(None)
    if not match:
        raise ValueError("Invalid key=value format")

    return match["key"], match["value"]


def x_keyvalue__mutmut_3(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.rstrip())
    if not match:
        raise ValueError("Invalid key=value format")

    return match["key"], match["value"]


def x_keyvalue__mutmut_4(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if match:
        raise ValueError("Invalid key=value format")

    return match["key"], match["value"]


def x_keyvalue__mutmut_5(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError(None)

    return match["key"], match["value"]


def x_keyvalue__mutmut_6(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError("XXInvalid key=value formatXX")

    return match["key"], match["value"]


def x_keyvalue__mutmut_7(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError("invalid key=value format")

    return match["key"], match["value"]


def x_keyvalue__mutmut_8(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError("INVALID KEY=VALUE FORMAT")

    return match["key"], match["value"]


def x_keyvalue__mutmut_9(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError("Invalid key=value format")

    return match["XXkeyXX"], match["value"]


def x_keyvalue__mutmut_10(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError("Invalid key=value format")

    return match["KEY"], match["value"]


def x_keyvalue__mutmut_11(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError("Invalid key=value format")

    return match["Key"], match["value"]


def x_keyvalue__mutmut_12(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError("Invalid key=value format")

    return match["key"], match["XXvalueXX"]


def x_keyvalue__mutmut_13(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError("Invalid key=value format")

    return match["key"], match["VALUE"]


def x_keyvalue__mutmut_14(value: str) -> tuple[str, str]:
    match = _KEYVALUE_RE.match(value.lstrip())
    if not match:
        raise ValueError("Invalid key=value format")

    return match["key"], match["Value"]

x_keyvalue__mutmut_mutants : ClassVar[MutantDict] = {
'x_keyvalue__mutmut_1': x_keyvalue__mutmut_1, 
    'x_keyvalue__mutmut_2': x_keyvalue__mutmut_2, 
    'x_keyvalue__mutmut_3': x_keyvalue__mutmut_3, 
    'x_keyvalue__mutmut_4': x_keyvalue__mutmut_4, 
    'x_keyvalue__mutmut_5': x_keyvalue__mutmut_5, 
    'x_keyvalue__mutmut_6': x_keyvalue__mutmut_6, 
    'x_keyvalue__mutmut_7': x_keyvalue__mutmut_7, 
    'x_keyvalue__mutmut_8': x_keyvalue__mutmut_8, 
    'x_keyvalue__mutmut_9': x_keyvalue__mutmut_9, 
    'x_keyvalue__mutmut_10': x_keyvalue__mutmut_10, 
    'x_keyvalue__mutmut_11': x_keyvalue__mutmut_11, 
    'x_keyvalue__mutmut_12': x_keyvalue__mutmut_12, 
    'x_keyvalue__mutmut_13': x_keyvalue__mutmut_13, 
    'x_keyvalue__mutmut_14': x_keyvalue__mutmut_14
}

def keyvalue(*args, **kwargs):
    result = _mutmut_trampoline(x_keyvalue__mutmut_orig, x_keyvalue__mutmut_mutants, args, kwargs)
    return result 

keyvalue.__signature__ = _mutmut_signature(x_keyvalue__mutmut_orig)
x_keyvalue__mutmut_orig.__name__ = 'x_keyvalue'


_TNum = TypeVar("_TNum", int, float)


# noinspection PyPep8Naming
class num(Generic[_TNum]):
    def xǁnumǁ__init____mutmut_orig(
        self,
        numtype: type[_TNum],
        ge: _TNum | None = None,
        gt: _TNum | None = None,
        le: _TNum | None = None,
        lt: _TNum | None = None,
    ):
        self.numtype: type[_TNum] = numtype
        self.ge: _TNum | None = ge
        self.gt: _TNum | None = gt
        self.le: _TNum | None = le
        self.lt: _TNum | None = lt
        self.__name__ = numtype.__name__
    def xǁnumǁ__init____mutmut_1(
        self,
        numtype: type[_TNum],
        ge: _TNum | None = None,
        gt: _TNum | None = None,
        le: _TNum | None = None,
        lt: _TNum | None = None,
    ):
        self.numtype: type[_TNum] = None
        self.ge: _TNum | None = ge
        self.gt: _TNum | None = gt
        self.le: _TNum | None = le
        self.lt: _TNum | None = lt
        self.__name__ = numtype.__name__
    def xǁnumǁ__init____mutmut_2(
        self,
        numtype: type[_TNum],
        ge: _TNum | None = None,
        gt: _TNum | None = None,
        le: _TNum | None = None,
        lt: _TNum | None = None,
    ):
        self.numtype: type[_TNum] = numtype
        self.ge: _TNum | None = None
        self.gt: _TNum | None = gt
        self.le: _TNum | None = le
        self.lt: _TNum | None = lt
        self.__name__ = numtype.__name__
    def xǁnumǁ__init____mutmut_3(
        self,
        numtype: type[_TNum],
        ge: _TNum | None = None,
        gt: _TNum | None = None,
        le: _TNum | None = None,
        lt: _TNum | None = None,
    ):
        self.numtype: type[_TNum] = numtype
        self.ge: _TNum | None = ge
        self.gt: _TNum | None = None
        self.le: _TNum | None = le
        self.lt: _TNum | None = lt
        self.__name__ = numtype.__name__
    def xǁnumǁ__init____mutmut_4(
        self,
        numtype: type[_TNum],
        ge: _TNum | None = None,
        gt: _TNum | None = None,
        le: _TNum | None = None,
        lt: _TNum | None = None,
    ):
        self.numtype: type[_TNum] = numtype
        self.ge: _TNum | None = ge
        self.gt: _TNum | None = gt
        self.le: _TNum | None = None
        self.lt: _TNum | None = lt
        self.__name__ = numtype.__name__
    def xǁnumǁ__init____mutmut_5(
        self,
        numtype: type[_TNum],
        ge: _TNum | None = None,
        gt: _TNum | None = None,
        le: _TNum | None = None,
        lt: _TNum | None = None,
    ):
        self.numtype: type[_TNum] = numtype
        self.ge: _TNum | None = ge
        self.gt: _TNum | None = gt
        self.le: _TNum | None = le
        self.lt: _TNum | None = None
        self.__name__ = numtype.__name__
    def xǁnumǁ__init____mutmut_6(
        self,
        numtype: type[_TNum],
        ge: _TNum | None = None,
        gt: _TNum | None = None,
        le: _TNum | None = None,
        lt: _TNum | None = None,
    ):
        self.numtype: type[_TNum] = numtype
        self.ge: _TNum | None = ge
        self.gt: _TNum | None = gt
        self.le: _TNum | None = le
        self.lt: _TNum | None = lt
        self.__name__ = None
    
    xǁnumǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁnumǁ__init____mutmut_1': xǁnumǁ__init____mutmut_1, 
        'xǁnumǁ__init____mutmut_2': xǁnumǁ__init____mutmut_2, 
        'xǁnumǁ__init____mutmut_3': xǁnumǁ__init____mutmut_3, 
        'xǁnumǁ__init____mutmut_4': xǁnumǁ__init____mutmut_4, 
        'xǁnumǁ__init____mutmut_5': xǁnumǁ__init____mutmut_5, 
        'xǁnumǁ__init____mutmut_6': xǁnumǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁnumǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁnumǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁnumǁ__init____mutmut_orig)
    xǁnumǁ__init____mutmut_orig.__name__ = 'xǁnumǁ__init__'

    def xǁnumǁ__call____mutmut_orig(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_1(self, value: Any) -> _TNum:
        val: _TNum = None

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_2(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(None)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_3(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_4(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None or val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_5(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val <= self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_6(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(None)
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_7(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_8(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None or val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_9(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val < self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_10(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(None)
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_11(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_12(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None or val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_13(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val >= self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_14(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(None)
        if self.lt is not None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_15(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is None and val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_16(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None or val >= self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_17(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val > self.lt:
            raise ValueError(f"{self.__name__} value must be <{self.lt}, but is {val}")

        return val

    def xǁnumǁ__call____mutmut_18(self, value: Any) -> _TNum:
        val: _TNum = self.numtype(value)

        if self.ge is not None and val < self.ge:
            raise ValueError(f"{self.__name__} value must be >={self.ge}, but is {val}")
        if self.gt is not None and val <= self.gt:
            raise ValueError(f"{self.__name__} value must be >{self.gt}, but is {val}")
        if self.le is not None and val > self.le:
            raise ValueError(f"{self.__name__} value must be <={self.le}, but is {val}")
        if self.lt is not None and val >= self.lt:
            raise ValueError(None)

        return val
    
    xǁnumǁ__call____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁnumǁ__call____mutmut_1': xǁnumǁ__call____mutmut_1, 
        'xǁnumǁ__call____mutmut_2': xǁnumǁ__call____mutmut_2, 
        'xǁnumǁ__call____mutmut_3': xǁnumǁ__call____mutmut_3, 
        'xǁnumǁ__call____mutmut_4': xǁnumǁ__call____mutmut_4, 
        'xǁnumǁ__call____mutmut_5': xǁnumǁ__call____mutmut_5, 
        'xǁnumǁ__call____mutmut_6': xǁnumǁ__call____mutmut_6, 
        'xǁnumǁ__call____mutmut_7': xǁnumǁ__call____mutmut_7, 
        'xǁnumǁ__call____mutmut_8': xǁnumǁ__call____mutmut_8, 
        'xǁnumǁ__call____mutmut_9': xǁnumǁ__call____mutmut_9, 
        'xǁnumǁ__call____mutmut_10': xǁnumǁ__call____mutmut_10, 
        'xǁnumǁ__call____mutmut_11': xǁnumǁ__call____mutmut_11, 
        'xǁnumǁ__call____mutmut_12': xǁnumǁ__call____mutmut_12, 
        'xǁnumǁ__call____mutmut_13': xǁnumǁ__call____mutmut_13, 
        'xǁnumǁ__call____mutmut_14': xǁnumǁ__call____mutmut_14, 
        'xǁnumǁ__call____mutmut_15': xǁnumǁ__call____mutmut_15, 
        'xǁnumǁ__call____mutmut_16': xǁnumǁ__call____mutmut_16, 
        'xǁnumǁ__call____mutmut_17': xǁnumǁ__call____mutmut_17, 
        'xǁnumǁ__call____mutmut_18': xǁnumǁ__call____mutmut_18
    }
    
    def __call__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁnumǁ__call____mutmut_orig"), object.__getattribute__(self, "xǁnumǁ__call____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __call__.__signature__ = _mutmut_signature(xǁnumǁ__call____mutmut_orig)
    xǁnumǁ__call____mutmut_orig.__name__ = 'xǁnumǁ__call__'

    def xǁnumǁ__hash____mutmut_orig(self) -> int:
        return hash((self.numtype, self.ge, self.gt, self.le, self.lt))

    def xǁnumǁ__hash____mutmut_1(self) -> int:
        return hash(None)
    
    xǁnumǁ__hash____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁnumǁ__hash____mutmut_1': xǁnumǁ__hash____mutmut_1
    }
    
    def __hash__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁnumǁ__hash____mutmut_orig"), object.__getattribute__(self, "xǁnumǁ__hash____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __hash__.__signature__ = _mutmut_signature(xǁnumǁ__hash____mutmut_orig)
    xǁnumǁ__hash____mutmut_orig.__name__ = 'xǁnumǁ__hash__'


__all__ = [
    "boolean",
    "comma_list",
    "comma_list_filter",
    "filesize",
    "keyvalue",
    "num",
]

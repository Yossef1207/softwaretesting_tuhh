from __future__ import annotations

import re
from collections.abc import Callable
from datetime import datetime, timezone, tzinfo
from typing import Generic, TypeVar

from isodate import LOCAL, parse_datetime  # type: ignore[import]


UTC = timezone.utc
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


def x_now__mutmut_orig(tz: tzinfo = UTC) -> datetime:
    return datetime.now(tz=tz)


def x_now__mutmut_1(tz: tzinfo = UTC) -> datetime:
    return datetime.now(tz=None)

x_now__mutmut_mutants : ClassVar[MutantDict] = {
'x_now__mutmut_1': x_now__mutmut_1
}

def now(*args, **kwargs):
    result = _mutmut_trampoline(x_now__mutmut_orig, x_now__mutmut_mutants, args, kwargs)
    return result 

now.__signature__ = _mutmut_signature(x_now__mutmut_orig)
x_now__mutmut_orig.__name__ = 'x_now'


def x_localnow__mutmut_orig() -> datetime:
    return datetime.now(tz=LOCAL)


def x_localnow__mutmut_1() -> datetime:
    return datetime.now(tz=None)

x_localnow__mutmut_mutants : ClassVar[MutantDict] = {
'x_localnow__mutmut_1': x_localnow__mutmut_1
}

def localnow(*args, **kwargs):
    result = _mutmut_trampoline(x_localnow__mutmut_orig, x_localnow__mutmut_mutants, args, kwargs)
    return result 

localnow.__signature__ = _mutmut_signature(x_localnow__mutmut_orig)
x_localnow__mutmut_orig.__name__ = 'x_localnow'


def x_fromtimestamp__mutmut_orig(timestamp: float, tz: tzinfo = UTC) -> datetime:
    return datetime.fromtimestamp(timestamp, tz=tz)


def x_fromtimestamp__mutmut_1(timestamp: float, tz: tzinfo = UTC) -> datetime:
    return datetime.fromtimestamp(None, tz=tz)


def x_fromtimestamp__mutmut_2(timestamp: float, tz: tzinfo = UTC) -> datetime:
    return datetime.fromtimestamp(timestamp, tz=None)


def x_fromtimestamp__mutmut_3(timestamp: float, tz: tzinfo = UTC) -> datetime:
    return datetime.fromtimestamp(tz=tz)


def x_fromtimestamp__mutmut_4(timestamp: float, tz: tzinfo = UTC) -> datetime:
    return datetime.fromtimestamp(timestamp, )

x_fromtimestamp__mutmut_mutants : ClassVar[MutantDict] = {
'x_fromtimestamp__mutmut_1': x_fromtimestamp__mutmut_1, 
    'x_fromtimestamp__mutmut_2': x_fromtimestamp__mutmut_2, 
    'x_fromtimestamp__mutmut_3': x_fromtimestamp__mutmut_3, 
    'x_fromtimestamp__mutmut_4': x_fromtimestamp__mutmut_4
}

def fromtimestamp(*args, **kwargs):
    result = _mutmut_trampoline(x_fromtimestamp__mutmut_orig, x_fromtimestamp__mutmut_mutants, args, kwargs)
    return result 

fromtimestamp.__signature__ = _mutmut_signature(x_fromtimestamp__mutmut_orig)
x_fromtimestamp__mutmut_orig.__name__ = 'x_fromtimestamp'


def x_fromlocaltimestamp__mutmut_orig(timestamp: float) -> datetime:
    return datetime.fromtimestamp(timestamp, tz=LOCAL)


def x_fromlocaltimestamp__mutmut_1(timestamp: float) -> datetime:
    return datetime.fromtimestamp(None, tz=LOCAL)


def x_fromlocaltimestamp__mutmut_2(timestamp: float) -> datetime:
    return datetime.fromtimestamp(timestamp, tz=None)


def x_fromlocaltimestamp__mutmut_3(timestamp: float) -> datetime:
    return datetime.fromtimestamp(tz=LOCAL)


def x_fromlocaltimestamp__mutmut_4(timestamp: float) -> datetime:
    return datetime.fromtimestamp(timestamp, )

x_fromlocaltimestamp__mutmut_mutants : ClassVar[MutantDict] = {
'x_fromlocaltimestamp__mutmut_1': x_fromlocaltimestamp__mutmut_1, 
    'x_fromlocaltimestamp__mutmut_2': x_fromlocaltimestamp__mutmut_2, 
    'x_fromlocaltimestamp__mutmut_3': x_fromlocaltimestamp__mutmut_3, 
    'x_fromlocaltimestamp__mutmut_4': x_fromlocaltimestamp__mutmut_4
}

def fromlocaltimestamp(*args, **kwargs):
    result = _mutmut_trampoline(x_fromlocaltimestamp__mutmut_orig, x_fromlocaltimestamp__mutmut_mutants, args, kwargs)
    return result 

fromlocaltimestamp.__signature__ = _mutmut_signature(x_fromlocaltimestamp__mutmut_orig)
x_fromlocaltimestamp__mutmut_orig.__name__ = 'x_fromlocaltimestamp'


_THMS = TypeVar("_THMS", int, float)


class _HoursMinutesSeconds(Generic[_THMS]):
    """
    Convert an optionally negative HMS-timestamp string to seconds, as float or int

    Accepted formats:

    - seconds
    - minutes":"seconds
    - hours":"minutes":"seconds
    - seconds"s"
    - minutes"m"
    - hours"h"
    - minutes"m"seconds"s"
    - hours"h"seconds"s"
    - hours"h"minutes"m"
    - hours"h"minutes"m"seconds"s"
    """

    __name__ = "hours_minutes_seconds"

    _re_float = re.compile(
        r"^-?\d+(?:\.\d+)?$",
    )
    _re_s = re.compile(
        r"""
            ^
            -?
            (?P<seconds>\d+(?:\.\d+)?)
            s
            $
        """,
        re.VERBOSE | re.IGNORECASE,
    )
    # noinspection RegExpSuspiciousBackref
    _re_ms = re.compile(
        r"""
            ^
            -?
            (?P<minutes>\d+)
            (?:(?P<sep>m)|:(?=.))
            (?:
                (?P<seconds>[0-5]?[0-9](?:\.\d+)?)
                (?(sep)s|)
            )?
            $
        """,
        re.VERBOSE | re.IGNORECASE,
    )
    # noinspection RegExpSuspiciousBackref
    _re_hms = re.compile(
        r"""
            ^
            -?
            (?P<hours>\d+)
            (?:(?P<sep>h)|:(?=.))
            (?:
                (?P<minutes>[0-5]?[0-9])
                (?(sep)m|:(?=.))
            )?
            (?:
                (?P<seconds>[0-5]?[0-9](?:\.\d+)?)
                (?(sep)s|)
            )?
            $
        """,
        re.VERBOSE | re.IGNORECASE,
    )

    def xǁ_HoursMinutesSecondsǁ__init____mutmut_orig(self, return_type: type[_THMS]):
        self._return_type: type[_THMS] = return_type

    def xǁ_HoursMinutesSecondsǁ__init____mutmut_1(self, return_type: type[_THMS]):
        self._return_type: type[_THMS] = None
    
    xǁ_HoursMinutesSecondsǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁ_HoursMinutesSecondsǁ__init____mutmut_1': xǁ_HoursMinutesSecondsǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁ_HoursMinutesSecondsǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁ_HoursMinutesSecondsǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁ_HoursMinutesSecondsǁ__init____mutmut_orig)
    xǁ_HoursMinutesSecondsǁ__init____mutmut_orig.__name__ = 'xǁ_HoursMinutesSecondsǁ__init__'

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_orig(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_1(self, value: str) -> _THMS:
        if self._re_float.match(None):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_2(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(None)

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_3(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(None))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_4(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = None
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_5(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(None) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_6(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) and self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_7(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(None) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_8(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) and self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_9(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(None)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_10(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_11(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = None

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_12(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = None
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_13(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 1.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_14(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds = float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_15(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds -= float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_16(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(None) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_17(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get(None) or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_18(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("XXhoursXX") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_19(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("HOURS") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_20(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("Hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_21(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") and 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_22(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 1.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_23(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) / 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_24(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3601.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_25(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds = float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_26(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds -= float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_27(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(None) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_28(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get(None) or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_29(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("XXminutesXX") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_30(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("MINUTES") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_31(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("Minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_32(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") and 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_33(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 1.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_34(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) / 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_35(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 61.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_36(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds = float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_37(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds -= float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_38(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(None)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_39(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get(None) or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_40(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("XXsecondsXX") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_41(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("SECONDS") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_42(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("Seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_43(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") and 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_44(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 1.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_45(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = None

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_46(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = +seconds if value[0] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_47(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[1] == "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_48(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] != "-" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_49(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "XX-XX" else seconds

        return self._return_type(res)

    def xǁ_HoursMinutesSecondsǁ__call____mutmut_50(self, value: str) -> _THMS:
        if self._re_float.match(value):
            return self._return_type(float(value))

        match = self._re_s.match(value) or self._re_ms.match(value) or self._re_hms.match(value)
        if not match:
            raise ValueError

        data = match.groupdict()

        seconds = 0.0
        seconds += float(data.get("hours") or 0.0) * 3600.0
        seconds += float(data.get("minutes") or 0.0) * 60.0
        seconds += float(data.get("seconds") or 0.0)

        res = -seconds if value[0] == "-" else seconds

        return self._return_type(None)
    
    xǁ_HoursMinutesSecondsǁ__call____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁ_HoursMinutesSecondsǁ__call____mutmut_1': xǁ_HoursMinutesSecondsǁ__call____mutmut_1, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_2': xǁ_HoursMinutesSecondsǁ__call____mutmut_2, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_3': xǁ_HoursMinutesSecondsǁ__call____mutmut_3, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_4': xǁ_HoursMinutesSecondsǁ__call____mutmut_4, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_5': xǁ_HoursMinutesSecondsǁ__call____mutmut_5, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_6': xǁ_HoursMinutesSecondsǁ__call____mutmut_6, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_7': xǁ_HoursMinutesSecondsǁ__call____mutmut_7, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_8': xǁ_HoursMinutesSecondsǁ__call____mutmut_8, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_9': xǁ_HoursMinutesSecondsǁ__call____mutmut_9, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_10': xǁ_HoursMinutesSecondsǁ__call____mutmut_10, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_11': xǁ_HoursMinutesSecondsǁ__call____mutmut_11, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_12': xǁ_HoursMinutesSecondsǁ__call____mutmut_12, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_13': xǁ_HoursMinutesSecondsǁ__call____mutmut_13, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_14': xǁ_HoursMinutesSecondsǁ__call____mutmut_14, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_15': xǁ_HoursMinutesSecondsǁ__call____mutmut_15, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_16': xǁ_HoursMinutesSecondsǁ__call____mutmut_16, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_17': xǁ_HoursMinutesSecondsǁ__call____mutmut_17, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_18': xǁ_HoursMinutesSecondsǁ__call____mutmut_18, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_19': xǁ_HoursMinutesSecondsǁ__call____mutmut_19, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_20': xǁ_HoursMinutesSecondsǁ__call____mutmut_20, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_21': xǁ_HoursMinutesSecondsǁ__call____mutmut_21, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_22': xǁ_HoursMinutesSecondsǁ__call____mutmut_22, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_23': xǁ_HoursMinutesSecondsǁ__call____mutmut_23, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_24': xǁ_HoursMinutesSecondsǁ__call____mutmut_24, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_25': xǁ_HoursMinutesSecondsǁ__call____mutmut_25, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_26': xǁ_HoursMinutesSecondsǁ__call____mutmut_26, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_27': xǁ_HoursMinutesSecondsǁ__call____mutmut_27, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_28': xǁ_HoursMinutesSecondsǁ__call____mutmut_28, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_29': xǁ_HoursMinutesSecondsǁ__call____mutmut_29, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_30': xǁ_HoursMinutesSecondsǁ__call____mutmut_30, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_31': xǁ_HoursMinutesSecondsǁ__call____mutmut_31, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_32': xǁ_HoursMinutesSecondsǁ__call____mutmut_32, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_33': xǁ_HoursMinutesSecondsǁ__call____mutmut_33, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_34': xǁ_HoursMinutesSecondsǁ__call____mutmut_34, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_35': xǁ_HoursMinutesSecondsǁ__call____mutmut_35, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_36': xǁ_HoursMinutesSecondsǁ__call____mutmut_36, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_37': xǁ_HoursMinutesSecondsǁ__call____mutmut_37, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_38': xǁ_HoursMinutesSecondsǁ__call____mutmut_38, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_39': xǁ_HoursMinutesSecondsǁ__call____mutmut_39, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_40': xǁ_HoursMinutesSecondsǁ__call____mutmut_40, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_41': xǁ_HoursMinutesSecondsǁ__call____mutmut_41, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_42': xǁ_HoursMinutesSecondsǁ__call____mutmut_42, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_43': xǁ_HoursMinutesSecondsǁ__call____mutmut_43, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_44': xǁ_HoursMinutesSecondsǁ__call____mutmut_44, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_45': xǁ_HoursMinutesSecondsǁ__call____mutmut_45, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_46': xǁ_HoursMinutesSecondsǁ__call____mutmut_46, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_47': xǁ_HoursMinutesSecondsǁ__call____mutmut_47, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_48': xǁ_HoursMinutesSecondsǁ__call____mutmut_48, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_49': xǁ_HoursMinutesSecondsǁ__call____mutmut_49, 
        'xǁ_HoursMinutesSecondsǁ__call____mutmut_50': xǁ_HoursMinutesSecondsǁ__call____mutmut_50
    }
    
    def __call__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁ_HoursMinutesSecondsǁ__call____mutmut_orig"), object.__getattribute__(self, "xǁ_HoursMinutesSecondsǁ__call____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __call__.__signature__ = _mutmut_signature(xǁ_HoursMinutesSecondsǁ__call____mutmut_orig)
    xǁ_HoursMinutesSecondsǁ__call____mutmut_orig.__name__ = 'xǁ_HoursMinutesSecondsǁ__call__'


hours_minutes_seconds: Callable[[str], int] = _HoursMinutesSeconds[int](int)
hours_minutes_seconds_float: Callable[[str], float] = _HoursMinutesSeconds[float](float)


def x_seconds_to_hhmmss__mutmut_orig(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_1(seconds):
    hours, seconds = None
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_2(seconds):
    hours, seconds = divmod(None, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_3(seconds):
    hours, seconds = divmod(seconds, None)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_4(seconds):
    hours, seconds = divmod(3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_5(seconds):
    hours, seconds = divmod(seconds, )
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_6(seconds):
    hours, seconds = divmod(seconds, 3601)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_7(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = None
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_8(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(None, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_9(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, None)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_10(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_11(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, )
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_12(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 61)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_13(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        None,
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_14(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        None,
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_15(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        None,
    )


def x_seconds_to_hhmmss__mutmut_16(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_17(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_18(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        )


def x_seconds_to_hhmmss__mutmut_19(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "XX{0:02d}:{1:02d}:{2}XX".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_20(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02D}:{1:02D}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_21(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(None),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_22(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(None),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_23(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(None) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_24(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "XX{0:02.1f}XX".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_25(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1F}".format(seconds) if seconds % 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_26(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds / 1 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_27(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 2 else "{0:02d}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_28(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(None),
    )


def x_seconds_to_hhmmss__mutmut_29(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "XX{0:02d}XX".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_30(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02D}".format(int(seconds)),
    )


def x_seconds_to_hhmmss__mutmut_31(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "{0:02d}:{1:02d}:{2}".format(
        int(hours),
        int(minutes),
        "{0:02.1f}".format(seconds) if seconds % 1 else "{0:02d}".format(int(None)),
    )

x_seconds_to_hhmmss__mutmut_mutants : ClassVar[MutantDict] = {
'x_seconds_to_hhmmss__mutmut_1': x_seconds_to_hhmmss__mutmut_1, 
    'x_seconds_to_hhmmss__mutmut_2': x_seconds_to_hhmmss__mutmut_2, 
    'x_seconds_to_hhmmss__mutmut_3': x_seconds_to_hhmmss__mutmut_3, 
    'x_seconds_to_hhmmss__mutmut_4': x_seconds_to_hhmmss__mutmut_4, 
    'x_seconds_to_hhmmss__mutmut_5': x_seconds_to_hhmmss__mutmut_5, 
    'x_seconds_to_hhmmss__mutmut_6': x_seconds_to_hhmmss__mutmut_6, 
    'x_seconds_to_hhmmss__mutmut_7': x_seconds_to_hhmmss__mutmut_7, 
    'x_seconds_to_hhmmss__mutmut_8': x_seconds_to_hhmmss__mutmut_8, 
    'x_seconds_to_hhmmss__mutmut_9': x_seconds_to_hhmmss__mutmut_9, 
    'x_seconds_to_hhmmss__mutmut_10': x_seconds_to_hhmmss__mutmut_10, 
    'x_seconds_to_hhmmss__mutmut_11': x_seconds_to_hhmmss__mutmut_11, 
    'x_seconds_to_hhmmss__mutmut_12': x_seconds_to_hhmmss__mutmut_12, 
    'x_seconds_to_hhmmss__mutmut_13': x_seconds_to_hhmmss__mutmut_13, 
    'x_seconds_to_hhmmss__mutmut_14': x_seconds_to_hhmmss__mutmut_14, 
    'x_seconds_to_hhmmss__mutmut_15': x_seconds_to_hhmmss__mutmut_15, 
    'x_seconds_to_hhmmss__mutmut_16': x_seconds_to_hhmmss__mutmut_16, 
    'x_seconds_to_hhmmss__mutmut_17': x_seconds_to_hhmmss__mutmut_17, 
    'x_seconds_to_hhmmss__mutmut_18': x_seconds_to_hhmmss__mutmut_18, 
    'x_seconds_to_hhmmss__mutmut_19': x_seconds_to_hhmmss__mutmut_19, 
    'x_seconds_to_hhmmss__mutmut_20': x_seconds_to_hhmmss__mutmut_20, 
    'x_seconds_to_hhmmss__mutmut_21': x_seconds_to_hhmmss__mutmut_21, 
    'x_seconds_to_hhmmss__mutmut_22': x_seconds_to_hhmmss__mutmut_22, 
    'x_seconds_to_hhmmss__mutmut_23': x_seconds_to_hhmmss__mutmut_23, 
    'x_seconds_to_hhmmss__mutmut_24': x_seconds_to_hhmmss__mutmut_24, 
    'x_seconds_to_hhmmss__mutmut_25': x_seconds_to_hhmmss__mutmut_25, 
    'x_seconds_to_hhmmss__mutmut_26': x_seconds_to_hhmmss__mutmut_26, 
    'x_seconds_to_hhmmss__mutmut_27': x_seconds_to_hhmmss__mutmut_27, 
    'x_seconds_to_hhmmss__mutmut_28': x_seconds_to_hhmmss__mutmut_28, 
    'x_seconds_to_hhmmss__mutmut_29': x_seconds_to_hhmmss__mutmut_29, 
    'x_seconds_to_hhmmss__mutmut_30': x_seconds_to_hhmmss__mutmut_30, 
    'x_seconds_to_hhmmss__mutmut_31': x_seconds_to_hhmmss__mutmut_31
}

def seconds_to_hhmmss(*args, **kwargs):
    result = _mutmut_trampoline(x_seconds_to_hhmmss__mutmut_orig, x_seconds_to_hhmmss__mutmut_mutants, args, kwargs)
    return result 

seconds_to_hhmmss.__signature__ = _mutmut_signature(x_seconds_to_hhmmss__mutmut_orig)
x_seconds_to_hhmmss__mutmut_orig.__name__ = 'x_seconds_to_hhmmss'


__all__ = [
    "UTC",
    "LOCAL",
    "parse_datetime",
    "now",
    "localnow",
    "fromtimestamp",
    "fromlocaltimestamp",
    "hours_minutes_seconds",
    "hours_minutes_seconds_float",
    "seconds_to_hhmmss",
]

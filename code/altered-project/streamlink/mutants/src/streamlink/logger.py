from __future__ import annotations

import logging
import sys
import warnings
from collections.abc import Iterator
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING
from pathlib import Path
from sys import version_info
from threading import Lock
from typing import IO, TYPE_CHECKING, Literal

# noinspection PyProtectedMember
from warnings import WarningMessage

from streamlink.exceptions import StreamlinkWarning
from streamlink.utils.times import fromlocaltimestamp


if TYPE_CHECKING:
    _BaseLoggerClass = logging.Logger
else:
    _BaseLoggerClass = logging.getLoggerClass()
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


class StreamlinkLogger(_BaseLoggerClass):
    def xǁStreamlinkLoggerǁiter__mutmut_orig(self, level: int, messages: Iterator[str], *args, **kwargs) -> Iterator[str]:
        """
        Iterator wrapper for logging multiple items in a single call and checking log level only once
        """

        if not self.isEnabledFor(level):
            yield from messages

        for message in messages:
            self._log(level, message, args, **kwargs)
            yield message
    def xǁStreamlinkLoggerǁiter__mutmut_1(self, level: int, messages: Iterator[str], *args, **kwargs) -> Iterator[str]:
        """
        Iterator wrapper for logging multiple items in a single call and checking log level only once
        """

        if self.isEnabledFor(level):
            yield from messages

        for message in messages:
            self._log(level, message, args, **kwargs)
            yield message
    def xǁStreamlinkLoggerǁiter__mutmut_2(self, level: int, messages: Iterator[str], *args, **kwargs) -> Iterator[str]:
        """
        Iterator wrapper for logging multiple items in a single call and checking log level only once
        """

        if not self.isEnabledFor(None):
            yield from messages

        for message in messages:
            self._log(level, message, args, **kwargs)
            yield message
    def xǁStreamlinkLoggerǁiter__mutmut_3(self, level: int, messages: Iterator[str], *args, **kwargs) -> Iterator[str]:
        """
        Iterator wrapper for logging multiple items in a single call and checking log level only once
        """

        if not self.isEnabledFor(level):
            yield from messages

        for message in messages:
            self._log(None, message, args, **kwargs)
            yield message
    def xǁStreamlinkLoggerǁiter__mutmut_4(self, level: int, messages: Iterator[str], *args, **kwargs) -> Iterator[str]:
        """
        Iterator wrapper for logging multiple items in a single call and checking log level only once
        """

        if not self.isEnabledFor(level):
            yield from messages

        for message in messages:
            self._log(level, None, args, **kwargs)
            yield message
    def xǁStreamlinkLoggerǁiter__mutmut_5(self, level: int, messages: Iterator[str], *args, **kwargs) -> Iterator[str]:
        """
        Iterator wrapper for logging multiple items in a single call and checking log level only once
        """

        if not self.isEnabledFor(level):
            yield from messages

        for message in messages:
            self._log(level, message, None, **kwargs)
            yield message
    def xǁStreamlinkLoggerǁiter__mutmut_6(self, level: int, messages: Iterator[str], *args, **kwargs) -> Iterator[str]:
        """
        Iterator wrapper for logging multiple items in a single call and checking log level only once
        """

        if not self.isEnabledFor(level):
            yield from messages

        for message in messages:
            self._log(message, args, **kwargs)
            yield message
    def xǁStreamlinkLoggerǁiter__mutmut_7(self, level: int, messages: Iterator[str], *args, **kwargs) -> Iterator[str]:
        """
        Iterator wrapper for logging multiple items in a single call and checking log level only once
        """

        if not self.isEnabledFor(level):
            yield from messages

        for message in messages:
            self._log(level, args, **kwargs)
            yield message
    def xǁStreamlinkLoggerǁiter__mutmut_8(self, level: int, messages: Iterator[str], *args, **kwargs) -> Iterator[str]:
        """
        Iterator wrapper for logging multiple items in a single call and checking log level only once
        """

        if not self.isEnabledFor(level):
            yield from messages

        for message in messages:
            self._log(level, message, **kwargs)
            yield message
    def xǁStreamlinkLoggerǁiter__mutmut_9(self, level: int, messages: Iterator[str], *args, **kwargs) -> Iterator[str]:
        """
        Iterator wrapper for logging multiple items in a single call and checking log level only once
        """

        if not self.isEnabledFor(level):
            yield from messages

        for message in messages:
            self._log(level, message, args, )
            yield message
    
    xǁStreamlinkLoggerǁiter__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkLoggerǁiter__mutmut_1': xǁStreamlinkLoggerǁiter__mutmut_1, 
        'xǁStreamlinkLoggerǁiter__mutmut_2': xǁStreamlinkLoggerǁiter__mutmut_2, 
        'xǁStreamlinkLoggerǁiter__mutmut_3': xǁStreamlinkLoggerǁiter__mutmut_3, 
        'xǁStreamlinkLoggerǁiter__mutmut_4': xǁStreamlinkLoggerǁiter__mutmut_4, 
        'xǁStreamlinkLoggerǁiter__mutmut_5': xǁStreamlinkLoggerǁiter__mutmut_5, 
        'xǁStreamlinkLoggerǁiter__mutmut_6': xǁStreamlinkLoggerǁiter__mutmut_6, 
        'xǁStreamlinkLoggerǁiter__mutmut_7': xǁStreamlinkLoggerǁiter__mutmut_7, 
        'xǁStreamlinkLoggerǁiter__mutmut_8': xǁStreamlinkLoggerǁiter__mutmut_8, 
        'xǁStreamlinkLoggerǁiter__mutmut_9': xǁStreamlinkLoggerǁiter__mutmut_9
    }
    
    def iter(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁStreamlinkLoggerǁiter__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkLoggerǁiter__mutmut_mutants"), args, kwargs, self)
        return result 
    
    iter.__signature__ = _mutmut_signature(xǁStreamlinkLoggerǁiter__mutmut_orig)
    xǁStreamlinkLoggerǁiter__mutmut_orig.__name__ = 'xǁStreamlinkLoggerǁiter'


FORMAT_STYLE: Literal["%", "{", "$"] = "{"
FORMAT_BASE = "[{name}][{levelname}] {message}"
FORMAT_DATE = "%H:%M:%S"
REMOVE_BASE = ["streamlink", "streamlink_cli"]

# Make NONE ("none") the highest possible level that suppresses all log messages:
#  `logging.NOTSET` (equal to 0) can't be used as the "none" level because of `logging.Logger.getEffectiveLevel()`, which
#  loops through the logger instance's ancestor chain and checks whether the instance's level is NOTSET. If it is NOTSET,
#  then it continues with the parent logger, which means that if the level of `streamlink.logger.root` was set to "none" and
#  its value NOTSET, then it would continue with `logging.root` whose default level is `logging.WARNING` (equal to 30).
NONE = sys.maxsize
# Add "trace" and "all" to Streamlink's log levels
TRACE = 5
ALL = 2

# Define Streamlink's log levels (and register both lowercase and uppercase names)
_levelToNames = {
    NONE: "none",
    CRITICAL: "critical",
    ERROR: "error",
    WARNING: "warning",
    INFO: "info",
    DEBUG: "debug",
    TRACE: "trace",
    ALL: "all",
}

_custom_levels = TRACE, ALL


def x__logmethodfactory__mutmut_orig(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_1(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info > (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_2(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (4, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_3(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 12):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_4(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(None):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_5(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = None
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_6(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["XXstacklevelXX"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_7(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["STACKLEVEL"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_8(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["Stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_9(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 3
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_10(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(None, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_11(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, None, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_12(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, None, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_13(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_14(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_15(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_16(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, )

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_17(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(None):
                self._log(level, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_18(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(None, message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_19(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, None, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_20(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, None, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_21(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(message, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_22(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, args, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_23(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, **kws)

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_24(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, )

    method.__name__ = name
    return method


def x__logmethodfactory__mutmut_25(level: int, name: str):
    # fix module name that gets read from the call stack in the logging module
    # https://github.com/python/cpython/commit/5ca6d7469be53960843df39bb900e9c3359f127f
    if version_info >= (3, 11):

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                # increase the stacklevel by one and skip the `trace()` call here
                kws["stacklevel"] = 2
                self._log(level, message, args, **kws)

    else:

        def method(self, message, *args, **kws):
            if self.isEnabledFor(level):
                self._log(level, message, args, **kws)

    method.__name__ = None
    return method

x__logmethodfactory__mutmut_mutants : ClassVar[MutantDict] = {
'x__logmethodfactory__mutmut_1': x__logmethodfactory__mutmut_1, 
    'x__logmethodfactory__mutmut_2': x__logmethodfactory__mutmut_2, 
    'x__logmethodfactory__mutmut_3': x__logmethodfactory__mutmut_3, 
    'x__logmethodfactory__mutmut_4': x__logmethodfactory__mutmut_4, 
    'x__logmethodfactory__mutmut_5': x__logmethodfactory__mutmut_5, 
    'x__logmethodfactory__mutmut_6': x__logmethodfactory__mutmut_6, 
    'x__logmethodfactory__mutmut_7': x__logmethodfactory__mutmut_7, 
    'x__logmethodfactory__mutmut_8': x__logmethodfactory__mutmut_8, 
    'x__logmethodfactory__mutmut_9': x__logmethodfactory__mutmut_9, 
    'x__logmethodfactory__mutmut_10': x__logmethodfactory__mutmut_10, 
    'x__logmethodfactory__mutmut_11': x__logmethodfactory__mutmut_11, 
    'x__logmethodfactory__mutmut_12': x__logmethodfactory__mutmut_12, 
    'x__logmethodfactory__mutmut_13': x__logmethodfactory__mutmut_13, 
    'x__logmethodfactory__mutmut_14': x__logmethodfactory__mutmut_14, 
    'x__logmethodfactory__mutmut_15': x__logmethodfactory__mutmut_15, 
    'x__logmethodfactory__mutmut_16': x__logmethodfactory__mutmut_16, 
    'x__logmethodfactory__mutmut_17': x__logmethodfactory__mutmut_17, 
    'x__logmethodfactory__mutmut_18': x__logmethodfactory__mutmut_18, 
    'x__logmethodfactory__mutmut_19': x__logmethodfactory__mutmut_19, 
    'x__logmethodfactory__mutmut_20': x__logmethodfactory__mutmut_20, 
    'x__logmethodfactory__mutmut_21': x__logmethodfactory__mutmut_21, 
    'x__logmethodfactory__mutmut_22': x__logmethodfactory__mutmut_22, 
    'x__logmethodfactory__mutmut_23': x__logmethodfactory__mutmut_23, 
    'x__logmethodfactory__mutmut_24': x__logmethodfactory__mutmut_24, 
    'x__logmethodfactory__mutmut_25': x__logmethodfactory__mutmut_25
}

def _logmethodfactory(*args, **kwargs):
    result = _mutmut_trampoline(x__logmethodfactory__mutmut_orig, x__logmethodfactory__mutmut_mutants, args, kwargs)
    return result 

_logmethodfactory.__signature__ = _mutmut_signature(x__logmethodfactory__mutmut_orig)
x__logmethodfactory__mutmut_orig.__name__ = 'x__logmethodfactory'


for _level, _name in _levelToNames.items():
    logging.addLevelName(_level, _name.upper())
    logging.addLevelName(_level, _name)

    if _level in _custom_levels:
        setattr(StreamlinkLogger, _name, _logmethodfactory(_level, _name))


_config_lock = Lock()


class StringFormatter(logging.Formatter):
    def xǁStringFormatterǁ__init____mutmut_orig(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_1(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(**kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_2(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, )
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_3(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = None
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_4(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base and []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_5(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = None

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_6(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = None
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_7(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord(None, 1, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_8(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", None, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_9(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, None, 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_10(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", None, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_11(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, None, None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_12(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord(1, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_13(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_14(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_15(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_16(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_17(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, "", None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_18(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, "", None, )
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_19(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("XXXX", 1, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_20(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 2, "", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_21(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "XXXX", 1, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_22(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 2, "", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_23(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, "XXXX", None, None)
        super().format(rec)
    def xǁStringFormatterǁ__init____mutmut_24(self, *args, remove_base: list[str] | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_base = remove_base or []
        self._usesTime = super().usesTime()

        # Validate the format's fields
        rec = logging.LogRecord("", 1, "", 1, "", None, None)
        super().format(None)
    
    xǁStringFormatterǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStringFormatterǁ__init____mutmut_1': xǁStringFormatterǁ__init____mutmut_1, 
        'xǁStringFormatterǁ__init____mutmut_2': xǁStringFormatterǁ__init____mutmut_2, 
        'xǁStringFormatterǁ__init____mutmut_3': xǁStringFormatterǁ__init____mutmut_3, 
        'xǁStringFormatterǁ__init____mutmut_4': xǁStringFormatterǁ__init____mutmut_4, 
        'xǁStringFormatterǁ__init____mutmut_5': xǁStringFormatterǁ__init____mutmut_5, 
        'xǁStringFormatterǁ__init____mutmut_6': xǁStringFormatterǁ__init____mutmut_6, 
        'xǁStringFormatterǁ__init____mutmut_7': xǁStringFormatterǁ__init____mutmut_7, 
        'xǁStringFormatterǁ__init____mutmut_8': xǁStringFormatterǁ__init____mutmut_8, 
        'xǁStringFormatterǁ__init____mutmut_9': xǁStringFormatterǁ__init____mutmut_9, 
        'xǁStringFormatterǁ__init____mutmut_10': xǁStringFormatterǁ__init____mutmut_10, 
        'xǁStringFormatterǁ__init____mutmut_11': xǁStringFormatterǁ__init____mutmut_11, 
        'xǁStringFormatterǁ__init____mutmut_12': xǁStringFormatterǁ__init____mutmut_12, 
        'xǁStringFormatterǁ__init____mutmut_13': xǁStringFormatterǁ__init____mutmut_13, 
        'xǁStringFormatterǁ__init____mutmut_14': xǁStringFormatterǁ__init____mutmut_14, 
        'xǁStringFormatterǁ__init____mutmut_15': xǁStringFormatterǁ__init____mutmut_15, 
        'xǁStringFormatterǁ__init____mutmut_16': xǁStringFormatterǁ__init____mutmut_16, 
        'xǁStringFormatterǁ__init____mutmut_17': xǁStringFormatterǁ__init____mutmut_17, 
        'xǁStringFormatterǁ__init____mutmut_18': xǁStringFormatterǁ__init____mutmut_18, 
        'xǁStringFormatterǁ__init____mutmut_19': xǁStringFormatterǁ__init____mutmut_19, 
        'xǁStringFormatterǁ__init____mutmut_20': xǁStringFormatterǁ__init____mutmut_20, 
        'xǁStringFormatterǁ__init____mutmut_21': xǁStringFormatterǁ__init____mutmut_21, 
        'xǁStringFormatterǁ__init____mutmut_22': xǁStringFormatterǁ__init____mutmut_22, 
        'xǁStringFormatterǁ__init____mutmut_23': xǁStringFormatterǁ__init____mutmut_23, 
        'xǁStringFormatterǁ__init____mutmut_24': xǁStringFormatterǁ__init____mutmut_24
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStringFormatterǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStringFormatterǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStringFormatterǁ__init____mutmut_orig)
    xǁStringFormatterǁ__init____mutmut_orig.__name__ = 'xǁStringFormatterǁ__init__'

    def usesTime(self):
        return self._usesTime

    def xǁStringFormatterǁformatTime__mutmut_orig(self, record, datefmt=None):
        tdt = fromlocaltimestamp(record.created)

        return tdt.strftime(datefmt or self.default_time_format)

    def xǁStringFormatterǁformatTime__mutmut_1(self, record, datefmt=None):
        tdt = None

        return tdt.strftime(datefmt or self.default_time_format)

    def xǁStringFormatterǁformatTime__mutmut_2(self, record, datefmt=None):
        tdt = fromlocaltimestamp(None)

        return tdt.strftime(datefmt or self.default_time_format)

    def xǁStringFormatterǁformatTime__mutmut_3(self, record, datefmt=None):
        tdt = fromlocaltimestamp(record.created)

        return tdt.strftime(None)

    def xǁStringFormatterǁformatTime__mutmut_4(self, record, datefmt=None):
        tdt = fromlocaltimestamp(record.created)

        return tdt.strftime(datefmt and self.default_time_format)
    
    xǁStringFormatterǁformatTime__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStringFormatterǁformatTime__mutmut_1': xǁStringFormatterǁformatTime__mutmut_1, 
        'xǁStringFormatterǁformatTime__mutmut_2': xǁStringFormatterǁformatTime__mutmut_2, 
        'xǁStringFormatterǁformatTime__mutmut_3': xǁStringFormatterǁformatTime__mutmut_3, 
        'xǁStringFormatterǁformatTime__mutmut_4': xǁStringFormatterǁformatTime__mutmut_4
    }
    
    def formatTime(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStringFormatterǁformatTime__mutmut_orig"), object.__getattribute__(self, "xǁStringFormatterǁformatTime__mutmut_mutants"), args, kwargs, self)
        return result 
    
    formatTime.__signature__ = _mutmut_signature(xǁStringFormatterǁformatTime__mutmut_orig)
    xǁStringFormatterǁformatTime__mutmut_orig.__name__ = 'xǁStringFormatterǁformatTime'

    def xǁStringFormatterǁformat__mutmut_orig(self, record):
        for rbase in self._remove_base:
            record.name = record.name.replace(f"{rbase}.", "")
        record.levelname = record.levelname.lower()

        return super().format(record)

    def xǁStringFormatterǁformat__mutmut_1(self, record):
        for rbase in self._remove_base:
            record.name = None
        record.levelname = record.levelname.lower()

        return super().format(record)

    def xǁStringFormatterǁformat__mutmut_2(self, record):
        for rbase in self._remove_base:
            record.name = record.name.replace(None, "")
        record.levelname = record.levelname.lower()

        return super().format(record)

    def xǁStringFormatterǁformat__mutmut_3(self, record):
        for rbase in self._remove_base:
            record.name = record.name.replace(f"{rbase}.", None)
        record.levelname = record.levelname.lower()

        return super().format(record)

    def xǁStringFormatterǁformat__mutmut_4(self, record):
        for rbase in self._remove_base:
            record.name = record.name.replace("")
        record.levelname = record.levelname.lower()

        return super().format(record)

    def xǁStringFormatterǁformat__mutmut_5(self, record):
        for rbase in self._remove_base:
            record.name = record.name.replace(f"{rbase}.", )
        record.levelname = record.levelname.lower()

        return super().format(record)

    def xǁStringFormatterǁformat__mutmut_6(self, record):
        for rbase in self._remove_base:
            record.name = record.name.replace(f"{rbase}.", "XXXX")
        record.levelname = record.levelname.lower()

        return super().format(record)

    def xǁStringFormatterǁformat__mutmut_7(self, record):
        for rbase in self._remove_base:
            record.name = record.name.replace(f"{rbase}.", "")
        record.levelname = None

        return super().format(record)

    def xǁStringFormatterǁformat__mutmut_8(self, record):
        for rbase in self._remove_base:
            record.name = record.name.replace(f"{rbase}.", "")
        record.levelname = record.levelname.upper()

        return super().format(record)

    def xǁStringFormatterǁformat__mutmut_9(self, record):
        for rbase in self._remove_base:
            record.name = record.name.replace(f"{rbase}.", "")
        record.levelname = record.levelname.lower()

        return super().format(None)
    
    xǁStringFormatterǁformat__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStringFormatterǁformat__mutmut_1': xǁStringFormatterǁformat__mutmut_1, 
        'xǁStringFormatterǁformat__mutmut_2': xǁStringFormatterǁformat__mutmut_2, 
        'xǁStringFormatterǁformat__mutmut_3': xǁStringFormatterǁformat__mutmut_3, 
        'xǁStringFormatterǁformat__mutmut_4': xǁStringFormatterǁformat__mutmut_4, 
        'xǁStringFormatterǁformat__mutmut_5': xǁStringFormatterǁformat__mutmut_5, 
        'xǁStringFormatterǁformat__mutmut_6': xǁStringFormatterǁformat__mutmut_6, 
        'xǁStringFormatterǁformat__mutmut_7': xǁStringFormatterǁformat__mutmut_7, 
        'xǁStringFormatterǁformat__mutmut_8': xǁStringFormatterǁformat__mutmut_8, 
        'xǁStringFormatterǁformat__mutmut_9': xǁStringFormatterǁformat__mutmut_9
    }
    
    def format(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStringFormatterǁformat__mutmut_orig"), object.__getattribute__(self, "xǁStringFormatterǁformat__mutmut_mutants"), args, kwargs, self)
        return result 
    
    format.__signature__ = _mutmut_signature(xǁStringFormatterǁformat__mutmut_orig)
    xǁStringFormatterǁformat__mutmut_orig.__name__ = 'xǁStringFormatterǁformat'


class StreamHandler(logging.StreamHandler):
    def xǁStreamHandlerǁ__init____mutmut_orig(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stream_reconfigure()
    def xǁStreamHandlerǁ__init____mutmut_1(self, *args, **kwargs):
        super().__init__(**kwargs)
        self._stream_reconfigure()
    def xǁStreamHandlerǁ__init____mutmut_2(self, *args, **kwargs):
        super().__init__(*args, )
        self._stream_reconfigure()
    
    xǁStreamHandlerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamHandlerǁ__init____mutmut_1': xǁStreamHandlerǁ__init____mutmut_1, 
        'xǁStreamHandlerǁ__init____mutmut_2': xǁStreamHandlerǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamHandlerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStreamHandlerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStreamHandlerǁ__init____mutmut_orig)
    xǁStreamHandlerǁ__init____mutmut_orig.__name__ = 'xǁStreamHandlerǁ__init__'

    def flush(self):
        try:
            super().flush()
        except OSError:
            # Python doesn't raise BrokenPipeError on Windows
            pass

    def xǁStreamHandlerǁsetStream__mutmut_orig(self, stream):
        res = super().setStream(stream)
        if res:  # pragma: no branch
            self._stream_reconfigure()

        return res

    def xǁStreamHandlerǁsetStream__mutmut_1(self, stream):
        res = None
        if res:  # pragma: no branch
            self._stream_reconfigure()

        return res

    def xǁStreamHandlerǁsetStream__mutmut_2(self, stream):
        res = super().setStream(None)
        if res:  # pragma: no branch
            self._stream_reconfigure()

        return res
    
    xǁStreamHandlerǁsetStream__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamHandlerǁsetStream__mutmut_1': xǁStreamHandlerǁsetStream__mutmut_1, 
        'xǁStreamHandlerǁsetStream__mutmut_2': xǁStreamHandlerǁsetStream__mutmut_2
    }
    
    def setStream(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamHandlerǁsetStream__mutmut_orig"), object.__getattribute__(self, "xǁStreamHandlerǁsetStream__mutmut_mutants"), args, kwargs, self)
        return result 
    
    setStream.__signature__ = _mutmut_signature(xǁStreamHandlerǁsetStream__mutmut_orig)
    xǁStreamHandlerǁsetStream__mutmut_orig.__name__ = 'xǁStreamHandlerǁsetStream'

    def xǁStreamHandlerǁ_stream_reconfigure__mutmut_orig(self):
        # make stream write calls escape unsupported characters (stdout/stderr encoding is not guaranteed to be utf-8)
        self.stream.reconfigure(errors="backslashreplace")

    def xǁStreamHandlerǁ_stream_reconfigure__mutmut_1(self):
        # make stream write calls escape unsupported characters (stdout/stderr encoding is not guaranteed to be utf-8)
        self.stream.reconfigure(errors=None)

    def xǁStreamHandlerǁ_stream_reconfigure__mutmut_2(self):
        # make stream write calls escape unsupported characters (stdout/stderr encoding is not guaranteed to be utf-8)
        self.stream.reconfigure(errors="XXbackslashreplaceXX")

    def xǁStreamHandlerǁ_stream_reconfigure__mutmut_3(self):
        # make stream write calls escape unsupported characters (stdout/stderr encoding is not guaranteed to be utf-8)
        self.stream.reconfigure(errors="BACKSLASHREPLACE")

    def xǁStreamHandlerǁ_stream_reconfigure__mutmut_4(self):
        # make stream write calls escape unsupported characters (stdout/stderr encoding is not guaranteed to be utf-8)
        self.stream.reconfigure(errors="Backslashreplace")
    
    xǁStreamHandlerǁ_stream_reconfigure__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamHandlerǁ_stream_reconfigure__mutmut_1': xǁStreamHandlerǁ_stream_reconfigure__mutmut_1, 
        'xǁStreamHandlerǁ_stream_reconfigure__mutmut_2': xǁStreamHandlerǁ_stream_reconfigure__mutmut_2, 
        'xǁStreamHandlerǁ_stream_reconfigure__mutmut_3': xǁStreamHandlerǁ_stream_reconfigure__mutmut_3, 
        'xǁStreamHandlerǁ_stream_reconfigure__mutmut_4': xǁStreamHandlerǁ_stream_reconfigure__mutmut_4
    }
    
    def _stream_reconfigure(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamHandlerǁ_stream_reconfigure__mutmut_orig"), object.__getattribute__(self, "xǁStreamHandlerǁ_stream_reconfigure__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _stream_reconfigure.__signature__ = _mutmut_signature(xǁStreamHandlerǁ_stream_reconfigure__mutmut_orig)
    xǁStreamHandlerǁ_stream_reconfigure__mutmut_orig.__name__ = 'xǁStreamHandlerǁ_stream_reconfigure'


class WarningLogRecord(logging.LogRecord):
    msg: WarningMessage  # type: ignore[assignment]

    def xǁWarningLogRecordǁ__init____mutmut_orig(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "warnings"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_1(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.name = "warnings"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_2(self, *args, **kwargs):
        super().__init__(*args, )
        self.name = "warnings"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_3(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = None
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_4(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "XXwarningsXX"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_5(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "WARNINGS"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_6(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Warnings"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_7(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "warnings"
        self.levelname = None
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_8(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "warnings"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = None
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_9(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "warnings"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = None
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_10(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "warnings"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(None)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_11(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "warnings"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = None
        self.module = self._path.stem
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_12(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "warnings"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = None
        self.lineno = self.msg.lineno

    def xǁWarningLogRecordǁ__init____mutmut_13(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "warnings"
        self.levelname = self.msg.category.__name__ if self.msg.category else UserWarning.__name__
        self.pathname = self.msg.filename
        self._path = Path(self.pathname)
        self.filename = self._path.name
        self.module = self._path.stem
        self.lineno = None
    
    xǁWarningLogRecordǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWarningLogRecordǁ__init____mutmut_1': xǁWarningLogRecordǁ__init____mutmut_1, 
        'xǁWarningLogRecordǁ__init____mutmut_2': xǁWarningLogRecordǁ__init____mutmut_2, 
        'xǁWarningLogRecordǁ__init____mutmut_3': xǁWarningLogRecordǁ__init____mutmut_3, 
        'xǁWarningLogRecordǁ__init____mutmut_4': xǁWarningLogRecordǁ__init____mutmut_4, 
        'xǁWarningLogRecordǁ__init____mutmut_5': xǁWarningLogRecordǁ__init____mutmut_5, 
        'xǁWarningLogRecordǁ__init____mutmut_6': xǁWarningLogRecordǁ__init____mutmut_6, 
        'xǁWarningLogRecordǁ__init____mutmut_7': xǁWarningLogRecordǁ__init____mutmut_7, 
        'xǁWarningLogRecordǁ__init____mutmut_8': xǁWarningLogRecordǁ__init____mutmut_8, 
        'xǁWarningLogRecordǁ__init____mutmut_9': xǁWarningLogRecordǁ__init____mutmut_9, 
        'xǁWarningLogRecordǁ__init____mutmut_10': xǁWarningLogRecordǁ__init____mutmut_10, 
        'xǁWarningLogRecordǁ__init____mutmut_11': xǁWarningLogRecordǁ__init____mutmut_11, 
        'xǁWarningLogRecordǁ__init____mutmut_12': xǁWarningLogRecordǁ__init____mutmut_12, 
        'xǁWarningLogRecordǁ__init____mutmut_13': xǁWarningLogRecordǁ__init____mutmut_13
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWarningLogRecordǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWarningLogRecordǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWarningLogRecordǁ__init____mutmut_orig)
    xǁWarningLogRecordǁ__init____mutmut_orig.__name__ = 'xǁWarningLogRecordǁ__init__'

    def xǁWarningLogRecordǁgetMessage__mutmut_orig(self) -> str:
        if self.msg.category and issubclass(self.msg.category, StreamlinkWarning):
            return f"{self.msg.message}"
        return f"{self.msg.message}\n  {self.pathname}:{self.lineno}"

    def xǁWarningLogRecordǁgetMessage__mutmut_1(self) -> str:
        if self.msg.category or issubclass(self.msg.category, StreamlinkWarning):
            return f"{self.msg.message}"
        return f"{self.msg.message}\n  {self.pathname}:{self.lineno}"

    def xǁWarningLogRecordǁgetMessage__mutmut_2(self) -> str:
        if self.msg.category and issubclass(None, StreamlinkWarning):
            return f"{self.msg.message}"
        return f"{self.msg.message}\n  {self.pathname}:{self.lineno}"

    def xǁWarningLogRecordǁgetMessage__mutmut_3(self) -> str:
        if self.msg.category and issubclass(self.msg.category, None):
            return f"{self.msg.message}"
        return f"{self.msg.message}\n  {self.pathname}:{self.lineno}"

    def xǁWarningLogRecordǁgetMessage__mutmut_4(self) -> str:
        if self.msg.category and issubclass(StreamlinkWarning):
            return f"{self.msg.message}"
        return f"{self.msg.message}\n  {self.pathname}:{self.lineno}"

    def xǁWarningLogRecordǁgetMessage__mutmut_5(self) -> str:
        if self.msg.category and issubclass(self.msg.category, ):
            return f"{self.msg.message}"
        return f"{self.msg.message}\n  {self.pathname}:{self.lineno}"
    
    xǁWarningLogRecordǁgetMessage__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWarningLogRecordǁgetMessage__mutmut_1': xǁWarningLogRecordǁgetMessage__mutmut_1, 
        'xǁWarningLogRecordǁgetMessage__mutmut_2': xǁWarningLogRecordǁgetMessage__mutmut_2, 
        'xǁWarningLogRecordǁgetMessage__mutmut_3': xǁWarningLogRecordǁgetMessage__mutmut_3, 
        'xǁWarningLogRecordǁgetMessage__mutmut_4': xǁWarningLogRecordǁgetMessage__mutmut_4, 
        'xǁWarningLogRecordǁgetMessage__mutmut_5': xǁWarningLogRecordǁgetMessage__mutmut_5
    }
    
    def getMessage(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWarningLogRecordǁgetMessage__mutmut_orig"), object.__getattribute__(self, "xǁWarningLogRecordǁgetMessage__mutmut_mutants"), args, kwargs, self)
        return result 
    
    getMessage.__signature__ = _mutmut_signature(xǁWarningLogRecordǁgetMessage__mutmut_orig)
    xǁWarningLogRecordǁgetMessage__mutmut_orig.__name__ = 'xǁWarningLogRecordǁgetMessage'


def x__log_record_factory__mutmut_orig(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_1(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(None, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_2(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, None, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_3(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, None, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_4(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, None, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_5(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, None, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_6(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, None, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_7(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, None, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_8(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, None, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_9(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, None)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_10(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_11(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_12(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_13(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_14(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_15(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_16(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_17(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_18(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, )

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_19(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(None, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_20(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, None, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_21(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, None, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_22(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, None, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_23(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, None, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_24(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, None, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_25(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, None, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_26(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_27(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_28(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_29(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, msg, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_30(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, args, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_31(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, exc_info, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_32(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, func=None, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_33(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, sinfo=None, **kwargs)


def x__log_record_factory__mutmut_34(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, **kwargs)


def x__log_record_factory__mutmut_35(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    if isinstance(msg, WarningMessage):
        # noinspection PyTypeChecker
        return WarningLogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)

    return _log_record_factory_default(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, )

x__log_record_factory__mutmut_mutants : ClassVar[MutantDict] = {
'x__log_record_factory__mutmut_1': x__log_record_factory__mutmut_1, 
    'x__log_record_factory__mutmut_2': x__log_record_factory__mutmut_2, 
    'x__log_record_factory__mutmut_3': x__log_record_factory__mutmut_3, 
    'x__log_record_factory__mutmut_4': x__log_record_factory__mutmut_4, 
    'x__log_record_factory__mutmut_5': x__log_record_factory__mutmut_5, 
    'x__log_record_factory__mutmut_6': x__log_record_factory__mutmut_6, 
    'x__log_record_factory__mutmut_7': x__log_record_factory__mutmut_7, 
    'x__log_record_factory__mutmut_8': x__log_record_factory__mutmut_8, 
    'x__log_record_factory__mutmut_9': x__log_record_factory__mutmut_9, 
    'x__log_record_factory__mutmut_10': x__log_record_factory__mutmut_10, 
    'x__log_record_factory__mutmut_11': x__log_record_factory__mutmut_11, 
    'x__log_record_factory__mutmut_12': x__log_record_factory__mutmut_12, 
    'x__log_record_factory__mutmut_13': x__log_record_factory__mutmut_13, 
    'x__log_record_factory__mutmut_14': x__log_record_factory__mutmut_14, 
    'x__log_record_factory__mutmut_15': x__log_record_factory__mutmut_15, 
    'x__log_record_factory__mutmut_16': x__log_record_factory__mutmut_16, 
    'x__log_record_factory__mutmut_17': x__log_record_factory__mutmut_17, 
    'x__log_record_factory__mutmut_18': x__log_record_factory__mutmut_18, 
    'x__log_record_factory__mutmut_19': x__log_record_factory__mutmut_19, 
    'x__log_record_factory__mutmut_20': x__log_record_factory__mutmut_20, 
    'x__log_record_factory__mutmut_21': x__log_record_factory__mutmut_21, 
    'x__log_record_factory__mutmut_22': x__log_record_factory__mutmut_22, 
    'x__log_record_factory__mutmut_23': x__log_record_factory__mutmut_23, 
    'x__log_record_factory__mutmut_24': x__log_record_factory__mutmut_24, 
    'x__log_record_factory__mutmut_25': x__log_record_factory__mutmut_25, 
    'x__log_record_factory__mutmut_26': x__log_record_factory__mutmut_26, 
    'x__log_record_factory__mutmut_27': x__log_record_factory__mutmut_27, 
    'x__log_record_factory__mutmut_28': x__log_record_factory__mutmut_28, 
    'x__log_record_factory__mutmut_29': x__log_record_factory__mutmut_29, 
    'x__log_record_factory__mutmut_30': x__log_record_factory__mutmut_30, 
    'x__log_record_factory__mutmut_31': x__log_record_factory__mutmut_31, 
    'x__log_record_factory__mutmut_32': x__log_record_factory__mutmut_32, 
    'x__log_record_factory__mutmut_33': x__log_record_factory__mutmut_33, 
    'x__log_record_factory__mutmut_34': x__log_record_factory__mutmut_34, 
    'x__log_record_factory__mutmut_35': x__log_record_factory__mutmut_35
}

def _log_record_factory(*args, **kwargs):
    result = _mutmut_trampoline(x__log_record_factory__mutmut_orig, x__log_record_factory__mutmut_mutants, args, kwargs)
    return result 

_log_record_factory.__signature__ = _mutmut_signature(x__log_record_factory__mutmut_orig)
x__log_record_factory__mutmut_orig.__name__ = 'x__log_record_factory'


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_orig(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_1(message, category, filename, lineno, file=None, line=None):
    if file is None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_2(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_3(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(None, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_4(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, None, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_5(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, None, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_6(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, None, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_7(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, None, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_8(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, None)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_9(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_10(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_11(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_12(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_13(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_14(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, )
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_15(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = None
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_16(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(None, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_17(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, None, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_18(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, None, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_19(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, None, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_20(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, None)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_21(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_22(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_23(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, lineno, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_24(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, None, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_25(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, line)
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_26(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, )
    root.log(WARNING, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_27(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(None, warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_28(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, None, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_29(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=None)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_30(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(warning, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_31(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, stacklevel=2)


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_32(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, )


# borrowed from stdlib and modified, so that `WarningMessage` gets passed as `msg` to the `WarningLogRecord`
def x__showwarning__mutmut_33(message, category, filename, lineno, file=None, line=None):
    if file is not None:  # pragma: no cover
        if _showwarning_default is not None:
            # noinspection PyCallingNonCallable
            _showwarning_default(message, category, filename, lineno, file, line)
        return

    warning = WarningMessage(message, category, filename, lineno, None, line)
    root.log(WARNING, warning, stacklevel=3)

x__showwarning__mutmut_mutants : ClassVar[MutantDict] = {
'x__showwarning__mutmut_1': x__showwarning__mutmut_1, 
    'x__showwarning__mutmut_2': x__showwarning__mutmut_2, 
    'x__showwarning__mutmut_3': x__showwarning__mutmut_3, 
    'x__showwarning__mutmut_4': x__showwarning__mutmut_4, 
    'x__showwarning__mutmut_5': x__showwarning__mutmut_5, 
    'x__showwarning__mutmut_6': x__showwarning__mutmut_6, 
    'x__showwarning__mutmut_7': x__showwarning__mutmut_7, 
    'x__showwarning__mutmut_8': x__showwarning__mutmut_8, 
    'x__showwarning__mutmut_9': x__showwarning__mutmut_9, 
    'x__showwarning__mutmut_10': x__showwarning__mutmut_10, 
    'x__showwarning__mutmut_11': x__showwarning__mutmut_11, 
    'x__showwarning__mutmut_12': x__showwarning__mutmut_12, 
    'x__showwarning__mutmut_13': x__showwarning__mutmut_13, 
    'x__showwarning__mutmut_14': x__showwarning__mutmut_14, 
    'x__showwarning__mutmut_15': x__showwarning__mutmut_15, 
    'x__showwarning__mutmut_16': x__showwarning__mutmut_16, 
    'x__showwarning__mutmut_17': x__showwarning__mutmut_17, 
    'x__showwarning__mutmut_18': x__showwarning__mutmut_18, 
    'x__showwarning__mutmut_19': x__showwarning__mutmut_19, 
    'x__showwarning__mutmut_20': x__showwarning__mutmut_20, 
    'x__showwarning__mutmut_21': x__showwarning__mutmut_21, 
    'x__showwarning__mutmut_22': x__showwarning__mutmut_22, 
    'x__showwarning__mutmut_23': x__showwarning__mutmut_23, 
    'x__showwarning__mutmut_24': x__showwarning__mutmut_24, 
    'x__showwarning__mutmut_25': x__showwarning__mutmut_25, 
    'x__showwarning__mutmut_26': x__showwarning__mutmut_26, 
    'x__showwarning__mutmut_27': x__showwarning__mutmut_27, 
    'x__showwarning__mutmut_28': x__showwarning__mutmut_28, 
    'x__showwarning__mutmut_29': x__showwarning__mutmut_29, 
    'x__showwarning__mutmut_30': x__showwarning__mutmut_30, 
    'x__showwarning__mutmut_31': x__showwarning__mutmut_31, 
    'x__showwarning__mutmut_32': x__showwarning__mutmut_32, 
    'x__showwarning__mutmut_33': x__showwarning__mutmut_33
}

def _showwarning(*args, **kwargs):
    result = _mutmut_trampoline(x__showwarning__mutmut_orig, x__showwarning__mutmut_mutants, args, kwargs)
    return result 

_showwarning.__signature__ = _mutmut_signature(x__showwarning__mutmut_orig)
x__showwarning__mutmut_orig.__name__ = 'x__showwarning'


def x_capturewarnings__mutmut_orig(capture=False):
    global _showwarning_default  # noqa: PLW0603

    if capture:
        if _showwarning_default is None:
            _showwarning_default = warnings.showwarning
            warnings.showwarning = _showwarning
    else:
        if _showwarning_default is not None:
            warnings.showwarning = _showwarning_default
            _showwarning_default = None


def x_capturewarnings__mutmut_1(capture=True):
    global _showwarning_default  # noqa: PLW0603

    if capture:
        if _showwarning_default is None:
            _showwarning_default = warnings.showwarning
            warnings.showwarning = _showwarning
    else:
        if _showwarning_default is not None:
            warnings.showwarning = _showwarning_default
            _showwarning_default = None


def x_capturewarnings__mutmut_2(capture=False):
    global _showwarning_default  # noqa: PLW0603

    if capture:
        if _showwarning_default is not None:
            _showwarning_default = warnings.showwarning
            warnings.showwarning = _showwarning
    else:
        if _showwarning_default is not None:
            warnings.showwarning = _showwarning_default
            _showwarning_default = None


def x_capturewarnings__mutmut_3(capture=False):
    global _showwarning_default  # noqa: PLW0603

    if capture:
        if _showwarning_default is None:
            _showwarning_default = None
            warnings.showwarning = _showwarning
    else:
        if _showwarning_default is not None:
            warnings.showwarning = _showwarning_default
            _showwarning_default = None


def x_capturewarnings__mutmut_4(capture=False):
    global _showwarning_default  # noqa: PLW0603

    if capture:
        if _showwarning_default is None:
            _showwarning_default = warnings.showwarning
            warnings.showwarning = None
    else:
        if _showwarning_default is not None:
            warnings.showwarning = _showwarning_default
            _showwarning_default = None


def x_capturewarnings__mutmut_5(capture=False):
    global _showwarning_default  # noqa: PLW0603

    if capture:
        if _showwarning_default is None:
            _showwarning_default = warnings.showwarning
            warnings.showwarning = _showwarning
    else:
        if _showwarning_default is None:
            warnings.showwarning = _showwarning_default
            _showwarning_default = None


def x_capturewarnings__mutmut_6(capture=False):
    global _showwarning_default  # noqa: PLW0603

    if capture:
        if _showwarning_default is None:
            _showwarning_default = warnings.showwarning
            warnings.showwarning = _showwarning
    else:
        if _showwarning_default is not None:
            warnings.showwarning = None
            _showwarning_default = None


def x_capturewarnings__mutmut_7(capture=False):
    global _showwarning_default  # noqa: PLW0603

    if capture:
        if _showwarning_default is None:
            _showwarning_default = warnings.showwarning
            warnings.showwarning = _showwarning
    else:
        if _showwarning_default is not None:
            warnings.showwarning = _showwarning_default
            _showwarning_default = ""

x_capturewarnings__mutmut_mutants : ClassVar[MutantDict] = {
'x_capturewarnings__mutmut_1': x_capturewarnings__mutmut_1, 
    'x_capturewarnings__mutmut_2': x_capturewarnings__mutmut_2, 
    'x_capturewarnings__mutmut_3': x_capturewarnings__mutmut_3, 
    'x_capturewarnings__mutmut_4': x_capturewarnings__mutmut_4, 
    'x_capturewarnings__mutmut_5': x_capturewarnings__mutmut_5, 
    'x_capturewarnings__mutmut_6': x_capturewarnings__mutmut_6, 
    'x_capturewarnings__mutmut_7': x_capturewarnings__mutmut_7
}

def capturewarnings(*args, **kwargs):
    result = _mutmut_trampoline(x_capturewarnings__mutmut_orig, x_capturewarnings__mutmut_mutants, args, kwargs)
    return result 

capturewarnings.__signature__ = _mutmut_signature(x_capturewarnings__mutmut_orig)
x_capturewarnings__mutmut_orig.__name__ = 'x_capturewarnings'


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_orig(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_1(
    *,
    filename: str | Path | None = None,
    filemode: str = "XXaXX",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_2(
    *,
    filename: str | Path | None = None,
    filemode: str = "A",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_3(
    *,
    filename: str | Path | None = None,
    filemode: str = "A",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_4(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = True,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_5(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = ""
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_6(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_7(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = None
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_8(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(None, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_9(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, None, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_10(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding=None)
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_11(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_12(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_13(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, )
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_14(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="XXutf-8XX")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_15(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="UTF-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_16(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="Utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_17(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_18(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = None

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_19(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(None)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_20(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_21(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = None
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_22(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=None,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_23(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=None,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_24(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=None,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_25(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=None,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_26(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_27(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_28(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_29(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_30(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base and REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_31(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(None)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_32(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(None)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_33(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_34(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(None)

        if capture_warnings:
            capturewarnings(True)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_35(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(None)

    return handler


# noinspection PyShadowingBuiltins,PyPep8Naming
def x_basicConfig__mutmut_36(
    *,
    filename: str | Path | None = None,
    filemode: str = "a",
    format: str = FORMAT_BASE,  # noqa: A002
    datefmt: str = FORMAT_DATE,
    style: Literal["%", "{", "$"] = FORMAT_STYLE,
    level: str | None = None,
    stream: IO | None = None,
    remove_base: list[str] | None = None,
    capture_warnings: bool = False,
) -> logging.StreamHandler | None:
    with _config_lock:
        handler: logging.StreamHandler | None = None
        if filename is not None:
            handler = logging.FileHandler(filename, filemode, encoding="utf-8")
        elif stream is not None:
            handler = StreamHandler(stream)

        if handler is not None:
            formatter = StringFormatter(
                fmt=format,
                datefmt=datefmt,
                style=style,
                remove_base=remove_base or REMOVE_BASE,
            )
            handler.setFormatter(formatter)

            root.addHandler(handler)

        if level is not None:
            root.setLevel(level)

        if capture_warnings:
            capturewarnings(False)

    return handler

x_basicConfig__mutmut_mutants : ClassVar[MutantDict] = {
'x_basicConfig__mutmut_1': x_basicConfig__mutmut_1, 
    'x_basicConfig__mutmut_2': x_basicConfig__mutmut_2, 
    'x_basicConfig__mutmut_3': x_basicConfig__mutmut_3, 
    'x_basicConfig__mutmut_4': x_basicConfig__mutmut_4, 
    'x_basicConfig__mutmut_5': x_basicConfig__mutmut_5, 
    'x_basicConfig__mutmut_6': x_basicConfig__mutmut_6, 
    'x_basicConfig__mutmut_7': x_basicConfig__mutmut_7, 
    'x_basicConfig__mutmut_8': x_basicConfig__mutmut_8, 
    'x_basicConfig__mutmut_9': x_basicConfig__mutmut_9, 
    'x_basicConfig__mutmut_10': x_basicConfig__mutmut_10, 
    'x_basicConfig__mutmut_11': x_basicConfig__mutmut_11, 
    'x_basicConfig__mutmut_12': x_basicConfig__mutmut_12, 
    'x_basicConfig__mutmut_13': x_basicConfig__mutmut_13, 
    'x_basicConfig__mutmut_14': x_basicConfig__mutmut_14, 
    'x_basicConfig__mutmut_15': x_basicConfig__mutmut_15, 
    'x_basicConfig__mutmut_16': x_basicConfig__mutmut_16, 
    'x_basicConfig__mutmut_17': x_basicConfig__mutmut_17, 
    'x_basicConfig__mutmut_18': x_basicConfig__mutmut_18, 
    'x_basicConfig__mutmut_19': x_basicConfig__mutmut_19, 
    'x_basicConfig__mutmut_20': x_basicConfig__mutmut_20, 
    'x_basicConfig__mutmut_21': x_basicConfig__mutmut_21, 
    'x_basicConfig__mutmut_22': x_basicConfig__mutmut_22, 
    'x_basicConfig__mutmut_23': x_basicConfig__mutmut_23, 
    'x_basicConfig__mutmut_24': x_basicConfig__mutmut_24, 
    'x_basicConfig__mutmut_25': x_basicConfig__mutmut_25, 
    'x_basicConfig__mutmut_26': x_basicConfig__mutmut_26, 
    'x_basicConfig__mutmut_27': x_basicConfig__mutmut_27, 
    'x_basicConfig__mutmut_28': x_basicConfig__mutmut_28, 
    'x_basicConfig__mutmut_29': x_basicConfig__mutmut_29, 
    'x_basicConfig__mutmut_30': x_basicConfig__mutmut_30, 
    'x_basicConfig__mutmut_31': x_basicConfig__mutmut_31, 
    'x_basicConfig__mutmut_32': x_basicConfig__mutmut_32, 
    'x_basicConfig__mutmut_33': x_basicConfig__mutmut_33, 
    'x_basicConfig__mutmut_34': x_basicConfig__mutmut_34, 
    'x_basicConfig__mutmut_35': x_basicConfig__mutmut_35, 
    'x_basicConfig__mutmut_36': x_basicConfig__mutmut_36
}

def basicConfig(*args, **kwargs):
    result = _mutmut_trampoline(x_basicConfig__mutmut_orig, x_basicConfig__mutmut_mutants, args, kwargs)
    return result 

basicConfig.__signature__ = _mutmut_signature(x_basicConfig__mutmut_orig)
x_basicConfig__mutmut_orig.__name__ = 'x_basicConfig'


_showwarning_default = None
_log_record_factory_default = logging.getLogRecordFactory()
logging.setLogRecordFactory(_log_record_factory)


logging.setLoggerClass(StreamlinkLogger)
root = logging.getLogger("streamlink")
root.setLevel(WARNING)

levels = list(_levelToNames.values())


__all__ = [
    "NONE",
    "CRITICAL",
    "ERROR",
    "WARNING",
    "INFO",
    "DEBUG",
    "TRACE",
    "ALL",
    "StreamlinkLogger",
    "basicConfig",
    "root",
    "levels",
    "capturewarnings",
]

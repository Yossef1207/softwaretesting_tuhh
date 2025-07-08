"""
$description Live TV channels and video on-demand service from RTVE, a Spanish public, state-owned broadcaster.
$url rtve.es
$type live, vod
$metadata id
$region Spain
"""

from __future__ import annotations

import logging
import re
from base64 import b64decode
from collections.abc import Iterator, Sequence
from io import BytesIO
from urllib.parse import urlparse

from streamlink.plugin import Plugin, PluginError, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.ffmpegmux import MuxedStream
from streamlink.stream.hls import HLSStream
from streamlink.stream.http import HTTPStream
from streamlink.utils.url import update_scheme


log = logging.getLogger(__name__)
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


class Base64Reader:
    def xǁBase64Readerǁ__init____mutmut_orig(self, data: str):
        stream = BytesIO(b64decode(data))

        def _iterate():
            while True:
                chunk = stream.read(1)
                if len(chunk) == 0:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_1(self, data: str):
        stream = None

        def _iterate():
            while True:
                chunk = stream.read(1)
                if len(chunk) == 0:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_2(self, data: str):
        stream = BytesIO(None)

        def _iterate():
            while True:
                chunk = stream.read(1)
                if len(chunk) == 0:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_3(self, data: str):
        stream = BytesIO(b64decode(None))

        def _iterate():
            while True:
                chunk = stream.read(1)
                if len(chunk) == 0:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_4(self, data: str):
        stream = BytesIO(b64decode(data))

        def _iterate():
            while False:
                chunk = stream.read(1)
                if len(chunk) == 0:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_5(self, data: str):
        stream = BytesIO(b64decode(data))

        def _iterate():
            while True:
                chunk = None
                if len(chunk) == 0:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_6(self, data: str):
        stream = BytesIO(b64decode(data))

        def _iterate():
            while True:
                chunk = stream.read(None)
                if len(chunk) == 0:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_7(self, data: str):
        stream = BytesIO(b64decode(data))

        def _iterate():
            while True:
                chunk = stream.read(2)
                if len(chunk) == 0:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_8(self, data: str):
        stream = BytesIO(b64decode(data))

        def _iterate():
            while True:
                chunk = stream.read(1)
                if len(chunk) != 0:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_9(self, data: str):
        stream = BytesIO(b64decode(data))

        def _iterate():
            while True:
                chunk = stream.read(1)
                if len(chunk) == 1:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_10(self, data: str):
        stream = BytesIO(b64decode(data))

        def _iterate():
            while True:
                chunk = stream.read(1)
                if len(chunk) == 0:
                    return
                yield ord(None)

        self._iterator: Iterator[int] = _iterate()
    def xǁBase64Readerǁ__init____mutmut_11(self, data: str):
        stream = BytesIO(b64decode(data))

        def _iterate():
            while True:
                chunk = stream.read(1)
                if len(chunk) == 0:
                    return
                yield ord(chunk)

        self._iterator: Iterator[int] = None
    
    xǁBase64Readerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBase64Readerǁ__init____mutmut_1': xǁBase64Readerǁ__init____mutmut_1, 
        'xǁBase64Readerǁ__init____mutmut_2': xǁBase64Readerǁ__init____mutmut_2, 
        'xǁBase64Readerǁ__init____mutmut_3': xǁBase64Readerǁ__init____mutmut_3, 
        'xǁBase64Readerǁ__init____mutmut_4': xǁBase64Readerǁ__init____mutmut_4, 
        'xǁBase64Readerǁ__init____mutmut_5': xǁBase64Readerǁ__init____mutmut_5, 
        'xǁBase64Readerǁ__init____mutmut_6': xǁBase64Readerǁ__init____mutmut_6, 
        'xǁBase64Readerǁ__init____mutmut_7': xǁBase64Readerǁ__init____mutmut_7, 
        'xǁBase64Readerǁ__init____mutmut_8': xǁBase64Readerǁ__init____mutmut_8, 
        'xǁBase64Readerǁ__init____mutmut_9': xǁBase64Readerǁ__init____mutmut_9, 
        'xǁBase64Readerǁ__init____mutmut_10': xǁBase64Readerǁ__init____mutmut_10, 
        'xǁBase64Readerǁ__init____mutmut_11': xǁBase64Readerǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBase64Readerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBase64Readerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBase64Readerǁ__init____mutmut_orig)
    xǁBase64Readerǁ__init____mutmut_orig.__name__ = 'xǁBase64Readerǁ__init__'

    def xǁBase64Readerǁread__mutmut_orig(self, num: int) -> Sequence[int]:
        res = []
        for _ in range(num):
            item = next(self._iterator, None)
            if item is None:
                break
            res.append(item)
        return res

    def xǁBase64Readerǁread__mutmut_1(self, num: int) -> Sequence[int]:
        res = None
        for _ in range(num):
            item = next(self._iterator, None)
            if item is None:
                break
            res.append(item)
        return res

    def xǁBase64Readerǁread__mutmut_2(self, num: int) -> Sequence[int]:
        res = []
        for _ in range(None):
            item = next(self._iterator, None)
            if item is None:
                break
            res.append(item)
        return res

    def xǁBase64Readerǁread__mutmut_3(self, num: int) -> Sequence[int]:
        res = []
        for _ in range(num):
            item = None
            if item is None:
                break
            res.append(item)
        return res

    def xǁBase64Readerǁread__mutmut_4(self, num: int) -> Sequence[int]:
        res = []
        for _ in range(num):
            item = next(None, None)
            if item is None:
                break
            res.append(item)
        return res

    def xǁBase64Readerǁread__mutmut_5(self, num: int) -> Sequence[int]:
        res = []
        for _ in range(num):
            item = next(None)
            if item is None:
                break
            res.append(item)
        return res

    def xǁBase64Readerǁread__mutmut_6(self, num: int) -> Sequence[int]:
        res = []
        for _ in range(num):
            item = next(self._iterator, )
            if item is None:
                break
            res.append(item)
        return res

    def xǁBase64Readerǁread__mutmut_7(self, num: int) -> Sequence[int]:
        res = []
        for _ in range(num):
            item = next(self._iterator, None)
            if item is not None:
                break
            res.append(item)
        return res

    def xǁBase64Readerǁread__mutmut_8(self, num: int) -> Sequence[int]:
        res = []
        for _ in range(num):
            item = next(self._iterator, None)
            if item is None:
                return
            res.append(item)
        return res

    def xǁBase64Readerǁread__mutmut_9(self, num: int) -> Sequence[int]:
        res = []
        for _ in range(num):
            item = next(self._iterator, None)
            if item is None:
                break
            res.append(None)
        return res
    
    xǁBase64Readerǁread__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBase64Readerǁread__mutmut_1': xǁBase64Readerǁread__mutmut_1, 
        'xǁBase64Readerǁread__mutmut_2': xǁBase64Readerǁread__mutmut_2, 
        'xǁBase64Readerǁread__mutmut_3': xǁBase64Readerǁread__mutmut_3, 
        'xǁBase64Readerǁread__mutmut_4': xǁBase64Readerǁread__mutmut_4, 
        'xǁBase64Readerǁread__mutmut_5': xǁBase64Readerǁread__mutmut_5, 
        'xǁBase64Readerǁread__mutmut_6': xǁBase64Readerǁread__mutmut_6, 
        'xǁBase64Readerǁread__mutmut_7': xǁBase64Readerǁread__mutmut_7, 
        'xǁBase64Readerǁread__mutmut_8': xǁBase64Readerǁread__mutmut_8, 
        'xǁBase64Readerǁread__mutmut_9': xǁBase64Readerǁread__mutmut_9
    }
    
    def read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBase64Readerǁread__mutmut_orig"), object.__getattribute__(self, "xǁBase64Readerǁread__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read.__signature__ = _mutmut_signature(xǁBase64Readerǁread__mutmut_orig)
    xǁBase64Readerǁread__mutmut_orig.__name__ = 'xǁBase64Readerǁread'

    def xǁBase64Readerǁskip__mutmut_orig(self, num: int) -> None:
        self.read(num)

    def xǁBase64Readerǁskip__mutmut_1(self, num: int) -> None:
        self.read(None)
    
    xǁBase64Readerǁskip__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBase64Readerǁskip__mutmut_1': xǁBase64Readerǁskip__mutmut_1
    }
    
    def skip(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBase64Readerǁskip__mutmut_orig"), object.__getattribute__(self, "xǁBase64Readerǁskip__mutmut_mutants"), args, kwargs, self)
        return result 
    
    skip.__signature__ = _mutmut_signature(xǁBase64Readerǁskip__mutmut_orig)
    xǁBase64Readerǁskip__mutmut_orig.__name__ = 'xǁBase64Readerǁskip'

    def xǁBase64Readerǁread_chars__mutmut_orig(self, num: int) -> str:
        return "".join(chr(item) for item in self.read(num))

    def xǁBase64Readerǁread_chars__mutmut_1(self, num: int) -> str:
        return "".join(None)

    def xǁBase64Readerǁread_chars__mutmut_2(self, num: int) -> str:
        return "XXXX".join(chr(item) for item in self.read(num))

    def xǁBase64Readerǁread_chars__mutmut_3(self, num: int) -> str:
        return "".join(chr(None) for item in self.read(num))

    def xǁBase64Readerǁread_chars__mutmut_4(self, num: int) -> str:
        return "".join(chr(item) for item in self.read(None))
    
    xǁBase64Readerǁread_chars__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBase64Readerǁread_chars__mutmut_1': xǁBase64Readerǁread_chars__mutmut_1, 
        'xǁBase64Readerǁread_chars__mutmut_2': xǁBase64Readerǁread_chars__mutmut_2, 
        'xǁBase64Readerǁread_chars__mutmut_3': xǁBase64Readerǁread_chars__mutmut_3, 
        'xǁBase64Readerǁread_chars__mutmut_4': xǁBase64Readerǁread_chars__mutmut_4
    }
    
    def read_chars(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBase64Readerǁread_chars__mutmut_orig"), object.__getattribute__(self, "xǁBase64Readerǁread_chars__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read_chars.__signature__ = _mutmut_signature(xǁBase64Readerǁread_chars__mutmut_orig)
    xǁBase64Readerǁread_chars__mutmut_orig.__name__ = 'xǁBase64Readerǁread_chars'

    def xǁBase64Readerǁread_int__mutmut_orig(self) -> int:
        a, b, c, d = self.read(4)
        return a << 24 | b << 16 | c << 8 | d

    def xǁBase64Readerǁread_int__mutmut_1(self) -> int:
        a, b, c, d = None
        return a << 24 | b << 16 | c << 8 | d

    def xǁBase64Readerǁread_int__mutmut_2(self) -> int:
        a, b, c, d = self.read(None)
        return a << 24 | b << 16 | c << 8 | d

    def xǁBase64Readerǁread_int__mutmut_3(self) -> int:
        a, b, c, d = self.read(5)
        return a << 24 | b << 16 | c << 8 | d

    def xǁBase64Readerǁread_int__mutmut_4(self) -> int:
        a, b, c, d = self.read(4)
        return a >> 24 | b << 16 | c << 8 | d

    def xǁBase64Readerǁread_int__mutmut_5(self) -> int:
        a, b, c, d = self.read(4)
        return a << 25 | b << 16 | c << 8 | d

    def xǁBase64Readerǁread_int__mutmut_6(self) -> int:
        a, b, c, d = self.read(4)
        return a << 24 & b << 16 | c << 8 | d

    def xǁBase64Readerǁread_int__mutmut_7(self) -> int:
        a, b, c, d = self.read(4)
        return a << 24 | b >> 16 | c << 8 | d

    def xǁBase64Readerǁread_int__mutmut_8(self) -> int:
        a, b, c, d = self.read(4)
        return a << 24 | b << 17 | c << 8 | d

    def xǁBase64Readerǁread_int__mutmut_9(self) -> int:
        a, b, c, d = self.read(4)
        return a << 24 | b << 16 & c << 8 | d

    def xǁBase64Readerǁread_int__mutmut_10(self) -> int:
        a, b, c, d = self.read(4)
        return a << 24 | b << 16 | c >> 8 | d

    def xǁBase64Readerǁread_int__mutmut_11(self) -> int:
        a, b, c, d = self.read(4)
        return a << 24 | b << 16 | c << 9 | d

    def xǁBase64Readerǁread_int__mutmut_12(self) -> int:
        a, b, c, d = self.read(4)
        return a << 24 | b << 16 | c << 8 & d
    
    xǁBase64Readerǁread_int__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBase64Readerǁread_int__mutmut_1': xǁBase64Readerǁread_int__mutmut_1, 
        'xǁBase64Readerǁread_int__mutmut_2': xǁBase64Readerǁread_int__mutmut_2, 
        'xǁBase64Readerǁread_int__mutmut_3': xǁBase64Readerǁread_int__mutmut_3, 
        'xǁBase64Readerǁread_int__mutmut_4': xǁBase64Readerǁread_int__mutmut_4, 
        'xǁBase64Readerǁread_int__mutmut_5': xǁBase64Readerǁread_int__mutmut_5, 
        'xǁBase64Readerǁread_int__mutmut_6': xǁBase64Readerǁread_int__mutmut_6, 
        'xǁBase64Readerǁread_int__mutmut_7': xǁBase64Readerǁread_int__mutmut_7, 
        'xǁBase64Readerǁread_int__mutmut_8': xǁBase64Readerǁread_int__mutmut_8, 
        'xǁBase64Readerǁread_int__mutmut_9': xǁBase64Readerǁread_int__mutmut_9, 
        'xǁBase64Readerǁread_int__mutmut_10': xǁBase64Readerǁread_int__mutmut_10, 
        'xǁBase64Readerǁread_int__mutmut_11': xǁBase64Readerǁread_int__mutmut_11, 
        'xǁBase64Readerǁread_int__mutmut_12': xǁBase64Readerǁread_int__mutmut_12
    }
    
    def read_int(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBase64Readerǁread_int__mutmut_orig"), object.__getattribute__(self, "xǁBase64Readerǁread_int__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read_int.__signature__ = _mutmut_signature(xǁBase64Readerǁread_int__mutmut_orig)
    xǁBase64Readerǁread_int__mutmut_orig.__name__ = 'xǁBase64Readerǁread_int'

    def xǁBase64Readerǁread_chunk__mutmut_orig(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(4)
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("Invalid chunk length")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_1(self) -> tuple[str, Sequence[int]]:
        size = None
        chunktype = self.read_chars(4)
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("Invalid chunk length")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_2(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = None
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("Invalid chunk length")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_3(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(None)
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("Invalid chunk length")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_4(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(5)
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("Invalid chunk length")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_5(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(4)
        chunkdata = None
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("Invalid chunk length")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_6(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(4)
        chunkdata = self.read(None)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("Invalid chunk length")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_7(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(4)
        chunkdata = self.read(size)
        if len(chunkdata) == size:  # pragma: no cover
            raise ValueError("Invalid chunk length")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_8(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(4)
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError(None)
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_9(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(4)
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("XXInvalid chunk lengthXX")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_10(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(4)
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("invalid chunk length")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_11(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(4)
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("INVALID CHUNK LENGTH")
        self.skip(4)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_12(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(4)
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("Invalid chunk length")
        self.skip(None)
        return chunktype, chunkdata

    def xǁBase64Readerǁread_chunk__mutmut_13(self) -> tuple[str, Sequence[int]]:
        size = self.read_int()
        chunktype = self.read_chars(4)
        chunkdata = self.read(size)
        if len(chunkdata) != size:  # pragma: no cover
            raise ValueError("Invalid chunk length")
        self.skip(5)
        return chunktype, chunkdata
    
    xǁBase64Readerǁread_chunk__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBase64Readerǁread_chunk__mutmut_1': xǁBase64Readerǁread_chunk__mutmut_1, 
        'xǁBase64Readerǁread_chunk__mutmut_2': xǁBase64Readerǁread_chunk__mutmut_2, 
        'xǁBase64Readerǁread_chunk__mutmut_3': xǁBase64Readerǁread_chunk__mutmut_3, 
        'xǁBase64Readerǁread_chunk__mutmut_4': xǁBase64Readerǁread_chunk__mutmut_4, 
        'xǁBase64Readerǁread_chunk__mutmut_5': xǁBase64Readerǁread_chunk__mutmut_5, 
        'xǁBase64Readerǁread_chunk__mutmut_6': xǁBase64Readerǁread_chunk__mutmut_6, 
        'xǁBase64Readerǁread_chunk__mutmut_7': xǁBase64Readerǁread_chunk__mutmut_7, 
        'xǁBase64Readerǁread_chunk__mutmut_8': xǁBase64Readerǁread_chunk__mutmut_8, 
        'xǁBase64Readerǁread_chunk__mutmut_9': xǁBase64Readerǁread_chunk__mutmut_9, 
        'xǁBase64Readerǁread_chunk__mutmut_10': xǁBase64Readerǁread_chunk__mutmut_10, 
        'xǁBase64Readerǁread_chunk__mutmut_11': xǁBase64Readerǁread_chunk__mutmut_11, 
        'xǁBase64Readerǁread_chunk__mutmut_12': xǁBase64Readerǁread_chunk__mutmut_12, 
        'xǁBase64Readerǁread_chunk__mutmut_13': xǁBase64Readerǁread_chunk__mutmut_13
    }
    
    def read_chunk(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBase64Readerǁread_chunk__mutmut_orig"), object.__getattribute__(self, "xǁBase64Readerǁread_chunk__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read_chunk.__signature__ = _mutmut_signature(xǁBase64Readerǁread_chunk__mutmut_orig)
    xǁBase64Readerǁread_chunk__mutmut_orig.__name__ = 'xǁBase64Readerǁread_chunk'

    def xǁBase64Readerǁ__iter____mutmut_orig(self):
        self.skip(8)
        while True:
            try:
                yield self.read_chunk()
            except ValueError:
                return

    def xǁBase64Readerǁ__iter____mutmut_1(self):
        self.skip(None)
        while True:
            try:
                yield self.read_chunk()
            except ValueError:
                return

    def xǁBase64Readerǁ__iter____mutmut_2(self):
        self.skip(9)
        while True:
            try:
                yield self.read_chunk()
            except ValueError:
                return

    def xǁBase64Readerǁ__iter____mutmut_3(self):
        self.skip(8)
        while False:
            try:
                yield self.read_chunk()
            except ValueError:
                return
    
    xǁBase64Readerǁ__iter____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBase64Readerǁ__iter____mutmut_1': xǁBase64Readerǁ__iter____mutmut_1, 
        'xǁBase64Readerǁ__iter____mutmut_2': xǁBase64Readerǁ__iter____mutmut_2, 
        'xǁBase64Readerǁ__iter____mutmut_3': xǁBase64Readerǁ__iter____mutmut_3
    }
    
    def __iter__(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁBase64Readerǁ__iter____mutmut_orig"), object.__getattribute__(self, "xǁBase64Readerǁ__iter____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __iter__.__signature__ = _mutmut_signature(xǁBase64Readerǁ__iter____mutmut_orig)
    xǁBase64Readerǁ__iter____mutmut_orig.__name__ = 'xǁBase64Readerǁ__iter__'


class ZTNR:
    @staticmethod
    def _get_alphabet(text: str) -> str:
        res = []
        j = 0
        k = 0
        for char in text:
            if k > 0:
                k -= 1
            else:
                res.append(char)
                j = (j + 1) % 4
                k = j
        return "".join(res)

    @staticmethod
    def _get_url(text: str, alphabet: str) -> str:
        res = []
        j = 0
        n = 0
        k = 3
        cont = 0
        for char in text:
            if j == 0:
                n = int(char) * 10
                j = 1
            elif k > 0:
                k -= 1
            else:
                res.append(alphabet[n + int(char)])
                j = 0
                k = cont % 4
                cont += 1
        return "".join(res)

    @classmethod
    def _get_source(cls, alphabet: str, data: str) -> str:
        return cls._get_url(data, cls._get_alphabet(alphabet))

    @classmethod
    def translate(cls, data: str) -> Iterator[tuple[str, str]]:
        reader = Base64Reader(data.replace("\n", ""))
        for chunk_type, chunk_data in reader:
            if chunk_type == "IEND":
                break
            if chunk_type == "tEXt":
                content = "".join(chr(item) for item in chunk_data if item > 0)
                if "#" not in content or "%%" not in content:
                    continue
                alphabet, content = content.split("#", 1)
                quality, content = content.split("%%", 1)
                yield quality, cls._get_source(alphabet, content)


@pluginmatcher(
    re.compile(r"https?://(?:www\.)?rtve\.es/play/videos/.+"),
)
class Rtve(Plugin):
    URL_M3U8 = "https://ztnr.rtve.es/ztnr/{id}.m3u8"
    URL_VIDEOS = "https://ztnr.rtve.es/ztnr/movil/thumbnail/rtveplayw/videos/{id}.png?q=v2"
    URL_SUBTITLES = "https://www.rtve.es/api/videos/{id}/subtitulos.json"

    def _get_streams(self):
        self.id = self.session.http.get(
            self.url,
            schema=validate.Schema(
                re.compile(r"\bdata-setup='({.+?})'", re.DOTALL),
                validate.none_or_all(
                    validate.get(1),
                    validate.parse_json(),
                    {
                        "idAsset": validate.any(int, validate.all(str, validate.transform(int))),
                    },
                    validate.get("idAsset"),
                ),
            ),
        )
        if not self.id:
            return

        # check obfuscated stream URLs via self.URL_VIDEOS and ZTNR.translate() first
        # self.URL_M3U8 appears to be valid for all streams, but doesn't provide any content in some cases
        try:
            urls = self.session.http.get(
                self.URL_VIDEOS.format(id=self.id),
                schema=validate.Schema(
                    validate.transform(ZTNR.translate),
                    validate.transform(list),
                    [(str, validate.url())],
                    validate.length(1),
                ),
            )
        except PluginError:
            # catch HTTP errors and validation errors, and fall back to generic HLS URL template
            url = self.URL_M3U8.format(id=self.id)
        else:
            url = next((url for _, url in urls if urlparse(url).path.endswith(".m3u8")), None)
            if not url:
                url = next((url for _, url in urls if urlparse(url).path.endswith(".mp4")), None)
                if url:
                    yield "vod", HTTPStream(self.session, url)
                return

        streams = HLSStream.parse_variant_playlist(self.session, url).items()

        if self.session.get_option("mux-subtitles"):
            subs = self.session.http.get(
                self.URL_SUBTITLES.format(id=self.id),
                schema=validate.Schema(
                    validate.parse_json(),
                    {
                        "page": {
                            "items": [
                                {
                                    "lang": str,
                                    "src": validate.url(),
                                },
                            ],
                        },
                    },
                    validate.get(("page", "items")),
                ),
            )
            if subs:
                subtitles = {
                    s["lang"]: HTTPStream(self.session, update_scheme("https://", s["src"], force=True))
                    for s in subs
                }  # fmt: skip
                for quality, stream in streams:
                    yield quality, MuxedStream(self.session, stream, subtitles=subtitles)
                return

        yield from streams


__plugin__ = Rtve

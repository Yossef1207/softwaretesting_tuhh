from threading import Event

from streamlink.buffers import Buffer
from streamlink.stream.stream import StreamIO
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


class FilteredStream(StreamIO):
    """StreamIO mixin for being able to pause read calls while filtering content"""

    buffer: Buffer

    def xǁFilteredStreamǁ__init____mutmut_orig(self, *args, **kwargs):
        self._event_filter = Event()
        self._event_filter.set()
        super().__init__(*args, **kwargs)

    def xǁFilteredStreamǁ__init____mutmut_1(self, *args, **kwargs):
        self._event_filter = None
        self._event_filter.set()
        super().__init__(*args, **kwargs)

    def xǁFilteredStreamǁ__init____mutmut_2(self, *args, **kwargs):
        self._event_filter = Event()
        self._event_filter.set()
        super().__init__(**kwargs)

    def xǁFilteredStreamǁ__init____mutmut_3(self, *args, **kwargs):
        self._event_filter = Event()
        self._event_filter.set()
        super().__init__(*args, )
    
    xǁFilteredStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFilteredStreamǁ__init____mutmut_1': xǁFilteredStreamǁ__init____mutmut_1, 
        'xǁFilteredStreamǁ__init____mutmut_2': xǁFilteredStreamǁ__init____mutmut_2, 
        'xǁFilteredStreamǁ__init____mutmut_3': xǁFilteredStreamǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilteredStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁFilteredStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁFilteredStreamǁ__init____mutmut_orig)
    xǁFilteredStreamǁ__init____mutmut_orig.__name__ = 'xǁFilteredStreamǁ__init__'

    def xǁFilteredStreamǁread__mutmut_orig(self, *args, **kwargs) -> bytes:
        read = super().read
        while True:
            try:
                return read(*args, **kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length > 0:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_1(self, *args, **kwargs) -> bytes:
        read = None
        while True:
            try:
                return read(*args, **kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length > 0:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_2(self, *args, **kwargs) -> bytes:
        read = super().read
        while False:
            try:
                return read(*args, **kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length > 0:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_3(self, *args, **kwargs) -> bytes:
        read = super().read
        while True:
            try:
                return read(**kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length > 0:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_4(self, *args, **kwargs) -> bytes:
        read = super().read
        while True:
            try:
                return read(*args, )
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length > 0:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_5(self, *args, **kwargs) -> bytes:
        read = super().read
        while True:
            try:
                return read(*args, **kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b"XXXX"
                # if data is available, try reading again
                if self.buffer.length > 0:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_6(self, *args, **kwargs) -> bytes:
        read = super().read
        while True:
            try:
                return read(*args, **kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length > 0:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_7(self, *args, **kwargs) -> bytes:
        read = super().read
        while True:
            try:
                return read(*args, **kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length > 0:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_8(self, *args, **kwargs) -> bytes:
        read = super().read
        while True:
            try:
                return read(*args, **kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length > 0:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_9(self, *args, **kwargs) -> bytes:
        read = super().read
        while True:
            try:
                return read(*args, **kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length >= 0:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_10(self, *args, **kwargs) -> bytes:
        read = super().read
        while True:
            try:
                return read(*args, **kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length > 1:
                    continue
                # raise if not filtering and no data available
                raise

    def xǁFilteredStreamǁread__mutmut_11(self, *args, **kwargs) -> bytes:
        read = super().read
        while True:
            try:
                return read(*args, **kwargs)
            except OSError:
                # wait indefinitely until filtering ends
                self._event_filter.wait()
                if self.buffer.closed:
                    return b""
                # if data is available, try reading again
                if self.buffer.length > 0:
                    break
                # raise if not filtering and no data available
                raise
    
    xǁFilteredStreamǁread__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFilteredStreamǁread__mutmut_1': xǁFilteredStreamǁread__mutmut_1, 
        'xǁFilteredStreamǁread__mutmut_2': xǁFilteredStreamǁread__mutmut_2, 
        'xǁFilteredStreamǁread__mutmut_3': xǁFilteredStreamǁread__mutmut_3, 
        'xǁFilteredStreamǁread__mutmut_4': xǁFilteredStreamǁread__mutmut_4, 
        'xǁFilteredStreamǁread__mutmut_5': xǁFilteredStreamǁread__mutmut_5, 
        'xǁFilteredStreamǁread__mutmut_6': xǁFilteredStreamǁread__mutmut_6, 
        'xǁFilteredStreamǁread__mutmut_7': xǁFilteredStreamǁread__mutmut_7, 
        'xǁFilteredStreamǁread__mutmut_8': xǁFilteredStreamǁread__mutmut_8, 
        'xǁFilteredStreamǁread__mutmut_9': xǁFilteredStreamǁread__mutmut_9, 
        'xǁFilteredStreamǁread__mutmut_10': xǁFilteredStreamǁread__mutmut_10, 
        'xǁFilteredStreamǁread__mutmut_11': xǁFilteredStreamǁread__mutmut_11
    }
    
    def read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilteredStreamǁread__mutmut_orig"), object.__getattribute__(self, "xǁFilteredStreamǁread__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read.__signature__ = _mutmut_signature(xǁFilteredStreamǁread__mutmut_orig)
    xǁFilteredStreamǁread__mutmut_orig.__name__ = 'xǁFilteredStreamǁread'

    def close(self) -> None:
        super().close()
        self._event_filter.set()

    def xǁFilteredStreamǁis_paused__mutmut_orig(self) -> bool:
        return not self._event_filter.is_set()

    def xǁFilteredStreamǁis_paused__mutmut_1(self) -> bool:
        return self._event_filter.is_set()
    
    xǁFilteredStreamǁis_paused__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFilteredStreamǁis_paused__mutmut_1': xǁFilteredStreamǁis_paused__mutmut_1
    }
    
    def is_paused(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilteredStreamǁis_paused__mutmut_orig"), object.__getattribute__(self, "xǁFilteredStreamǁis_paused__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_paused.__signature__ = _mutmut_signature(xǁFilteredStreamǁis_paused__mutmut_orig)
    xǁFilteredStreamǁis_paused__mutmut_orig.__name__ = 'xǁFilteredStreamǁis_paused'

    def pause(self) -> None:
        self._event_filter.clear()

    def resume(self) -> None:
        self._event_filter.set()

    def xǁFilteredStreamǁfilter_wait__mutmut_orig(self, timeout=None):
        return self._event_filter.wait(timeout)

    def xǁFilteredStreamǁfilter_wait__mutmut_1(self, timeout=None):
        return self._event_filter.wait(None)
    
    xǁFilteredStreamǁfilter_wait__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFilteredStreamǁfilter_wait__mutmut_1': xǁFilteredStreamǁfilter_wait__mutmut_1
    }
    
    def filter_wait(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilteredStreamǁfilter_wait__mutmut_orig"), object.__getattribute__(self, "xǁFilteredStreamǁfilter_wait__mutmut_mutants"), args, kwargs, self)
        return result 
    
    filter_wait.__signature__ = _mutmut_signature(xǁFilteredStreamǁfilter_wait__mutmut_orig)
    xǁFilteredStreamǁfilter_wait__mutmut_orig.__name__ = 'xǁFilteredStreamǁfilter_wait'

import io
from threading import Thread

from streamlink.buffers import Buffer, RingBuffer
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


class StreamIOWrapper(io.IOBase):
    """Wraps file-like objects that are not inheriting from IOBase"""

    def xǁStreamIOWrapperǁ__init____mutmut_orig(self, fd):
        self.fd = fd

    def xǁStreamIOWrapperǁ__init____mutmut_1(self, fd):
        self.fd = None
    
    xǁStreamIOWrapperǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamIOWrapperǁ__init____mutmut_1': xǁStreamIOWrapperǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamIOWrapperǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStreamIOWrapperǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStreamIOWrapperǁ__init____mutmut_orig)
    xǁStreamIOWrapperǁ__init____mutmut_orig.__name__ = 'xǁStreamIOWrapperǁ__init__'

    def xǁStreamIOWrapperǁread__mutmut_orig(self, size=-1):
        return self.fd.read(size)

    def xǁStreamIOWrapperǁread__mutmut_1(self, size=-1):
        return self.fd.read(None)
    
    xǁStreamIOWrapperǁread__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamIOWrapperǁread__mutmut_1': xǁStreamIOWrapperǁread__mutmut_1
    }
    
    def read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamIOWrapperǁread__mutmut_orig"), object.__getattribute__(self, "xǁStreamIOWrapperǁread__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read.__signature__ = _mutmut_signature(xǁStreamIOWrapperǁread__mutmut_orig)
    xǁStreamIOWrapperǁread__mutmut_orig.__name__ = 'xǁStreamIOWrapperǁread'

    def xǁStreamIOWrapperǁclose__mutmut_orig(self):
        if hasattr(self.fd, "close"):
            self.fd.close()

    def xǁStreamIOWrapperǁclose__mutmut_1(self):
        if hasattr(None, "close"):
            self.fd.close()

    def xǁStreamIOWrapperǁclose__mutmut_2(self):
        if hasattr(self.fd, None):
            self.fd.close()

    def xǁStreamIOWrapperǁclose__mutmut_3(self):
        if hasattr("close"):
            self.fd.close()

    def xǁStreamIOWrapperǁclose__mutmut_4(self):
        if hasattr(self.fd, ):
            self.fd.close()

    def xǁStreamIOWrapperǁclose__mutmut_5(self):
        if hasattr(self.fd, "XXcloseXX"):
            self.fd.close()

    def xǁStreamIOWrapperǁclose__mutmut_6(self):
        if hasattr(self.fd, "CLOSE"):
            self.fd.close()

    def xǁStreamIOWrapperǁclose__mutmut_7(self):
        if hasattr(self.fd, "Close"):
            self.fd.close()
    
    xǁStreamIOWrapperǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamIOWrapperǁclose__mutmut_1': xǁStreamIOWrapperǁclose__mutmut_1, 
        'xǁStreamIOWrapperǁclose__mutmut_2': xǁStreamIOWrapperǁclose__mutmut_2, 
        'xǁStreamIOWrapperǁclose__mutmut_3': xǁStreamIOWrapperǁclose__mutmut_3, 
        'xǁStreamIOWrapperǁclose__mutmut_4': xǁStreamIOWrapperǁclose__mutmut_4, 
        'xǁStreamIOWrapperǁclose__mutmut_5': xǁStreamIOWrapperǁclose__mutmut_5, 
        'xǁStreamIOWrapperǁclose__mutmut_6': xǁStreamIOWrapperǁclose__mutmut_6, 
        'xǁStreamIOWrapperǁclose__mutmut_7': xǁStreamIOWrapperǁclose__mutmut_7
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamIOWrapperǁclose__mutmut_orig"), object.__getattribute__(self, "xǁStreamIOWrapperǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁStreamIOWrapperǁclose__mutmut_orig)
    xǁStreamIOWrapperǁclose__mutmut_orig.__name__ = 'xǁStreamIOWrapperǁclose'


class StreamIOIterWrapper(io.IOBase):
    """Wraps a iterator and turn it into a file-like object"""

    def xǁStreamIOIterWrapperǁ__init____mutmut_orig(self, iterator):
        self.iterator = iterator
        self.buffer = Buffer()

    def xǁStreamIOIterWrapperǁ__init____mutmut_1(self, iterator):
        self.iterator = None
        self.buffer = Buffer()

    def xǁStreamIOIterWrapperǁ__init____mutmut_2(self, iterator):
        self.iterator = iterator
        self.buffer = None
    
    xǁStreamIOIterWrapperǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamIOIterWrapperǁ__init____mutmut_1': xǁStreamIOIterWrapperǁ__init____mutmut_1, 
        'xǁStreamIOIterWrapperǁ__init____mutmut_2': xǁStreamIOIterWrapperǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamIOIterWrapperǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStreamIOIterWrapperǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStreamIOIterWrapperǁ__init____mutmut_orig)
    xǁStreamIOIterWrapperǁ__init____mutmut_orig.__name__ = 'xǁStreamIOIterWrapperǁ__init__'

    def xǁStreamIOIterWrapperǁread__mutmut_orig(self, size=-1):
        if size < 0:
            size = self.buffer.length

        while self.buffer.length < size:
            try:
                chunk = next(self.iterator)
                self.buffer.write(chunk)
            except StopIteration:
                break

        return self.buffer.read(size)

    def xǁStreamIOIterWrapperǁread__mutmut_1(self, size=-1):
        if size <= 0:
            size = self.buffer.length

        while self.buffer.length < size:
            try:
                chunk = next(self.iterator)
                self.buffer.write(chunk)
            except StopIteration:
                break

        return self.buffer.read(size)

    def xǁStreamIOIterWrapperǁread__mutmut_2(self, size=-1):
        if size < 1:
            size = self.buffer.length

        while self.buffer.length < size:
            try:
                chunk = next(self.iterator)
                self.buffer.write(chunk)
            except StopIteration:
                break

        return self.buffer.read(size)

    def xǁStreamIOIterWrapperǁread__mutmut_3(self, size=-1):
        if size < 0:
            size = None

        while self.buffer.length < size:
            try:
                chunk = next(self.iterator)
                self.buffer.write(chunk)
            except StopIteration:
                break

        return self.buffer.read(size)

    def xǁStreamIOIterWrapperǁread__mutmut_4(self, size=-1):
        if size < 0:
            size = self.buffer.length

        while self.buffer.length <= size:
            try:
                chunk = next(self.iterator)
                self.buffer.write(chunk)
            except StopIteration:
                break

        return self.buffer.read(size)

    def xǁStreamIOIterWrapperǁread__mutmut_5(self, size=-1):
        if size < 0:
            size = self.buffer.length

        while self.buffer.length < size:
            try:
                chunk = None
                self.buffer.write(chunk)
            except StopIteration:
                break

        return self.buffer.read(size)

    def xǁStreamIOIterWrapperǁread__mutmut_6(self, size=-1):
        if size < 0:
            size = self.buffer.length

        while self.buffer.length < size:
            try:
                chunk = next(None)
                self.buffer.write(chunk)
            except StopIteration:
                break

        return self.buffer.read(size)

    def xǁStreamIOIterWrapperǁread__mutmut_7(self, size=-1):
        if size < 0:
            size = self.buffer.length

        while self.buffer.length < size:
            try:
                chunk = next(self.iterator)
                self.buffer.write(None)
            except StopIteration:
                break

        return self.buffer.read(size)

    def xǁStreamIOIterWrapperǁread__mutmut_8(self, size=-1):
        if size < 0:
            size = self.buffer.length

        while self.buffer.length < size:
            try:
                chunk = next(self.iterator)
                self.buffer.write(chunk)
            except StopIteration:
                return

        return self.buffer.read(size)

    def xǁStreamIOIterWrapperǁread__mutmut_9(self, size=-1):
        if size < 0:
            size = self.buffer.length

        while self.buffer.length < size:
            try:
                chunk = next(self.iterator)
                self.buffer.write(chunk)
            except StopIteration:
                break

        return self.buffer.read(None)
    
    xǁStreamIOIterWrapperǁread__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamIOIterWrapperǁread__mutmut_1': xǁStreamIOIterWrapperǁread__mutmut_1, 
        'xǁStreamIOIterWrapperǁread__mutmut_2': xǁStreamIOIterWrapperǁread__mutmut_2, 
        'xǁStreamIOIterWrapperǁread__mutmut_3': xǁStreamIOIterWrapperǁread__mutmut_3, 
        'xǁStreamIOIterWrapperǁread__mutmut_4': xǁStreamIOIterWrapperǁread__mutmut_4, 
        'xǁStreamIOIterWrapperǁread__mutmut_5': xǁStreamIOIterWrapperǁread__mutmut_5, 
        'xǁStreamIOIterWrapperǁread__mutmut_6': xǁStreamIOIterWrapperǁread__mutmut_6, 
        'xǁStreamIOIterWrapperǁread__mutmut_7': xǁStreamIOIterWrapperǁread__mutmut_7, 
        'xǁStreamIOIterWrapperǁread__mutmut_8': xǁStreamIOIterWrapperǁread__mutmut_8, 
        'xǁStreamIOIterWrapperǁread__mutmut_9': xǁStreamIOIterWrapperǁread__mutmut_9
    }
    
    def read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamIOIterWrapperǁread__mutmut_orig"), object.__getattribute__(self, "xǁStreamIOIterWrapperǁread__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read.__signature__ = _mutmut_signature(xǁStreamIOIterWrapperǁread__mutmut_orig)
    xǁStreamIOIterWrapperǁread__mutmut_orig.__name__ = 'xǁStreamIOIterWrapperǁread'

    def close(self):
        pass


class StreamIOThreadWrapper(io.IOBase):
    """Wraps a file-like object in a thread.

    Useful for getting control over read timeout where
    timeout handling is missing or out of our control.
    """

    class Filler(Thread):
        def __init__(self, fd, buffer):
            super().__init__()

            self.error = None
            self.fd = fd
            self.buffer = buffer
            self.daemon = True
            self.running = False

        def run(self):
            self.running = True

            while self.running:
                try:
                    data = self.fd.read(8192)
                except OSError as error:
                    self.error = error
                    break

                if len(data) == 0:
                    break

                self.buffer.write(data)

            self.stop()

        def stop(self):
            self.running = False
            self.buffer.close()

            if hasattr(self.fd, "close"):
                try:
                    self.fd.close()
                except Exception:
                    pass

    def xǁStreamIOThreadWrapperǁ__init____mutmut_orig(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("ringbuffer-size"))
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_1(self, session, fd, timeout=31):
        self.buffer = RingBuffer(session.get_option("ringbuffer-size"))
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_2(self, session, fd, timeout=30):
        self.buffer = None
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_3(self, session, fd, timeout=30):
        self.buffer = RingBuffer(None)
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_4(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option(None))
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_5(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("XXringbuffer-sizeXX"))
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_6(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("RINGBUFFER-SIZE"))
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_7(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("Ringbuffer-size"))
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_8(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("ringbuffer-size"))
        self.fd = None
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_9(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("ringbuffer-size"))
        self.fd = fd
        self.timeout = None

        self.filler = StreamIOThreadWrapper.Filler(self.fd, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_10(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("ringbuffer-size"))
        self.fd = fd
        self.timeout = timeout

        self.filler = None
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_11(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("ringbuffer-size"))
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(None, self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_12(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("ringbuffer-size"))
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, None)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_13(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("ringbuffer-size"))
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.buffer)
        self.filler.start()

    def xǁStreamIOThreadWrapperǁ__init____mutmut_14(self, session, fd, timeout=30):
        self.buffer = RingBuffer(session.get_option("ringbuffer-size"))
        self.fd = fd
        self.timeout = timeout

        self.filler = StreamIOThreadWrapper.Filler(self.fd, )
        self.filler.start()
    
    xǁStreamIOThreadWrapperǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamIOThreadWrapperǁ__init____mutmut_1': xǁStreamIOThreadWrapperǁ__init____mutmut_1, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_2': xǁStreamIOThreadWrapperǁ__init____mutmut_2, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_3': xǁStreamIOThreadWrapperǁ__init____mutmut_3, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_4': xǁStreamIOThreadWrapperǁ__init____mutmut_4, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_5': xǁStreamIOThreadWrapperǁ__init____mutmut_5, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_6': xǁStreamIOThreadWrapperǁ__init____mutmut_6, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_7': xǁStreamIOThreadWrapperǁ__init____mutmut_7, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_8': xǁStreamIOThreadWrapperǁ__init____mutmut_8, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_9': xǁStreamIOThreadWrapperǁ__init____mutmut_9, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_10': xǁStreamIOThreadWrapperǁ__init____mutmut_10, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_11': xǁStreamIOThreadWrapperǁ__init____mutmut_11, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_12': xǁStreamIOThreadWrapperǁ__init____mutmut_12, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_13': xǁStreamIOThreadWrapperǁ__init____mutmut_13, 
        'xǁStreamIOThreadWrapperǁ__init____mutmut_14': xǁStreamIOThreadWrapperǁ__init____mutmut_14
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamIOThreadWrapperǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStreamIOThreadWrapperǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStreamIOThreadWrapperǁ__init____mutmut_orig)
    xǁStreamIOThreadWrapperǁ__init____mutmut_orig.__name__ = 'xǁStreamIOThreadWrapperǁ__init__'

    def xǁStreamIOThreadWrapperǁread__mutmut_orig(self, size=-1):
        if self.filler.error and self.buffer.length == 0:
            raise self.filler.error

        return self.buffer.read(size, block=self.filler.is_alive(), timeout=self.timeout)

    def xǁStreamIOThreadWrapperǁread__mutmut_1(self, size=-1):
        if self.filler.error or self.buffer.length == 0:
            raise self.filler.error

        return self.buffer.read(size, block=self.filler.is_alive(), timeout=self.timeout)

    def xǁStreamIOThreadWrapperǁread__mutmut_2(self, size=-1):
        if self.filler.error and self.buffer.length != 0:
            raise self.filler.error

        return self.buffer.read(size, block=self.filler.is_alive(), timeout=self.timeout)

    def xǁStreamIOThreadWrapperǁread__mutmut_3(self, size=-1):
        if self.filler.error and self.buffer.length == 1:
            raise self.filler.error

        return self.buffer.read(size, block=self.filler.is_alive(), timeout=self.timeout)

    def xǁStreamIOThreadWrapperǁread__mutmut_4(self, size=-1):
        if self.filler.error and self.buffer.length == 0:
            raise self.filler.error

        return self.buffer.read(None, block=self.filler.is_alive(), timeout=self.timeout)

    def xǁStreamIOThreadWrapperǁread__mutmut_5(self, size=-1):
        if self.filler.error and self.buffer.length == 0:
            raise self.filler.error

        return self.buffer.read(size, block=None, timeout=self.timeout)

    def xǁStreamIOThreadWrapperǁread__mutmut_6(self, size=-1):
        if self.filler.error and self.buffer.length == 0:
            raise self.filler.error

        return self.buffer.read(size, block=self.filler.is_alive(), timeout=None)

    def xǁStreamIOThreadWrapperǁread__mutmut_7(self, size=-1):
        if self.filler.error and self.buffer.length == 0:
            raise self.filler.error

        return self.buffer.read(block=self.filler.is_alive(), timeout=self.timeout)

    def xǁStreamIOThreadWrapperǁread__mutmut_8(self, size=-1):
        if self.filler.error and self.buffer.length == 0:
            raise self.filler.error

        return self.buffer.read(size, timeout=self.timeout)

    def xǁStreamIOThreadWrapperǁread__mutmut_9(self, size=-1):
        if self.filler.error and self.buffer.length == 0:
            raise self.filler.error

        return self.buffer.read(size, block=self.filler.is_alive(), )
    
    xǁStreamIOThreadWrapperǁread__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamIOThreadWrapperǁread__mutmut_1': xǁStreamIOThreadWrapperǁread__mutmut_1, 
        'xǁStreamIOThreadWrapperǁread__mutmut_2': xǁStreamIOThreadWrapperǁread__mutmut_2, 
        'xǁStreamIOThreadWrapperǁread__mutmut_3': xǁStreamIOThreadWrapperǁread__mutmut_3, 
        'xǁStreamIOThreadWrapperǁread__mutmut_4': xǁStreamIOThreadWrapperǁread__mutmut_4, 
        'xǁStreamIOThreadWrapperǁread__mutmut_5': xǁStreamIOThreadWrapperǁread__mutmut_5, 
        'xǁStreamIOThreadWrapperǁread__mutmut_6': xǁStreamIOThreadWrapperǁread__mutmut_6, 
        'xǁStreamIOThreadWrapperǁread__mutmut_7': xǁStreamIOThreadWrapperǁread__mutmut_7, 
        'xǁStreamIOThreadWrapperǁread__mutmut_8': xǁStreamIOThreadWrapperǁread__mutmut_8, 
        'xǁStreamIOThreadWrapperǁread__mutmut_9': xǁStreamIOThreadWrapperǁread__mutmut_9
    }
    
    def read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamIOThreadWrapperǁread__mutmut_orig"), object.__getattribute__(self, "xǁStreamIOThreadWrapperǁread__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read.__signature__ = _mutmut_signature(xǁStreamIOThreadWrapperǁread__mutmut_orig)
    xǁStreamIOThreadWrapperǁread__mutmut_orig.__name__ = 'xǁStreamIOThreadWrapperǁread'

    def close(self):
        self.filler.stop()

        if self.filler.is_alive():
            self.filler.join()


__all__ = ["StreamIOWrapper", "StreamIOIterWrapper", "StreamIOThreadWrapper"]

from collections import deque
from io import BytesIO
from threading import Event, Lock
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


class Chunk(BytesIO):
    """A single chunk, part of the buffer."""

    def xǁChunkǁ__init____mutmut_orig(self, buf):
        self.length = len(buf)
        BytesIO.__init__(self, buf)

    def xǁChunkǁ__init____mutmut_1(self, buf):
        self.length = None
        BytesIO.__init__(self, buf)

    def xǁChunkǁ__init____mutmut_2(self, buf):
        self.length = len(buf)
        BytesIO.__init__(None, buf)

    def xǁChunkǁ__init____mutmut_3(self, buf):
        self.length = len(buf)
        BytesIO.__init__(self, None)

    def xǁChunkǁ__init____mutmut_4(self, buf):
        self.length = len(buf)
        BytesIO.__init__(buf)

    def xǁChunkǁ__init____mutmut_5(self, buf):
        self.length = len(buf)
        BytesIO.__init__(self, )
    
    xǁChunkǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁChunkǁ__init____mutmut_1': xǁChunkǁ__init____mutmut_1, 
        'xǁChunkǁ__init____mutmut_2': xǁChunkǁ__init____mutmut_2, 
        'xǁChunkǁ__init____mutmut_3': xǁChunkǁ__init____mutmut_3, 
        'xǁChunkǁ__init____mutmut_4': xǁChunkǁ__init____mutmut_4, 
        'xǁChunkǁ__init____mutmut_5': xǁChunkǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁChunkǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁChunkǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁChunkǁ__init____mutmut_orig)
    xǁChunkǁ__init____mutmut_orig.__name__ = 'xǁChunkǁ__init__'

    @property
    def empty(self):
        return self.tell() == self.length


class Buffer:
    """Simple buffer for use in single-threaded consumer/filler.

    Stores chunks in a deque to avoid inefficient reallocating
    of large buffers.
    """

    def xǁBufferǁ__init____mutmut_orig(self):
        self.chunks = deque()
        self.current_chunk = None
        self.closed = False
        self.length = 0
        self.written_once = False

    def xǁBufferǁ__init____mutmut_1(self):
        self.chunks = None
        self.current_chunk = None
        self.closed = False
        self.length = 0
        self.written_once = False

    def xǁBufferǁ__init____mutmut_2(self):
        self.chunks = deque()
        self.current_chunk = ""
        self.closed = False
        self.length = 0
        self.written_once = False

    def xǁBufferǁ__init____mutmut_3(self):
        self.chunks = deque()
        self.current_chunk = None
        self.closed = None
        self.length = 0
        self.written_once = False

    def xǁBufferǁ__init____mutmut_4(self):
        self.chunks = deque()
        self.current_chunk = None
        self.closed = True
        self.length = 0
        self.written_once = False

    def xǁBufferǁ__init____mutmut_5(self):
        self.chunks = deque()
        self.current_chunk = None
        self.closed = False
        self.length = None
        self.written_once = False

    def xǁBufferǁ__init____mutmut_6(self):
        self.chunks = deque()
        self.current_chunk = None
        self.closed = False
        self.length = 1
        self.written_once = False

    def xǁBufferǁ__init____mutmut_7(self):
        self.chunks = deque()
        self.current_chunk = None
        self.closed = False
        self.length = 0
        self.written_once = None

    def xǁBufferǁ__init____mutmut_8(self):
        self.chunks = deque()
        self.current_chunk = None
        self.closed = False
        self.length = 0
        self.written_once = True
    
    xǁBufferǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBufferǁ__init____mutmut_1': xǁBufferǁ__init____mutmut_1, 
        'xǁBufferǁ__init____mutmut_2': xǁBufferǁ__init____mutmut_2, 
        'xǁBufferǁ__init____mutmut_3': xǁBufferǁ__init____mutmut_3, 
        'xǁBufferǁ__init____mutmut_4': xǁBufferǁ__init____mutmut_4, 
        'xǁBufferǁ__init____mutmut_5': xǁBufferǁ__init____mutmut_5, 
        'xǁBufferǁ__init____mutmut_6': xǁBufferǁ__init____mutmut_6, 
        'xǁBufferǁ__init____mutmut_7': xǁBufferǁ__init____mutmut_7, 
        'xǁBufferǁ__init____mutmut_8': xǁBufferǁ__init____mutmut_8
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBufferǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBufferǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBufferǁ__init____mutmut_orig)
    xǁBufferǁ__init____mutmut_orig.__name__ = 'xǁBufferǁ__init__'

    def xǁBufferǁ_iterate_chunks__mutmut_orig(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = self.current_chunk or Chunk(self.chunks.popleft())
            except IndexError:
                break

            data = current_chunk.read(bytes_left)
            bytes_left -= len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_1(self, size):
        bytes_left = None

        while bytes_left:
            try:
                current_chunk = self.current_chunk or Chunk(self.chunks.popleft())
            except IndexError:
                break

            data = current_chunk.read(bytes_left)
            bytes_left -= len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_2(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = None
            except IndexError:
                break

            data = current_chunk.read(bytes_left)
            bytes_left -= len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_3(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = self.current_chunk and Chunk(self.chunks.popleft())
            except IndexError:
                break

            data = current_chunk.read(bytes_left)
            bytes_left -= len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_4(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = self.current_chunk or Chunk(None)
            except IndexError:
                break

            data = current_chunk.read(bytes_left)
            bytes_left -= len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_5(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = self.current_chunk or Chunk(self.chunks.popleft())
            except IndexError:
                return

            data = current_chunk.read(bytes_left)
            bytes_left -= len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_6(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = self.current_chunk or Chunk(self.chunks.popleft())
            except IndexError:
                break

            data = None
            bytes_left -= len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_7(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = self.current_chunk or Chunk(self.chunks.popleft())
            except IndexError:
                break

            data = current_chunk.read(None)
            bytes_left -= len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_8(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = self.current_chunk or Chunk(self.chunks.popleft())
            except IndexError:
                break

            data = current_chunk.read(bytes_left)
            bytes_left = len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_9(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = self.current_chunk or Chunk(self.chunks.popleft())
            except IndexError:
                break

            data = current_chunk.read(bytes_left)
            bytes_left += len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_10(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = self.current_chunk or Chunk(self.chunks.popleft())
            except IndexError:
                break

            data = current_chunk.read(bytes_left)
            bytes_left -= len(data)

            if current_chunk.empty:
                self.current_chunk = ""
            else:
                self.current_chunk = current_chunk

            yield data

    def xǁBufferǁ_iterate_chunks__mutmut_11(self, size):
        bytes_left = size

        while bytes_left:
            try:
                current_chunk = self.current_chunk or Chunk(self.chunks.popleft())
            except IndexError:
                break

            data = current_chunk.read(bytes_left)
            bytes_left -= len(data)

            if current_chunk.empty:
                self.current_chunk = None
            else:
                self.current_chunk = None

            yield data
    
    xǁBufferǁ_iterate_chunks__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBufferǁ_iterate_chunks__mutmut_1': xǁBufferǁ_iterate_chunks__mutmut_1, 
        'xǁBufferǁ_iterate_chunks__mutmut_2': xǁBufferǁ_iterate_chunks__mutmut_2, 
        'xǁBufferǁ_iterate_chunks__mutmut_3': xǁBufferǁ_iterate_chunks__mutmut_3, 
        'xǁBufferǁ_iterate_chunks__mutmut_4': xǁBufferǁ_iterate_chunks__mutmut_4, 
        'xǁBufferǁ_iterate_chunks__mutmut_5': xǁBufferǁ_iterate_chunks__mutmut_5, 
        'xǁBufferǁ_iterate_chunks__mutmut_6': xǁBufferǁ_iterate_chunks__mutmut_6, 
        'xǁBufferǁ_iterate_chunks__mutmut_7': xǁBufferǁ_iterate_chunks__mutmut_7, 
        'xǁBufferǁ_iterate_chunks__mutmut_8': xǁBufferǁ_iterate_chunks__mutmut_8, 
        'xǁBufferǁ_iterate_chunks__mutmut_9': xǁBufferǁ_iterate_chunks__mutmut_9, 
        'xǁBufferǁ_iterate_chunks__mutmut_10': xǁBufferǁ_iterate_chunks__mutmut_10, 
        'xǁBufferǁ_iterate_chunks__mutmut_11': xǁBufferǁ_iterate_chunks__mutmut_11
    }
    
    def _iterate_chunks(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁBufferǁ_iterate_chunks__mutmut_orig"), object.__getattribute__(self, "xǁBufferǁ_iterate_chunks__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _iterate_chunks.__signature__ = _mutmut_signature(xǁBufferǁ_iterate_chunks__mutmut_orig)
    xǁBufferǁ_iterate_chunks__mutmut_orig.__name__ = 'xǁBufferǁ_iterate_chunks'

    def xǁBufferǁwrite__mutmut_orig(self, data):
        if not self.closed:
            data = bytes(data)  # Copy so that original buffer may be reused
            self.chunks.append(data)
            self.length += len(data)
            self.written_once = True

    def xǁBufferǁwrite__mutmut_1(self, data):
        if self.closed:
            data = bytes(data)  # Copy so that original buffer may be reused
            self.chunks.append(data)
            self.length += len(data)
            self.written_once = True

    def xǁBufferǁwrite__mutmut_2(self, data):
        if not self.closed:
            data = None  # Copy so that original buffer may be reused
            self.chunks.append(data)
            self.length += len(data)
            self.written_once = True

    def xǁBufferǁwrite__mutmut_3(self, data):
        if not self.closed:
            data = bytes(None)  # Copy so that original buffer may be reused
            self.chunks.append(data)
            self.length += len(data)
            self.written_once = True

    def xǁBufferǁwrite__mutmut_4(self, data):
        if not self.closed:
            data = bytes(data)  # Copy so that original buffer may be reused
            self.chunks.append(None)
            self.length += len(data)
            self.written_once = True

    def xǁBufferǁwrite__mutmut_5(self, data):
        if not self.closed:
            data = bytes(data)  # Copy so that original buffer may be reused
            self.chunks.append(data)
            self.length = len(data)
            self.written_once = True

    def xǁBufferǁwrite__mutmut_6(self, data):
        if not self.closed:
            data = bytes(data)  # Copy so that original buffer may be reused
            self.chunks.append(data)
            self.length -= len(data)
            self.written_once = True

    def xǁBufferǁwrite__mutmut_7(self, data):
        if not self.closed:
            data = bytes(data)  # Copy so that original buffer may be reused
            self.chunks.append(data)
            self.length += len(data)
            self.written_once = None

    def xǁBufferǁwrite__mutmut_8(self, data):
        if not self.closed:
            data = bytes(data)  # Copy so that original buffer may be reused
            self.chunks.append(data)
            self.length += len(data)
            self.written_once = False
    
    xǁBufferǁwrite__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBufferǁwrite__mutmut_1': xǁBufferǁwrite__mutmut_1, 
        'xǁBufferǁwrite__mutmut_2': xǁBufferǁwrite__mutmut_2, 
        'xǁBufferǁwrite__mutmut_3': xǁBufferǁwrite__mutmut_3, 
        'xǁBufferǁwrite__mutmut_4': xǁBufferǁwrite__mutmut_4, 
        'xǁBufferǁwrite__mutmut_5': xǁBufferǁwrite__mutmut_5, 
        'xǁBufferǁwrite__mutmut_6': xǁBufferǁwrite__mutmut_6, 
        'xǁBufferǁwrite__mutmut_7': xǁBufferǁwrite__mutmut_7, 
        'xǁBufferǁwrite__mutmut_8': xǁBufferǁwrite__mutmut_8
    }
    
    def write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBufferǁwrite__mutmut_orig"), object.__getattribute__(self, "xǁBufferǁwrite__mutmut_mutants"), args, kwargs, self)
        return result 
    
    write.__signature__ = _mutmut_signature(xǁBufferǁwrite__mutmut_orig)
    xǁBufferǁwrite__mutmut_orig.__name__ = 'xǁBufferǁwrite'

    def xǁBufferǁread__mutmut_orig(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_1(self, size=-1):
        if size <= 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_2(self, size=-1):
        if size < 1 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_3(self, size=-1):
        if size < 0 and size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_4(self, size=-1):
        if size < 0 or size >= self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_5(self, size=-1):
        if size < 0 or size > self.length:
            size = None

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_6(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_7(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b"XXXX"

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_8(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_9(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_10(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_11(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = None
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_12(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(None)
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_13(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"XXXX".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_14(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_15(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_16(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_17(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(None))
        self.length -= len(data)

        return data

    def xǁBufferǁread__mutmut_18(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length = len(data)

        return data

    def xǁBufferǁread__mutmut_19(self, size=-1):
        if size < 0 or size > self.length:
            size = self.length

        if not size:
            return b""

        data = b"".join(self._iterate_chunks(size))
        self.length += len(data)

        return data
    
    xǁBufferǁread__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBufferǁread__mutmut_1': xǁBufferǁread__mutmut_1, 
        'xǁBufferǁread__mutmut_2': xǁBufferǁread__mutmut_2, 
        'xǁBufferǁread__mutmut_3': xǁBufferǁread__mutmut_3, 
        'xǁBufferǁread__mutmut_4': xǁBufferǁread__mutmut_4, 
        'xǁBufferǁread__mutmut_5': xǁBufferǁread__mutmut_5, 
        'xǁBufferǁread__mutmut_6': xǁBufferǁread__mutmut_6, 
        'xǁBufferǁread__mutmut_7': xǁBufferǁread__mutmut_7, 
        'xǁBufferǁread__mutmut_8': xǁBufferǁread__mutmut_8, 
        'xǁBufferǁread__mutmut_9': xǁBufferǁread__mutmut_9, 
        'xǁBufferǁread__mutmut_10': xǁBufferǁread__mutmut_10, 
        'xǁBufferǁread__mutmut_11': xǁBufferǁread__mutmut_11, 
        'xǁBufferǁread__mutmut_12': xǁBufferǁread__mutmut_12, 
        'xǁBufferǁread__mutmut_13': xǁBufferǁread__mutmut_13, 
        'xǁBufferǁread__mutmut_14': xǁBufferǁread__mutmut_14, 
        'xǁBufferǁread__mutmut_15': xǁBufferǁread__mutmut_15, 
        'xǁBufferǁread__mutmut_16': xǁBufferǁread__mutmut_16, 
        'xǁBufferǁread__mutmut_17': xǁBufferǁread__mutmut_17, 
        'xǁBufferǁread__mutmut_18': xǁBufferǁread__mutmut_18, 
        'xǁBufferǁread__mutmut_19': xǁBufferǁread__mutmut_19
    }
    
    def read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBufferǁread__mutmut_orig"), object.__getattribute__(self, "xǁBufferǁread__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read.__signature__ = _mutmut_signature(xǁBufferǁread__mutmut_orig)
    xǁBufferǁread__mutmut_orig.__name__ = 'xǁBufferǁread'

    def xǁBufferǁclose__mutmut_orig(self):
        self.closed = True

    def xǁBufferǁclose__mutmut_1(self):
        self.closed = None

    def xǁBufferǁclose__mutmut_2(self):
        self.closed = False
    
    xǁBufferǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBufferǁclose__mutmut_1': xǁBufferǁclose__mutmut_1, 
        'xǁBufferǁclose__mutmut_2': xǁBufferǁclose__mutmut_2
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBufferǁclose__mutmut_orig"), object.__getattribute__(self, "xǁBufferǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁBufferǁclose__mutmut_orig)
    xǁBufferǁclose__mutmut_orig.__name__ = 'xǁBufferǁclose'


class RingBuffer(Buffer):
    """Circular buffer for use in multi-threaded consumer/filler."""

    def xǁRingBufferǁ__init____mutmut_orig(self, size=8192 * 4):
        Buffer.__init__(self)

        self.buffer_size = size
        self.buffer_lock = Lock()

        self.event_free = Event()
        self.event_free.set()
        self.event_used = Event()

    def xǁRingBufferǁ__init____mutmut_1(self, size=8192 * 4):
        Buffer.__init__(None)

        self.buffer_size = size
        self.buffer_lock = Lock()

        self.event_free = Event()
        self.event_free.set()
        self.event_used = Event()

    def xǁRingBufferǁ__init____mutmut_2(self, size=8192 * 4):
        Buffer.__init__(self)

        self.buffer_size = None
        self.buffer_lock = Lock()

        self.event_free = Event()
        self.event_free.set()
        self.event_used = Event()

    def xǁRingBufferǁ__init____mutmut_3(self, size=8192 * 4):
        Buffer.__init__(self)

        self.buffer_size = size
        self.buffer_lock = None

        self.event_free = Event()
        self.event_free.set()
        self.event_used = Event()

    def xǁRingBufferǁ__init____mutmut_4(self, size=8192 * 4):
        Buffer.__init__(self)

        self.buffer_size = size
        self.buffer_lock = Lock()

        self.event_free = None
        self.event_free.set()
        self.event_used = Event()

    def xǁRingBufferǁ__init____mutmut_5(self, size=8192 * 4):
        Buffer.__init__(self)

        self.buffer_size = size
        self.buffer_lock = Lock()

        self.event_free = Event()
        self.event_free.set()
        self.event_used = None
    
    xǁRingBufferǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRingBufferǁ__init____mutmut_1': xǁRingBufferǁ__init____mutmut_1, 
        'xǁRingBufferǁ__init____mutmut_2': xǁRingBufferǁ__init____mutmut_2, 
        'xǁRingBufferǁ__init____mutmut_3': xǁRingBufferǁ__init____mutmut_3, 
        'xǁRingBufferǁ__init____mutmut_4': xǁRingBufferǁ__init____mutmut_4, 
        'xǁRingBufferǁ__init____mutmut_5': xǁRingBufferǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRingBufferǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁRingBufferǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁRingBufferǁ__init____mutmut_orig)
    xǁRingBufferǁ__init____mutmut_orig.__name__ = 'xǁRingBufferǁ__init__'

    def xǁRingBufferǁ_check_events__mutmut_orig(self):
        if self.length > 0:
            self.event_used.set()
        else:
            self.event_used.clear()

        if self.is_full:
            self.event_free.clear()
        else:
            self.event_free.set()

    def xǁRingBufferǁ_check_events__mutmut_1(self):
        if self.length >= 0:
            self.event_used.set()
        else:
            self.event_used.clear()

        if self.is_full:
            self.event_free.clear()
        else:
            self.event_free.set()

    def xǁRingBufferǁ_check_events__mutmut_2(self):
        if self.length > 1:
            self.event_used.set()
        else:
            self.event_used.clear()

        if self.is_full:
            self.event_free.clear()
        else:
            self.event_free.set()
    
    xǁRingBufferǁ_check_events__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRingBufferǁ_check_events__mutmut_1': xǁRingBufferǁ_check_events__mutmut_1, 
        'xǁRingBufferǁ_check_events__mutmut_2': xǁRingBufferǁ_check_events__mutmut_2
    }
    
    def _check_events(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRingBufferǁ_check_events__mutmut_orig"), object.__getattribute__(self, "xǁRingBufferǁ_check_events__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _check_events.__signature__ = _mutmut_signature(xǁRingBufferǁ_check_events__mutmut_orig)
    xǁRingBufferǁ_check_events__mutmut_orig.__name__ = 'xǁRingBufferǁ_check_events'

    def xǁRingBufferǁ_read__mutmut_orig(self, size=-1):
        with self.buffer_lock:
            data = Buffer.read(self, size)

            self._check_events()

        return data

    def xǁRingBufferǁ_read__mutmut_1(self, size=-1):
        with self.buffer_lock:
            data = None

            self._check_events()

        return data

    def xǁRingBufferǁ_read__mutmut_2(self, size=-1):
        with self.buffer_lock:
            data = Buffer.read(None, size)

            self._check_events()

        return data

    def xǁRingBufferǁ_read__mutmut_3(self, size=-1):
        with self.buffer_lock:
            data = Buffer.read(self, None)

            self._check_events()

        return data

    def xǁRingBufferǁ_read__mutmut_4(self, size=-1):
        with self.buffer_lock:
            data = Buffer.read(size)

            self._check_events()

        return data

    def xǁRingBufferǁ_read__mutmut_5(self, size=-1):
        with self.buffer_lock:
            data = Buffer.read(self, )

            self._check_events()

        return data
    
    xǁRingBufferǁ_read__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRingBufferǁ_read__mutmut_1': xǁRingBufferǁ_read__mutmut_1, 
        'xǁRingBufferǁ_read__mutmut_2': xǁRingBufferǁ_read__mutmut_2, 
        'xǁRingBufferǁ_read__mutmut_3': xǁRingBufferǁ_read__mutmut_3, 
        'xǁRingBufferǁ_read__mutmut_4': xǁRingBufferǁ_read__mutmut_4, 
        'xǁRingBufferǁ_read__mutmut_5': xǁRingBufferǁ_read__mutmut_5
    }
    
    def _read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRingBufferǁ_read__mutmut_orig"), object.__getattribute__(self, "xǁRingBufferǁ_read__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _read.__signature__ = _mutmut_signature(xǁRingBufferǁ_read__mutmut_orig)
    xǁRingBufferǁ_read__mutmut_orig.__name__ = 'xǁRingBufferǁ_read'

    def xǁRingBufferǁread__mutmut_orig(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(timeout) and self.length == 0:
                raise OSError("Read timeout")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_1(self, size=-1, block=False, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(timeout) and self.length == 0:
                raise OSError("Read timeout")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_2(self, size=-1, block=True, timeout=None):
        if block or not self.closed:
            if not self.event_used.wait(timeout) and self.length == 0:
                raise OSError("Read timeout")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_3(self, size=-1, block=True, timeout=None):
        if block and self.closed:
            if not self.event_used.wait(timeout) and self.length == 0:
                raise OSError("Read timeout")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_4(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if self.event_used.wait(timeout) and self.length == 0:
                raise OSError("Read timeout")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_5(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(None) and self.length == 0:
                raise OSError("Read timeout")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_6(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(timeout) or self.length == 0:
                raise OSError("Read timeout")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_7(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(timeout) and self.length != 0:
                raise OSError("Read timeout")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_8(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(timeout) and self.length == 1:
                raise OSError("Read timeout")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_9(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(timeout) and self.length == 0:
                raise OSError(None)

        return self._read(size)

    def xǁRingBufferǁread__mutmut_10(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(timeout) and self.length == 0:
                raise OSError("XXRead timeoutXX")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_11(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(timeout) and self.length == 0:
                raise OSError("read timeout")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_12(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(timeout) and self.length == 0:
                raise OSError("READ TIMEOUT")

        return self._read(size)

    def xǁRingBufferǁread__mutmut_13(self, size=-1, block=True, timeout=None):
        if block and not self.closed:
            if not self.event_used.wait(timeout) and self.length == 0:
                raise OSError("Read timeout")

        return self._read(None)
    
    xǁRingBufferǁread__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRingBufferǁread__mutmut_1': xǁRingBufferǁread__mutmut_1, 
        'xǁRingBufferǁread__mutmut_2': xǁRingBufferǁread__mutmut_2, 
        'xǁRingBufferǁread__mutmut_3': xǁRingBufferǁread__mutmut_3, 
        'xǁRingBufferǁread__mutmut_4': xǁRingBufferǁread__mutmut_4, 
        'xǁRingBufferǁread__mutmut_5': xǁRingBufferǁread__mutmut_5, 
        'xǁRingBufferǁread__mutmut_6': xǁRingBufferǁread__mutmut_6, 
        'xǁRingBufferǁread__mutmut_7': xǁRingBufferǁread__mutmut_7, 
        'xǁRingBufferǁread__mutmut_8': xǁRingBufferǁread__mutmut_8, 
        'xǁRingBufferǁread__mutmut_9': xǁRingBufferǁread__mutmut_9, 
        'xǁRingBufferǁread__mutmut_10': xǁRingBufferǁread__mutmut_10, 
        'xǁRingBufferǁread__mutmut_11': xǁRingBufferǁread__mutmut_11, 
        'xǁRingBufferǁread__mutmut_12': xǁRingBufferǁread__mutmut_12, 
        'xǁRingBufferǁread__mutmut_13': xǁRingBufferǁread__mutmut_13
    }
    
    def read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRingBufferǁread__mutmut_orig"), object.__getattribute__(self, "xǁRingBufferǁread__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read.__signature__ = _mutmut_signature(xǁRingBufferǁread__mutmut_orig)
    xǁRingBufferǁread__mutmut_orig.__name__ = 'xǁRingBufferǁread'

    def xǁRingBufferǁwrite__mutmut_orig(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_1(self, data):
        if self.closed:
            return

        data_left = None
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_2(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = None

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_3(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left >= 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_4(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 1:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_5(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = None
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_6(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(None, data_left)
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_7(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, None)
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_8(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(data_left)
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_9(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, )
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_10(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = None

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_11(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total + data_left

                Buffer.write(self, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_12(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(None, data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_13(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(self, None)
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_14(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(data[written : written + write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_15(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(self, )
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_16(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(self, data[written : written - write_len])
                data_left -= write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_17(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left = write_len

                self._check_events()

    def xǁRingBufferǁwrite__mutmut_18(self, data):
        if self.closed:
            return

        data_left = len(data)
        data_total = len(data)

        while data_left > 0:
            self.event_free.wait()

            if self.closed:
                return

            with self.buffer_lock:
                write_len = min(self.free, data_left)
                written = data_total - data_left

                Buffer.write(self, data[written : written + write_len])
                data_left += write_len

                self._check_events()
    
    xǁRingBufferǁwrite__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRingBufferǁwrite__mutmut_1': xǁRingBufferǁwrite__mutmut_1, 
        'xǁRingBufferǁwrite__mutmut_2': xǁRingBufferǁwrite__mutmut_2, 
        'xǁRingBufferǁwrite__mutmut_3': xǁRingBufferǁwrite__mutmut_3, 
        'xǁRingBufferǁwrite__mutmut_4': xǁRingBufferǁwrite__mutmut_4, 
        'xǁRingBufferǁwrite__mutmut_5': xǁRingBufferǁwrite__mutmut_5, 
        'xǁRingBufferǁwrite__mutmut_6': xǁRingBufferǁwrite__mutmut_6, 
        'xǁRingBufferǁwrite__mutmut_7': xǁRingBufferǁwrite__mutmut_7, 
        'xǁRingBufferǁwrite__mutmut_8': xǁRingBufferǁwrite__mutmut_8, 
        'xǁRingBufferǁwrite__mutmut_9': xǁRingBufferǁwrite__mutmut_9, 
        'xǁRingBufferǁwrite__mutmut_10': xǁRingBufferǁwrite__mutmut_10, 
        'xǁRingBufferǁwrite__mutmut_11': xǁRingBufferǁwrite__mutmut_11, 
        'xǁRingBufferǁwrite__mutmut_12': xǁRingBufferǁwrite__mutmut_12, 
        'xǁRingBufferǁwrite__mutmut_13': xǁRingBufferǁwrite__mutmut_13, 
        'xǁRingBufferǁwrite__mutmut_14': xǁRingBufferǁwrite__mutmut_14, 
        'xǁRingBufferǁwrite__mutmut_15': xǁRingBufferǁwrite__mutmut_15, 
        'xǁRingBufferǁwrite__mutmut_16': xǁRingBufferǁwrite__mutmut_16, 
        'xǁRingBufferǁwrite__mutmut_17': xǁRingBufferǁwrite__mutmut_17, 
        'xǁRingBufferǁwrite__mutmut_18': xǁRingBufferǁwrite__mutmut_18
    }
    
    def write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRingBufferǁwrite__mutmut_orig"), object.__getattribute__(self, "xǁRingBufferǁwrite__mutmut_mutants"), args, kwargs, self)
        return result 
    
    write.__signature__ = _mutmut_signature(xǁRingBufferǁwrite__mutmut_orig)
    xǁRingBufferǁwrite__mutmut_orig.__name__ = 'xǁRingBufferǁwrite'

    def xǁRingBufferǁresize__mutmut_orig(self, size):
        with self.buffer_lock:
            self.buffer_size = size

            self._check_events()

    def xǁRingBufferǁresize__mutmut_1(self, size):
        with self.buffer_lock:
            self.buffer_size = None

            self._check_events()
    
    xǁRingBufferǁresize__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRingBufferǁresize__mutmut_1': xǁRingBufferǁresize__mutmut_1
    }
    
    def resize(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRingBufferǁresize__mutmut_orig"), object.__getattribute__(self, "xǁRingBufferǁresize__mutmut_mutants"), args, kwargs, self)
        return result 
    
    resize.__signature__ = _mutmut_signature(xǁRingBufferǁresize__mutmut_orig)
    xǁRingBufferǁresize__mutmut_orig.__name__ = 'xǁRingBufferǁresize'

    def xǁRingBufferǁwait_free__mutmut_orig(self, timeout=None):
        return self.event_free.wait(timeout)

    def xǁRingBufferǁwait_free__mutmut_1(self, timeout=None):
        return self.event_free.wait(None)
    
    xǁRingBufferǁwait_free__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRingBufferǁwait_free__mutmut_1': xǁRingBufferǁwait_free__mutmut_1
    }
    
    def wait_free(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRingBufferǁwait_free__mutmut_orig"), object.__getattribute__(self, "xǁRingBufferǁwait_free__mutmut_mutants"), args, kwargs, self)
        return result 
    
    wait_free.__signature__ = _mutmut_signature(xǁRingBufferǁwait_free__mutmut_orig)
    xǁRingBufferǁwait_free__mutmut_orig.__name__ = 'xǁRingBufferǁwait_free'

    def xǁRingBufferǁwait_used__mutmut_orig(self, timeout=None):
        return self.event_used.wait(timeout)

    def xǁRingBufferǁwait_used__mutmut_1(self, timeout=None):
        return self.event_used.wait(None)
    
    xǁRingBufferǁwait_used__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRingBufferǁwait_used__mutmut_1': xǁRingBufferǁwait_used__mutmut_1
    }
    
    def wait_used(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRingBufferǁwait_used__mutmut_orig"), object.__getattribute__(self, "xǁRingBufferǁwait_used__mutmut_mutants"), args, kwargs, self)
        return result 
    
    wait_used.__signature__ = _mutmut_signature(xǁRingBufferǁwait_used__mutmut_orig)
    xǁRingBufferǁwait_used__mutmut_orig.__name__ = 'xǁRingBufferǁwait_used'

    def xǁRingBufferǁclose__mutmut_orig(self):
        Buffer.close(self)

        # Make sure we don't let a .write() and .read() block forever
        self.event_free.set()
        self.event_used.set()

    def xǁRingBufferǁclose__mutmut_1(self):
        Buffer.close(None)

        # Make sure we don't let a .write() and .read() block forever
        self.event_free.set()
        self.event_used.set()
    
    xǁRingBufferǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRingBufferǁclose__mutmut_1': xǁRingBufferǁclose__mutmut_1
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRingBufferǁclose__mutmut_orig"), object.__getattribute__(self, "xǁRingBufferǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁRingBufferǁclose__mutmut_orig)
    xǁRingBufferǁclose__mutmut_orig.__name__ = 'xǁRingBufferǁclose'

    @property
    def free(self):
        return max(self.buffer_size - self.length, 0)

    @property
    def is_full(self):
        return self.free == 0


__all__ = ["Buffer", "RingBuffer"]

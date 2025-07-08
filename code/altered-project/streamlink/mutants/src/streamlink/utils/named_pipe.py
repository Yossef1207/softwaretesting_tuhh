from __future__ import annotations

import abc
import logging
import os
import random
import tempfile
import threading
from contextlib import suppress
from pathlib import Path

from streamlink.compat import is_win32


try:
    from ctypes import byref, c_ulong, c_void_p, cast, windll  # type: ignore[attr-defined]
except ImportError:
    pass


log = logging.getLogger(__name__)

_lock = threading.Lock()
_id = 0
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


class NamedPipeBase(abc.ABC):
    path: Path

    def xǁNamedPipeBaseǁ__init____mutmut_orig(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id += 1
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(0, 9999)}"
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_1(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id = 1
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(0, 9999)}"
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_2(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id -= 1
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(0, 9999)}"
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_3(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id += 2
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(0, 9999)}"
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_4(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id += 1
            self.name = None
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_5(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id += 1
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(None, 9999)}"
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_6(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id += 1
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(0, None)}"
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_7(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id += 1
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(9999)}"
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_8(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id += 1
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(0, )}"
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_9(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id += 1
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(1, 9999)}"
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_10(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id += 1
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(0, 10000)}"
        log.info(f"Creating pipe {self.name}")
        self._create()

    def xǁNamedPipeBaseǁ__init____mutmut_11(self):
        global _id  # noqa: PLW0603
        with _lock:
            _id += 1
            self.name = f"streamlinkpipe-{os.getpid()}-{_id}-{random.randint(0, 9999)}"
        log.info(None)
        self._create()
    
    xǁNamedPipeBaseǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNamedPipeBaseǁ__init____mutmut_1': xǁNamedPipeBaseǁ__init____mutmut_1, 
        'xǁNamedPipeBaseǁ__init____mutmut_2': xǁNamedPipeBaseǁ__init____mutmut_2, 
        'xǁNamedPipeBaseǁ__init____mutmut_3': xǁNamedPipeBaseǁ__init____mutmut_3, 
        'xǁNamedPipeBaseǁ__init____mutmut_4': xǁNamedPipeBaseǁ__init____mutmut_4, 
        'xǁNamedPipeBaseǁ__init____mutmut_5': xǁNamedPipeBaseǁ__init____mutmut_5, 
        'xǁNamedPipeBaseǁ__init____mutmut_6': xǁNamedPipeBaseǁ__init____mutmut_6, 
        'xǁNamedPipeBaseǁ__init____mutmut_7': xǁNamedPipeBaseǁ__init____mutmut_7, 
        'xǁNamedPipeBaseǁ__init____mutmut_8': xǁNamedPipeBaseǁ__init____mutmut_8, 
        'xǁNamedPipeBaseǁ__init____mutmut_9': xǁNamedPipeBaseǁ__init____mutmut_9, 
        'xǁNamedPipeBaseǁ__init____mutmut_10': xǁNamedPipeBaseǁ__init____mutmut_10, 
        'xǁNamedPipeBaseǁ__init____mutmut_11': xǁNamedPipeBaseǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNamedPipeBaseǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁNamedPipeBaseǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁNamedPipeBaseǁ__init____mutmut_orig)
    xǁNamedPipeBaseǁ__init____mutmut_orig.__name__ = 'xǁNamedPipeBaseǁ__init__'

    @abc.abstractmethod
    def _create(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def open(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def write(self, data) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def close(self) -> None:
        raise NotImplementedError


class NamedPipePosix(NamedPipeBase):
    mode = "wb"
    permissions = 0o660
    fifo = None

    def xǁNamedPipePosixǁ_create__mutmut_orig(self):
        self.path = Path(tempfile.gettempdir(), self.name)
        os.mkfifo(self.path, self.permissions)

    def xǁNamedPipePosixǁ_create__mutmut_1(self):
        self.path = None
        os.mkfifo(self.path, self.permissions)

    def xǁNamedPipePosixǁ_create__mutmut_2(self):
        self.path = Path(None, self.name)
        os.mkfifo(self.path, self.permissions)

    def xǁNamedPipePosixǁ_create__mutmut_3(self):
        self.path = Path(tempfile.gettempdir(), None)
        os.mkfifo(self.path, self.permissions)

    def xǁNamedPipePosixǁ_create__mutmut_4(self):
        self.path = Path(self.name)
        os.mkfifo(self.path, self.permissions)

    def xǁNamedPipePosixǁ_create__mutmut_5(self):
        self.path = Path(tempfile.gettempdir(), )
        os.mkfifo(self.path, self.permissions)

    def xǁNamedPipePosixǁ_create__mutmut_6(self):
        self.path = Path(tempfile.gettempdir(), self.name)
        os.mkfifo(None, self.permissions)

    def xǁNamedPipePosixǁ_create__mutmut_7(self):
        self.path = Path(tempfile.gettempdir(), self.name)
        os.mkfifo(self.path, None)

    def xǁNamedPipePosixǁ_create__mutmut_8(self):
        self.path = Path(tempfile.gettempdir(), self.name)
        os.mkfifo(self.permissions)

    def xǁNamedPipePosixǁ_create__mutmut_9(self):
        self.path = Path(tempfile.gettempdir(), self.name)
        os.mkfifo(self.path, )
    
    xǁNamedPipePosixǁ_create__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNamedPipePosixǁ_create__mutmut_1': xǁNamedPipePosixǁ_create__mutmut_1, 
        'xǁNamedPipePosixǁ_create__mutmut_2': xǁNamedPipePosixǁ_create__mutmut_2, 
        'xǁNamedPipePosixǁ_create__mutmut_3': xǁNamedPipePosixǁ_create__mutmut_3, 
        'xǁNamedPipePosixǁ_create__mutmut_4': xǁNamedPipePosixǁ_create__mutmut_4, 
        'xǁNamedPipePosixǁ_create__mutmut_5': xǁNamedPipePosixǁ_create__mutmut_5, 
        'xǁNamedPipePosixǁ_create__mutmut_6': xǁNamedPipePosixǁ_create__mutmut_6, 
        'xǁNamedPipePosixǁ_create__mutmut_7': xǁNamedPipePosixǁ_create__mutmut_7, 
        'xǁNamedPipePosixǁ_create__mutmut_8': xǁNamedPipePosixǁ_create__mutmut_8, 
        'xǁNamedPipePosixǁ_create__mutmut_9': xǁNamedPipePosixǁ_create__mutmut_9
    }
    
    def _create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNamedPipePosixǁ_create__mutmut_orig"), object.__getattribute__(self, "xǁNamedPipePosixǁ_create__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _create.__signature__ = _mutmut_signature(xǁNamedPipePosixǁ_create__mutmut_orig)
    xǁNamedPipePosixǁ_create__mutmut_orig.__name__ = 'xǁNamedPipePosixǁ_create'

    def xǁNamedPipePosixǁopen__mutmut_orig(self):
        self.fifo = open(self.path, self.mode)

    def xǁNamedPipePosixǁopen__mutmut_1(self):
        self.fifo = None

    def xǁNamedPipePosixǁopen__mutmut_2(self):
        self.fifo = open(None, self.mode)

    def xǁNamedPipePosixǁopen__mutmut_3(self):
        self.fifo = open(self.path, None)

    def xǁNamedPipePosixǁopen__mutmut_4(self):
        self.fifo = open(self.mode)

    def xǁNamedPipePosixǁopen__mutmut_5(self):
        self.fifo = open(self.path, )
    
    xǁNamedPipePosixǁopen__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNamedPipePosixǁopen__mutmut_1': xǁNamedPipePosixǁopen__mutmut_1, 
        'xǁNamedPipePosixǁopen__mutmut_2': xǁNamedPipePosixǁopen__mutmut_2, 
        'xǁNamedPipePosixǁopen__mutmut_3': xǁNamedPipePosixǁopen__mutmut_3, 
        'xǁNamedPipePosixǁopen__mutmut_4': xǁNamedPipePosixǁopen__mutmut_4, 
        'xǁNamedPipePosixǁopen__mutmut_5': xǁNamedPipePosixǁopen__mutmut_5
    }
    
    def open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNamedPipePosixǁopen__mutmut_orig"), object.__getattribute__(self, "xǁNamedPipePosixǁopen__mutmut_mutants"), args, kwargs, self)
        return result 
    
    open.__signature__ = _mutmut_signature(xǁNamedPipePosixǁopen__mutmut_orig)
    xǁNamedPipePosixǁopen__mutmut_orig.__name__ = 'xǁNamedPipePosixǁopen'

    def xǁNamedPipePosixǁwrite__mutmut_orig(self, data):
        return self.fifo.write(data)

    def xǁNamedPipePosixǁwrite__mutmut_1(self, data):
        return self.fifo.write(None)
    
    xǁNamedPipePosixǁwrite__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNamedPipePosixǁwrite__mutmut_1': xǁNamedPipePosixǁwrite__mutmut_1
    }
    
    def write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNamedPipePosixǁwrite__mutmut_orig"), object.__getattribute__(self, "xǁNamedPipePosixǁwrite__mutmut_mutants"), args, kwargs, self)
        return result 
    
    write.__signature__ = _mutmut_signature(xǁNamedPipePosixǁwrite__mutmut_orig)
    xǁNamedPipePosixǁwrite__mutmut_orig.__name__ = 'xǁNamedPipePosixǁwrite'

    def xǁNamedPipePosixǁclose__mutmut_orig(self):
        try:
            if self.fifo is not None:
                self.fifo.close()
        except OSError:
            raise
        finally:
            with suppress(OSError):
                self.path.unlink()
            self.fifo = None

    def xǁNamedPipePosixǁclose__mutmut_1(self):
        try:
            if self.fifo is None:
                self.fifo.close()
        except OSError:
            raise
        finally:
            with suppress(OSError):
                self.path.unlink()
            self.fifo = None

    def xǁNamedPipePosixǁclose__mutmut_2(self):
        try:
            if self.fifo is not None:
                self.fifo.close()
        except OSError:
            raise
        finally:
            with suppress(None):
                self.path.unlink()
            self.fifo = None

    def xǁNamedPipePosixǁclose__mutmut_3(self):
        try:
            if self.fifo is not None:
                self.fifo.close()
        except OSError:
            raise
        finally:
            with suppress(OSError):
                self.path.unlink()
            self.fifo = ""
    
    xǁNamedPipePosixǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNamedPipePosixǁclose__mutmut_1': xǁNamedPipePosixǁclose__mutmut_1, 
        'xǁNamedPipePosixǁclose__mutmut_2': xǁNamedPipePosixǁclose__mutmut_2, 
        'xǁNamedPipePosixǁclose__mutmut_3': xǁNamedPipePosixǁclose__mutmut_3
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNamedPipePosixǁclose__mutmut_orig"), object.__getattribute__(self, "xǁNamedPipePosixǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁNamedPipePosixǁclose__mutmut_orig)
    xǁNamedPipePosixǁclose__mutmut_orig.__name__ = 'xǁNamedPipePosixǁclose'


class NamedPipeWindows(NamedPipeBase):
    bufsize = 8192
    pipe = None

    PIPE_ACCESS_OUTBOUND = 0x00000002
    PIPE_TYPE_BYTE = 0x00000000
    PIPE_READMODE_BYTE = 0x00000000
    PIPE_WAIT = 0x00000000
    PIPE_UNLIMITED_INSTANCES = 255
    INVALID_HANDLE_VALUE = -1

    @staticmethod
    def _get_last_error():
        error_code = windll.kernel32.GetLastError()
        raise OSError(f"Named pipe error code 0x{error_code:08X}")

    def xǁNamedPipeWindowsǁ_create__mutmut_orig(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_1(self):
        self.path = None
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_2(self):
        self.path = Path(None, self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_3(self):
        self.path = Path("\\\\.\\pipe", None)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_4(self):
        self.path = Path(self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_5(self):
        self.path = Path("\\\\.\\pipe", )
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_6(self):
        self.path = Path("XX\\\\.\\pipeXX", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_7(self):
        self.path = Path("\\\\.\\PIPE", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_8(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = None
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_9(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            None,
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_10(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            None,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_11(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            None,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_12(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            None,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_13(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            None,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_14(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            None,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_15(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            None,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_16(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_17(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_18(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_19(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_20(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_21(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_22(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_23(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_24(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(None),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_25(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE & self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_26(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE & self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_27(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            1,
            None,
        )
        if self.pipe == self.INVALID_HANDLE_VALUE:
            self._get_last_error()

    def xǁNamedPipeWindowsǁ_create__mutmut_28(self):
        self.path = Path("\\\\.\\pipe", self.name)
        self.pipe = windll.kernel32.CreateNamedPipeW(
            str(self.path),
            self.PIPE_ACCESS_OUTBOUND,
            self.PIPE_TYPE_BYTE | self.PIPE_READMODE_BYTE | self.PIPE_WAIT,
            self.PIPE_UNLIMITED_INSTANCES,
            self.bufsize,
            self.bufsize,
            0,
            None,
        )
        if self.pipe != self.INVALID_HANDLE_VALUE:
            self._get_last_error()
    
    xǁNamedPipeWindowsǁ_create__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNamedPipeWindowsǁ_create__mutmut_1': xǁNamedPipeWindowsǁ_create__mutmut_1, 
        'xǁNamedPipeWindowsǁ_create__mutmut_2': xǁNamedPipeWindowsǁ_create__mutmut_2, 
        'xǁNamedPipeWindowsǁ_create__mutmut_3': xǁNamedPipeWindowsǁ_create__mutmut_3, 
        'xǁNamedPipeWindowsǁ_create__mutmut_4': xǁNamedPipeWindowsǁ_create__mutmut_4, 
        'xǁNamedPipeWindowsǁ_create__mutmut_5': xǁNamedPipeWindowsǁ_create__mutmut_5, 
        'xǁNamedPipeWindowsǁ_create__mutmut_6': xǁNamedPipeWindowsǁ_create__mutmut_6, 
        'xǁNamedPipeWindowsǁ_create__mutmut_7': xǁNamedPipeWindowsǁ_create__mutmut_7, 
        'xǁNamedPipeWindowsǁ_create__mutmut_8': xǁNamedPipeWindowsǁ_create__mutmut_8, 
        'xǁNamedPipeWindowsǁ_create__mutmut_9': xǁNamedPipeWindowsǁ_create__mutmut_9, 
        'xǁNamedPipeWindowsǁ_create__mutmut_10': xǁNamedPipeWindowsǁ_create__mutmut_10, 
        'xǁNamedPipeWindowsǁ_create__mutmut_11': xǁNamedPipeWindowsǁ_create__mutmut_11, 
        'xǁNamedPipeWindowsǁ_create__mutmut_12': xǁNamedPipeWindowsǁ_create__mutmut_12, 
        'xǁNamedPipeWindowsǁ_create__mutmut_13': xǁNamedPipeWindowsǁ_create__mutmut_13, 
        'xǁNamedPipeWindowsǁ_create__mutmut_14': xǁNamedPipeWindowsǁ_create__mutmut_14, 
        'xǁNamedPipeWindowsǁ_create__mutmut_15': xǁNamedPipeWindowsǁ_create__mutmut_15, 
        'xǁNamedPipeWindowsǁ_create__mutmut_16': xǁNamedPipeWindowsǁ_create__mutmut_16, 
        'xǁNamedPipeWindowsǁ_create__mutmut_17': xǁNamedPipeWindowsǁ_create__mutmut_17, 
        'xǁNamedPipeWindowsǁ_create__mutmut_18': xǁNamedPipeWindowsǁ_create__mutmut_18, 
        'xǁNamedPipeWindowsǁ_create__mutmut_19': xǁNamedPipeWindowsǁ_create__mutmut_19, 
        'xǁNamedPipeWindowsǁ_create__mutmut_20': xǁNamedPipeWindowsǁ_create__mutmut_20, 
        'xǁNamedPipeWindowsǁ_create__mutmut_21': xǁNamedPipeWindowsǁ_create__mutmut_21, 
        'xǁNamedPipeWindowsǁ_create__mutmut_22': xǁNamedPipeWindowsǁ_create__mutmut_22, 
        'xǁNamedPipeWindowsǁ_create__mutmut_23': xǁNamedPipeWindowsǁ_create__mutmut_23, 
        'xǁNamedPipeWindowsǁ_create__mutmut_24': xǁNamedPipeWindowsǁ_create__mutmut_24, 
        'xǁNamedPipeWindowsǁ_create__mutmut_25': xǁNamedPipeWindowsǁ_create__mutmut_25, 
        'xǁNamedPipeWindowsǁ_create__mutmut_26': xǁNamedPipeWindowsǁ_create__mutmut_26, 
        'xǁNamedPipeWindowsǁ_create__mutmut_27': xǁNamedPipeWindowsǁ_create__mutmut_27, 
        'xǁNamedPipeWindowsǁ_create__mutmut_28': xǁNamedPipeWindowsǁ_create__mutmut_28
    }
    
    def _create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNamedPipeWindowsǁ_create__mutmut_orig"), object.__getattribute__(self, "xǁNamedPipeWindowsǁ_create__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _create.__signature__ = _mutmut_signature(xǁNamedPipeWindowsǁ_create__mutmut_orig)
    xǁNamedPipeWindowsǁ_create__mutmut_orig.__name__ = 'xǁNamedPipeWindowsǁ_create'

    def xǁNamedPipeWindowsǁopen__mutmut_orig(self):
        windll.kernel32.ConnectNamedPipe(self.pipe, None)

    def xǁNamedPipeWindowsǁopen__mutmut_1(self):
        windll.kernel32.ConnectNamedPipe(None, None)

    def xǁNamedPipeWindowsǁopen__mutmut_2(self):
        windll.kernel32.ConnectNamedPipe(None)

    def xǁNamedPipeWindowsǁopen__mutmut_3(self):
        windll.kernel32.ConnectNamedPipe(self.pipe, )
    
    xǁNamedPipeWindowsǁopen__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNamedPipeWindowsǁopen__mutmut_1': xǁNamedPipeWindowsǁopen__mutmut_1, 
        'xǁNamedPipeWindowsǁopen__mutmut_2': xǁNamedPipeWindowsǁopen__mutmut_2, 
        'xǁNamedPipeWindowsǁopen__mutmut_3': xǁNamedPipeWindowsǁopen__mutmut_3
    }
    
    def open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNamedPipeWindowsǁopen__mutmut_orig"), object.__getattribute__(self, "xǁNamedPipeWindowsǁopen__mutmut_mutants"), args, kwargs, self)
        return result 
    
    open.__signature__ = _mutmut_signature(xǁNamedPipeWindowsǁopen__mutmut_orig)
    xǁNamedPipeWindowsǁopen__mutmut_orig.__name__ = 'xǁNamedPipeWindowsǁopen'

    def xǁNamedPipeWindowsǁwrite__mutmut_orig(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, c_void_p),
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_1(self, data):
        written = None
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, c_void_p),
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_2(self, data):
        written = c_ulong(None)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, c_void_p),
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_3(self, data):
        written = c_ulong(1)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, c_void_p),
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_4(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            None,
            cast(data, c_void_p),
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_5(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            None,
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_6(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, c_void_p),
            None,
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_7(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, c_void_p),
            len(data),
            None,
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_8(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            cast(data, c_void_p),
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_9(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_10(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, c_void_p),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_11(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, c_void_p),
            len(data),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_12(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, c_void_p),
            len(data),
            byref(written),
            )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_13(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(None, c_void_p),
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_14(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, None),
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_15(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(c_void_p),
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_16(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, ),
            len(data),
            byref(written),
            None,
        )
        return written.value

    def xǁNamedPipeWindowsǁwrite__mutmut_17(self, data):
        written = c_ulong(0)
        windll.kernel32.WriteFile(
            self.pipe,
            cast(data, c_void_p),
            len(data),
            byref(None),
            None,
        )
        return written.value
    
    xǁNamedPipeWindowsǁwrite__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNamedPipeWindowsǁwrite__mutmut_1': xǁNamedPipeWindowsǁwrite__mutmut_1, 
        'xǁNamedPipeWindowsǁwrite__mutmut_2': xǁNamedPipeWindowsǁwrite__mutmut_2, 
        'xǁNamedPipeWindowsǁwrite__mutmut_3': xǁNamedPipeWindowsǁwrite__mutmut_3, 
        'xǁNamedPipeWindowsǁwrite__mutmut_4': xǁNamedPipeWindowsǁwrite__mutmut_4, 
        'xǁNamedPipeWindowsǁwrite__mutmut_5': xǁNamedPipeWindowsǁwrite__mutmut_5, 
        'xǁNamedPipeWindowsǁwrite__mutmut_6': xǁNamedPipeWindowsǁwrite__mutmut_6, 
        'xǁNamedPipeWindowsǁwrite__mutmut_7': xǁNamedPipeWindowsǁwrite__mutmut_7, 
        'xǁNamedPipeWindowsǁwrite__mutmut_8': xǁNamedPipeWindowsǁwrite__mutmut_8, 
        'xǁNamedPipeWindowsǁwrite__mutmut_9': xǁNamedPipeWindowsǁwrite__mutmut_9, 
        'xǁNamedPipeWindowsǁwrite__mutmut_10': xǁNamedPipeWindowsǁwrite__mutmut_10, 
        'xǁNamedPipeWindowsǁwrite__mutmut_11': xǁNamedPipeWindowsǁwrite__mutmut_11, 
        'xǁNamedPipeWindowsǁwrite__mutmut_12': xǁNamedPipeWindowsǁwrite__mutmut_12, 
        'xǁNamedPipeWindowsǁwrite__mutmut_13': xǁNamedPipeWindowsǁwrite__mutmut_13, 
        'xǁNamedPipeWindowsǁwrite__mutmut_14': xǁNamedPipeWindowsǁwrite__mutmut_14, 
        'xǁNamedPipeWindowsǁwrite__mutmut_15': xǁNamedPipeWindowsǁwrite__mutmut_15, 
        'xǁNamedPipeWindowsǁwrite__mutmut_16': xǁNamedPipeWindowsǁwrite__mutmut_16, 
        'xǁNamedPipeWindowsǁwrite__mutmut_17': xǁNamedPipeWindowsǁwrite__mutmut_17
    }
    
    def write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNamedPipeWindowsǁwrite__mutmut_orig"), object.__getattribute__(self, "xǁNamedPipeWindowsǁwrite__mutmut_mutants"), args, kwargs, self)
        return result 
    
    write.__signature__ = _mutmut_signature(xǁNamedPipeWindowsǁwrite__mutmut_orig)
    xǁNamedPipeWindowsǁwrite__mutmut_orig.__name__ = 'xǁNamedPipeWindowsǁwrite'

    def xǁNamedPipeWindowsǁclose__mutmut_orig(self):
        try:
            if self.pipe is not None:
                windll.kernel32.DisconnectNamedPipe(self.pipe)
                windll.kernel32.CloseHandle(self.pipe)
        except OSError:
            raise
        finally:
            self.pipe = None

    def xǁNamedPipeWindowsǁclose__mutmut_1(self):
        try:
            if self.pipe is None:
                windll.kernel32.DisconnectNamedPipe(self.pipe)
                windll.kernel32.CloseHandle(self.pipe)
        except OSError:
            raise
        finally:
            self.pipe = None

    def xǁNamedPipeWindowsǁclose__mutmut_2(self):
        try:
            if self.pipe is not None:
                windll.kernel32.DisconnectNamedPipe(None)
                windll.kernel32.CloseHandle(self.pipe)
        except OSError:
            raise
        finally:
            self.pipe = None

    def xǁNamedPipeWindowsǁclose__mutmut_3(self):
        try:
            if self.pipe is not None:
                windll.kernel32.DisconnectNamedPipe(self.pipe)
                windll.kernel32.CloseHandle(None)
        except OSError:
            raise
        finally:
            self.pipe = None

    def xǁNamedPipeWindowsǁclose__mutmut_4(self):
        try:
            if self.pipe is not None:
                windll.kernel32.DisconnectNamedPipe(self.pipe)
                windll.kernel32.CloseHandle(self.pipe)
        except OSError:
            raise
        finally:
            self.pipe = ""
    
    xǁNamedPipeWindowsǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNamedPipeWindowsǁclose__mutmut_1': xǁNamedPipeWindowsǁclose__mutmut_1, 
        'xǁNamedPipeWindowsǁclose__mutmut_2': xǁNamedPipeWindowsǁclose__mutmut_2, 
        'xǁNamedPipeWindowsǁclose__mutmut_3': xǁNamedPipeWindowsǁclose__mutmut_3, 
        'xǁNamedPipeWindowsǁclose__mutmut_4': xǁNamedPipeWindowsǁclose__mutmut_4
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNamedPipeWindowsǁclose__mutmut_orig"), object.__getattribute__(self, "xǁNamedPipeWindowsǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁNamedPipeWindowsǁclose__mutmut_orig)
    xǁNamedPipeWindowsǁclose__mutmut_orig.__name__ = 'xǁNamedPipeWindowsǁclose'


NamedPipe: type[NamedPipeBase]
if not is_win32:
    NamedPipe = NamedPipePosix
else:
    NamedPipe = NamedPipeWindows

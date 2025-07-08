from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from streamlink.compat import is_win32
from streamlink_cli.compat import stdout
from streamlink_cli.output.abc import Output


if is_win32:
    import msvcrt
    from os import O_BINARY  # type: ignore[attr-defined]
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


class FileOutput(Output):
    def xǁFileOutputǁ__init____mutmut_orig(
        self,
        filename: Path | None = None,
        fd: BinaryIO | None = None,
        record: FileOutput | None = None,
    ):
        super().__init__()
        self.filename = filename
        self.fd = fd
        self.record = record
    def xǁFileOutputǁ__init____mutmut_1(
        self,
        filename: Path | None = None,
        fd: BinaryIO | None = None,
        record: FileOutput | None = None,
    ):
        super().__init__()
        self.filename = None
        self.fd = fd
        self.record = record
    def xǁFileOutputǁ__init____mutmut_2(
        self,
        filename: Path | None = None,
        fd: BinaryIO | None = None,
        record: FileOutput | None = None,
    ):
        super().__init__()
        self.filename = filename
        self.fd = None
        self.record = record
    def xǁFileOutputǁ__init____mutmut_3(
        self,
        filename: Path | None = None,
        fd: BinaryIO | None = None,
        record: FileOutput | None = None,
    ):
        super().__init__()
        self.filename = filename
        self.fd = fd
        self.record = None
    
    xǁFileOutputǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileOutputǁ__init____mutmut_1': xǁFileOutputǁ__init____mutmut_1, 
        'xǁFileOutputǁ__init____mutmut_2': xǁFileOutputǁ__init____mutmut_2, 
        'xǁFileOutputǁ__init____mutmut_3': xǁFileOutputǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileOutputǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁFileOutputǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁFileOutputǁ__init____mutmut_orig)
    xǁFileOutputǁ__init____mutmut_orig.__name__ = 'xǁFileOutputǁ__init__'

    def xǁFileOutputǁ_open__mutmut_orig(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_1(self):
        if self.filename:
            self.filename.parent.mkdir(parents=None, exist_ok=True)
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_2(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=None)
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_3(self):
        if self.filename:
            self.filename.parent.mkdir(exist_ok=True)
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_4(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, )
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_5(self):
        if self.filename:
            self.filename.parent.mkdir(parents=False, exist_ok=True)
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_6(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=False)
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_7(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            self.fd = None

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_8(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            self.fd = self.filename.open(None)

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_9(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            self.fd = self.filename.open("XXwbXX")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_10(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            self.fd = self.filename.open("WB")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_11(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            self.fd = self.filename.open("Wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), O_BINARY)

    def xǁFileOutputǁ_open__mutmut_12(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(None, O_BINARY)

    def xǁFileOutputǁ_open__mutmut_13(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), None)

    def xǁFileOutputǁ_open__mutmut_14(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(O_BINARY)

    def xǁFileOutputǁ_open__mutmut_15(self):
        if self.filename:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            self.fd = self.filename.open("wb")

        if self.record:
            self.record.open()

        if is_win32:
            msvcrt.setmode(self.fd.fileno(), )
    
    xǁFileOutputǁ_open__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileOutputǁ_open__mutmut_1': xǁFileOutputǁ_open__mutmut_1, 
        'xǁFileOutputǁ_open__mutmut_2': xǁFileOutputǁ_open__mutmut_2, 
        'xǁFileOutputǁ_open__mutmut_3': xǁFileOutputǁ_open__mutmut_3, 
        'xǁFileOutputǁ_open__mutmut_4': xǁFileOutputǁ_open__mutmut_4, 
        'xǁFileOutputǁ_open__mutmut_5': xǁFileOutputǁ_open__mutmut_5, 
        'xǁFileOutputǁ_open__mutmut_6': xǁFileOutputǁ_open__mutmut_6, 
        'xǁFileOutputǁ_open__mutmut_7': xǁFileOutputǁ_open__mutmut_7, 
        'xǁFileOutputǁ_open__mutmut_8': xǁFileOutputǁ_open__mutmut_8, 
        'xǁFileOutputǁ_open__mutmut_9': xǁFileOutputǁ_open__mutmut_9, 
        'xǁFileOutputǁ_open__mutmut_10': xǁFileOutputǁ_open__mutmut_10, 
        'xǁFileOutputǁ_open__mutmut_11': xǁFileOutputǁ_open__mutmut_11, 
        'xǁFileOutputǁ_open__mutmut_12': xǁFileOutputǁ_open__mutmut_12, 
        'xǁFileOutputǁ_open__mutmut_13': xǁFileOutputǁ_open__mutmut_13, 
        'xǁFileOutputǁ_open__mutmut_14': xǁFileOutputǁ_open__mutmut_14, 
        'xǁFileOutputǁ_open__mutmut_15': xǁFileOutputǁ_open__mutmut_15
    }
    
    def _open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileOutputǁ_open__mutmut_orig"), object.__getattribute__(self, "xǁFileOutputǁ_open__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _open.__signature__ = _mutmut_signature(xǁFileOutputǁ_open__mutmut_orig)
    xǁFileOutputǁ_open__mutmut_orig.__name__ = 'xǁFileOutputǁ_open'

    def xǁFileOutputǁ_close__mutmut_orig(self):
        if self.fd is not stdout:
            self.fd.close()
        if self.record:
            self.record.close()

    def xǁFileOutputǁ_close__mutmut_1(self):
        if self.fd is stdout:
            self.fd.close()
        if self.record:
            self.record.close()
    
    xǁFileOutputǁ_close__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileOutputǁ_close__mutmut_1': xǁFileOutputǁ_close__mutmut_1
    }
    
    def _close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileOutputǁ_close__mutmut_orig"), object.__getattribute__(self, "xǁFileOutputǁ_close__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _close.__signature__ = _mutmut_signature(xǁFileOutputǁ_close__mutmut_orig)
    xǁFileOutputǁ_close__mutmut_orig.__name__ = 'xǁFileOutputǁ_close'

    def xǁFileOutputǁ_write__mutmut_orig(self, data):
        self.fd.write(data)
        if self.record:
            self.record.write(data)

    def xǁFileOutputǁ_write__mutmut_1(self, data):
        self.fd.write(None)
        if self.record:
            self.record.write(data)

    def xǁFileOutputǁ_write__mutmut_2(self, data):
        self.fd.write(data)
        if self.record:
            self.record.write(None)
    
    xǁFileOutputǁ_write__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileOutputǁ_write__mutmut_1': xǁFileOutputǁ_write__mutmut_1, 
        'xǁFileOutputǁ_write__mutmut_2': xǁFileOutputǁ_write__mutmut_2
    }
    
    def _write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileOutputǁ_write__mutmut_orig"), object.__getattribute__(self, "xǁFileOutputǁ_write__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _write.__signature__ = _mutmut_signature(xǁFileOutputǁ_write__mutmut_orig)
    xǁFileOutputǁ_write__mutmut_orig.__name__ = 'xǁFileOutputǁ_write'

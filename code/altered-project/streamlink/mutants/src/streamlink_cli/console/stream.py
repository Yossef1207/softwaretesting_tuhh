from __future__ import annotations

import os
from io import TextIOWrapper
from threading import RLock
from typing import Iterable, Iterator

from streamlink.compat import is_win32
from streamlink_cli.console.stream_wrapper import StreamWrapper
from streamlink_cli.console.windows import WindowsConsole
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


class ConsoleStatusMessage(str):
    pass


class ConsoleOutputStream(StreamWrapper):
    def __new__(cls, stream: TextIOWrapper) -> ConsoleOutputStream:
        if stream.isatty():
            if (
                is_win32
                and (windows_console := WindowsConsole(stream))
                and not windows_console.supports_virtual_terminal_processing()
            ):
                console_output_stream_windows = super().__new__(ConsoleOutputStreamWindows)
                console_output_stream_windows.windows_console = windows_console
                return console_output_stream_windows

            if os.environ.get("TERM", "").lower() not in ("dumb", "unknown"):
                return super().__new__(ConsoleOutputStreamANSI)

        return super().__new__(cls)

    def xǁConsoleOutputStreamǁ__init____mutmut_orig(self, stream: TextIOWrapper):
        super().__init__(stream)
        self._lock = RLock()
        self._line_buffer: list[str] = []

    def xǁConsoleOutputStreamǁ__init____mutmut_1(self, stream: TextIOWrapper):
        super().__init__(None)
        self._lock = RLock()
        self._line_buffer: list[str] = []

    def xǁConsoleOutputStreamǁ__init____mutmut_2(self, stream: TextIOWrapper):
        super().__init__(stream)
        self._lock = None
        self._line_buffer: list[str] = []

    def xǁConsoleOutputStreamǁ__init____mutmut_3(self, stream: TextIOWrapper):
        super().__init__(stream)
        self._lock = RLock()
        self._line_buffer: list[str] = None
    
    xǁConsoleOutputStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputStreamǁ__init____mutmut_1': xǁConsoleOutputStreamǁ__init____mutmut_1, 
        'xǁConsoleOutputStreamǁ__init____mutmut_2': xǁConsoleOutputStreamǁ__init____mutmut_2, 
        'xǁConsoleOutputStreamǁ__init____mutmut_3': xǁConsoleOutputStreamǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁConsoleOutputStreamǁ__init____mutmut_orig)
    xǁConsoleOutputStreamǁ__init____mutmut_orig.__name__ = 'xǁConsoleOutputStreamǁ__init__'

    @classmethod
    def supports_status_messages(cls):
        return False

    def xǁConsoleOutputStreamǁ_get_lines__mutmut_orig(self, msg: str) -> Iterator[str]:
        while msg:
            line, nl, msg = msg.partition("\n")
            if nl:
                yield f"{''.join(self._line_buffer)}{line}{nl}"
                self._line_buffer.clear()
            else:
                self._line_buffer.append(line)

    def xǁConsoleOutputStreamǁ_get_lines__mutmut_1(self, msg: str) -> Iterator[str]:
        while msg:
            line, nl, msg = None
            if nl:
                yield f"{''.join(self._line_buffer)}{line}{nl}"
                self._line_buffer.clear()
            else:
                self._line_buffer.append(line)

    def xǁConsoleOutputStreamǁ_get_lines__mutmut_2(self, msg: str) -> Iterator[str]:
        while msg:
            line, nl, msg = msg.partition(None)
            if nl:
                yield f"{''.join(self._line_buffer)}{line}{nl}"
                self._line_buffer.clear()
            else:
                self._line_buffer.append(line)

    def xǁConsoleOutputStreamǁ_get_lines__mutmut_3(self, msg: str) -> Iterator[str]:
        while msg:
            line, nl, msg = msg.rpartition("\n")
            if nl:
                yield f"{''.join(self._line_buffer)}{line}{nl}"
                self._line_buffer.clear()
            else:
                self._line_buffer.append(line)

    def xǁConsoleOutputStreamǁ_get_lines__mutmut_4(self, msg: str) -> Iterator[str]:
        while msg:
            line, nl, msg = msg.partition("XX\nXX")
            if nl:
                yield f"{''.join(self._line_buffer)}{line}{nl}"
                self._line_buffer.clear()
            else:
                self._line_buffer.append(line)

    def xǁConsoleOutputStreamǁ_get_lines__mutmut_5(self, msg: str) -> Iterator[str]:
        while msg:
            line, nl, msg = msg.partition("\N")
            if nl:
                yield f"{''.join(self._line_buffer)}{line}{nl}"
                self._line_buffer.clear()
            else:
                self._line_buffer.append(line)

    def xǁConsoleOutputStreamǁ_get_lines__mutmut_6(self, msg: str) -> Iterator[str]:
        while msg:
            line, nl, msg = msg.partition("\n")
            if nl:
                yield f"{''.join(None)}{line}{nl}"
                self._line_buffer.clear()
            else:
                self._line_buffer.append(line)

    def xǁConsoleOutputStreamǁ_get_lines__mutmut_7(self, msg: str) -> Iterator[str]:
        while msg:
            line, nl, msg = msg.partition("\n")
            if nl:
                yield f"{'XXXX'.join(self._line_buffer)}{line}{nl}"
                self._line_buffer.clear()
            else:
                self._line_buffer.append(line)

    def xǁConsoleOutputStreamǁ_get_lines__mutmut_8(self, msg: str) -> Iterator[str]:
        while msg:
            line, nl, msg = msg.partition("\n")
            if nl:
                yield f"{''.join(self._line_buffer)}{line}{nl}"
                self._line_buffer.clear()
            else:
                self._line_buffer.append(None)
    
    xǁConsoleOutputStreamǁ_get_lines__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputStreamǁ_get_lines__mutmut_1': xǁConsoleOutputStreamǁ_get_lines__mutmut_1, 
        'xǁConsoleOutputStreamǁ_get_lines__mutmut_2': xǁConsoleOutputStreamǁ_get_lines__mutmut_2, 
        'xǁConsoleOutputStreamǁ_get_lines__mutmut_3': xǁConsoleOutputStreamǁ_get_lines__mutmut_3, 
        'xǁConsoleOutputStreamǁ_get_lines__mutmut_4': xǁConsoleOutputStreamǁ_get_lines__mutmut_4, 
        'xǁConsoleOutputStreamǁ_get_lines__mutmut_5': xǁConsoleOutputStreamǁ_get_lines__mutmut_5, 
        'xǁConsoleOutputStreamǁ_get_lines__mutmut_6': xǁConsoleOutputStreamǁ_get_lines__mutmut_6, 
        'xǁConsoleOutputStreamǁ_get_lines__mutmut_7': xǁConsoleOutputStreamǁ_get_lines__mutmut_7, 
        'xǁConsoleOutputStreamǁ_get_lines__mutmut_8': xǁConsoleOutputStreamǁ_get_lines__mutmut_8
    }
    
    def _get_lines(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁConsoleOutputStreamǁ_get_lines__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputStreamǁ_get_lines__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_lines.__signature__ = _mutmut_signature(xǁConsoleOutputStreamǁ_get_lines__mutmut_orig)
    xǁConsoleOutputStreamǁ_get_lines__mutmut_orig.__name__ = 'xǁConsoleOutputStreamǁ_get_lines'

    def xǁConsoleOutputStreamǁclose__mutmut_orig(self):
        with self._lock:
            if not self.closed:
                self.flush()

            return self._stream.close()

    def xǁConsoleOutputStreamǁclose__mutmut_1(self):
        with self._lock:
            if self.closed:
                self.flush()

            return self._stream.close()
    
    xǁConsoleOutputStreamǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputStreamǁclose__mutmut_1': xǁConsoleOutputStreamǁclose__mutmut_1
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputStreamǁclose__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputStreamǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁConsoleOutputStreamǁclose__mutmut_orig)
    xǁConsoleOutputStreamǁclose__mutmut_orig.__name__ = 'xǁConsoleOutputStreamǁclose'

    def xǁConsoleOutputStreamǁflush__mutmut_orig(self):
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if rest := "".join(self._line_buffer):
                self._line_buffer.clear()
                self._stream.write(rest)
            self._stream.flush()

    def xǁConsoleOutputStreamǁflush__mutmut_1(self):
        with self._lock:
            if self._stream.closed:
                raise ValueError(None)

            if rest := "".join(self._line_buffer):
                self._line_buffer.clear()
                self._stream.write(rest)
            self._stream.flush()

    def xǁConsoleOutputStreamǁflush__mutmut_2(self):
        with self._lock:
            if self._stream.closed:
                raise ValueError("XXI/O operation on closed file.XX")

            if rest := "".join(self._line_buffer):
                self._line_buffer.clear()
                self._stream.write(rest)
            self._stream.flush()

    def xǁConsoleOutputStreamǁflush__mutmut_3(self):
        with self._lock:
            if self._stream.closed:
                raise ValueError("i/o operation on closed file.")

            if rest := "".join(self._line_buffer):
                self._line_buffer.clear()
                self._stream.write(rest)
            self._stream.flush()

    def xǁConsoleOutputStreamǁflush__mutmut_4(self):
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O OPERATION ON CLOSED FILE.")

            if rest := "".join(self._line_buffer):
                self._line_buffer.clear()
                self._stream.write(rest)
            self._stream.flush()

    def xǁConsoleOutputStreamǁflush__mutmut_5(self):
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/o operation on closed file.")

            if rest := "".join(self._line_buffer):
                self._line_buffer.clear()
                self._stream.write(rest)
            self._stream.flush()

    def xǁConsoleOutputStreamǁflush__mutmut_6(self):
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if rest := "".join(None):
                self._line_buffer.clear()
                self._stream.write(rest)
            self._stream.flush()

    def xǁConsoleOutputStreamǁflush__mutmut_7(self):
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if rest := "XXXX".join(self._line_buffer):
                self._line_buffer.clear()
                self._stream.write(rest)
            self._stream.flush()

    def xǁConsoleOutputStreamǁflush__mutmut_8(self):
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if rest := "".join(self._line_buffer):
                self._line_buffer.clear()
                self._stream.write(None)
            self._stream.flush()
    
    xǁConsoleOutputStreamǁflush__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputStreamǁflush__mutmut_1': xǁConsoleOutputStreamǁflush__mutmut_1, 
        'xǁConsoleOutputStreamǁflush__mutmut_2': xǁConsoleOutputStreamǁflush__mutmut_2, 
        'xǁConsoleOutputStreamǁflush__mutmut_3': xǁConsoleOutputStreamǁflush__mutmut_3, 
        'xǁConsoleOutputStreamǁflush__mutmut_4': xǁConsoleOutputStreamǁflush__mutmut_4, 
        'xǁConsoleOutputStreamǁflush__mutmut_5': xǁConsoleOutputStreamǁflush__mutmut_5, 
        'xǁConsoleOutputStreamǁflush__mutmut_6': xǁConsoleOutputStreamǁflush__mutmut_6, 
        'xǁConsoleOutputStreamǁflush__mutmut_7': xǁConsoleOutputStreamǁflush__mutmut_7, 
        'xǁConsoleOutputStreamǁflush__mutmut_8': xǁConsoleOutputStreamǁflush__mutmut_8
    }
    
    def flush(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputStreamǁflush__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputStreamǁflush__mutmut_mutants"), args, kwargs, self)
        return result 
    
    flush.__signature__ = _mutmut_signature(xǁConsoleOutputStreamǁflush__mutmut_orig)
    xǁConsoleOutputStreamǁflush__mutmut_orig.__name__ = 'xǁConsoleOutputStreamǁflush'

    def xǁConsoleOutputStreamǁwrite__mutmut_orig(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_1(self, s: str) -> int:
        written = None

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_2(self, s: str) -> int:
        written = 1

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_3(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError(None)

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_4(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("XXI/O operation on closed file.XX")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_5(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("i/o operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_6(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O OPERATION ON CLOSED FILE.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_7(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/o operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_8(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(None) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_9(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_10(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(None):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_11(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "XXXX".join(self._get_lines(s)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_12(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(None)):
                    written = self._stream.write(lines)

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_13(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = None

        return written

    def xǁConsoleOutputStreamǁwrite__mutmut_14(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                if lines := "".join(self._get_lines(s)):
                    written = self._stream.write(None)

        return written
    
    xǁConsoleOutputStreamǁwrite__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputStreamǁwrite__mutmut_1': xǁConsoleOutputStreamǁwrite__mutmut_1, 
        'xǁConsoleOutputStreamǁwrite__mutmut_2': xǁConsoleOutputStreamǁwrite__mutmut_2, 
        'xǁConsoleOutputStreamǁwrite__mutmut_3': xǁConsoleOutputStreamǁwrite__mutmut_3, 
        'xǁConsoleOutputStreamǁwrite__mutmut_4': xǁConsoleOutputStreamǁwrite__mutmut_4, 
        'xǁConsoleOutputStreamǁwrite__mutmut_5': xǁConsoleOutputStreamǁwrite__mutmut_5, 
        'xǁConsoleOutputStreamǁwrite__mutmut_6': xǁConsoleOutputStreamǁwrite__mutmut_6, 
        'xǁConsoleOutputStreamǁwrite__mutmut_7': xǁConsoleOutputStreamǁwrite__mutmut_7, 
        'xǁConsoleOutputStreamǁwrite__mutmut_8': xǁConsoleOutputStreamǁwrite__mutmut_8, 
        'xǁConsoleOutputStreamǁwrite__mutmut_9': xǁConsoleOutputStreamǁwrite__mutmut_9, 
        'xǁConsoleOutputStreamǁwrite__mutmut_10': xǁConsoleOutputStreamǁwrite__mutmut_10, 
        'xǁConsoleOutputStreamǁwrite__mutmut_11': xǁConsoleOutputStreamǁwrite__mutmut_11, 
        'xǁConsoleOutputStreamǁwrite__mutmut_12': xǁConsoleOutputStreamǁwrite__mutmut_12, 
        'xǁConsoleOutputStreamǁwrite__mutmut_13': xǁConsoleOutputStreamǁwrite__mutmut_13, 
        'xǁConsoleOutputStreamǁwrite__mutmut_14': xǁConsoleOutputStreamǁwrite__mutmut_14
    }
    
    def write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputStreamǁwrite__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputStreamǁwrite__mutmut_mutants"), args, kwargs, self)
        return result 
    
    write.__signature__ = _mutmut_signature(xǁConsoleOutputStreamǁwrite__mutmut_orig)
    xǁConsoleOutputStreamǁwrite__mutmut_orig.__name__ = 'xǁConsoleOutputStreamǁwrite'

    def xǁConsoleOutputStreamǁwritelines__mutmut_orig(self, lines: Iterable[str], /) -> None:  # type: ignore[override]
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            self.write("".join(lines))

    def xǁConsoleOutputStreamǁwritelines__mutmut_1(self, lines: Iterable[str], /) -> None:  # type: ignore[override]
        with self._lock:
            if self._stream.closed:
                raise ValueError(None)

            self.write("".join(lines))

    def xǁConsoleOutputStreamǁwritelines__mutmut_2(self, lines: Iterable[str], /) -> None:  # type: ignore[override]
        with self._lock:
            if self._stream.closed:
                raise ValueError("XXI/O operation on closed file.XX")

            self.write("".join(lines))

    def xǁConsoleOutputStreamǁwritelines__mutmut_3(self, lines: Iterable[str], /) -> None:  # type: ignore[override]
        with self._lock:
            if self._stream.closed:
                raise ValueError("i/o operation on closed file.")

            self.write("".join(lines))

    def xǁConsoleOutputStreamǁwritelines__mutmut_4(self, lines: Iterable[str], /) -> None:  # type: ignore[override]
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O OPERATION ON CLOSED FILE.")

            self.write("".join(lines))

    def xǁConsoleOutputStreamǁwritelines__mutmut_5(self, lines: Iterable[str], /) -> None:  # type: ignore[override]
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/o operation on closed file.")

            self.write("".join(lines))

    def xǁConsoleOutputStreamǁwritelines__mutmut_6(self, lines: Iterable[str], /) -> None:  # type: ignore[override]
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            self.write(None)

    def xǁConsoleOutputStreamǁwritelines__mutmut_7(self, lines: Iterable[str], /) -> None:  # type: ignore[override]
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            self.write("".join(None))

    def xǁConsoleOutputStreamǁwritelines__mutmut_8(self, lines: Iterable[str], /) -> None:  # type: ignore[override]
        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            self.write("XXXX".join(lines))
    
    xǁConsoleOutputStreamǁwritelines__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputStreamǁwritelines__mutmut_1': xǁConsoleOutputStreamǁwritelines__mutmut_1, 
        'xǁConsoleOutputStreamǁwritelines__mutmut_2': xǁConsoleOutputStreamǁwritelines__mutmut_2, 
        'xǁConsoleOutputStreamǁwritelines__mutmut_3': xǁConsoleOutputStreamǁwritelines__mutmut_3, 
        'xǁConsoleOutputStreamǁwritelines__mutmut_4': xǁConsoleOutputStreamǁwritelines__mutmut_4, 
        'xǁConsoleOutputStreamǁwritelines__mutmut_5': xǁConsoleOutputStreamǁwritelines__mutmut_5, 
        'xǁConsoleOutputStreamǁwritelines__mutmut_6': xǁConsoleOutputStreamǁwritelines__mutmut_6, 
        'xǁConsoleOutputStreamǁwritelines__mutmut_7': xǁConsoleOutputStreamǁwritelines__mutmut_7, 
        'xǁConsoleOutputStreamǁwritelines__mutmut_8': xǁConsoleOutputStreamǁwritelines__mutmut_8
    }
    
    def writelines(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputStreamǁwritelines__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputStreamǁwritelines__mutmut_mutants"), args, kwargs, self)
        return result 
    
    writelines.__signature__ = _mutmut_signature(xǁConsoleOutputStreamǁwritelines__mutmut_orig)
    xǁConsoleOutputStreamǁwritelines__mutmut_orig.__name__ = 'xǁConsoleOutputStreamǁwritelines'


class _ConsoleOutputStreamWithStatusMessages(ConsoleOutputStream):
    def xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_orig(self, stream: TextIOWrapper):
        super().__init__(stream)
        self._last_status: str = ""
    def xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_1(self, stream: TextIOWrapper):
        super().__init__(None)
        self._last_status: str = ""
    def xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_2(self, stream: TextIOWrapper):
        super().__init__(stream)
        self._last_status: str = None
    def xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_3(self, stream: TextIOWrapper):
        super().__init__(stream)
        self._last_status: str = "XXXX"
    
    xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_1': xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_1, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_2': xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_2, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_3': xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_orig)
    xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init____mutmut_orig.__name__ = 'xǁ_ConsoleOutputStreamWithStatusMessagesǁ__init__'

    @classmethod
    def supports_status_messages(cls):
        return True

    def clear_line(self, s: str) -> str:  # pragma: no cover
        return s

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_orig(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_1(self):
        with self._lock:
            if self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_2(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = None
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_3(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(None)
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_4(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(None)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_5(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{'XXXX'.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_6(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = None
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_7(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(None)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_8(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{'XXXX'.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_9(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = None
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_10(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "XX\nXX"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_11(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\N"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_12(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = None
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_13(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = "XXXX"
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_14(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = None
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_15(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = "XXXX"
                if s:
                    self._stream.write(s)
                    self._stream.flush()

            return self._stream.close()

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_16(self):
        with self._lock:
            if not self.closed:
                if self._line_buffer:
                    if self._last_status:
                        s = self.clear_line(f"{''.join(self._line_buffer)}\n{self._last_status}\n")
                    else:
                        s = f"{''.join(self._line_buffer)}\n"
                else:
                    if self._last_status:
                        s = "\n"
                    else:
                        s = ""
                self._line_buffer.clear()
                self._last_status = ""
                if s:
                    self._stream.write(None)
                    self._stream.flush()

            return self._stream.close()
    
    xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_1': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_1, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_2': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_2, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_3': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_3, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_4': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_4, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_5': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_5, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_6': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_6, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_7': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_7, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_8': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_8, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_9': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_9, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_10': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_10, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_11': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_11, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_12': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_12, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_13': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_13, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_14': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_14, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_15': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_15, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_16': xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_16
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_orig"), object.__getattribute__(self, "xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_orig)
    xǁ_ConsoleOutputStreamWithStatusMessagesǁclose__mutmut_orig.__name__ = 'xǁ_ConsoleOutputStreamWithStatusMessagesǁclose'

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_orig(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_1(self, s: str) -> int:
        written = None

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_2(self, s: str) -> int:
        written = 1

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_3(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError(None)

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_4(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("XXI/O operation on closed file.XX")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_5(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("i/o operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_6(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O OPERATION ON CLOSED FILE.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_7(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/o operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_8(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(None) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_9(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is not ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_10(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = None
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_11(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip(None)
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_12(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("XX\r\nXX")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_13(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\R\N")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_14(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = None
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_15(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = None
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_16(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(None)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_17(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = None
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_18(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = None
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_19(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(None)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_20(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(None):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_21(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "XXXX".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_22(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(None)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_23(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = None
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_24(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(None)
                else:
                    s = lines
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_25(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = None
                written = self._stream.write(s)

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_26(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = None

        return written

    def xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_27(self, s: str) -> int:
        written = 0

        with self._lock:
            if self._stream.closed:
                raise ValueError("I/O operation on closed file.")

            if type(s) is ConsoleStatusMessage:
                s = s.strip("\r\n")
                if self._last_status:
                    self._last_status = s
                    s = self.clear_line(s)
                else:
                    self._last_status = s
                written = self._stream.write(s)
                self._stream.flush()

            elif lines := "".join(self._get_lines(s)):
                if self._last_status:
                    s = self.clear_line(f"{lines}{self._last_status}")
                else:
                    s = lines
                written = self._stream.write(None)

        return written
    
    xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_1': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_1, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_2': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_2, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_3': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_3, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_4': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_4, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_5': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_5, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_6': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_6, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_7': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_7, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_8': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_8, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_9': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_9, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_10': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_10, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_11': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_11, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_12': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_12, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_13': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_13, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_14': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_14, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_15': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_15, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_16': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_16, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_17': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_17, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_18': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_18, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_19': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_19, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_20': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_20, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_21': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_21, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_22': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_22, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_23': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_23, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_24': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_24, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_25': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_25, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_26': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_26, 
        'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_27': xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_27
    }
    
    def write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_orig"), object.__getattribute__(self, "xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_mutants"), args, kwargs, self)
        return result 
    
    write.__signature__ = _mutmut_signature(xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_orig)
    xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite__mutmut_orig.__name__ = 'xǁ_ConsoleOutputStreamWithStatusMessagesǁwrite'


class ConsoleOutputStreamANSI(_ConsoleOutputStreamWithStatusMessages):
    _CR_CLREOL = "\r\x1b[K"

    def clear_line(self, s: str) -> str:
        return f"{self._CR_CLREOL}{s}"


class ConsoleOutputStreamWindows(_ConsoleOutputStreamWithStatusMessages):
    windows_console: WindowsConsole

    def clear_line(self, s: str) -> str:
        self.windows_console.clear_line()

        return s

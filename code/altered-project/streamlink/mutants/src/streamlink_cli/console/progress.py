from __future__ import annotations

import os
from collections import deque
from collections.abc import Callable, Iterable, Mapping
from math import floor
from pathlib import PurePath
from string import Formatter as StringFormatter
from threading import Event, RLock, Thread
from time import time
from typing import TYPE_CHECKING

from streamlink_cli.console.console import ConsoleOutput
from streamlink_cli.console.terminal import cut_text, term_width, text_width


if TYPE_CHECKING:
    from typing_extensions import TypeAlias


_stringformatter = StringFormatter()
_TFormat: TypeAlias = "Iterable[Iterable[tuple[str, str | None, str | None, str | None]]]"
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


class ProgressFormatter:
    # Store formats as a tuple of lists of parsed format strings,
    # so when iterating, we don't have to parse over and over again.
    # Reserve at least 15 characters for the path, so it can be truncated with enough useful information.
    FORMATS: _TFormat = tuple(
        list(_stringformatter.parse(fmt))
        for fmt in (
            "[download] Written {written} to {path:15} ({elapsed} @ {speed})",
            "[download] Written {written} ({elapsed} @ {speed})",
            "[download] {written} ({elapsed} @ {speed})",
            "[download] {written} ({elapsed})",
            "[download] {written}",
        )
    )
    FORMATS_NOSPEED: _TFormat = tuple(
        list(_stringformatter.parse(fmt))
        for fmt in (
            "[download] Written {written} to {path:15} ({elapsed})",
            "[download] Written {written} ({elapsed})",
            "[download] {written} ({elapsed})",
            "[download] {written}",
        )
    )

    # Use U+2026 (HORIZONTAL ELLIPSIS) to be able to distinguish between "." and ".." when truncating relative paths
    ELLIPSIS: str = "…"

    @classmethod
    def format(cls, formats: _TFormat, params: Mapping[str, str | Callable[[int], str]]) -> str:
        width = term_width()
        static: list[str] = []
        variable: list[tuple[int, Callable[[int], str], int]] = []

        for fmt in formats:
            static.clear()
            variable.clear()
            length = 0
            # Get literal texts, static segments and variable segments from the parsed format
            # and calculate the overall length of the literal texts and static segments after substituting them.
            for literal_text, field_name, format_spec, _conversion in fmt:
                static.append(literal_text)
                length += len(literal_text)
                if field_name is None:
                    continue
                if field_name not in params:
                    break
                value_or_callable = params[field_name]
                if not callable(value_or_callable):
                    static.append(value_or_callable)
                    length += len(value_or_callable)
                else:
                    variable.append((len(static), value_or_callable, int(format_spec or 0)))
                    static.append("")
            else:
                # No variable segments? Just check if the resulting string fits into the size constraints.
                if not variable:
                    if length > width:
                        continue
                    else:
                        break

                # Get the available space for each variable segment (share space equally and round down).
                max_width = int((width - length) / len(variable))
                # If at least one variable segment doesn't fit, continue with the next format.
                if max_width < 1 or any(max_width < min_width for _, __, min_width in variable):
                    continue
                # All variable segments fit, so finally format them, but continue with the next format if there's an error.
                # noinspection PyBroadException
                try:
                    for idx, fn, _ in variable:
                        static[idx] = fn(max_width)
                except Exception:
                    continue
                break

        return "".join(static)

    @staticmethod
    def _round(num: float, n: int = 2) -> float:
        return floor(num * 10**n) / 10**n

    @classmethod
    def format_filesize(cls, size: float, suffix: str = "") -> str:
        if size < 1024:
            return f"{size:.0f} bytes{suffix}"
        if size < 2**20:
            return f"{cls._round(size / 2**10, 2):.2f} KiB{suffix}"
        if size < 2**30:
            return f"{cls._round(size / 2**20, 2):.2f} MiB{suffix}"
        if size < 2**40:
            return f"{cls._round(size / 2**30, 2):.2f} GiB{suffix}"

        return f"{cls._round(size / 2**40, 2):.2f} TiB{suffix}"

    @classmethod
    def format_time(cls, elapsed: float) -> str:
        elapsed = max(elapsed, 0)

        if elapsed < 60:
            return f"{int(elapsed % 60):1d}s"
        if elapsed < 3600:
            return f"{int(elapsed % 3600 / 60):1d}m{int(elapsed % 60):02d}s"

        return f"{int(elapsed / 3600)}h{int(elapsed % 3600 / 60):02d}m{int(elapsed % 60):02d}s"

    @classmethod
    def format_path(cls, path: PurePath, max_width: int) -> str:
        # Quick check if the path fits
        string = str(path)
        width = text_width(string)
        if width <= max_width:
            return string

        # Since the path doesn't fit, we always need to add an ellipsis.
        # On Windows, we also need to add the "drive" part (which is an empty string on PurePosixPath)
        max_width -= text_width(path.drive) + text_width(cls.ELLIPSIS)

        # Ignore the path's first part, aka the "anchor" (drive + root)
        parts = os.path.sep.join(path.parts[1:] if path.drive else path.parts)
        truncated = cut_text(parts, max_width)

        return f"{path.drive}{cls.ELLIPSIS}{truncated}"


class Progress(Thread):
    def xǁProgressǁ__init____mutmut_orig(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_1(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 1.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_2(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 21,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_3(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 3,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_4(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = False,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_5(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=None)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_6(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=False)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_7(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = None
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_8(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = None

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_9(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = None

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_10(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = None
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_11(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = None
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_12(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = None
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_13(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = None
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_14(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=None)
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_15(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(None))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_16(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history * interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_17(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = None

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_18(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(None)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_19(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold * interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_20(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = None
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_21(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 1.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_22(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = None
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_23(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 1
        self.written: int = 0
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_24(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = None
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_25(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 1
        self.status: bool = status
    def xǁProgressǁ__init____mutmut_26(
        self,
        console: ConsoleOutput,
        path: PurePath,
        interval: float = 0.25,
        history: int = 20,
        threshold: int = 2,
        status: bool = True,
    ):
        """
        :param console: The console output
        :param interval: Time in seconds between updates
        :param history: Number of seconds of how long download speed history is kept
        :param threshold: Number of seconds until download speed is shown
        """

        super().__init__(daemon=True)
        self._wait = Event()
        self._lock = RLock()

        self.formatter = ProgressFormatter()

        self.console: ConsoleOutput = console
        self.path: PurePath = path
        self.interval: float = interval
        self.history: deque[tuple[float, int]] = deque(maxlen=int(history / interval))
        self.threshold: int = int(threshold / interval)

        self.started: float = 0.0
        self.overall: int = 0
        self.written: int = 0
        self.status: bool = None
    
    xǁProgressǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProgressǁ__init____mutmut_1': xǁProgressǁ__init____mutmut_1, 
        'xǁProgressǁ__init____mutmut_2': xǁProgressǁ__init____mutmut_2, 
        'xǁProgressǁ__init____mutmut_3': xǁProgressǁ__init____mutmut_3, 
        'xǁProgressǁ__init____mutmut_4': xǁProgressǁ__init____mutmut_4, 
        'xǁProgressǁ__init____mutmut_5': xǁProgressǁ__init____mutmut_5, 
        'xǁProgressǁ__init____mutmut_6': xǁProgressǁ__init____mutmut_6, 
        'xǁProgressǁ__init____mutmut_7': xǁProgressǁ__init____mutmut_7, 
        'xǁProgressǁ__init____mutmut_8': xǁProgressǁ__init____mutmut_8, 
        'xǁProgressǁ__init____mutmut_9': xǁProgressǁ__init____mutmut_9, 
        'xǁProgressǁ__init____mutmut_10': xǁProgressǁ__init____mutmut_10, 
        'xǁProgressǁ__init____mutmut_11': xǁProgressǁ__init____mutmut_11, 
        'xǁProgressǁ__init____mutmut_12': xǁProgressǁ__init____mutmut_12, 
        'xǁProgressǁ__init____mutmut_13': xǁProgressǁ__init____mutmut_13, 
        'xǁProgressǁ__init____mutmut_14': xǁProgressǁ__init____mutmut_14, 
        'xǁProgressǁ__init____mutmut_15': xǁProgressǁ__init____mutmut_15, 
        'xǁProgressǁ__init____mutmut_16': xǁProgressǁ__init____mutmut_16, 
        'xǁProgressǁ__init____mutmut_17': xǁProgressǁ__init____mutmut_17, 
        'xǁProgressǁ__init____mutmut_18': xǁProgressǁ__init____mutmut_18, 
        'xǁProgressǁ__init____mutmut_19': xǁProgressǁ__init____mutmut_19, 
        'xǁProgressǁ__init____mutmut_20': xǁProgressǁ__init____mutmut_20, 
        'xǁProgressǁ__init____mutmut_21': xǁProgressǁ__init____mutmut_21, 
        'xǁProgressǁ__init____mutmut_22': xǁProgressǁ__init____mutmut_22, 
        'xǁProgressǁ__init____mutmut_23': xǁProgressǁ__init____mutmut_23, 
        'xǁProgressǁ__init____mutmut_24': xǁProgressǁ__init____mutmut_24, 
        'xǁProgressǁ__init____mutmut_25': xǁProgressǁ__init____mutmut_25, 
        'xǁProgressǁ__init____mutmut_26': xǁProgressǁ__init____mutmut_26
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProgressǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁProgressǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁProgressǁ__init____mutmut_orig)
    xǁProgressǁ__init____mutmut_orig.__name__ = 'xǁProgressǁ__init__'

    def close(self):
        self._wait.set()

    def xǁProgressǁwrite__mutmut_orig(self, chunk: bytes):
        size = len(chunk)
        with self._lock:
            self.overall += size
            self.written += size

    def xǁProgressǁwrite__mutmut_1(self, chunk: bytes):
        size = None
        with self._lock:
            self.overall += size
            self.written += size

    def xǁProgressǁwrite__mutmut_2(self, chunk: bytes):
        size = len(chunk)
        with self._lock:
            self.overall = size
            self.written += size

    def xǁProgressǁwrite__mutmut_3(self, chunk: bytes):
        size = len(chunk)
        with self._lock:
            self.overall -= size
            self.written += size

    def xǁProgressǁwrite__mutmut_4(self, chunk: bytes):
        size = len(chunk)
        with self._lock:
            self.overall += size
            self.written = size

    def xǁProgressǁwrite__mutmut_5(self, chunk: bytes):
        size = len(chunk)
        with self._lock:
            self.overall += size
            self.written -= size
    
    xǁProgressǁwrite__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProgressǁwrite__mutmut_1': xǁProgressǁwrite__mutmut_1, 
        'xǁProgressǁwrite__mutmut_2': xǁProgressǁwrite__mutmut_2, 
        'xǁProgressǁwrite__mutmut_3': xǁProgressǁwrite__mutmut_3, 
        'xǁProgressǁwrite__mutmut_4': xǁProgressǁwrite__mutmut_4, 
        'xǁProgressǁwrite__mutmut_5': xǁProgressǁwrite__mutmut_5
    }
    
    def write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProgressǁwrite__mutmut_orig"), object.__getattribute__(self, "xǁProgressǁwrite__mutmut_mutants"), args, kwargs, self)
        return result 
    
    write.__signature__ = _mutmut_signature(xǁProgressǁwrite__mutmut_orig)
    xǁProgressǁwrite__mutmut_orig.__name__ = 'xǁProgressǁwrite'

    def xǁProgressǁrun__mutmut_orig(self):
        self.started = time()
        try:
            while not self._wait.wait(self.interval):
                self.update()
        finally:
            self.update()

    def xǁProgressǁrun__mutmut_1(self):
        self.started = None
        try:
            while not self._wait.wait(self.interval):
                self.update()
        finally:
            self.update()

    def xǁProgressǁrun__mutmut_2(self):
        self.started = time()
        try:
            while self._wait.wait(self.interval):
                self.update()
        finally:
            self.update()

    def xǁProgressǁrun__mutmut_3(self):
        self.started = time()
        try:
            while not self._wait.wait(None):
                self.update()
        finally:
            self.update()
    
    xǁProgressǁrun__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProgressǁrun__mutmut_1': xǁProgressǁrun__mutmut_1, 
        'xǁProgressǁrun__mutmut_2': xǁProgressǁrun__mutmut_2, 
        'xǁProgressǁrun__mutmut_3': xǁProgressǁrun__mutmut_3
    }
    
    def run(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProgressǁrun__mutmut_orig"), object.__getattribute__(self, "xǁProgressǁrun__mutmut_mutants"), args, kwargs, self)
        return result 
    
    run.__signature__ = _mutmut_signature(xǁProgressǁrun__mutmut_orig)
    xǁProgressǁrun__mutmut_orig.__name__ = 'xǁProgressǁrun'

    def xǁProgressǁupdate__mutmut_orig(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_1(self):
        with self._lock:
            now = None
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_2(self):
        with self._lock:
            now = time()
            formatter = None
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_3(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = None

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_4(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append(None)
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_5(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = None

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_6(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 1

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_7(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = None
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_8(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) > self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_9(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_10(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history and now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_11(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now != history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_12(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[1][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_13(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][1]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_14(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = None
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_15(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = None
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_16(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = "XXXX"
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_17(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = None
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_18(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = None

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_19(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(None, "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_20(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), None)

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_21(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize("/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_22(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), )

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_23(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(None) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_24(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) * (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_25(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now + history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_26(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[1][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_27(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][1]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_28(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "XX/sXX")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_29(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/S")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_30(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = None

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_31(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                writtenXX=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_32(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsedXX=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_33(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speedXX=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_34(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                pathXX=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_35(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=None,
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_36(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=None,
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_37(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=None,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_38(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=None,
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_39(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_40(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_41(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_42(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_43(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(None),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_44(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(None),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_45(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now + self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_46(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: None,
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_47(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(None, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_48(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, None),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_49(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_50(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, ),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_51(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = None
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_52(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(None, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_53(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, None)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_54(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_55(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, )
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_56(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(None)
            else:
                self.console.msg(status)

    def xǁProgressǁupdate__mutmut_57(self):
        with self._lock:
            now = time()
            formatter = self.formatter
            history = self.history

            history.append((now, self.written))
            self.written = 0

            has_history = len(history) >= self.threshold
            if not has_history or now == history[0][0]:
                formats = formatter.FORMATS_NOSPEED
                speed = ""
            else:
                formats = formatter.FORMATS
                speed = formatter.format_filesize(sum(size for _, size in history) / (now - history[0][0]), "/s")

            params = dict(
                written=formatter.format_filesize(self.overall),
                elapsed=formatter.format_time(now - self.started),
                speed=speed,
                path=lambda max_width: formatter.format_path(self.path, max_width),
            )

            status = formatter.format(formats, params)
            if self.status:
                self.console.msg_status(status)
            else:
                self.console.msg(None)
    
    xǁProgressǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProgressǁupdate__mutmut_1': xǁProgressǁupdate__mutmut_1, 
        'xǁProgressǁupdate__mutmut_2': xǁProgressǁupdate__mutmut_2, 
        'xǁProgressǁupdate__mutmut_3': xǁProgressǁupdate__mutmut_3, 
        'xǁProgressǁupdate__mutmut_4': xǁProgressǁupdate__mutmut_4, 
        'xǁProgressǁupdate__mutmut_5': xǁProgressǁupdate__mutmut_5, 
        'xǁProgressǁupdate__mutmut_6': xǁProgressǁupdate__mutmut_6, 
        'xǁProgressǁupdate__mutmut_7': xǁProgressǁupdate__mutmut_7, 
        'xǁProgressǁupdate__mutmut_8': xǁProgressǁupdate__mutmut_8, 
        'xǁProgressǁupdate__mutmut_9': xǁProgressǁupdate__mutmut_9, 
        'xǁProgressǁupdate__mutmut_10': xǁProgressǁupdate__mutmut_10, 
        'xǁProgressǁupdate__mutmut_11': xǁProgressǁupdate__mutmut_11, 
        'xǁProgressǁupdate__mutmut_12': xǁProgressǁupdate__mutmut_12, 
        'xǁProgressǁupdate__mutmut_13': xǁProgressǁupdate__mutmut_13, 
        'xǁProgressǁupdate__mutmut_14': xǁProgressǁupdate__mutmut_14, 
        'xǁProgressǁupdate__mutmut_15': xǁProgressǁupdate__mutmut_15, 
        'xǁProgressǁupdate__mutmut_16': xǁProgressǁupdate__mutmut_16, 
        'xǁProgressǁupdate__mutmut_17': xǁProgressǁupdate__mutmut_17, 
        'xǁProgressǁupdate__mutmut_18': xǁProgressǁupdate__mutmut_18, 
        'xǁProgressǁupdate__mutmut_19': xǁProgressǁupdate__mutmut_19, 
        'xǁProgressǁupdate__mutmut_20': xǁProgressǁupdate__mutmut_20, 
        'xǁProgressǁupdate__mutmut_21': xǁProgressǁupdate__mutmut_21, 
        'xǁProgressǁupdate__mutmut_22': xǁProgressǁupdate__mutmut_22, 
        'xǁProgressǁupdate__mutmut_23': xǁProgressǁupdate__mutmut_23, 
        'xǁProgressǁupdate__mutmut_24': xǁProgressǁupdate__mutmut_24, 
        'xǁProgressǁupdate__mutmut_25': xǁProgressǁupdate__mutmut_25, 
        'xǁProgressǁupdate__mutmut_26': xǁProgressǁupdate__mutmut_26, 
        'xǁProgressǁupdate__mutmut_27': xǁProgressǁupdate__mutmut_27, 
        'xǁProgressǁupdate__mutmut_28': xǁProgressǁupdate__mutmut_28, 
        'xǁProgressǁupdate__mutmut_29': xǁProgressǁupdate__mutmut_29, 
        'xǁProgressǁupdate__mutmut_30': xǁProgressǁupdate__mutmut_30, 
        'xǁProgressǁupdate__mutmut_31': xǁProgressǁupdate__mutmut_31, 
        'xǁProgressǁupdate__mutmut_32': xǁProgressǁupdate__mutmut_32, 
        'xǁProgressǁupdate__mutmut_33': xǁProgressǁupdate__mutmut_33, 
        'xǁProgressǁupdate__mutmut_34': xǁProgressǁupdate__mutmut_34, 
        'xǁProgressǁupdate__mutmut_35': xǁProgressǁupdate__mutmut_35, 
        'xǁProgressǁupdate__mutmut_36': xǁProgressǁupdate__mutmut_36, 
        'xǁProgressǁupdate__mutmut_37': xǁProgressǁupdate__mutmut_37, 
        'xǁProgressǁupdate__mutmut_38': xǁProgressǁupdate__mutmut_38, 
        'xǁProgressǁupdate__mutmut_39': xǁProgressǁupdate__mutmut_39, 
        'xǁProgressǁupdate__mutmut_40': xǁProgressǁupdate__mutmut_40, 
        'xǁProgressǁupdate__mutmut_41': xǁProgressǁupdate__mutmut_41, 
        'xǁProgressǁupdate__mutmut_42': xǁProgressǁupdate__mutmut_42, 
        'xǁProgressǁupdate__mutmut_43': xǁProgressǁupdate__mutmut_43, 
        'xǁProgressǁupdate__mutmut_44': xǁProgressǁupdate__mutmut_44, 
        'xǁProgressǁupdate__mutmut_45': xǁProgressǁupdate__mutmut_45, 
        'xǁProgressǁupdate__mutmut_46': xǁProgressǁupdate__mutmut_46, 
        'xǁProgressǁupdate__mutmut_47': xǁProgressǁupdate__mutmut_47, 
        'xǁProgressǁupdate__mutmut_48': xǁProgressǁupdate__mutmut_48, 
        'xǁProgressǁupdate__mutmut_49': xǁProgressǁupdate__mutmut_49, 
        'xǁProgressǁupdate__mutmut_50': xǁProgressǁupdate__mutmut_50, 
        'xǁProgressǁupdate__mutmut_51': xǁProgressǁupdate__mutmut_51, 
        'xǁProgressǁupdate__mutmut_52': xǁProgressǁupdate__mutmut_52, 
        'xǁProgressǁupdate__mutmut_53': xǁProgressǁupdate__mutmut_53, 
        'xǁProgressǁupdate__mutmut_54': xǁProgressǁupdate__mutmut_54, 
        'xǁProgressǁupdate__mutmut_55': xǁProgressǁupdate__mutmut_55, 
        'xǁProgressǁupdate__mutmut_56': xǁProgressǁupdate__mutmut_56, 
        'xǁProgressǁupdate__mutmut_57': xǁProgressǁupdate__mutmut_57
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProgressǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁProgressǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁProgressǁupdate__mutmut_orig)
    xǁProgressǁupdate__mutmut_orig.__name__ = 'xǁProgressǁupdate'

from __future__ import annotations

import logging
import sys
import tempfile
from collections.abc import AsyncGenerator, Generator
from contextlib import AbstractAsyncContextManager, asynccontextmanager, contextmanager
from functools import partial
from pathlib import Path
from subprocess import DEVNULL

import trio

from streamlink.compat import BaseExceptionGroup
from streamlink.utils.path import resolve_executable
from streamlink.webbrowser.exceptions import WebbrowserError


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


class Webbrowser:
    ERROR_RESOLVE = "Could not find web browser executable"

    TIMEOUT = 10

    @classmethod
    def names(cls) -> list[str]:
        return []

    @classmethod
    def fallback_paths(cls) -> list[str | Path]:
        return []

    @classmethod
    def launch_args(cls) -> list[str]:
        return []

    def xǁWebbrowserǁ__init____mutmut_orig(self, executable: str | None = None):
        resolved = resolve_executable(executable, self.names(), self.fallback_paths())
        if not resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_1(self, executable: str | None = None):
        resolved = None
        if not resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_2(self, executable: str | None = None):
        resolved = resolve_executable(None, self.names(), self.fallback_paths())
        if not resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_3(self, executable: str | None = None):
        resolved = resolve_executable(executable, None, self.fallback_paths())
        if not resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_4(self, executable: str | None = None):
        resolved = resolve_executable(executable, self.names(), None)
        if not resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_5(self, executable: str | None = None):
        resolved = resolve_executable(self.names(), self.fallback_paths())
        if not resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_6(self, executable: str | None = None):
        resolved = resolve_executable(executable, self.fallback_paths())
        if not resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_7(self, executable: str | None = None):
        resolved = resolve_executable(executable, self.names(), )
        if not resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_8(self, executable: str | None = None):
        resolved = resolve_executable(executable, self.names(), self.fallback_paths())
        if resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_9(self, executable: str | None = None):
        resolved = resolve_executable(executable, self.names(), self.fallback_paths())
        if not resolved:
            raise WebbrowserError(
                None,
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_10(self, executable: str | None = None):
        resolved = resolve_executable(executable, self.names(), self.fallback_paths())
        if not resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = None
        self.arguments: list[str] = self.launch_args().copy()

    def xǁWebbrowserǁ__init____mutmut_11(self, executable: str | None = None):
        resolved = resolve_executable(executable, self.names(), self.fallback_paths())
        if not resolved:
            raise WebbrowserError(
                f"Invalid web browser executable: {executable}"
                if executable
                else f"{self.ERROR_RESOLVE}: Please set the path to a supported web browser using --webbrowser-executable",
            )

        self.executable: str | Path = resolved
        self.arguments: list[str] = None
    
    xǁWebbrowserǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebbrowserǁ__init____mutmut_1': xǁWebbrowserǁ__init____mutmut_1, 
        'xǁWebbrowserǁ__init____mutmut_2': xǁWebbrowserǁ__init____mutmut_2, 
        'xǁWebbrowserǁ__init____mutmut_3': xǁWebbrowserǁ__init____mutmut_3, 
        'xǁWebbrowserǁ__init____mutmut_4': xǁWebbrowserǁ__init____mutmut_4, 
        'xǁWebbrowserǁ__init____mutmut_5': xǁWebbrowserǁ__init____mutmut_5, 
        'xǁWebbrowserǁ__init____mutmut_6': xǁWebbrowserǁ__init____mutmut_6, 
        'xǁWebbrowserǁ__init____mutmut_7': xǁWebbrowserǁ__init____mutmut_7, 
        'xǁWebbrowserǁ__init____mutmut_8': xǁWebbrowserǁ__init____mutmut_8, 
        'xǁWebbrowserǁ__init____mutmut_9': xǁWebbrowserǁ__init____mutmut_9, 
        'xǁWebbrowserǁ__init____mutmut_10': xǁWebbrowserǁ__init____mutmut_10, 
        'xǁWebbrowserǁ__init____mutmut_11': xǁWebbrowserǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebbrowserǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWebbrowserǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWebbrowserǁ__init____mutmut_orig)
    xǁWebbrowserǁ__init____mutmut_orig.__name__ = 'xǁWebbrowserǁ__init__'

    def xǁWebbrowserǁlaunch__mutmut_orig(self, headless: bool = False, timeout: float | None = None) -> AbstractAsyncContextManager[trio.Nursery]:
        return self._launch(self.executable, self.arguments, headless=headless, timeout=timeout)

    def xǁWebbrowserǁlaunch__mutmut_1(self, headless: bool = True, timeout: float | None = None) -> AbstractAsyncContextManager[trio.Nursery]:
        return self._launch(self.executable, self.arguments, headless=headless, timeout=timeout)

    def xǁWebbrowserǁlaunch__mutmut_2(self, headless: bool = False, timeout: float | None = None) -> AbstractAsyncContextManager[trio.Nursery]:
        return self._launch(None, self.arguments, headless=headless, timeout=timeout)

    def xǁWebbrowserǁlaunch__mutmut_3(self, headless: bool = False, timeout: float | None = None) -> AbstractAsyncContextManager[trio.Nursery]:
        return self._launch(self.executable, None, headless=headless, timeout=timeout)

    def xǁWebbrowserǁlaunch__mutmut_4(self, headless: bool = False, timeout: float | None = None) -> AbstractAsyncContextManager[trio.Nursery]:
        return self._launch(self.executable, self.arguments, headless=None, timeout=timeout)

    def xǁWebbrowserǁlaunch__mutmut_5(self, headless: bool = False, timeout: float | None = None) -> AbstractAsyncContextManager[trio.Nursery]:
        return self._launch(self.executable, self.arguments, headless=headless, timeout=None)

    def xǁWebbrowserǁlaunch__mutmut_6(self, headless: bool = False, timeout: float | None = None) -> AbstractAsyncContextManager[trio.Nursery]:
        return self._launch(self.arguments, headless=headless, timeout=timeout)

    def xǁWebbrowserǁlaunch__mutmut_7(self, headless: bool = False, timeout: float | None = None) -> AbstractAsyncContextManager[trio.Nursery]:
        return self._launch(self.executable, headless=headless, timeout=timeout)

    def xǁWebbrowserǁlaunch__mutmut_8(self, headless: bool = False, timeout: float | None = None) -> AbstractAsyncContextManager[trio.Nursery]:
        return self._launch(self.executable, self.arguments, timeout=timeout)

    def xǁWebbrowserǁlaunch__mutmut_9(self, headless: bool = False, timeout: float | None = None) -> AbstractAsyncContextManager[trio.Nursery]:
        return self._launch(self.executable, self.arguments, headless=headless, )
    
    xǁWebbrowserǁlaunch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebbrowserǁlaunch__mutmut_1': xǁWebbrowserǁlaunch__mutmut_1, 
        'xǁWebbrowserǁlaunch__mutmut_2': xǁWebbrowserǁlaunch__mutmut_2, 
        'xǁWebbrowserǁlaunch__mutmut_3': xǁWebbrowserǁlaunch__mutmut_3, 
        'xǁWebbrowserǁlaunch__mutmut_4': xǁWebbrowserǁlaunch__mutmut_4, 
        'xǁWebbrowserǁlaunch__mutmut_5': xǁWebbrowserǁlaunch__mutmut_5, 
        'xǁWebbrowserǁlaunch__mutmut_6': xǁWebbrowserǁlaunch__mutmut_6, 
        'xǁWebbrowserǁlaunch__mutmut_7': xǁWebbrowserǁlaunch__mutmut_7, 
        'xǁWebbrowserǁlaunch__mutmut_8': xǁWebbrowserǁlaunch__mutmut_8, 
        'xǁWebbrowserǁlaunch__mutmut_9': xǁWebbrowserǁlaunch__mutmut_9
    }
    
    def launch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebbrowserǁlaunch__mutmut_orig"), object.__getattribute__(self, "xǁWebbrowserǁlaunch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    launch.__signature__ = _mutmut_signature(xǁWebbrowserǁlaunch__mutmut_orig)
    xǁWebbrowserǁlaunch__mutmut_orig.__name__ = 'xǁWebbrowserǁlaunch'

    def xǁWebbrowserǁ_launch__mutmut_orig(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(executable, arguments, headless, timeout)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_1(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = True,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(executable, arguments, headless, timeout)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_2(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is not None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(executable, arguments, headless, timeout)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_3(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = None

        launcher = _WebbrowserLauncher(executable, arguments, headless, timeout)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_4(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = None

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_5(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(None, arguments, headless, timeout)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_6(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(executable, None, headless, timeout)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_7(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(executable, arguments, None, timeout)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_8(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(executable, arguments, headless, None)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_9(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(arguments, headless, timeout)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_10(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(executable, headless, timeout)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_11(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(executable, arguments, timeout)

        # noinspection PyArgumentList
        return launcher.launch()

    def xǁWebbrowserǁ_launch__mutmut_12(
        self,
        executable: str | Path,
        arguments: list[str],
        headless: bool = False,
        timeout: float | None = None,
    ) -> AbstractAsyncContextManager[trio.Nursery]:
        if timeout is None:
            timeout = self.TIMEOUT

        launcher = _WebbrowserLauncher(executable, arguments, headless, )

        # noinspection PyArgumentList
        return launcher.launch()
    
    xǁWebbrowserǁ_launch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebbrowserǁ_launch__mutmut_1': xǁWebbrowserǁ_launch__mutmut_1, 
        'xǁWebbrowserǁ_launch__mutmut_2': xǁWebbrowserǁ_launch__mutmut_2, 
        'xǁWebbrowserǁ_launch__mutmut_3': xǁWebbrowserǁ_launch__mutmut_3, 
        'xǁWebbrowserǁ_launch__mutmut_4': xǁWebbrowserǁ_launch__mutmut_4, 
        'xǁWebbrowserǁ_launch__mutmut_5': xǁWebbrowserǁ_launch__mutmut_5, 
        'xǁWebbrowserǁ_launch__mutmut_6': xǁWebbrowserǁ_launch__mutmut_6, 
        'xǁWebbrowserǁ_launch__mutmut_7': xǁWebbrowserǁ_launch__mutmut_7, 
        'xǁWebbrowserǁ_launch__mutmut_8': xǁWebbrowserǁ_launch__mutmut_8, 
        'xǁWebbrowserǁ_launch__mutmut_9': xǁWebbrowserǁ_launch__mutmut_9, 
        'xǁWebbrowserǁ_launch__mutmut_10': xǁWebbrowserǁ_launch__mutmut_10, 
        'xǁWebbrowserǁ_launch__mutmut_11': xǁWebbrowserǁ_launch__mutmut_11, 
        'xǁWebbrowserǁ_launch__mutmut_12': xǁWebbrowserǁ_launch__mutmut_12
    }
    
    def _launch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebbrowserǁ_launch__mutmut_orig"), object.__getattribute__(self, "xǁWebbrowserǁ_launch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _launch.__signature__ = _mutmut_signature(xǁWebbrowserǁ_launch__mutmut_orig)
    xǁWebbrowserǁ_launch__mutmut_orig.__name__ = 'xǁWebbrowserǁ_launch'

    @staticmethod
    @contextmanager
    def _create_temp_dir() -> Generator[str, None, None]:
        kwargs = {"ignore_cleanup_errors": True} if sys.version_info >= (3, 10) else {}
        with tempfile.TemporaryDirectory(**kwargs) as temp_file:  # type: ignore[call-overload]
            yield temp_file


class _WebbrowserLauncher:
    def xǁ_WebbrowserLauncherǁ__init____mutmut_orig(self, executable: str | Path, arguments: list[str], headless: bool, timeout: float):
        self.executable = executable
        self.arguments = arguments
        self.headless = headless
        self.timeout = timeout
        self._process_ended_early = False
    def xǁ_WebbrowserLauncherǁ__init____mutmut_1(self, executable: str | Path, arguments: list[str], headless: bool, timeout: float):
        self.executable = None
        self.arguments = arguments
        self.headless = headless
        self.timeout = timeout
        self._process_ended_early = False
    def xǁ_WebbrowserLauncherǁ__init____mutmut_2(self, executable: str | Path, arguments: list[str], headless: bool, timeout: float):
        self.executable = executable
        self.arguments = None
        self.headless = headless
        self.timeout = timeout
        self._process_ended_early = False
    def xǁ_WebbrowserLauncherǁ__init____mutmut_3(self, executable: str | Path, arguments: list[str], headless: bool, timeout: float):
        self.executable = executable
        self.arguments = arguments
        self.headless = None
        self.timeout = timeout
        self._process_ended_early = False
    def xǁ_WebbrowserLauncherǁ__init____mutmut_4(self, executable: str | Path, arguments: list[str], headless: bool, timeout: float):
        self.executable = executable
        self.arguments = arguments
        self.headless = headless
        self.timeout = None
        self._process_ended_early = False
    def xǁ_WebbrowserLauncherǁ__init____mutmut_5(self, executable: str | Path, arguments: list[str], headless: bool, timeout: float):
        self.executable = executable
        self.arguments = arguments
        self.headless = headless
        self.timeout = timeout
        self._process_ended_early = None
    def xǁ_WebbrowserLauncherǁ__init____mutmut_6(self, executable: str | Path, arguments: list[str], headless: bool, timeout: float):
        self.executable = executable
        self.arguments = arguments
        self.headless = headless
        self.timeout = timeout
        self._process_ended_early = True
    
    xǁ_WebbrowserLauncherǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁ_WebbrowserLauncherǁ__init____mutmut_1': xǁ_WebbrowserLauncherǁ__init____mutmut_1, 
        'xǁ_WebbrowserLauncherǁ__init____mutmut_2': xǁ_WebbrowserLauncherǁ__init____mutmut_2, 
        'xǁ_WebbrowserLauncherǁ__init____mutmut_3': xǁ_WebbrowserLauncherǁ__init____mutmut_3, 
        'xǁ_WebbrowserLauncherǁ__init____mutmut_4': xǁ_WebbrowserLauncherǁ__init____mutmut_4, 
        'xǁ_WebbrowserLauncherǁ__init____mutmut_5': xǁ_WebbrowserLauncherǁ__init____mutmut_5, 
        'xǁ_WebbrowserLauncherǁ__init____mutmut_6': xǁ_WebbrowserLauncherǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁ_WebbrowserLauncherǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁ_WebbrowserLauncherǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁ_WebbrowserLauncherǁ__init____mutmut_orig)
    xǁ_WebbrowserLauncherǁ__init____mutmut_orig.__name__ = 'xǁ_WebbrowserLauncherǁ__init__'

    @asynccontextmanager
    async def launch(self) -> AsyncGenerator[trio.Nursery, None]:
        try:
            headless = self.headless
            async with trio.open_nursery() as nursery:
                log.info(f"Launching web browser: {self.executable} ({headless=})")
                # the process is run in a separate task
                run_process = partial(
                    trio.run_process,
                    [self.executable, *self.arguments],
                    check=False,
                    stdout=DEVNULL,
                    stderr=DEVNULL,
                )
                # trio ensures that the process gets terminated when the task group gets cancelled
                process: trio.Process = await nursery.start(run_process)
                # the process watcher task cancels the entire task group when the user terminates/kills the process
                nursery.start_soon(self._task_process_watcher, process, nursery)
                try:
                    # the application logic is run here
                    with trio.move_on_after(self.timeout) as cancel_scope:
                        yield nursery
                    # check if the application logic has timed out
                    if cancel_scope.cancelled_caught:
                        log.warning("Web browser task group has timed out")
                finally:
                    # check if the task group hasn't been cancelled yet in the process watcher task
                    if not self._process_ended_early:
                        log.debug("Waiting for web browser process to terminate")
                    # once the application logic is done, cancel the entire task group and terminate/kill the process
                    nursery.cancel_scope.cancel()
        except BaseExceptionGroup as exc_grp:  # TODO: py310 support end: use except*
            exc: BaseException | BaseExceptionGroup | None = exc_grp.subgroup((KeyboardInterrupt, SystemExit))
            if not exc:  # not a KeyboardInterrupt or SystemExit
                raise
            while isinstance(exc, BaseExceptionGroup):  # get the first actual exception in the potentially nested groups
                exc = exc.exceptions[0]
            raise exc from exc.__context__

    async def xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_orig(self, process: trio.Process, nursery: trio.Nursery) -> None:
        """Task for cancelling the launch task group if the user closes the browser or if it exits early on its own"""
        await process.wait()
        # if the task group hasn't been cancelled yet, then the application logic was still running
        if not nursery.cancel_scope.cancel_called:  # pragma: no branch
            self._process_ended_early = True
            log.warning("Web browser process ended early")
            nursery.cancel_scope.cancel()

    async def xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_1(self, process: trio.Process, nursery: trio.Nursery) -> None:
        """Task for cancelling the launch task group if the user closes the browser or if it exits early on its own"""
        await process.wait()
        # if the task group hasn't been cancelled yet, then the application logic was still running
        if nursery.cancel_scope.cancel_called:  # pragma: no branch
            self._process_ended_early = True
            log.warning("Web browser process ended early")
            nursery.cancel_scope.cancel()

    async def xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_2(self, process: trio.Process, nursery: trio.Nursery) -> None:
        """Task for cancelling the launch task group if the user closes the browser or if it exits early on its own"""
        await process.wait()
        # if the task group hasn't been cancelled yet, then the application logic was still running
        if not nursery.cancel_scope.cancel_called:  # pragma: no branch
            self._process_ended_early = None
            log.warning("Web browser process ended early")
            nursery.cancel_scope.cancel()

    async def xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_3(self, process: trio.Process, nursery: trio.Nursery) -> None:
        """Task for cancelling the launch task group if the user closes the browser or if it exits early on its own"""
        await process.wait()
        # if the task group hasn't been cancelled yet, then the application logic was still running
        if not nursery.cancel_scope.cancel_called:  # pragma: no branch
            self._process_ended_early = False
            log.warning("Web browser process ended early")
            nursery.cancel_scope.cancel()

    async def xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_4(self, process: trio.Process, nursery: trio.Nursery) -> None:
        """Task for cancelling the launch task group if the user closes the browser or if it exits early on its own"""
        await process.wait()
        # if the task group hasn't been cancelled yet, then the application logic was still running
        if not nursery.cancel_scope.cancel_called:  # pragma: no branch
            self._process_ended_early = True
            log.warning(None)
            nursery.cancel_scope.cancel()

    async def xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_5(self, process: trio.Process, nursery: trio.Nursery) -> None:
        """Task for cancelling the launch task group if the user closes the browser or if it exits early on its own"""
        await process.wait()
        # if the task group hasn't been cancelled yet, then the application logic was still running
        if not nursery.cancel_scope.cancel_called:  # pragma: no branch
            self._process_ended_early = True
            log.warning("XXWeb browser process ended earlyXX")
            nursery.cancel_scope.cancel()

    async def xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_6(self, process: trio.Process, nursery: trio.Nursery) -> None:
        """Task for cancelling the launch task group if the user closes the browser or if it exits early on its own"""
        await process.wait()
        # if the task group hasn't been cancelled yet, then the application logic was still running
        if not nursery.cancel_scope.cancel_called:  # pragma: no branch
            self._process_ended_early = True
            log.warning("web browser process ended early")
            nursery.cancel_scope.cancel()

    async def xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_7(self, process: trio.Process, nursery: trio.Nursery) -> None:
        """Task for cancelling the launch task group if the user closes the browser or if it exits early on its own"""
        await process.wait()
        # if the task group hasn't been cancelled yet, then the application logic was still running
        if not nursery.cancel_scope.cancel_called:  # pragma: no branch
            self._process_ended_early = True
            log.warning("WEB BROWSER PROCESS ENDED EARLY")
            nursery.cancel_scope.cancel()
    
    xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_1': xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_1, 
        'xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_2': xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_2, 
        'xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_3': xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_3, 
        'xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_4': xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_4, 
        'xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_5': xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_5, 
        'xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_6': xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_6, 
        'xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_7': xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_7
    }
    
    def _task_process_watcher(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_orig"), object.__getattribute__(self, "xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _task_process_watcher.__signature__ = _mutmut_signature(xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_orig)
    xǁ_WebbrowserLauncherǁ_task_process_watcher__mutmut_orig.__name__ = 'xǁ_WebbrowserLauncherǁ_task_process_watcher'

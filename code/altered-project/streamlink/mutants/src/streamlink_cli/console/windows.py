from __future__ import annotations

import sys
from collections.abc import Sequence
from ctypes import CDLL, POINTER, Structure, byref
from ctypes.wintypes import (
    BOOL,
    DWORD,
    HANDLE,
    SHORT,
    SMALL_RECT,
    WCHAR,
    WORD,
)
from io import TextIOWrapper
from typing import Callable, ClassVar
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


# https://learn.microsoft.com/en-us/windows/console/coord-str
class COORD(Structure):
    _fields_: ClassVar = [
        ("X", SHORT),
        ("Y", SHORT),
    ]


# https://learn.microsoft.com/en-us/windows/console/console-screen-buffer-info-str
# noinspection PyPep8Naming
class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    _fields_: ClassVar = [
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", WORD),
        ("srWindow", SMALL_RECT),
        ("dwMaximumWindowSize", COORD),
    ]


class _WinApiCall:
    argtypes: ClassVar[Sequence]
    restype: ClassVar
    method: Callable

    def xǁ_WinApiCallǁ__init____mutmut_orig(self, dll: CDLL):
        self._dll = dll
        method = getattr(dll, self.__class__.__name__)
        method.argtypes = self.argtypes
        method.restype = self.restype
        self.method = method

    def xǁ_WinApiCallǁ__init____mutmut_1(self, dll: CDLL):
        self._dll = None
        method = getattr(dll, self.__class__.__name__)
        method.argtypes = self.argtypes
        method.restype = self.restype
        self.method = method

    def xǁ_WinApiCallǁ__init____mutmut_2(self, dll: CDLL):
        self._dll = dll
        method = None
        method.argtypes = self.argtypes
        method.restype = self.restype
        self.method = method

    def xǁ_WinApiCallǁ__init____mutmut_3(self, dll: CDLL):
        self._dll = dll
        method = getattr(None, self.__class__.__name__)
        method.argtypes = self.argtypes
        method.restype = self.restype
        self.method = method

    def xǁ_WinApiCallǁ__init____mutmut_4(self, dll: CDLL):
        self._dll = dll
        method = getattr(dll, None)
        method.argtypes = self.argtypes
        method.restype = self.restype
        self.method = method

    def xǁ_WinApiCallǁ__init____mutmut_5(self, dll: CDLL):
        self._dll = dll
        method = getattr(self.__class__.__name__)
        method.argtypes = self.argtypes
        method.restype = self.restype
        self.method = method

    def xǁ_WinApiCallǁ__init____mutmut_6(self, dll: CDLL):
        self._dll = dll
        method = getattr(dll, )
        method.argtypes = self.argtypes
        method.restype = self.restype
        self.method = method

    def xǁ_WinApiCallǁ__init____mutmut_7(self, dll: CDLL):
        self._dll = dll
        method = getattr(dll, self.__class__.__name__)
        method.argtypes = None
        method.restype = self.restype
        self.method = method

    def xǁ_WinApiCallǁ__init____mutmut_8(self, dll: CDLL):
        self._dll = dll
        method = getattr(dll, self.__class__.__name__)
        method.argtypes = self.argtypes
        method.restype = None
        self.method = method

    def xǁ_WinApiCallǁ__init____mutmut_9(self, dll: CDLL):
        self._dll = dll
        method = getattr(dll, self.__class__.__name__)
        method.argtypes = self.argtypes
        method.restype = self.restype
        self.method = None
    
    xǁ_WinApiCallǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁ_WinApiCallǁ__init____mutmut_1': xǁ_WinApiCallǁ__init____mutmut_1, 
        'xǁ_WinApiCallǁ__init____mutmut_2': xǁ_WinApiCallǁ__init____mutmut_2, 
        'xǁ_WinApiCallǁ__init____mutmut_3': xǁ_WinApiCallǁ__init____mutmut_3, 
        'xǁ_WinApiCallǁ__init____mutmut_4': xǁ_WinApiCallǁ__init____mutmut_4, 
        'xǁ_WinApiCallǁ__init____mutmut_5': xǁ_WinApiCallǁ__init____mutmut_5, 
        'xǁ_WinApiCallǁ__init____mutmut_6': xǁ_WinApiCallǁ__init____mutmut_6, 
        'xǁ_WinApiCallǁ__init____mutmut_7': xǁ_WinApiCallǁ__init____mutmut_7, 
        'xǁ_WinApiCallǁ__init____mutmut_8': xǁ_WinApiCallǁ__init____mutmut_8, 
        'xǁ_WinApiCallǁ__init____mutmut_9': xǁ_WinApiCallǁ__init____mutmut_9
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁ_WinApiCallǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁ_WinApiCallǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁ_WinApiCallǁ__init____mutmut_orig)
    xǁ_WinApiCallǁ__init____mutmut_orig.__name__ = 'xǁ_WinApiCallǁ__init__'

    def __call__(self, *args):  # pragma: no cover
        return self.method(*args)

    def xǁ_WinApiCallǁ_call_success__mutmut_orig(self, *args):
        if not self.method(*args):
            # https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror
            # https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes#system-error-codes
            last_error = self._dll.GetLastError()

            raise OSError(f"Error while calling kernel32.{self.__class__.__name__} ({last_error=:#x})")

    def xǁ_WinApiCallǁ_call_success__mutmut_1(self, *args):
        if self.method(*args):
            # https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror
            # https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes#system-error-codes
            last_error = self._dll.GetLastError()

            raise OSError(f"Error while calling kernel32.{self.__class__.__name__} ({last_error=:#x})")

    def xǁ_WinApiCallǁ_call_success__mutmut_2(self, *args):
        if not self.method(*args):
            # https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror
            # https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes#system-error-codes
            last_error = None

            raise OSError(f"Error while calling kernel32.{self.__class__.__name__} ({last_error=:#x})")

    def xǁ_WinApiCallǁ_call_success__mutmut_3(self, *args):
        if not self.method(*args):
            # https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror
            # https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes#system-error-codes
            last_error = self._dll.GetLastError()

            raise OSError(None)
    
    xǁ_WinApiCallǁ_call_success__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁ_WinApiCallǁ_call_success__mutmut_1': xǁ_WinApiCallǁ_call_success__mutmut_1, 
        'xǁ_WinApiCallǁ_call_success__mutmut_2': xǁ_WinApiCallǁ_call_success__mutmut_2, 
        'xǁ_WinApiCallǁ_call_success__mutmut_3': xǁ_WinApiCallǁ_call_success__mutmut_3
    }
    
    def _call_success(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁ_WinApiCallǁ_call_success__mutmut_orig"), object.__getattribute__(self, "xǁ_WinApiCallǁ_call_success__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _call_success.__signature__ = _mutmut_signature(xǁ_WinApiCallǁ_call_success__mutmut_orig)
    xǁ_WinApiCallǁ_call_success__mutmut_orig.__name__ = 'xǁ_WinApiCallǁ_call_success'


class GetStdHandle(_WinApiCall):
    """
    https://learn.microsoft.com/en-us/windows/console/getstdhandle
    """

    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12

    argtypes: ClassVar = [DWORD]
    restype: ClassVar = HANDLE

    def xǁGetStdHandleǁ__call____mutmut_orig(self, handle: TextIOWrapper | None) -> HANDLE:
        if handle is sys.stderr:
            std_handle = self.STD_ERROR_HANDLE
        else:
            std_handle = self.STD_OUTPUT_HANDLE

        return self.method(std_handle)

    def xǁGetStdHandleǁ__call____mutmut_1(self, handle: TextIOWrapper | None) -> HANDLE:
        if handle is not sys.stderr:
            std_handle = self.STD_ERROR_HANDLE
        else:
            std_handle = self.STD_OUTPUT_HANDLE

        return self.method(std_handle)

    def xǁGetStdHandleǁ__call____mutmut_2(self, handle: TextIOWrapper | None) -> HANDLE:
        if handle is sys.stderr:
            std_handle = None
        else:
            std_handle = self.STD_OUTPUT_HANDLE

        return self.method(std_handle)

    def xǁGetStdHandleǁ__call____mutmut_3(self, handle: TextIOWrapper | None) -> HANDLE:
        if handle is sys.stderr:
            std_handle = self.STD_ERROR_HANDLE
        else:
            std_handle = None

        return self.method(std_handle)

    def xǁGetStdHandleǁ__call____mutmut_4(self, handle: TextIOWrapper | None) -> HANDLE:
        if handle is sys.stderr:
            std_handle = self.STD_ERROR_HANDLE
        else:
            std_handle = self.STD_OUTPUT_HANDLE

        return self.method(None)
    
    xǁGetStdHandleǁ__call____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGetStdHandleǁ__call____mutmut_1': xǁGetStdHandleǁ__call____mutmut_1, 
        'xǁGetStdHandleǁ__call____mutmut_2': xǁGetStdHandleǁ__call____mutmut_2, 
        'xǁGetStdHandleǁ__call____mutmut_3': xǁGetStdHandleǁ__call____mutmut_3, 
        'xǁGetStdHandleǁ__call____mutmut_4': xǁGetStdHandleǁ__call____mutmut_4
    }
    
    def __call__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGetStdHandleǁ__call____mutmut_orig"), object.__getattribute__(self, "xǁGetStdHandleǁ__call____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __call__.__signature__ = _mutmut_signature(xǁGetStdHandleǁ__call____mutmut_orig)
    xǁGetStdHandleǁ__call____mutmut_orig.__name__ = 'xǁGetStdHandleǁ__call__'


class GetConsoleMode(_WinApiCall):
    """
    https://learn.microsoft.com/en-us/windows/console/getconsolemode
    """

    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 4

    argtypes: ClassVar = [HANDLE, POINTER(DWORD)]
    restype: ClassVar = BOOL

    def xǁGetConsoleModeǁ__call____mutmut_orig(self, console_output: HANDLE) -> int:
        mode = DWORD()
        self._call_success(console_output, mode)

        return mode.value

    def xǁGetConsoleModeǁ__call____mutmut_1(self, console_output: HANDLE) -> int:
        mode = None
        self._call_success(console_output, mode)

        return mode.value

    def xǁGetConsoleModeǁ__call____mutmut_2(self, console_output: HANDLE) -> int:
        mode = DWORD()
        self._call_success(None, mode)

        return mode.value

    def xǁGetConsoleModeǁ__call____mutmut_3(self, console_output: HANDLE) -> int:
        mode = DWORD()
        self._call_success(console_output, None)

        return mode.value

    def xǁGetConsoleModeǁ__call____mutmut_4(self, console_output: HANDLE) -> int:
        mode = DWORD()
        self._call_success(mode)

        return mode.value

    def xǁGetConsoleModeǁ__call____mutmut_5(self, console_output: HANDLE) -> int:
        mode = DWORD()
        self._call_success(console_output, )

        return mode.value
    
    xǁGetConsoleModeǁ__call____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGetConsoleModeǁ__call____mutmut_1': xǁGetConsoleModeǁ__call____mutmut_1, 
        'xǁGetConsoleModeǁ__call____mutmut_2': xǁGetConsoleModeǁ__call____mutmut_2, 
        'xǁGetConsoleModeǁ__call____mutmut_3': xǁGetConsoleModeǁ__call____mutmut_3, 
        'xǁGetConsoleModeǁ__call____mutmut_4': xǁGetConsoleModeǁ__call____mutmut_4, 
        'xǁGetConsoleModeǁ__call____mutmut_5': xǁGetConsoleModeǁ__call____mutmut_5
    }
    
    def __call__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGetConsoleModeǁ__call____mutmut_orig"), object.__getattribute__(self, "xǁGetConsoleModeǁ__call____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __call__.__signature__ = _mutmut_signature(xǁGetConsoleModeǁ__call____mutmut_orig)
    xǁGetConsoleModeǁ__call____mutmut_orig.__name__ = 'xǁGetConsoleModeǁ__call__'

    def xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_orig(self, console_output: HANDLE) -> bool:
        try:
            console_mode = self(console_output)
        except OSError:
            return False

        return console_mode & self.ENABLE_VIRTUAL_TERMINAL_PROCESSING > 0

    def xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_1(self, console_output: HANDLE) -> bool:
        try:
            console_mode = None
        except OSError:
            return False

        return console_mode & self.ENABLE_VIRTUAL_TERMINAL_PROCESSING > 0

    def xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_2(self, console_output: HANDLE) -> bool:
        try:
            console_mode = self(None)
        except OSError:
            return False

        return console_mode & self.ENABLE_VIRTUAL_TERMINAL_PROCESSING > 0

    def xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_3(self, console_output: HANDLE) -> bool:
        try:
            console_mode = self(console_output)
        except OSError:
            return True

        return console_mode & self.ENABLE_VIRTUAL_TERMINAL_PROCESSING > 0

    def xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_4(self, console_output: HANDLE) -> bool:
        try:
            console_mode = self(console_output)
        except OSError:
            return False

        return console_mode | self.ENABLE_VIRTUAL_TERMINAL_PROCESSING > 0

    def xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_5(self, console_output: HANDLE) -> bool:
        try:
            console_mode = self(console_output)
        except OSError:
            return False

        return console_mode & self.ENABLE_VIRTUAL_TERMINAL_PROCESSING >= 0

    def xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_6(self, console_output: HANDLE) -> bool:
        try:
            console_mode = self(console_output)
        except OSError:
            return False

        return console_mode & self.ENABLE_VIRTUAL_TERMINAL_PROCESSING > 1
    
    xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_1': xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_1, 
        'xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_2': xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_2, 
        'xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_3': xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_3, 
        'xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_4': xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_4, 
        'xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_5': xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_5, 
        'xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_6': xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_6
    }
    
    def supports_virtual_terminal_processing(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_orig"), object.__getattribute__(self, "xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_mutants"), args, kwargs, self)
        return result 
    
    supports_virtual_terminal_processing.__signature__ = _mutmut_signature(xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_orig)
    xǁGetConsoleModeǁsupports_virtual_terminal_processing__mutmut_orig.__name__ = 'xǁGetConsoleModeǁsupports_virtual_terminal_processing'


class GetConsoleScreenBufferInfo(_WinApiCall):
    """
    https://learn.microsoft.com/en-us/windows/console/getconsolescreenbufferinfo
    """

    argtypes: ClassVar = [HANDLE, POINTER(CONSOLE_SCREEN_BUFFER_INFO)]
    restype: ClassVar = BOOL

    def xǁGetConsoleScreenBufferInfoǁ__call____mutmut_orig(self, console_output: HANDLE) -> CONSOLE_SCREEN_BUFFER_INFO:
        console_screen_buffer_info = CONSOLE_SCREEN_BUFFER_INFO()
        self._call_success(console_output, byref(console_screen_buffer_info))

        return console_screen_buffer_info

    def xǁGetConsoleScreenBufferInfoǁ__call____mutmut_1(self, console_output: HANDLE) -> CONSOLE_SCREEN_BUFFER_INFO:
        console_screen_buffer_info = None
        self._call_success(console_output, byref(console_screen_buffer_info))

        return console_screen_buffer_info

    def xǁGetConsoleScreenBufferInfoǁ__call____mutmut_2(self, console_output: HANDLE) -> CONSOLE_SCREEN_BUFFER_INFO:
        console_screen_buffer_info = CONSOLE_SCREEN_BUFFER_INFO()
        self._call_success(None, byref(console_screen_buffer_info))

        return console_screen_buffer_info

    def xǁGetConsoleScreenBufferInfoǁ__call____mutmut_3(self, console_output: HANDLE) -> CONSOLE_SCREEN_BUFFER_INFO:
        console_screen_buffer_info = CONSOLE_SCREEN_BUFFER_INFO()
        self._call_success(console_output, None)

        return console_screen_buffer_info

    def xǁGetConsoleScreenBufferInfoǁ__call____mutmut_4(self, console_output: HANDLE) -> CONSOLE_SCREEN_BUFFER_INFO:
        console_screen_buffer_info = CONSOLE_SCREEN_BUFFER_INFO()
        self._call_success(byref(console_screen_buffer_info))

        return console_screen_buffer_info

    def xǁGetConsoleScreenBufferInfoǁ__call____mutmut_5(self, console_output: HANDLE) -> CONSOLE_SCREEN_BUFFER_INFO:
        console_screen_buffer_info = CONSOLE_SCREEN_BUFFER_INFO()
        self._call_success(console_output, )

        return console_screen_buffer_info

    def xǁGetConsoleScreenBufferInfoǁ__call____mutmut_6(self, console_output: HANDLE) -> CONSOLE_SCREEN_BUFFER_INFO:
        console_screen_buffer_info = CONSOLE_SCREEN_BUFFER_INFO()
        self._call_success(console_output, byref(None))

        return console_screen_buffer_info
    
    xǁGetConsoleScreenBufferInfoǁ__call____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁGetConsoleScreenBufferInfoǁ__call____mutmut_1': xǁGetConsoleScreenBufferInfoǁ__call____mutmut_1, 
        'xǁGetConsoleScreenBufferInfoǁ__call____mutmut_2': xǁGetConsoleScreenBufferInfoǁ__call____mutmut_2, 
        'xǁGetConsoleScreenBufferInfoǁ__call____mutmut_3': xǁGetConsoleScreenBufferInfoǁ__call____mutmut_3, 
        'xǁGetConsoleScreenBufferInfoǁ__call____mutmut_4': xǁGetConsoleScreenBufferInfoǁ__call____mutmut_4, 
        'xǁGetConsoleScreenBufferInfoǁ__call____mutmut_5': xǁGetConsoleScreenBufferInfoǁ__call____mutmut_5, 
        'xǁGetConsoleScreenBufferInfoǁ__call____mutmut_6': xǁGetConsoleScreenBufferInfoǁ__call____mutmut_6
    }
    
    def __call__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGetConsoleScreenBufferInfoǁ__call____mutmut_orig"), object.__getattribute__(self, "xǁGetConsoleScreenBufferInfoǁ__call____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __call__.__signature__ = _mutmut_signature(xǁGetConsoleScreenBufferInfoǁ__call____mutmut_orig)
    xǁGetConsoleScreenBufferInfoǁ__call____mutmut_orig.__name__ = 'xǁGetConsoleScreenBufferInfoǁ__call__'


class SetConsoleCursorPosition(_WinApiCall):
    """
    https://learn.microsoft.com/en-us/windows/console/setconsolecursorposition
    """

    argtypes: ClassVar = [HANDLE, COORD]
    restype: ClassVar = BOOL

    def xǁSetConsoleCursorPositionǁ__call____mutmut_orig(self, console_output: HANDLE, cursor_position: COORD) -> None:
        self._call_success(console_output, cursor_position)

    def xǁSetConsoleCursorPositionǁ__call____mutmut_1(self, console_output: HANDLE, cursor_position: COORD) -> None:
        self._call_success(None, cursor_position)

    def xǁSetConsoleCursorPositionǁ__call____mutmut_2(self, console_output: HANDLE, cursor_position: COORD) -> None:
        self._call_success(console_output, None)

    def xǁSetConsoleCursorPositionǁ__call____mutmut_3(self, console_output: HANDLE, cursor_position: COORD) -> None:
        self._call_success(cursor_position)

    def xǁSetConsoleCursorPositionǁ__call____mutmut_4(self, console_output: HANDLE, cursor_position: COORD) -> None:
        self._call_success(console_output, )
    
    xǁSetConsoleCursorPositionǁ__call____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetConsoleCursorPositionǁ__call____mutmut_1': xǁSetConsoleCursorPositionǁ__call____mutmut_1, 
        'xǁSetConsoleCursorPositionǁ__call____mutmut_2': xǁSetConsoleCursorPositionǁ__call____mutmut_2, 
        'xǁSetConsoleCursorPositionǁ__call____mutmut_3': xǁSetConsoleCursorPositionǁ__call____mutmut_3, 
        'xǁSetConsoleCursorPositionǁ__call____mutmut_4': xǁSetConsoleCursorPositionǁ__call____mutmut_4
    }
    
    def __call__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetConsoleCursorPositionǁ__call____mutmut_orig"), object.__getattribute__(self, "xǁSetConsoleCursorPositionǁ__call____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __call__.__signature__ = _mutmut_signature(xǁSetConsoleCursorPositionǁ__call____mutmut_orig)
    xǁSetConsoleCursorPositionǁ__call____mutmut_orig.__name__ = 'xǁSetConsoleCursorPositionǁ__call__'


class FillConsoleOutputAttribute(_WinApiCall):
    """
    https://learn.microsoft.com/en-us/windows/console/fillconsoleoutputattribute
    """

    argtypes: ClassVar = [HANDLE, WORD, DWORD, COORD, POINTER(DWORD)]
    restype: ClassVar = BOOL

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_orig(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, size, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_1(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = None
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, size, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_2(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(None)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, size, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_3(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = None
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, size, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_4(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(None)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, size, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_5(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = None
        self._call_success(console_output, attrs, size, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_6(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(None, attrs, size, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_7(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, None, size, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_8(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, None, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_9(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, size, None, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_10(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, size, write_coord, None)

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_11(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(attrs, size, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_12(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, size, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_13(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, write_coord, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_14(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, size, byref(number_of_attrs_written))

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_15(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, size, write_coord, )

        return number_of_attrs_written.value

    def xǁFillConsoleOutputAttributeǁ__call____mutmut_16(self, console_output: HANDLE, attribute: int, length: int, write_coord: COORD) -> int:
        attrs = WORD(attribute)
        size = DWORD(length)
        number_of_attrs_written = DWORD()
        self._call_success(console_output, attrs, size, write_coord, byref(None))

        return number_of_attrs_written.value
    
    xǁFillConsoleOutputAttributeǁ__call____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFillConsoleOutputAttributeǁ__call____mutmut_1': xǁFillConsoleOutputAttributeǁ__call____mutmut_1, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_2': xǁFillConsoleOutputAttributeǁ__call____mutmut_2, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_3': xǁFillConsoleOutputAttributeǁ__call____mutmut_3, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_4': xǁFillConsoleOutputAttributeǁ__call____mutmut_4, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_5': xǁFillConsoleOutputAttributeǁ__call____mutmut_5, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_6': xǁFillConsoleOutputAttributeǁ__call____mutmut_6, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_7': xǁFillConsoleOutputAttributeǁ__call____mutmut_7, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_8': xǁFillConsoleOutputAttributeǁ__call____mutmut_8, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_9': xǁFillConsoleOutputAttributeǁ__call____mutmut_9, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_10': xǁFillConsoleOutputAttributeǁ__call____mutmut_10, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_11': xǁFillConsoleOutputAttributeǁ__call____mutmut_11, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_12': xǁFillConsoleOutputAttributeǁ__call____mutmut_12, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_13': xǁFillConsoleOutputAttributeǁ__call____mutmut_13, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_14': xǁFillConsoleOutputAttributeǁ__call____mutmut_14, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_15': xǁFillConsoleOutputAttributeǁ__call____mutmut_15, 
        'xǁFillConsoleOutputAttributeǁ__call____mutmut_16': xǁFillConsoleOutputAttributeǁ__call____mutmut_16
    }
    
    def __call__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFillConsoleOutputAttributeǁ__call____mutmut_orig"), object.__getattribute__(self, "xǁFillConsoleOutputAttributeǁ__call____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __call__.__signature__ = _mutmut_signature(xǁFillConsoleOutputAttributeǁ__call____mutmut_orig)
    xǁFillConsoleOutputAttributeǁ__call____mutmut_orig.__name__ = 'xǁFillConsoleOutputAttributeǁ__call__'


class FillConsoleOutputCharacterW(_WinApiCall):
    """
    https://learn.microsoft.com/en-us/windows/console/fillconsoleoutputcharacter
    """

    argtypes: ClassVar = [HANDLE, WCHAR, DWORD, COORD, POINTER(DWORD)]
    restype: ClassVar = BOOL

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_orig(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, size, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_1(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = None
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, size, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_2(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(None)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, size, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_3(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = None
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, size, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_4(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(None)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, size, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_5(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = None
        self._call_success(console_output, char, size, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_6(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(None, char, size, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_7(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, None, size, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_8(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, None, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_9(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, size, None, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_10(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, size, write_coord, None)

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_11(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(char, size, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_12(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, size, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_13(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, write_coord, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_14(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, size, byref(number_of_chars_written))

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_15(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, size, write_coord, )

        return number_of_chars_written.value

    def xǁFillConsoleOutputCharacterWǁ__call____mutmut_16(self, console_output: HANDLE, character: str, length: int, write_coord: COORD) -> int:
        char = WCHAR(character)
        size = DWORD(length)
        number_of_chars_written = DWORD()
        self._call_success(console_output, char, size, write_coord, byref(None))

        return number_of_chars_written.value
    
    xǁFillConsoleOutputCharacterWǁ__call____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFillConsoleOutputCharacterWǁ__call____mutmut_1': xǁFillConsoleOutputCharacterWǁ__call____mutmut_1, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_2': xǁFillConsoleOutputCharacterWǁ__call____mutmut_2, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_3': xǁFillConsoleOutputCharacterWǁ__call____mutmut_3, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_4': xǁFillConsoleOutputCharacterWǁ__call____mutmut_4, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_5': xǁFillConsoleOutputCharacterWǁ__call____mutmut_5, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_6': xǁFillConsoleOutputCharacterWǁ__call____mutmut_6, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_7': xǁFillConsoleOutputCharacterWǁ__call____mutmut_7, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_8': xǁFillConsoleOutputCharacterWǁ__call____mutmut_8, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_9': xǁFillConsoleOutputCharacterWǁ__call____mutmut_9, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_10': xǁFillConsoleOutputCharacterWǁ__call____mutmut_10, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_11': xǁFillConsoleOutputCharacterWǁ__call____mutmut_11, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_12': xǁFillConsoleOutputCharacterWǁ__call____mutmut_12, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_13': xǁFillConsoleOutputCharacterWǁ__call____mutmut_13, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_14': xǁFillConsoleOutputCharacterWǁ__call____mutmut_14, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_15': xǁFillConsoleOutputCharacterWǁ__call____mutmut_15, 
        'xǁFillConsoleOutputCharacterWǁ__call____mutmut_16': xǁFillConsoleOutputCharacterWǁ__call____mutmut_16
    }
    
    def __call__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFillConsoleOutputCharacterWǁ__call____mutmut_orig"), object.__getattribute__(self, "xǁFillConsoleOutputCharacterWǁ__call____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __call__.__signature__ = _mutmut_signature(xǁFillConsoleOutputCharacterWǁ__call____mutmut_orig)
    xǁFillConsoleOutputCharacterWǁ__call____mutmut_orig.__name__ = 'xǁFillConsoleOutputCharacterWǁ__call__'


class WindowsConsole:
    def __new__(cls, *args, **kwargs):
        try:
            from ctypes import windll  # noqa: PLC0415
        except ImportError:  # pragma: no cover
            return None

        kernel32 = windll.kernel32
        cls.get_std_handle = GetStdHandle(kernel32)
        cls.get_console_mode = GetConsoleMode(kernel32)
        cls.get_console_screen_buffer_info = GetConsoleScreenBufferInfo(kernel32)
        cls.set_console_cursor_position = SetConsoleCursorPosition(kernel32)
        cls.fill_console_output_attribute = FillConsoleOutputAttribute(kernel32)
        cls.fill_console_output_character_w = FillConsoleOutputCharacterW(kernel32)

        return super().__new__(cls)

    def xǁWindowsConsoleǁ__init____mutmut_orig(self, handle: TextIOWrapper | None = None):
        self.handle = self.get_std_handle(handle)

    def xǁWindowsConsoleǁ__init____mutmut_1(self, handle: TextIOWrapper | None = None):
        self.handle = None

    def xǁWindowsConsoleǁ__init____mutmut_2(self, handle: TextIOWrapper | None = None):
        self.handle = self.get_std_handle(None)
    
    xǁWindowsConsoleǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWindowsConsoleǁ__init____mutmut_1': xǁWindowsConsoleǁ__init____mutmut_1, 
        'xǁWindowsConsoleǁ__init____mutmut_2': xǁWindowsConsoleǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWindowsConsoleǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWindowsConsoleǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWindowsConsoleǁ__init____mutmut_orig)
    xǁWindowsConsoleǁ__init____mutmut_orig.__name__ = 'xǁWindowsConsoleǁ__init__'

    def xǁWindowsConsoleǁsupports_virtual_terminal_processing__mutmut_orig(self):
        return self.get_console_mode.supports_virtual_terminal_processing(self.handle)

    def xǁWindowsConsoleǁsupports_virtual_terminal_processing__mutmut_1(self):
        return self.get_console_mode.supports_virtual_terminal_processing(None)
    
    xǁWindowsConsoleǁsupports_virtual_terminal_processing__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWindowsConsoleǁsupports_virtual_terminal_processing__mutmut_1': xǁWindowsConsoleǁsupports_virtual_terminal_processing__mutmut_1
    }
    
    def supports_virtual_terminal_processing(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWindowsConsoleǁsupports_virtual_terminal_processing__mutmut_orig"), object.__getattribute__(self, "xǁWindowsConsoleǁsupports_virtual_terminal_processing__mutmut_mutants"), args, kwargs, self)
        return result 
    
    supports_virtual_terminal_processing.__signature__ = _mutmut_signature(xǁWindowsConsoleǁsupports_virtual_terminal_processing__mutmut_orig)
    xǁWindowsConsoleǁsupports_virtual_terminal_processing__mutmut_orig.__name__ = 'xǁWindowsConsoleǁsupports_virtual_terminal_processing'

    def xǁWindowsConsoleǁclear_line__mutmut_orig(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_1(self):
        info = None

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_2(self):
        info = self.get_console_screen_buffer_info(None)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_3(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = None
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_4(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = None
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_5(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = None
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_6(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=None, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_7(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=None)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_8(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_9(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, )
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_10(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=1, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_11(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(None, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_12(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, None, length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_13(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", None, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_14(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, None)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_15(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(" ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_16(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_17(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_18(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, )
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_19(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, "XX XX", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_20(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(None, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_21(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, None, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_22(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, None, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_23(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, None)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_24(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_25(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, length, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_26(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, cursor_position)
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_27(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, )
        self.set_console_cursor_position(self.handle, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_28(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(None, cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_29(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, None)

    def xǁWindowsConsoleǁclear_line__mutmut_30(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(cursor_position)

    def xǁWindowsConsoleǁclear_line__mutmut_31(self):
        info = self.get_console_screen_buffer_info(self.handle)

        def_attrs = info.wAttributes
        length = info.dwSize.X
        cursor_position = COORD(X=0, Y=info.dwCursorPosition.Y)
        self.fill_console_output_character_w(self.handle, " ", length, cursor_position)
        self.fill_console_output_attribute(self.handle, def_attrs, length, cursor_position)
        self.set_console_cursor_position(self.handle, )
    
    xǁWindowsConsoleǁclear_line__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWindowsConsoleǁclear_line__mutmut_1': xǁWindowsConsoleǁclear_line__mutmut_1, 
        'xǁWindowsConsoleǁclear_line__mutmut_2': xǁWindowsConsoleǁclear_line__mutmut_2, 
        'xǁWindowsConsoleǁclear_line__mutmut_3': xǁWindowsConsoleǁclear_line__mutmut_3, 
        'xǁWindowsConsoleǁclear_line__mutmut_4': xǁWindowsConsoleǁclear_line__mutmut_4, 
        'xǁWindowsConsoleǁclear_line__mutmut_5': xǁWindowsConsoleǁclear_line__mutmut_5, 
        'xǁWindowsConsoleǁclear_line__mutmut_6': xǁWindowsConsoleǁclear_line__mutmut_6, 
        'xǁWindowsConsoleǁclear_line__mutmut_7': xǁWindowsConsoleǁclear_line__mutmut_7, 
        'xǁWindowsConsoleǁclear_line__mutmut_8': xǁWindowsConsoleǁclear_line__mutmut_8, 
        'xǁWindowsConsoleǁclear_line__mutmut_9': xǁWindowsConsoleǁclear_line__mutmut_9, 
        'xǁWindowsConsoleǁclear_line__mutmut_10': xǁWindowsConsoleǁclear_line__mutmut_10, 
        'xǁWindowsConsoleǁclear_line__mutmut_11': xǁWindowsConsoleǁclear_line__mutmut_11, 
        'xǁWindowsConsoleǁclear_line__mutmut_12': xǁWindowsConsoleǁclear_line__mutmut_12, 
        'xǁWindowsConsoleǁclear_line__mutmut_13': xǁWindowsConsoleǁclear_line__mutmut_13, 
        'xǁWindowsConsoleǁclear_line__mutmut_14': xǁWindowsConsoleǁclear_line__mutmut_14, 
        'xǁWindowsConsoleǁclear_line__mutmut_15': xǁWindowsConsoleǁclear_line__mutmut_15, 
        'xǁWindowsConsoleǁclear_line__mutmut_16': xǁWindowsConsoleǁclear_line__mutmut_16, 
        'xǁWindowsConsoleǁclear_line__mutmut_17': xǁWindowsConsoleǁclear_line__mutmut_17, 
        'xǁWindowsConsoleǁclear_line__mutmut_18': xǁWindowsConsoleǁclear_line__mutmut_18, 
        'xǁWindowsConsoleǁclear_line__mutmut_19': xǁWindowsConsoleǁclear_line__mutmut_19, 
        'xǁWindowsConsoleǁclear_line__mutmut_20': xǁWindowsConsoleǁclear_line__mutmut_20, 
        'xǁWindowsConsoleǁclear_line__mutmut_21': xǁWindowsConsoleǁclear_line__mutmut_21, 
        'xǁWindowsConsoleǁclear_line__mutmut_22': xǁWindowsConsoleǁclear_line__mutmut_22, 
        'xǁWindowsConsoleǁclear_line__mutmut_23': xǁWindowsConsoleǁclear_line__mutmut_23, 
        'xǁWindowsConsoleǁclear_line__mutmut_24': xǁWindowsConsoleǁclear_line__mutmut_24, 
        'xǁWindowsConsoleǁclear_line__mutmut_25': xǁWindowsConsoleǁclear_line__mutmut_25, 
        'xǁWindowsConsoleǁclear_line__mutmut_26': xǁWindowsConsoleǁclear_line__mutmut_26, 
        'xǁWindowsConsoleǁclear_line__mutmut_27': xǁWindowsConsoleǁclear_line__mutmut_27, 
        'xǁWindowsConsoleǁclear_line__mutmut_28': xǁWindowsConsoleǁclear_line__mutmut_28, 
        'xǁWindowsConsoleǁclear_line__mutmut_29': xǁWindowsConsoleǁclear_line__mutmut_29, 
        'xǁWindowsConsoleǁclear_line__mutmut_30': xǁWindowsConsoleǁclear_line__mutmut_30, 
        'xǁWindowsConsoleǁclear_line__mutmut_31': xǁWindowsConsoleǁclear_line__mutmut_31
    }
    
    def clear_line(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWindowsConsoleǁclear_line__mutmut_orig"), object.__getattribute__(self, "xǁWindowsConsoleǁclear_line__mutmut_mutants"), args, kwargs, self)
        return result 
    
    clear_line.__signature__ = _mutmut_signature(xǁWindowsConsoleǁclear_line__mutmut_orig)
    xǁWindowsConsoleǁclear_line__mutmut_orig.__name__ = 'xǁWindowsConsoleǁclear_line'

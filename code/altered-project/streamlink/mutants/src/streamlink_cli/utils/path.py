from __future__ import annotations

import re
from collections.abc import Callable
from pathlib import Path

from streamlink.compat import is_win32


REPLACEMENT = "_"
SPECIAL_PATH_PARTS = (".", "..")

_UNPRINTABLE = "".join(chr(c) for c in range(32))
_UNSUPPORTED_POSIX = "/"
_UNSUPPORTED_WIN32 = '\x7f"*/:<>?\\|'

RE_CHARS_POSIX = re.compile(f"[{re.escape(_UNPRINTABLE + _UNSUPPORTED_POSIX)}]+")
RE_CHARS_WIN32 = re.compile(f"[{re.escape(_UNPRINTABLE + _UNSUPPORTED_WIN32)}]+")
if is_win32:
    RE_CHARS = RE_CHARS_WIN32
else:
    RE_CHARS = RE_CHARS_POSIX
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


def x_replace_chars__mutmut_orig(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_1(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is not None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_2(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = None
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_3(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = None
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_4(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.upper()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_5(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap not in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_6(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("XXposixXX", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_7(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("POSIX", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_8(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("Posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_9(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "XXunixXX"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_10(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "UNIX"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_11(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "Unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_12(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = None
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_13(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap not in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_14(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("XXwindowsXX", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_15(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("WINDOWS", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_16(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("Windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_17(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "XXwin32XX"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_18(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "WIN32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_19(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "Win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_20(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = None
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_21(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError(None)

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_22(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("XXInvalid charmapXX")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_23(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("invalid charmap")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_24(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("INVALID CHARMAP")

    return pattern.sub(replacement, path)


def x_replace_chars__mutmut_25(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(None, path)


def x_replace_chars__mutmut_26(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, None)


def x_replace_chars__mutmut_27(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(path)


def x_replace_chars__mutmut_28(path: str, charmap: str | None = None, replacement: str = REPLACEMENT) -> str:
    if charmap is None:
        pattern = RE_CHARS
    else:
        charmap = charmap.lower()
        if charmap in ("posix", "unix"):
            pattern = RE_CHARS_POSIX
        elif charmap in ("windows", "win32"):
            pattern = RE_CHARS_WIN32
        else:
            raise ValueError("Invalid charmap")

    return pattern.sub(replacement, )

x_replace_chars__mutmut_mutants : ClassVar[MutantDict] = {
'x_replace_chars__mutmut_1': x_replace_chars__mutmut_1, 
    'x_replace_chars__mutmut_2': x_replace_chars__mutmut_2, 
    'x_replace_chars__mutmut_3': x_replace_chars__mutmut_3, 
    'x_replace_chars__mutmut_4': x_replace_chars__mutmut_4, 
    'x_replace_chars__mutmut_5': x_replace_chars__mutmut_5, 
    'x_replace_chars__mutmut_6': x_replace_chars__mutmut_6, 
    'x_replace_chars__mutmut_7': x_replace_chars__mutmut_7, 
    'x_replace_chars__mutmut_8': x_replace_chars__mutmut_8, 
    'x_replace_chars__mutmut_9': x_replace_chars__mutmut_9, 
    'x_replace_chars__mutmut_10': x_replace_chars__mutmut_10, 
    'x_replace_chars__mutmut_11': x_replace_chars__mutmut_11, 
    'x_replace_chars__mutmut_12': x_replace_chars__mutmut_12, 
    'x_replace_chars__mutmut_13': x_replace_chars__mutmut_13, 
    'x_replace_chars__mutmut_14': x_replace_chars__mutmut_14, 
    'x_replace_chars__mutmut_15': x_replace_chars__mutmut_15, 
    'x_replace_chars__mutmut_16': x_replace_chars__mutmut_16, 
    'x_replace_chars__mutmut_17': x_replace_chars__mutmut_17, 
    'x_replace_chars__mutmut_18': x_replace_chars__mutmut_18, 
    'x_replace_chars__mutmut_19': x_replace_chars__mutmut_19, 
    'x_replace_chars__mutmut_20': x_replace_chars__mutmut_20, 
    'x_replace_chars__mutmut_21': x_replace_chars__mutmut_21, 
    'x_replace_chars__mutmut_22': x_replace_chars__mutmut_22, 
    'x_replace_chars__mutmut_23': x_replace_chars__mutmut_23, 
    'x_replace_chars__mutmut_24': x_replace_chars__mutmut_24, 
    'x_replace_chars__mutmut_25': x_replace_chars__mutmut_25, 
    'x_replace_chars__mutmut_26': x_replace_chars__mutmut_26, 
    'x_replace_chars__mutmut_27': x_replace_chars__mutmut_27, 
    'x_replace_chars__mutmut_28': x_replace_chars__mutmut_28
}

def replace_chars(*args, **kwargs):
    result = _mutmut_trampoline(x_replace_chars__mutmut_orig, x_replace_chars__mutmut_mutants, args, kwargs)
    return result 

replace_chars.__signature__ = _mutmut_signature(x_replace_chars__mutmut_orig)
x_replace_chars__mutmut_orig.__name__ = 'x_replace_chars'


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_orig(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_1(path: str, length: int = 256, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_2(path: str, length: int = 255, keep_extension: bool = False) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_3(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = None

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_4(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(None, 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_5(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", None)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_6(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_7(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", )

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_8(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.split(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_9(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit("XX.XX", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_10(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 2)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_11(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_12(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension and len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_13(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) != 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_14(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 2 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_15(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 and len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_16(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) >= 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_17(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 11:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_18(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = None
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_19(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode(None)
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_20(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("XXutf-8XX")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_21(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("UTF-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_22(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("Utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_23(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = None
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_24(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = None
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_25(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode(None, errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_26(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors=None)
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_27(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode(errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_28(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", )
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_29(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("XXutf-8XX", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_30(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("UTF-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_31(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("Utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_32(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="XXignoreXX")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_33(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="IGNORE")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_34(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="Ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_35(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = None
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_36(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode(None)
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_37(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[1].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_38(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("XXutf-8XX")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_39(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("UTF-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_40(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("Utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_41(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = None
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_42(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length + len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_43(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) + 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_44(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 2]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_45(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = None
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_46(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode(None, errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_47(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors=None)
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_48(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode(errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_49(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", )
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_50(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("XXutf-8XX", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_51(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("UTF-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_52(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("Utf-8", errors="ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_53(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="XXignoreXX")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_54(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="IGNORE")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_55(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="Ignore")
    return f"{decoded}.{parts[1]}"


# This method does not take care of unicode modifier characters when truncating
def x_truncate_path__mutmut_56(path: str, length: int = 255, keep_extension: bool = True) -> str:
    parts = path.rsplit(".", 1)

    # no file name extension (no dot separator in path or file name extension too long):
    # truncate the whole thing
    if not keep_extension or len(parts) == 1 or len(parts[1]) > 10:
        encoded = path.encode("utf-8")
        truncated = encoded[:length]
        decoded = truncated.decode("utf-8", errors="ignore")
        return decoded

    # truncate file name, but keep file name extension
    encoded = parts[0].encode("utf-8")
    truncated = encoded[: length - len(parts[1]) - 1]
    decoded = truncated.decode("utf-8", errors="ignore")
    return f"{decoded}.{parts[2]}"

x_truncate_path__mutmut_mutants : ClassVar[MutantDict] = {
'x_truncate_path__mutmut_1': x_truncate_path__mutmut_1, 
    'x_truncate_path__mutmut_2': x_truncate_path__mutmut_2, 
    'x_truncate_path__mutmut_3': x_truncate_path__mutmut_3, 
    'x_truncate_path__mutmut_4': x_truncate_path__mutmut_4, 
    'x_truncate_path__mutmut_5': x_truncate_path__mutmut_5, 
    'x_truncate_path__mutmut_6': x_truncate_path__mutmut_6, 
    'x_truncate_path__mutmut_7': x_truncate_path__mutmut_7, 
    'x_truncate_path__mutmut_8': x_truncate_path__mutmut_8, 
    'x_truncate_path__mutmut_9': x_truncate_path__mutmut_9, 
    'x_truncate_path__mutmut_10': x_truncate_path__mutmut_10, 
    'x_truncate_path__mutmut_11': x_truncate_path__mutmut_11, 
    'x_truncate_path__mutmut_12': x_truncate_path__mutmut_12, 
    'x_truncate_path__mutmut_13': x_truncate_path__mutmut_13, 
    'x_truncate_path__mutmut_14': x_truncate_path__mutmut_14, 
    'x_truncate_path__mutmut_15': x_truncate_path__mutmut_15, 
    'x_truncate_path__mutmut_16': x_truncate_path__mutmut_16, 
    'x_truncate_path__mutmut_17': x_truncate_path__mutmut_17, 
    'x_truncate_path__mutmut_18': x_truncate_path__mutmut_18, 
    'x_truncate_path__mutmut_19': x_truncate_path__mutmut_19, 
    'x_truncate_path__mutmut_20': x_truncate_path__mutmut_20, 
    'x_truncate_path__mutmut_21': x_truncate_path__mutmut_21, 
    'x_truncate_path__mutmut_22': x_truncate_path__mutmut_22, 
    'x_truncate_path__mutmut_23': x_truncate_path__mutmut_23, 
    'x_truncate_path__mutmut_24': x_truncate_path__mutmut_24, 
    'x_truncate_path__mutmut_25': x_truncate_path__mutmut_25, 
    'x_truncate_path__mutmut_26': x_truncate_path__mutmut_26, 
    'x_truncate_path__mutmut_27': x_truncate_path__mutmut_27, 
    'x_truncate_path__mutmut_28': x_truncate_path__mutmut_28, 
    'x_truncate_path__mutmut_29': x_truncate_path__mutmut_29, 
    'x_truncate_path__mutmut_30': x_truncate_path__mutmut_30, 
    'x_truncate_path__mutmut_31': x_truncate_path__mutmut_31, 
    'x_truncate_path__mutmut_32': x_truncate_path__mutmut_32, 
    'x_truncate_path__mutmut_33': x_truncate_path__mutmut_33, 
    'x_truncate_path__mutmut_34': x_truncate_path__mutmut_34, 
    'x_truncate_path__mutmut_35': x_truncate_path__mutmut_35, 
    'x_truncate_path__mutmut_36': x_truncate_path__mutmut_36, 
    'x_truncate_path__mutmut_37': x_truncate_path__mutmut_37, 
    'x_truncate_path__mutmut_38': x_truncate_path__mutmut_38, 
    'x_truncate_path__mutmut_39': x_truncate_path__mutmut_39, 
    'x_truncate_path__mutmut_40': x_truncate_path__mutmut_40, 
    'x_truncate_path__mutmut_41': x_truncate_path__mutmut_41, 
    'x_truncate_path__mutmut_42': x_truncate_path__mutmut_42, 
    'x_truncate_path__mutmut_43': x_truncate_path__mutmut_43, 
    'x_truncate_path__mutmut_44': x_truncate_path__mutmut_44, 
    'x_truncate_path__mutmut_45': x_truncate_path__mutmut_45, 
    'x_truncate_path__mutmut_46': x_truncate_path__mutmut_46, 
    'x_truncate_path__mutmut_47': x_truncate_path__mutmut_47, 
    'x_truncate_path__mutmut_48': x_truncate_path__mutmut_48, 
    'x_truncate_path__mutmut_49': x_truncate_path__mutmut_49, 
    'x_truncate_path__mutmut_50': x_truncate_path__mutmut_50, 
    'x_truncate_path__mutmut_51': x_truncate_path__mutmut_51, 
    'x_truncate_path__mutmut_52': x_truncate_path__mutmut_52, 
    'x_truncate_path__mutmut_53': x_truncate_path__mutmut_53, 
    'x_truncate_path__mutmut_54': x_truncate_path__mutmut_54, 
    'x_truncate_path__mutmut_55': x_truncate_path__mutmut_55, 
    'x_truncate_path__mutmut_56': x_truncate_path__mutmut_56
}

def truncate_path(*args, **kwargs):
    result = _mutmut_trampoline(x_truncate_path__mutmut_orig, x_truncate_path__mutmut_mutants, args, kwargs)
    return result 

truncate_path.__signature__ = _mutmut_signature(x_truncate_path__mutmut_orig)
x_truncate_path__mutmut_orig.__name__ = 'x_truncate_path'


def x_replace_path__mutmut_orig(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_1(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = None
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_2(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(None, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_3(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, None)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_4(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_5(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, )
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_6(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part == newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_7(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart or newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_8(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart not in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_9(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = None
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_10(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(None).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_11(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = None

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_12(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) + 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_13(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 2

    return Path(*(get_part(part, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_14(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(None, i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_15(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, None) for i, part in enumerate(parts)))


def x_replace_path__mutmut_16(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(i == last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_17(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, ) for i, part in enumerate(parts)))


def x_replace_path__mutmut_18(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i != last) for i, part in enumerate(parts)))


def x_replace_path__mutmut_19(pathlike: str | Path, mapper: Callable[[str, bool], str]) -> Path:
    def get_part(part: str, isfile: bool) -> str:
        newpart = mapper(part, isfile)
        return REPLACEMENT if part != newpart and newpart in SPECIAL_PATH_PARTS else newpart

    parts = Path(pathlike).expanduser().parts
    last = len(parts) - 1

    return Path(*(get_part(part, i == last) for i, part in enumerate(None)))

x_replace_path__mutmut_mutants : ClassVar[MutantDict] = {
'x_replace_path__mutmut_1': x_replace_path__mutmut_1, 
    'x_replace_path__mutmut_2': x_replace_path__mutmut_2, 
    'x_replace_path__mutmut_3': x_replace_path__mutmut_3, 
    'x_replace_path__mutmut_4': x_replace_path__mutmut_4, 
    'x_replace_path__mutmut_5': x_replace_path__mutmut_5, 
    'x_replace_path__mutmut_6': x_replace_path__mutmut_6, 
    'x_replace_path__mutmut_7': x_replace_path__mutmut_7, 
    'x_replace_path__mutmut_8': x_replace_path__mutmut_8, 
    'x_replace_path__mutmut_9': x_replace_path__mutmut_9, 
    'x_replace_path__mutmut_10': x_replace_path__mutmut_10, 
    'x_replace_path__mutmut_11': x_replace_path__mutmut_11, 
    'x_replace_path__mutmut_12': x_replace_path__mutmut_12, 
    'x_replace_path__mutmut_13': x_replace_path__mutmut_13, 
    'x_replace_path__mutmut_14': x_replace_path__mutmut_14, 
    'x_replace_path__mutmut_15': x_replace_path__mutmut_15, 
    'x_replace_path__mutmut_16': x_replace_path__mutmut_16, 
    'x_replace_path__mutmut_17': x_replace_path__mutmut_17, 
    'x_replace_path__mutmut_18': x_replace_path__mutmut_18, 
    'x_replace_path__mutmut_19': x_replace_path__mutmut_19
}

def replace_path(*args, **kwargs):
    result = _mutmut_trampoline(x_replace_path__mutmut_orig, x_replace_path__mutmut_mutants, args, kwargs)
    return result 

replace_path.__signature__ = _mutmut_signature(x_replace_path__mutmut_orig)
x_replace_path__mutmut_orig.__name__ = 'x_replace_path'

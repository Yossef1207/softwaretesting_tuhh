from __future__ import annotations

import os
import tempfile
from pathlib import Path

from streamlink.compat import is_darwin, is_win32


DEFAULT_STREAM_METADATA = {
    "id": "Unknown ID",
    "title": "Unknown Title",
    "author": "Unknown Author",
    "category": "No Category",
    "game": "No Game/Category",
}

PROGRESS_INTERVAL_NO_STATUS = 2

CONFIG_FILES: list[Path]
PLUGIN_DIRS: list[Path]
LOG_DIR: Path

if is_win32:
    APPDATA = Path(os.environ.get("APPDATA") or Path.home() / "AppData")
    CONFIG_FILES = [
        APPDATA / "streamlink" / "config",
    ]
    PLUGIN_DIRS = [
        APPDATA / "streamlink" / "plugins",
    ]
    LOG_DIR = Path(tempfile.gettempdir()) / "streamlink" / "logs"
elif is_darwin:
    XDG_CONFIG_HOME = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config")).expanduser()
    CONFIG_FILES = [
        Path.home() / "Library" / "Application Support" / "streamlink" / "config",
    ]
    PLUGIN_DIRS = [
        Path.home() / "Library" / "Application Support" / "streamlink" / "plugins",
    ]
    LOG_DIR = Path.home() / "Library" / "Logs" / "streamlink"
else:
    XDG_CONFIG_HOME = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config")).expanduser()
    XDG_DATA_HOME = Path(os.environ.get("XDG_DATA_HOME", "~/.local/share")).expanduser()
    XDG_STATE_HOME = Path(os.environ.get("XDG_STATE_HOME", "~/.local/state")).expanduser()
    CONFIG_FILES = [
        XDG_CONFIG_HOME / "streamlink" / "config",
    ]
    PLUGIN_DIRS = [
        XDG_DATA_HOME / "streamlink" / "plugins",
    ]
    LOG_DIR = XDG_STATE_HOME / "streamlink" / "logs"

STREAM_SYNONYMS = ["best", "worst", "best-unfiltered", "worst-unfiltered"]
STREAM_PASSTHROUGH = ["hls", "http"]


__all__ = [
    "CONFIG_FILES",
    "DEFAULT_STREAM_METADATA",
    "LOG_DIR",
    "PLUGIN_DIRS",
    "PROGRESS_INTERVAL_NO_STATUS",
    "STREAM_PASSTHROUGH",
    "STREAM_SYNONYMS",
]
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

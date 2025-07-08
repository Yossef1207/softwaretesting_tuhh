from __future__ import annotations

from collections.abc import Iterable
from os import environ
from pathlib import Path
from shutil import which

from streamlink.compat import is_darwin, is_win32
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


def x__resolve_executable__mutmut_orig(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_1(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = None
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_2(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(None)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_3(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(None).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_4(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = None
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_5(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = None
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_6(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(None)
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_7(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path * exe)
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_8(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath not in checked:
                continue
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_9(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath in checked:
                break
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_10(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath in checked:
                continue
            checked.add(None)
            resolved = which(fullpath)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_11(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = None
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_12(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = which(None)
            if resolved:
                return Path(resolved).resolve()

    return None


def x__resolve_executable__mutmut_13(paths: Iterable[Path], *exes: str) -> Path | None:
    for exe in exes:
        resolved = which(exe)
        if resolved:
            return Path(resolved).resolve()

    checked = set()
    for path in paths:
        for exe in exes:
            fullpath = str(path / exe)
            if fullpath in checked:
                continue
            checked.add(fullpath)
            resolved = which(fullpath)
            if resolved:
                return Path(None).resolve()

    return None

x__resolve_executable__mutmut_mutants : ClassVar[MutantDict] = {
'x__resolve_executable__mutmut_1': x__resolve_executable__mutmut_1, 
    'x__resolve_executable__mutmut_2': x__resolve_executable__mutmut_2, 
    'x__resolve_executable__mutmut_3': x__resolve_executable__mutmut_3, 
    'x__resolve_executable__mutmut_4': x__resolve_executable__mutmut_4, 
    'x__resolve_executable__mutmut_5': x__resolve_executable__mutmut_5, 
    'x__resolve_executable__mutmut_6': x__resolve_executable__mutmut_6, 
    'x__resolve_executable__mutmut_7': x__resolve_executable__mutmut_7, 
    'x__resolve_executable__mutmut_8': x__resolve_executable__mutmut_8, 
    'x__resolve_executable__mutmut_9': x__resolve_executable__mutmut_9, 
    'x__resolve_executable__mutmut_10': x__resolve_executable__mutmut_10, 
    'x__resolve_executable__mutmut_11': x__resolve_executable__mutmut_11, 
    'x__resolve_executable__mutmut_12': x__resolve_executable__mutmut_12, 
    'x__resolve_executable__mutmut_13': x__resolve_executable__mutmut_13
}

def _resolve_executable(*args, **kwargs):
    result = _mutmut_trampoline(x__resolve_executable__mutmut_orig, x__resolve_executable__mutmut_mutants, args, kwargs)
    return result 

_resolve_executable.__signature__ = _mutmut_signature(x__resolve_executable__mutmut_orig)
x__resolve_executable__mutmut_orig.__name__ = 'x__resolve_executable'


def x__find_default_player_win32__mutmut_orig() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_1() -> Path | None:
    envvars = None
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_2() -> Path | None:
    envvars = "XXPROGRAMFILESXX", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_3() -> Path | None:
    envvars = "programfiles", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_4() -> Path | None:
    envvars = "Programfiles", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_5() -> Path | None:
    envvars = "PROGRAMFILES", "XXPROGRAMFILES(X86)XX", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_6() -> Path | None:
    envvars = "PROGRAMFILES", "programfiles(x86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_7() -> Path | None:
    envvars = "PROGRAMFILES", "Programfiles(x86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_8() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "XXPROGRAMW6432XX"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_9() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "programw6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_10() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "Programw6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_11() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = None

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_12() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() * "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_13() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "XXVideoLANXX" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_14() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "videolan" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_15() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VIDEOLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_16() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "Videolan" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_17() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" * "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_18() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "XXVLCXX"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_19() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "vlc"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_20() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "Vlc"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_21() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        None,
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_22() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        None,
    )  # fmt: skip


def x__find_default_player_win32__mutmut_23() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_24() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        )  # fmt: skip


def x__find_default_player_win32__mutmut_25() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(None) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_26() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) * subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_27() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(None, None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_28() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(None) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_29() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, ) for envvar in envvars)
            if p
        ),
        "vlc.exe",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_30() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "XXvlc.exeXX",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_31() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "VLC.EXE",
    )  # fmt: skip


def x__find_default_player_win32__mutmut_32() -> Path | None:
    envvars = "PROGRAMFILES", "PROGRAMFILES(X86)", "PROGRAMW6432"
    subpath = Path() / "VideoLAN" / "VLC"

    return _resolve_executable(
        (
            Path(p) / subpath
            for p in (environ.get(envvar, None) for envvar in envvars)
            if p
        ),
        "Vlc.exe",
    )  # fmt: skip

x__find_default_player_win32__mutmut_mutants : ClassVar[MutantDict] = {
'x__find_default_player_win32__mutmut_1': x__find_default_player_win32__mutmut_1, 
    'x__find_default_player_win32__mutmut_2': x__find_default_player_win32__mutmut_2, 
    'x__find_default_player_win32__mutmut_3': x__find_default_player_win32__mutmut_3, 
    'x__find_default_player_win32__mutmut_4': x__find_default_player_win32__mutmut_4, 
    'x__find_default_player_win32__mutmut_5': x__find_default_player_win32__mutmut_5, 
    'x__find_default_player_win32__mutmut_6': x__find_default_player_win32__mutmut_6, 
    'x__find_default_player_win32__mutmut_7': x__find_default_player_win32__mutmut_7, 
    'x__find_default_player_win32__mutmut_8': x__find_default_player_win32__mutmut_8, 
    'x__find_default_player_win32__mutmut_9': x__find_default_player_win32__mutmut_9, 
    'x__find_default_player_win32__mutmut_10': x__find_default_player_win32__mutmut_10, 
    'x__find_default_player_win32__mutmut_11': x__find_default_player_win32__mutmut_11, 
    'x__find_default_player_win32__mutmut_12': x__find_default_player_win32__mutmut_12, 
    'x__find_default_player_win32__mutmut_13': x__find_default_player_win32__mutmut_13, 
    'x__find_default_player_win32__mutmut_14': x__find_default_player_win32__mutmut_14, 
    'x__find_default_player_win32__mutmut_15': x__find_default_player_win32__mutmut_15, 
    'x__find_default_player_win32__mutmut_16': x__find_default_player_win32__mutmut_16, 
    'x__find_default_player_win32__mutmut_17': x__find_default_player_win32__mutmut_17, 
    'x__find_default_player_win32__mutmut_18': x__find_default_player_win32__mutmut_18, 
    'x__find_default_player_win32__mutmut_19': x__find_default_player_win32__mutmut_19, 
    'x__find_default_player_win32__mutmut_20': x__find_default_player_win32__mutmut_20, 
    'x__find_default_player_win32__mutmut_21': x__find_default_player_win32__mutmut_21, 
    'x__find_default_player_win32__mutmut_22': x__find_default_player_win32__mutmut_22, 
    'x__find_default_player_win32__mutmut_23': x__find_default_player_win32__mutmut_23, 
    'x__find_default_player_win32__mutmut_24': x__find_default_player_win32__mutmut_24, 
    'x__find_default_player_win32__mutmut_25': x__find_default_player_win32__mutmut_25, 
    'x__find_default_player_win32__mutmut_26': x__find_default_player_win32__mutmut_26, 
    'x__find_default_player_win32__mutmut_27': x__find_default_player_win32__mutmut_27, 
    'x__find_default_player_win32__mutmut_28': x__find_default_player_win32__mutmut_28, 
    'x__find_default_player_win32__mutmut_29': x__find_default_player_win32__mutmut_29, 
    'x__find_default_player_win32__mutmut_30': x__find_default_player_win32__mutmut_30, 
    'x__find_default_player_win32__mutmut_31': x__find_default_player_win32__mutmut_31, 
    'x__find_default_player_win32__mutmut_32': x__find_default_player_win32__mutmut_32
}

def _find_default_player_win32(*args, **kwargs):
    result = _mutmut_trampoline(x__find_default_player_win32__mutmut_orig, x__find_default_player_win32__mutmut_mutants, args, kwargs)
    return result 

_find_default_player_win32.__signature__ = _mutmut_signature(x__find_default_player_win32__mutmut_orig)
x__find_default_player_win32__mutmut_orig.__name__ = 'x__find_default_player_win32'


def x__find_default_player_darwin__mutmut_orig() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_1() -> Path | None:
    subpath = None

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_2() -> Path | None:
    subpath = Path() * "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_3() -> Path | None:
    subpath = Path() / "XXApplicationsXX" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_4() -> Path | None:
    subpath = Path() / "applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_5() -> Path | None:
    subpath = Path() / "APPLICATIONS" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_6() -> Path | None:
    subpath = Path() / "Applications" * "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_7() -> Path | None:
    subpath = Path() / "Applications" / "XXVLC.appXX" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_8() -> Path | None:
    subpath = Path() / "Applications" / "vlc.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_9() -> Path | None:
    subpath = Path() / "Applications" / "VLC.APP" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_10() -> Path | None:
    subpath = Path() / "Applications" / "Vlc.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_11() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" * "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_12() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "XXContentsXX" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_13() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_14() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "CONTENTS" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_15() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" * "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_16() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "XXMacOSXX"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_17() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "macos"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_18() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MACOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_19() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "Macos"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_20() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        None,
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_21() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        None,
        "vlc",
    )


def x__find_default_player_darwin__mutmut_22() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        None,
    )


def x__find_default_player_darwin__mutmut_23() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_24() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "vlc",
    )


def x__find_default_player_darwin__mutmut_25() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        )


def x__find_default_player_darwin__mutmut_26() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path(None) / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_27() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("XX/XX") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_28() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") * subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_29() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() * subpath,
        ],
        "VLC",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_30() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "XXVLCXX",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_31() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "vlc",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_32() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "Vlc",
        "vlc",
    )


def x__find_default_player_darwin__mutmut_33() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "XXvlcXX",
    )


def x__find_default_player_darwin__mutmut_34() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "VLC",
    )


def x__find_default_player_darwin__mutmut_35() -> Path | None:
    subpath = Path() / "Applications" / "VLC.app" / "Contents" / "MacOS"

    return _resolve_executable(
        [
            Path("/") / subpath,
            Path.home() / subpath,
        ],
        "VLC",
        "Vlc",
    )

x__find_default_player_darwin__mutmut_mutants : ClassVar[MutantDict] = {
'x__find_default_player_darwin__mutmut_1': x__find_default_player_darwin__mutmut_1, 
    'x__find_default_player_darwin__mutmut_2': x__find_default_player_darwin__mutmut_2, 
    'x__find_default_player_darwin__mutmut_3': x__find_default_player_darwin__mutmut_3, 
    'x__find_default_player_darwin__mutmut_4': x__find_default_player_darwin__mutmut_4, 
    'x__find_default_player_darwin__mutmut_5': x__find_default_player_darwin__mutmut_5, 
    'x__find_default_player_darwin__mutmut_6': x__find_default_player_darwin__mutmut_6, 
    'x__find_default_player_darwin__mutmut_7': x__find_default_player_darwin__mutmut_7, 
    'x__find_default_player_darwin__mutmut_8': x__find_default_player_darwin__mutmut_8, 
    'x__find_default_player_darwin__mutmut_9': x__find_default_player_darwin__mutmut_9, 
    'x__find_default_player_darwin__mutmut_10': x__find_default_player_darwin__mutmut_10, 
    'x__find_default_player_darwin__mutmut_11': x__find_default_player_darwin__mutmut_11, 
    'x__find_default_player_darwin__mutmut_12': x__find_default_player_darwin__mutmut_12, 
    'x__find_default_player_darwin__mutmut_13': x__find_default_player_darwin__mutmut_13, 
    'x__find_default_player_darwin__mutmut_14': x__find_default_player_darwin__mutmut_14, 
    'x__find_default_player_darwin__mutmut_15': x__find_default_player_darwin__mutmut_15, 
    'x__find_default_player_darwin__mutmut_16': x__find_default_player_darwin__mutmut_16, 
    'x__find_default_player_darwin__mutmut_17': x__find_default_player_darwin__mutmut_17, 
    'x__find_default_player_darwin__mutmut_18': x__find_default_player_darwin__mutmut_18, 
    'x__find_default_player_darwin__mutmut_19': x__find_default_player_darwin__mutmut_19, 
    'x__find_default_player_darwin__mutmut_20': x__find_default_player_darwin__mutmut_20, 
    'x__find_default_player_darwin__mutmut_21': x__find_default_player_darwin__mutmut_21, 
    'x__find_default_player_darwin__mutmut_22': x__find_default_player_darwin__mutmut_22, 
    'x__find_default_player_darwin__mutmut_23': x__find_default_player_darwin__mutmut_23, 
    'x__find_default_player_darwin__mutmut_24': x__find_default_player_darwin__mutmut_24, 
    'x__find_default_player_darwin__mutmut_25': x__find_default_player_darwin__mutmut_25, 
    'x__find_default_player_darwin__mutmut_26': x__find_default_player_darwin__mutmut_26, 
    'x__find_default_player_darwin__mutmut_27': x__find_default_player_darwin__mutmut_27, 
    'x__find_default_player_darwin__mutmut_28': x__find_default_player_darwin__mutmut_28, 
    'x__find_default_player_darwin__mutmut_29': x__find_default_player_darwin__mutmut_29, 
    'x__find_default_player_darwin__mutmut_30': x__find_default_player_darwin__mutmut_30, 
    'x__find_default_player_darwin__mutmut_31': x__find_default_player_darwin__mutmut_31, 
    'x__find_default_player_darwin__mutmut_32': x__find_default_player_darwin__mutmut_32, 
    'x__find_default_player_darwin__mutmut_33': x__find_default_player_darwin__mutmut_33, 
    'x__find_default_player_darwin__mutmut_34': x__find_default_player_darwin__mutmut_34, 
    'x__find_default_player_darwin__mutmut_35': x__find_default_player_darwin__mutmut_35
}

def _find_default_player_darwin(*args, **kwargs):
    result = _mutmut_trampoline(x__find_default_player_darwin__mutmut_orig, x__find_default_player_darwin__mutmut_mutants, args, kwargs)
    return result 

_find_default_player_darwin.__signature__ = _mutmut_signature(x__find_default_player_darwin__mutmut_orig)
x__find_default_player_darwin__mutmut_orig.__name__ = 'x__find_default_player_darwin'


def x__find_default_player_other__mutmut_orig() -> Path | None:
    return _resolve_executable(
        [],
        "vlc",
    )


def x__find_default_player_other__mutmut_1() -> Path | None:
    return _resolve_executable(
        None,
        "vlc",
    )


def x__find_default_player_other__mutmut_2() -> Path | None:
    return _resolve_executable(
        [],
        None,
    )


def x__find_default_player_other__mutmut_3() -> Path | None:
    return _resolve_executable(
        "vlc",
    )


def x__find_default_player_other__mutmut_4() -> Path | None:
    return _resolve_executable(
        [],
        )


def x__find_default_player_other__mutmut_5() -> Path | None:
    return _resolve_executable(
        [],
        "XXvlcXX",
    )


def x__find_default_player_other__mutmut_6() -> Path | None:
    return _resolve_executable(
        [],
        "VLC",
    )


def x__find_default_player_other__mutmut_7() -> Path | None:
    return _resolve_executable(
        [],
        "Vlc",
    )

x__find_default_player_other__mutmut_mutants : ClassVar[MutantDict] = {
'x__find_default_player_other__mutmut_1': x__find_default_player_other__mutmut_1, 
    'x__find_default_player_other__mutmut_2': x__find_default_player_other__mutmut_2, 
    'x__find_default_player_other__mutmut_3': x__find_default_player_other__mutmut_3, 
    'x__find_default_player_other__mutmut_4': x__find_default_player_other__mutmut_4, 
    'x__find_default_player_other__mutmut_5': x__find_default_player_other__mutmut_5, 
    'x__find_default_player_other__mutmut_6': x__find_default_player_other__mutmut_6, 
    'x__find_default_player_other__mutmut_7': x__find_default_player_other__mutmut_7
}

def _find_default_player_other(*args, **kwargs):
    result = _mutmut_trampoline(x__find_default_player_other__mutmut_orig, x__find_default_player_other__mutmut_mutants, args, kwargs)
    return result 

_find_default_player_other.__signature__ = _mutmut_signature(x__find_default_player_other__mutmut_orig)
x__find_default_player_other__mutmut_orig.__name__ = 'x__find_default_player_other'


def find_default_player() -> Path | None:
    if is_win32:
        return _find_default_player_win32()
    elif is_darwin:
        return _find_default_player_darwin()
    else:
        return _find_default_player_other()

from __future__ import annotations

from pathlib import Path
from shutil import which
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


def x_resolve_executable__mutmut_orig(
    custom: str | Path | None = None,
    names: list[str] | None = None,
    fallbacks: list[str | Path] | None = None,
) -> str | Path | None:
    if custom:
        return which(custom)

    for item in (names or []) + (fallbacks or []):
        executable = which(item)
        if executable:
            return executable

    return None


def x_resolve_executable__mutmut_1(
    custom: str | Path | None = None,
    names: list[str] | None = None,
    fallbacks: list[str | Path] | None = None,
) -> str | Path | None:
    if custom:
        return which(None)

    for item in (names or []) + (fallbacks or []):
        executable = which(item)
        if executable:
            return executable

    return None


def x_resolve_executable__mutmut_2(
    custom: str | Path | None = None,
    names: list[str] | None = None,
    fallbacks: list[str | Path] | None = None,
) -> str | Path | None:
    if custom:
        return which(custom)

    for item in (names and []) + (fallbacks or []):
        executable = which(item)
        if executable:
            return executable

    return None


def x_resolve_executable__mutmut_3(
    custom: str | Path | None = None,
    names: list[str] | None = None,
    fallbacks: list[str | Path] | None = None,
) -> str | Path | None:
    if custom:
        return which(custom)

    for item in (names or []) - (fallbacks or []):
        executable = which(item)
        if executable:
            return executable

    return None


def x_resolve_executable__mutmut_4(
    custom: str | Path | None = None,
    names: list[str] | None = None,
    fallbacks: list[str | Path] | None = None,
) -> str | Path | None:
    if custom:
        return which(custom)

    for item in (names or []) + (fallbacks and []):
        executable = which(item)
        if executable:
            return executable

    return None


def x_resolve_executable__mutmut_5(
    custom: str | Path | None = None,
    names: list[str] | None = None,
    fallbacks: list[str | Path] | None = None,
) -> str | Path | None:
    if custom:
        return which(custom)

    for item in (names or []) + (fallbacks or []):
        executable = None
        if executable:
            return executable

    return None


def x_resolve_executable__mutmut_6(
    custom: str | Path | None = None,
    names: list[str] | None = None,
    fallbacks: list[str | Path] | None = None,
) -> str | Path | None:
    if custom:
        return which(custom)

    for item in (names or []) + (fallbacks or []):
        executable = which(None)
        if executable:
            return executable

    return None

x_resolve_executable__mutmut_mutants : ClassVar[MutantDict] = {
'x_resolve_executable__mutmut_1': x_resolve_executable__mutmut_1, 
    'x_resolve_executable__mutmut_2': x_resolve_executable__mutmut_2, 
    'x_resolve_executable__mutmut_3': x_resolve_executable__mutmut_3, 
    'x_resolve_executable__mutmut_4': x_resolve_executable__mutmut_4, 
    'x_resolve_executable__mutmut_5': x_resolve_executable__mutmut_5, 
    'x_resolve_executable__mutmut_6': x_resolve_executable__mutmut_6
}

def resolve_executable(*args, **kwargs):
    result = _mutmut_trampoline(x_resolve_executable__mutmut_orig, x_resolve_executable__mutmut_mutants, args, kwargs)
    return result 

resolve_executable.__signature__ = _mutmut_signature(x_resolve_executable__mutmut_orig)
x_resolve_executable__mutmut_orig.__name__ = 'x_resolve_executable'

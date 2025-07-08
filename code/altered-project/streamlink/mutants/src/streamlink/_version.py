# This module will get replaced by versioningit when building a source distribution
# and instead of trying to get the version string from git, a static version string will be set


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
def x__get_version__mutmut_orig() -> str:
    """
    Get the current version from git in "editable" installs
    """
    from pathlib import Path  # noqa: PLC0415
    from versioningit import get_version  # noqa: PLC0415
    import streamlink  # noqa: PLC0415

    return get_version(project_dir=Path(streamlink.__file__).parents[2])
def x__get_version__mutmut_1() -> str:
    """
    Get the current version from git in "editable" installs
    """
    from pathlib import Path  # noqa: PLC0415
    from versioningit import get_version  # noqa: PLC0415
    import streamlink  # noqa: PLC0415

    return get_version(project_dir=None)
def x__get_version__mutmut_2() -> str:
    """
    Get the current version from git in "editable" installs
    """
    from pathlib import Path  # noqa: PLC0415
    from versioningit import get_version  # noqa: PLC0415
    import streamlink  # noqa: PLC0415

    return get_version(project_dir=Path(None).parents[2])
def x__get_version__mutmut_3() -> str:
    """
    Get the current version from git in "editable" installs
    """
    from pathlib import Path  # noqa: PLC0415
    from versioningit import get_version  # noqa: PLC0415
    import streamlink  # noqa: PLC0415

    return get_version(project_dir=Path(streamlink.__file__).parents[3])

x__get_version__mutmut_mutants : ClassVar[MutantDict] = {
'x__get_version__mutmut_1': x__get_version__mutmut_1, 
    'x__get_version__mutmut_2': x__get_version__mutmut_2, 
    'x__get_version__mutmut_3': x__get_version__mutmut_3
}

def _get_version(*args, **kwargs):
    result = _mutmut_trampoline(x__get_version__mutmut_orig, x__get_version__mutmut_mutants, args, kwargs)
    return result 

_get_version.__signature__ = _mutmut_signature(x__get_version__mutmut_orig)
x__get_version__mutmut_orig.__name__ = 'x__get_version'


__version__ = _get_version()

from signal import SIGINT, SIGTERM, signal
from sys import exit  # noqa: A004
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


def x__exit__mutmut_orig(*_):
    # don't raise a KeyboardInterrupt until streamlink_cli has been fully initialized
    exit(128 | 2)


def x__exit__mutmut_1(*_):
    # don't raise a KeyboardInterrupt until streamlink_cli has been fully initialized
    exit(None)


def x__exit__mutmut_2(*_):
    # don't raise a KeyboardInterrupt until streamlink_cli has been fully initialized
    exit(129 | 2)


def x__exit__mutmut_3(*_):
    # don't raise a KeyboardInterrupt until streamlink_cli has been fully initialized
    exit(128 & 2)


def x__exit__mutmut_4(*_):
    # don't raise a KeyboardInterrupt until streamlink_cli has been fully initialized
    exit(128 | 3)

x__exit__mutmut_mutants : ClassVar[MutantDict] = {
'x__exit__mutmut_1': x__exit__mutmut_1, 
    'x__exit__mutmut_2': x__exit__mutmut_2, 
    'x__exit__mutmut_3': x__exit__mutmut_3, 
    'x__exit__mutmut_4': x__exit__mutmut_4
}

def _exit(*args, **kwargs):
    result = _mutmut_trampoline(x__exit__mutmut_orig, x__exit__mutmut_mutants, args, kwargs)
    return result 

_exit.__signature__ = _mutmut_signature(x__exit__mutmut_orig)
x__exit__mutmut_orig.__name__ = 'x__exit'


# override default SIGINT handler (and set SIGTERM handler) as early as possible
signal(SIGINT, _exit)
signal(SIGTERM, _exit)

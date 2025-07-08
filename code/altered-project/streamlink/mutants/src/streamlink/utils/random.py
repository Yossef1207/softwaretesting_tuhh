from random import choice


CHOICES_NUM = "0123456789"
CHOICES_ALPHA_LOWER = "abcdefghijklmnopqrstuvwxyz"
CHOICES_ALPHA_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHOICES_ALPHA = f"{CHOICES_ALPHA_LOWER}{CHOICES_ALPHA_UPPER}"
CHOICES_ALPHA_NUM = f"{CHOICES_NUM}{CHOICES_ALPHA}"
CHOICES_HEX_LOWER = f"{CHOICES_NUM}{CHOICES_ALPHA_LOWER[:6]}"
CHOICES_HEX_UPPER = f"{CHOICES_NUM}{CHOICES_ALPHA_UPPER[:6]}"
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


def x_random_token__mutmut_orig(length: int = 32, choices: str = CHOICES_ALPHA_NUM) -> str:
    return "".join(choice(choices) for _ in range(length))


def x_random_token__mutmut_1(length: int = 33, choices: str = CHOICES_ALPHA_NUM) -> str:
    return "".join(choice(choices) for _ in range(length))


def x_random_token__mutmut_2(length: int = 32, choices: str = CHOICES_ALPHA_NUM) -> str:
    return "".join(None)


def x_random_token__mutmut_3(length: int = 32, choices: str = CHOICES_ALPHA_NUM) -> str:
    return "XXXX".join(choice(choices) for _ in range(length))


def x_random_token__mutmut_4(length: int = 32, choices: str = CHOICES_ALPHA_NUM) -> str:
    return "".join(choice(None) for _ in range(length))


def x_random_token__mutmut_5(length: int = 32, choices: str = CHOICES_ALPHA_NUM) -> str:
    return "".join(choice(choices) for _ in range(None))

x_random_token__mutmut_mutants : ClassVar[MutantDict] = {
'x_random_token__mutmut_1': x_random_token__mutmut_1, 
    'x_random_token__mutmut_2': x_random_token__mutmut_2, 
    'x_random_token__mutmut_3': x_random_token__mutmut_3, 
    'x_random_token__mutmut_4': x_random_token__mutmut_4, 
    'x_random_token__mutmut_5': x_random_token__mutmut_5
}

def random_token(*args, **kwargs):
    result = _mutmut_trampoline(x_random_token__mutmut_orig, x_random_token__mutmut_mutants, args, kwargs)
    return result 

random_token.__signature__ = _mutmut_signature(x_random_token__mutmut_orig)
x_random_token__mutmut_orig.__name__ = 'x_random_token'

from streamlink.user_input import UserInputRequester
from streamlink_cli.console.console import ConsoleOutput
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


class ConsoleUserInputRequester(UserInputRequester):
    """
    Request input from the user on the console using the standard ask/askpass methods
    """

    def xǁConsoleUserInputRequesterǁ__init____mutmut_orig(self, console: ConsoleOutput):
        self.console = console

    def xǁConsoleUserInputRequesterǁ__init____mutmut_1(self, console: ConsoleOutput):
        self.console = None
    
    xǁConsoleUserInputRequesterǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleUserInputRequesterǁ__init____mutmut_1': xǁConsoleUserInputRequesterǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleUserInputRequesterǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁConsoleUserInputRequesterǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁConsoleUserInputRequesterǁ__init____mutmut_orig)
    xǁConsoleUserInputRequesterǁ__init____mutmut_orig.__name__ = 'xǁConsoleUserInputRequesterǁ__init__'

    def xǁConsoleUserInputRequesterǁask__mutmut_orig(self, prompt: str) -> str:
        return self.console.ask(f"{prompt.strip()}: ")

    def xǁConsoleUserInputRequesterǁask__mutmut_1(self, prompt: str) -> str:
        return self.console.ask(None)
    
    xǁConsoleUserInputRequesterǁask__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleUserInputRequesterǁask__mutmut_1': xǁConsoleUserInputRequesterǁask__mutmut_1
    }
    
    def ask(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleUserInputRequesterǁask__mutmut_orig"), object.__getattribute__(self, "xǁConsoleUserInputRequesterǁask__mutmut_mutants"), args, kwargs, self)
        return result 
    
    ask.__signature__ = _mutmut_signature(xǁConsoleUserInputRequesterǁask__mutmut_orig)
    xǁConsoleUserInputRequesterǁask__mutmut_orig.__name__ = 'xǁConsoleUserInputRequesterǁask'

    def xǁConsoleUserInputRequesterǁask_password__mutmut_orig(self, prompt: str) -> str:
        return self.console.ask_password(f"{prompt.strip()}: ")

    def xǁConsoleUserInputRequesterǁask_password__mutmut_1(self, prompt: str) -> str:
        return self.console.ask_password(None)
    
    xǁConsoleUserInputRequesterǁask_password__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleUserInputRequesterǁask_password__mutmut_1': xǁConsoleUserInputRequesterǁask_password__mutmut_1
    }
    
    def ask_password(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleUserInputRequesterǁask_password__mutmut_orig"), object.__getattribute__(self, "xǁConsoleUserInputRequesterǁask_password__mutmut_mutants"), args, kwargs, self)
        return result 
    
    ask_password.__signature__ = _mutmut_signature(xǁConsoleUserInputRequesterǁask_password__mutmut_orig)
    xǁConsoleUserInputRequesterǁask_password__mutmut_orig.__name__ = 'xǁConsoleUserInputRequesterǁask_password'

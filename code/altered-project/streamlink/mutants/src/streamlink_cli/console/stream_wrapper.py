from __future__ import annotations

from io import TextIOWrapper
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


class StreamWrapper:
    def xǁStreamWrapperǁ__init____mutmut_orig(self, stream):
        super().__init__()
        self._stream = stream
        self._target = None
    def xǁStreamWrapperǁ__init____mutmut_1(self, stream):
        super().__init__()
        self._stream = None
        self._target = None
    def xǁStreamWrapperǁ__init____mutmut_2(self, stream):
        super().__init__()
        self._stream = stream
        self._target = ""
    
    xǁStreamWrapperǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamWrapperǁ__init____mutmut_1': xǁStreamWrapperǁ__init____mutmut_1, 
        'xǁStreamWrapperǁ__init____mutmut_2': xǁStreamWrapperǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamWrapperǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStreamWrapperǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStreamWrapperǁ__init____mutmut_orig)
    xǁStreamWrapperǁ__init____mutmut_orig.__name__ = 'xǁStreamWrapperǁ__init__'

    @classmethod
    def wrap(cls, obj, attr):
        stream = getattr(obj, attr)
        if not isinstance(stream, TextIOWrapper):
            raise AttributeError(f"{stream!r} is not a TextIOWrapper object ({obj!r}, {attr!r})")

        console_output_stream = cls(stream)
        console_output_stream._wrap(obj, attr)

        return console_output_stream

    def xǁStreamWrapperǁ_wrap__mutmut_orig(self, obj, attr):
        self._target = obj, attr
        setattr(obj, attr, self)

    def xǁStreamWrapperǁ_wrap__mutmut_1(self, obj, attr):
        self._target = None
        setattr(obj, attr, self)

    def xǁStreamWrapperǁ_wrap__mutmut_2(self, obj, attr):
        self._target = obj, attr
        setattr(None, attr, self)

    def xǁStreamWrapperǁ_wrap__mutmut_3(self, obj, attr):
        self._target = obj, attr
        setattr(obj, None, self)

    def xǁStreamWrapperǁ_wrap__mutmut_4(self, obj, attr):
        self._target = obj, attr
        setattr(obj, attr, None)

    def xǁStreamWrapperǁ_wrap__mutmut_5(self, obj, attr):
        self._target = obj, attr
        setattr(attr, self)

    def xǁStreamWrapperǁ_wrap__mutmut_6(self, obj, attr):
        self._target = obj, attr
        setattr(obj, self)

    def xǁStreamWrapperǁ_wrap__mutmut_7(self, obj, attr):
        self._target = obj, attr
        setattr(obj, attr, )
    
    xǁStreamWrapperǁ_wrap__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamWrapperǁ_wrap__mutmut_1': xǁStreamWrapperǁ_wrap__mutmut_1, 
        'xǁStreamWrapperǁ_wrap__mutmut_2': xǁStreamWrapperǁ_wrap__mutmut_2, 
        'xǁStreamWrapperǁ_wrap__mutmut_3': xǁStreamWrapperǁ_wrap__mutmut_3, 
        'xǁStreamWrapperǁ_wrap__mutmut_4': xǁStreamWrapperǁ_wrap__mutmut_4, 
        'xǁStreamWrapperǁ_wrap__mutmut_5': xǁStreamWrapperǁ_wrap__mutmut_5, 
        'xǁStreamWrapperǁ_wrap__mutmut_6': xǁStreamWrapperǁ_wrap__mutmut_6, 
        'xǁStreamWrapperǁ_wrap__mutmut_7': xǁStreamWrapperǁ_wrap__mutmut_7
    }
    
    def _wrap(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamWrapperǁ_wrap__mutmut_orig"), object.__getattribute__(self, "xǁStreamWrapperǁ_wrap__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _wrap.__signature__ = _mutmut_signature(xǁStreamWrapperǁ_wrap__mutmut_orig)
    xǁStreamWrapperǁ_wrap__mutmut_orig.__name__ = 'xǁStreamWrapperǁ_wrap'

    def xǁStreamWrapperǁrestore__mutmut_orig(self):
        if self._target:  # pragma: no branch
            setattr(*self._target, self._stream)

    def xǁStreamWrapperǁrestore__mutmut_1(self):
        if self._target:  # pragma: no branch
            setattr(*self._target, None)

    def xǁStreamWrapperǁrestore__mutmut_2(self):
        if self._target:  # pragma: no branch
            setattr(self._stream)

    def xǁStreamWrapperǁrestore__mutmut_3(self):
        if self._target:  # pragma: no branch
            setattr(*self._target, )
    
    xǁStreamWrapperǁrestore__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamWrapperǁrestore__mutmut_1': xǁStreamWrapperǁrestore__mutmut_1, 
        'xǁStreamWrapperǁrestore__mutmut_2': xǁStreamWrapperǁrestore__mutmut_2, 
        'xǁStreamWrapperǁrestore__mutmut_3': xǁStreamWrapperǁrestore__mutmut_3
    }
    
    def restore(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamWrapperǁrestore__mutmut_orig"), object.__getattribute__(self, "xǁStreamWrapperǁrestore__mutmut_mutants"), args, kwargs, self)
        return result 
    
    restore.__signature__ = _mutmut_signature(xǁStreamWrapperǁrestore__mutmut_orig)
    xǁStreamWrapperǁrestore__mutmut_orig.__name__ = 'xǁStreamWrapperǁrestore'

    def xǁStreamWrapperǁ__getattr____mutmut_orig(self, name):
        return getattr(self._stream, name)

    def xǁStreamWrapperǁ__getattr____mutmut_1(self, name):
        return getattr(None, name)

    def xǁStreamWrapperǁ__getattr____mutmut_2(self, name):
        return getattr(self._stream, None)

    def xǁStreamWrapperǁ__getattr____mutmut_3(self, name):
        return getattr(name)

    def xǁStreamWrapperǁ__getattr____mutmut_4(self, name):
        return getattr(self._stream, )
    
    xǁStreamWrapperǁ__getattr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamWrapperǁ__getattr____mutmut_1': xǁStreamWrapperǁ__getattr____mutmut_1, 
        'xǁStreamWrapperǁ__getattr____mutmut_2': xǁStreamWrapperǁ__getattr____mutmut_2, 
        'xǁStreamWrapperǁ__getattr____mutmut_3': xǁStreamWrapperǁ__getattr____mutmut_3, 
        'xǁStreamWrapperǁ__getattr____mutmut_4': xǁStreamWrapperǁ__getattr____mutmut_4
    }
    
    def __getattr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamWrapperǁ__getattr____mutmut_orig"), object.__getattribute__(self, "xǁStreamWrapperǁ__getattr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __getattr__.__signature__ = _mutmut_signature(xǁStreamWrapperǁ__getattr____mutmut_orig)
    xǁStreamWrapperǁ__getattr____mutmut_orig.__name__ = 'xǁStreamWrapperǁ__getattr__'

    def __del__(self):  # pragma: no cover
        # Don't automatically close the underlying buffer on object destruction, as this breaks our tests.
        # We manually close the wrapped streams ourselves.
        return

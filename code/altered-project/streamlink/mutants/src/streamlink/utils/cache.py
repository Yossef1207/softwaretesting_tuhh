from __future__ import annotations

from collections import OrderedDict
from typing import Generic, TypeVar


TCacheKey = TypeVar("TCacheKey")
TCacheValue = TypeVar("TCacheValue")
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


class LRUCache(Generic[TCacheKey, TCacheValue]):
    def xǁLRUCacheǁ__init____mutmut_orig(self, num: int):
        self.cache: OrderedDict[TCacheKey, TCacheValue] = OrderedDict()
        self.num = num
    def xǁLRUCacheǁ__init____mutmut_1(self, num: int):
        self.cache: OrderedDict[TCacheKey, TCacheValue] = None
        self.num = num
    def xǁLRUCacheǁ__init____mutmut_2(self, num: int):
        self.cache: OrderedDict[TCacheKey, TCacheValue] = OrderedDict()
        self.num = None
    
    xǁLRUCacheǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLRUCacheǁ__init____mutmut_1': xǁLRUCacheǁ__init____mutmut_1, 
        'xǁLRUCacheǁ__init____mutmut_2': xǁLRUCacheǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLRUCacheǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁLRUCacheǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁLRUCacheǁ__init____mutmut_orig)
    xǁLRUCacheǁ__init____mutmut_orig.__name__ = 'xǁLRUCacheǁ__init__'

    def xǁLRUCacheǁget__mutmut_orig(self, key: TCacheKey) -> TCacheValue | None:
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def xǁLRUCacheǁget__mutmut_1(self, key: TCacheKey) -> TCacheValue | None:
        if key in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def xǁLRUCacheǁget__mutmut_2(self, key: TCacheKey) -> TCacheValue | None:
        if key not in self.cache:
            return None
        self.cache.move_to_end(None)
        return self.cache[key]
    
    xǁLRUCacheǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLRUCacheǁget__mutmut_1': xǁLRUCacheǁget__mutmut_1, 
        'xǁLRUCacheǁget__mutmut_2': xǁLRUCacheǁget__mutmut_2
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLRUCacheǁget__mutmut_orig"), object.__getattribute__(self, "xǁLRUCacheǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁLRUCacheǁget__mutmut_orig)
    xǁLRUCacheǁget__mutmut_orig.__name__ = 'xǁLRUCacheǁget'

    def xǁLRUCacheǁset__mutmut_orig(self, key: TCacheKey, value: TCacheValue) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.num:
            self.cache.popitem(last=False)

    def xǁLRUCacheǁset__mutmut_1(self, key: TCacheKey, value: TCacheValue) -> None:
        self.cache[key] = None
        self.cache.move_to_end(key)
        if len(self.cache) > self.num:
            self.cache.popitem(last=False)

    def xǁLRUCacheǁset__mutmut_2(self, key: TCacheKey, value: TCacheValue) -> None:
        self.cache[key] = value
        self.cache.move_to_end(None)
        if len(self.cache) > self.num:
            self.cache.popitem(last=False)

    def xǁLRUCacheǁset__mutmut_3(self, key: TCacheKey, value: TCacheValue) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) >= self.num:
            self.cache.popitem(last=False)

    def xǁLRUCacheǁset__mutmut_4(self, key: TCacheKey, value: TCacheValue) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.num:
            self.cache.popitem(last=None)

    def xǁLRUCacheǁset__mutmut_5(self, key: TCacheKey, value: TCacheValue) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.num:
            self.cache.popitem(last=True)
    
    xǁLRUCacheǁset__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLRUCacheǁset__mutmut_1': xǁLRUCacheǁset__mutmut_1, 
        'xǁLRUCacheǁset__mutmut_2': xǁLRUCacheǁset__mutmut_2, 
        'xǁLRUCacheǁset__mutmut_3': xǁLRUCacheǁset__mutmut_3, 
        'xǁLRUCacheǁset__mutmut_4': xǁLRUCacheǁset__mutmut_4, 
        'xǁLRUCacheǁset__mutmut_5': xǁLRUCacheǁset__mutmut_5
    }
    
    def set(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLRUCacheǁset__mutmut_orig"), object.__getattribute__(self, "xǁLRUCacheǁset__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set.__signature__ = _mutmut_signature(xǁLRUCacheǁset__mutmut_orig)
    xǁLRUCacheǁset__mutmut_orig.__name__ = 'xǁLRUCacheǁset'

from __future__ import annotations

from collections import defaultdict
from itertools import count
from threading import RLock, Thread
from typing import Iterator


_threadname_lock = RLock()
_threadname_counters: defaultdict[str, Iterator[int]] = defaultdict(count)
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


class NamedThread(Thread):
    def xǁNamedThreadǁ__init____mutmut_orig(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = self.__class__.__name__
            if name:
                newname += f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["name"] = f"{newname}-{next(_threadname_counters[newname])}"

        super().__init__(*args, **kwargs)
    def xǁNamedThreadǁ__init____mutmut_1(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = None
            if name:
                newname += f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["name"] = f"{newname}-{next(_threadname_counters[newname])}"

        super().__init__(*args, **kwargs)
    def xǁNamedThreadǁ__init____mutmut_2(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = self.__class__.__name__
            if name:
                newname = f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["name"] = f"{newname}-{next(_threadname_counters[newname])}"

        super().__init__(*args, **kwargs)
    def xǁNamedThreadǁ__init____mutmut_3(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = self.__class__.__name__
            if name:
                newname -= f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["name"] = f"{newname}-{next(_threadname_counters[newname])}"

        super().__init__(*args, **kwargs)
    def xǁNamedThreadǁ__init____mutmut_4(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = self.__class__.__name__
            if name:
                newname += f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["name"] = None

        super().__init__(*args, **kwargs)
    def xǁNamedThreadǁ__init____mutmut_5(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = self.__class__.__name__
            if name:
                newname += f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["XXnameXX"] = f"{newname}-{next(_threadname_counters[newname])}"

        super().__init__(*args, **kwargs)
    def xǁNamedThreadǁ__init____mutmut_6(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = self.__class__.__name__
            if name:
                newname += f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["NAME"] = f"{newname}-{next(_threadname_counters[newname])}"

        super().__init__(*args, **kwargs)
    def xǁNamedThreadǁ__init____mutmut_7(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = self.__class__.__name__
            if name:
                newname += f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["Name"] = f"{newname}-{next(_threadname_counters[newname])}"

        super().__init__(*args, **kwargs)
    def xǁNamedThreadǁ__init____mutmut_8(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = self.__class__.__name__
            if name:
                newname += f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["name"] = f"{newname}-{next(None)}"

        super().__init__(*args, **kwargs)
    def xǁNamedThreadǁ__init____mutmut_9(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = self.__class__.__name__
            if name:
                newname += f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["name"] = f"{newname}-{next(_threadname_counters[newname])}"

        super().__init__(**kwargs)
    def xǁNamedThreadǁ__init____mutmut_10(self, *args, name: str | None = None, **kwargs):
        with _threadname_lock:
            newname = self.__class__.__name__
            if name:
                newname += f"-{name}"

            # noinspection PyUnresolvedReferences
            kwargs["name"] = f"{newname}-{next(_threadname_counters[newname])}"

        super().__init__(*args, )
    
    xǁNamedThreadǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNamedThreadǁ__init____mutmut_1': xǁNamedThreadǁ__init____mutmut_1, 
        'xǁNamedThreadǁ__init____mutmut_2': xǁNamedThreadǁ__init____mutmut_2, 
        'xǁNamedThreadǁ__init____mutmut_3': xǁNamedThreadǁ__init____mutmut_3, 
        'xǁNamedThreadǁ__init____mutmut_4': xǁNamedThreadǁ__init____mutmut_4, 
        'xǁNamedThreadǁ__init____mutmut_5': xǁNamedThreadǁ__init____mutmut_5, 
        'xǁNamedThreadǁ__init____mutmut_6': xǁNamedThreadǁ__init____mutmut_6, 
        'xǁNamedThreadǁ__init____mutmut_7': xǁNamedThreadǁ__init____mutmut_7, 
        'xǁNamedThreadǁ__init____mutmut_8': xǁNamedThreadǁ__init____mutmut_8, 
        'xǁNamedThreadǁ__init____mutmut_9': xǁNamedThreadǁ__init____mutmut_9, 
        'xǁNamedThreadǁ__init____mutmut_10': xǁNamedThreadǁ__init____mutmut_10
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNamedThreadǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁNamedThreadǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁNamedThreadǁ__init____mutmut_orig)
    xǁNamedThreadǁ__init____mutmut_orig.__name__ = 'xǁNamedThreadǁ__init__'

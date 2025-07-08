from __future__ import annotations

import argparse
from collections.abc import Callable, Iterable, Iterator, Mapping
from typing import Any, ClassVar, Dict, Literal, TypeVar
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


class Options(Dict[str, Any]):
    """
    For storing options to be used by the Streamlink session and plugins, with default values.

    Note: Option names are normalized by replacing "_" with "-".
          This means that the keys ``example_one`` and ``example-one`` are equivalent.
    """

    #: Optional getter mapping for :class:`Options` subclasses
    _MAP_GETTERS: ClassVar[Mapping[str, Callable[[Any, str], Any]]] = {}

    #: Optional setter mapping for :class:`Options` subclasses
    _MAP_SETTERS: ClassVar[Mapping[str, Callable[[Any, str, Any], None]]] = {}

    def xǁOptionsǁ__init____mutmut_orig(self, defaults: Mapping[str, Any] | None = None):
        super().__init__()
        self._defaults = self._normalize_dict(defaults or {})
        super().update(self._defaults)

    def xǁOptionsǁ__init____mutmut_1(self, defaults: Mapping[str, Any] | None = None):
        super().__init__()
        self._defaults = None
        super().update(self._defaults)

    def xǁOptionsǁ__init____mutmut_2(self, defaults: Mapping[str, Any] | None = None):
        super().__init__()
        self._defaults = self._normalize_dict(None)
        super().update(self._defaults)

    def xǁOptionsǁ__init____mutmut_3(self, defaults: Mapping[str, Any] | None = None):
        super().__init__()
        self._defaults = self._normalize_dict(defaults and {})
        super().update(self._defaults)

    def xǁOptionsǁ__init____mutmut_4(self, defaults: Mapping[str, Any] | None = None):
        super().__init__()
        self._defaults = self._normalize_dict(defaults or {})
        super().update(None)
    
    xǁOptionsǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOptionsǁ__init____mutmut_1': xǁOptionsǁ__init____mutmut_1, 
        'xǁOptionsǁ__init____mutmut_2': xǁOptionsǁ__init____mutmut_2, 
        'xǁOptionsǁ__init____mutmut_3': xǁOptionsǁ__init____mutmut_3, 
        'xǁOptionsǁ__init____mutmut_4': xǁOptionsǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOptionsǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁOptionsǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁOptionsǁ__init____mutmut_orig)
    xǁOptionsǁ__init____mutmut_orig.__name__ = 'xǁOptionsǁ__init__'

    @staticmethod
    def _normalize_key(name: str) -> str:
        return name.replace("_", "-")

    @classmethod
    def _normalize_dict(cls, src: Mapping[str, Any]) -> dict[str, Any]:
        normalize_key = cls._normalize_key
        return {normalize_key(key): value for key, value in src.items()}

    @property
    def defaults(self):
        return self._defaults

    def xǁOptionsǁclear__mutmut_orig(self) -> None:
        """Restore default options"""

        super().clear()
        self.update(self._defaults)

    def xǁOptionsǁclear__mutmut_1(self) -> None:
        """Restore default options"""

        super().clear()
        self.update(None)
    
    xǁOptionsǁclear__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOptionsǁclear__mutmut_1': xǁOptionsǁclear__mutmut_1
    }
    
    def clear(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOptionsǁclear__mutmut_orig"), object.__getattribute__(self, "xǁOptionsǁclear__mutmut_mutants"), args, kwargs, self)
        return result 
    
    clear.__signature__ = _mutmut_signature(xǁOptionsǁclear__mutmut_orig)
    xǁOptionsǁclear__mutmut_orig.__name__ = 'xǁOptionsǁclear'

    def xǁOptionsǁget__mutmut_orig(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_GETTERS.get(normalized)
        if method is not None:
            return method(self, normalized)
        else:
            return super().get(normalized)

    def xǁOptionsǁget__mutmut_1(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = None
        method = self._MAP_GETTERS.get(normalized)
        if method is not None:
            return method(self, normalized)
        else:
            return super().get(normalized)

    def xǁOptionsǁget__mutmut_2(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = self._normalize_key(None)
        method = self._MAP_GETTERS.get(normalized)
        if method is not None:
            return method(self, normalized)
        else:
            return super().get(normalized)

    def xǁOptionsǁget__mutmut_3(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = self._normalize_key(key)
        method = None
        if method is not None:
            return method(self, normalized)
        else:
            return super().get(normalized)

    def xǁOptionsǁget__mutmut_4(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_GETTERS.get(None)
        if method is not None:
            return method(self, normalized)
        else:
            return super().get(normalized)

    def xǁOptionsǁget__mutmut_5(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_GETTERS.get(normalized)
        if method is None:
            return method(self, normalized)
        else:
            return super().get(normalized)

    def xǁOptionsǁget__mutmut_6(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_GETTERS.get(normalized)
        if method is not None:
            return method(None, normalized)
        else:
            return super().get(normalized)

    def xǁOptionsǁget__mutmut_7(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_GETTERS.get(normalized)
        if method is not None:
            return method(self, None)
        else:
            return super().get(normalized)

    def xǁOptionsǁget__mutmut_8(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_GETTERS.get(normalized)
        if method is not None:
            return method(normalized)
        else:
            return super().get(normalized)

    def xǁOptionsǁget__mutmut_9(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_GETTERS.get(normalized)
        if method is not None:
            return method(self, )
        else:
            return super().get(normalized)

    def xǁOptionsǁget__mutmut_10(self, key: str) -> Any:  # type: ignore[override]
        """Get the stored value of a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_GETTERS.get(normalized)
        if method is not None:
            return method(self, normalized)
        else:
            return super().get(None)
    
    xǁOptionsǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOptionsǁget__mutmut_1': xǁOptionsǁget__mutmut_1, 
        'xǁOptionsǁget__mutmut_2': xǁOptionsǁget__mutmut_2, 
        'xǁOptionsǁget__mutmut_3': xǁOptionsǁget__mutmut_3, 
        'xǁOptionsǁget__mutmut_4': xǁOptionsǁget__mutmut_4, 
        'xǁOptionsǁget__mutmut_5': xǁOptionsǁget__mutmut_5, 
        'xǁOptionsǁget__mutmut_6': xǁOptionsǁget__mutmut_6, 
        'xǁOptionsǁget__mutmut_7': xǁOptionsǁget__mutmut_7, 
        'xǁOptionsǁget__mutmut_8': xǁOptionsǁget__mutmut_8, 
        'xǁOptionsǁget__mutmut_9': xǁOptionsǁget__mutmut_9, 
        'xǁOptionsǁget__mutmut_10': xǁOptionsǁget__mutmut_10
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOptionsǁget__mutmut_orig"), object.__getattribute__(self, "xǁOptionsǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁOptionsǁget__mutmut_orig)
    xǁOptionsǁget__mutmut_orig.__name__ = 'xǁOptionsǁget'

    def xǁOptionsǁget_explicit__mutmut_orig(self, key: str) -> Any:
        """Get the stored value of a specific key and ignore any get-mappings"""

        normalized = self._normalize_key(key)
        return super().get(normalized)

    def xǁOptionsǁget_explicit__mutmut_1(self, key: str) -> Any:
        """Get the stored value of a specific key and ignore any get-mappings"""

        normalized = None
        return super().get(normalized)

    def xǁOptionsǁget_explicit__mutmut_2(self, key: str) -> Any:
        """Get the stored value of a specific key and ignore any get-mappings"""

        normalized = self._normalize_key(None)
        return super().get(normalized)

    def xǁOptionsǁget_explicit__mutmut_3(self, key: str) -> Any:
        """Get the stored value of a specific key and ignore any get-mappings"""

        normalized = self._normalize_key(key)
        return super().get(None)
    
    xǁOptionsǁget_explicit__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOptionsǁget_explicit__mutmut_1': xǁOptionsǁget_explicit__mutmut_1, 
        'xǁOptionsǁget_explicit__mutmut_2': xǁOptionsǁget_explicit__mutmut_2, 
        'xǁOptionsǁget_explicit__mutmut_3': xǁOptionsǁget_explicit__mutmut_3
    }
    
    def get_explicit(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOptionsǁget_explicit__mutmut_orig"), object.__getattribute__(self, "xǁOptionsǁget_explicit__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_explicit.__signature__ = _mutmut_signature(xǁOptionsǁget_explicit__mutmut_orig)
    xǁOptionsǁget_explicit__mutmut_orig.__name__ = 'xǁOptionsǁget_explicit'

    def xǁOptionsǁset__mutmut_orig(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, normalized, value)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_1(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = None
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, normalized, value)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_2(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(None)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, normalized, value)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_3(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = None
        if method is not None:
            method(self, normalized, value)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_4(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(None)
        if method is not None:
            method(self, normalized, value)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_5(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is None:
            method(self, normalized, value)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_6(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(None, normalized, value)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_7(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, None, value)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_8(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, normalized, None)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_9(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(normalized, value)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_10(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, value)
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_11(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, normalized, )
        else:
            super().__setitem__(normalized, value)

    def xǁOptionsǁset__mutmut_12(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, normalized, value)
        else:
            super().__setitem__(None, value)

    def xǁOptionsǁset__mutmut_13(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, normalized, value)
        else:
            super().__setitem__(normalized, None)

    def xǁOptionsǁset__mutmut_14(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, normalized, value)
        else:
            super().__setitem__(value)

    def xǁOptionsǁset__mutmut_15(self, key: str, value: Any) -> None:
        """Set the value for a specific key"""

        normalized = self._normalize_key(key)
        method = self._MAP_SETTERS.get(normalized)
        if method is not None:
            method(self, normalized, value)
        else:
            super().__setitem__(normalized, )
    
    xǁOptionsǁset__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOptionsǁset__mutmut_1': xǁOptionsǁset__mutmut_1, 
        'xǁOptionsǁset__mutmut_2': xǁOptionsǁset__mutmut_2, 
        'xǁOptionsǁset__mutmut_3': xǁOptionsǁset__mutmut_3, 
        'xǁOptionsǁset__mutmut_4': xǁOptionsǁset__mutmut_4, 
        'xǁOptionsǁset__mutmut_5': xǁOptionsǁset__mutmut_5, 
        'xǁOptionsǁset__mutmut_6': xǁOptionsǁset__mutmut_6, 
        'xǁOptionsǁset__mutmut_7': xǁOptionsǁset__mutmut_7, 
        'xǁOptionsǁset__mutmut_8': xǁOptionsǁset__mutmut_8, 
        'xǁOptionsǁset__mutmut_9': xǁOptionsǁset__mutmut_9, 
        'xǁOptionsǁset__mutmut_10': xǁOptionsǁset__mutmut_10, 
        'xǁOptionsǁset__mutmut_11': xǁOptionsǁset__mutmut_11, 
        'xǁOptionsǁset__mutmut_12': xǁOptionsǁset__mutmut_12, 
        'xǁOptionsǁset__mutmut_13': xǁOptionsǁset__mutmut_13, 
        'xǁOptionsǁset__mutmut_14': xǁOptionsǁset__mutmut_14, 
        'xǁOptionsǁset__mutmut_15': xǁOptionsǁset__mutmut_15
    }
    
    def set(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOptionsǁset__mutmut_orig"), object.__getattribute__(self, "xǁOptionsǁset__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set.__signature__ = _mutmut_signature(xǁOptionsǁset__mutmut_orig)
    xǁOptionsǁset__mutmut_orig.__name__ = 'xǁOptionsǁset'

    def xǁOptionsǁset_explicit__mutmut_orig(self, key: str, value: Any) -> None:
        """Set the value for a specific key and ignore any set-mappings"""

        normalized = self._normalize_key(key)
        super().__setitem__(normalized, value)

    def xǁOptionsǁset_explicit__mutmut_1(self, key: str, value: Any) -> None:
        """Set the value for a specific key and ignore any set-mappings"""

        normalized = None
        super().__setitem__(normalized, value)

    def xǁOptionsǁset_explicit__mutmut_2(self, key: str, value: Any) -> None:
        """Set the value for a specific key and ignore any set-mappings"""

        normalized = self._normalize_key(None)
        super().__setitem__(normalized, value)

    def xǁOptionsǁset_explicit__mutmut_3(self, key: str, value: Any) -> None:
        """Set the value for a specific key and ignore any set-mappings"""

        normalized = self._normalize_key(key)
        super().__setitem__(None, value)

    def xǁOptionsǁset_explicit__mutmut_4(self, key: str, value: Any) -> None:
        """Set the value for a specific key and ignore any set-mappings"""

        normalized = self._normalize_key(key)
        super().__setitem__(normalized, None)

    def xǁOptionsǁset_explicit__mutmut_5(self, key: str, value: Any) -> None:
        """Set the value for a specific key and ignore any set-mappings"""

        normalized = self._normalize_key(key)
        super().__setitem__(value)

    def xǁOptionsǁset_explicit__mutmut_6(self, key: str, value: Any) -> None:
        """Set the value for a specific key and ignore any set-mappings"""

        normalized = self._normalize_key(key)
        super().__setitem__(normalized, )
    
    xǁOptionsǁset_explicit__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOptionsǁset_explicit__mutmut_1': xǁOptionsǁset_explicit__mutmut_1, 
        'xǁOptionsǁset_explicit__mutmut_2': xǁOptionsǁset_explicit__mutmut_2, 
        'xǁOptionsǁset_explicit__mutmut_3': xǁOptionsǁset_explicit__mutmut_3, 
        'xǁOptionsǁset_explicit__mutmut_4': xǁOptionsǁset_explicit__mutmut_4, 
        'xǁOptionsǁset_explicit__mutmut_5': xǁOptionsǁset_explicit__mutmut_5, 
        'xǁOptionsǁset_explicit__mutmut_6': xǁOptionsǁset_explicit__mutmut_6
    }
    
    def set_explicit(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOptionsǁset_explicit__mutmut_orig"), object.__getattribute__(self, "xǁOptionsǁset_explicit__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set_explicit.__signature__ = _mutmut_signature(xǁOptionsǁset_explicit__mutmut_orig)
    xǁOptionsǁset_explicit__mutmut_orig.__name__ = 'xǁOptionsǁset_explicit'

    # noinspection PyMethodOverriding
    def xǁOptionsǁupdate__mutmut_orig(self, options: Mapping[str, Any]) -> None:  # type: ignore[override]
        """Merge options"""

        for key, value in options.items():
            self.set(key, value)

    # noinspection PyMethodOverriding
    def xǁOptionsǁupdate__mutmut_1(self, options: Mapping[str, Any]) -> None:  # type: ignore[override]
        """Merge options"""

        for key, value in options.items():
            self.set(None, value)

    # noinspection PyMethodOverriding
    def xǁOptionsǁupdate__mutmut_2(self, options: Mapping[str, Any]) -> None:  # type: ignore[override]
        """Merge options"""

        for key, value in options.items():
            self.set(key, None)

    # noinspection PyMethodOverriding
    def xǁOptionsǁupdate__mutmut_3(self, options: Mapping[str, Any]) -> None:  # type: ignore[override]
        """Merge options"""

        for key, value in options.items():
            self.set(value)

    # noinspection PyMethodOverriding
    def xǁOptionsǁupdate__mutmut_4(self, options: Mapping[str, Any]) -> None:  # type: ignore[override]
        """Merge options"""

        for key, value in options.items():
            self.set(key, )
    
    xǁOptionsǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOptionsǁupdate__mutmut_1': xǁOptionsǁupdate__mutmut_1, 
        'xǁOptionsǁupdate__mutmut_2': xǁOptionsǁupdate__mutmut_2, 
        'xǁOptionsǁupdate__mutmut_3': xǁOptionsǁupdate__mutmut_3, 
        'xǁOptionsǁupdate__mutmut_4': xǁOptionsǁupdate__mutmut_4
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOptionsǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁOptionsǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁOptionsǁupdate__mutmut_orig)
    xǁOptionsǁupdate__mutmut_orig.__name__ = 'xǁOptionsǁupdate'

    def xǁOptionsǁ__getitem____mutmut_orig(self, item):
        return self.get(item)

    def xǁOptionsǁ__getitem____mutmut_1(self, item):
        return self.get(None)
    
    xǁOptionsǁ__getitem____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOptionsǁ__getitem____mutmut_1': xǁOptionsǁ__getitem____mutmut_1
    }
    
    def __getitem__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOptionsǁ__getitem____mutmut_orig"), object.__getattribute__(self, "xǁOptionsǁ__getitem____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __getitem__.__signature__ = _mutmut_signature(xǁOptionsǁ__getitem____mutmut_orig)
    xǁOptionsǁ__getitem____mutmut_orig.__name__ = 'xǁOptionsǁ__getitem__'

    def xǁOptionsǁ__setitem____mutmut_orig(self, item, value):
        return self.set(item, value)

    def xǁOptionsǁ__setitem____mutmut_1(self, item, value):
        return self.set(None, value)

    def xǁOptionsǁ__setitem____mutmut_2(self, item, value):
        return self.set(item, None)

    def xǁOptionsǁ__setitem____mutmut_3(self, item, value):
        return self.set(value)

    def xǁOptionsǁ__setitem____mutmut_4(self, item, value):
        return self.set(item, )
    
    xǁOptionsǁ__setitem____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOptionsǁ__setitem____mutmut_1': xǁOptionsǁ__setitem____mutmut_1, 
        'xǁOptionsǁ__setitem____mutmut_2': xǁOptionsǁ__setitem____mutmut_2, 
        'xǁOptionsǁ__setitem____mutmut_3': xǁOptionsǁ__setitem____mutmut_3, 
        'xǁOptionsǁ__setitem____mutmut_4': xǁOptionsǁ__setitem____mutmut_4
    }
    
    def __setitem__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOptionsǁ__setitem____mutmut_orig"), object.__getattribute__(self, "xǁOptionsǁ__setitem____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __setitem__.__signature__ = _mutmut_signature(xǁOptionsǁ__setitem____mutmut_orig)
    xǁOptionsǁ__setitem____mutmut_orig.__name__ = 'xǁOptionsǁ__setitem__'


_TChoices = TypeVar("_TChoices", bound=Iterable)


class Argument:
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_orig(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_1(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = True,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_2(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = True,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_3(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = None

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_4(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = None
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_5(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = None
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_6(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = None
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_7(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = None
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_8(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_9(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(None) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_10(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = None
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_11(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = None
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_12(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help != argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_13(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = None  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_14(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(None)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_15(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_16(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None or not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_17(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_18(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = None
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_19(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_20(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(None) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_21(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = None
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_22(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(None)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_23(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_24(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None or not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_25(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_26(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_27(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = None
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_28(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = None
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_29(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_30(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(None) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_31(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action != "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_32(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "XXstore_trueXX":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_33(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "STORE_TRUE":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_34(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "Store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_35(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = None
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_36(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = False
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_37(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = None
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_38(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = True if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_39(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is not None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_40(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action != "store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_41(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "XXstore_falseXX":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_42(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "STORE_FALSE":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_43(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "Store_false":
            self.const = False
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_44(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = None
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_45(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = True
            self._default = True if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_46(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = None
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_47(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = False if default is None else default
    # noinspection PyShadowingBuiltins
    def xǁArgumentǁ__init____mutmut_48(
        self,
        name: str,
        # `ArgumentParser.add_argument()` keywords
        action: str | None = None,
        nargs: int | Literal["?", "*", "+"] | None = None,
        const: Any = None,
        default: Any = None,
        type: Callable[[Any], _TChoices | Any] | None = None,  # noqa: A002
        choices: _TChoices | None = None,
        required: bool = False,
        help: str | None = None,  # noqa: A002
        metavar: str | list[str] | tuple[str, ...] | None = None,
        dest: str | None = None,
        # additional `Argument()` keywords
        requires: str | list[str] | tuple[str, ...] | None = None,
        prompt: str | None = None,
        sensitive: bool = False,
        argument_name: str | None = None,
    ):
        """
        Accepts most of the parameters accepted by :meth:`argparse.ArgumentParser.add_argument()`, except that

        - ``name`` is the name relative to the plugin name (can be overridden by ``argument_name``)
          and that only one argument name is supported
        - ``action`` must be a string and can't be a custom :class:`Action <argparse.Action>`
        - ``required`` is a special case which is only enforced if the plugin is in use

        This class should not be instantiated directly.
        See the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator for adding custom plugin arguments.

        :param name: Argument name, without leading ``--`` or plugin name prefixes, e.g. ``"username"``, ``"password"``, etc.
        :param action: See :meth:`ArgumentParser.add_argument()`
        :param nargs: See :meth:`ArgumentParser.add_argument()`
        :param const: See :meth:`ArgumentParser.add_argument()`
        :param default: See :meth:`ArgumentParser.add_argument()`
        :param type: See :meth:`ArgumentParser.add_argument()`
        :param choices: See :meth:`ArgumentParser.add_argument()`
        :param required: See :meth:`ArgumentParser.add_argument()`
        :param help: See :meth:`ArgumentParser.add_argument()`
        :param metavar: See :meth:`ArgumentParser.add_argument()`
        :param dest: See :meth:`ArgumentParser.add_argument()`
        :param requires: List of other arguments which this argument requires, e.g. ``["password"]``
        :param prompt: If the argument is required and not set, then this prompt message will be shown instead
        :param sensitive: Whether the argument is sensitive and should be masked (passwords, etc.)
        :param argument_name: Custom CLI argument name without the automatically added plugin name prefix
        """

        self.name = name

        self.action = action
        self.nargs = nargs
        self.const = const
        self.type = type
        self.choices: tuple[Any, ...] | None = tuple(choices) if choices else None
        self.required = required
        # argparse compares the object identity of argparse.SUPPRESS
        self.help = argparse.SUPPRESS if help == argparse.SUPPRESS else help
        self.metavar: str | tuple[str, ...] | None = (
            tuple(metavar)
            if metavar is not None and not isinstance(metavar, str)
            else metavar
        )  # fmt: skip

        self._default = default
        self._dest = self._normalize_dest(dest) if dest else None

        self.requires: tuple[str, ...] = (
            tuple(requires)
            if requires is not None and not isinstance(requires, str)
            else ((requires,) if requires is not None else ())
        )
        self.prompt = prompt
        self.sensitive = sensitive
        self._argument_name = self._normalize_name(argument_name) if argument_name else None

        # special cases for storing the default value to check whether a plugin argument was set or not
        if action == "store_true":
            self.const = True
            self._default = False if default is None else default
        elif action == "store_false":
            self.const = False
            self._default = True if default is not None else default
    
    xǁArgumentǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentǁ__init____mutmut_1': xǁArgumentǁ__init____mutmut_1, 
        'xǁArgumentǁ__init____mutmut_2': xǁArgumentǁ__init____mutmut_2, 
        'xǁArgumentǁ__init____mutmut_3': xǁArgumentǁ__init____mutmut_3, 
        'xǁArgumentǁ__init____mutmut_4': xǁArgumentǁ__init____mutmut_4, 
        'xǁArgumentǁ__init____mutmut_5': xǁArgumentǁ__init____mutmut_5, 
        'xǁArgumentǁ__init____mutmut_6': xǁArgumentǁ__init____mutmut_6, 
        'xǁArgumentǁ__init____mutmut_7': xǁArgumentǁ__init____mutmut_7, 
        'xǁArgumentǁ__init____mutmut_8': xǁArgumentǁ__init____mutmut_8, 
        'xǁArgumentǁ__init____mutmut_9': xǁArgumentǁ__init____mutmut_9, 
        'xǁArgumentǁ__init____mutmut_10': xǁArgumentǁ__init____mutmut_10, 
        'xǁArgumentǁ__init____mutmut_11': xǁArgumentǁ__init____mutmut_11, 
        'xǁArgumentǁ__init____mutmut_12': xǁArgumentǁ__init____mutmut_12, 
        'xǁArgumentǁ__init____mutmut_13': xǁArgumentǁ__init____mutmut_13, 
        'xǁArgumentǁ__init____mutmut_14': xǁArgumentǁ__init____mutmut_14, 
        'xǁArgumentǁ__init____mutmut_15': xǁArgumentǁ__init____mutmut_15, 
        'xǁArgumentǁ__init____mutmut_16': xǁArgumentǁ__init____mutmut_16, 
        'xǁArgumentǁ__init____mutmut_17': xǁArgumentǁ__init____mutmut_17, 
        'xǁArgumentǁ__init____mutmut_18': xǁArgumentǁ__init____mutmut_18, 
        'xǁArgumentǁ__init____mutmut_19': xǁArgumentǁ__init____mutmut_19, 
        'xǁArgumentǁ__init____mutmut_20': xǁArgumentǁ__init____mutmut_20, 
        'xǁArgumentǁ__init____mutmut_21': xǁArgumentǁ__init____mutmut_21, 
        'xǁArgumentǁ__init____mutmut_22': xǁArgumentǁ__init____mutmut_22, 
        'xǁArgumentǁ__init____mutmut_23': xǁArgumentǁ__init____mutmut_23, 
        'xǁArgumentǁ__init____mutmut_24': xǁArgumentǁ__init____mutmut_24, 
        'xǁArgumentǁ__init____mutmut_25': xǁArgumentǁ__init____mutmut_25, 
        'xǁArgumentǁ__init____mutmut_26': xǁArgumentǁ__init____mutmut_26, 
        'xǁArgumentǁ__init____mutmut_27': xǁArgumentǁ__init____mutmut_27, 
        'xǁArgumentǁ__init____mutmut_28': xǁArgumentǁ__init____mutmut_28, 
        'xǁArgumentǁ__init____mutmut_29': xǁArgumentǁ__init____mutmut_29, 
        'xǁArgumentǁ__init____mutmut_30': xǁArgumentǁ__init____mutmut_30, 
        'xǁArgumentǁ__init____mutmut_31': xǁArgumentǁ__init____mutmut_31, 
        'xǁArgumentǁ__init____mutmut_32': xǁArgumentǁ__init____mutmut_32, 
        'xǁArgumentǁ__init____mutmut_33': xǁArgumentǁ__init____mutmut_33, 
        'xǁArgumentǁ__init____mutmut_34': xǁArgumentǁ__init____mutmut_34, 
        'xǁArgumentǁ__init____mutmut_35': xǁArgumentǁ__init____mutmut_35, 
        'xǁArgumentǁ__init____mutmut_36': xǁArgumentǁ__init____mutmut_36, 
        'xǁArgumentǁ__init____mutmut_37': xǁArgumentǁ__init____mutmut_37, 
        'xǁArgumentǁ__init____mutmut_38': xǁArgumentǁ__init____mutmut_38, 
        'xǁArgumentǁ__init____mutmut_39': xǁArgumentǁ__init____mutmut_39, 
        'xǁArgumentǁ__init____mutmut_40': xǁArgumentǁ__init____mutmut_40, 
        'xǁArgumentǁ__init____mutmut_41': xǁArgumentǁ__init____mutmut_41, 
        'xǁArgumentǁ__init____mutmut_42': xǁArgumentǁ__init____mutmut_42, 
        'xǁArgumentǁ__init____mutmut_43': xǁArgumentǁ__init____mutmut_43, 
        'xǁArgumentǁ__init____mutmut_44': xǁArgumentǁ__init____mutmut_44, 
        'xǁArgumentǁ__init____mutmut_45': xǁArgumentǁ__init____mutmut_45, 
        'xǁArgumentǁ__init____mutmut_46': xǁArgumentǁ__init____mutmut_46, 
        'xǁArgumentǁ__init____mutmut_47': xǁArgumentǁ__init____mutmut_47, 
        'xǁArgumentǁ__init____mutmut_48': xǁArgumentǁ__init____mutmut_48
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁArgumentǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁArgumentǁ__init____mutmut_orig)
    xǁArgumentǁ__init____mutmut_orig.__name__ = 'xǁArgumentǁ__init__'

    @staticmethod
    def _normalize_name(name: str) -> str:
        return name.replace("_", "-").strip("-")

    @staticmethod
    def _normalize_dest(name: str) -> str:
        return name.replace("-", "_")

    def xǁArgumentǁ_name__mutmut_orig(self, plugin):
        return self._argument_name or self._normalize_name(f"{plugin}-{self.name}")

    def xǁArgumentǁ_name__mutmut_1(self, plugin):
        return self._argument_name and self._normalize_name(f"{plugin}-{self.name}")

    def xǁArgumentǁ_name__mutmut_2(self, plugin):
        return self._argument_name or self._normalize_name(None)
    
    xǁArgumentǁ_name__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentǁ_name__mutmut_1': xǁArgumentǁ_name__mutmut_1, 
        'xǁArgumentǁ_name__mutmut_2': xǁArgumentǁ_name__mutmut_2
    }
    
    def _name(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentǁ_name__mutmut_orig"), object.__getattribute__(self, "xǁArgumentǁ_name__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _name.__signature__ = _mutmut_signature(xǁArgumentǁ_name__mutmut_orig)
    xǁArgumentǁ_name__mutmut_orig.__name__ = 'xǁArgumentǁ_name'

    def xǁArgumentǁargument_name__mutmut_orig(self, plugin):
        return f"--{self._name(plugin)}"

    def xǁArgumentǁargument_name__mutmut_1(self, plugin):
        return f"--{self._name(None)}"
    
    xǁArgumentǁargument_name__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentǁargument_name__mutmut_1': xǁArgumentǁargument_name__mutmut_1
    }
    
    def argument_name(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentǁargument_name__mutmut_orig"), object.__getattribute__(self, "xǁArgumentǁargument_name__mutmut_mutants"), args, kwargs, self)
        return result 
    
    argument_name.__signature__ = _mutmut_signature(xǁArgumentǁargument_name__mutmut_orig)
    xǁArgumentǁargument_name__mutmut_orig.__name__ = 'xǁArgumentǁargument_name'

    def xǁArgumentǁnamespace_dest__mutmut_orig(self, plugin):
        return self._normalize_dest(self._name(plugin))

    def xǁArgumentǁnamespace_dest__mutmut_1(self, plugin):
        return self._normalize_dest(None)

    def xǁArgumentǁnamespace_dest__mutmut_2(self, plugin):
        return self._normalize_dest(self._name(None))
    
    xǁArgumentǁnamespace_dest__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentǁnamespace_dest__mutmut_1': xǁArgumentǁnamespace_dest__mutmut_1, 
        'xǁArgumentǁnamespace_dest__mutmut_2': xǁArgumentǁnamespace_dest__mutmut_2
    }
    
    def namespace_dest(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentǁnamespace_dest__mutmut_orig"), object.__getattribute__(self, "xǁArgumentǁnamespace_dest__mutmut_mutants"), args, kwargs, self)
        return result 
    
    namespace_dest.__signature__ = _mutmut_signature(xǁArgumentǁnamespace_dest__mutmut_orig)
    xǁArgumentǁnamespace_dest__mutmut_orig.__name__ = 'xǁArgumentǁnamespace_dest'

    @property
    def dest(self) -> str:
        return self._dest or self._normalize_dest(self.name)

    @property
    def default(self):  # read-only
        return self._default

    # `ArgumentParser.add_argument()` keywords, except `name_or_flags` and `required`
    _ARGPARSE_ARGUMENT_KEYWORDS: ClassVar[Mapping[str, str]] = {
        "action": "action",
        "nargs": "nargs",
        "const": "const",
        "default": "default",
        "type": "type",
        "choices": "choices",
        "help": "help",
        "metavar": "metavar",
        "dest": "_dest",
    }

    @property
    def options(self) -> Mapping[str, Any]:
        return {
            name: getattr(self, attr)
            for name, attr in self._ARGPARSE_ARGUMENT_KEYWORDS.items()
            # don't pass keywords with ``None`` values to ``ArgumentParser.add_argument()``
            if (
                getattr(self, attr) is not None
                # don't include the const option value if the action is store_true or store_false
                and not (name == "const" and self.action in ("store_true", "store_false"))
            )
        }

    def xǁArgumentǁ__hash____mutmut_orig(self):
        return hash((
            self.name,
            self.action,
            self.nargs,
            self.const,
            self.type,
            self.choices,
            self.required,
            self.help,
            self.metavar,
            self._default,
            self._dest,
            self.requires,
            self.prompt,
            self.sensitive,
            self._argument_name,
        ))

    def xǁArgumentǁ__hash____mutmut_1(self):
        return hash(None)
    
    xǁArgumentǁ__hash____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentǁ__hash____mutmut_1': xǁArgumentǁ__hash____mutmut_1
    }
    
    def __hash__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentǁ__hash____mutmut_orig"), object.__getattribute__(self, "xǁArgumentǁ__hash____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __hash__.__signature__ = _mutmut_signature(xǁArgumentǁ__hash____mutmut_orig)
    xǁArgumentǁ__hash____mutmut_orig.__name__ = 'xǁArgumentǁ__hash__'

    def xǁArgumentǁ__eq____mutmut_orig(self, other):
        return isinstance(other, self.__class__) and hash(self) == hash(other)

    def xǁArgumentǁ__eq____mutmut_1(self, other):
        return isinstance(other, self.__class__) or hash(self) == hash(other)

    def xǁArgumentǁ__eq____mutmut_2(self, other):
        return isinstance(other, self.__class__) and hash(None) == hash(other)

    def xǁArgumentǁ__eq____mutmut_3(self, other):
        return isinstance(other, self.__class__) and hash(self) != hash(other)

    def xǁArgumentǁ__eq____mutmut_4(self, other):
        return isinstance(other, self.__class__) and hash(self) == hash(None)
    
    xǁArgumentǁ__eq____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentǁ__eq____mutmut_1': xǁArgumentǁ__eq____mutmut_1, 
        'xǁArgumentǁ__eq____mutmut_2': xǁArgumentǁ__eq____mutmut_2, 
        'xǁArgumentǁ__eq____mutmut_3': xǁArgumentǁ__eq____mutmut_3, 
        'xǁArgumentǁ__eq____mutmut_4': xǁArgumentǁ__eq____mutmut_4
    }
    
    def __eq__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentǁ__eq____mutmut_orig"), object.__getattribute__(self, "xǁArgumentǁ__eq____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __eq__.__signature__ = _mutmut_signature(xǁArgumentǁ__eq____mutmut_orig)
    xǁArgumentǁ__eq____mutmut_orig.__name__ = 'xǁArgumentǁ__eq__'


class Arguments(Dict[str, Argument]):
    """
    A collection of :class:`Argument` instances for :class:`Plugin <streamlink.plugin.Plugin>` classes.

    Should not be called directly, see the :func:`pluginargument <streamlink.plugin.pluginargument>` decorator.
    """

    def xǁArgumentsǁ__init____mutmut_orig(self, *args):
        # keep the initial arguments of the constructor in reverse order (see __iter__())
        super().__init__({arg.name: arg for arg in reversed(args)})

    def xǁArgumentsǁ__init____mutmut_1(self, *args):
        # keep the initial arguments of the constructor in reverse order (see __iter__())
        super().__init__(None)

    def xǁArgumentsǁ__init____mutmut_2(self, *args):
        # keep the initial arguments of the constructor in reverse order (see __iter__())
        super().__init__({arg.name: arg for arg in reversed(None)})
    
    xǁArgumentsǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentsǁ__init____mutmut_1': xǁArgumentsǁ__init____mutmut_1, 
        'xǁArgumentsǁ__init____mutmut_2': xǁArgumentsǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentsǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁArgumentsǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁArgumentsǁ__init____mutmut_orig)
    xǁArgumentsǁ__init____mutmut_orig.__name__ = 'xǁArgumentsǁ__init__'

    def xǁArgumentsǁ__iter____mutmut_orig(self) -> Iterator[Argument]:  # type: ignore[override]
        # iterate in reverse order due to add() being called by multiple pluginargument decorators in reverse order
        return reversed(self.values())

    def xǁArgumentsǁ__iter____mutmut_1(self) -> Iterator[Argument]:  # type: ignore[override]
        # iterate in reverse order due to add() being called by multiple pluginargument decorators in reverse order
        return reversed(None)
    
    xǁArgumentsǁ__iter____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentsǁ__iter____mutmut_1': xǁArgumentsǁ__iter____mutmut_1
    }
    
    def __iter__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentsǁ__iter____mutmut_orig"), object.__getattribute__(self, "xǁArgumentsǁ__iter____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __iter__.__signature__ = _mutmut_signature(xǁArgumentsǁ__iter____mutmut_orig)
    xǁArgumentsǁ__iter____mutmut_orig.__name__ = 'xǁArgumentsǁ__iter__'

    def xǁArgumentsǁ__hash____mutmut_orig(self):
        return hash(tuple(self.items()))

    def xǁArgumentsǁ__hash____mutmut_1(self):
        return hash(None)

    def xǁArgumentsǁ__hash____mutmut_2(self):
        return hash(tuple(None))
    
    xǁArgumentsǁ__hash____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentsǁ__hash____mutmut_1': xǁArgumentsǁ__hash____mutmut_1, 
        'xǁArgumentsǁ__hash____mutmut_2': xǁArgumentsǁ__hash____mutmut_2
    }
    
    def __hash__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentsǁ__hash____mutmut_orig"), object.__getattribute__(self, "xǁArgumentsǁ__hash____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __hash__.__signature__ = _mutmut_signature(xǁArgumentsǁ__hash____mutmut_orig)
    xǁArgumentsǁ__hash____mutmut_orig.__name__ = 'xǁArgumentsǁ__hash__'

    def xǁArgumentsǁ__eq____mutmut_orig(self, other):
        return isinstance(other, self.__class__) and hash(self) == hash(other)

    def xǁArgumentsǁ__eq____mutmut_1(self, other):
        return isinstance(other, self.__class__) or hash(self) == hash(other)

    def xǁArgumentsǁ__eq____mutmut_2(self, other):
        return isinstance(other, self.__class__) and hash(None) == hash(other)

    def xǁArgumentsǁ__eq____mutmut_3(self, other):
        return isinstance(other, self.__class__) and hash(self) != hash(other)

    def xǁArgumentsǁ__eq____mutmut_4(self, other):
        return isinstance(other, self.__class__) and hash(self) == hash(None)
    
    xǁArgumentsǁ__eq____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentsǁ__eq____mutmut_1': xǁArgumentsǁ__eq____mutmut_1, 
        'xǁArgumentsǁ__eq____mutmut_2': xǁArgumentsǁ__eq____mutmut_2, 
        'xǁArgumentsǁ__eq____mutmut_3': xǁArgumentsǁ__eq____mutmut_3, 
        'xǁArgumentsǁ__eq____mutmut_4': xǁArgumentsǁ__eq____mutmut_4
    }
    
    def __eq__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentsǁ__eq____mutmut_orig"), object.__getattribute__(self, "xǁArgumentsǁ__eq____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __eq__.__signature__ = _mutmut_signature(xǁArgumentsǁ__eq____mutmut_orig)
    xǁArgumentsǁ__eq____mutmut_orig.__name__ = 'xǁArgumentsǁ__eq__'

    def xǁArgumentsǁ__ne____mutmut_orig(self, other):
        return not self.__eq__(other)

    def xǁArgumentsǁ__ne____mutmut_1(self, other):
        return self.__eq__(other)

    def xǁArgumentsǁ__ne____mutmut_2(self, other):
        return not self.__eq__(None)
    
    xǁArgumentsǁ__ne____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentsǁ__ne____mutmut_1': xǁArgumentsǁ__ne____mutmut_1, 
        'xǁArgumentsǁ__ne____mutmut_2': xǁArgumentsǁ__ne____mutmut_2
    }
    
    def __ne__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentsǁ__ne____mutmut_orig"), object.__getattribute__(self, "xǁArgumentsǁ__ne____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __ne__.__signature__ = _mutmut_signature(xǁArgumentsǁ__ne____mutmut_orig)
    xǁArgumentsǁ__ne____mutmut_orig.__name__ = 'xǁArgumentsǁ__ne__'

    def xǁArgumentsǁadd__mutmut_orig(self, argument: Argument) -> None:
        self[argument.name] = argument

    def xǁArgumentsǁadd__mutmut_1(self, argument: Argument) -> None:
        self[argument.name] = None
    
    xǁArgumentsǁadd__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentsǁadd__mutmut_1': xǁArgumentsǁadd__mutmut_1
    }
    
    def add(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁArgumentsǁadd__mutmut_orig"), object.__getattribute__(self, "xǁArgumentsǁadd__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add.__signature__ = _mutmut_signature(xǁArgumentsǁadd__mutmut_orig)
    xǁArgumentsǁadd__mutmut_orig.__name__ = 'xǁArgumentsǁadd'

    def xǁArgumentsǁrequires__mutmut_orig(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_1(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = None
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_2(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = None
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_3(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(None)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_4(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = None
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_5(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(None)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_6(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_7(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(None)

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_8(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name not in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_9(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError(None)
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_10(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("XXcycle detected in plugin argument configXX")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_11(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("CYCLE DETECTED IN PLUGIN ARGUMENT CONFIG")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_12(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("Cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_13(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(None)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_14(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(None):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_15(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name not in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_16(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError(None)
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_17(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("XXcycle detected in plugin argument configXX")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_18(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("CYCLE DETECTED IN PLUGIN ARGUMENT CONFIG")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_19(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("Cycle detected in plugin argument config")
                results.add(r.name)
                yield r

    def xǁArgumentsǁrequires__mutmut_20(self, name: str) -> Iterator[Argument]:
        """
        Find all :class:`Argument` instances required by name
        """

        results = {name}
        argument = self.get(name)
        for reqname in argument.requires if argument else []:
            required = self.get(reqname)
            if not required:
                raise KeyError(f"{reqname} is not a valid argument for this plugin")

            if required.name in results:
                raise RuntimeError("cycle detected in plugin argument config")
            results.add(required.name)
            yield required

            for r in self.requires(required.name):
                if r.name in results:
                    raise RuntimeError("cycle detected in plugin argument config")
                results.add(None)
                yield r
    
    xǁArgumentsǁrequires__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁArgumentsǁrequires__mutmut_1': xǁArgumentsǁrequires__mutmut_1, 
        'xǁArgumentsǁrequires__mutmut_2': xǁArgumentsǁrequires__mutmut_2, 
        'xǁArgumentsǁrequires__mutmut_3': xǁArgumentsǁrequires__mutmut_3, 
        'xǁArgumentsǁrequires__mutmut_4': xǁArgumentsǁrequires__mutmut_4, 
        'xǁArgumentsǁrequires__mutmut_5': xǁArgumentsǁrequires__mutmut_5, 
        'xǁArgumentsǁrequires__mutmut_6': xǁArgumentsǁrequires__mutmut_6, 
        'xǁArgumentsǁrequires__mutmut_7': xǁArgumentsǁrequires__mutmut_7, 
        'xǁArgumentsǁrequires__mutmut_8': xǁArgumentsǁrequires__mutmut_8, 
        'xǁArgumentsǁrequires__mutmut_9': xǁArgumentsǁrequires__mutmut_9, 
        'xǁArgumentsǁrequires__mutmut_10': xǁArgumentsǁrequires__mutmut_10, 
        'xǁArgumentsǁrequires__mutmut_11': xǁArgumentsǁrequires__mutmut_11, 
        'xǁArgumentsǁrequires__mutmut_12': xǁArgumentsǁrequires__mutmut_12, 
        'xǁArgumentsǁrequires__mutmut_13': xǁArgumentsǁrequires__mutmut_13, 
        'xǁArgumentsǁrequires__mutmut_14': xǁArgumentsǁrequires__mutmut_14, 
        'xǁArgumentsǁrequires__mutmut_15': xǁArgumentsǁrequires__mutmut_15, 
        'xǁArgumentsǁrequires__mutmut_16': xǁArgumentsǁrequires__mutmut_16, 
        'xǁArgumentsǁrequires__mutmut_17': xǁArgumentsǁrequires__mutmut_17, 
        'xǁArgumentsǁrequires__mutmut_18': xǁArgumentsǁrequires__mutmut_18, 
        'xǁArgumentsǁrequires__mutmut_19': xǁArgumentsǁrequires__mutmut_19, 
        'xǁArgumentsǁrequires__mutmut_20': xǁArgumentsǁrequires__mutmut_20
    }
    
    def requires(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁArgumentsǁrequires__mutmut_orig"), object.__getattribute__(self, "xǁArgumentsǁrequires__mutmut_mutants"), args, kwargs, self)
        return result 
    
    requires.__signature__ = _mutmut_signature(xǁArgumentsǁrequires__mutmut_orig)
    xǁArgumentsǁrequires__mutmut_orig.__name__ = 'xǁArgumentsǁrequires'


__all__ = [
    "Argument",
    "Arguments",
    "Options",
]

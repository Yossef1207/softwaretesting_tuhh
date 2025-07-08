from __future__ import annotations

import io
import json
import logging

from streamlink.session import Streamlink


log = logging.getLogger(__name__)
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


class Stream:
    """
    This is a base class that should be inherited when implementing
    different stream types. Should only be created by plugins.
    """

    __shortname__ = "stream"

    @classmethod
    def shortname(cls):
        return cls.__shortname__

    def xǁStreamǁ__init____mutmut_orig(self, session: Streamlink):
        """
        :param session: Streamlink session instance
        """

        self.session: Streamlink = session

    def xǁStreamǁ__init____mutmut_1(self, session: Streamlink):
        """
        :param session: Streamlink session instance
        """

        self.session: Streamlink = None
    
    xǁStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamǁ__init____mutmut_1': xǁStreamǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStreamǁ__init____mutmut_orig)
    xǁStreamǁ__init____mutmut_orig.__name__ = 'xǁStreamǁ__init__'

    def xǁStreamǁ__repr____mutmut_orig(self):
        params = [repr(self.shortname())]
        for method in self.to_url, self.to_manifest_url:
            try:
                params.append(repr(method()))
            except TypeError:
                pass

        return f"<{self.__class__.__name__} [{', '.join(params)}]>"

    def xǁStreamǁ__repr____mutmut_1(self):
        params = None
        for method in self.to_url, self.to_manifest_url:
            try:
                params.append(repr(method()))
            except TypeError:
                pass

        return f"<{self.__class__.__name__} [{', '.join(params)}]>"

    def xǁStreamǁ__repr____mutmut_2(self):
        params = [repr(None)]
        for method in self.to_url, self.to_manifest_url:
            try:
                params.append(repr(method()))
            except TypeError:
                pass

        return f"<{self.__class__.__name__} [{', '.join(params)}]>"

    def xǁStreamǁ__repr____mutmut_3(self):
        params = [repr(self.shortname())]
        for method in self.to_url, self.to_manifest_url:
            try:
                params.append(None)
            except TypeError:
                pass

        return f"<{self.__class__.__name__} [{', '.join(params)}]>"

    def xǁStreamǁ__repr____mutmut_4(self):
        params = [repr(self.shortname())]
        for method in self.to_url, self.to_manifest_url:
            try:
                params.append(repr(None))
            except TypeError:
                pass

        return f"<{self.__class__.__name__} [{', '.join(params)}]>"

    def xǁStreamǁ__repr____mutmut_5(self):
        params = [repr(self.shortname())]
        for method in self.to_url, self.to_manifest_url:
            try:
                params.append(repr(method()))
            except TypeError:
                pass

        return f"<{self.__class__.__name__} [{', '.join(None)}]>"

    def xǁStreamǁ__repr____mutmut_6(self):
        params = [repr(self.shortname())]
        for method in self.to_url, self.to_manifest_url:
            try:
                params.append(repr(method()))
            except TypeError:
                pass

        return f"<{self.__class__.__name__} [{'XX, XX'.join(params)}]>"
    
    xǁStreamǁ__repr____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamǁ__repr____mutmut_1': xǁStreamǁ__repr____mutmut_1, 
        'xǁStreamǁ__repr____mutmut_2': xǁStreamǁ__repr____mutmut_2, 
        'xǁStreamǁ__repr____mutmut_3': xǁStreamǁ__repr____mutmut_3, 
        'xǁStreamǁ__repr____mutmut_4': xǁStreamǁ__repr____mutmut_4, 
        'xǁStreamǁ__repr____mutmut_5': xǁStreamǁ__repr____mutmut_5, 
        'xǁStreamǁ__repr____mutmut_6': xǁStreamǁ__repr____mutmut_6
    }
    
    def __repr__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamǁ__repr____mutmut_orig"), object.__getattribute__(self, "xǁStreamǁ__repr____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __repr__.__signature__ = _mutmut_signature(xǁStreamǁ__repr____mutmut_orig)
    xǁStreamǁ__repr____mutmut_orig.__name__ = 'xǁStreamǁ__repr__'

    def xǁStreamǁ__json____mutmut_orig(self):  # noqa: PLW3201
        return dict(type=self.shortname())

    def xǁStreamǁ__json____mutmut_1(self):  # noqa: PLW3201
        return dict(typeXX=self.shortname())

    def xǁStreamǁ__json____mutmut_2(self):  # noqa: PLW3201
        return dict(type=None)
    
    xǁStreamǁ__json____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamǁ__json____mutmut_1': xǁStreamǁ__json____mutmut_1, 
        'xǁStreamǁ__json____mutmut_2': xǁStreamǁ__json____mutmut_2
    }
    
    def __json__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamǁ__json____mutmut_orig"), object.__getattribute__(self, "xǁStreamǁ__json____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __json__.__signature__ = _mutmut_signature(xǁStreamǁ__json____mutmut_orig)
    xǁStreamǁ__json____mutmut_orig.__name__ = 'xǁStreamǁ__json__'

    @property
    def json(self):
        obj = self.__json__()
        return json.dumps(obj)

    def xǁStreamǁto_url__mutmut_orig(self):
        raise TypeError(f"<{self.__class__.__name__} [{self.shortname()}]> cannot be translated to a URL")

    def xǁStreamǁto_url__mutmut_1(self):
        raise TypeError(None)
    
    xǁStreamǁto_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamǁto_url__mutmut_1': xǁStreamǁto_url__mutmut_1
    }
    
    def to_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamǁto_url__mutmut_orig"), object.__getattribute__(self, "xǁStreamǁto_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    to_url.__signature__ = _mutmut_signature(xǁStreamǁto_url__mutmut_orig)
    xǁStreamǁto_url__mutmut_orig.__name__ = 'xǁStreamǁto_url'

    def xǁStreamǁto_manifest_url__mutmut_orig(self):
        raise TypeError(f"<{self.__class__.__name__} [{self.shortname()}]> cannot be translated to a manifest URL")

    def xǁStreamǁto_manifest_url__mutmut_1(self):
        raise TypeError(None)
    
    xǁStreamǁto_manifest_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamǁto_manifest_url__mutmut_1': xǁStreamǁto_manifest_url__mutmut_1
    }
    
    def to_manifest_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamǁto_manifest_url__mutmut_orig"), object.__getattribute__(self, "xǁStreamǁto_manifest_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    to_manifest_url.__signature__ = _mutmut_signature(xǁStreamǁto_manifest_url__mutmut_orig)
    xǁStreamǁto_manifest_url__mutmut_orig.__name__ = 'xǁStreamǁto_manifest_url'

    def open(self) -> StreamIO:
        """
        Attempts to open a connection to the stream.
        Returns a file-like object that can be used to read the stream data.

        :raises StreamError: on failure
        """

        raise NotImplementedError


class StreamIO(io.IOBase):
    pass


__all__ = ["Stream", "StreamIO"]

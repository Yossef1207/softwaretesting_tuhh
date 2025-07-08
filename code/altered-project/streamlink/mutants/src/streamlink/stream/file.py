"""
Stream wrapper around a file
"""

from streamlink.stream.stream import Stream
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


class FileStream(Stream):
    __shortname__ = "file"

    def xǁFileStreamǁ__init____mutmut_orig(self, session, path=None, fileobj=None):
        super().__init__(session)
        self.path = path
        self.fileobj = fileobj
        if not self.path and not self.fileobj:
            raise ValueError("path or fileobj must be set")

    def xǁFileStreamǁ__init____mutmut_1(self, session, path=None, fileobj=None):
        super().__init__(None)
        self.path = path
        self.fileobj = fileobj
        if not self.path and not self.fileobj:
            raise ValueError("path or fileobj must be set")

    def xǁFileStreamǁ__init____mutmut_2(self, session, path=None, fileobj=None):
        super().__init__(session)
        self.path = None
        self.fileobj = fileobj
        if not self.path and not self.fileobj:
            raise ValueError("path or fileobj must be set")

    def xǁFileStreamǁ__init____mutmut_3(self, session, path=None, fileobj=None):
        super().__init__(session)
        self.path = path
        self.fileobj = None
        if not self.path and not self.fileobj:
            raise ValueError("path or fileobj must be set")

    def xǁFileStreamǁ__init____mutmut_4(self, session, path=None, fileobj=None):
        super().__init__(session)
        self.path = path
        self.fileobj = fileobj
        if self.path and not self.fileobj:
            raise ValueError("path or fileobj must be set")

    def xǁFileStreamǁ__init____mutmut_5(self, session, path=None, fileobj=None):
        super().__init__(session)
        self.path = path
        self.fileobj = fileobj
        if not self.path or not self.fileobj:
            raise ValueError("path or fileobj must be set")

    def xǁFileStreamǁ__init____mutmut_6(self, session, path=None, fileobj=None):
        super().__init__(session)
        self.path = path
        self.fileobj = fileobj
        if not self.path and self.fileobj:
            raise ValueError("path or fileobj must be set")

    def xǁFileStreamǁ__init____mutmut_7(self, session, path=None, fileobj=None):
        super().__init__(session)
        self.path = path
        self.fileobj = fileobj
        if not self.path and not self.fileobj:
            raise ValueError(None)

    def xǁFileStreamǁ__init____mutmut_8(self, session, path=None, fileobj=None):
        super().__init__(session)
        self.path = path
        self.fileobj = fileobj
        if not self.path and not self.fileobj:
            raise ValueError("XXpath or fileobj must be setXX")

    def xǁFileStreamǁ__init____mutmut_9(self, session, path=None, fileobj=None):
        super().__init__(session)
        self.path = path
        self.fileobj = fileobj
        if not self.path and not self.fileobj:
            raise ValueError("PATH OR FILEOBJ MUST BE SET")

    def xǁFileStreamǁ__init____mutmut_10(self, session, path=None, fileobj=None):
        super().__init__(session)
        self.path = path
        self.fileobj = fileobj
        if not self.path and not self.fileobj:
            raise ValueError("Path or fileobj must be set")
    
    xǁFileStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileStreamǁ__init____mutmut_1': xǁFileStreamǁ__init____mutmut_1, 
        'xǁFileStreamǁ__init____mutmut_2': xǁFileStreamǁ__init____mutmut_2, 
        'xǁFileStreamǁ__init____mutmut_3': xǁFileStreamǁ__init____mutmut_3, 
        'xǁFileStreamǁ__init____mutmut_4': xǁFileStreamǁ__init____mutmut_4, 
        'xǁFileStreamǁ__init____mutmut_5': xǁFileStreamǁ__init____mutmut_5, 
        'xǁFileStreamǁ__init____mutmut_6': xǁFileStreamǁ__init____mutmut_6, 
        'xǁFileStreamǁ__init____mutmut_7': xǁFileStreamǁ__init____mutmut_7, 
        'xǁFileStreamǁ__init____mutmut_8': xǁFileStreamǁ__init____mutmut_8, 
        'xǁFileStreamǁ__init____mutmut_9': xǁFileStreamǁ__init____mutmut_9, 
        'xǁFileStreamǁ__init____mutmut_10': xǁFileStreamǁ__init____mutmut_10
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁFileStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁFileStreamǁ__init____mutmut_orig)
    xǁFileStreamǁ__init____mutmut_orig.__name__ = 'xǁFileStreamǁ__init__'

    def xǁFileStreamǁ__json____mutmut_orig(self):  # noqa: PLW3201
        json = super().__json__()

        if self.path:
            json["path"] = self.path

        return json

    def xǁFileStreamǁ__json____mutmut_1(self):  # noqa: PLW3201
        json = None

        if self.path:
            json["path"] = self.path

        return json

    def xǁFileStreamǁ__json____mutmut_2(self):  # noqa: PLW3201
        json = super().__json__()

        if self.path:
            json["path"] = None

        return json

    def xǁFileStreamǁ__json____mutmut_3(self):  # noqa: PLW3201
        json = super().__json__()

        if self.path:
            json["XXpathXX"] = self.path

        return json

    def xǁFileStreamǁ__json____mutmut_4(self):  # noqa: PLW3201
        json = super().__json__()

        if self.path:
            json["PATH"] = self.path

        return json

    def xǁFileStreamǁ__json____mutmut_5(self):  # noqa: PLW3201
        json = super().__json__()

        if self.path:
            json["Path"] = self.path

        return json
    
    xǁFileStreamǁ__json____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileStreamǁ__json____mutmut_1': xǁFileStreamǁ__json____mutmut_1, 
        'xǁFileStreamǁ__json____mutmut_2': xǁFileStreamǁ__json____mutmut_2, 
        'xǁFileStreamǁ__json____mutmut_3': xǁFileStreamǁ__json____mutmut_3, 
        'xǁFileStreamǁ__json____mutmut_4': xǁFileStreamǁ__json____mutmut_4, 
        'xǁFileStreamǁ__json____mutmut_5': xǁFileStreamǁ__json____mutmut_5
    }
    
    def __json__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileStreamǁ__json____mutmut_orig"), object.__getattribute__(self, "xǁFileStreamǁ__json____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __json__.__signature__ = _mutmut_signature(xǁFileStreamǁ__json____mutmut_orig)
    xǁFileStreamǁ__json____mutmut_orig.__name__ = 'xǁFileStreamǁ__json__'

    def xǁFileStreamǁto_url__mutmut_orig(self):
        if self.path is None:
            return super().to_url()

        return self.path

    def xǁFileStreamǁto_url__mutmut_1(self):
        if self.path is not None:
            return super().to_url()

        return self.path
    
    xǁFileStreamǁto_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileStreamǁto_url__mutmut_1': xǁFileStreamǁto_url__mutmut_1
    }
    
    def to_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileStreamǁto_url__mutmut_orig"), object.__getattribute__(self, "xǁFileStreamǁto_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    to_url.__signature__ = _mutmut_signature(xǁFileStreamǁto_url__mutmut_orig)
    xǁFileStreamǁto_url__mutmut_orig.__name__ = 'xǁFileStreamǁto_url'

    def xǁFileStreamǁopen__mutmut_orig(self):
        return self.fileobj or open(self.path, "rb")

    def xǁFileStreamǁopen__mutmut_1(self):
        return self.fileobj and open(self.path, "rb")

    def xǁFileStreamǁopen__mutmut_2(self):
        return self.fileobj or open(None, "rb")

    def xǁFileStreamǁopen__mutmut_3(self):
        return self.fileobj or open(self.path, None)

    def xǁFileStreamǁopen__mutmut_4(self):
        return self.fileobj or open("rb")

    def xǁFileStreamǁopen__mutmut_5(self):
        return self.fileobj or open(self.path, )

    def xǁFileStreamǁopen__mutmut_6(self):
        return self.fileobj or open(self.path, "XXrbXX")

    def xǁFileStreamǁopen__mutmut_7(self):
        return self.fileobj or open(self.path, "RB")

    def xǁFileStreamǁopen__mutmut_8(self):
        return self.fileobj or open(self.path, "Rb")
    
    xǁFileStreamǁopen__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileStreamǁopen__mutmut_1': xǁFileStreamǁopen__mutmut_1, 
        'xǁFileStreamǁopen__mutmut_2': xǁFileStreamǁopen__mutmut_2, 
        'xǁFileStreamǁopen__mutmut_3': xǁFileStreamǁopen__mutmut_3, 
        'xǁFileStreamǁopen__mutmut_4': xǁFileStreamǁopen__mutmut_4, 
        'xǁFileStreamǁopen__mutmut_5': xǁFileStreamǁopen__mutmut_5, 
        'xǁFileStreamǁopen__mutmut_6': xǁFileStreamǁopen__mutmut_6, 
        'xǁFileStreamǁopen__mutmut_7': xǁFileStreamǁopen__mutmut_7, 
        'xǁFileStreamǁopen__mutmut_8': xǁFileStreamǁopen__mutmut_8
    }
    
    def open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileStreamǁopen__mutmut_orig"), object.__getattribute__(self, "xǁFileStreamǁopen__mutmut_mutants"), args, kwargs, self)
        return result 
    
    open.__signature__ = _mutmut_signature(xǁFileStreamǁopen__mutmut_orig)
    xǁFileStreamǁopen__mutmut_orig.__name__ = 'xǁFileStreamǁopen'

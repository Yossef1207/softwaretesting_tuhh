"""
$description Ukrainian live TV channels from 1 + 1 Media group, including 1 + 1, 2 + 2, PLUSPLUS, TET and UNIAN.
$url 1plus1.video
$type live
"""

import logging
import re
from base64 import b64decode
from time import time
from urllib.parse import urljoin, urlparse

from streamlink.exceptions import NoStreamsError, PluginError
from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream
from streamlink.utils.times import fromlocaltimestamp


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


class OnePlusOneHLS(HLSStream):
    __shortname__ = "hls-oneplusone"

    def xǁOnePlusOneHLSǁ__init____mutmut_orig(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_1(self, session, url, self_url=None, **args):
        super().__init__(None, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_2(self, session, url, self_url=None, **args):
        super().__init__(session, None, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_3(self, session, url, self_url=None, **args):
        super().__init__(url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_4(self, session, url, self_url=None, **args):
        super().__init__(session, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_5(self, session, url, self_url=None, **args):
        super().__init__(session, url, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_6(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, )
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_7(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = None

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_8(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = None
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_9(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(None)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_10(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = None
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_11(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = None
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_12(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split(None)[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_13(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.rsplit("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_14(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("XX/XX")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_15(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[+1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_16(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-2]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_17(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = None
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_18(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(None) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_19(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split(None)[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_20(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.rsplit("/")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_21(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("XX/XX")[2]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_22(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[3]) - 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_23(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) + 15
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_24(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 16
        self.api = OnePlusOneAPI(session, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_25(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = None

    def xǁOnePlusOneHLSǁ__init____mutmut_26(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(None, self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_27(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, None)

    def xǁOnePlusOneHLSǁ__init____mutmut_28(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(self_url)

    def xǁOnePlusOneHLSǁ__init____mutmut_29(self, session, url, self_url=None, **args):
        super().__init__(session, url, None, **args)
        self._url = url

        first_parsed = urlparse(self._url)
        self._first_netloc = first_parsed.netloc
        self._first_path_chunklist = first_parsed.path.split("/")[-1]
        self.watch_timeout = int(first_parsed.path.split("/")[2]) - 15
        self.api = OnePlusOneAPI(session, )
    
    xǁOnePlusOneHLSǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOnePlusOneHLSǁ__init____mutmut_1': xǁOnePlusOneHLSǁ__init____mutmut_1, 
        'xǁOnePlusOneHLSǁ__init____mutmut_2': xǁOnePlusOneHLSǁ__init____mutmut_2, 
        'xǁOnePlusOneHLSǁ__init____mutmut_3': xǁOnePlusOneHLSǁ__init____mutmut_3, 
        'xǁOnePlusOneHLSǁ__init____mutmut_4': xǁOnePlusOneHLSǁ__init____mutmut_4, 
        'xǁOnePlusOneHLSǁ__init____mutmut_5': xǁOnePlusOneHLSǁ__init____mutmut_5, 
        'xǁOnePlusOneHLSǁ__init____mutmut_6': xǁOnePlusOneHLSǁ__init____mutmut_6, 
        'xǁOnePlusOneHLSǁ__init____mutmut_7': xǁOnePlusOneHLSǁ__init____mutmut_7, 
        'xǁOnePlusOneHLSǁ__init____mutmut_8': xǁOnePlusOneHLSǁ__init____mutmut_8, 
        'xǁOnePlusOneHLSǁ__init____mutmut_9': xǁOnePlusOneHLSǁ__init____mutmut_9, 
        'xǁOnePlusOneHLSǁ__init____mutmut_10': xǁOnePlusOneHLSǁ__init____mutmut_10, 
        'xǁOnePlusOneHLSǁ__init____mutmut_11': xǁOnePlusOneHLSǁ__init____mutmut_11, 
        'xǁOnePlusOneHLSǁ__init____mutmut_12': xǁOnePlusOneHLSǁ__init____mutmut_12, 
        'xǁOnePlusOneHLSǁ__init____mutmut_13': xǁOnePlusOneHLSǁ__init____mutmut_13, 
        'xǁOnePlusOneHLSǁ__init____mutmut_14': xǁOnePlusOneHLSǁ__init____mutmut_14, 
        'xǁOnePlusOneHLSǁ__init____mutmut_15': xǁOnePlusOneHLSǁ__init____mutmut_15, 
        'xǁOnePlusOneHLSǁ__init____mutmut_16': xǁOnePlusOneHLSǁ__init____mutmut_16, 
        'xǁOnePlusOneHLSǁ__init____mutmut_17': xǁOnePlusOneHLSǁ__init____mutmut_17, 
        'xǁOnePlusOneHLSǁ__init____mutmut_18': xǁOnePlusOneHLSǁ__init____mutmut_18, 
        'xǁOnePlusOneHLSǁ__init____mutmut_19': xǁOnePlusOneHLSǁ__init____mutmut_19, 
        'xǁOnePlusOneHLSǁ__init____mutmut_20': xǁOnePlusOneHLSǁ__init____mutmut_20, 
        'xǁOnePlusOneHLSǁ__init____mutmut_21': xǁOnePlusOneHLSǁ__init____mutmut_21, 
        'xǁOnePlusOneHLSǁ__init____mutmut_22': xǁOnePlusOneHLSǁ__init____mutmut_22, 
        'xǁOnePlusOneHLSǁ__init____mutmut_23': xǁOnePlusOneHLSǁ__init____mutmut_23, 
        'xǁOnePlusOneHLSǁ__init____mutmut_24': xǁOnePlusOneHLSǁ__init____mutmut_24, 
        'xǁOnePlusOneHLSǁ__init____mutmut_25': xǁOnePlusOneHLSǁ__init____mutmut_25, 
        'xǁOnePlusOneHLSǁ__init____mutmut_26': xǁOnePlusOneHLSǁ__init____mutmut_26, 
        'xǁOnePlusOneHLSǁ__init____mutmut_27': xǁOnePlusOneHLSǁ__init____mutmut_27, 
        'xǁOnePlusOneHLSǁ__init____mutmut_28': xǁOnePlusOneHLSǁ__init____mutmut_28, 
        'xǁOnePlusOneHLSǁ__init____mutmut_29': xǁOnePlusOneHLSǁ__init____mutmut_29
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOnePlusOneHLSǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁOnePlusOneHLSǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁOnePlusOneHLSǁ__init____mutmut_orig)
    xǁOnePlusOneHLSǁ__init____mutmut_orig.__name__ = 'xǁOnePlusOneHLSǁ__init__'

    def xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_orig(self):
        when = fromlocaltimestamp(self.watch_timeout).isoformat(" ")
        log.debug(f"next watch_timeout at {when}")

    def xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_1(self):
        when = None
        log.debug(f"next watch_timeout at {when}")

    def xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_2(self):
        when = fromlocaltimestamp(self.watch_timeout).isoformat(None)
        log.debug(f"next watch_timeout at {when}")

    def xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_3(self):
        when = fromlocaltimestamp(None).isoformat(" ")
        log.debug(f"next watch_timeout at {when}")

    def xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_4(self):
        when = fromlocaltimestamp(self.watch_timeout).isoformat("XX XX")
        log.debug(f"next watch_timeout at {when}")

    def xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_5(self):
        when = fromlocaltimestamp(self.watch_timeout).isoformat(" ")
        log.debug(None)
    
    xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_1': xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_1, 
        'xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_2': xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_2, 
        'xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_3': xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_3, 
        'xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_4': xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_4, 
        'xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_5': xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_5
    }
    
    def _next_watch_timeout(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_orig"), object.__getattribute__(self, "xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _next_watch_timeout.__signature__ = _mutmut_signature(xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_orig)
    xǁOnePlusOneHLSǁ_next_watch_timeout__mutmut_orig.__name__ = 'xǁOnePlusOneHLSǁ_next_watch_timeout'

    def open(self):
        self._next_watch_timeout()
        return super().open()

    @property
    def url(self):
        if int(time()) >= self.watch_timeout:
            log.debug("Reloading HLS URL")
            hls_url = self.api.get_hls_url()
            if not hls_url:
                self.watch_timeout += 10
                return self._url
            parsed = urlparse(hls_url)
            path_parts = parsed.path.split("/")
            path_parts[-1] = self._first_path_chunklist
            self.watch_timeout = int(path_parts[2]) - 15
            self._next_watch_timeout()

            self._url = parsed._replace(
                netloc=self._first_netloc,
                path="/".join(list(path_parts)),
            ).geturl()
        return self._url


class OnePlusOneAPI:
    def xǁOnePlusOneAPIǁ__init____mutmut_orig(self, session, url):
        self.session = session
        self.url = url
    def xǁOnePlusOneAPIǁ__init____mutmut_1(self, session, url):
        self.session = None
        self.url = url
    def xǁOnePlusOneAPIǁ__init____mutmut_2(self, session, url):
        self.session = session
        self.url = None
    
    xǁOnePlusOneAPIǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOnePlusOneAPIǁ__init____mutmut_1': xǁOnePlusOneAPIǁ__init____mutmut_1, 
        'xǁOnePlusOneAPIǁ__init____mutmut_2': xǁOnePlusOneAPIǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOnePlusOneAPIǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁOnePlusOneAPIǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁOnePlusOneAPIǁ__init____mutmut_orig)
    xǁOnePlusOneAPIǁ__init____mutmut_orig.__name__ = 'xǁOnePlusOneAPIǁ__init__'

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_orig(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_1(self):
        self.session.http.cookies.clear()
        url_parts = None
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_2(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=None,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_3(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=None,
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_4(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_5(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_6(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                None,
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_7(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                None,
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_8(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_9(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_10(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(None),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_11(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string("XX.//iframe[contains(@src,'embed')]/@srcXX"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_12(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//IFRAME[CONTAINS(@SRC,'EMBED')]/@SRC"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_13(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_14(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(None)
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_15(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update(None)

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_16(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"XXRefererXX": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_17(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_18(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"REFERER": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_19(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = None
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_20(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=None,
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_21(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=None,
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_22(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_23(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_24(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(None, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_25(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, None),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_26(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_27(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, ),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_28(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    None,
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_29(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    None,
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_30(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    None,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_31(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    None,
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_32(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    None,
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_33(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    None,
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_34(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    None,
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_35(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    None,
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_36(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    None,
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_37(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_38(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_39(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_40(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_41(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_42(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_43(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_44(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_45(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_46(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(None),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_47(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string("XX.//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()XX"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_48(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//SCRIPT[@TYPE='TEXT/JAVASCRIPT'][CONTAINS(TEXT(),'OVVA-PLAYER')]/TEXT()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_49(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(None),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_50(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(None)),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_51(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"XXovva-player\",\"([^\"]*)\"\)XX")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_52(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_53(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"OVVA-PLAYER\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_54(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"Ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_55(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(None),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_56(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(2),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_57(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(None),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_58(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: None),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_59(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(None).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_60(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"XXbalancerXX": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_61(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"BALANCER": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_62(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"Balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_63(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get(None),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_64(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("XXbalancerXX"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_65(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("BALANCER"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_66(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("Balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_67(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(None)
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_68(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(None)
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_69(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=None,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_70(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=None,
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_71(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_72(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_73(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                None,
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_74(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                None,
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_75(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                None,
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_76(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_77(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_78(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_79(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(None),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_80(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: None),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_81(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split(None)),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_82(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.rsplit("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_83(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("XX=XX")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_84(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["XX302XX", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_85(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=None)],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_86(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(None))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_87(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith("XX.m3u8XX"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_88(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".M3U8"))],
                validate.get(1),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_89(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(None),
            ),
        )

    def xǁOnePlusOneAPIǁget_hls_url__mutmut_90(self):
        self.session.http.cookies.clear()
        url_parts = self.session.http.get(
            url=self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'embed')]/@src"),
            ),
        )
        if not url_parts:
            raise NoStreamsError

        log.trace(f"url_parts={url_parts}")
        self.session.http.headers.update({"Referer": self.url})

        try:
            url_ovva = self.session.http.get(
                url=urljoin(self.url, url_parts),
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//script[@type='text/javascript'][contains(text(),'ovva-player')]/text()"),
                    str,
                    validate.regex(re.compile(r"ovva-player\",\"([^\"]*)\"\)")),
                    validate.get(1),
                    validate.transform(lambda x: b64decode(x).decode()),
                    validate.parse_json(),
                    {"balancer": validate.url()},
                    validate.get("balancer"),
                ),
            )
        except PluginError as err:
            log.error(f"ovva-player: {err}")
            return

        log.debug(f"url_ovva={url_ovva}")
        return self.session.http.get(
            url=url_ovva,
            schema=validate.Schema(
                validate.transform(lambda x: x.split("=")),
                ["302", validate.url(path=validate.endswith(".m3u8"))],
                validate.get(2),
            ),
        )
    
    xǁOnePlusOneAPIǁget_hls_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁOnePlusOneAPIǁget_hls_url__mutmut_1': xǁOnePlusOneAPIǁget_hls_url__mutmut_1, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_2': xǁOnePlusOneAPIǁget_hls_url__mutmut_2, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_3': xǁOnePlusOneAPIǁget_hls_url__mutmut_3, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_4': xǁOnePlusOneAPIǁget_hls_url__mutmut_4, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_5': xǁOnePlusOneAPIǁget_hls_url__mutmut_5, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_6': xǁOnePlusOneAPIǁget_hls_url__mutmut_6, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_7': xǁOnePlusOneAPIǁget_hls_url__mutmut_7, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_8': xǁOnePlusOneAPIǁget_hls_url__mutmut_8, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_9': xǁOnePlusOneAPIǁget_hls_url__mutmut_9, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_10': xǁOnePlusOneAPIǁget_hls_url__mutmut_10, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_11': xǁOnePlusOneAPIǁget_hls_url__mutmut_11, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_12': xǁOnePlusOneAPIǁget_hls_url__mutmut_12, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_13': xǁOnePlusOneAPIǁget_hls_url__mutmut_13, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_14': xǁOnePlusOneAPIǁget_hls_url__mutmut_14, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_15': xǁOnePlusOneAPIǁget_hls_url__mutmut_15, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_16': xǁOnePlusOneAPIǁget_hls_url__mutmut_16, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_17': xǁOnePlusOneAPIǁget_hls_url__mutmut_17, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_18': xǁOnePlusOneAPIǁget_hls_url__mutmut_18, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_19': xǁOnePlusOneAPIǁget_hls_url__mutmut_19, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_20': xǁOnePlusOneAPIǁget_hls_url__mutmut_20, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_21': xǁOnePlusOneAPIǁget_hls_url__mutmut_21, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_22': xǁOnePlusOneAPIǁget_hls_url__mutmut_22, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_23': xǁOnePlusOneAPIǁget_hls_url__mutmut_23, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_24': xǁOnePlusOneAPIǁget_hls_url__mutmut_24, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_25': xǁOnePlusOneAPIǁget_hls_url__mutmut_25, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_26': xǁOnePlusOneAPIǁget_hls_url__mutmut_26, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_27': xǁOnePlusOneAPIǁget_hls_url__mutmut_27, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_28': xǁOnePlusOneAPIǁget_hls_url__mutmut_28, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_29': xǁOnePlusOneAPIǁget_hls_url__mutmut_29, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_30': xǁOnePlusOneAPIǁget_hls_url__mutmut_30, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_31': xǁOnePlusOneAPIǁget_hls_url__mutmut_31, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_32': xǁOnePlusOneAPIǁget_hls_url__mutmut_32, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_33': xǁOnePlusOneAPIǁget_hls_url__mutmut_33, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_34': xǁOnePlusOneAPIǁget_hls_url__mutmut_34, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_35': xǁOnePlusOneAPIǁget_hls_url__mutmut_35, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_36': xǁOnePlusOneAPIǁget_hls_url__mutmut_36, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_37': xǁOnePlusOneAPIǁget_hls_url__mutmut_37, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_38': xǁOnePlusOneAPIǁget_hls_url__mutmut_38, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_39': xǁOnePlusOneAPIǁget_hls_url__mutmut_39, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_40': xǁOnePlusOneAPIǁget_hls_url__mutmut_40, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_41': xǁOnePlusOneAPIǁget_hls_url__mutmut_41, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_42': xǁOnePlusOneAPIǁget_hls_url__mutmut_42, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_43': xǁOnePlusOneAPIǁget_hls_url__mutmut_43, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_44': xǁOnePlusOneAPIǁget_hls_url__mutmut_44, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_45': xǁOnePlusOneAPIǁget_hls_url__mutmut_45, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_46': xǁOnePlusOneAPIǁget_hls_url__mutmut_46, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_47': xǁOnePlusOneAPIǁget_hls_url__mutmut_47, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_48': xǁOnePlusOneAPIǁget_hls_url__mutmut_48, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_49': xǁOnePlusOneAPIǁget_hls_url__mutmut_49, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_50': xǁOnePlusOneAPIǁget_hls_url__mutmut_50, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_51': xǁOnePlusOneAPIǁget_hls_url__mutmut_51, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_52': xǁOnePlusOneAPIǁget_hls_url__mutmut_52, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_53': xǁOnePlusOneAPIǁget_hls_url__mutmut_53, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_54': xǁOnePlusOneAPIǁget_hls_url__mutmut_54, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_55': xǁOnePlusOneAPIǁget_hls_url__mutmut_55, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_56': xǁOnePlusOneAPIǁget_hls_url__mutmut_56, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_57': xǁOnePlusOneAPIǁget_hls_url__mutmut_57, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_58': xǁOnePlusOneAPIǁget_hls_url__mutmut_58, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_59': xǁOnePlusOneAPIǁget_hls_url__mutmut_59, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_60': xǁOnePlusOneAPIǁget_hls_url__mutmut_60, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_61': xǁOnePlusOneAPIǁget_hls_url__mutmut_61, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_62': xǁOnePlusOneAPIǁget_hls_url__mutmut_62, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_63': xǁOnePlusOneAPIǁget_hls_url__mutmut_63, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_64': xǁOnePlusOneAPIǁget_hls_url__mutmut_64, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_65': xǁOnePlusOneAPIǁget_hls_url__mutmut_65, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_66': xǁOnePlusOneAPIǁget_hls_url__mutmut_66, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_67': xǁOnePlusOneAPIǁget_hls_url__mutmut_67, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_68': xǁOnePlusOneAPIǁget_hls_url__mutmut_68, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_69': xǁOnePlusOneAPIǁget_hls_url__mutmut_69, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_70': xǁOnePlusOneAPIǁget_hls_url__mutmut_70, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_71': xǁOnePlusOneAPIǁget_hls_url__mutmut_71, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_72': xǁOnePlusOneAPIǁget_hls_url__mutmut_72, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_73': xǁOnePlusOneAPIǁget_hls_url__mutmut_73, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_74': xǁOnePlusOneAPIǁget_hls_url__mutmut_74, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_75': xǁOnePlusOneAPIǁget_hls_url__mutmut_75, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_76': xǁOnePlusOneAPIǁget_hls_url__mutmut_76, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_77': xǁOnePlusOneAPIǁget_hls_url__mutmut_77, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_78': xǁOnePlusOneAPIǁget_hls_url__mutmut_78, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_79': xǁOnePlusOneAPIǁget_hls_url__mutmut_79, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_80': xǁOnePlusOneAPIǁget_hls_url__mutmut_80, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_81': xǁOnePlusOneAPIǁget_hls_url__mutmut_81, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_82': xǁOnePlusOneAPIǁget_hls_url__mutmut_82, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_83': xǁOnePlusOneAPIǁget_hls_url__mutmut_83, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_84': xǁOnePlusOneAPIǁget_hls_url__mutmut_84, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_85': xǁOnePlusOneAPIǁget_hls_url__mutmut_85, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_86': xǁOnePlusOneAPIǁget_hls_url__mutmut_86, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_87': xǁOnePlusOneAPIǁget_hls_url__mutmut_87, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_88': xǁOnePlusOneAPIǁget_hls_url__mutmut_88, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_89': xǁOnePlusOneAPIǁget_hls_url__mutmut_89, 
        'xǁOnePlusOneAPIǁget_hls_url__mutmut_90': xǁOnePlusOneAPIǁget_hls_url__mutmut_90
    }
    
    def get_hls_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁOnePlusOneAPIǁget_hls_url__mutmut_orig"), object.__getattribute__(self, "xǁOnePlusOneAPIǁget_hls_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_hls_url.__signature__ = _mutmut_signature(xǁOnePlusOneAPIǁget_hls_url__mutmut_orig)
    xǁOnePlusOneAPIǁget_hls_url__mutmut_orig.__name__ = 'xǁOnePlusOneAPIǁget_hls_url'


@pluginmatcher(
    re.compile(r"https?://1plus1\.video/(?:\w{2}/)?tvguide/[^/]+/online"),
)
class OnePlusOne(Plugin):
    def _get_streams(self):
        self.api = OnePlusOneAPI(self.session, self.url)
        url_hls = self.api.get_hls_url()
        if not url_hls:
            return
        for q, s in HLSStream.parse_variant_playlist(self.session, url_hls).items():
            yield q, OnePlusOneHLS(self.session, s.url, self_url=self.url)


__plugin__ = OnePlusOne

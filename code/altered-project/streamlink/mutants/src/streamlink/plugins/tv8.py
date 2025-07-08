"""
$description Turkish live TV channel owned by Acun Medya Group.
$url tv8.com.tr
$type live
"""

import logging
import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream, HLSStreamReader, HLSStreamWriter


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


class TV8HLSStreamWriter(HLSStreamWriter):
    ad_re = re.compile(r"/ad/|/crea/")

    def xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_orig(self, segment):
        return self.ad_re.search(segment.uri) is not None or super().should_filter_segment(segment)

    def xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_1(self, segment):
        return self.ad_re.search(None) is not None or super().should_filter_segment(segment)

    def xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_2(self, segment):
        return self.ad_re.search(segment.uri) is None or super().should_filter_segment(segment)

    def xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_3(self, segment):
        return self.ad_re.search(segment.uri) is not None and super().should_filter_segment(segment)

    def xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_4(self, segment):
        return self.ad_re.search(segment.uri) is not None or super().should_filter_segment(None)
    
    xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_1': xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_1, 
        'xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_2': xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_2, 
        'xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_3': xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_3, 
        'xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_4': xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_4
    }
    
    def should_filter_segment(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_orig"), object.__getattribute__(self, "xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_mutants"), args, kwargs, self)
        return result 
    
    should_filter_segment.__signature__ = _mutmut_signature(xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_orig)
    xǁTV8HLSStreamWriterǁshould_filter_segment__mutmut_orig.__name__ = 'xǁTV8HLSStreamWriterǁshould_filter_segment'


class TV8HLSStreamReader(HLSStreamReader):
    __writer__ = TV8HLSStreamWriter


class TV8HLSStream(HLSStream):
    __reader__ = TV8HLSStreamReader


@pluginmatcher(
    re.compile(r"https?://www\.tv8\.com\.tr/canli-yayin"),
)
class TV8(Plugin):
    def _get_streams(self):
        hls_url = self.session.http.get(
            self.url,
            schema=validate.Schema(
                re.compile(r"""var\s+videoUrl\s*=\s*(?P<q>["'])(?P<hls_url>https?://.*?\.m3u8.*?)(?P=q)"""),
                validate.any(None, validate.get("hls_url")),
            ),
        )
        if hls_url is not None:
            return TV8HLSStream.parse_variant_playlist(self.session, hls_url)


__plugin__ = TV8

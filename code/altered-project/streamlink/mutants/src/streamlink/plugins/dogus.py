"""
$description Turkish live TV channels from Dogus Group, including Euro Star, Star and NTV.
$url eurostartv.com.tr
$url kralmuzik.com.tr
$url ntv.com.tr
$url startv.com.tr
$type live
"""

import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream
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


@pluginmatcher(re.compile(r"https?://(?:www\.)?eurostartv\.com\.tr/canli-izle"))
@pluginmatcher(re.compile(r"https?://(?:www\.)?kralmuzik\.com\.tr/tv/.+"))
@pluginmatcher(re.compile(r"https?://(?:www\.)?ntv\.com\.tr/canli-yayin/ntv"))
@pluginmatcher(re.compile(r"https?://(?:www\.)?startv\.com\.tr/canli-yayin"))
class Dogus(Plugin):
    _re_live_hls = re.compile(r"'(https?://[^']+/live/hls/[^']+)'")
    _re_yt_script = re.compile(r"youtube\.init\('([\w-]{11})'")

    def _get_streams(self):
        root = self.session.http.get(self.url, schema=validate.Schema(validate.parse_html()))

        # https://www.ntv.com.tr/canli-yayin/ntv?youtube=true
        yt_iframe = root.xpath("string(.//iframe[contains(@src,'youtube.com')][1]/@src)")
        # https://www.startv.com.tr/canli-yayin
        dm_iframe = root.xpath("string(.//iframe[contains(@src,'dailymotion.com')][1]/@src)")
        # https://www.kralmuzik.com.tr/tv/kral-tv
        # https://www.kralmuzik.com.tr/tv/kral-pop-tv
        yt_script = root.xpath("string(.//script[contains(text(), 'youtube.init')][1]/text())")
        if yt_script:
            m = self._re_yt_script.search(yt_script)
            if m:
                yt_iframe = f"https://www.youtube.com/watch?v={m.group(1)}"

        iframe = yt_iframe or dm_iframe
        if iframe:
            return self.session.streams(iframe)

        # http://eurostartv.com.tr/canli-izle
        dd_script = root.xpath("string(.//script[contains(text(), '/live/hls/')][1]/text())")
        if dd_script:
            m = self._re_live_hls.search(dd_script)
            if m:
                return HLSStream.parse_variant_playlist(self.session, m.group(1))


__plugin__ = Dogus

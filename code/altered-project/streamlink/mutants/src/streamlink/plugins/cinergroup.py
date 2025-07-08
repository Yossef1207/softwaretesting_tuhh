"""
$description Turkish live TV channels from Ciner Group, including Haberturk TV and Show TV.
$url bloomberght.com
$url haberturk.com
$url haberturk.tv
$url showmax.com.tr
$url showturk.com.tr
$url showtv.com.tr
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


@pluginmatcher(
    name="bloomberght",
    pattern=re.compile(r"https?://(?:www\.)?bloomberght\.com/tv/?"),
)
@pluginmatcher(
    name="haberturk",
    pattern=re.compile(r"https?://(?:www\.)?haberturk\.(?:com|tv)(?:/tv)?/canliyayin/?"),
)
@pluginmatcher(
    name="showmax",
    pattern=re.compile(r"https?://(?:www\.)?showmax\.com\.tr/canli-?yayin/?"),
)
@pluginmatcher(
    name="showturk",
    pattern=re.compile(r"https?://(?:www\.)?showturk\.com\.tr/canli-?yayin(?:/showtv)?/?"),
)
@pluginmatcher(
    name="showtv",
    pattern=re.compile(r"https?://(?:www\.)?showtv\.com\.tr/canli-yayin(?:/showtv)?/?"),
)
class CinerGroup(Plugin):
    @staticmethod
    def _schema_videourl():
        return validate.Schema(
            validate.xml_xpath_string(".//script[contains(text(), 'videoUrl')]/text()"),
            validate.none_or_all(
                re.compile(r"""(?<!//)\s*var\s+videoUrl\s*=\s*(?P<q>['"])(?P<url>.+?)(?P=q)"""),
                validate.none_or_all(
                    validate.get("url"),
                    validate.url(),
                ),
            ),
        )

    @staticmethod
    def _schema_data_ht():
        return validate.Schema(
            validate.xml_xpath_string(".//div[@data-ht][1]/@data-ht"),
            validate.none_or_all(
                validate.parse_json(),
                {
                    "ht_stream_m3u8": validate.url(),
                },
                validate.get("ht_stream_m3u8"),
            ),
        )

    def _get_streams(self):
        root = self.session.http.get(self.url, schema=validate.Schema(validate.parse_html()))
        schema_getters = self._schema_videourl, self._schema_data_ht
        stream_url = next((res for res in (getter().validate(root) for getter in schema_getters) if res), None)

        if stream_url:
            return HLSStream.parse_variant_playlist(self.session, stream_url)


__plugin__ = CinerGroup

"""
$description German news and documentaries TV channel, owned by Axel Springer SE.
$url welt.de
$type live, vod
$metadata title
$region Germany
$notes Some VODs are mp4 which may not stream, use -o to download
"""

import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream
from streamlink.stream.http import HTTPStream
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
    re.compile(r"https?://(\w+\.)?welt\.de/?"),
)
class Welt(Plugin):
    _re_vod_quality = re.compile(r"_(\d+)\.mp4$")

    def _get_streams(self):
        data = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string("""
                    .//script
                    [starts-with(@data-internal-ref,'WeltVideoPlayer-') or @data-content='VideoPlayer.Config']
                    /text()
                """),
                validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "title": str,
                        "sources": [
                            validate.all(
                                {
                                    "src": validate.url(),
                                    "extension": str,
                                },
                                validate.union_get("extension", "src"),
                            ),
                        ],
                    },
                    validate.union_get("sources", "title"),
                ),
            ),
        )
        if not data:
            return

        sources, self.title = data

        self.session.http.headers.update({"Referer": self.url})

        http_streams = {}
        for extension, src in sources:
            if extension == "m3u8":
                return HLSStream.parse_variant_playlist(self.session, src)
            if extension == "mp4":
                quality = self._re_vod_quality.search(src)
                if quality:
                    http_streams[f"{quality[1]}k"] = HTTPStream(self.session, src)

        return http_streams


__plugin__ = Welt

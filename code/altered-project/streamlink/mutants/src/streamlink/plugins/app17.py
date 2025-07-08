"""
$description Social platform delivering live broadcasts on diverse topics, from politics and music to entertainment.
$url 17app.co
$type live
"""

import logging
import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream
from streamlink.stream.http import HTTPStream


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


@pluginmatcher(
    re.compile(r"https?://17\.live/.+/live/(?P<channel>[^/&?]+)"),
)
class App17(Plugin):
    def _get_streams(self):
        channel = self.match.group("channel")
        self.session.http.headers.update({"Referer": self.url})
        data = self.session.http.post(
            f"https://wap-api.17app.co/api/v1/lives/{channel}/viewers/alive",
            data={"liveStreamID": channel},
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    {
                        "rtmpUrls": [
                            {
                                validate.optional("provider"): validate.any(int, None),
                                "url": validate.url(path=validate.endswith(".flv")),
                            },
                        ],
                    },
                    {"errorCode": int, "errorMessage": str},
                ),
            ),
            acceptable_status=(200, 403, 404, 420),
        )
        log.trace(f"{data!r}")
        if data.get("errorCode"):
            log.error(f"{data['errorCode']} - {data['errorMessage'].replace('Something wrong: ', '')}")
            return

        flv_url = data["rtmpUrls"][0]["url"]
        yield "live", HTTPStream(self.session, flv_url)

        if "wansu-" in flv_url:
            hls_url = flv_url.replace(".flv", "/playlist.m3u8")
        else:
            hls_url = flv_url.replace("live-hdl", "live-hls").replace(".flv", ".m3u8")

        s = HLSStream.parse_variant_playlist(self.session, hls_url)
        if not s:
            yield "live", HLSStream(self.session, hls_url)
        elif len(s) == 1:
            yield "live", next(iter(s.values()))
        else:
            yield from s.items()


__plugin__ = App17

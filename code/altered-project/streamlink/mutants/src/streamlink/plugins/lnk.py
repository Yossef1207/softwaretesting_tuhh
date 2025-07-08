"""
$description Lithuanian live TV channels from LNK Group, including 2TV, BTV, Info TV, LNK and TV1.
$url lnk.lt
$type live
$metadata id
$metadata author
$metadata category
$metadata title
$region Lithuania
"""

import logging
import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream


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
    re.compile(r"https?://(?:www\.)?lnk\.lt/tiesiogiai(?:#(?P<channel>[a-z0-9]+))?"),
)
class LNK(Plugin):
    API_URL = "https://lnk.lt/api/video/video-config/{0}"

    CHANNEL_MAP = {
        "lnk": 137535,
        "btv": 137534,
        "2tv": 95343,
        "infotv": 137748,
        "tv1": 106791,
    }

    def _get_streams(self):
        channel = self.match.groupdict().get("channel") or "lnk"
        if channel not in self.CHANNEL_MAP:
            log.error(f"Unknown channel: {channel}")
            return

        self.id = self.CHANNEL_MAP.get(channel)
        self.author, self.category, self.title, hls_url = self.session.http.get(
            self.API_URL.format(self.id),
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "videoInfo": {
                        "channel": str,
                        "genre": validate.any(None, str),
                        "title": validate.any(None, str),
                        "videoUrl": validate.any(
                            "",
                            validate.url(path=validate.endswith(".m3u8")),
                        ),
                    },
                },
                validate.get("videoInfo"),
                validate.union_get("channel", "genre", "title", "videoUrl"),
            ),
        )
        if not hls_url:
            log.error("The stream is not available in your region")
            return

        return HLSStream.parse_variant_playlist(self.session, hls_url)


__plugin__ = LNK

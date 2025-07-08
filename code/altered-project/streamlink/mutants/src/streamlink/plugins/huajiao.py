"""
$description Chinese live-streaming platform for live video game broadcasts and individual live streams.
$url huajiao.com
$type live
$metadata author
$metadata category
$metadata title
"""

import base64
import random
import re
import time
import uuid

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
    re.compile(r"https?://(?:www\.)?huajiao\.com/l/(?P<channel>[^/]+)"),
)
class Huajiao(Plugin):
    URL_LAPI = "https://g2.live.360.cn/liveplay"

    def _get_streams(self):
        data = self.session.http.get(
            self.url,
            schema=validate.Schema(
                re.compile(r"var\s*feed\s*=\s*(?P<feed>{.+?})\s*;", re.DOTALL),
                validate.none_or_all(
                    validate.get("feed"),
                    validate.parse_json(),
                    {
                        "author": {
                            "nickname": str,
                        },
                        "feed": {
                            "title": str,
                            "game": str,
                            "m3u8": validate.any("", validate.url()),
                            "sn": str,
                        },
                        "relay": {
                            "channel": str,
                        },
                    },
                    validate.union_get(
                        ("author", "nickname"),
                        ("feed", "title"),
                        ("feed", "game"),
                        ("feed", "m3u8"),
                        ("feed", "sn"),
                        ("relay", "channel"),
                    ),
                ),
            ),
        )
        if not data:
            return

        self.author, self.title, self.category, m3u8, sn, channel_sid = data

        if m3u8:
            return HLSStream(self.session, m3u8)

        stream_url = self.session.http.get(
            self.URL_LAPI,
            params={
                "stype": "flv",
                "channel": channel_sid,
                "bid": "huajiao",
                "sn": sn,
                "sid": uuid.uuid4().hex.upper(),
                "_rate": "xd",
                "ts": time.time(),
                "r": random.random(),
            },
            schema=validate.Schema(
                validate.transform(lambda text: base64.b64decode(text[0:3] + text[6:]).decode("utf-8")),
                validate.parse_json(),
                {"main": validate.url()},
                validate.get("main"),
            ),
        )
        return {"live": HTTPStream(self.session, stream_url)}


__plugin__ = Huajiao

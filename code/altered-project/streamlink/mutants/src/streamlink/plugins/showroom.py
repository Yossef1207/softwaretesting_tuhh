"""
$description Japanese live-streaming service used primarily by Japanese idols & voice actors and their fans.
$url showroom-live.com
$type live
$metadata title
"""

import logging
import re
from urllib.parse import parse_qsl, urlparse

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
    re.compile(r"https?://(?:\w+\.)?showroom-live\.com/"),
)
class Showroom(Plugin):
    LIVE_STATUS = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session.set_option("hls-playlist-reload-time", "segment")

    def _get_streams(self):
        room_id = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//nav//a[contains(@href,'/room/profile?')]/@href"),
                validate.none_or_all(
                    validate.transform(lambda _url_profile: dict(parse_qsl(urlparse(_url_profile).query))),
                    validate.get("room_id"),
                ),
            ),
        )
        if not room_id:
            return

        log.debug(f"Room ID: {room_id}")

        live_status, self.title = self.session.http.get(
            "https://www.showroom-live.com/api/live/live_info",
            params={
                "room_id": room_id,
            },
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "live_status": int,
                    "room_name": str,
                },
                validate.union_get(
                    "live_status",
                    "room_name",
                ),
            ),
        )
        if live_status != self.LIVE_STATUS:
            log.info("This stream is currently offline")
            return

        url = self.session.http.get(
            "https://www.showroom-live.com/api/live/streaming_url",
            params={
                "room_id": room_id,
                "abr_available": 1,
            },
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "streaming_url_list": [
                        {
                            "type": str,
                            "url": validate.url(),
                        },
                    ],
                },
                validate.get("streaming_url_list"),
                validate.filter(lambda p: p["type"] == "hls_all"),
                validate.get((0, "url")),
            ),
        )

        res = self.session.http.get(url, acceptable_status=(200, 403, 404))
        if res.headers["Content-Type"] not in ("application/x-mpegURL", "application/vnd.apple.mpegurl"):
            log.error("This stream is restricted")
            return

        return HLSStream.parse_variant_playlist(self.session, url)


__plugin__ = Showroom

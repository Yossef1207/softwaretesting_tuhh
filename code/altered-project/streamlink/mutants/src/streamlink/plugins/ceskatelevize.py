"""
$description Live TV channels from CT, a Czech public, state-owned broadcaster.
$url ceskatelevize.cz
$type live
$metadata id
$metadata title
$region Czechia
"""

import logging
import re
from uuid import uuid4

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.dash import DASHStream


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
    name="channel",
    pattern=re.compile(r"https?://(?P<channel>ct24|decko)\.ceskatelevize\.cz/"),
)
@pluginmatcher(
    name="sport",
    pattern=re.compile(r"https?://sport\.ceskatelevize\.cz/"),
)
@pluginmatcher(
    name="default",
    pattern=re.compile(r"https?://(?:www\.)?ceskatelevize\.cz/zive/\w+"),
)
class Ceskatelevize(Plugin):
    URL_API_CHANNEL = "https://api.ceskatelevize.cz/video/v1/playlist-live/v1/stream-data/channel/{channel}"

    CHANNELS = {
        "ct24": "CH_24",
        "decko": "CH_5",
    }

    def get_streams_from_api(self, channel):
        if not channel:
            return

        self.title, is_blocked, url = self.session.http.get(
            self.URL_API_CHANNEL.format(channel=channel),
            params={
                "canPlayDRM": "false",
                "streamType": "dash",
                "quality": "web",
                "maxQualityCount": 5,
                "sessionId": uuid4(),
            },
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "streamUrls": {
                        "isBlocked": bool,
                        "main": validate.url(),
                    },
                    "title": str,
                },
                validate.union_get(
                    "title",
                    ("streamUrls", "isBlocked"),
                    ("streamUrls", "main"),
                ),
            ),
        )

        if is_blocked:
            log.error("The stream is inaccessible")
            return

        return url

    def get_streams_channel(self):
        self.id = self.CHANNELS.get(self.match["channel"])

        return self.get_streams_from_api(self.id)

    def get_streams_sport(self):
        schema = validate.Schema(
            validate.parse_html(),
            validate.xml_xpath_string(".//section[@id='live']/@data-ctcomp-data"),
            validate.none_or_all(
                validate.parse_json(),
                {
                    "items": [
                        {
                            "items": [
                                {
                                    validate.optional("video"): {
                                        "data": {
                                            "source": {
                                                "playlist": [
                                                    {
                                                        "id": str,
                                                        "drm": int,
                                                    },
                                                ],
                                            },
                                        },
                                    },
                                },
                            ],
                        },
                    ],
                },
                validate.get(("items", 0, "items", 0, "video", "data", "source", "playlist", 0, "id")),
            ),
        )

        self.id = self.session.http.get(self.url, schema=schema)

        return self.get_streams_from_api(self.id)

    def get_streams_default(self):
        schema = validate.Schema(
            validate.parse_html(),
            validate.xml_xpath_string(".//script[@id='__NEXT_DATA__'][text()]/text()"),
            str,
            validate.parse_json(),
            {
                "props": {
                    "pageProps": {
                        validate.optional("data"): validate.all(
                            {
                                "liveBroadcast": {
                                    "id": str,
                                },
                            },
                            validate.get(("liveBroadcast", "id")),
                        ),
                    },
                },
            },
            validate.get(("props", "pageProps", "data")),
        )

        self.id = self.session.http.get(self.url, schema=schema)

        return self.get_streams_from_api(self.id)

    def _get_streams(self):
        if self.matches["channel"]:
            url = self.get_streams_channel()
        elif self.matches["sport"]:
            url = self.get_streams_sport()
        else:
            url = self.get_streams_default()

        if not url:
            return

        return DASHStream.parse_manifest(self.session, url)


__plugin__ = Ceskatelevize

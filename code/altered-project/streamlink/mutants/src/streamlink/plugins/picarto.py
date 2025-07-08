"""
$description Global live-streaming and video hosting platform for the creative community.
$url picarto.tv
$type live, vod
$metadata author
$metadata category
$metadata title
"""

import logging
import re
from textwrap import dedent
from urllib.parse import urlparse

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
    name="streampopout",
    pattern=re.compile(r"https?://(?:www\.)?picarto\.tv/streampopout/(?P<po_user>[^/]+)/public$"),
)
@pluginmatcher(
    name="videopopout",
    pattern=re.compile(r"https?://(?:www\.)?picarto\.tv/videopopout/(?P<po_vod_id>\d+)$"),
)
@pluginmatcher(
    name="vod",
    pattern=re.compile(r"https?://(?:www\.)?picarto\.tv/[^/]+/videos/(?P<vod_id>\d+)$"),
)
@pluginmatcher(
    name="user",
    pattern=re.compile(r"https?://(?:www\.)?picarto\.tv/(?P<user>[^/?&]+)$"),
)
class Picarto(Plugin):
    API_URL_LIVE = "https://ptvintern.picarto.tv/api/channel/detail/{username}"
    API_URL_VOD = "https://ptvintern.picarto.tv/ptvapi"
    HLS_URL = "https://{netloc}/stream/hls/{file_name}/index.m3u8"

    def get_live(self, username):
        channel, multistreams, loadbalancer = self.session.http.get(
            self.API_URL_LIVE.format(username=username),
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "channel": validate.any(
                        None,
                        {
                            "id": int,
                            "title": str,
                            "private": bool,
                            "categories": [{"name": str}],
                        },
                    ),
                    "getMultiStreams": validate.any(
                        None,
                        {
                            "streams": [
                                {
                                    "id": int,
                                    "channelId": int,
                                    "name": str,
                                    "online": bool,
                                    "stream_name": str,
                                },
                            ],
                        },
                    ),
                    "getLoadBalancerUrl": validate.any(
                        None,
                        {
                            "url": validate.any(None, validate.transform(lambda url: urlparse(url).netloc)),
                        },
                    ),
                },
                validate.union_get("channel", "getMultiStreams", "getLoadBalancerUrl"),
            ),
        )
        if not channel or not multistreams or not loadbalancer:
            return

        if channel["private"]:
            log.error("This is a private stream")
            return

        user_id = channel["id"]
        if not (stream := next((stream for stream in multistreams["streams"] if stream["channelId"] == user_id), None)):
            log.error("No available stream found in 'multistreams' data")
            return

        self.author = username
        self.category = next(iter(channel["categories"]), {}).get("name")
        self.title = channel["title"]

        hls_url = self.HLS_URL.format(
            netloc=loadbalancer["url"],
            file_name=stream["stream_name"],
        )

        return HLSStream.parse_variant_playlist(self.session, hls_url)

    def get_vod(self, vod_id):
        data = {
            "query": dedent("""
                query ($videoId: ID!) {
                  video(id: $videoId) {
                    id
                    title
                    file_name
                    video_recording_image_url
                    channel {
                      name
                    }
                  }
                }
            """).lstrip(),
            "variables": {"videoId": vod_id},
        }
        vod_data = self.session.http.post(
            self.API_URL_VOD,
            json=data,
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "data": {
                        "video": validate.any(
                            None,
                            {
                                "id": int,
                                "title": str,
                                "file_name": str,
                                "video_recording_image_url": str,
                                "channel": {"name": str},
                            },
                        ),
                    },
                },
                validate.get(("data", "video")),
            ),
        )
        if not vod_data:
            return

        self.author = vod_data["channel"]["name"]
        self.category = "VOD"
        self.title = vod_data["title"]

        netloc = urlparse(vod_data["video_recording_image_url"]).netloc
        hls_url = self.HLS_URL.format(
            netloc=netloc,
            file_name=vod_data["file_name"],
        )

        return HLSStream.parse_variant_playlist(self.session, hls_url)

    def _get_streams(self):
        m = self.match.groupdict()

        if m.get("po_vod_id") or m.get("vod_id"):
            log.debug("Type=VOD")
            return self.get_vod(m.get("po_vod_id") or m.get("vod_id"))
        elif m.get("po_user") or m.get("user"):
            log.debug("Type=Live")
            return self.get_live(m.get("po_user") or m.get("user"))


__plugin__ = Picarto

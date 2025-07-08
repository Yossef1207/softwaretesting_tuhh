"""
$description Global live-streaming platform owned by BitTorrent, Inc.
$url dlive.tv
$type live, vod
$metadata id
$metadata author
$metadata category
$metadata title
"""

import logging
import re
from textwrap import dedent

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


class DLiveHLSStream(HLSStream):
    URL_SIGN = "https://live.prd.dlive.tv/hls/sign/url"

    def xǁDLiveHLSStreamǁ__init____mutmut_orig(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_1(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_2(self, *args, **kwargs):
        super().__init__(*args, )
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_3(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = None

    def xǁDLiveHLSStreamǁ__init____mutmut_4(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["XXurlXX"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_5(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["URL"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_6(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["Url"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_7(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            None,
            json={"playlisturi": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_8(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json=None,
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_9(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["url"]},
            schema=None,
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_10(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            json={"playlisturi": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_11(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_12(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["url"]},
            )

    def xǁDLiveHLSStreamǁ__init____mutmut_13(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"XXplaylisturiXX": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_14(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"PLAYLISTURI": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_15(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"Playlisturi": self.args["url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_16(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["XXurlXX"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_17(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["URL"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_18(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["Url"]},
            schema=validate.Schema(validate.url()),
        )

    def xǁDLiveHLSStreamǁ__init____mutmut_19(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args["url"] = self.session.http.post(
            self.URL_SIGN,
            json={"playlisturi": self.args["url"]},
            schema=validate.Schema(None),
        )
    
    xǁDLiveHLSStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDLiveHLSStreamǁ__init____mutmut_1': xǁDLiveHLSStreamǁ__init____mutmut_1, 
        'xǁDLiveHLSStreamǁ__init____mutmut_2': xǁDLiveHLSStreamǁ__init____mutmut_2, 
        'xǁDLiveHLSStreamǁ__init____mutmut_3': xǁDLiveHLSStreamǁ__init____mutmut_3, 
        'xǁDLiveHLSStreamǁ__init____mutmut_4': xǁDLiveHLSStreamǁ__init____mutmut_4, 
        'xǁDLiveHLSStreamǁ__init____mutmut_5': xǁDLiveHLSStreamǁ__init____mutmut_5, 
        'xǁDLiveHLSStreamǁ__init____mutmut_6': xǁDLiveHLSStreamǁ__init____mutmut_6, 
        'xǁDLiveHLSStreamǁ__init____mutmut_7': xǁDLiveHLSStreamǁ__init____mutmut_7, 
        'xǁDLiveHLSStreamǁ__init____mutmut_8': xǁDLiveHLSStreamǁ__init____mutmut_8, 
        'xǁDLiveHLSStreamǁ__init____mutmut_9': xǁDLiveHLSStreamǁ__init____mutmut_9, 
        'xǁDLiveHLSStreamǁ__init____mutmut_10': xǁDLiveHLSStreamǁ__init____mutmut_10, 
        'xǁDLiveHLSStreamǁ__init____mutmut_11': xǁDLiveHLSStreamǁ__init____mutmut_11, 
        'xǁDLiveHLSStreamǁ__init____mutmut_12': xǁDLiveHLSStreamǁ__init____mutmut_12, 
        'xǁDLiveHLSStreamǁ__init____mutmut_13': xǁDLiveHLSStreamǁ__init____mutmut_13, 
        'xǁDLiveHLSStreamǁ__init____mutmut_14': xǁDLiveHLSStreamǁ__init____mutmut_14, 
        'xǁDLiveHLSStreamǁ__init____mutmut_15': xǁDLiveHLSStreamǁ__init____mutmut_15, 
        'xǁDLiveHLSStreamǁ__init____mutmut_16': xǁDLiveHLSStreamǁ__init____mutmut_16, 
        'xǁDLiveHLSStreamǁ__init____mutmut_17': xǁDLiveHLSStreamǁ__init____mutmut_17, 
        'xǁDLiveHLSStreamǁ__init____mutmut_18': xǁDLiveHLSStreamǁ__init____mutmut_18, 
        'xǁDLiveHLSStreamǁ__init____mutmut_19': xǁDLiveHLSStreamǁ__init____mutmut_19
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDLiveHLSStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁDLiveHLSStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁDLiveHLSStreamǁ__init____mutmut_orig)
    xǁDLiveHLSStreamǁ__init____mutmut_orig.__name__ = 'xǁDLiveHLSStreamǁ__init__'


@pluginmatcher(
    name="live",
    pattern=re.compile(
        r"https?://(?:www\.)?dlive\.tv/(?P<channel>[^/?#]+)(?:$|[?#])",
    ),
)
@pluginmatcher(
    name="vod",
    pattern=re.compile(
        r"https?://(?:www\.)?dlive\.tv/p/(?P<video>[^/?#]+)(?:$|[?#])",
    ),
)
class DLive(Plugin):
    URL_API = "https://graphigo.prd.dlive.tv/"
    URL_LIVE = "https://live.prd.dlive.tv/hls/live/{username}.m3u8"

    QUALITY_WEIGHTS = {
        "src": 1080,
    }

    @classmethod
    def stream_weight(cls, key):
        weight = cls.QUALITY_WEIGHTS.get(key)
        if weight:
            return weight, "dlive"

        return super().stream_weight(key)

    def _get_streams_video(self, video):
        log.debug(f"Getting video HLS streams for {video}")

        self.id = video
        hls_url, self.author, self.category, self.title = self.session.http.post(
            self.URL_API,
            json={
                "query": dedent(f"""
                    query {{
                        pastBroadcast(permlink:"{video}") {{
                            playbackUrl
                            creator {{
                                username
                            }}
                            category {{
                                title
                            }}
                            title
                        }}
                    }}
                """),
            },
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "data": {
                        "pastBroadcast": {
                            "playbackUrl": validate.url(path=validate.endswith(".m3u8")),
                            "creator": {
                                "username": str,
                            },
                            "category": {
                                "title": str,
                            },
                            "title": str,
                        },
                    },
                },
                validate.get(("data", "pastBroadcast")),
                validate.union_get(
                    "playbackUrl",
                    ("creator", "username"),
                    ("category", "title"),
                    "title",
                ),
            ),
        )

        return HLSStream.parse_variant_playlist(self.session, hls_url)

    def _get_streams_live(self, channel):
        log.debug(f"Getting live HLS streams for {channel}")

        self.author = channel
        username, self.title = self.session.http.post(
            self.URL_API,
            json={
                "query": dedent(f"""
                    query {{
                        userByDisplayName(displayname:"{channel}") {{
                            username
                            livestream {{
                                title
                            }}
                        }}
                    }}
                """),
            },
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "data": {
                        "userByDisplayName": {
                            "username": str,
                            "livestream": {
                                "title": str,
                            },
                        },
                    },
                },
                validate.get(("data", "userByDisplayName")),
                validate.union_get(
                    "username",
                    ("livestream", "title"),
                ),
            ),
        )

        return DLiveHLSStream.parse_variant_playlist(self.session, self.URL_LIVE.format(username=username))

    def _get_streams(self):
        self.session.http.headers.update({
            "Origin": "https://dlive.tv",
            "Referer": "https://dlive.tv/",
        })

        if self.matches["live"]:
            return self._get_streams_live(self.match["channel"])
        if self.matches["vod"]:
            return self._get_streams_video(self.match["video"])


__plugin__ = DLive

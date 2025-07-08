"""
$description Global live-streaming and video on-demand hosting platform.
$url players.brightcove.net
$type live, vod
$metadata title
"""

import logging
import re
from urllib.parse import urlparse

from streamlink.plugin import Plugin, PluginError, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream
from streamlink.stream.http import HTTPStream
from streamlink.utils.parse import parse_qsd


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


class BrightcovePlayer:
    URL_PLAYER = "https://players.brightcove.net/{account_id}/{player_id}/index.html?videoId={video_id}"
    URL_API = "https://edge.api.brightcove.com/playback/v1/accounts/{account_id}/videos/{video_id}"

    def xǁBrightcovePlayerǁ__init____mutmut_orig(self, session, account_id, player_id="default_default"):
        self.session = session
        self.account_id = account_id
        self.player_id = player_id
        self.title = None
        log.debug(f"Creating player for account {account_id} (player_id={player_id})")

    def xǁBrightcovePlayerǁ__init____mutmut_1(self, session, account_id, player_id="XXdefault_defaultXX"):
        self.session = session
        self.account_id = account_id
        self.player_id = player_id
        self.title = None
        log.debug(f"Creating player for account {account_id} (player_id={player_id})")

    def xǁBrightcovePlayerǁ__init____mutmut_2(self, session, account_id, player_id="DEFAULT_DEFAULT"):
        self.session = session
        self.account_id = account_id
        self.player_id = player_id
        self.title = None
        log.debug(f"Creating player for account {account_id} (player_id={player_id})")

    def xǁBrightcovePlayerǁ__init____mutmut_3(self, session, account_id, player_id="Default_default"):
        self.session = session
        self.account_id = account_id
        self.player_id = player_id
        self.title = None
        log.debug(f"Creating player for account {account_id} (player_id={player_id})")

    def xǁBrightcovePlayerǁ__init____mutmut_4(self, session, account_id, player_id="default_default"):
        self.session = None
        self.account_id = account_id
        self.player_id = player_id
        self.title = None
        log.debug(f"Creating player for account {account_id} (player_id={player_id})")

    def xǁBrightcovePlayerǁ__init____mutmut_5(self, session, account_id, player_id="default_default"):
        self.session = session
        self.account_id = None
        self.player_id = player_id
        self.title = None
        log.debug(f"Creating player for account {account_id} (player_id={player_id})")

    def xǁBrightcovePlayerǁ__init____mutmut_6(self, session, account_id, player_id="default_default"):
        self.session = session
        self.account_id = account_id
        self.player_id = None
        self.title = None
        log.debug(f"Creating player for account {account_id} (player_id={player_id})")

    def xǁBrightcovePlayerǁ__init____mutmut_7(self, session, account_id, player_id="default_default"):
        self.session = session
        self.account_id = account_id
        self.player_id = player_id
        self.title = ""
        log.debug(f"Creating player for account {account_id} (player_id={player_id})")

    def xǁBrightcovePlayerǁ__init____mutmut_8(self, session, account_id, player_id="default_default"):
        self.session = session
        self.account_id = account_id
        self.player_id = player_id
        self.title = None
        log.debug(None)
    
    xǁBrightcovePlayerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBrightcovePlayerǁ__init____mutmut_1': xǁBrightcovePlayerǁ__init____mutmut_1, 
        'xǁBrightcovePlayerǁ__init____mutmut_2': xǁBrightcovePlayerǁ__init____mutmut_2, 
        'xǁBrightcovePlayerǁ__init____mutmut_3': xǁBrightcovePlayerǁ__init____mutmut_3, 
        'xǁBrightcovePlayerǁ__init____mutmut_4': xǁBrightcovePlayerǁ__init____mutmut_4, 
        'xǁBrightcovePlayerǁ__init____mutmut_5': xǁBrightcovePlayerǁ__init____mutmut_5, 
        'xǁBrightcovePlayerǁ__init____mutmut_6': xǁBrightcovePlayerǁ__init____mutmut_6, 
        'xǁBrightcovePlayerǁ__init____mutmut_7': xǁBrightcovePlayerǁ__init____mutmut_7, 
        'xǁBrightcovePlayerǁ__init____mutmut_8': xǁBrightcovePlayerǁ__init____mutmut_8
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBrightcovePlayerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBrightcovePlayerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBrightcovePlayerǁ__init____mutmut_orig)
    xǁBrightcovePlayerǁ__init____mutmut_orig.__name__ = 'xǁBrightcovePlayerǁ__init__'

    def xǁBrightcovePlayerǁget_streams__mutmut_orig(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_1(self, video_id):
        log.debug(None)

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_2(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = None

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_3(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=None,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_4(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=None,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_5(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=None,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_6(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_7(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_8(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_9(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = None
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_10(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            None,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_11(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params=None,
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_12(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=None,
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_13(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_14(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_15(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_16(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"XXvideoIdXX": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_17(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoid": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_18(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"VIDEOID": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_19(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"Videoid": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_20(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                None,
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_21(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                None,
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_22(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_23(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_24(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(None),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_25(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, None),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_26(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_27(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, ),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_28(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get(None)),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_29(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("XXkeyXX")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_30(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("KEY")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_31(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("Key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_32(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_33(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError(None)
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_34(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("XXCould not find Brightcove policy keyXX")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_35(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("could not find brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_36(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("COULD NOT FIND BRIGHTCOVE POLICY KEY")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_37(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_38(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(None)

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_39(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update(None)
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_40(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"XXRefererXX": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_41(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_42(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"REFERER": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_43(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = None

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_44(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            None,
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_45(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers=None,
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_46(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=None,
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_47(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_48(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_49(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_50(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=None, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_51(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=None),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_52(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_53(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, ),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_54(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"XXAcceptXX": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_55(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_56(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"ACCEPT": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_57(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                None,
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_58(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                None,
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_59(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                None,
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_60(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_61(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_62(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_63(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "XXsourcesXX": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_64(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "SOURCES": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_65(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "Sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_66(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "XXsrcXX": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_67(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "SRC": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_68(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "Src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_69(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional(None): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_70(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("XXtypeXX"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_71(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("TYPE"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_72(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("Type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_73(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional(None): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_74(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("XXcontainerXX"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_75(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("CONTAINER"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_76(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("Container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_77(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional(None): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_78(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("XXheightXX"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_79(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("HEIGHT"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_80(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("Height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_81(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional(None): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_82(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("XXavg_bitrateXX"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_83(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("AVG_BITRATE"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_84(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("Avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_85(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional(None): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_86(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("XXnameXX"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_87(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("NAME"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_88(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("Name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_89(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get(None, "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_90(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", None),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_91(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_92(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", ),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_93(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("XXsourcesXX", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_94(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("SOURCES", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_95(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("Sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_96(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "XXnameXX"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_97(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "NAME"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_98(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "Name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_99(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get(None) in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_100(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("XXtypeXX") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_101(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("TYPE") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_102(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("Type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_103(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") not in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_104(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("XXapplication/vnd.apple.mpegurlXX", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_105(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("APPLICATION/VND.APPLE.MPEGURL", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_106(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("Application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_107(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "XXapplication/x-mpegURLXX"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_108(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegurl"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_109(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "APPLICATION/X-MPEGURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_110(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "Application/x-mpegurl"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_111(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(None, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_112(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, None).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_113(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_114(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, ).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_115(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get(None)).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_116(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("XXsrcXX")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_117(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("SRC")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_118(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("Src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_119(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get(None) == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_120(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("XXcontainerXX") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_121(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("CONTAINER") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_122(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("Container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_123(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") != "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_124(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "XXMP4XX":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_125(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "mp4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_126(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "Mp4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_127(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get(None):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_128(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("XXheightXX"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_129(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("HEIGHT"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_130(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("Height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_131(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = None
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_132(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get(None)}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_133(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('XXheightXX')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_134(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('HEIGHT')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_135(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('Height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_136(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get(None):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_137(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("XXavg_bitrateXX"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_138(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("AVG_BITRATE"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_139(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("Avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_140(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = None
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_141(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get(None) // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_142(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('XXavg_bitrateXX') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_143(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('AVG_BITRATE') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_144(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('Avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_145(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') / 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_146(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1001}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_147(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = None

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_148(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "XXliveXX"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_149(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "LIVE"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_150(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "Live"

                yield q, HTTPStream(self.session, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_151(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(None, source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_152(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, None)

    def xǁBrightcovePlayerǁget_streams__mutmut_153(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(source.get("src"))

    def xǁBrightcovePlayerǁget_streams__mutmut_154(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, )

    def xǁBrightcovePlayerǁget_streams__mutmut_155(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get(None))

    def xǁBrightcovePlayerǁget_streams__mutmut_156(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("XXsrcXX"))

    def xǁBrightcovePlayerǁget_streams__mutmut_157(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("SRC"))

    def xǁBrightcovePlayerǁget_streams__mutmut_158(self, video_id):
        log.debug(f"Finding streams for video: {video_id}")

        player_url = self.URL_PLAYER.format(
            account_id=self.account_id,
            player_id=self.player_id,
            video_id=video_id,
        )

        policy_key = self.session.http.get(
            player_url,
            params={"videoId": video_id},
            schema=validate.Schema(
                re.compile(r"""policyKey\s*:\s*(?P<q>['"])(?P<key>[\w-]+)(?P=q)"""),
                validate.any(None, validate.get("key")),
            ),
        )
        if not policy_key:
            raise PluginError("Could not find Brightcove policy key")
        log.debug(f"Found policy key: {policy_key}")

        self.session.http.headers.update({"Referer": player_url})
        sources, self.title = self.session.http.get(
            self.URL_API.format(account_id=self.account_id, video_id=video_id),
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            "src": validate.url(),
                            validate.optional("type"): str,
                            validate.optional("container"): str,
                            validate.optional("height"): int,
                            validate.optional("avg_bitrate"): int,
                        },
                    ],
                    validate.optional("name"): str,
                },
                validate.union_get("sources", "name"),
            ),
        )

        for source in sources:
            if source.get("type") in ("application/vnd.apple.mpegurl", "application/x-mpegURL"):
                yield from HLSStream.parse_variant_playlist(self.session, source.get("src")).items()

            elif source.get("container") == "MP4":
                # determine quality name
                if source.get("height"):
                    q = f"{source.get('height')}p"
                elif source.get("avg_bitrate"):
                    q = f"{source.get('avg_bitrate') // 1000}k"
                else:
                    q = "live"

                yield q, HTTPStream(self.session, source.get("Src"))
    
    xǁBrightcovePlayerǁget_streams__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBrightcovePlayerǁget_streams__mutmut_1': xǁBrightcovePlayerǁget_streams__mutmut_1, 
        'xǁBrightcovePlayerǁget_streams__mutmut_2': xǁBrightcovePlayerǁget_streams__mutmut_2, 
        'xǁBrightcovePlayerǁget_streams__mutmut_3': xǁBrightcovePlayerǁget_streams__mutmut_3, 
        'xǁBrightcovePlayerǁget_streams__mutmut_4': xǁBrightcovePlayerǁget_streams__mutmut_4, 
        'xǁBrightcovePlayerǁget_streams__mutmut_5': xǁBrightcovePlayerǁget_streams__mutmut_5, 
        'xǁBrightcovePlayerǁget_streams__mutmut_6': xǁBrightcovePlayerǁget_streams__mutmut_6, 
        'xǁBrightcovePlayerǁget_streams__mutmut_7': xǁBrightcovePlayerǁget_streams__mutmut_7, 
        'xǁBrightcovePlayerǁget_streams__mutmut_8': xǁBrightcovePlayerǁget_streams__mutmut_8, 
        'xǁBrightcovePlayerǁget_streams__mutmut_9': xǁBrightcovePlayerǁget_streams__mutmut_9, 
        'xǁBrightcovePlayerǁget_streams__mutmut_10': xǁBrightcovePlayerǁget_streams__mutmut_10, 
        'xǁBrightcovePlayerǁget_streams__mutmut_11': xǁBrightcovePlayerǁget_streams__mutmut_11, 
        'xǁBrightcovePlayerǁget_streams__mutmut_12': xǁBrightcovePlayerǁget_streams__mutmut_12, 
        'xǁBrightcovePlayerǁget_streams__mutmut_13': xǁBrightcovePlayerǁget_streams__mutmut_13, 
        'xǁBrightcovePlayerǁget_streams__mutmut_14': xǁBrightcovePlayerǁget_streams__mutmut_14, 
        'xǁBrightcovePlayerǁget_streams__mutmut_15': xǁBrightcovePlayerǁget_streams__mutmut_15, 
        'xǁBrightcovePlayerǁget_streams__mutmut_16': xǁBrightcovePlayerǁget_streams__mutmut_16, 
        'xǁBrightcovePlayerǁget_streams__mutmut_17': xǁBrightcovePlayerǁget_streams__mutmut_17, 
        'xǁBrightcovePlayerǁget_streams__mutmut_18': xǁBrightcovePlayerǁget_streams__mutmut_18, 
        'xǁBrightcovePlayerǁget_streams__mutmut_19': xǁBrightcovePlayerǁget_streams__mutmut_19, 
        'xǁBrightcovePlayerǁget_streams__mutmut_20': xǁBrightcovePlayerǁget_streams__mutmut_20, 
        'xǁBrightcovePlayerǁget_streams__mutmut_21': xǁBrightcovePlayerǁget_streams__mutmut_21, 
        'xǁBrightcovePlayerǁget_streams__mutmut_22': xǁBrightcovePlayerǁget_streams__mutmut_22, 
        'xǁBrightcovePlayerǁget_streams__mutmut_23': xǁBrightcovePlayerǁget_streams__mutmut_23, 
        'xǁBrightcovePlayerǁget_streams__mutmut_24': xǁBrightcovePlayerǁget_streams__mutmut_24, 
        'xǁBrightcovePlayerǁget_streams__mutmut_25': xǁBrightcovePlayerǁget_streams__mutmut_25, 
        'xǁBrightcovePlayerǁget_streams__mutmut_26': xǁBrightcovePlayerǁget_streams__mutmut_26, 
        'xǁBrightcovePlayerǁget_streams__mutmut_27': xǁBrightcovePlayerǁget_streams__mutmut_27, 
        'xǁBrightcovePlayerǁget_streams__mutmut_28': xǁBrightcovePlayerǁget_streams__mutmut_28, 
        'xǁBrightcovePlayerǁget_streams__mutmut_29': xǁBrightcovePlayerǁget_streams__mutmut_29, 
        'xǁBrightcovePlayerǁget_streams__mutmut_30': xǁBrightcovePlayerǁget_streams__mutmut_30, 
        'xǁBrightcovePlayerǁget_streams__mutmut_31': xǁBrightcovePlayerǁget_streams__mutmut_31, 
        'xǁBrightcovePlayerǁget_streams__mutmut_32': xǁBrightcovePlayerǁget_streams__mutmut_32, 
        'xǁBrightcovePlayerǁget_streams__mutmut_33': xǁBrightcovePlayerǁget_streams__mutmut_33, 
        'xǁBrightcovePlayerǁget_streams__mutmut_34': xǁBrightcovePlayerǁget_streams__mutmut_34, 
        'xǁBrightcovePlayerǁget_streams__mutmut_35': xǁBrightcovePlayerǁget_streams__mutmut_35, 
        'xǁBrightcovePlayerǁget_streams__mutmut_36': xǁBrightcovePlayerǁget_streams__mutmut_36, 
        'xǁBrightcovePlayerǁget_streams__mutmut_37': xǁBrightcovePlayerǁget_streams__mutmut_37, 
        'xǁBrightcovePlayerǁget_streams__mutmut_38': xǁBrightcovePlayerǁget_streams__mutmut_38, 
        'xǁBrightcovePlayerǁget_streams__mutmut_39': xǁBrightcovePlayerǁget_streams__mutmut_39, 
        'xǁBrightcovePlayerǁget_streams__mutmut_40': xǁBrightcovePlayerǁget_streams__mutmut_40, 
        'xǁBrightcovePlayerǁget_streams__mutmut_41': xǁBrightcovePlayerǁget_streams__mutmut_41, 
        'xǁBrightcovePlayerǁget_streams__mutmut_42': xǁBrightcovePlayerǁget_streams__mutmut_42, 
        'xǁBrightcovePlayerǁget_streams__mutmut_43': xǁBrightcovePlayerǁget_streams__mutmut_43, 
        'xǁBrightcovePlayerǁget_streams__mutmut_44': xǁBrightcovePlayerǁget_streams__mutmut_44, 
        'xǁBrightcovePlayerǁget_streams__mutmut_45': xǁBrightcovePlayerǁget_streams__mutmut_45, 
        'xǁBrightcovePlayerǁget_streams__mutmut_46': xǁBrightcovePlayerǁget_streams__mutmut_46, 
        'xǁBrightcovePlayerǁget_streams__mutmut_47': xǁBrightcovePlayerǁget_streams__mutmut_47, 
        'xǁBrightcovePlayerǁget_streams__mutmut_48': xǁBrightcovePlayerǁget_streams__mutmut_48, 
        'xǁBrightcovePlayerǁget_streams__mutmut_49': xǁBrightcovePlayerǁget_streams__mutmut_49, 
        'xǁBrightcovePlayerǁget_streams__mutmut_50': xǁBrightcovePlayerǁget_streams__mutmut_50, 
        'xǁBrightcovePlayerǁget_streams__mutmut_51': xǁBrightcovePlayerǁget_streams__mutmut_51, 
        'xǁBrightcovePlayerǁget_streams__mutmut_52': xǁBrightcovePlayerǁget_streams__mutmut_52, 
        'xǁBrightcovePlayerǁget_streams__mutmut_53': xǁBrightcovePlayerǁget_streams__mutmut_53, 
        'xǁBrightcovePlayerǁget_streams__mutmut_54': xǁBrightcovePlayerǁget_streams__mutmut_54, 
        'xǁBrightcovePlayerǁget_streams__mutmut_55': xǁBrightcovePlayerǁget_streams__mutmut_55, 
        'xǁBrightcovePlayerǁget_streams__mutmut_56': xǁBrightcovePlayerǁget_streams__mutmut_56, 
        'xǁBrightcovePlayerǁget_streams__mutmut_57': xǁBrightcovePlayerǁget_streams__mutmut_57, 
        'xǁBrightcovePlayerǁget_streams__mutmut_58': xǁBrightcovePlayerǁget_streams__mutmut_58, 
        'xǁBrightcovePlayerǁget_streams__mutmut_59': xǁBrightcovePlayerǁget_streams__mutmut_59, 
        'xǁBrightcovePlayerǁget_streams__mutmut_60': xǁBrightcovePlayerǁget_streams__mutmut_60, 
        'xǁBrightcovePlayerǁget_streams__mutmut_61': xǁBrightcovePlayerǁget_streams__mutmut_61, 
        'xǁBrightcovePlayerǁget_streams__mutmut_62': xǁBrightcovePlayerǁget_streams__mutmut_62, 
        'xǁBrightcovePlayerǁget_streams__mutmut_63': xǁBrightcovePlayerǁget_streams__mutmut_63, 
        'xǁBrightcovePlayerǁget_streams__mutmut_64': xǁBrightcovePlayerǁget_streams__mutmut_64, 
        'xǁBrightcovePlayerǁget_streams__mutmut_65': xǁBrightcovePlayerǁget_streams__mutmut_65, 
        'xǁBrightcovePlayerǁget_streams__mutmut_66': xǁBrightcovePlayerǁget_streams__mutmut_66, 
        'xǁBrightcovePlayerǁget_streams__mutmut_67': xǁBrightcovePlayerǁget_streams__mutmut_67, 
        'xǁBrightcovePlayerǁget_streams__mutmut_68': xǁBrightcovePlayerǁget_streams__mutmut_68, 
        'xǁBrightcovePlayerǁget_streams__mutmut_69': xǁBrightcovePlayerǁget_streams__mutmut_69, 
        'xǁBrightcovePlayerǁget_streams__mutmut_70': xǁBrightcovePlayerǁget_streams__mutmut_70, 
        'xǁBrightcovePlayerǁget_streams__mutmut_71': xǁBrightcovePlayerǁget_streams__mutmut_71, 
        'xǁBrightcovePlayerǁget_streams__mutmut_72': xǁBrightcovePlayerǁget_streams__mutmut_72, 
        'xǁBrightcovePlayerǁget_streams__mutmut_73': xǁBrightcovePlayerǁget_streams__mutmut_73, 
        'xǁBrightcovePlayerǁget_streams__mutmut_74': xǁBrightcovePlayerǁget_streams__mutmut_74, 
        'xǁBrightcovePlayerǁget_streams__mutmut_75': xǁBrightcovePlayerǁget_streams__mutmut_75, 
        'xǁBrightcovePlayerǁget_streams__mutmut_76': xǁBrightcovePlayerǁget_streams__mutmut_76, 
        'xǁBrightcovePlayerǁget_streams__mutmut_77': xǁBrightcovePlayerǁget_streams__mutmut_77, 
        'xǁBrightcovePlayerǁget_streams__mutmut_78': xǁBrightcovePlayerǁget_streams__mutmut_78, 
        'xǁBrightcovePlayerǁget_streams__mutmut_79': xǁBrightcovePlayerǁget_streams__mutmut_79, 
        'xǁBrightcovePlayerǁget_streams__mutmut_80': xǁBrightcovePlayerǁget_streams__mutmut_80, 
        'xǁBrightcovePlayerǁget_streams__mutmut_81': xǁBrightcovePlayerǁget_streams__mutmut_81, 
        'xǁBrightcovePlayerǁget_streams__mutmut_82': xǁBrightcovePlayerǁget_streams__mutmut_82, 
        'xǁBrightcovePlayerǁget_streams__mutmut_83': xǁBrightcovePlayerǁget_streams__mutmut_83, 
        'xǁBrightcovePlayerǁget_streams__mutmut_84': xǁBrightcovePlayerǁget_streams__mutmut_84, 
        'xǁBrightcovePlayerǁget_streams__mutmut_85': xǁBrightcovePlayerǁget_streams__mutmut_85, 
        'xǁBrightcovePlayerǁget_streams__mutmut_86': xǁBrightcovePlayerǁget_streams__mutmut_86, 
        'xǁBrightcovePlayerǁget_streams__mutmut_87': xǁBrightcovePlayerǁget_streams__mutmut_87, 
        'xǁBrightcovePlayerǁget_streams__mutmut_88': xǁBrightcovePlayerǁget_streams__mutmut_88, 
        'xǁBrightcovePlayerǁget_streams__mutmut_89': xǁBrightcovePlayerǁget_streams__mutmut_89, 
        'xǁBrightcovePlayerǁget_streams__mutmut_90': xǁBrightcovePlayerǁget_streams__mutmut_90, 
        'xǁBrightcovePlayerǁget_streams__mutmut_91': xǁBrightcovePlayerǁget_streams__mutmut_91, 
        'xǁBrightcovePlayerǁget_streams__mutmut_92': xǁBrightcovePlayerǁget_streams__mutmut_92, 
        'xǁBrightcovePlayerǁget_streams__mutmut_93': xǁBrightcovePlayerǁget_streams__mutmut_93, 
        'xǁBrightcovePlayerǁget_streams__mutmut_94': xǁBrightcovePlayerǁget_streams__mutmut_94, 
        'xǁBrightcovePlayerǁget_streams__mutmut_95': xǁBrightcovePlayerǁget_streams__mutmut_95, 
        'xǁBrightcovePlayerǁget_streams__mutmut_96': xǁBrightcovePlayerǁget_streams__mutmut_96, 
        'xǁBrightcovePlayerǁget_streams__mutmut_97': xǁBrightcovePlayerǁget_streams__mutmut_97, 
        'xǁBrightcovePlayerǁget_streams__mutmut_98': xǁBrightcovePlayerǁget_streams__mutmut_98, 
        'xǁBrightcovePlayerǁget_streams__mutmut_99': xǁBrightcovePlayerǁget_streams__mutmut_99, 
        'xǁBrightcovePlayerǁget_streams__mutmut_100': xǁBrightcovePlayerǁget_streams__mutmut_100, 
        'xǁBrightcovePlayerǁget_streams__mutmut_101': xǁBrightcovePlayerǁget_streams__mutmut_101, 
        'xǁBrightcovePlayerǁget_streams__mutmut_102': xǁBrightcovePlayerǁget_streams__mutmut_102, 
        'xǁBrightcovePlayerǁget_streams__mutmut_103': xǁBrightcovePlayerǁget_streams__mutmut_103, 
        'xǁBrightcovePlayerǁget_streams__mutmut_104': xǁBrightcovePlayerǁget_streams__mutmut_104, 
        'xǁBrightcovePlayerǁget_streams__mutmut_105': xǁBrightcovePlayerǁget_streams__mutmut_105, 
        'xǁBrightcovePlayerǁget_streams__mutmut_106': xǁBrightcovePlayerǁget_streams__mutmut_106, 
        'xǁBrightcovePlayerǁget_streams__mutmut_107': xǁBrightcovePlayerǁget_streams__mutmut_107, 
        'xǁBrightcovePlayerǁget_streams__mutmut_108': xǁBrightcovePlayerǁget_streams__mutmut_108, 
        'xǁBrightcovePlayerǁget_streams__mutmut_109': xǁBrightcovePlayerǁget_streams__mutmut_109, 
        'xǁBrightcovePlayerǁget_streams__mutmut_110': xǁBrightcovePlayerǁget_streams__mutmut_110, 
        'xǁBrightcovePlayerǁget_streams__mutmut_111': xǁBrightcovePlayerǁget_streams__mutmut_111, 
        'xǁBrightcovePlayerǁget_streams__mutmut_112': xǁBrightcovePlayerǁget_streams__mutmut_112, 
        'xǁBrightcovePlayerǁget_streams__mutmut_113': xǁBrightcovePlayerǁget_streams__mutmut_113, 
        'xǁBrightcovePlayerǁget_streams__mutmut_114': xǁBrightcovePlayerǁget_streams__mutmut_114, 
        'xǁBrightcovePlayerǁget_streams__mutmut_115': xǁBrightcovePlayerǁget_streams__mutmut_115, 
        'xǁBrightcovePlayerǁget_streams__mutmut_116': xǁBrightcovePlayerǁget_streams__mutmut_116, 
        'xǁBrightcovePlayerǁget_streams__mutmut_117': xǁBrightcovePlayerǁget_streams__mutmut_117, 
        'xǁBrightcovePlayerǁget_streams__mutmut_118': xǁBrightcovePlayerǁget_streams__mutmut_118, 
        'xǁBrightcovePlayerǁget_streams__mutmut_119': xǁBrightcovePlayerǁget_streams__mutmut_119, 
        'xǁBrightcovePlayerǁget_streams__mutmut_120': xǁBrightcovePlayerǁget_streams__mutmut_120, 
        'xǁBrightcovePlayerǁget_streams__mutmut_121': xǁBrightcovePlayerǁget_streams__mutmut_121, 
        'xǁBrightcovePlayerǁget_streams__mutmut_122': xǁBrightcovePlayerǁget_streams__mutmut_122, 
        'xǁBrightcovePlayerǁget_streams__mutmut_123': xǁBrightcovePlayerǁget_streams__mutmut_123, 
        'xǁBrightcovePlayerǁget_streams__mutmut_124': xǁBrightcovePlayerǁget_streams__mutmut_124, 
        'xǁBrightcovePlayerǁget_streams__mutmut_125': xǁBrightcovePlayerǁget_streams__mutmut_125, 
        'xǁBrightcovePlayerǁget_streams__mutmut_126': xǁBrightcovePlayerǁget_streams__mutmut_126, 
        'xǁBrightcovePlayerǁget_streams__mutmut_127': xǁBrightcovePlayerǁget_streams__mutmut_127, 
        'xǁBrightcovePlayerǁget_streams__mutmut_128': xǁBrightcovePlayerǁget_streams__mutmut_128, 
        'xǁBrightcovePlayerǁget_streams__mutmut_129': xǁBrightcovePlayerǁget_streams__mutmut_129, 
        'xǁBrightcovePlayerǁget_streams__mutmut_130': xǁBrightcovePlayerǁget_streams__mutmut_130, 
        'xǁBrightcovePlayerǁget_streams__mutmut_131': xǁBrightcovePlayerǁget_streams__mutmut_131, 
        'xǁBrightcovePlayerǁget_streams__mutmut_132': xǁBrightcovePlayerǁget_streams__mutmut_132, 
        'xǁBrightcovePlayerǁget_streams__mutmut_133': xǁBrightcovePlayerǁget_streams__mutmut_133, 
        'xǁBrightcovePlayerǁget_streams__mutmut_134': xǁBrightcovePlayerǁget_streams__mutmut_134, 
        'xǁBrightcovePlayerǁget_streams__mutmut_135': xǁBrightcovePlayerǁget_streams__mutmut_135, 
        'xǁBrightcovePlayerǁget_streams__mutmut_136': xǁBrightcovePlayerǁget_streams__mutmut_136, 
        'xǁBrightcovePlayerǁget_streams__mutmut_137': xǁBrightcovePlayerǁget_streams__mutmut_137, 
        'xǁBrightcovePlayerǁget_streams__mutmut_138': xǁBrightcovePlayerǁget_streams__mutmut_138, 
        'xǁBrightcovePlayerǁget_streams__mutmut_139': xǁBrightcovePlayerǁget_streams__mutmut_139, 
        'xǁBrightcovePlayerǁget_streams__mutmut_140': xǁBrightcovePlayerǁget_streams__mutmut_140, 
        'xǁBrightcovePlayerǁget_streams__mutmut_141': xǁBrightcovePlayerǁget_streams__mutmut_141, 
        'xǁBrightcovePlayerǁget_streams__mutmut_142': xǁBrightcovePlayerǁget_streams__mutmut_142, 
        'xǁBrightcovePlayerǁget_streams__mutmut_143': xǁBrightcovePlayerǁget_streams__mutmut_143, 
        'xǁBrightcovePlayerǁget_streams__mutmut_144': xǁBrightcovePlayerǁget_streams__mutmut_144, 
        'xǁBrightcovePlayerǁget_streams__mutmut_145': xǁBrightcovePlayerǁget_streams__mutmut_145, 
        'xǁBrightcovePlayerǁget_streams__mutmut_146': xǁBrightcovePlayerǁget_streams__mutmut_146, 
        'xǁBrightcovePlayerǁget_streams__mutmut_147': xǁBrightcovePlayerǁget_streams__mutmut_147, 
        'xǁBrightcovePlayerǁget_streams__mutmut_148': xǁBrightcovePlayerǁget_streams__mutmut_148, 
        'xǁBrightcovePlayerǁget_streams__mutmut_149': xǁBrightcovePlayerǁget_streams__mutmut_149, 
        'xǁBrightcovePlayerǁget_streams__mutmut_150': xǁBrightcovePlayerǁget_streams__mutmut_150, 
        'xǁBrightcovePlayerǁget_streams__mutmut_151': xǁBrightcovePlayerǁget_streams__mutmut_151, 
        'xǁBrightcovePlayerǁget_streams__mutmut_152': xǁBrightcovePlayerǁget_streams__mutmut_152, 
        'xǁBrightcovePlayerǁget_streams__mutmut_153': xǁBrightcovePlayerǁget_streams__mutmut_153, 
        'xǁBrightcovePlayerǁget_streams__mutmut_154': xǁBrightcovePlayerǁget_streams__mutmut_154, 
        'xǁBrightcovePlayerǁget_streams__mutmut_155': xǁBrightcovePlayerǁget_streams__mutmut_155, 
        'xǁBrightcovePlayerǁget_streams__mutmut_156': xǁBrightcovePlayerǁget_streams__mutmut_156, 
        'xǁBrightcovePlayerǁget_streams__mutmut_157': xǁBrightcovePlayerǁget_streams__mutmut_157, 
        'xǁBrightcovePlayerǁget_streams__mutmut_158': xǁBrightcovePlayerǁget_streams__mutmut_158
    }
    
    def get_streams(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁBrightcovePlayerǁget_streams__mutmut_orig"), object.__getattribute__(self, "xǁBrightcovePlayerǁget_streams__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_streams.__signature__ = _mutmut_signature(xǁBrightcovePlayerǁget_streams__mutmut_orig)
    xǁBrightcovePlayerǁget_streams__mutmut_orig.__name__ = 'xǁBrightcovePlayerǁget_streams'


@pluginmatcher(
    re.compile(r"https?://players\.brightcove\.net/(?P<account_id>[^/]+)/(?P<player_id>[^/]+)/index\.html"),
)
class Brightcove(Plugin):
    def _get_streams(self):
        video_id = parse_qsd(urlparse(self.url).query).get("videoId")
        player = BrightcovePlayer(self.session, self.match.group("account_id"), self.match.group("player_id"))
        streams = dict(player.get_streams(video_id))
        self.title = player.title

        return streams


__plugin__ = Brightcove

"""
$description Esports tournaments run by BlastTV, based in Denmark.
$url blast.tv
$type live, vod
$metadata id
$metadata title
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
    name="live",
    pattern=re.compile(r"^https?://(?:www\.)?blast\.tv(?:/?$|/live(?:/(?P<channel>[a-z0-9_-]+))?)"),
)
@pluginmatcher(
    name="vod",
    pattern=re.compile(r"^https?://(?:www\.)?blast\.tv/(?P<game>[^/]+)/tournaments/[^/]+/match/(?P<shortid>\w+)/"),
)
class BlastTv(Plugin):
    _URL_API_LIVE = "https://api.blast.tv/v1/broadcasts/live"
    _URL_API_MATCHES = "https://api.blast.tv/v2/games/{game}/matches/{shortid}"
    _URL_API_REWATCH = "https://api.blast.tv/v1/videos/rewatch/{id}"

    def _get_live(self):
        channel = self.match["channel"]

        live_channels = self.session.http.get(
            self._URL_API_LIVE,
            schema=validate.Schema(
                validate.parse_json(),
                [
                    {
                        "id": str,
                        "slug": str,
                        "priority": int,
                        "title": str,
                        "videoSrc": validate.any("", validate.url(path=validate.endswith(".m3u8"))),
                        "videoAlternativeSrc": validate.any("", validate.url(scheme="http")),
                    },
                ],
            ),
        )

        for live_channel in sorted(live_channels, key=lambda x: x["priority"]):
            if channel and channel != live_channel["slug"]:
                continue

            if live_channel["videoSrc"]:
                self.id = live_channel["id"]
                self.title = live_channel["title"]
                return HLSStream.parse_variant_playlist(self.session, live_channel["videoSrc"])

            if live_channel["videoAlternativeSrc"]:
                return self.session.streams(live_channel["videoAlternativeSrc"])

    def _get_vod(self):
        self.id, external_stream_url = self.session.http.get(
            self._URL_API_MATCHES.format(
                game=self.match["game"],
                shortid=self.match["shortid"],
            ),
            acceptable_status=(200, 404),
            schema=validate.Schema(
                validate.parse_json(),
                {
                    validate.optional("id"): str,
                    validate.optional("metadata"): validate.all(
                        {
                            validate.optional("externalStreamUrl"): validate.any("", validate.url(scheme="http")),
                        },
                        validate.get("externalStreamUrl"),
                    ),
                },
                validate.union_get(
                    "id",
                    "metadata",
                ),
            ),
        )
        if not self.id:
            return

        if external_stream_url:
            return self.session.streams(external_stream_url)

        hls_url = self.session.http.get(
            self._URL_API_REWATCH.format(id=self.id),
            acceptable_status=(200, 404),
            schema=validate.Schema(
                validate.parse_json(),
                {
                    validate.optional("src"): validate.url(path=validate.endswith(".m3u8")),
                },
                validate.get("src"),
            ),
        )
        if not hls_url:
            return

        return HLSStream.parse_variant_playlist(self.session, hls_url)

    def _get_streams(self):
        if self.matches["live"]:
            return self._get_live()
        if self.matches["vod"]:
            return self._get_vod()


__plugin__ = BlastTv

"""
$description Live TV channels and video on-demand service from CCMA, a Catalan public, state-owned broadcaster.
$url 3cat.cat
$url ccma.cat
$type live, vod
$region Spain
"""

import logging
import re

from streamlink.exceptions import NoStreamsError, PluginError
from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.dash import DASHStream
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
    name="live",
    pattern=re.compile(r"https://(?:www)?\.(?:3cat|ccma)\.cat/3cat/directes/(?P<ident>[^/?]+)"),
)
@pluginmatcher(
    name="vod",
    pattern=re.compile(r"https://(?:www)?\.(?:3cat|ccma)\.cat/3cat/[^/]+/video/(?P<ident>\d+)"),
)
class TV3Cat(Plugin):
    _URL_API_GEO = "https://dinamics.ccma.cat/geo.json"
    _URL_API_MEDIA = "https://api-media.ccma.cat/pvideo/media.jsp"

    _MAP_CHANNEL_IDENTS = {
        "catalunya-radio": "cr",
        "catalunya-informacio": "ci",
        "catalunya-musica": "cm",
        "icat": "ic",
    }

    def _call_api_media(self, fmt, schema, params):
        geo = self.session.http.get(
            self._URL_API_GEO,
            schema=validate.Schema(
                validate.parse_json(),
                {"geo": str},
                validate.get("geo"),
            ),
        )
        if not geo:
            raise PluginError("Missing 'geo' value")

        log.debug(f"{geo=}")
        schema = validate.all(
            {
                "geo": str,
                "format": fmt,
                "url": schema,
            },
            validate.union_get("geo", "url"),
        )

        ident = self.match["ident"]
        streams = self.session.http.get(
            self._URL_API_MEDIA,
            params={
                "media": "video",
                "versio": "vast",
                "idint": self._MAP_CHANNEL_IDENTS.get(ident, ident),
                "profile": "pc_3cat",
                **(params or {}),
            },
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "media": validate.any(
                        [schema],
                        validate.all(
                            schema,
                            validate.transform(lambda item: [item]),
                        ),
                    ),
                },
                validate.get("media"),
            ),
        )

        log.debug(f"{streams=}")
        for _geo, data in streams:
            if _geo == geo:
                return data

        log.error("The content is geo-blocked")
        raise NoStreamsError

    def _get_live(self):
        schema = validate.url(path=validate.endswith(".m3u8"))
        url = self._call_api_media("HLS", schema, {"desplacament": 0})
        return HLSStream.parse_variant_playlist(self.session, url)

    def _get_vod(self):
        schema = [
            validate.all(
                {
                    "label": str,
                    "file": validate.url(),
                },
                validate.union_get("label", "file"),
            ),
        ]
        urls = self._call_api_media("MP4", schema, {"format": "dm"})
        for label, url in urls:
            if label == "DASH":
                yield from DASHStream.parse_manifest(self.session, url).items()
            else:
                yield label, HTTPStream(self.session, url)

    def _get_streams(self):
        if self.matches["live"]:
            return self._get_live()
        else:
            return self._get_vod()


__plugin__ = TV3Cat

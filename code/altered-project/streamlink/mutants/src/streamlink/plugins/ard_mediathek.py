"""
$description Live TV channels and video on-demand service from ARD, a German public, independent broadcaster.
$url ardmediathek.de
$url mediathek.daserste.de
$type live, vod
$metadata title
$region Germany
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
    name="live",
    pattern=re.compile(r"https?://(\w+\.)?ardmediathek\.de/live/(?:[^/]+/)?(?P<id_live>\w+)(?:\?|$)"),
)
@pluginmatcher(
    name="video",
    pattern=re.compile(r"https?://(\w+\.)?ardmediathek\.de/video/(?:[^/]+/[^/]+/[^/]+/)?(?P<id_video>\w+)(?:\?|$)"),
)
class ARDMediathek(Plugin):
    _URL_API = "https://api.ardmediathek.de/page-gateway/pages/ard/item/{item}"
    _QUALITY_MAP = {
        4: "1080p",
        3: "720p",
        2: "540p",
        1: "360p",
        0: "270p",
    }

    def _get_streams(self):
        data_json = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//script[@type='application/json'][@id='fetchedContextValue2'][1]/text()"),
                validate.none_or_all(
                    validate.parse_json(),
                    [validate.list(str, {"data": dict})],
                    validate.filter(lambda item: item[0].startswith("https://api.ardmediathek.de/page-gateway/pages/")),
                    validate.any(
                        validate.get((0, 1, "data")),
                        [],
                    ),
                ),
            ),
        )
        if not data_json:
            data_json = self.session.http.get(
                self._URL_API.format(item=self.match["id_live"] if self.matches["live"] else self.match["id_video"]),
                params={
                    "devicetype": "pc",
                    "embedded": "false",
                },
                schema=validate.Schema(validate.parse_json()),
            )
        if not data_json:
            return

        schema_data = validate.Schema({
            "id": str,
            "widgets": validate.all(
                [dict],
                validate.filter(lambda item: item.get("mediaCollection")),
                validate.get(0),
                validate.any(
                    None,
                    validate.all(
                        {
                            "geoblocked": bool,
                            "publicationService": {
                                "name": str,
                            },
                            "show": validate.any(
                                None,
                                validate.all(
                                    {"title": str},
                                    validate.get("title"),
                                ),
                            ),
                            "title": str,
                            "mediaCollection": {
                                "embedded": {
                                    "_mediaArray": [
                                        validate.all(
                                            {
                                                "_mediaStreamArray": [
                                                    validate.all(
                                                        {
                                                            "_quality": validate.any(str, int),
                                                            "_stream": validate.url(),
                                                        },
                                                        validate.union_get("_quality", "_stream"),
                                                    ),
                                                ],
                                            },
                                            validate.get("_mediaStreamArray"),
                                            validate.transform(dict),
                                        ),
                                    ],
                                },
                            },
                        },
                        validate.union_get(
                            "geoblocked",
                            ("mediaCollection", "embedded", "_mediaArray", 0),
                            ("publicationService", "name"),
                            "title",
                            "show",
                        ),
                    ),
                ),
            ),
        })
        data = schema_data.validate(data_json)

        log.debug(f"Found media id: {data['id']}")
        if not data["widgets"]:
            log.info("The content is unavailable")
            return

        geoblocked, media, self.author, self.title, show = data["widgets"]
        if geoblocked:
            log.info("The content is not available in your region")
            return
        if show:
            self.title = f"{show}: {self.title}"

        if media.get("auto"):
            yield from HLSStream.parse_variant_playlist(self.session, media.get("auto")).items()
        else:
            for quality, stream in media.items():
                yield self._QUALITY_MAP.get(quality, quality), HTTPStream(self.session, stream)


__plugin__ = ARDMediathek

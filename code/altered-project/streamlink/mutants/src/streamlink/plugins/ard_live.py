"""
$description Live TV channels and video on-demand service from ARD, a German public, independent broadcaster.
$url daserste.de
$type live, vod
$metadata title
$region Germany
"""

import logging
import re
from urllib.parse import urljoin

from streamlink.plugin import Plugin, PluginError, pluginmatcher
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
    re.compile(r"https?://((www|live)\.)?daserste\.de/"),
)
class ARDLive(Plugin):
    _URL_DATA_BASE = "https://www.daserste.de/"
    _QUALITY_MAP = {
        4: "1080p",
        3: "720p",
        2: "540p",
        1: "270p",
        0: "180p",
    }

    def _get_streams(self):
        try:
            data_url = self.session.http.get(
                self.url,
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_find(".//*[@data-ctrl-player]"),
                    validate.get("data-ctrl-player"),
                    validate.transform(lambda s: s.replace("'", '"')),
                    validate.parse_json(),
                    {"url": str},
                    validate.get("url"),
                ),
            )
        except PluginError:
            return

        data_url = urljoin(self._URL_DATA_BASE, data_url)
        log.debug(f"Player URL: '{data_url}'")

        self.title, media = self.session.http.get(
            data_url,
            schema=validate.Schema(
                validate.parse_json(name="MEDIAINFO"),
                {
                    "mc": {
                        validate.optional("_title"): str,
                        "_mediaArray": [
                            validate.all(
                                {
                                    "_mediaStreamArray": [
                                        validate.all(
                                            {
                                                "_quality": validate.any(str, int),
                                                "_stream": [validate.url()],
                                            },
                                            validate.union_get("_quality", ("_stream", 0)),
                                        ),
                                    ],
                                },
                                validate.get("_mediaStreamArray"),
                                validate.transform(dict),
                            ),
                        ],
                    },
                },
                validate.get("mc"),
                validate.union_get("_title", ("_mediaArray", 0)),
            ),
        )

        if media.get("auto"):
            yield from HLSStream.parse_variant_playlist(self.session, media.get("auto")).items()
        else:
            for quality, stream in media.items():
                yield self._QUALITY_MAP.get(quality, quality), HTTPStream(self.session, stream)


__plugin__ = ARDLive

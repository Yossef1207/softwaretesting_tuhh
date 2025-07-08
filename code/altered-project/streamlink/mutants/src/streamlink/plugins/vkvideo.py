"""
$description Russian live-streaming platform for gaming and esports, owned by VKontakte. Formerly called vkplay.
$url live.vkvideo.ru
$url live.vkplay.ru
$url vkplay.live
$type live
$metadata id
$metadata author
$metadata category
$metadata title
"""

import logging
import re

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
    re.compile(r"https?://(?:live\.vkvideo\.ru|live\.vkplay\.ru|vkplay\.live)/(?P<channel_name>\w+)/?$"),
)
class VKvideo(Plugin):
    API_URL = "https://api.live.vkvideo.ru/v1"

    def _get_streams(self):
        self.author = self.match["channel_name"]
        log.debug(f"Channel name: {self.author}")

        data = self.session.http.get(
            f"{self.API_URL}/blog/{self.author}/public_video_stream",
            headers={"Referer": self.url},
            acceptable_status=(200, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {"error": str, "error_description": str},
                        validate.get("error_description"),
                    ),
                    validate.all(
                        {
                            validate.optional("category"): validate.all(
                                {
                                    "title": str,
                                },
                                validate.get("title"),
                            ),
                            "title": str,
                            "data": validate.any(
                                [
                                    validate.all(
                                        {
                                            "vid": str,
                                            "playerUrls": [
                                                validate.all(
                                                    {
                                                        "type": str,
                                                        "url": validate.any("", validate.url()),
                                                    },
                                                    validate.union_get("type", "url"),
                                                ),
                                            ],
                                        },
                                        validate.union_get("vid", "playerUrls"),
                                    ),
                                ],
                                [],
                            ),
                        },
                        validate.union_get(
                            "category",
                            "title",
                            ("data", 0),
                        ),
                    ),
                ),
            ),
        )
        if isinstance(data, str):
            log.error(data)
            return

        self.category, self.title, streamdata = data
        if not streamdata:
            return

        self.id, streams = streamdata

        for streamtype, streamurl in streams:
            if streamurl and streamtype == "live_hls":
                return HLSStream.parse_variant_playlist(self.session, streamurl)


__plugin__ = VKvideo

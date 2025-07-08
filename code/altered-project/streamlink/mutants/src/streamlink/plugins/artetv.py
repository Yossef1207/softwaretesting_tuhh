"""
$description European public service channel promoting culture, including magazine shows, concerts and documentaries.
$url arte.tv
$type live, vod
$metadata id
$metadata title
"""

import logging
import re
from operator import itemgetter

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
    name="live",
    pattern=re.compile(
        r"https?://(?:\w+\.)?arte\.tv/(?P<language>[a-z]{2})/(?:direct|live)/?",
    ),
)
@pluginmatcher(
    name="vod",
    pattern=re.compile(
        r"https?://(?:\w+\.)?arte\.tv/(?:guide/)?(?P<language>[a-z]{2})/(?:videos/)?(?P<video_id>(?!RC-|videos)[^/]+?)/.+",
    ),
)
class ArteTV(Plugin):
    API_URL = "https://api.arte.tv/api/player/v2/config/{language}/{id}"

    def _get_streams(self):
        self.id = self.match["video_id"] if self.matches["vod"] else "LIVE"

        json_url = self.API_URL.format(
            language=self.match["language"],
            id=self.id,
        )
        streams, metadata = self.session.http.get(
            json_url,
            schema=validate.Schema(
                validate.parse_json(),
                {"data": {"attributes": dict}},
                validate.get(("data", "attributes")),
                {
                    "streams": validate.any(
                        [],
                        [
                            validate.all(
                                {
                                    "slot": int,
                                    "protocol": str,
                                    "url": validate.url(),
                                },
                                validate.union_get("slot", "protocol", "url"),
                            ),
                        ],
                    ),
                    "metadata": {
                        "title": str,
                        "subtitle": validate.any(None, str),
                    },
                },
                validate.union_get("streams", "metadata"),
            ),
        )

        self.title = f"{metadata['title']} - {metadata['subtitle']}" if metadata["subtitle"] else metadata["title"]

        for _slot, protocol, url in sorted(streams, key=itemgetter(0)):
            if "HLS" not in protocol:
                continue
            return HLSStream.parse_variant_playlist(self.session, url)


__plugin__ = ArteTV

"""
$description Global live-streaming platform for the creative community.
$url piczel.tv
$type live
$metadata id
$metadata author
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
    re.compile(r"https?://piczel\.tv/watch/(?P<channel>\w+)"),
)
class Piczel(Plugin):
    _URL_STREAMS = "https://piczel.tv/api/streams"
    _URL_HLS = "https://playback.piczel.tv/live/{id}/llhls.m3u8?_HLS_legacy=YES"

    def _get_streams(self):
        channel = self.match.group("channel")

        data = self.session.http.get(
            self._URL_STREAMS,
            params={
                "followedStreams": "false",
                "live_only": "false",
                "sfw": "false",
            },
            schema=validate.Schema(
                validate.parse_json(),
                [
                    {
                        "slug": str,
                        "live": bool,
                        "id": int,
                        "username": str,
                        "title": str,
                    },
                ],
                validate.filter(lambda item: item["slug"] == channel),
                validate.get(0),
                validate.any(
                    None,
                    validate.union_get(
                        "id",
                        "username",
                        "title",
                        "live",
                    ),
                ),
            ),
        )
        if not data:
            return

        self.id, self.author, self.title, is_live = data
        if not is_live:
            return

        return HLSStream.parse_variant_playlist(self.session, self._URL_HLS.format(id=self.id))


__plugin__ = Piczel

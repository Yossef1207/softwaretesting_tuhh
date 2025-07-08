"""
$description Live TV channels from DR, a Danish public, state-owned broadcaster.
$url dr.dk
$type live
$region Denmark
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
    re.compile(r"https?://(?:www\.)?dr\.dk/drtv(/kanal/[\w-]+)"),
)
class DRDK(Plugin):
    live_api_url = "https://www.dr-massive.com/api/page"

    _live_data_schema = validate.Schema(
        {
            "item": {
                "customFields": {
                    validate.optional("hlsURL"): validate.url(),
                    validate.optional("hlsWithSubtitlesURL"): validate.url(),
                },
            },
        },
        validate.get("item"),
        validate.get("customFields"),
    )

    def _get_live(self, path):
        params = dict(
            ff="idp",
            path=path,
        )
        res = self.session.http.get(self.live_api_url, params=params)
        playlists = self.session.http.json(res, schema=self._live_data_schema)

        streams = {}
        for name, url in playlists.items():
            name_prefix = ""
            if name == "hlsWithSubtitlesURL":
                name_prefix = "subtitled_"

            streams.update(
                HLSStream.parse_variant_playlist(
                    self.session,
                    url,
                    name_prefix=name_prefix,
                ),
            )

        return streams

    def _get_streams(self):
        path = self.match.group(1)
        log.debug("Path={0}".format(path))

        return self._get_live(path)


__plugin__ = DRDK

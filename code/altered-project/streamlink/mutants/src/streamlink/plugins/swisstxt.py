"""
$description Live TV channels from RSI and SRF, operations of SRG SSR, a Swiss public broadcaster.
$url srf.ch
$url rsi.ch
$type live
$region Switzerland
"""

import logging
import re
from urllib.parse import parse_qsl, urlparse, urlunparse

from streamlink.plugin import Plugin, pluginmatcher
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
    re.compile(r"https?://(?:live\.(rsi)\.ch/|(?:www\.)?(srf)\.ch/sport/resultcenter)"),
)
class Swisstxt(Plugin):
    api_url = "http://event.api.swisstxt.ch/v1/stream/{site}/byEventItemIdAndType/{id}/HLS"

    def get_stream_url(self, event_id):
        site = self.match.group(1) or self.match.group(2)
        api_url = self.api_url.format(id=event_id, site=site.upper())
        log.debug("Calling API: {0}".format(api_url))

        stream_url = self.session.http.get(api_url).text.strip("\"'")

        parsed = urlparse(stream_url)
        query = dict(parse_qsl(parsed.query))
        return urlunparse(parsed._replace(query="")), query

    def _get_streams(self):
        event_id = dict(parse_qsl(urlparse(self.url).query.lower())).get("eventid")
        if event_id is None:
            return

        stream_url, params = self.get_stream_url(event_id)
        return HLSStream.parse_variant_playlist(self.session, stream_url, params=params)


__plugin__ = Swisstxt

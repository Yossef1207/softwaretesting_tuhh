"""
$description Live TV channels from LTV, a Latvian public, state-owned broadcaster.
$url ltv.lsm.lv
$url replay.lsm.lv
$type live, vod
$region Latvia
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
    re.compile(r"https://(?:ltv|replay)\.lsm\.lv/(?:lv/tiesraide|ru/efir)/"),
)
class LtvLsmLv(Plugin):
    URL_API = "https://player.cloudycdn.services/player/ltvlive/channel/{channel_id}/"

    def _get_streams(self):
        self.session.http.headers.update({"Referer": self.url})

        iframe_url = self.session.http.get(
            self.url,
            schema=validate.Schema(
                re.compile(r"""(?P<q>")https:\\u002F\\u002Fltv\.lsm\.lv\\u002Fembed\\u002Flive\?\S+?(?P=q)"""),
                validate.none_or_all(
                    validate.get(0),
                    validate.parse_json(),
                ),
            ),
        )
        if not iframe_url:
            log.error("Could not find video player iframe")
            return

        starts_at, channel_id = self.session.http.get(
            iframe_url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//live[1]/@*[name()=':embed-data']"),
                str,
                validate.parse_json(),
                {
                    "parentInfo": {"starts_at": validate.any(None, str)},
                    "source": {"item_id": str},
                },
                validate.union_get(
                    ("parentInfo", "starts_at"),
                    ("source", "item_id"),
                ),
            ),
        )
        if channel_id is None:
            return
        log.debug(f"Found channel ID: {channel_id}")

        if starts_at is not None:
            log.error(f"Stream starts at {starts_at}")
            return

        stream_sources = self.session.http.post(
            self.URL_API.format(channel_id=channel_id),
            data={
                "refer": "ltv.lsm.lv",
                "playertype": "regular",
                "protocol": "hls",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "source": {
                        "sources": validate.all(
                            [{"type": str, "src": validate.url()}],
                            validate.filter(lambda src: src["type"] == "application/x-mpegURL"),
                            validate.map(lambda src: src.get("src")),
                        ),
                    },
                },
                validate.get(("source", "sources")),
            ),
        )
        for surl in stream_sources:
            yield from HLSStream.parse_variant_playlist(self.session, surl).items()


__plugin__ = LtvLsmLv

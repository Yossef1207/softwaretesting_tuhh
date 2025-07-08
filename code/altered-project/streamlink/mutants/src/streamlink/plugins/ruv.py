"""
$description Live TV channels and video on-demand service from RUV, an Icelandic public, state-owned broadcaster.
$url ruv.is
$type live, vod
$region Iceland
"""

import logging
import re
from textwrap import dedent

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
    pattern=re.compile(r"https?://(?:www\.)?ruv\.is/(?:sjonvarp|utvarp)/beint/(?P<channel>\w+)$"),
)
@pluginmatcher(
    name="vod",
    pattern=re.compile(r"https?://(?:www\.)?ruv\.is/(?:sjonvarp|utvarp)/spila/[^/]+/(?P<id>\d+)/(?P<episode>[^/]+)/?"),
)
class Ruv(Plugin):
    _URL_API_CHANNEL = "https://geo.spilari.ruv.is/channel/{channel}"
    _URL_API_GQL = "https://spilari.nyr.ruv.is/gql/"

    def _get_live(self):
        url = self.session.http.get(
            self._URL_API_CHANNEL.format(channel=self.match["channel"]),
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "url": validate.url(),
                },
                validate.get("url"),
            ),
        )
        if self.session.http.head(url, raise_for_status=False).status_code >= 400:
            log.error("The content is not available in your region")
            return

        return HLSStream.parse_variant_playlist(self.session, url)

    def _get_vod(self):
        query = f"""
            query getProgram($id: Int!) {{
              Program(id: $id) {{
                title
                episodes(limit: 1, id: {{value: "{self.match["episode"]}"}}) {{
                  title
                  file
                }}
              }}
            }}
        """

        self.author, self.title, url = self.session.http.post(
            self._URL_API_GQL,
            json={
                "operationName": "getProgram",
                "query": dedent(query).strip(),
                "variables": {
                    "id": int(self.match["id"]),
                },
            },
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "data": {
                        "Program": {
                            "episodes": validate.list(
                                {
                                    "file": validate.url(),
                                    "title": str,
                                },
                            ),
                            "title": str,
                        },
                    },
                },
                validate.get(("data", "Program")),
                validate.union_get(
                    "title",
                    ("episodes", 0, "title"),
                    ("episodes", 0, "file"),
                ),
            ),
        )

        if not url.endswith(".m3u8"):
            return {"vod": HTTPStream(self.session, url)}
        else:
            return HLSStream.parse_variant_playlist(self.session, url)

    def _get_streams(self):
        if self.matches["live"]:
            return self._get_live()
        else:
            return self._get_vod()


__plugin__ = Ruv

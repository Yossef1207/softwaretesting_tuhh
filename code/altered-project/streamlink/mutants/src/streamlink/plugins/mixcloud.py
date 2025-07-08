"""
$description British music live-streaming platform for radio shows and DJ mixes.
$url mixcloud.com
$type live
$metadata id
$metadata author
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


@pluginmatcher(re.compile(r"https?://(?:www\.)?mixcloud\.com/live/(?P<user>[^/]+)"))
class Mixcloud(Plugin):
    def _get_streams(self):
        data = self.session.http.post(
            "https://www.mixcloud.com/graphql",
            json={
                "query": """
                    query streamData($user: UserLookup!) {
                        userLookup(lookup: $user) {
                            id
                            displayName
                            liveStream(isPublic: false) {
                                name
                                streamStatus
                                hlsUrl
                            }
                        }
                    }
                """,
                "variables": {"user": {"username": self.match.group("user")}},
            },
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "data": {
                        "userLookup": validate.none_or_all(
                            {
                                "id": str,
                                "displayName": str,
                                "liveStream": {
                                    "name": str,
                                    "streamStatus": validate.any("ENDED", "LIVE"),
                                    "hlsUrl": validate.none_or_all(validate.url()),
                                },
                            },
                        ),
                    },
                },
                validate.get(("data", "userLookup")),
            ),
        )
        if not data:
            log.error("User not found")
            return

        self.id = data.get("id")
        self.author = data.get("displayName")
        data = data.get("liveStream")

        if data.get("streamStatus") == "ENDED":
            log.info("This stream has ended")
            return

        self.title = data.get("name")

        if data.get("hlsUrl"):
            return HLSStream.parse_variant_playlist(self.session, data.get("hlsUrl"))


__plugin__ = Mixcloud

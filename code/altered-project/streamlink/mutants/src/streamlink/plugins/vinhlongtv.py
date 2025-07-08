"""
$description Vietnamese live TV channels from THVL, including THVL1, THVL2, THVL3 and THVL4.
$url thvli.vn
$type live
$metadata id
$metadata title
$region Vietnam
"""

import logging
import re
from datetime import datetime, timezone
from hashlib import md5

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
    re.compile(r"https?://(?:www\.)?thvli\.vn/live/(?P<channel>[^/]+)"),
)
class VinhLongTV(Plugin):
    _API_URL = "https://api.thvli.vn/backend/cm/get_detail/{channel}/"
    _API_KEY_DATE = "Kh0ngDuLieu"
    _API_KEY_TIME = "C0R0i"
    _API_KEY_SECRET = "Kh0aAnT0an"

    def _get_headers(self):
        now = datetime.now(tz=timezone.utc)
        date = now.strftime("%Y%m%d")
        time = now.strftime("%H%M%S")
        dtstr = f"{date}{time}"
        dthash = md5(dtstr.encode()).hexdigest()
        key_value = f"{dthash[:3]}{dthash[-3:]}"
        key_access = f"{self._API_KEY_DATE}{date}{self._API_KEY_TIME}{time}{self._API_KEY_SECRET}{key_value}"

        return {
            "X-SFD-Date": dtstr,
            "X-SFD-Key": md5(key_access.encode()).hexdigest(),
        }

    def _get_streams(self):
        channel = self.match.group("channel")
        params = {"timezone": "UTC"}
        headers = self._get_headers()

        self.id, self.title, hls_url = self.session.http.get(
            self._API_URL.format(channel=channel),
            params=params,
            headers=headers,
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "id": str,
                    "title": str,
                    "link_play": str,
                },
                validate.union_get(
                    "id",
                    "title",
                    "link_play",
                ),
            ),
        )

        return HLSStream.parse_variant_playlist(self.session, hls_url)


__plugin__ = VinhLongTV

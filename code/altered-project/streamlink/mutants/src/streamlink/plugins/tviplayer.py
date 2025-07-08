"""
$description Live TV channels and video on-demand service from TVI, a Portuguese free-to-air broadcaster.
$url tviplayer.iol.pt
$type live, vod
"""

import logging
import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream
from streamlink.utils.url import update_qsd


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
    re.compile(r"https://tviplayer\.iol\.pt/(?:direto|programa)/"),
)
class TVIPlayer(Plugin):
    def _get_streams(self):
        self.session.http.headers.update({"Referer": "https://tviplayer.iol.pt/"})
        data = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//script[contains(text(),'.m3u8')]/text()"),
                validate.none_or_all(
                    re.compile(r"jsonData\s*=\s*(?P<json>{.+?})\s*;", re.DOTALL),
                    validate.none_or_all(
                        validate.get("json"),
                        validate.parse_json(),
                        {
                            "id": str,
                            "liveType": str,
                            "videoType": str,
                            "videoUrl": validate.url(path=validate.endswith(".m3u8")),
                            validate.optional("channel"): str,
                        },
                    ),
                ),
            ),
        )
        if not data:
            return
        log.debug(f"{data!r}")

        if data["liveType"].upper() == "DIRETO" and data["videoType"].upper() == "LIVE":
            geo_path = "live"
        else:
            geo_path = "vod"
        data_geo = self.session.http.get(
            f"https://services.iol.pt/direitos/rights/{geo_path}?id={data['id']}",
            acceptable_status=(200, 403),
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "code": str,
                    "error": validate.any(None, str),
                    "detail": str,
                },
            ),
        )
        log.debug(f"{data_geo!r}")
        if data_geo["detail"] != "ok":
            log.error(f"{data_geo['detail']}")
            return

        wmsAuthSign = self.session.http.get(
            "https://services.iol.pt/matrix?userId=",
            schema=validate.Schema(str),
        )
        hls_url = update_qsd(data["videoUrl"], {"wmsAuthSign": wmsAuthSign})
        return HLSStream.parse_variant_playlist(self.session, hls_url)


__plugin__ = TVIPlayer

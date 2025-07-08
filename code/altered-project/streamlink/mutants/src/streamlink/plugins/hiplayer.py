"""
$description United Arab Emirates CDN hosting live content for various websites in The Middle East.
$url alwasat.ly
$type live
$region various
"""

import base64
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


@pluginmatcher(name="alwasatly", pattern=re.compile(r"https?://(?:www\.)?alwasat\.ly"))
class HiPlayer(Plugin):
    DAI_URL = "https://pubads.g.doubleclick.net/ssai/event/{0}/streams"

    def _get_streams(self):
        js_url = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//script[contains(text(), 'https://hiplayer.hibridcdn.net/l/')]/text()"),
                validate.none_or_all(
                    re.compile(r"""(?P<q>['"])(?P<url>https://hiplayer.hibridcdn.net/l/.+?)(?P=q)"""),
                    validate.none_or_all(
                        validate.get("url"),
                        validate.url(),
                    ),
                ),
            ),
        )
        if not js_url:
            log.error("Could not find JS URL")
            return

        log.debug(f"JS URL={js_url}")

        data = self.session.http.get(
            js_url,
            schema=validate.Schema(
                re.compile(r"\[(?P<data>[^]]+)]\.join\([\"']{2}\)"),
                validate.none_or_all(
                    validate.get("data"),
                    validate.transform(lambda s: re.sub(r"['\", ]", "", s)),
                    validate.transform(base64.b64decode),
                    validate.parse_json(),
                    validate.any(
                        None,
                        {
                            "daiEnabled": bool,
                            "daiAssetKey": str,
                            "daiApiKey": str,
                            "streamUrl": validate.any(validate.url(), ""),
                        },
                    ),
                ),
            ),
        )
        if not data:
            log.error("Could not find base64 encoded JSON data")
            return

        hls_url = data["streamUrl"]

        if data["daiEnabled"]:
            log.debug("daiEnabled=true")
            hls_url = self.session.http.post(
                self.DAI_URL.format(data["daiAssetKey"]),
                data={"api-key": data["daiApiKey"]},
                schema=validate.Schema(
                    validate.parse_json(),
                    {
                        "stream_manifest": validate.url(),
                    },
                    validate.get("stream_manifest"),
                ),
            )

        if hls_url:
            return HLSStream.parse_variant_playlist(self.session, hls_url)


__plugin__ = HiPlayer

"""
$description Live TV channels and video on-demand service from RTP, a Portuguese public, state-owned broadcaster.
$url rtp.pt/play
$type live, vod
$region Portugal
"""

import re
from base64 import b64decode
from urllib.parse import unquote

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import useragents, validate
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
    re.compile(r"https?://www\.rtp\.pt/play/"),
)
class RTPPlay(Plugin):
    def _get_streams(self):
        self.session.http.headers.update({
            "User-Agent": useragents.CHROME,
            "Referer": self.url,
        })

        re_m3u8 = re.compile(
            r"""
                hls\s*:\s*(?:
                    (?P<q>["'])(?P<string>.*?)(?P=q)
                    |
                    decodeURIComponent\s*\((?P<obfuscated>\[.*?])\.join\(
                    |
                    atob\s*\(\s*decodeURIComponent\s*\((?P<obfuscated_b64>\[.*?])\.join\(
                )
            """,
            re.VERBOSE,
        )

        hls_url = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.transform(lambda text: next(reversed(list(re_m3u8.finditer(text))), None)),
                validate.any(
                    None,
                    validate.all(
                        validate.get("string"),
                        str,
                        validate.any(
                            "",
                            validate.url(),
                        ),
                    ),
                    validate.all(
                        validate.get("obfuscated"),
                        str,
                        validate.parse_json(),
                        validate.transform(lambda arr: unquote("".join(arr))),
                        validate.url(),
                    ),
                    validate.all(
                        validate.get("obfuscated_b64"),
                        str,
                        validate.parse_json(),
                        validate.transform(lambda arr: unquote("".join(arr))),
                        validate.transform(lambda b64: b64decode(b64).decode("utf-8")),
                        validate.url(),
                    ),
                ),
            ),
        )
        if hls_url:
            return HLSStream.parse_variant_playlist(self.session, hls_url)


__plugin__ = RTPPlay

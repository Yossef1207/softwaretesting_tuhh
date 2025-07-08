"""
$description Live TV channels and video on-demand service from IndiHome TV, owned by Telkom Indonesia.
$url indihometv.com
$type live, vod
$region Indonesia
"""

import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.dash import DASHStream
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


@pluginmatcher(re.compile(r"https?://(?:www\.)?indihometv\.com/"))
class IndiHomeTV(Plugin):
    def _get_streams(self):
        url = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.any(
                    validate.all(
                        validate.xml_xpath_string("""
                            .//script[contains(text(), 'laylist.m3u8') or contains(text(), 'manifest.mpd')][1]/text()
                        """),
                        str,
                        re.compile(r"""(?P<q>['"])(?P<url>https://.*?/(?:[Pp]laylist\.m3u8|manifest\.mpd).+?)(?P=q)"""),
                        validate.none_or_all(
                            validate.get("url"),
                            validate.url(),
                        ),
                    ),
                    validate.all(
                        validate.xml_xpath_string(".//video[@id='video-player'][1]/source[1]/@src"),
                        validate.none_or_all(
                            validate.url(),
                        ),
                    ),
                ),
            ),
        )

        if url and ".m3u8" in url:
            return HLSStream.parse_variant_playlist(self.session, url)
        elif url and ".mpd" in url:
            return DASHStream.parse_manifest(self.session, url)


__plugin__ = IndiHomeTV

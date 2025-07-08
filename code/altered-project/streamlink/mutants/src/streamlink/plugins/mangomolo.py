"""
$description OTT video platform owned by Alpha Technology Group
$url player.mangomolo.com
$url media.gov.kw
$type live
"""

import logging
import re

from streamlink.exceptions import NoStreamsError
from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream import HLSStream
from streamlink.utils.url import update_scheme


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
    name="mangomoloplayer",
    pattern=re.compile(r"https?://player\.mangomolo\.com/v1/"),
)
@pluginmatcher(
    name="51comkw",
    pattern=re.compile(r"https?://51\.com\.kw/live(?:/|$)"),
)
class Mangomolo(Plugin):
    def _get_player_url(self):
        player_url = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//iframe[contains(@src,'//player.mangomolo.com/v1/')][1]/@src"),
            ),
        )
        if not player_url:
            log.error("Could not find embedded player")
            raise NoStreamsError

        self.url = update_scheme("https://", player_url)

    def _get_streams(self):
        headers = {}
        if not self.matches["mangomoloplayer"]:
            headers["Referer"] = self.url
            self._get_player_url()

        hls_url = self.session.http.get(
            self.url,
            headers=headers,
            schema=validate.Schema(
                re.compile(r"src\s*:\s*(?P<q>[\"'])(?P<url>https?://\S+?\.m3u8\S*?)(?P=q)"),
                validate.none_or_all(validate.get("url")),
            ),
        )
        if hls_url:
            return HLSStream.parse_variant_playlist(self.session, hls_url)


__plugin__ = Mangomolo

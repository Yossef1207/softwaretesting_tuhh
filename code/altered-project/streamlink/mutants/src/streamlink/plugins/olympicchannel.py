"""
$description Live TV channel and video on-demand service run by the International Olympic Committee.
$url olympicchannel.com
$url olympics.com
$type live, vod
$notes Only non-premium content is available
"""

import logging
import re
from time import time
from urllib.parse import urljoin, urlparse

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
    re.compile(r"https?://(\w+\.)?(?:olympics|olympicchannel)\.com/(?:[\w-]+/)?../.+"),
)
class OlympicChannel(Plugin):
    def _get_streams(self):
        data = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.union((
                    validate.xml_xpath_string(".//*[@data-content-url][1]/@data-content-url"),
                    validate.xml_xpath_string(".//*[@data-d3vp-plugin='THEOplayer'][@data-content][1]/@data-content"),
                )),
            ),
        )
        if not data:
            return

        api_url, api_data = data
        api_schema = validate.Schema(
            validate.parse_json(),
            [
                {
                    validate.optional("src"): validate.url(),
                    validate.optional("srcType"): "HLS",
                },
            ],
            validate.get((0, "src")),
        )
        if api_data:
            stream_url = api_schema.validate(api_data)
        else:
            stream_url = self.session.http.get(
                urljoin(self.url, api_url),
                headers={"Referer": self.url},
                schema=api_schema,
            )

        parsed = urlparse(stream_url)
        stream_url = self.session.http.get(
            urljoin(self.url, "/tokenGenerator"),
            params={
                "url": stream_url,
                "domain": f"{parsed.scheme}://{parsed.netloc}",
                "_ts": int(time()),
            },
            headers={"Referer": self.url},
            schema=validate.Schema(
                validate.parse_json(),
                validate.url(),
            ),
        )
        return HLSStream.parse_variant_playlist(self.session, stream_url)


__plugin__ = OlympicChannel

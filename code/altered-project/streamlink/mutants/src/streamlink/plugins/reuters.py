"""
$description Global business, financial, national and international news.
$url reuters.com
$url reuters.tv
$type live, vod
"""

import logging
import re

from streamlink.plugin import Plugin, PluginError, pluginmatcher
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
    re.compile(r"https?://([\w-]+\.)*reuters\.(com|tv)"),
)
class Reuters(Plugin):
    def _get_data(self):
        root = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
            ),
        )

        try:
            log.debug("Trying to find source via meta tag")
            schema = validate.Schema(
                validate.xml_xpath_string(".//meta[@property='og:video'][1]/@content"),
                validate.url(),
            )
            return schema.validate(root)
        except PluginError:
            pass

        try:
            log.debug("Trying to find source via next-head")
            schema = validate.Schema(
                validate.xml_findtext(".//script[@type='application/ld+json'][@class='next-head']"),
                validate.parse_json(),
                {"contentUrl": validate.url()},
                validate.get("contentUrl"),
            )
            return schema.validate(root)
        except PluginError:
            pass

        schema_fusion = validate.xml_findtext(".//script[@type='application/javascript'][@id='fusion-metadata']")
        schema_video = validate.all(
            {"source": {"hls": validate.url()}},
            validate.get(("source", "hls")),
        )
        try:
            log.debug("Trying to find source via fusion-metadata globalContent")
            schema = validate.Schema(
                schema_fusion,
                validate.regex(re.compile(r"Fusion\s*\.\s*globalContent\s*=\s*(?P<json>{.+?})\s*;\s*Fusion\s*\.", re.DOTALL)),
                validate.get("json"),
                validate.parse_json(),
                {"result": {"related_content": {"videos": list}}},
                validate.get(("result", "related_content", "videos", 0)),
                schema_video,
            )
            return schema.validate(root)
        except PluginError:
            pass

        try:
            log.debug("Trying to find source via fusion-metadata contentCache")
            schema = validate.Schema(
                schema_fusion,
                validate.regex(re.compile(r"Fusion\s*\.\s*contentCache\s*=\s*(?P<json>{.+?})\s*;\s*Fusion\s*\.", re.DOTALL)),
                validate.get("json"),
                validate.parse_json(),
                {"videohub-by-guid-v1": {str: {"data": {"result": {"videos": list}}}}},
                validate.get("videohub-by-guid-v1"),
                validate.transform(lambda obj: obj[next(iter((obj.keys())))]),
                validate.get(("data", "result", "videos", 0)),
                schema_video,
            )
            return schema.validate(root)
        except PluginError:
            pass

    def _get_streams(self):
        hls_url = self._get_data()
        if hls_url:
            return HLSStream.parse_variant_playlist(self.session, hls_url)


__plugin__ = Reuters

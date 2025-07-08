"""
$description Indian live TV channels and video on-demand service. OTT service from YuppTV.
$url yupptv.com
$type live, vod
$account Some streams require an account and subscription
"""

import logging
import re
import time

from streamlink.plugin import Plugin, pluginargument, pluginmatcher
from streamlink.plugin.api import useragents
from streamlink.stream.hls import HLSStream, HLSStreamReader, HLSStreamWriter


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


class HLSStreamWriterYupptv(HLSStreamWriter):
    def xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_orig(self, segment):
        return ".ts" not in segment.uri or super().should_filter_segment(segment)
    def xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_1(self, segment):
        return "XX.tsXX" not in segment.uri or super().should_filter_segment(segment)
    def xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_2(self, segment):
        return ".TS" not in segment.uri or super().should_filter_segment(segment)
    def xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_3(self, segment):
        return ".ts" in segment.uri or super().should_filter_segment(segment)
    def xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_4(self, segment):
        return ".ts" not in segment.uri and super().should_filter_segment(segment)
    def xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_5(self, segment):
        return ".ts" not in segment.uri or super().should_filter_segment(None)
    
    xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_1': xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_1, 
        'xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_2': xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_2, 
        'xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_3': xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_3, 
        'xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_4': xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_4, 
        'xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_5': xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_5
    }
    
    def should_filter_segment(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_orig"), object.__getattribute__(self, "xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_mutants"), args, kwargs, self)
        return result 
    
    should_filter_segment.__signature__ = _mutmut_signature(xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_orig)
    xǁHLSStreamWriterYupptvǁshould_filter_segment__mutmut_orig.__name__ = 'xǁHLSStreamWriterYupptvǁshould_filter_segment'


class HLSStreamReaderYupptv(HLSStreamReader):
    __writer__ = HLSStreamWriterYupptv


class HLSStreamYupptv(HLSStream):
    __reader__ = HLSStreamReaderYupptv


@pluginmatcher(
    re.compile(r"https?://(?:www\.)?yupptv\.com"),
)
@pluginargument(
    "boxid",
    requires=["yuppflixtoken"],
    sensitive=True,
    metavar="BOXID",
    help="The yupptv.com boxid that's used in the BoxId cookie.",
)
@pluginargument(
    "yuppflixtoken",
    sensitive=True,
    metavar="YUPPFLIXTOKEN",
    help="The yupptv.com yuppflixtoken that's used in the YuppflixToken cookie.",
)
@pluginargument(
    "purge-credentials",
    action="store_true",
    help="Purge cached YuppTV credentials to initiate a new session and reauthenticate.",
)
class YuppTV(Plugin):
    _cookie_expiry = 3600 * 24 * 365

    def _login_using_box_id_and_yuppflix_token(self, box_id, yuppflix_token):
        time_now = time.time()

        self.session.http.cookies.set(
            "BoxId",
            box_id,
            domain="www.yupptv.com",
            path="/",
            expires=time_now + self._cookie_expiry,
        )
        self.session.http.cookies.set(
            "YuppflixToken",
            yuppflix_token,
            domain="www.yupptv.com",
            path="/",
            expires=time_now + self._cookie_expiry,
        )

        self.save_cookies()
        log.info("Successfully set BoxId and YuppflixToken")

    def _get_streams(self):
        self.session.http.headers.update({"User-Agent": useragents.CHROME})
        self.session.http.headers.update({"Origin": "https://www.yupptv.com"})

        authed = (
            self.session.http.cookies.get("BoxId")
            and self.session.http.cookies.get("YuppflixToken")
        )  # fmt: skip

        login_box_id = self.get_option("boxid")
        login_yuppflix_token = self.get_option("yuppflixtoken")

        if self.options.get("purge_credentials"):
            self.clear_cookies()
            authed = False
            log.info("All credentials were successfully removed")

        if authed:
            log.debug("Attempting to authenticate using cached cookies")
        elif login_box_id and login_yuppflix_token:
            self._login_using_box_id_and_yuppflix_token(
                login_box_id,
                login_yuppflix_token,
            )
            authed = True

        page = self.session.http.get(self.url)
        if authed and "btnsignup" in page.text:
            log.error("This device requires renewed credentials to log in")
            return

        match = re.search(r"""src:\s*(?P<q>["'])(?P<url>.+?)(?P=q)""", page.text)
        if not match or "preview/" in match["url"]:
            if "btnsignup" in page.text:
                log.error("This stream requires you to login")
            else:
                log.error("This stream requires a subscription")
            return

        def override_encoding(res, *_, **__):
            res.encoding = "utf-8"

        return HLSStreamYupptv.parse_variant_playlist(
            self.session,
            match["url"],
            hooks={"response": override_encoding},
        )


__plugin__ = YuppTV

"""
$description South Korean live-streaming platform for gaming, entertainment, and other creative content. Owned by Naver.
$url chzzk.naver.com
$type live, vod
$metadata id
$metadata author
$metadata category
$metadata title
"""

import logging
import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.dash import DASHStream
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


class ChzzkAPI:
    _CHANNELS_LIVE_DETAIL_URL = "https://api.chzzk.naver.com/service/v2/channels/{channel_id}/live-detail"
    _VIDEOS_URL = "https://api.chzzk.naver.com/service/v2/videos/{video_id}"
    _CLIP_URL = "https://api.chzzk.naver.com/service/v1/play-info/clip/{clip_id}"

    def xǁChzzkAPIǁ__init____mutmut_orig(self, session):
        self._session = session

    def xǁChzzkAPIǁ__init____mutmut_1(self, session):
        self._session = None
    
    xǁChzzkAPIǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁChzzkAPIǁ__init____mutmut_1': xǁChzzkAPIǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁChzzkAPIǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁChzzkAPIǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁChzzkAPIǁ__init____mutmut_orig)
    xǁChzzkAPIǁ__init____mutmut_orig.__name__ = 'xǁChzzkAPIǁ__init__'

    def xǁChzzkAPIǁ_query_api__mutmut_orig(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_1(self, url, *schemas):
        return self._session.http.get(
            None,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_2(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=None,
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_3(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=None,
        )

    def xǁChzzkAPIǁ_query_api__mutmut_4(self, url, *schemas):
        return self._session.http.get(
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_5(self, url, *schemas):
        return self._session.http.get(
            url,
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_6(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            )

    def xǁChzzkAPIǁ_query_api__mutmut_7(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(201, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_8(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 401, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_9(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 405),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_10(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                None,
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_11(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                None,
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_12(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_13(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_14(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    None,
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_15(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    None,
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_16(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    None,
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_17(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_18(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_19(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_20(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        None,
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_21(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        None,
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_22(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_23(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_24(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "XXcodeXX": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_25(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "CODE": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_26(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "Code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_27(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "XXmessageXX": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_28(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "MESSAGE": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_29(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "Message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_30(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(None),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_31(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: None),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_32(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("XXerrorXX", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_33(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("ERROR", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_34(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("Error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_35(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["XXmessageXX"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_36(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["MESSAGE"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_37(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["Message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_38(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        None,
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_39(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        None,
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_40(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_41(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_42(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "XXcodeXX": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_43(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "CODE": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_44(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "Code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_45(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 201,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_46(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "XXcontentXX": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_47(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "CONTENT": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_48(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "Content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_49(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(None),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_50(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: None),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_51(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("XXsuccessXX", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_52(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("SUCCESS", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_53(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("Success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_54(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        None,
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_55(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        None,
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_56(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        None,
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_57(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_58(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_59(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_60(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_61(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "XXcodeXX": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_62(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "CODE": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_63(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "Code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_64(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 201,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_65(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "XXcontentXX": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_66(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "CONTENT": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_67(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "Content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_68(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get(None),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_69(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("XXcontentXX"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_70(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("CONTENT"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_71(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("Content"),
                        *schemas,
                        validate.transform(lambda data: ("success", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_72(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(None),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_73(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: None),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_74(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("XXsuccessXX", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_75(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("SUCCESS", data)),
                    ),
                ),
            ),
        )

    def xǁChzzkAPIǁ_query_api__mutmut_76(self, url, *schemas):
        return self._session.http.get(
            url,
            acceptable_status=(200, 400, 404),
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        {
                            "code": int,
                            "message": str,
                        },
                        validate.transform(lambda data: ("error", data["message"])),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": None,
                        },
                        validate.transform(lambda _: ("success", None)),
                    ),
                    validate.all(
                        {
                            "code": 200,
                            "content": dict,
                        },
                        validate.get("content"),
                        *schemas,
                        validate.transform(lambda data: ("Success", data)),
                    ),
                ),
            ),
        )
    
    xǁChzzkAPIǁ_query_api__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁChzzkAPIǁ_query_api__mutmut_1': xǁChzzkAPIǁ_query_api__mutmut_1, 
        'xǁChzzkAPIǁ_query_api__mutmut_2': xǁChzzkAPIǁ_query_api__mutmut_2, 
        'xǁChzzkAPIǁ_query_api__mutmut_3': xǁChzzkAPIǁ_query_api__mutmut_3, 
        'xǁChzzkAPIǁ_query_api__mutmut_4': xǁChzzkAPIǁ_query_api__mutmut_4, 
        'xǁChzzkAPIǁ_query_api__mutmut_5': xǁChzzkAPIǁ_query_api__mutmut_5, 
        'xǁChzzkAPIǁ_query_api__mutmut_6': xǁChzzkAPIǁ_query_api__mutmut_6, 
        'xǁChzzkAPIǁ_query_api__mutmut_7': xǁChzzkAPIǁ_query_api__mutmut_7, 
        'xǁChzzkAPIǁ_query_api__mutmut_8': xǁChzzkAPIǁ_query_api__mutmut_8, 
        'xǁChzzkAPIǁ_query_api__mutmut_9': xǁChzzkAPIǁ_query_api__mutmut_9, 
        'xǁChzzkAPIǁ_query_api__mutmut_10': xǁChzzkAPIǁ_query_api__mutmut_10, 
        'xǁChzzkAPIǁ_query_api__mutmut_11': xǁChzzkAPIǁ_query_api__mutmut_11, 
        'xǁChzzkAPIǁ_query_api__mutmut_12': xǁChzzkAPIǁ_query_api__mutmut_12, 
        'xǁChzzkAPIǁ_query_api__mutmut_13': xǁChzzkAPIǁ_query_api__mutmut_13, 
        'xǁChzzkAPIǁ_query_api__mutmut_14': xǁChzzkAPIǁ_query_api__mutmut_14, 
        'xǁChzzkAPIǁ_query_api__mutmut_15': xǁChzzkAPIǁ_query_api__mutmut_15, 
        'xǁChzzkAPIǁ_query_api__mutmut_16': xǁChzzkAPIǁ_query_api__mutmut_16, 
        'xǁChzzkAPIǁ_query_api__mutmut_17': xǁChzzkAPIǁ_query_api__mutmut_17, 
        'xǁChzzkAPIǁ_query_api__mutmut_18': xǁChzzkAPIǁ_query_api__mutmut_18, 
        'xǁChzzkAPIǁ_query_api__mutmut_19': xǁChzzkAPIǁ_query_api__mutmut_19, 
        'xǁChzzkAPIǁ_query_api__mutmut_20': xǁChzzkAPIǁ_query_api__mutmut_20, 
        'xǁChzzkAPIǁ_query_api__mutmut_21': xǁChzzkAPIǁ_query_api__mutmut_21, 
        'xǁChzzkAPIǁ_query_api__mutmut_22': xǁChzzkAPIǁ_query_api__mutmut_22, 
        'xǁChzzkAPIǁ_query_api__mutmut_23': xǁChzzkAPIǁ_query_api__mutmut_23, 
        'xǁChzzkAPIǁ_query_api__mutmut_24': xǁChzzkAPIǁ_query_api__mutmut_24, 
        'xǁChzzkAPIǁ_query_api__mutmut_25': xǁChzzkAPIǁ_query_api__mutmut_25, 
        'xǁChzzkAPIǁ_query_api__mutmut_26': xǁChzzkAPIǁ_query_api__mutmut_26, 
        'xǁChzzkAPIǁ_query_api__mutmut_27': xǁChzzkAPIǁ_query_api__mutmut_27, 
        'xǁChzzkAPIǁ_query_api__mutmut_28': xǁChzzkAPIǁ_query_api__mutmut_28, 
        'xǁChzzkAPIǁ_query_api__mutmut_29': xǁChzzkAPIǁ_query_api__mutmut_29, 
        'xǁChzzkAPIǁ_query_api__mutmut_30': xǁChzzkAPIǁ_query_api__mutmut_30, 
        'xǁChzzkAPIǁ_query_api__mutmut_31': xǁChzzkAPIǁ_query_api__mutmut_31, 
        'xǁChzzkAPIǁ_query_api__mutmut_32': xǁChzzkAPIǁ_query_api__mutmut_32, 
        'xǁChzzkAPIǁ_query_api__mutmut_33': xǁChzzkAPIǁ_query_api__mutmut_33, 
        'xǁChzzkAPIǁ_query_api__mutmut_34': xǁChzzkAPIǁ_query_api__mutmut_34, 
        'xǁChzzkAPIǁ_query_api__mutmut_35': xǁChzzkAPIǁ_query_api__mutmut_35, 
        'xǁChzzkAPIǁ_query_api__mutmut_36': xǁChzzkAPIǁ_query_api__mutmut_36, 
        'xǁChzzkAPIǁ_query_api__mutmut_37': xǁChzzkAPIǁ_query_api__mutmut_37, 
        'xǁChzzkAPIǁ_query_api__mutmut_38': xǁChzzkAPIǁ_query_api__mutmut_38, 
        'xǁChzzkAPIǁ_query_api__mutmut_39': xǁChzzkAPIǁ_query_api__mutmut_39, 
        'xǁChzzkAPIǁ_query_api__mutmut_40': xǁChzzkAPIǁ_query_api__mutmut_40, 
        'xǁChzzkAPIǁ_query_api__mutmut_41': xǁChzzkAPIǁ_query_api__mutmut_41, 
        'xǁChzzkAPIǁ_query_api__mutmut_42': xǁChzzkAPIǁ_query_api__mutmut_42, 
        'xǁChzzkAPIǁ_query_api__mutmut_43': xǁChzzkAPIǁ_query_api__mutmut_43, 
        'xǁChzzkAPIǁ_query_api__mutmut_44': xǁChzzkAPIǁ_query_api__mutmut_44, 
        'xǁChzzkAPIǁ_query_api__mutmut_45': xǁChzzkAPIǁ_query_api__mutmut_45, 
        'xǁChzzkAPIǁ_query_api__mutmut_46': xǁChzzkAPIǁ_query_api__mutmut_46, 
        'xǁChzzkAPIǁ_query_api__mutmut_47': xǁChzzkAPIǁ_query_api__mutmut_47, 
        'xǁChzzkAPIǁ_query_api__mutmut_48': xǁChzzkAPIǁ_query_api__mutmut_48, 
        'xǁChzzkAPIǁ_query_api__mutmut_49': xǁChzzkAPIǁ_query_api__mutmut_49, 
        'xǁChzzkAPIǁ_query_api__mutmut_50': xǁChzzkAPIǁ_query_api__mutmut_50, 
        'xǁChzzkAPIǁ_query_api__mutmut_51': xǁChzzkAPIǁ_query_api__mutmut_51, 
        'xǁChzzkAPIǁ_query_api__mutmut_52': xǁChzzkAPIǁ_query_api__mutmut_52, 
        'xǁChzzkAPIǁ_query_api__mutmut_53': xǁChzzkAPIǁ_query_api__mutmut_53, 
        'xǁChzzkAPIǁ_query_api__mutmut_54': xǁChzzkAPIǁ_query_api__mutmut_54, 
        'xǁChzzkAPIǁ_query_api__mutmut_55': xǁChzzkAPIǁ_query_api__mutmut_55, 
        'xǁChzzkAPIǁ_query_api__mutmut_56': xǁChzzkAPIǁ_query_api__mutmut_56, 
        'xǁChzzkAPIǁ_query_api__mutmut_57': xǁChzzkAPIǁ_query_api__mutmut_57, 
        'xǁChzzkAPIǁ_query_api__mutmut_58': xǁChzzkAPIǁ_query_api__mutmut_58, 
        'xǁChzzkAPIǁ_query_api__mutmut_59': xǁChzzkAPIǁ_query_api__mutmut_59, 
        'xǁChzzkAPIǁ_query_api__mutmut_60': xǁChzzkAPIǁ_query_api__mutmut_60, 
        'xǁChzzkAPIǁ_query_api__mutmut_61': xǁChzzkAPIǁ_query_api__mutmut_61, 
        'xǁChzzkAPIǁ_query_api__mutmut_62': xǁChzzkAPIǁ_query_api__mutmut_62, 
        'xǁChzzkAPIǁ_query_api__mutmut_63': xǁChzzkAPIǁ_query_api__mutmut_63, 
        'xǁChzzkAPIǁ_query_api__mutmut_64': xǁChzzkAPIǁ_query_api__mutmut_64, 
        'xǁChzzkAPIǁ_query_api__mutmut_65': xǁChzzkAPIǁ_query_api__mutmut_65, 
        'xǁChzzkAPIǁ_query_api__mutmut_66': xǁChzzkAPIǁ_query_api__mutmut_66, 
        'xǁChzzkAPIǁ_query_api__mutmut_67': xǁChzzkAPIǁ_query_api__mutmut_67, 
        'xǁChzzkAPIǁ_query_api__mutmut_68': xǁChzzkAPIǁ_query_api__mutmut_68, 
        'xǁChzzkAPIǁ_query_api__mutmut_69': xǁChzzkAPIǁ_query_api__mutmut_69, 
        'xǁChzzkAPIǁ_query_api__mutmut_70': xǁChzzkAPIǁ_query_api__mutmut_70, 
        'xǁChzzkAPIǁ_query_api__mutmut_71': xǁChzzkAPIǁ_query_api__mutmut_71, 
        'xǁChzzkAPIǁ_query_api__mutmut_72': xǁChzzkAPIǁ_query_api__mutmut_72, 
        'xǁChzzkAPIǁ_query_api__mutmut_73': xǁChzzkAPIǁ_query_api__mutmut_73, 
        'xǁChzzkAPIǁ_query_api__mutmut_74': xǁChzzkAPIǁ_query_api__mutmut_74, 
        'xǁChzzkAPIǁ_query_api__mutmut_75': xǁChzzkAPIǁ_query_api__mutmut_75, 
        'xǁChzzkAPIǁ_query_api__mutmut_76': xǁChzzkAPIǁ_query_api__mutmut_76
    }
    
    def _query_api(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁChzzkAPIǁ_query_api__mutmut_orig"), object.__getattribute__(self, "xǁChzzkAPIǁ_query_api__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _query_api.__signature__ = _mutmut_signature(xǁChzzkAPIǁ_query_api__mutmut_orig)
    xǁChzzkAPIǁ_query_api__mutmut_orig.__name__ = 'xǁChzzkAPIǁ_query_api'

    def xǁChzzkAPIǁget_live_detail__mutmut_orig(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_1(self, channel_id):
        return self._query_api(
            None,
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_2(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            None,
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_3(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            None,
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_4(self, channel_id):
        return self._query_api(
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_5(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_6(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            )

    def xǁChzzkAPIǁget_live_detail__mutmut_7(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=None),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_8(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "XXstatusXX": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_9(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "STATUS": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_10(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "Status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_11(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "XXliveIdXX": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_12(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveid": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_13(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "LIVEID": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_14(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "Liveid": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_15(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "XXliveTitleXX": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_16(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "livetitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_17(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "LIVETITLE": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_18(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "Livetitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_19(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(None, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_20(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_21(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, ),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_22(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "XXliveCategoryXX": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_23(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "livecategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_24(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "LIVECATEGORY": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_25(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "Livecategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_26(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(None, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_27(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_28(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, ),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_29(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "XXadultXX": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_30(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "ADULT": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_31(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "Adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_32(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "XXchannelXX": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_33(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "CHANNEL": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_34(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "Channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_35(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    None,
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_36(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    None,
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_37(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_38(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_39(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"XXchannelNameXX": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_40(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelname": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_41(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"CHANNELNAME": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_42(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"Channelname": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_43(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get(None),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_44(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("XXchannelNameXX"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_45(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelname"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_46(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("CHANNELNAME"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_47(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("Channelname"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_48(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "XXlivePlaybackJsonXX": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_49(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "liveplaybackjson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_50(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "LIVEPLAYBACKJSON": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_51(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "Liveplaybackjson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_52(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    None,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_53(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    None,
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_54(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    None,
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_55(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    None,
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_56(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_57(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_58(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_59(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_60(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "XXmediaXX": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_61(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "MEDIA": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_62(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "Media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_63(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                None,
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_64(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                None,
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_65(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_66(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_67(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "XXmediaIdXX": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_68(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaid": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_69(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "MEDIAID": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_70(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "Mediaid": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_71(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "XXprotocolXX": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_72(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "PROTOCOL": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_73(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "Protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_74(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "XXpathXX": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_75(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "PATH": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_76(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "Path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_77(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    None,
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_78(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    None,
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_79(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    None,
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_80(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_81(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_82(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_83(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "XXmediaIdXX",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_84(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaid",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_85(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "MEDIAID",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_86(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "Mediaid",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_87(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "XXprotocolXX",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_88(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "PROTOCOL",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_89(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "Protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_90(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "XXpathXX",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_91(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "PATH",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_92(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "Path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_93(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get(None),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_94(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("XXmediaXX"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_95(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("MEDIA"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_96(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("Media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_97(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                None,
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_98(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                None,
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_99(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                None,
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_100(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                None,
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_101(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                None,
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_102(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                None,
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_103(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                None,
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_104(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_105(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_106(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_107(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_108(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_109(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_110(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_111(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "XXlivePlaybackJsonXX",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_112(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "liveplaybackjson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_113(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "LIVEPLAYBACKJSON",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_114(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "Liveplaybackjson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_115(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "XXstatusXX",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_116(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "STATUS",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_117(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "Status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_118(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "XXliveIdXX",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_119(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveid",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_120(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "LIVEID",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_121(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "Liveid",
                "channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_122(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "XXchannelXX",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_123(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "CHANNEL",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_124(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "Channel",
                "liveCategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_125(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "XXliveCategoryXX",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_126(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "livecategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_127(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "LIVECATEGORY",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_128(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "Livecategory",
                "liveTitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_129(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "XXliveTitleXX",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_130(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "livetitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_131(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "LIVETITLE",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_132(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "Livetitle",
                "adult",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_133(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "XXadultXX",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_134(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "ADULT",
            ),
        )

    def xǁChzzkAPIǁget_live_detail__mutmut_135(self, channel_id):
        return self._query_api(
            self._CHANNELS_LIVE_DETAIL_URL.format(channel_id=channel_id),
            {
                "status": str,
                "liveId": int,
                "liveTitle": validate.any(str, None),
                "liveCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
                "livePlaybackJson": validate.none_or_all(
                    str,
                    validate.parse_json(),
                    {
                        "media": [
                            validate.all(
                                {
                                    "mediaId": str,
                                    "protocol": str,
                                    "path": validate.url(),
                                },
                                validate.union_get(
                                    "mediaId",
                                    "protocol",
                                    "path",
                                ),
                            ),
                        ],
                    },
                    validate.get("media"),
                ),
            },
            validate.union_get(
                "livePlaybackJson",
                "status",
                "liveId",
                "channel",
                "liveCategory",
                "liveTitle",
                "Adult",
            ),
        )
    
    xǁChzzkAPIǁget_live_detail__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁChzzkAPIǁget_live_detail__mutmut_1': xǁChzzkAPIǁget_live_detail__mutmut_1, 
        'xǁChzzkAPIǁget_live_detail__mutmut_2': xǁChzzkAPIǁget_live_detail__mutmut_2, 
        'xǁChzzkAPIǁget_live_detail__mutmut_3': xǁChzzkAPIǁget_live_detail__mutmut_3, 
        'xǁChzzkAPIǁget_live_detail__mutmut_4': xǁChzzkAPIǁget_live_detail__mutmut_4, 
        'xǁChzzkAPIǁget_live_detail__mutmut_5': xǁChzzkAPIǁget_live_detail__mutmut_5, 
        'xǁChzzkAPIǁget_live_detail__mutmut_6': xǁChzzkAPIǁget_live_detail__mutmut_6, 
        'xǁChzzkAPIǁget_live_detail__mutmut_7': xǁChzzkAPIǁget_live_detail__mutmut_7, 
        'xǁChzzkAPIǁget_live_detail__mutmut_8': xǁChzzkAPIǁget_live_detail__mutmut_8, 
        'xǁChzzkAPIǁget_live_detail__mutmut_9': xǁChzzkAPIǁget_live_detail__mutmut_9, 
        'xǁChzzkAPIǁget_live_detail__mutmut_10': xǁChzzkAPIǁget_live_detail__mutmut_10, 
        'xǁChzzkAPIǁget_live_detail__mutmut_11': xǁChzzkAPIǁget_live_detail__mutmut_11, 
        'xǁChzzkAPIǁget_live_detail__mutmut_12': xǁChzzkAPIǁget_live_detail__mutmut_12, 
        'xǁChzzkAPIǁget_live_detail__mutmut_13': xǁChzzkAPIǁget_live_detail__mutmut_13, 
        'xǁChzzkAPIǁget_live_detail__mutmut_14': xǁChzzkAPIǁget_live_detail__mutmut_14, 
        'xǁChzzkAPIǁget_live_detail__mutmut_15': xǁChzzkAPIǁget_live_detail__mutmut_15, 
        'xǁChzzkAPIǁget_live_detail__mutmut_16': xǁChzzkAPIǁget_live_detail__mutmut_16, 
        'xǁChzzkAPIǁget_live_detail__mutmut_17': xǁChzzkAPIǁget_live_detail__mutmut_17, 
        'xǁChzzkAPIǁget_live_detail__mutmut_18': xǁChzzkAPIǁget_live_detail__mutmut_18, 
        'xǁChzzkAPIǁget_live_detail__mutmut_19': xǁChzzkAPIǁget_live_detail__mutmut_19, 
        'xǁChzzkAPIǁget_live_detail__mutmut_20': xǁChzzkAPIǁget_live_detail__mutmut_20, 
        'xǁChzzkAPIǁget_live_detail__mutmut_21': xǁChzzkAPIǁget_live_detail__mutmut_21, 
        'xǁChzzkAPIǁget_live_detail__mutmut_22': xǁChzzkAPIǁget_live_detail__mutmut_22, 
        'xǁChzzkAPIǁget_live_detail__mutmut_23': xǁChzzkAPIǁget_live_detail__mutmut_23, 
        'xǁChzzkAPIǁget_live_detail__mutmut_24': xǁChzzkAPIǁget_live_detail__mutmut_24, 
        'xǁChzzkAPIǁget_live_detail__mutmut_25': xǁChzzkAPIǁget_live_detail__mutmut_25, 
        'xǁChzzkAPIǁget_live_detail__mutmut_26': xǁChzzkAPIǁget_live_detail__mutmut_26, 
        'xǁChzzkAPIǁget_live_detail__mutmut_27': xǁChzzkAPIǁget_live_detail__mutmut_27, 
        'xǁChzzkAPIǁget_live_detail__mutmut_28': xǁChzzkAPIǁget_live_detail__mutmut_28, 
        'xǁChzzkAPIǁget_live_detail__mutmut_29': xǁChzzkAPIǁget_live_detail__mutmut_29, 
        'xǁChzzkAPIǁget_live_detail__mutmut_30': xǁChzzkAPIǁget_live_detail__mutmut_30, 
        'xǁChzzkAPIǁget_live_detail__mutmut_31': xǁChzzkAPIǁget_live_detail__mutmut_31, 
        'xǁChzzkAPIǁget_live_detail__mutmut_32': xǁChzzkAPIǁget_live_detail__mutmut_32, 
        'xǁChzzkAPIǁget_live_detail__mutmut_33': xǁChzzkAPIǁget_live_detail__mutmut_33, 
        'xǁChzzkAPIǁget_live_detail__mutmut_34': xǁChzzkAPIǁget_live_detail__mutmut_34, 
        'xǁChzzkAPIǁget_live_detail__mutmut_35': xǁChzzkAPIǁget_live_detail__mutmut_35, 
        'xǁChzzkAPIǁget_live_detail__mutmut_36': xǁChzzkAPIǁget_live_detail__mutmut_36, 
        'xǁChzzkAPIǁget_live_detail__mutmut_37': xǁChzzkAPIǁget_live_detail__mutmut_37, 
        'xǁChzzkAPIǁget_live_detail__mutmut_38': xǁChzzkAPIǁget_live_detail__mutmut_38, 
        'xǁChzzkAPIǁget_live_detail__mutmut_39': xǁChzzkAPIǁget_live_detail__mutmut_39, 
        'xǁChzzkAPIǁget_live_detail__mutmut_40': xǁChzzkAPIǁget_live_detail__mutmut_40, 
        'xǁChzzkAPIǁget_live_detail__mutmut_41': xǁChzzkAPIǁget_live_detail__mutmut_41, 
        'xǁChzzkAPIǁget_live_detail__mutmut_42': xǁChzzkAPIǁget_live_detail__mutmut_42, 
        'xǁChzzkAPIǁget_live_detail__mutmut_43': xǁChzzkAPIǁget_live_detail__mutmut_43, 
        'xǁChzzkAPIǁget_live_detail__mutmut_44': xǁChzzkAPIǁget_live_detail__mutmut_44, 
        'xǁChzzkAPIǁget_live_detail__mutmut_45': xǁChzzkAPIǁget_live_detail__mutmut_45, 
        'xǁChzzkAPIǁget_live_detail__mutmut_46': xǁChzzkAPIǁget_live_detail__mutmut_46, 
        'xǁChzzkAPIǁget_live_detail__mutmut_47': xǁChzzkAPIǁget_live_detail__mutmut_47, 
        'xǁChzzkAPIǁget_live_detail__mutmut_48': xǁChzzkAPIǁget_live_detail__mutmut_48, 
        'xǁChzzkAPIǁget_live_detail__mutmut_49': xǁChzzkAPIǁget_live_detail__mutmut_49, 
        'xǁChzzkAPIǁget_live_detail__mutmut_50': xǁChzzkAPIǁget_live_detail__mutmut_50, 
        'xǁChzzkAPIǁget_live_detail__mutmut_51': xǁChzzkAPIǁget_live_detail__mutmut_51, 
        'xǁChzzkAPIǁget_live_detail__mutmut_52': xǁChzzkAPIǁget_live_detail__mutmut_52, 
        'xǁChzzkAPIǁget_live_detail__mutmut_53': xǁChzzkAPIǁget_live_detail__mutmut_53, 
        'xǁChzzkAPIǁget_live_detail__mutmut_54': xǁChzzkAPIǁget_live_detail__mutmut_54, 
        'xǁChzzkAPIǁget_live_detail__mutmut_55': xǁChzzkAPIǁget_live_detail__mutmut_55, 
        'xǁChzzkAPIǁget_live_detail__mutmut_56': xǁChzzkAPIǁget_live_detail__mutmut_56, 
        'xǁChzzkAPIǁget_live_detail__mutmut_57': xǁChzzkAPIǁget_live_detail__mutmut_57, 
        'xǁChzzkAPIǁget_live_detail__mutmut_58': xǁChzzkAPIǁget_live_detail__mutmut_58, 
        'xǁChzzkAPIǁget_live_detail__mutmut_59': xǁChzzkAPIǁget_live_detail__mutmut_59, 
        'xǁChzzkAPIǁget_live_detail__mutmut_60': xǁChzzkAPIǁget_live_detail__mutmut_60, 
        'xǁChzzkAPIǁget_live_detail__mutmut_61': xǁChzzkAPIǁget_live_detail__mutmut_61, 
        'xǁChzzkAPIǁget_live_detail__mutmut_62': xǁChzzkAPIǁget_live_detail__mutmut_62, 
        'xǁChzzkAPIǁget_live_detail__mutmut_63': xǁChzzkAPIǁget_live_detail__mutmut_63, 
        'xǁChzzkAPIǁget_live_detail__mutmut_64': xǁChzzkAPIǁget_live_detail__mutmut_64, 
        'xǁChzzkAPIǁget_live_detail__mutmut_65': xǁChzzkAPIǁget_live_detail__mutmut_65, 
        'xǁChzzkAPIǁget_live_detail__mutmut_66': xǁChzzkAPIǁget_live_detail__mutmut_66, 
        'xǁChzzkAPIǁget_live_detail__mutmut_67': xǁChzzkAPIǁget_live_detail__mutmut_67, 
        'xǁChzzkAPIǁget_live_detail__mutmut_68': xǁChzzkAPIǁget_live_detail__mutmut_68, 
        'xǁChzzkAPIǁget_live_detail__mutmut_69': xǁChzzkAPIǁget_live_detail__mutmut_69, 
        'xǁChzzkAPIǁget_live_detail__mutmut_70': xǁChzzkAPIǁget_live_detail__mutmut_70, 
        'xǁChzzkAPIǁget_live_detail__mutmut_71': xǁChzzkAPIǁget_live_detail__mutmut_71, 
        'xǁChzzkAPIǁget_live_detail__mutmut_72': xǁChzzkAPIǁget_live_detail__mutmut_72, 
        'xǁChzzkAPIǁget_live_detail__mutmut_73': xǁChzzkAPIǁget_live_detail__mutmut_73, 
        'xǁChzzkAPIǁget_live_detail__mutmut_74': xǁChzzkAPIǁget_live_detail__mutmut_74, 
        'xǁChzzkAPIǁget_live_detail__mutmut_75': xǁChzzkAPIǁget_live_detail__mutmut_75, 
        'xǁChzzkAPIǁget_live_detail__mutmut_76': xǁChzzkAPIǁget_live_detail__mutmut_76, 
        'xǁChzzkAPIǁget_live_detail__mutmut_77': xǁChzzkAPIǁget_live_detail__mutmut_77, 
        'xǁChzzkAPIǁget_live_detail__mutmut_78': xǁChzzkAPIǁget_live_detail__mutmut_78, 
        'xǁChzzkAPIǁget_live_detail__mutmut_79': xǁChzzkAPIǁget_live_detail__mutmut_79, 
        'xǁChzzkAPIǁget_live_detail__mutmut_80': xǁChzzkAPIǁget_live_detail__mutmut_80, 
        'xǁChzzkAPIǁget_live_detail__mutmut_81': xǁChzzkAPIǁget_live_detail__mutmut_81, 
        'xǁChzzkAPIǁget_live_detail__mutmut_82': xǁChzzkAPIǁget_live_detail__mutmut_82, 
        'xǁChzzkAPIǁget_live_detail__mutmut_83': xǁChzzkAPIǁget_live_detail__mutmut_83, 
        'xǁChzzkAPIǁget_live_detail__mutmut_84': xǁChzzkAPIǁget_live_detail__mutmut_84, 
        'xǁChzzkAPIǁget_live_detail__mutmut_85': xǁChzzkAPIǁget_live_detail__mutmut_85, 
        'xǁChzzkAPIǁget_live_detail__mutmut_86': xǁChzzkAPIǁget_live_detail__mutmut_86, 
        'xǁChzzkAPIǁget_live_detail__mutmut_87': xǁChzzkAPIǁget_live_detail__mutmut_87, 
        'xǁChzzkAPIǁget_live_detail__mutmut_88': xǁChzzkAPIǁget_live_detail__mutmut_88, 
        'xǁChzzkAPIǁget_live_detail__mutmut_89': xǁChzzkAPIǁget_live_detail__mutmut_89, 
        'xǁChzzkAPIǁget_live_detail__mutmut_90': xǁChzzkAPIǁget_live_detail__mutmut_90, 
        'xǁChzzkAPIǁget_live_detail__mutmut_91': xǁChzzkAPIǁget_live_detail__mutmut_91, 
        'xǁChzzkAPIǁget_live_detail__mutmut_92': xǁChzzkAPIǁget_live_detail__mutmut_92, 
        'xǁChzzkAPIǁget_live_detail__mutmut_93': xǁChzzkAPIǁget_live_detail__mutmut_93, 
        'xǁChzzkAPIǁget_live_detail__mutmut_94': xǁChzzkAPIǁget_live_detail__mutmut_94, 
        'xǁChzzkAPIǁget_live_detail__mutmut_95': xǁChzzkAPIǁget_live_detail__mutmut_95, 
        'xǁChzzkAPIǁget_live_detail__mutmut_96': xǁChzzkAPIǁget_live_detail__mutmut_96, 
        'xǁChzzkAPIǁget_live_detail__mutmut_97': xǁChzzkAPIǁget_live_detail__mutmut_97, 
        'xǁChzzkAPIǁget_live_detail__mutmut_98': xǁChzzkAPIǁget_live_detail__mutmut_98, 
        'xǁChzzkAPIǁget_live_detail__mutmut_99': xǁChzzkAPIǁget_live_detail__mutmut_99, 
        'xǁChzzkAPIǁget_live_detail__mutmut_100': xǁChzzkAPIǁget_live_detail__mutmut_100, 
        'xǁChzzkAPIǁget_live_detail__mutmut_101': xǁChzzkAPIǁget_live_detail__mutmut_101, 
        'xǁChzzkAPIǁget_live_detail__mutmut_102': xǁChzzkAPIǁget_live_detail__mutmut_102, 
        'xǁChzzkAPIǁget_live_detail__mutmut_103': xǁChzzkAPIǁget_live_detail__mutmut_103, 
        'xǁChzzkAPIǁget_live_detail__mutmut_104': xǁChzzkAPIǁget_live_detail__mutmut_104, 
        'xǁChzzkAPIǁget_live_detail__mutmut_105': xǁChzzkAPIǁget_live_detail__mutmut_105, 
        'xǁChzzkAPIǁget_live_detail__mutmut_106': xǁChzzkAPIǁget_live_detail__mutmut_106, 
        'xǁChzzkAPIǁget_live_detail__mutmut_107': xǁChzzkAPIǁget_live_detail__mutmut_107, 
        'xǁChzzkAPIǁget_live_detail__mutmut_108': xǁChzzkAPIǁget_live_detail__mutmut_108, 
        'xǁChzzkAPIǁget_live_detail__mutmut_109': xǁChzzkAPIǁget_live_detail__mutmut_109, 
        'xǁChzzkAPIǁget_live_detail__mutmut_110': xǁChzzkAPIǁget_live_detail__mutmut_110, 
        'xǁChzzkAPIǁget_live_detail__mutmut_111': xǁChzzkAPIǁget_live_detail__mutmut_111, 
        'xǁChzzkAPIǁget_live_detail__mutmut_112': xǁChzzkAPIǁget_live_detail__mutmut_112, 
        'xǁChzzkAPIǁget_live_detail__mutmut_113': xǁChzzkAPIǁget_live_detail__mutmut_113, 
        'xǁChzzkAPIǁget_live_detail__mutmut_114': xǁChzzkAPIǁget_live_detail__mutmut_114, 
        'xǁChzzkAPIǁget_live_detail__mutmut_115': xǁChzzkAPIǁget_live_detail__mutmut_115, 
        'xǁChzzkAPIǁget_live_detail__mutmut_116': xǁChzzkAPIǁget_live_detail__mutmut_116, 
        'xǁChzzkAPIǁget_live_detail__mutmut_117': xǁChzzkAPIǁget_live_detail__mutmut_117, 
        'xǁChzzkAPIǁget_live_detail__mutmut_118': xǁChzzkAPIǁget_live_detail__mutmut_118, 
        'xǁChzzkAPIǁget_live_detail__mutmut_119': xǁChzzkAPIǁget_live_detail__mutmut_119, 
        'xǁChzzkAPIǁget_live_detail__mutmut_120': xǁChzzkAPIǁget_live_detail__mutmut_120, 
        'xǁChzzkAPIǁget_live_detail__mutmut_121': xǁChzzkAPIǁget_live_detail__mutmut_121, 
        'xǁChzzkAPIǁget_live_detail__mutmut_122': xǁChzzkAPIǁget_live_detail__mutmut_122, 
        'xǁChzzkAPIǁget_live_detail__mutmut_123': xǁChzzkAPIǁget_live_detail__mutmut_123, 
        'xǁChzzkAPIǁget_live_detail__mutmut_124': xǁChzzkAPIǁget_live_detail__mutmut_124, 
        'xǁChzzkAPIǁget_live_detail__mutmut_125': xǁChzzkAPIǁget_live_detail__mutmut_125, 
        'xǁChzzkAPIǁget_live_detail__mutmut_126': xǁChzzkAPIǁget_live_detail__mutmut_126, 
        'xǁChzzkAPIǁget_live_detail__mutmut_127': xǁChzzkAPIǁget_live_detail__mutmut_127, 
        'xǁChzzkAPIǁget_live_detail__mutmut_128': xǁChzzkAPIǁget_live_detail__mutmut_128, 
        'xǁChzzkAPIǁget_live_detail__mutmut_129': xǁChzzkAPIǁget_live_detail__mutmut_129, 
        'xǁChzzkAPIǁget_live_detail__mutmut_130': xǁChzzkAPIǁget_live_detail__mutmut_130, 
        'xǁChzzkAPIǁget_live_detail__mutmut_131': xǁChzzkAPIǁget_live_detail__mutmut_131, 
        'xǁChzzkAPIǁget_live_detail__mutmut_132': xǁChzzkAPIǁget_live_detail__mutmut_132, 
        'xǁChzzkAPIǁget_live_detail__mutmut_133': xǁChzzkAPIǁget_live_detail__mutmut_133, 
        'xǁChzzkAPIǁget_live_detail__mutmut_134': xǁChzzkAPIǁget_live_detail__mutmut_134, 
        'xǁChzzkAPIǁget_live_detail__mutmut_135': xǁChzzkAPIǁget_live_detail__mutmut_135
    }
    
    def get_live_detail(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁChzzkAPIǁget_live_detail__mutmut_orig"), object.__getattribute__(self, "xǁChzzkAPIǁget_live_detail__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_live_detail.__signature__ = _mutmut_signature(xǁChzzkAPIǁget_live_detail__mutmut_orig)
    xǁChzzkAPIǁget_live_detail__mutmut_orig.__name__ = 'xǁChzzkAPIǁget_live_detail'

    def xǁChzzkAPIǁget_videos__mutmut_orig(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_1(self, video_id):
        return self._query_api(
            None,
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_2(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            None,
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_3(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            None,
        )

    def xǁChzzkAPIǁget_videos__mutmut_4(self, video_id):
        return self._query_api(
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_5(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_6(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            )

    def xǁChzzkAPIǁget_videos__mutmut_7(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=None),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_8(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "XXinKeyXX": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_9(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inkey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_10(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "INKEY": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_11(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "Inkey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_12(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(None, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_13(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_14(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, ),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_15(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "XXvideoNoXX": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_16(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videono": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_17(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "VIDEONO": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_18(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "Videono": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_19(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(None, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_20(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_21(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, ),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_22(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "XXvideoIdXX": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_23(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoid": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_24(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "VIDEOID": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_25(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "Videoid": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_26(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(None, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_27(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_28(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, ),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_29(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "XXvideoTitleXX": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_30(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videotitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_31(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "VIDEOTITLE": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_32(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "Videotitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_33(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(None, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_34(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_35(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, ),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_36(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "XXvideoCategoryXX": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_37(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videocategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_38(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "VIDEOCATEGORY": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_39(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "Videocategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_40(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(None, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_41(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_42(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, ),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_43(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "XXadultXX": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_44(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "ADULT": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_45(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "Adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_46(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "XXchannelXX": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_47(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "CHANNEL": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_48(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "Channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_49(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    None,
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_50(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    None,
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_51(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_52(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_53(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"XXchannelNameXX": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_54(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelname": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_55(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"CHANNELNAME": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_56(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"Channelname": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_57(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get(None),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_58(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("XXchannelNameXX"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_59(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelname"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_60(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("CHANNELNAME"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_61(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("Channelname"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_62(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                None,
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_63(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                None,
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_64(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                None,
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_65(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                None,
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_66(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                None,
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_67(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                None,
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_68(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                None,
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_69(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_70(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_71(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_72(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_73(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_74(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_75(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_76(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "XXadultXX",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_77(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "ADULT",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_78(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "Adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_79(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "XXinKeyXX",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_80(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inkey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_81(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "INKEY",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_82(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "Inkey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_83(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "XXvideoIdXX",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_84(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoid",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_85(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "VIDEOID",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_86(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "Videoid",
                "videoNo",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_87(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "XXvideoNoXX",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_88(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videono",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_89(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "VIDEONO",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_90(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "Videono",
                "channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_91(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "XXchannelXX",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_92(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "CHANNEL",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_93(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "Channel",
                "videoTitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_94(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "XXvideoTitleXX",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_95(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videotitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_96(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "VIDEOTITLE",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_97(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "Videotitle",
                "videoCategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_98(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "XXvideoCategoryXX",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_99(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "videocategory",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_100(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "VIDEOCATEGORY",
            ),
        )

    def xǁChzzkAPIǁget_videos__mutmut_101(self, video_id):
        return self._query_api(
            self._VIDEOS_URL.format(video_id=video_id),
            {
                "inKey": validate.any(str, None),
                "videoNo": validate.any(int, None),
                "videoId": validate.any(str, None),
                "videoTitle": validate.any(str, None),
                "videoCategory": validate.any(str, None),
                "adult": bool,
                "channel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union_get(
                "adult",
                "inKey",
                "videoId",
                "videoNo",
                "channel",
                "videoTitle",
                "Videocategory",
            ),
        )
    
    xǁChzzkAPIǁget_videos__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁChzzkAPIǁget_videos__mutmut_1': xǁChzzkAPIǁget_videos__mutmut_1, 
        'xǁChzzkAPIǁget_videos__mutmut_2': xǁChzzkAPIǁget_videos__mutmut_2, 
        'xǁChzzkAPIǁget_videos__mutmut_3': xǁChzzkAPIǁget_videos__mutmut_3, 
        'xǁChzzkAPIǁget_videos__mutmut_4': xǁChzzkAPIǁget_videos__mutmut_4, 
        'xǁChzzkAPIǁget_videos__mutmut_5': xǁChzzkAPIǁget_videos__mutmut_5, 
        'xǁChzzkAPIǁget_videos__mutmut_6': xǁChzzkAPIǁget_videos__mutmut_6, 
        'xǁChzzkAPIǁget_videos__mutmut_7': xǁChzzkAPIǁget_videos__mutmut_7, 
        'xǁChzzkAPIǁget_videos__mutmut_8': xǁChzzkAPIǁget_videos__mutmut_8, 
        'xǁChzzkAPIǁget_videos__mutmut_9': xǁChzzkAPIǁget_videos__mutmut_9, 
        'xǁChzzkAPIǁget_videos__mutmut_10': xǁChzzkAPIǁget_videos__mutmut_10, 
        'xǁChzzkAPIǁget_videos__mutmut_11': xǁChzzkAPIǁget_videos__mutmut_11, 
        'xǁChzzkAPIǁget_videos__mutmut_12': xǁChzzkAPIǁget_videos__mutmut_12, 
        'xǁChzzkAPIǁget_videos__mutmut_13': xǁChzzkAPIǁget_videos__mutmut_13, 
        'xǁChzzkAPIǁget_videos__mutmut_14': xǁChzzkAPIǁget_videos__mutmut_14, 
        'xǁChzzkAPIǁget_videos__mutmut_15': xǁChzzkAPIǁget_videos__mutmut_15, 
        'xǁChzzkAPIǁget_videos__mutmut_16': xǁChzzkAPIǁget_videos__mutmut_16, 
        'xǁChzzkAPIǁget_videos__mutmut_17': xǁChzzkAPIǁget_videos__mutmut_17, 
        'xǁChzzkAPIǁget_videos__mutmut_18': xǁChzzkAPIǁget_videos__mutmut_18, 
        'xǁChzzkAPIǁget_videos__mutmut_19': xǁChzzkAPIǁget_videos__mutmut_19, 
        'xǁChzzkAPIǁget_videos__mutmut_20': xǁChzzkAPIǁget_videos__mutmut_20, 
        'xǁChzzkAPIǁget_videos__mutmut_21': xǁChzzkAPIǁget_videos__mutmut_21, 
        'xǁChzzkAPIǁget_videos__mutmut_22': xǁChzzkAPIǁget_videos__mutmut_22, 
        'xǁChzzkAPIǁget_videos__mutmut_23': xǁChzzkAPIǁget_videos__mutmut_23, 
        'xǁChzzkAPIǁget_videos__mutmut_24': xǁChzzkAPIǁget_videos__mutmut_24, 
        'xǁChzzkAPIǁget_videos__mutmut_25': xǁChzzkAPIǁget_videos__mutmut_25, 
        'xǁChzzkAPIǁget_videos__mutmut_26': xǁChzzkAPIǁget_videos__mutmut_26, 
        'xǁChzzkAPIǁget_videos__mutmut_27': xǁChzzkAPIǁget_videos__mutmut_27, 
        'xǁChzzkAPIǁget_videos__mutmut_28': xǁChzzkAPIǁget_videos__mutmut_28, 
        'xǁChzzkAPIǁget_videos__mutmut_29': xǁChzzkAPIǁget_videos__mutmut_29, 
        'xǁChzzkAPIǁget_videos__mutmut_30': xǁChzzkAPIǁget_videos__mutmut_30, 
        'xǁChzzkAPIǁget_videos__mutmut_31': xǁChzzkAPIǁget_videos__mutmut_31, 
        'xǁChzzkAPIǁget_videos__mutmut_32': xǁChzzkAPIǁget_videos__mutmut_32, 
        'xǁChzzkAPIǁget_videos__mutmut_33': xǁChzzkAPIǁget_videos__mutmut_33, 
        'xǁChzzkAPIǁget_videos__mutmut_34': xǁChzzkAPIǁget_videos__mutmut_34, 
        'xǁChzzkAPIǁget_videos__mutmut_35': xǁChzzkAPIǁget_videos__mutmut_35, 
        'xǁChzzkAPIǁget_videos__mutmut_36': xǁChzzkAPIǁget_videos__mutmut_36, 
        'xǁChzzkAPIǁget_videos__mutmut_37': xǁChzzkAPIǁget_videos__mutmut_37, 
        'xǁChzzkAPIǁget_videos__mutmut_38': xǁChzzkAPIǁget_videos__mutmut_38, 
        'xǁChzzkAPIǁget_videos__mutmut_39': xǁChzzkAPIǁget_videos__mutmut_39, 
        'xǁChzzkAPIǁget_videos__mutmut_40': xǁChzzkAPIǁget_videos__mutmut_40, 
        'xǁChzzkAPIǁget_videos__mutmut_41': xǁChzzkAPIǁget_videos__mutmut_41, 
        'xǁChzzkAPIǁget_videos__mutmut_42': xǁChzzkAPIǁget_videos__mutmut_42, 
        'xǁChzzkAPIǁget_videos__mutmut_43': xǁChzzkAPIǁget_videos__mutmut_43, 
        'xǁChzzkAPIǁget_videos__mutmut_44': xǁChzzkAPIǁget_videos__mutmut_44, 
        'xǁChzzkAPIǁget_videos__mutmut_45': xǁChzzkAPIǁget_videos__mutmut_45, 
        'xǁChzzkAPIǁget_videos__mutmut_46': xǁChzzkAPIǁget_videos__mutmut_46, 
        'xǁChzzkAPIǁget_videos__mutmut_47': xǁChzzkAPIǁget_videos__mutmut_47, 
        'xǁChzzkAPIǁget_videos__mutmut_48': xǁChzzkAPIǁget_videos__mutmut_48, 
        'xǁChzzkAPIǁget_videos__mutmut_49': xǁChzzkAPIǁget_videos__mutmut_49, 
        'xǁChzzkAPIǁget_videos__mutmut_50': xǁChzzkAPIǁget_videos__mutmut_50, 
        'xǁChzzkAPIǁget_videos__mutmut_51': xǁChzzkAPIǁget_videos__mutmut_51, 
        'xǁChzzkAPIǁget_videos__mutmut_52': xǁChzzkAPIǁget_videos__mutmut_52, 
        'xǁChzzkAPIǁget_videos__mutmut_53': xǁChzzkAPIǁget_videos__mutmut_53, 
        'xǁChzzkAPIǁget_videos__mutmut_54': xǁChzzkAPIǁget_videos__mutmut_54, 
        'xǁChzzkAPIǁget_videos__mutmut_55': xǁChzzkAPIǁget_videos__mutmut_55, 
        'xǁChzzkAPIǁget_videos__mutmut_56': xǁChzzkAPIǁget_videos__mutmut_56, 
        'xǁChzzkAPIǁget_videos__mutmut_57': xǁChzzkAPIǁget_videos__mutmut_57, 
        'xǁChzzkAPIǁget_videos__mutmut_58': xǁChzzkAPIǁget_videos__mutmut_58, 
        'xǁChzzkAPIǁget_videos__mutmut_59': xǁChzzkAPIǁget_videos__mutmut_59, 
        'xǁChzzkAPIǁget_videos__mutmut_60': xǁChzzkAPIǁget_videos__mutmut_60, 
        'xǁChzzkAPIǁget_videos__mutmut_61': xǁChzzkAPIǁget_videos__mutmut_61, 
        'xǁChzzkAPIǁget_videos__mutmut_62': xǁChzzkAPIǁget_videos__mutmut_62, 
        'xǁChzzkAPIǁget_videos__mutmut_63': xǁChzzkAPIǁget_videos__mutmut_63, 
        'xǁChzzkAPIǁget_videos__mutmut_64': xǁChzzkAPIǁget_videos__mutmut_64, 
        'xǁChzzkAPIǁget_videos__mutmut_65': xǁChzzkAPIǁget_videos__mutmut_65, 
        'xǁChzzkAPIǁget_videos__mutmut_66': xǁChzzkAPIǁget_videos__mutmut_66, 
        'xǁChzzkAPIǁget_videos__mutmut_67': xǁChzzkAPIǁget_videos__mutmut_67, 
        'xǁChzzkAPIǁget_videos__mutmut_68': xǁChzzkAPIǁget_videos__mutmut_68, 
        'xǁChzzkAPIǁget_videos__mutmut_69': xǁChzzkAPIǁget_videos__mutmut_69, 
        'xǁChzzkAPIǁget_videos__mutmut_70': xǁChzzkAPIǁget_videos__mutmut_70, 
        'xǁChzzkAPIǁget_videos__mutmut_71': xǁChzzkAPIǁget_videos__mutmut_71, 
        'xǁChzzkAPIǁget_videos__mutmut_72': xǁChzzkAPIǁget_videos__mutmut_72, 
        'xǁChzzkAPIǁget_videos__mutmut_73': xǁChzzkAPIǁget_videos__mutmut_73, 
        'xǁChzzkAPIǁget_videos__mutmut_74': xǁChzzkAPIǁget_videos__mutmut_74, 
        'xǁChzzkAPIǁget_videos__mutmut_75': xǁChzzkAPIǁget_videos__mutmut_75, 
        'xǁChzzkAPIǁget_videos__mutmut_76': xǁChzzkAPIǁget_videos__mutmut_76, 
        'xǁChzzkAPIǁget_videos__mutmut_77': xǁChzzkAPIǁget_videos__mutmut_77, 
        'xǁChzzkAPIǁget_videos__mutmut_78': xǁChzzkAPIǁget_videos__mutmut_78, 
        'xǁChzzkAPIǁget_videos__mutmut_79': xǁChzzkAPIǁget_videos__mutmut_79, 
        'xǁChzzkAPIǁget_videos__mutmut_80': xǁChzzkAPIǁget_videos__mutmut_80, 
        'xǁChzzkAPIǁget_videos__mutmut_81': xǁChzzkAPIǁget_videos__mutmut_81, 
        'xǁChzzkAPIǁget_videos__mutmut_82': xǁChzzkAPIǁget_videos__mutmut_82, 
        'xǁChzzkAPIǁget_videos__mutmut_83': xǁChzzkAPIǁget_videos__mutmut_83, 
        'xǁChzzkAPIǁget_videos__mutmut_84': xǁChzzkAPIǁget_videos__mutmut_84, 
        'xǁChzzkAPIǁget_videos__mutmut_85': xǁChzzkAPIǁget_videos__mutmut_85, 
        'xǁChzzkAPIǁget_videos__mutmut_86': xǁChzzkAPIǁget_videos__mutmut_86, 
        'xǁChzzkAPIǁget_videos__mutmut_87': xǁChzzkAPIǁget_videos__mutmut_87, 
        'xǁChzzkAPIǁget_videos__mutmut_88': xǁChzzkAPIǁget_videos__mutmut_88, 
        'xǁChzzkAPIǁget_videos__mutmut_89': xǁChzzkAPIǁget_videos__mutmut_89, 
        'xǁChzzkAPIǁget_videos__mutmut_90': xǁChzzkAPIǁget_videos__mutmut_90, 
        'xǁChzzkAPIǁget_videos__mutmut_91': xǁChzzkAPIǁget_videos__mutmut_91, 
        'xǁChzzkAPIǁget_videos__mutmut_92': xǁChzzkAPIǁget_videos__mutmut_92, 
        'xǁChzzkAPIǁget_videos__mutmut_93': xǁChzzkAPIǁget_videos__mutmut_93, 
        'xǁChzzkAPIǁget_videos__mutmut_94': xǁChzzkAPIǁget_videos__mutmut_94, 
        'xǁChzzkAPIǁget_videos__mutmut_95': xǁChzzkAPIǁget_videos__mutmut_95, 
        'xǁChzzkAPIǁget_videos__mutmut_96': xǁChzzkAPIǁget_videos__mutmut_96, 
        'xǁChzzkAPIǁget_videos__mutmut_97': xǁChzzkAPIǁget_videos__mutmut_97, 
        'xǁChzzkAPIǁget_videos__mutmut_98': xǁChzzkAPIǁget_videos__mutmut_98, 
        'xǁChzzkAPIǁget_videos__mutmut_99': xǁChzzkAPIǁget_videos__mutmut_99, 
        'xǁChzzkAPIǁget_videos__mutmut_100': xǁChzzkAPIǁget_videos__mutmut_100, 
        'xǁChzzkAPIǁget_videos__mutmut_101': xǁChzzkAPIǁget_videos__mutmut_101
    }
    
    def get_videos(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁChzzkAPIǁget_videos__mutmut_orig"), object.__getattribute__(self, "xǁChzzkAPIǁget_videos__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_videos.__signature__ = _mutmut_signature(xǁChzzkAPIǁget_videos__mutmut_orig)
    xǁChzzkAPIǁget_videos__mutmut_orig.__name__ = 'xǁChzzkAPIǁget_videos'

    def xǁChzzkAPIǁget_clips__mutmut_orig(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_1(self, clip_id):
        return self._query_api(
            None,
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_2(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            None,
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_3(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            None,
        )

    def xǁChzzkAPIǁget_clips__mutmut_4(self, clip_id):
        return self._query_api(
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_5(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_6(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            )

    def xǁChzzkAPIǁget_clips__mutmut_7(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=None),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_8(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional(None): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_9(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("XXinKeyXX"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_10(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inkey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_11(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("INKEY"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_12(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("Inkey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_13(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(None, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_14(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_15(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, ),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_16(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional(None): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_17(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("XXvideoIdXX"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_18(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoid"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_19(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("VIDEOID"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_20(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("Videoid"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_21(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(None, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_22(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_23(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, ),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_24(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "XXcontentIdXX": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_25(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentid": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_26(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "CONTENTID": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_27(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "Contentid": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_28(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "XXcontentTitleXX": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_29(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contenttitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_30(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "CONTENTTITLE": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_31(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "Contenttitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_32(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "XXadultXX": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_33(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "ADULT": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_34(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "Adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_35(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "XXownerChannelXX": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_36(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerchannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_37(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "OWNERCHANNEL": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_38(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "Ownerchannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_39(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    None,
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_40(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    None,
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_41(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_42(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_43(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"XXchannelNameXX": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_44(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelname": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_45(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"CHANNELNAME": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_46(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"Channelname": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_47(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get(None),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_48(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("XXchannelNameXX"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_49(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelname"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_50(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("CHANNELNAME"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_51(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("Channelname"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_52(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union(None),
        )

    def xǁChzzkAPIǁget_clips__mutmut_53(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get(None),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_54(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("XXadultXX"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_55(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("ADULT"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_56(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("Adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_57(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get(None),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_58(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("XXinKeyXX"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_59(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inkey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_60(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("INKEY"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_61(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("Inkey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_62(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get(None),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_63(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("XXvideoIdXX"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_64(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoid"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_65(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("VIDEOID"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_66(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("Videoid"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_67(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get(None),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_68(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("XXcontentIdXX"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_69(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentid"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_70(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("CONTENTID"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_71(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("Contentid"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_72(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get(None),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_73(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("XXownerChannelXX"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_74(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerchannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_75(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("OWNERCHANNEL"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_76(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("Ownerchannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_77(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get(None),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_78(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("XXcontentTitleXX"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_79(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contenttitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_80(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("CONTENTTITLE"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_81(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("Contenttitle"),
                validate.transform(lambda _: None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_82(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(None),
            )),
        )

    def xǁChzzkAPIǁget_clips__mutmut_83(self, clip_id):
        return self._query_api(
            self._CLIP_URL.format(clip_id=clip_id),
            {
                validate.optional("inKey"): validate.any(str, None),
                validate.optional("videoId"): validate.any(str, None),
                "contentId": str,
                "contentTitle": str,
                "adult": bool,
                "ownerChannel": validate.all(
                    {"channelName": str},
                    validate.get("channelName"),
                ),
            },
            validate.union((
                validate.get("adult"),
                validate.get("inKey"),
                validate.get("videoId"),
                validate.get("contentId"),
                validate.get("ownerChannel"),
                validate.get("contentTitle"),
                validate.transform(lambda _: 0),
            )),
        )
    
    xǁChzzkAPIǁget_clips__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁChzzkAPIǁget_clips__mutmut_1': xǁChzzkAPIǁget_clips__mutmut_1, 
        'xǁChzzkAPIǁget_clips__mutmut_2': xǁChzzkAPIǁget_clips__mutmut_2, 
        'xǁChzzkAPIǁget_clips__mutmut_3': xǁChzzkAPIǁget_clips__mutmut_3, 
        'xǁChzzkAPIǁget_clips__mutmut_4': xǁChzzkAPIǁget_clips__mutmut_4, 
        'xǁChzzkAPIǁget_clips__mutmut_5': xǁChzzkAPIǁget_clips__mutmut_5, 
        'xǁChzzkAPIǁget_clips__mutmut_6': xǁChzzkAPIǁget_clips__mutmut_6, 
        'xǁChzzkAPIǁget_clips__mutmut_7': xǁChzzkAPIǁget_clips__mutmut_7, 
        'xǁChzzkAPIǁget_clips__mutmut_8': xǁChzzkAPIǁget_clips__mutmut_8, 
        'xǁChzzkAPIǁget_clips__mutmut_9': xǁChzzkAPIǁget_clips__mutmut_9, 
        'xǁChzzkAPIǁget_clips__mutmut_10': xǁChzzkAPIǁget_clips__mutmut_10, 
        'xǁChzzkAPIǁget_clips__mutmut_11': xǁChzzkAPIǁget_clips__mutmut_11, 
        'xǁChzzkAPIǁget_clips__mutmut_12': xǁChzzkAPIǁget_clips__mutmut_12, 
        'xǁChzzkAPIǁget_clips__mutmut_13': xǁChzzkAPIǁget_clips__mutmut_13, 
        'xǁChzzkAPIǁget_clips__mutmut_14': xǁChzzkAPIǁget_clips__mutmut_14, 
        'xǁChzzkAPIǁget_clips__mutmut_15': xǁChzzkAPIǁget_clips__mutmut_15, 
        'xǁChzzkAPIǁget_clips__mutmut_16': xǁChzzkAPIǁget_clips__mutmut_16, 
        'xǁChzzkAPIǁget_clips__mutmut_17': xǁChzzkAPIǁget_clips__mutmut_17, 
        'xǁChzzkAPIǁget_clips__mutmut_18': xǁChzzkAPIǁget_clips__mutmut_18, 
        'xǁChzzkAPIǁget_clips__mutmut_19': xǁChzzkAPIǁget_clips__mutmut_19, 
        'xǁChzzkAPIǁget_clips__mutmut_20': xǁChzzkAPIǁget_clips__mutmut_20, 
        'xǁChzzkAPIǁget_clips__mutmut_21': xǁChzzkAPIǁget_clips__mutmut_21, 
        'xǁChzzkAPIǁget_clips__mutmut_22': xǁChzzkAPIǁget_clips__mutmut_22, 
        'xǁChzzkAPIǁget_clips__mutmut_23': xǁChzzkAPIǁget_clips__mutmut_23, 
        'xǁChzzkAPIǁget_clips__mutmut_24': xǁChzzkAPIǁget_clips__mutmut_24, 
        'xǁChzzkAPIǁget_clips__mutmut_25': xǁChzzkAPIǁget_clips__mutmut_25, 
        'xǁChzzkAPIǁget_clips__mutmut_26': xǁChzzkAPIǁget_clips__mutmut_26, 
        'xǁChzzkAPIǁget_clips__mutmut_27': xǁChzzkAPIǁget_clips__mutmut_27, 
        'xǁChzzkAPIǁget_clips__mutmut_28': xǁChzzkAPIǁget_clips__mutmut_28, 
        'xǁChzzkAPIǁget_clips__mutmut_29': xǁChzzkAPIǁget_clips__mutmut_29, 
        'xǁChzzkAPIǁget_clips__mutmut_30': xǁChzzkAPIǁget_clips__mutmut_30, 
        'xǁChzzkAPIǁget_clips__mutmut_31': xǁChzzkAPIǁget_clips__mutmut_31, 
        'xǁChzzkAPIǁget_clips__mutmut_32': xǁChzzkAPIǁget_clips__mutmut_32, 
        'xǁChzzkAPIǁget_clips__mutmut_33': xǁChzzkAPIǁget_clips__mutmut_33, 
        'xǁChzzkAPIǁget_clips__mutmut_34': xǁChzzkAPIǁget_clips__mutmut_34, 
        'xǁChzzkAPIǁget_clips__mutmut_35': xǁChzzkAPIǁget_clips__mutmut_35, 
        'xǁChzzkAPIǁget_clips__mutmut_36': xǁChzzkAPIǁget_clips__mutmut_36, 
        'xǁChzzkAPIǁget_clips__mutmut_37': xǁChzzkAPIǁget_clips__mutmut_37, 
        'xǁChzzkAPIǁget_clips__mutmut_38': xǁChzzkAPIǁget_clips__mutmut_38, 
        'xǁChzzkAPIǁget_clips__mutmut_39': xǁChzzkAPIǁget_clips__mutmut_39, 
        'xǁChzzkAPIǁget_clips__mutmut_40': xǁChzzkAPIǁget_clips__mutmut_40, 
        'xǁChzzkAPIǁget_clips__mutmut_41': xǁChzzkAPIǁget_clips__mutmut_41, 
        'xǁChzzkAPIǁget_clips__mutmut_42': xǁChzzkAPIǁget_clips__mutmut_42, 
        'xǁChzzkAPIǁget_clips__mutmut_43': xǁChzzkAPIǁget_clips__mutmut_43, 
        'xǁChzzkAPIǁget_clips__mutmut_44': xǁChzzkAPIǁget_clips__mutmut_44, 
        'xǁChzzkAPIǁget_clips__mutmut_45': xǁChzzkAPIǁget_clips__mutmut_45, 
        'xǁChzzkAPIǁget_clips__mutmut_46': xǁChzzkAPIǁget_clips__mutmut_46, 
        'xǁChzzkAPIǁget_clips__mutmut_47': xǁChzzkAPIǁget_clips__mutmut_47, 
        'xǁChzzkAPIǁget_clips__mutmut_48': xǁChzzkAPIǁget_clips__mutmut_48, 
        'xǁChzzkAPIǁget_clips__mutmut_49': xǁChzzkAPIǁget_clips__mutmut_49, 
        'xǁChzzkAPIǁget_clips__mutmut_50': xǁChzzkAPIǁget_clips__mutmut_50, 
        'xǁChzzkAPIǁget_clips__mutmut_51': xǁChzzkAPIǁget_clips__mutmut_51, 
        'xǁChzzkAPIǁget_clips__mutmut_52': xǁChzzkAPIǁget_clips__mutmut_52, 
        'xǁChzzkAPIǁget_clips__mutmut_53': xǁChzzkAPIǁget_clips__mutmut_53, 
        'xǁChzzkAPIǁget_clips__mutmut_54': xǁChzzkAPIǁget_clips__mutmut_54, 
        'xǁChzzkAPIǁget_clips__mutmut_55': xǁChzzkAPIǁget_clips__mutmut_55, 
        'xǁChzzkAPIǁget_clips__mutmut_56': xǁChzzkAPIǁget_clips__mutmut_56, 
        'xǁChzzkAPIǁget_clips__mutmut_57': xǁChzzkAPIǁget_clips__mutmut_57, 
        'xǁChzzkAPIǁget_clips__mutmut_58': xǁChzzkAPIǁget_clips__mutmut_58, 
        'xǁChzzkAPIǁget_clips__mutmut_59': xǁChzzkAPIǁget_clips__mutmut_59, 
        'xǁChzzkAPIǁget_clips__mutmut_60': xǁChzzkAPIǁget_clips__mutmut_60, 
        'xǁChzzkAPIǁget_clips__mutmut_61': xǁChzzkAPIǁget_clips__mutmut_61, 
        'xǁChzzkAPIǁget_clips__mutmut_62': xǁChzzkAPIǁget_clips__mutmut_62, 
        'xǁChzzkAPIǁget_clips__mutmut_63': xǁChzzkAPIǁget_clips__mutmut_63, 
        'xǁChzzkAPIǁget_clips__mutmut_64': xǁChzzkAPIǁget_clips__mutmut_64, 
        'xǁChzzkAPIǁget_clips__mutmut_65': xǁChzzkAPIǁget_clips__mutmut_65, 
        'xǁChzzkAPIǁget_clips__mutmut_66': xǁChzzkAPIǁget_clips__mutmut_66, 
        'xǁChzzkAPIǁget_clips__mutmut_67': xǁChzzkAPIǁget_clips__mutmut_67, 
        'xǁChzzkAPIǁget_clips__mutmut_68': xǁChzzkAPIǁget_clips__mutmut_68, 
        'xǁChzzkAPIǁget_clips__mutmut_69': xǁChzzkAPIǁget_clips__mutmut_69, 
        'xǁChzzkAPIǁget_clips__mutmut_70': xǁChzzkAPIǁget_clips__mutmut_70, 
        'xǁChzzkAPIǁget_clips__mutmut_71': xǁChzzkAPIǁget_clips__mutmut_71, 
        'xǁChzzkAPIǁget_clips__mutmut_72': xǁChzzkAPIǁget_clips__mutmut_72, 
        'xǁChzzkAPIǁget_clips__mutmut_73': xǁChzzkAPIǁget_clips__mutmut_73, 
        'xǁChzzkAPIǁget_clips__mutmut_74': xǁChzzkAPIǁget_clips__mutmut_74, 
        'xǁChzzkAPIǁget_clips__mutmut_75': xǁChzzkAPIǁget_clips__mutmut_75, 
        'xǁChzzkAPIǁget_clips__mutmut_76': xǁChzzkAPIǁget_clips__mutmut_76, 
        'xǁChzzkAPIǁget_clips__mutmut_77': xǁChzzkAPIǁget_clips__mutmut_77, 
        'xǁChzzkAPIǁget_clips__mutmut_78': xǁChzzkAPIǁget_clips__mutmut_78, 
        'xǁChzzkAPIǁget_clips__mutmut_79': xǁChzzkAPIǁget_clips__mutmut_79, 
        'xǁChzzkAPIǁget_clips__mutmut_80': xǁChzzkAPIǁget_clips__mutmut_80, 
        'xǁChzzkAPIǁget_clips__mutmut_81': xǁChzzkAPIǁget_clips__mutmut_81, 
        'xǁChzzkAPIǁget_clips__mutmut_82': xǁChzzkAPIǁget_clips__mutmut_82, 
        'xǁChzzkAPIǁget_clips__mutmut_83': xǁChzzkAPIǁget_clips__mutmut_83
    }
    
    def get_clips(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁChzzkAPIǁget_clips__mutmut_orig"), object.__getattribute__(self, "xǁChzzkAPIǁget_clips__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_clips.__signature__ = _mutmut_signature(xǁChzzkAPIǁget_clips__mutmut_orig)
    xǁChzzkAPIǁget_clips__mutmut_orig.__name__ = 'xǁChzzkAPIǁget_clips'


@pluginmatcher(
    name="live",
    pattern=re.compile(
        r"https?://chzzk\.naver\.com/live/(?P<channel_id>[^/?]+)",
    ),
)
@pluginmatcher(
    name="video",
    pattern=re.compile(
        r"https?://chzzk\.naver\.com/video/(?P<video_id>[^/?]+)",
    ),
)
@pluginmatcher(
    name="clip",
    pattern=re.compile(
        r"https?://chzzk\.naver\.com/clips/(?P<clip_id>[^/?]+)",
    ),
)
class Chzzk(Plugin):
    _API_VOD_PLAYBACK_URL = "https://apis.naver.com/neonplayer/vodplay/v2/playback/{video_id}?key={in_key}"

    _STATUS_OPEN = "OPEN"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._api = ChzzkAPI(self.session)

    def _get_live(self, channel_id):
        datatype, data = self._api.get_live_detail(channel_id)
        if datatype == "error":
            log.error(data)
            return
        if data is None:
            return

        media, status, self.id, self.author, self.category, self.title, adult = data
        if status != self._STATUS_OPEN:
            log.error("The stream is unavailable")
            return
        if media is None:
            log.error(f"This stream is {'for adults only' if adult else 'unavailable'}")
            return

        for media_id, media_protocol, media_path in media:
            if media_protocol == "HLS" and media_id == "HLS":
                return HLSStream.parse_variant_playlist(
                    self.session,
                    media_path,
                    channel_id=channel_id,
                    ffmpeg_options={"copyts": True},
                )

    def _get_vod_playback(self, datatype, data):
        if datatype == "error":
            log.error(data)
            return

        adult, in_key, vod_id, *metadata = data

        if in_key is None or vod_id is None:
            log.error(f"This stream is {'for adults only' if adult else 'unavailable'}")
            return

        self.id, self.author, self.title, self.category = metadata

        for name, stream in DASHStream.parse_manifest(
            self.session,
            self._API_VOD_PLAYBACK_URL.format(video_id=vod_id, in_key=in_key),
            headers={"Accept": "application/dash+xml"},
        ).items():
            if stream.video_representation.mimeType == "video/mp2t":
                yield name, stream

    def _get_video(self, video_id):
        return self._get_vod_playback(
            *self._api.get_videos(video_id),
        )

    def _get_clip(self, clip_id):
        return self._get_vod_playback(
            *self._api.get_clips(clip_id),
        )

    def _get_streams(self):
        if self.matches["live"]:
            return self._get_live(self.match["channel_id"])
        elif self.matches["video"]:
            return self._get_video(self.match["video_id"])
        elif self.matches["clip"]:
            return self._get_clip(self.match["clip_id"])


__plugin__ = Chzzk

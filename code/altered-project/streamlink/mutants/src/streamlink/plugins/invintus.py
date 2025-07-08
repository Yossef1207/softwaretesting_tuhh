"""
$description Global live streaming and video on-demand hosting platform.
$url player.invintus.com
$type live, vod
"""

import json
import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream
from streamlink.utils.url import update_scheme
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
    re.compile(r"https?://player\.invintus\.com/\?clientID=(\d+)&eventID=(\d+)"),
)
class InvintusMedia(Plugin):
    WSC_API_KEY = "7WhiEBzijpritypp8bqcU7pfU9uicDR"  # hard coded in the middle of https://player.invintus.com/app.js
    API_URL = "https://api.v3.invintusmedia.com/v2/Event/getDetailed"

    api_response_schema = validate.Schema({"data": {"streamingURIs": {"main": validate.url()}}})

    def _get_streams(self):
        postdata = {
            "clientID": self.match.group(1),
            "showEncoder": True,
            "showMediaAssets": True,
            "showStreams": True,
            "includePrivate": False,
            "advancedDetails": True,
            "VAST": True,
            "eventID": self.match.group(2),
        }
        headers = {
            "Content-Type": "application/json",
            "wsc-api-key": self.WSC_API_KEY,
            "Authorization": "embedder",
        }
        res = self.session.http.post(self.API_URL, data=json.dumps(postdata), headers=headers)
        api_response = self.session.http.json(res, schema=self.api_response_schema)
        if api_response is None:
            return

        hls_url = api_response["data"]["streamingURIs"]["main"]
        return HLSStream.parse_variant_playlist(self.session, update_scheme("https://", hls_url))


__plugin__ = InvintusMedia

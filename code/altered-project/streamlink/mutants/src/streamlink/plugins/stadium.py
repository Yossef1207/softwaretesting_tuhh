"""
$description Sporting live stream and video content, owned by Silver Chalice and Sinclair Broadcast Group.
$url watchstadium.com
$type live, vod
"""

import logging
import re

from streamlink.plugin import Plugin, PluginError, pluginmatcher
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
    re.compile(r"https?://(?:www\.)?watchstadium\.com/"),
)
class Stadium(Plugin):
    _API_URL = "https://edge.api.brightcove.com/playback/v1/accounts/{data_account}/videos/{data_video_id}"
    _PLAYER_URL = "https://players.brightcove.net/{data_account}/{data_player}_default/index.min.js"

    def _get_streams(self):
        try:
            data = self.session.http.get(
                self.url,
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_find(".//video[@id='brightcove_video_player']"),
                    validate.union_get("data-video-id", "data-account", "data-ad-config-id", "data-player"),
                ),
            )
        except PluginError:
            return
        data_video_id, data_account, data_ad_config_id, data_player = data

        url = self._PLAYER_URL.format(data_account=data_account, data_player=data_player)
        policy_key = self.session.http.get(
            url,
            schema=validate.Schema(
                re.compile(r"""options:\s*{.+policyKey:\s*"([^"]+)""", re.DOTALL),
                validate.any(None, validate.get(1)),
            ),
        )
        if not policy_key:
            return

        url = self._API_URL.format(data_account=data_account, data_video_id=data_video_id)
        if data_ad_config_id is not None:
            url = update_qsd(url, dict(ad_config_id=data_ad_config_id))

        streams = self.session.http.get(
            url,
            headers={"Accept": f"application/json;pk={policy_key}"},
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "sources": [
                        {
                            validate.optional("type"): str,
                            "src": validate.url(),
                        },
                    ],
                },
                validate.get("sources"),
                validate.filter(lambda source: source.get("type") == "application/x-mpegURL"),
            ),
        )

        for stream in streams:
            return HLSStream.parse_variant_playlist(self.session, stream["src"])


__plugin__ = Stadium

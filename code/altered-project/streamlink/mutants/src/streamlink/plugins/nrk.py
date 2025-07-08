"""
$description Live TV channels and video on-demand service from NRK, a Norwegian public, state-owned broadcaster.
$url tv.nrk.no
$url radio.nrk.no
$type live, vod
$region Norway
"""

import logging
import re

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream
from streamlink.stream.http import HTTPStream


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
    re.compile(r"https?://(?:tv|radio)\.nrk\.no/(program|direkte|serie|podkast)(?:/.+)?/([^/]+)"),
)
class NRK(Plugin):
    _URL_MANIFEST = "https://psapi.nrk.no/playback/manifest/{manifest_type}/{program_id}"
    _URL_METADATA = "https://psapi.nrk.no/playback/metadata/{manifest_type}/{program_id}?eea-portability=true"

    _MAP_MANIFEST_TYPE = {
        "direkte": "channel",
        "serie": "program",
        "program": "program",
        "podkast": "podcast",
    }

    def _get_metadata(self, manifest_type, program_id):
        url_metadata = self._URL_METADATA.format(manifest_type=manifest_type, program_id=program_id)
        non_playable = self.session.http.get(
            url_metadata,
            schema=validate.Schema(
                validate.parse_json(),
                {
                    validate.optional("nonPlayable"): validate.none_or_all(
                        {
                            "reason": str,
                            "endUserMessage": str,
                        },
                        validate.union_get("reason", "endUserMessage"),
                    ),
                },
                validate.get("nonPlayable"),
            ),
        )
        if non_playable:
            reason, end_user_message = non_playable
            log.error(f"Not playable: {reason} - {end_user_message or 'error'}")
            return False

        return True

    def _update_program_id(self, program_id):
        new_program_id = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_xpath_string(".//meta[@property='nrk:program-id']/@content"),
            ),
        )
        return new_program_id or program_id

    def _get_assets(self, manifest_type, program_id):
        return self.session.http.get(
            self._URL_MANIFEST.format(manifest_type=manifest_type, program_id=program_id),
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "playable": {
                        "assets": [
                            validate.all(
                                {
                                    "url": validate.url(),
                                    "format": str,
                                },
                                validate.union_get("format", "url"),
                            ),
                        ],
                    },
                },
                validate.get(("playable", "assets")),
            ),
        )

    def _get_streams(self):
        program_type, program_id = self.match.groups()
        manifest_type = self._MAP_MANIFEST_TYPE.get(program_type)
        if manifest_type is None:
            log.error(f"Unknown program type '{program_type}'")
            return

        program_id = self._update_program_id(program_id)
        if self._get_metadata(manifest_type, program_id) is False:
            return

        assets = self._get_assets(manifest_type, program_id)

        # just return the first item
        for stream_type, stream_url in assets:
            if stream_type == "HLS":
                return HLSStream.parse_variant_playlist(self.session, stream_url)
            return [("live", HTTPStream(self.session, stream_url))]


__plugin__ = NRK

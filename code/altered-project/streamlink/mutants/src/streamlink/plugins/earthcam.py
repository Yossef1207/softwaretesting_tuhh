"""
$description A network of live webcams for tourism and entertainment.
$url earthcam.com
$type live, vod
$metadata author
$metadata category
$metadata title
$notes Only works for the cams hosted on EarthCam
"""

import logging
import re
from urllib.parse import urlparse

from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream
from streamlink.utils.parse import parse_qsd
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
    re.compile(r"https?://(?:www\.)?earthcam\.com/"),
)
class EarthCam(Plugin):
    def _get_streams(self):
        data = self.session.http.get(
            self.url,
            schema=validate.Schema(
                re.compile(r"""var\s+json_base\s*=\s*(?P<json>{.*?});""", re.DOTALL),
                validate.none_or_all(
                    validate.get("json"),
                    validate.parse_json(),
                    {
                        "cam": {
                            str: {
                                "live_type": str,
                                "html5_streamingdomain": str,
                                "html5_streampath": str,
                                "group": str,
                                "location": str,
                                "title": str,
                                "liveon": str,
                                "defaulttab": str,
                            },
                        },
                    },
                    validate.get("cam"),
                ),
            ),
        )
        if not data:
            return

        cam_name = parse_qsd(urlparse(self.url).query).get("cam") or next(iter(data.keys()), None)
        cam_data = data.get(cam_name)
        if not cam_data:
            return

        # exclude everything other than live video streams
        if cam_data["live_type"] != "flashvideo" or cam_data["liveon"] != "true" or cam_data["defaulttab"] != "live":
            return

        log.debug(f"Found cam {cam_name}")
        hls_domain = cam_data["html5_streamingdomain"]
        hls_playpath = cam_data["html5_streampath"]

        self.author = cam_data["group"]
        self.category = cam_data["location"]
        self.title = cam_data["title"]

        if hls_playpath:
            hls_url = update_scheme("https://", f"{hls_domain}{hls_playpath}")
            yield from HLSStream.parse_variant_playlist(self.session, hls_url).items()


__plugin__ = EarthCam

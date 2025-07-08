"""
$description Live TV channel and video on-demand service from CMM, a Spanish public, state-owned broadcaster.
$url cmmedia.es
$type live, vod
$metadata id
$metadata author
$metadata category
$metadata title
$notes Content not licensed for digital distribution is unavailable via the live channel stream.
"""

import logging
import re

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


@pluginmatcher(re.compile(r"https?://(?:www\.)?cmmedia\.es"))
class CMMedia(Plugin):
    @staticmethod
    def is_restricted(data):
        items = {k: v for k, v in data.items() if k.startswith("is")}
        for k, v in items.items():
            log.debug(f"{k}: {v}")

        restrictions = [k for k, v in items.items() if v]
        if restrictions:
            log.error(f"This site is restricted: ({', '.join(restrictions)})")
            return True

        return False

    def _get_streams(self):
        self.author, iframe_url = self.session.http.get(
            self.url,
            schema=validate.Schema(
                validate.parse_html(),
                validate.union((
                    validate.xml_xpath_string(".//h1[contains(@class, 'btn-title')]/text()"),
                    validate.all(
                        validate.xml_xpath_string(".//script[contains(text(), '/embedIframeJs/')]/text()"),
                        validate.none_or_all(
                            re.compile(r"""{getKs\((?P<q>")(?P<url>.+?)(?P=q)"""),
                            validate.none_or_all(validate.get("url"), validate.url()),
                        ),
                    ),
                )),
            ),
        )
        if not iframe_url:
            return

        m = re.search(r"/p/(\d+)/sp/(\d+)/", iframe_url)
        if not m:
            log.error("Failed to find partner IDs in IFRAME URL")
            return

        p = m.group(1)
        sp = m.group(2)

        json = self.session.http.get(
            iframe_url,
            schema=validate.Schema(
                re.compile(r"twindow\.kalturaIframePackageData\s*=\s*({.*});[\\nt]*var isIE8"),
                validate.none_or_all(
                    validate.get(1),
                    validate.transform(lambda text: re.sub(r'\\"', r'"', text)),
                    validate.parse_json(),
                    validate.any(
                        {
                            "entryResult": {
                                "contextData": {
                                    "isSiteRestricted": bool,
                                    "isCountryRestricted": bool,
                                    "isSessionRestricted": bool,
                                    "isIpAddressRestricted": bool,
                                    "isUserAgentRestricted": bool,
                                    "flavorAssets": [
                                        {
                                            "id": str,
                                        },
                                    ],
                                },
                                "meta": {
                                    "id": str,
                                    "name": str,
                                    "categories": validate.any(None, str),
                                },
                            },
                        },
                        {"error": str},
                    ),
                ),
            ),
        )

        if not json:
            return

        if "error" in json:
            log.error(f"API error: {json['error']}")
            return

        json = json.get("entryResult")

        if self.is_restricted(json["contextData"]):
            return

        self.id = json["meta"]["id"]
        self.title = json["meta"]["name"]
        self.category = json["meta"]["categories"]

        for asset in json["contextData"]["flavorAssets"]:
            yield from HLSStream.parse_variant_playlist(
                self.session,
                (
                    f"https://cdnapisec.kaltura.com/p/{p}/sp/{sp}/playManifest/entryId/{json['meta']['id']}"
                    + f"/flavorIds/{asset['id']}/format/applehttp/protocol/https/a.m3u8"
                ),
                name_fmt="{pixels}_{bitrate}",
            ).items()


__plugin__ = CMMedia

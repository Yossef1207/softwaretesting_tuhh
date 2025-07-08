"""
$description Turkish live TV channels and video on-demand service from Dogan Group, including CNN Turk and Kanal D.
$url cnnturk.com
$url dreamturk.com.tr
$url dreamtv.com.tr
$url kanald.com.tr
$url teve2.com.tr
$type live, vod
"""

import logging
import re
from urllib.parse import urljoin

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


@pluginmatcher(re.compile(r"https?://(?:www\.)?cnnturk\.com/"))
@pluginmatcher(re.compile(r"https?://(?:www\.)?(dreamturk|dreamtv)\.com\.tr/"))
@pluginmatcher(re.compile(r"https?://(?:www\.)?teve2\.com\.tr/"))
@pluginmatcher(re.compile(r"https?://(?:www\.)?kanald\.com\.tr/"))
class Dogan(Plugin):
    # based on the order of matchers
    API_URLS = [
        "/api/media?id={id}",
        "/actions/content/media/{id}",
        "/action/media/{id}",
    ]
    API_URL_OLD = "/actions/media?id={id}"

    @staticmethod
    def _get_hls_url(root):
        schema = validate.Schema(
            validate.xml_xpath_string(".//*[@data-live][contains(@data-url,'.m3u8')]/@data-url"),
        )

        return schema.validate(root)

    @staticmethod
    def _get_content_id(root):
        schema = validate.Schema(
            validate.any(
                validate.all(
                    validate.xml_xpath_string("""
                        .//div[@data-id][
                            @data-live
                            or @id='video-element'
                            or @id='player-container'
                            or contains(@class, 'player-container')
                        ][1]/@data-id
                    """),
                    str,
                ),
                # xpath query needs to have a lower priority
                validate.all(
                    validate.xml_xpath_string(
                        ".//body[@data-content-id][1]/@data-content-id",
                    ),
                    str,
                ),
            ),
        )

        return schema.validate(root)

    def _api_query_new(self, content_id, api_url):
        url = urljoin(self.url, api_url.format(id=content_id))
        data = self.session.http.get(
            url,
            schema=validate.Schema(
                validate.parse_json(),
                validate.any(
                    validate.all(
                        str,
                        validate.parse_json(),
                        {"Error": str},
                        validate.get("Error"),
                    ),
                    validate.all(
                        {
                            "Media": {
                                "Link": {
                                    "ContentId": str,
                                    validate.optional("DefaultServiceUrl"): validate.any(validate.url(), ""),
                                    validate.optional("ServiceUrl"): validate.any(validate.url(), ""),
                                    "SecurePath": str,
                                },
                            },
                        },
                        validate.get(("Media", "Link")),
                        validate.union_get("ServiceUrl", "DefaultServiceUrl", "SecurePath", "ContentId"),
                    ),
                ),
            ),
        )
        if isinstance(data, str):
            log.error(data)
            return

        service_url, default_service_url, secure_path, content_id = data

        if default_service_url == "https://www.kanald.com.tr":
            self.url = default_service_url
            return self._api_query_old(content_id)

        if re.match(r"^https?://", secure_path):
            return secure_path

        return urljoin(service_url or default_service_url, secure_path)

    def _api_query_old(self, content_id):
        url = urljoin(self.url, self.API_URL_OLD.format(id=content_id))
        service_url, default_service_url, secure_path = self.session.http.get(
            url,
            schema=validate.Schema(
                validate.parse_json(),
                {
                    "data": {
                        "id": str,
                        "media": {
                            "link": {
                                validate.optional("defaultServiceUrl"): validate.any(validate.url(), ""),
                                validate.optional("serviceUrl"): validate.any(validate.url(), ""),
                                "securePath": str,
                            },
                        },
                    },
                },
                validate.get(("data", "media", "link")),
                validate.union_get("serviceUrl", "defaultServiceUrl", "securePath"),
            ),
        )

        return urljoin(service_url or default_service_url, secure_path)

    def _query_hls_url(self, content_id):
        for idx, match in enumerate(self.matches[: len(self.API_URLS)]):
            if match:
                return self._api_query_new(content_id, self.API_URLS[idx])

        return self._api_query_old(content_id)

    def _get_streams(self):
        root = self.session.http.get(self.url, schema=validate.Schema(validate.parse_html()))

        hls_url = self._get_hls_url(root)
        if not hls_url:
            try:
                content_id = self._get_content_id(root)
            except PluginError:
                log.error("Could not find the content ID for this stream")
                return

            log.debug(f"Loading content: {content_id}")
            hls_url = self._query_hls_url(content_id)

        if hls_url:
            return HLSStream.parse_variant_playlist(self.session, hls_url)


__plugin__ = Dogan

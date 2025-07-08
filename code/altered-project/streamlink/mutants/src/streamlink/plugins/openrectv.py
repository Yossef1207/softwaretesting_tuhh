"""
$description Japanese live-streaming and video hosting social platform.
$url openrec.tv
$type live, vod
"""

import logging
import re

from streamlink.plugin import Plugin, pluginargument, pluginmatcher
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
    re.compile(r"https?://(?:www\.)?openrec\.tv/(?:live|movie)/(?P<id>[^/]+)"),
)
@pluginargument(
    "email",
    requires=["password"],
    metavar="EMAIL",
    help="The email associated with your openrectv account, required to access any openrectv stream.",
)
@pluginargument(
    "password",
    sensitive=True,
    metavar="PASSWORD",
    help="An openrectv account password to use with --openrectv-email.",
)
class OPENRECtv(Plugin):
    _stores_re = re.compile(r"window.stores\s*=\s*({.*?});", re.DOTALL | re.MULTILINE)
    _config_re = re.compile(r"window.sharedConfig\s*=\s*({.*?});", re.DOTALL | re.MULTILINE)

    movie_info_url = "https://public.openrec.tv/external/api/v5/movies/{id}"
    subscription_info_url = "https://apiv5.openrec.tv/api/v5/movies/{id}/detail"
    login_url = "https://www.openrec.tv/viewapp/v4/mobile/user/login"

    _info_schema = validate.Schema({
        validate.optional("id"): str,
        validate.optional("title"): str,
        validate.optional("movie_type"): str,
        validate.optional("onair_status"): validate.any(None, int),
        validate.optional("public_type"): str,
        validate.optional("media"): {
            "url": validate.any(None, validate.url()),
            "url_public": validate.any(None, validate.url()),
            "url_ull": validate.any(None, validate.url()),
        },
        validate.optional("subs_trial_media"): {
            "url": validate.any(None, validate.url()),
            "url_ull": validate.any(None, validate.url()),
        },
    })

    _subscription_schema = validate.Schema({
        validate.optional("status"): int,
        validate.optional("data"): {
            "items": [
                {
                    "media": {
                        "url": validate.any(None, validate.url()),
                    },
                },
            ],
        },
    })

    _login_schema = validate.Schema({
        validate.optional("error_message"): str,
        "status": int,
        validate.optional("data"): object,
    })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_id = None

    def login(self, email, password):
        res = self.session.http.post(self.login_url, data={"mail": email, "password": password})
        data = self.session.http.json(res, self._login_schema)
        if data["status"] == 0:
            log.debug("Logged in as {0}".format(data["data"]["user_name"]))
        else:
            log.error("Failed to login: {0}".format(data["error_message"]))
        return data["status"] == 0

    def _get_movie_data(self):
        url = self.movie_info_url.format(id=self.video_id)
        res = self.session.http.get(
            url,
            headers={
                "access-token": self.session.http.cookies.get("access_token"),
                "uuid": self.session.http.cookies.get("uuid"),
            },
        )
        data = self.session.http.json(res, schema=self._info_schema)

        if data["id"]:
            log.debug("Got valid detail response")
            return data
        else:
            log.error("Failed to get video stream: {0}".format(data["message"]))

    def _get_subscription_movie_data(self):
        url = self.subscription_info_url.format(id=self.video_id)
        res = self.session.http.get(
            url,
            headers={
                "access-token": self.session.http.cookies.get("access_token"),
                "uuid": self.session.http.cookies.get("uuid"),
            },
        )
        data = self.session.http.json(res, schema=self._subscription_schema)

        if data["status"] == 0:
            log.debug("Got valid subscription info")
            return data
        else:
            log.error("Failed to get video stream: {0}".format(data["message"]))

    def get_author(self):
        mdata = self._get_movie_data()
        if mdata:
            return mdata["channel"]["name"]

    def get_title(self):
        mdata = self._get_movie_data()
        if mdata:
            return mdata["title"]

    def _get_streams(self):
        self.video_id = self.url.rsplit("/", 1)[-1]
        if self.get_option("email") and self.get_option("password"):
            self.login(self.get_option("email"), self.get_option("password"))
        mdata = self._get_movie_data()

        if mdata:
            log.debug("Found video: {0} ({1})".format(mdata["title"], mdata["id"]))
            m3u8_file = None
            # subscription
            if mdata["public_type"] == "member":
                subs_data = self._get_subscription_movie_data()
                m3u8_file = subs_data["data"]["items"][0]["media"]["url"]
            # streaming
            elif mdata["onair_status"] == 1:
                m3u8_file = mdata["media"]["url_ull"] or mdata["subs_trial_media"]["url_ull"]
            # archive
            elif mdata["onair_status"] == 2 and mdata["media"]["url_public"] is not None:
                m3u8_file = mdata["media"]["url_public"].replace("public.m3u8", "playlist.m3u8")
            # uploaded video
            elif mdata["onair_status"] is None and mdata["movie_type"] == "2":
                m3u8_file = mdata["media"]["url"]
            else:
                log.error("There is no video file.")

            if m3u8_file is not None:
                yield from HLSStream.parse_variant_playlist(
                    self.session,
                    m3u8_file,
                    headers={"Referer": self.url},
                ).items()

        else:
            log.error("You don't have the authority or no video file.")


__plugin__ = OPENRECtv

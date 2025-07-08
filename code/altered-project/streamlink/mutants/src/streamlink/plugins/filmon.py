"""
$description Live local TV channels and video on-demand service. OTT service from FilmOn.
$url filmon.com
$type live, vod
$notes Some VODs are mp4 which may not stream, use -o to download
"""

from __future__ import annotations

import logging
import re
import time
from collections.abc import Iterator
from urllib.parse import urlparse, urlunparse

from streamlink.exceptions import PluginError, StreamError
from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.session.http import TLSSecLevel1Adapter
from streamlink.stream.hls import HLSStream, HLSStreamReader, HLSStreamWorker
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


class FilmOnHLSStreamWorker(HLSStreamWorker):
    def xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_orig(self):
        try:
            return super()._fetch_playlist()
        except StreamError as err:
            # noinspection PyUnresolvedReferences
            if err.err.response.status_code in (403, 502):
                self.stream.watch_timeout = 0
                self.playlist_reload_time = 0
                log.debug(f"Force-reloading the channel playlist on error: {err}")
            raise err
    def xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_1(self):
        try:
            return super()._fetch_playlist()
        except StreamError as err:
            # noinspection PyUnresolvedReferences
            if err.err.response.status_code not in (403, 502):
                self.stream.watch_timeout = 0
                self.playlist_reload_time = 0
                log.debug(f"Force-reloading the channel playlist on error: {err}")
            raise err
    def xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_2(self):
        try:
            return super()._fetch_playlist()
        except StreamError as err:
            # noinspection PyUnresolvedReferences
            if err.err.response.status_code in (404, 502):
                self.stream.watch_timeout = 0
                self.playlist_reload_time = 0
                log.debug(f"Force-reloading the channel playlist on error: {err}")
            raise err
    def xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_3(self):
        try:
            return super()._fetch_playlist()
        except StreamError as err:
            # noinspection PyUnresolvedReferences
            if err.err.response.status_code in (403, 503):
                self.stream.watch_timeout = 0
                self.playlist_reload_time = 0
                log.debug(f"Force-reloading the channel playlist on error: {err}")
            raise err
    def xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_4(self):
        try:
            return super()._fetch_playlist()
        except StreamError as err:
            # noinspection PyUnresolvedReferences
            if err.err.response.status_code in (403, 502):
                self.stream.watch_timeout = None
                self.playlist_reload_time = 0
                log.debug(f"Force-reloading the channel playlist on error: {err}")
            raise err
    def xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_5(self):
        try:
            return super()._fetch_playlist()
        except StreamError as err:
            # noinspection PyUnresolvedReferences
            if err.err.response.status_code in (403, 502):
                self.stream.watch_timeout = 1
                self.playlist_reload_time = 0
                log.debug(f"Force-reloading the channel playlist on error: {err}")
            raise err
    def xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_6(self):
        try:
            return super()._fetch_playlist()
        except StreamError as err:
            # noinspection PyUnresolvedReferences
            if err.err.response.status_code in (403, 502):
                self.stream.watch_timeout = 0
                self.playlist_reload_time = None
                log.debug(f"Force-reloading the channel playlist on error: {err}")
            raise err
    def xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_7(self):
        try:
            return super()._fetch_playlist()
        except StreamError as err:
            # noinspection PyUnresolvedReferences
            if err.err.response.status_code in (403, 502):
                self.stream.watch_timeout = 0
                self.playlist_reload_time = 1
                log.debug(f"Force-reloading the channel playlist on error: {err}")
            raise err
    def xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_8(self):
        try:
            return super()._fetch_playlist()
        except StreamError as err:
            # noinspection PyUnresolvedReferences
            if err.err.response.status_code in (403, 502):
                self.stream.watch_timeout = 0
                self.playlist_reload_time = 0
                log.debug(None)
            raise err
    
    xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_1': xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_1, 
        'xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_2': xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_2, 
        'xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_3': xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_3, 
        'xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_4': xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_4, 
        'xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_5': xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_5, 
        'xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_6': xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_6, 
        'xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_7': xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_7, 
        'xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_8': xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_8
    }
    
    def _fetch_playlist(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_orig"), object.__getattribute__(self, "xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _fetch_playlist.__signature__ = _mutmut_signature(xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_orig)
    xǁFilmOnHLSStreamWorkerǁ_fetch_playlist__mutmut_orig.__name__ = 'xǁFilmOnHLSStreamWorkerǁ_fetch_playlist'


class FilmOnHLSStreamReader(HLSStreamReader):
    __worker__ = FilmOnHLSStreamWorker


class FilmOnHLS(HLSStream):
    __shortname__ = "hls-filmon"
    __reader__ = FilmOnHLSStreamReader

    def xǁFilmOnHLSǁ__init____mutmut_orig(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_1(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="XXhighXX", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_2(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="HIGH", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_3(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="High", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_4(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is not None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_5(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None or vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_6(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is not None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_7(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError(None)

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_8(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("XXChannel or vod_id must be setXX")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_9(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_10(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("CHANNEL OR VOD_ID MUST BE SET")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_11(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(None, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_12(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, None, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_13(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_14(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_15(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, )
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_16(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = None
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_17(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = None
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_18(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = None
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_19(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = None
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_20(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = None
        self.watch_timeout = 0.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_21(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = None
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_22(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 1.0
        self._first_netloc = ""

    def xǁFilmOnHLSǁ__init____mutmut_23(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = None

    def xǁFilmOnHLSǁ__init____mutmut_24(self, session, url: str, api: "FilmOnAPI", channel=None, vod_id=None, quality="high", **args):
        if channel is None and vod_id is None:
            raise PluginError("Channel or vod_id must be set")

        super().__init__(session, url, **args)
        self.api = api
        self.channel = channel
        self.vod_id = vod_id
        self.quality = quality
        self._url = url
        self.watch_timeout = 0.0
        self._first_netloc = "XXXX"
    
    xǁFilmOnHLSǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFilmOnHLSǁ__init____mutmut_1': xǁFilmOnHLSǁ__init____mutmut_1, 
        'xǁFilmOnHLSǁ__init____mutmut_2': xǁFilmOnHLSǁ__init____mutmut_2, 
        'xǁFilmOnHLSǁ__init____mutmut_3': xǁFilmOnHLSǁ__init____mutmut_3, 
        'xǁFilmOnHLSǁ__init____mutmut_4': xǁFilmOnHLSǁ__init____mutmut_4, 
        'xǁFilmOnHLSǁ__init____mutmut_5': xǁFilmOnHLSǁ__init____mutmut_5, 
        'xǁFilmOnHLSǁ__init____mutmut_6': xǁFilmOnHLSǁ__init____mutmut_6, 
        'xǁFilmOnHLSǁ__init____mutmut_7': xǁFilmOnHLSǁ__init____mutmut_7, 
        'xǁFilmOnHLSǁ__init____mutmut_8': xǁFilmOnHLSǁ__init____mutmut_8, 
        'xǁFilmOnHLSǁ__init____mutmut_9': xǁFilmOnHLSǁ__init____mutmut_9, 
        'xǁFilmOnHLSǁ__init____mutmut_10': xǁFilmOnHLSǁ__init____mutmut_10, 
        'xǁFilmOnHLSǁ__init____mutmut_11': xǁFilmOnHLSǁ__init____mutmut_11, 
        'xǁFilmOnHLSǁ__init____mutmut_12': xǁFilmOnHLSǁ__init____mutmut_12, 
        'xǁFilmOnHLSǁ__init____mutmut_13': xǁFilmOnHLSǁ__init____mutmut_13, 
        'xǁFilmOnHLSǁ__init____mutmut_14': xǁFilmOnHLSǁ__init____mutmut_14, 
        'xǁFilmOnHLSǁ__init____mutmut_15': xǁFilmOnHLSǁ__init____mutmut_15, 
        'xǁFilmOnHLSǁ__init____mutmut_16': xǁFilmOnHLSǁ__init____mutmut_16, 
        'xǁFilmOnHLSǁ__init____mutmut_17': xǁFilmOnHLSǁ__init____mutmut_17, 
        'xǁFilmOnHLSǁ__init____mutmut_18': xǁFilmOnHLSǁ__init____mutmut_18, 
        'xǁFilmOnHLSǁ__init____mutmut_19': xǁFilmOnHLSǁ__init____mutmut_19, 
        'xǁFilmOnHLSǁ__init____mutmut_20': xǁFilmOnHLSǁ__init____mutmut_20, 
        'xǁFilmOnHLSǁ__init____mutmut_21': xǁFilmOnHLSǁ__init____mutmut_21, 
        'xǁFilmOnHLSǁ__init____mutmut_22': xǁFilmOnHLSǁ__init____mutmut_22, 
        'xǁFilmOnHLSǁ__init____mutmut_23': xǁFilmOnHLSǁ__init____mutmut_23, 
        'xǁFilmOnHLSǁ__init____mutmut_24': xǁFilmOnHLSǁ__init____mutmut_24
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmOnHLSǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁFilmOnHLSǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁFilmOnHLSǁ__init____mutmut_orig)
    xǁFilmOnHLSǁ__init____mutmut_orig.__name__ = 'xǁFilmOnHLSǁ__init__'

    def xǁFilmOnHLSǁ_get_stream_data__mutmut_orig(self) -> Iterator[tuple[str, str, int]]:
        if self.channel:
            log.debug(f"Reloading FilmOn channel playlist: {self.channel}")
            yield from self.api.channel(self.channel)
        elif self.vod_id:
            log.debug(f"Reloading FilmOn VOD playlist: {self.vod_id}")
            yield from self.api.vod(self.vod_id)

    def xǁFilmOnHLSǁ_get_stream_data__mutmut_1(self) -> Iterator[tuple[str, str, int]]:
        if self.channel:
            log.debug(None)
            yield from self.api.channel(self.channel)
        elif self.vod_id:
            log.debug(f"Reloading FilmOn VOD playlist: {self.vod_id}")
            yield from self.api.vod(self.vod_id)

    def xǁFilmOnHLSǁ_get_stream_data__mutmut_2(self) -> Iterator[tuple[str, str, int]]:
        if self.channel:
            log.debug(f"Reloading FilmOn channel playlist: {self.channel}")
            yield from self.api.channel(None)
        elif self.vod_id:
            log.debug(f"Reloading FilmOn VOD playlist: {self.vod_id}")
            yield from self.api.vod(self.vod_id)

    def xǁFilmOnHLSǁ_get_stream_data__mutmut_3(self) -> Iterator[tuple[str, str, int]]:
        if self.channel:
            log.debug(f"Reloading FilmOn channel playlist: {self.channel}")
            yield from self.api.channel(self.channel)
        elif self.vod_id:
            log.debug(None)
            yield from self.api.vod(self.vod_id)

    def xǁFilmOnHLSǁ_get_stream_data__mutmut_4(self) -> Iterator[tuple[str, str, int]]:
        if self.channel:
            log.debug(f"Reloading FilmOn channel playlist: {self.channel}")
            yield from self.api.channel(self.channel)
        elif self.vod_id:
            log.debug(f"Reloading FilmOn VOD playlist: {self.vod_id}")
            yield from self.api.vod(None)
    
    xǁFilmOnHLSǁ_get_stream_data__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFilmOnHLSǁ_get_stream_data__mutmut_1': xǁFilmOnHLSǁ_get_stream_data__mutmut_1, 
        'xǁFilmOnHLSǁ_get_stream_data__mutmut_2': xǁFilmOnHLSǁ_get_stream_data__mutmut_2, 
        'xǁFilmOnHLSǁ_get_stream_data__mutmut_3': xǁFilmOnHLSǁ_get_stream_data__mutmut_3, 
        'xǁFilmOnHLSǁ_get_stream_data__mutmut_4': xǁFilmOnHLSǁ_get_stream_data__mutmut_4
    }
    
    def _get_stream_data(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁFilmOnHLSǁ_get_stream_data__mutmut_orig"), object.__getattribute__(self, "xǁFilmOnHLSǁ_get_stream_data__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_stream_data.__signature__ = _mutmut_signature(xǁFilmOnHLSǁ_get_stream_data__mutmut_orig)
    xǁFilmOnHLSǁ_get_stream_data__mutmut_orig.__name__ = 'xǁFilmOnHLSǁ_get_stream_data'

    @property
    def url(self) -> str:
        if time.time() <= self.watch_timeout:
            return self._url

        # If the watch timeout has passed then refresh the playlist from the API
        for quality, url, timeout in self._get_stream_data():
            if quality == self.quality:
                self.watch_timeout = time.time() + timeout

                if not self.channel:
                    self._url = url
                else:
                    parsed = urlparse(url)
                    if not self._first_netloc:
                        # save the first netloc
                        self._first_netloc = parsed.netloc
                    # always use the first saved netloc
                    self._url = parsed._replace(netloc=self._first_netloc).geturl()

                return self._url

        raise TypeError("Stream has expired and cannot be translated to a URL")


class FilmOnAPI:
    channel_url = "https://www.filmon.com/ajax/getChannelInfo"
    vod_url = "https://vms-admin.filmon.com/api/video/movie?id={0}"

    ATTEMPTS = 5
    TIMEOUT = 0.75

    stream_schema = validate.all(
        {
            "quality": str,
            "url": validate.url(),
            "watch-timeout": int,
        },
        validate.union_get("quality", "url", "watch-timeout"),
    )

    def xǁFilmOnAPIǁ__init____mutmut_orig(self, session):
        self.session = session

    def xǁFilmOnAPIǁ__init____mutmut_1(self, session):
        self.session = None
    
    xǁFilmOnAPIǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFilmOnAPIǁ__init____mutmut_1': xǁFilmOnAPIǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmOnAPIǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁFilmOnAPIǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁFilmOnAPIǁ__init____mutmut_orig)
    xǁFilmOnAPIǁ__init____mutmut_orig.__name__ = 'xǁFilmOnAPIǁ__init__'

    def xǁFilmOnAPIǁchannel__mutmut_orig(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_1(self, channel) -> list[tuple[str, str, int]]:
        num = None
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_2(self, channel) -> list[tuple[str, str, int]]:
        num = 2
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_3(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while False:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_4(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    None,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_5(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data=None,
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_6(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers=None,
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_7(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=None,
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_8(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_9(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_10(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_11(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_12(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "XXchannel_idXX": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_13(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "CHANNEL_ID": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_14(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "Channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_15(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "XXqualityXX": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_16(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "QUALITY": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_17(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "Quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_18(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "XXlowXX",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_19(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "LOW",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_20(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "Low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_21(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"XXX-Requested-WithXX": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_22(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"x-requested-with": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_23(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-REQUESTED-WITH": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_24(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-requested-with": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_25(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XXXMLHttpRequestXX"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_26(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "xmlhttprequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_27(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHTTPREQUEST"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_28(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "Xmlhttprequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_29(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        None,
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_30(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        None,
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_31(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        None,
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_32(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_33(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_34(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_35(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"XXstreamsXX": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_36(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"STREAMS": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_37(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"Streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_38(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get(None),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_39(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("XXstreamsXX"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_40(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("STREAMS"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_41(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("Streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_42(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(None)
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_43(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num > self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_44(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = None
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_45(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num - 1
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_46(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 2
                time.sleep(self.TIMEOUT)

    def xǁFilmOnAPIǁchannel__mutmut_47(self, channel) -> list[tuple[str, str, int]]:
        num = 1
        while True:
            # retry for 50X errors or validation errors at the same time
            try:
                return self.session.http.post(
                    self.channel_url,
                    data={
                        "channel_id": channel,
                        "quality": "low",
                    },
                    headers={"X-Requested-With": "XMLHttpRequest"},
                    schema=validate.Schema(
                        validate.parse_json(),
                        {"streams": [self.stream_schema]},
                        validate.get("streams"),
                    ),
                )
            except PluginError:
                log.debug(f"Received invalid or non-JSON data, attempt {num}/{self.ATTEMPTS}")
                if num >= self.ATTEMPTS:
                    raise
                num = num + 1
                time.sleep(None)
    
    xǁFilmOnAPIǁchannel__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFilmOnAPIǁchannel__mutmut_1': xǁFilmOnAPIǁchannel__mutmut_1, 
        'xǁFilmOnAPIǁchannel__mutmut_2': xǁFilmOnAPIǁchannel__mutmut_2, 
        'xǁFilmOnAPIǁchannel__mutmut_3': xǁFilmOnAPIǁchannel__mutmut_3, 
        'xǁFilmOnAPIǁchannel__mutmut_4': xǁFilmOnAPIǁchannel__mutmut_4, 
        'xǁFilmOnAPIǁchannel__mutmut_5': xǁFilmOnAPIǁchannel__mutmut_5, 
        'xǁFilmOnAPIǁchannel__mutmut_6': xǁFilmOnAPIǁchannel__mutmut_6, 
        'xǁFilmOnAPIǁchannel__mutmut_7': xǁFilmOnAPIǁchannel__mutmut_7, 
        'xǁFilmOnAPIǁchannel__mutmut_8': xǁFilmOnAPIǁchannel__mutmut_8, 
        'xǁFilmOnAPIǁchannel__mutmut_9': xǁFilmOnAPIǁchannel__mutmut_9, 
        'xǁFilmOnAPIǁchannel__mutmut_10': xǁFilmOnAPIǁchannel__mutmut_10, 
        'xǁFilmOnAPIǁchannel__mutmut_11': xǁFilmOnAPIǁchannel__mutmut_11, 
        'xǁFilmOnAPIǁchannel__mutmut_12': xǁFilmOnAPIǁchannel__mutmut_12, 
        'xǁFilmOnAPIǁchannel__mutmut_13': xǁFilmOnAPIǁchannel__mutmut_13, 
        'xǁFilmOnAPIǁchannel__mutmut_14': xǁFilmOnAPIǁchannel__mutmut_14, 
        'xǁFilmOnAPIǁchannel__mutmut_15': xǁFilmOnAPIǁchannel__mutmut_15, 
        'xǁFilmOnAPIǁchannel__mutmut_16': xǁFilmOnAPIǁchannel__mutmut_16, 
        'xǁFilmOnAPIǁchannel__mutmut_17': xǁFilmOnAPIǁchannel__mutmut_17, 
        'xǁFilmOnAPIǁchannel__mutmut_18': xǁFilmOnAPIǁchannel__mutmut_18, 
        'xǁFilmOnAPIǁchannel__mutmut_19': xǁFilmOnAPIǁchannel__mutmut_19, 
        'xǁFilmOnAPIǁchannel__mutmut_20': xǁFilmOnAPIǁchannel__mutmut_20, 
        'xǁFilmOnAPIǁchannel__mutmut_21': xǁFilmOnAPIǁchannel__mutmut_21, 
        'xǁFilmOnAPIǁchannel__mutmut_22': xǁFilmOnAPIǁchannel__mutmut_22, 
        'xǁFilmOnAPIǁchannel__mutmut_23': xǁFilmOnAPIǁchannel__mutmut_23, 
        'xǁFilmOnAPIǁchannel__mutmut_24': xǁFilmOnAPIǁchannel__mutmut_24, 
        'xǁFilmOnAPIǁchannel__mutmut_25': xǁFilmOnAPIǁchannel__mutmut_25, 
        'xǁFilmOnAPIǁchannel__mutmut_26': xǁFilmOnAPIǁchannel__mutmut_26, 
        'xǁFilmOnAPIǁchannel__mutmut_27': xǁFilmOnAPIǁchannel__mutmut_27, 
        'xǁFilmOnAPIǁchannel__mutmut_28': xǁFilmOnAPIǁchannel__mutmut_28, 
        'xǁFilmOnAPIǁchannel__mutmut_29': xǁFilmOnAPIǁchannel__mutmut_29, 
        'xǁFilmOnAPIǁchannel__mutmut_30': xǁFilmOnAPIǁchannel__mutmut_30, 
        'xǁFilmOnAPIǁchannel__mutmut_31': xǁFilmOnAPIǁchannel__mutmut_31, 
        'xǁFilmOnAPIǁchannel__mutmut_32': xǁFilmOnAPIǁchannel__mutmut_32, 
        'xǁFilmOnAPIǁchannel__mutmut_33': xǁFilmOnAPIǁchannel__mutmut_33, 
        'xǁFilmOnAPIǁchannel__mutmut_34': xǁFilmOnAPIǁchannel__mutmut_34, 
        'xǁFilmOnAPIǁchannel__mutmut_35': xǁFilmOnAPIǁchannel__mutmut_35, 
        'xǁFilmOnAPIǁchannel__mutmut_36': xǁFilmOnAPIǁchannel__mutmut_36, 
        'xǁFilmOnAPIǁchannel__mutmut_37': xǁFilmOnAPIǁchannel__mutmut_37, 
        'xǁFilmOnAPIǁchannel__mutmut_38': xǁFilmOnAPIǁchannel__mutmut_38, 
        'xǁFilmOnAPIǁchannel__mutmut_39': xǁFilmOnAPIǁchannel__mutmut_39, 
        'xǁFilmOnAPIǁchannel__mutmut_40': xǁFilmOnAPIǁchannel__mutmut_40, 
        'xǁFilmOnAPIǁchannel__mutmut_41': xǁFilmOnAPIǁchannel__mutmut_41, 
        'xǁFilmOnAPIǁchannel__mutmut_42': xǁFilmOnAPIǁchannel__mutmut_42, 
        'xǁFilmOnAPIǁchannel__mutmut_43': xǁFilmOnAPIǁchannel__mutmut_43, 
        'xǁFilmOnAPIǁchannel__mutmut_44': xǁFilmOnAPIǁchannel__mutmut_44, 
        'xǁFilmOnAPIǁchannel__mutmut_45': xǁFilmOnAPIǁchannel__mutmut_45, 
        'xǁFilmOnAPIǁchannel__mutmut_46': xǁFilmOnAPIǁchannel__mutmut_46, 
        'xǁFilmOnAPIǁchannel__mutmut_47': xǁFilmOnAPIǁchannel__mutmut_47
    }
    
    def channel(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmOnAPIǁchannel__mutmut_orig"), object.__getattribute__(self, "xǁFilmOnAPIǁchannel__mutmut_mutants"), args, kwargs, self)
        return result 
    
    channel.__signature__ = _mutmut_signature(xǁFilmOnAPIǁchannel__mutmut_orig)
    xǁFilmOnAPIǁchannel__mutmut_orig.__name__ = 'xǁFilmOnAPIǁchannel'

    def xǁFilmOnAPIǁvod__mutmut_orig(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_1(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            None,
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_2(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=None,
        )

    def xǁFilmOnAPIǁvod__mutmut_3(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_4(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            )

    def xǁFilmOnAPIǁvod__mutmut_5(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(None),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_6(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                None,
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_7(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                None,
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_8(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                None,
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_9(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                None,
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_10(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_11(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_12(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_13(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                ),
        )

    def xǁFilmOnAPIǁvod__mutmut_14(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"XXresponseXX": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_15(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"RESPONSE": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_16(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"Response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_17(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"XXstreamsXX": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_18(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"STREAMS": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_19(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"Streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_20(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(None),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_21(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("XXresponseXX", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_22(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("RESPONSE", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_23(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("Response", "streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_24(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "XXstreamsXX")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_25(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "STREAMS")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_26(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "Streams")),
                validate.transform(lambda d: d.values()),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_27(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(None),
            ),
        )

    def xǁFilmOnAPIǁvod__mutmut_28(self, vod_id) -> list[tuple[str, str, int]]:
        return self.session.http.get(
            self.vod_url.format(vod_id),
            schema=validate.Schema(
                validate.parse_json(),
                {"response": {"streams": {str: self.stream_schema}}},
                validate.get(("response", "streams")),
                validate.transform(lambda d: None),
            ),
        )
    
    xǁFilmOnAPIǁvod__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFilmOnAPIǁvod__mutmut_1': xǁFilmOnAPIǁvod__mutmut_1, 
        'xǁFilmOnAPIǁvod__mutmut_2': xǁFilmOnAPIǁvod__mutmut_2, 
        'xǁFilmOnAPIǁvod__mutmut_3': xǁFilmOnAPIǁvod__mutmut_3, 
        'xǁFilmOnAPIǁvod__mutmut_4': xǁFilmOnAPIǁvod__mutmut_4, 
        'xǁFilmOnAPIǁvod__mutmut_5': xǁFilmOnAPIǁvod__mutmut_5, 
        'xǁFilmOnAPIǁvod__mutmut_6': xǁFilmOnAPIǁvod__mutmut_6, 
        'xǁFilmOnAPIǁvod__mutmut_7': xǁFilmOnAPIǁvod__mutmut_7, 
        'xǁFilmOnAPIǁvod__mutmut_8': xǁFilmOnAPIǁvod__mutmut_8, 
        'xǁFilmOnAPIǁvod__mutmut_9': xǁFilmOnAPIǁvod__mutmut_9, 
        'xǁFilmOnAPIǁvod__mutmut_10': xǁFilmOnAPIǁvod__mutmut_10, 
        'xǁFilmOnAPIǁvod__mutmut_11': xǁFilmOnAPIǁvod__mutmut_11, 
        'xǁFilmOnAPIǁvod__mutmut_12': xǁFilmOnAPIǁvod__mutmut_12, 
        'xǁFilmOnAPIǁvod__mutmut_13': xǁFilmOnAPIǁvod__mutmut_13, 
        'xǁFilmOnAPIǁvod__mutmut_14': xǁFilmOnAPIǁvod__mutmut_14, 
        'xǁFilmOnAPIǁvod__mutmut_15': xǁFilmOnAPIǁvod__mutmut_15, 
        'xǁFilmOnAPIǁvod__mutmut_16': xǁFilmOnAPIǁvod__mutmut_16, 
        'xǁFilmOnAPIǁvod__mutmut_17': xǁFilmOnAPIǁvod__mutmut_17, 
        'xǁFilmOnAPIǁvod__mutmut_18': xǁFilmOnAPIǁvod__mutmut_18, 
        'xǁFilmOnAPIǁvod__mutmut_19': xǁFilmOnAPIǁvod__mutmut_19, 
        'xǁFilmOnAPIǁvod__mutmut_20': xǁFilmOnAPIǁvod__mutmut_20, 
        'xǁFilmOnAPIǁvod__mutmut_21': xǁFilmOnAPIǁvod__mutmut_21, 
        'xǁFilmOnAPIǁvod__mutmut_22': xǁFilmOnAPIǁvod__mutmut_22, 
        'xǁFilmOnAPIǁvod__mutmut_23': xǁFilmOnAPIǁvod__mutmut_23, 
        'xǁFilmOnAPIǁvod__mutmut_24': xǁFilmOnAPIǁvod__mutmut_24, 
        'xǁFilmOnAPIǁvod__mutmut_25': xǁFilmOnAPIǁvod__mutmut_25, 
        'xǁFilmOnAPIǁvod__mutmut_26': xǁFilmOnAPIǁvod__mutmut_26, 
        'xǁFilmOnAPIǁvod__mutmut_27': xǁFilmOnAPIǁvod__mutmut_27, 
        'xǁFilmOnAPIǁvod__mutmut_28': xǁFilmOnAPIǁvod__mutmut_28
    }
    
    def vod(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmOnAPIǁvod__mutmut_orig"), object.__getattribute__(self, "xǁFilmOnAPIǁvod__mutmut_mutants"), args, kwargs, self)
        return result 
    
    vod.__signature__ = _mutmut_signature(xǁFilmOnAPIǁvod__mutmut_orig)
    xǁFilmOnAPIǁvod__mutmut_orig.__name__ = 'xǁFilmOnAPIǁvod'


@pluginmatcher(
    re.compile(
        r"""
            https?://(?:www\.)?filmon\.(?:tv|com)/
            (?:
                (?:
                    index/popout\?
                    |
                    (?:tv/)?channel/(?:export\?)?
                    |
                    tv/(?!channel/)
                    |
                    channel/
                    |
                    (?P<is_group>group/)
                )(?:channel_id=)?(?P<channel>[-_\w]+)
                |
                vod/view/(?P<vod_id>[^/?&]+)
            )
        """,
        re.VERBOSE,
    ),
)
class Filmon(Plugin):
    quality_weights = {
        "high": 720,
        "low": 480,
    }

    TIME_CHANNEL = 60 * 60 * 24 * 365

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parsed = urlparse(self.url)
        if parsed.path.startswith("/channel/"):
            self.url = urlunparse(parsed._replace(path=parsed.path.replace("/channel/", "/tv/")))
        self.api = FilmOnAPI(self.session)

        adapter = TLSSecLevel1Adapter()
        self.session.http.mount("https://filmon.com", adapter)
        self.session.http.mount("https://www.filmon.com", adapter)
        self.session.http.mount("https://vms-admin.filmon.com/", adapter)

        self.session.options.set("hls-playlist-reload-time", "segment")

    @classmethod
    def stream_weight(cls, key):
        weight = cls.quality_weights.get(key)
        if weight:
            return weight, "filmon"

        return super().stream_weight(key)

    def _get_streams(self):
        channel = self.match.group("channel")
        vod_id = self.match.group("vod_id")
        is_group = self.match.group("is_group")

        # get cookies
        self.session.http.get(self.url)

        if vod_id:
            for quality, url, _timeout in self.api.vod(vod_id):
                if url.endswith(".m3u8"):
                    streams = HLSStream.parse_variant_playlist(self.session, url)
                    if streams:
                        yield from streams.items()
                        return
                    yield quality, HLSStream(self.session, url)
                elif url.endswith(".mp4"):
                    yield quality, HTTPStream(self.session, url)
        else:
            if not channel or channel.isdigit():
                id_ = channel
            else:
                id_ = self.cache.get(channel)
                if id_ is not None:
                    log.debug(f"Found cached channel ID: {id_}")
                else:
                    id_ = self.session.http.get(
                        self.url,
                        schema=validate.Schema(
                            re.compile(r"""channel_id\s*=\s*(?P<q>['"]?)(?P<value>\d+)(?P=q)"""),
                            validate.any(None, validate.get("value")),
                        ),
                    )
                    log.debug(f"Found channel ID: {id_}")
                    # do not cache a group url
                    if id_ and not is_group:
                        self.cache.set(channel, id_, expires=self.TIME_CHANNEL)

            if id_ is None:
                raise PluginError(f"Unable to find channel ID: {channel}")

            try:
                for quality, url, _timeout in self.api.channel(id_):
                    yield quality, FilmOnHLS(self.session, url, self.api, channel=id_, quality=quality)
            except Exception:
                if channel and not channel.isdigit():
                    self.cache.set(channel, None, expires=0)
                    log.debug(f"Reset cached channel: {channel}")
                raise


__plugin__ = Filmon

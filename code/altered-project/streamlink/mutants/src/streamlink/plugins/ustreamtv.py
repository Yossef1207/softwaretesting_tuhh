"""
$description Global live-streaming and video on-demand platform owned by IBM.
$url ustream.tv
$url video.ibm.com
$type live, vod
"""

from __future__ import annotations

import logging
import re
from collections import deque
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from random import randint
from threading import Event, RLock
from typing import Any
from urllib.parse import urljoin, urlunparse

from requests import Response

from streamlink.exceptions import PluginError, StreamError
from streamlink.plugin import Plugin, pluginargument, pluginmatcher
from streamlink.plugin.api import useragents, validate
from streamlink.plugin.api.websocket import WebsocketClient
from streamlink.stream.ffmpegmux import MuxedStream
from streamlink.stream.segmented import Segment, SegmentedStreamReader, SegmentedStreamWorker, SegmentedStreamWriter
from streamlink.stream.stream import Stream
from streamlink.utils.parse import parse_json


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


@dataclass
class _StreamFormat:
    contentType: str
    sourceStreamVersion: int
    initUrl: str
    segmentUrl: str
    bitrate: int


@dataclass
class StreamFormatVideo(_StreamFormat):
    height: int


@dataclass
class StreamFormatAudio(_StreamFormat):
    language: str = ""


@dataclass
class UStreamTVSegment(Segment):
    available_at: datetime
    hash: str
    path: str

    # the segment URLs depend on the CDN and the chosen stream format and its segment template string
    def url(self, base: str | None, template: str) -> str:
        return urljoin(
            base or "",
            f"{self.path}/{template.replace('%', str(self.num), 1).replace('%', self.hash, 1)}",
        )


class UStreamTVWsClient(WebsocketClient):
    API_URL = "wss://r{0}-1-{1}-{2}-ws-{3}.ums.services.video.ibm.com/1/ustream"
    APP_ID = 3
    APP_VERSION = 2

    STREAM_OPENED_TIMEOUT = 6

    _schema_cmd = validate.Schema({
        "cmd": str,
        "args": [{str: object}],
    })
    _schema_stream_formats = validate.Schema({
        "streams": [
            validate.any(
                validate.all(
                    {
                        "contentType": "video/mp4",
                        "sourceStreamVersion": int,
                        "initUrl": str,
                        "segmentUrl": str,
                        "bitrate": int,
                        "height": int,
                    },
                    validate.transform(lambda obj: StreamFormatVideo(**obj)),
                ),
                validate.all(
                    {
                        "contentType": "audio/mp4",
                        "sourceStreamVersion": int,
                        "initUrl": str,
                        "segmentUrl": str,
                        "bitrate": int,
                        validate.optional("language"): str,
                    },
                    validate.transform(lambda obj: StreamFormatAudio(**obj)),
                ),
                object,
            ),
        ],
    })
    _schema_stream_segments = validate.Schema({
        "chunkId": int,
        "chunkTime": int,
        "contentAccess": validate.all(
            {
                "accessList": [
                    {
                        "data": {
                            "path": str,
                        },
                    },
                ],
            },
            validate.get(("accessList", 0, "data", "path")),
        ),
        "hashes": {validate.transform(int): str},
    })

    stream_cdn: str | None = None
    stream_formats_video: list[StreamFormatVideo] | None = None
    stream_formats_audio: list[StreamFormatAudio] | None = None
    stream_initial_id: int | None = None

    def xǁUStreamTVWsClientǁ__init____mutmut_orig(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_1(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="XXliveXX",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_2(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="LIVE",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_3(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="Live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_4(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = None
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_5(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = None
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_6(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = ""
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_7(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = None
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_8(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = None
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_9(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = None

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_10(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = None
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_11(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = None
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_12(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = None
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_13(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = None
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_14(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = None
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_15(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = None
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_16(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = None

        super().__init__(session, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_17(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(None, self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_18(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, None, origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_19(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin=None)

    def xǁUStreamTVWsClientǁ__init____mutmut_20(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(self._get_url(), origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_21(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, origin="https://www.ustream.tv")

    def xǁUStreamTVWsClientǁ__init____mutmut_22(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), )

    def xǁUStreamTVWsClientǁ__init____mutmut_23(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="XXhttps://www.ustream.tvXX")

    def xǁUStreamTVWsClientǁ__init____mutmut_24(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="HTTPS://WWW.USTREAM.TV")

    def xǁUStreamTVWsClientǁ__init____mutmut_25(
        self,
        session,
        media_id,
        application,
        referrer=None,
        cluster="live",
        password=None,
        app_id=APP_ID,
        app_version=APP_VERSION,
    ) -> None:
        self.opened = Event()
        self.ready = Event()
        self.stream_error = None
        # a list of deques subscribed by worker threads which independently need to read segments
        self.stream_segments_subscribers: list[deque[UStreamTVSegment]] = []
        self.stream_segments_initial: deque[UStreamTVSegment] = deque()
        self.stream_segments_lock = RLock()

        self.media_id = media_id
        self.application = application
        self.referrer = referrer
        self.cluster = cluster
        self.password = password
        self.app_id = app_id
        self.app_version = app_version

        super().__init__(session, self._get_url(), origin="Https://www.ustream.tv")
    
    xǁUStreamTVWsClientǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ__init____mutmut_1': xǁUStreamTVWsClientǁ__init____mutmut_1, 
        'xǁUStreamTVWsClientǁ__init____mutmut_2': xǁUStreamTVWsClientǁ__init____mutmut_2, 
        'xǁUStreamTVWsClientǁ__init____mutmut_3': xǁUStreamTVWsClientǁ__init____mutmut_3, 
        'xǁUStreamTVWsClientǁ__init____mutmut_4': xǁUStreamTVWsClientǁ__init____mutmut_4, 
        'xǁUStreamTVWsClientǁ__init____mutmut_5': xǁUStreamTVWsClientǁ__init____mutmut_5, 
        'xǁUStreamTVWsClientǁ__init____mutmut_6': xǁUStreamTVWsClientǁ__init____mutmut_6, 
        'xǁUStreamTVWsClientǁ__init____mutmut_7': xǁUStreamTVWsClientǁ__init____mutmut_7, 
        'xǁUStreamTVWsClientǁ__init____mutmut_8': xǁUStreamTVWsClientǁ__init____mutmut_8, 
        'xǁUStreamTVWsClientǁ__init____mutmut_9': xǁUStreamTVWsClientǁ__init____mutmut_9, 
        'xǁUStreamTVWsClientǁ__init____mutmut_10': xǁUStreamTVWsClientǁ__init____mutmut_10, 
        'xǁUStreamTVWsClientǁ__init____mutmut_11': xǁUStreamTVWsClientǁ__init____mutmut_11, 
        'xǁUStreamTVWsClientǁ__init____mutmut_12': xǁUStreamTVWsClientǁ__init____mutmut_12, 
        'xǁUStreamTVWsClientǁ__init____mutmut_13': xǁUStreamTVWsClientǁ__init____mutmut_13, 
        'xǁUStreamTVWsClientǁ__init____mutmut_14': xǁUStreamTVWsClientǁ__init____mutmut_14, 
        'xǁUStreamTVWsClientǁ__init____mutmut_15': xǁUStreamTVWsClientǁ__init____mutmut_15, 
        'xǁUStreamTVWsClientǁ__init____mutmut_16': xǁUStreamTVWsClientǁ__init____mutmut_16, 
        'xǁUStreamTVWsClientǁ__init____mutmut_17': xǁUStreamTVWsClientǁ__init____mutmut_17, 
        'xǁUStreamTVWsClientǁ__init____mutmut_18': xǁUStreamTVWsClientǁ__init____mutmut_18, 
        'xǁUStreamTVWsClientǁ__init____mutmut_19': xǁUStreamTVWsClientǁ__init____mutmut_19, 
        'xǁUStreamTVWsClientǁ__init____mutmut_20': xǁUStreamTVWsClientǁ__init____mutmut_20, 
        'xǁUStreamTVWsClientǁ__init____mutmut_21': xǁUStreamTVWsClientǁ__init____mutmut_21, 
        'xǁUStreamTVWsClientǁ__init____mutmut_22': xǁUStreamTVWsClientǁ__init____mutmut_22, 
        'xǁUStreamTVWsClientǁ__init____mutmut_23': xǁUStreamTVWsClientǁ__init____mutmut_23, 
        'xǁUStreamTVWsClientǁ__init____mutmut_24': xǁUStreamTVWsClientǁ__init____mutmut_24, 
        'xǁUStreamTVWsClientǁ__init____mutmut_25': xǁUStreamTVWsClientǁ__init____mutmut_25
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ__init____mutmut_orig)
    xǁUStreamTVWsClientǁ__init____mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ__init__'

    def xǁUStreamTVWsClientǁ_get_url__mutmut_orig(self):
        return self.API_URL.format(randint(0, 0xFFFFFF), self.media_id, self.application, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_1(self):
        return self.API_URL.format(None, self.media_id, self.application, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_2(self):
        return self.API_URL.format(randint(0, 0xFFFFFF), None, self.application, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_3(self):
        return self.API_URL.format(randint(0, 0xFFFFFF), self.media_id, None, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_4(self):
        return self.API_URL.format(randint(0, 0xFFFFFF), self.media_id, self.application, None)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_5(self):
        return self.API_URL.format(self.media_id, self.application, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_6(self):
        return self.API_URL.format(randint(0, 0xFFFFFF), self.application, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_7(self):
        return self.API_URL.format(randint(0, 0xFFFFFF), self.media_id, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_8(self):
        return self.API_URL.format(randint(0, 0xFFFFFF), self.media_id, self.application, )

    def xǁUStreamTVWsClientǁ_get_url__mutmut_9(self):
        return self.API_URL.format(randint(None, 0xFFFFFF), self.media_id, self.application, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_10(self):
        return self.API_URL.format(randint(0, None), self.media_id, self.application, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_11(self):
        return self.API_URL.format(randint(0xFFFFFF), self.media_id, self.application, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_12(self):
        return self.API_URL.format(randint(0, ), self.media_id, self.application, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_13(self):
        return self.API_URL.format(randint(1, 0xFFFFFF), self.media_id, self.application, self.cluster)

    def xǁUStreamTVWsClientǁ_get_url__mutmut_14(self):
        return self.API_URL.format(randint(0, 16777216), self.media_id, self.application, self.cluster)
    
    xǁUStreamTVWsClientǁ_get_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_get_url__mutmut_1': xǁUStreamTVWsClientǁ_get_url__mutmut_1, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_2': xǁUStreamTVWsClientǁ_get_url__mutmut_2, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_3': xǁUStreamTVWsClientǁ_get_url__mutmut_3, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_4': xǁUStreamTVWsClientǁ_get_url__mutmut_4, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_5': xǁUStreamTVWsClientǁ_get_url__mutmut_5, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_6': xǁUStreamTVWsClientǁ_get_url__mutmut_6, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_7': xǁUStreamTVWsClientǁ_get_url__mutmut_7, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_8': xǁUStreamTVWsClientǁ_get_url__mutmut_8, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_9': xǁUStreamTVWsClientǁ_get_url__mutmut_9, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_10': xǁUStreamTVWsClientǁ_get_url__mutmut_10, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_11': xǁUStreamTVWsClientǁ_get_url__mutmut_11, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_12': xǁUStreamTVWsClientǁ_get_url__mutmut_12, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_13': xǁUStreamTVWsClientǁ_get_url__mutmut_13, 
        'xǁUStreamTVWsClientǁ_get_url__mutmut_14': xǁUStreamTVWsClientǁ_get_url__mutmut_14
    }
    
    def _get_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_get_url__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_get_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_url.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_get_url__mutmut_orig)
    xǁUStreamTVWsClientǁ_get_url__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_get_url'

    def xǁUStreamTVWsClientǁ_set_error__mutmut_orig(self, error: Any):
        self.stream_error = error
        self.ready.set()

    def xǁUStreamTVWsClientǁ_set_error__mutmut_1(self, error: Any):
        self.stream_error = None
        self.ready.set()
    
    xǁUStreamTVWsClientǁ_set_error__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_set_error__mutmut_1': xǁUStreamTVWsClientǁ_set_error__mutmut_1
    }
    
    def _set_error(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_set_error__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_set_error__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _set_error.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_set_error__mutmut_orig)
    xǁUStreamTVWsClientǁ_set_error__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_set_error'

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_orig(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("Stream opened, keeping websocket connection alive")
            else:
                log.info("Closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_1(self):
        if self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("Stream opened, keeping websocket connection alive")
            else:
                log.info("Closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_2(self):
        if not self.ready.is_set() or self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("Stream opened, keeping websocket connection alive")
            else:
                log.info("Closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_3(self):
        if not self.ready.is_set() and self.stream_cdn or self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("Stream opened, keeping websocket connection alive")
            else:
                log.info("Closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_4(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("Stream opened, keeping websocket connection alive")
            else:
                log.info("Closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_5(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(None):
                log.debug("Stream opened, keeping websocket connection alive")
            else:
                log.info("Closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_6(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug(None)
            else:
                log.info("Closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_7(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("XXStream opened, keeping websocket connection aliveXX")
            else:
                log.info("Closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_8(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("stream opened, keeping websocket connection alive")
            else:
                log.info("Closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_9(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("STREAM OPENED, KEEPING WEBSOCKET CONNECTION ALIVE")
            else:
                log.info("Closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_10(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("Stream opened, keeping websocket connection alive")
            else:
                log.info(None)
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_11(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("Stream opened, keeping websocket connection alive")
            else:
                log.info("XXClosing websocket connectionXX")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_12(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("Stream opened, keeping websocket connection alive")
            else:
                log.info("closing websocket connection")
                self.ws.close()

    def xǁUStreamTVWsClientǁ_set_ready__mutmut_13(self):
        if not self.ready.is_set() and self.stream_cdn and self.stream_initial_id is not None:
            self.ready.set()

            if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
                log.debug("Stream opened, keeping websocket connection alive")
            else:
                log.info("CLOSING WEBSOCKET CONNECTION")
                self.ws.close()
    
    xǁUStreamTVWsClientǁ_set_ready__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_set_ready__mutmut_1': xǁUStreamTVWsClientǁ_set_ready__mutmut_1, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_2': xǁUStreamTVWsClientǁ_set_ready__mutmut_2, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_3': xǁUStreamTVWsClientǁ_set_ready__mutmut_3, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_4': xǁUStreamTVWsClientǁ_set_ready__mutmut_4, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_5': xǁUStreamTVWsClientǁ_set_ready__mutmut_5, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_6': xǁUStreamTVWsClientǁ_set_ready__mutmut_6, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_7': xǁUStreamTVWsClientǁ_set_ready__mutmut_7, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_8': xǁUStreamTVWsClientǁ_set_ready__mutmut_8, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_9': xǁUStreamTVWsClientǁ_set_ready__mutmut_9, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_10': xǁUStreamTVWsClientǁ_set_ready__mutmut_10, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_11': xǁUStreamTVWsClientǁ_set_ready__mutmut_11, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_12': xǁUStreamTVWsClientǁ_set_ready__mutmut_12, 
        'xǁUStreamTVWsClientǁ_set_ready__mutmut_13': xǁUStreamTVWsClientǁ_set_ready__mutmut_13
    }
    
    def _set_ready(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_set_ready__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_set_ready__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _set_ready.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_set_ready__mutmut_orig)
    xǁUStreamTVWsClientǁ_set_ready__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_set_ready'

    def xǁUStreamTVWsClientǁsegments_subscribe__mutmut_orig(self) -> deque[UStreamTVSegment]:
        with self.stream_segments_lock:
            # copy the initial segments deque (segments arrive early)
            new_deque = self.stream_segments_initial.copy()
            self.stream_segments_subscribers.append(new_deque)

            return new_deque

    def xǁUStreamTVWsClientǁsegments_subscribe__mutmut_1(self) -> deque[UStreamTVSegment]:
        with self.stream_segments_lock:
            # copy the initial segments deque (segments arrive early)
            new_deque = None
            self.stream_segments_subscribers.append(new_deque)

            return new_deque

    def xǁUStreamTVWsClientǁsegments_subscribe__mutmut_2(self) -> deque[UStreamTVSegment]:
        with self.stream_segments_lock:
            # copy the initial segments deque (segments arrive early)
            new_deque = self.stream_segments_initial.copy()
            self.stream_segments_subscribers.append(None)

            return new_deque
    
    xǁUStreamTVWsClientǁsegments_subscribe__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁsegments_subscribe__mutmut_1': xǁUStreamTVWsClientǁsegments_subscribe__mutmut_1, 
        'xǁUStreamTVWsClientǁsegments_subscribe__mutmut_2': xǁUStreamTVWsClientǁsegments_subscribe__mutmut_2
    }
    
    def segments_subscribe(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁsegments_subscribe__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁsegments_subscribe__mutmut_mutants"), args, kwargs, self)
        return result 
    
    segments_subscribe.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁsegments_subscribe__mutmut_orig)
    xǁUStreamTVWsClientǁsegments_subscribe__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁsegments_subscribe'

    def xǁUStreamTVWsClientǁ_segments_append__mutmut_orig(self, segment: UStreamTVSegment):
        # if there are no subscribers yet, add segment(s) to the initial deque
        if not self.stream_segments_subscribers:
            self.stream_segments_initial.append(segment)
        else:
            for subscriber_deque in self.stream_segments_subscribers:
                subscriber_deque.append(segment)

    def xǁUStreamTVWsClientǁ_segments_append__mutmut_1(self, segment: UStreamTVSegment):
        # if there are no subscribers yet, add segment(s) to the initial deque
        if self.stream_segments_subscribers:
            self.stream_segments_initial.append(segment)
        else:
            for subscriber_deque in self.stream_segments_subscribers:
                subscriber_deque.append(segment)

    def xǁUStreamTVWsClientǁ_segments_append__mutmut_2(self, segment: UStreamTVSegment):
        # if there are no subscribers yet, add segment(s) to the initial deque
        if not self.stream_segments_subscribers:
            self.stream_segments_initial.append(None)
        else:
            for subscriber_deque in self.stream_segments_subscribers:
                subscriber_deque.append(segment)

    def xǁUStreamTVWsClientǁ_segments_append__mutmut_3(self, segment: UStreamTVSegment):
        # if there are no subscribers yet, add segment(s) to the initial deque
        if not self.stream_segments_subscribers:
            self.stream_segments_initial.append(segment)
        else:
            for subscriber_deque in self.stream_segments_subscribers:
                subscriber_deque.append(None)
    
    xǁUStreamTVWsClientǁ_segments_append__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_segments_append__mutmut_1': xǁUStreamTVWsClientǁ_segments_append__mutmut_1, 
        'xǁUStreamTVWsClientǁ_segments_append__mutmut_2': xǁUStreamTVWsClientǁ_segments_append__mutmut_2, 
        'xǁUStreamTVWsClientǁ_segments_append__mutmut_3': xǁUStreamTVWsClientǁ_segments_append__mutmut_3
    }
    
    def _segments_append(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_segments_append__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_segments_append__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _segments_append.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_segments_append__mutmut_orig)
    xǁUStreamTVWsClientǁ_segments_append__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_segments_append'

    def xǁUStreamTVWsClientǁon_open__mutmut_orig(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_1(self, wsapp):
        args = None
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_2(self, wsapp):
        args = {
            "XXtypeXX": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_3(self, wsapp):
        args = {
            "TYPE": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_4(self, wsapp):
        args = {
            "Type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_5(self, wsapp):
        args = {
            "type": "XXviewerXX",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_6(self, wsapp):
        args = {
            "type": "VIEWER",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_7(self, wsapp):
        args = {
            "type": "Viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_8(self, wsapp):
        args = {
            "type": "viewer",
            "XXappIdXX": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_9(self, wsapp):
        args = {
            "type": "viewer",
            "appid": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_10(self, wsapp):
        args = {
            "type": "viewer",
            "APPID": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_11(self, wsapp):
        args = {
            "type": "viewer",
            "Appid": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_12(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "XXappVersionXX": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_13(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appversion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_14(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "APPVERSION": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_15(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "Appversion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_16(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "XXrsidXX": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_17(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "RSID": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_18(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "Rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_19(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(None, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_20(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, None):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_21(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_22(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, ):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_23(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(1, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_24(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10000000001):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_25(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(None, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_26(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, None):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_27(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_28(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, ):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_29(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(1, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_30(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10000000001):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_31(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "XXrpinXX": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_32(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "RPIN": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_33(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "Rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_34(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(None, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_35(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, None)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_36(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_37(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, )}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_38(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(1, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_39(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1000000000000001)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_40(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "XXreferrerXX": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_41(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "REFERRER": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_42(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "Referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_43(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "XXclusterHostXX": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_44(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterhost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_45(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "CLUSTERHOST": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_46(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "Clusterhost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_47(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "XXr%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tvXX",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_48(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaid%-%mediatype%-%protocolprefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_49(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "R%RND%-1-%MEDIAID%-%MEDIATYPE%-%PROTOCOLPREFIX%-%CLUSTER%.UMS.USTREAM.TV",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_50(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "R%rnd%-1-%mediaid%-%mediatype%-%protocolprefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_51(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "XXmediaXX": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_52(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "MEDIA": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_53(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "Media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_54(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "XXapplicationXX": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_55(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "APPLICATION": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_56(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "Application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_57(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = None

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_58(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["XXpasswordXX"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_59(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["PASSWORD"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_60(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["Password"] = self.password

        self.send_json({
            "cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_61(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json(None)

    def xǁUStreamTVWsClientǁon_open__mutmut_62(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "XXcmdXX": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_63(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "CMD": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_64(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "Cmd": "connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_65(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "XXconnectXX",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_66(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "CONNECT",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_67(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "Connect",
            "args": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_68(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "XXargsXX": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_69(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "ARGS": [args],
        })

    def xǁUStreamTVWsClientǁon_open__mutmut_70(self, wsapp):
        args = {
            "type": "viewer",
            "appId": self.app_id,
            "appVersion": self.app_version,
            "rsid": f"{randint(0, 10_000_000_000):x}:{randint(0, 10_000_000_000):x}",
            "rpin": f"_rpin.{randint(0, 1_000_000_000_000_000)}",
            "referrer": self.referrer,
            "clusterHost": "r%rnd%-1-%mediaId%-%mediaType%-%protocolPrefix%-%cluster%.ums.ustream.tv",
            "media": self.media_id,
            "application": self.application,
        }
        if self.password:
            args["password"] = self.password

        self.send_json({
            "cmd": "connect",
            "Args": [args],
        })
    
    xǁUStreamTVWsClientǁon_open__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁon_open__mutmut_1': xǁUStreamTVWsClientǁon_open__mutmut_1, 
        'xǁUStreamTVWsClientǁon_open__mutmut_2': xǁUStreamTVWsClientǁon_open__mutmut_2, 
        'xǁUStreamTVWsClientǁon_open__mutmut_3': xǁUStreamTVWsClientǁon_open__mutmut_3, 
        'xǁUStreamTVWsClientǁon_open__mutmut_4': xǁUStreamTVWsClientǁon_open__mutmut_4, 
        'xǁUStreamTVWsClientǁon_open__mutmut_5': xǁUStreamTVWsClientǁon_open__mutmut_5, 
        'xǁUStreamTVWsClientǁon_open__mutmut_6': xǁUStreamTVWsClientǁon_open__mutmut_6, 
        'xǁUStreamTVWsClientǁon_open__mutmut_7': xǁUStreamTVWsClientǁon_open__mutmut_7, 
        'xǁUStreamTVWsClientǁon_open__mutmut_8': xǁUStreamTVWsClientǁon_open__mutmut_8, 
        'xǁUStreamTVWsClientǁon_open__mutmut_9': xǁUStreamTVWsClientǁon_open__mutmut_9, 
        'xǁUStreamTVWsClientǁon_open__mutmut_10': xǁUStreamTVWsClientǁon_open__mutmut_10, 
        'xǁUStreamTVWsClientǁon_open__mutmut_11': xǁUStreamTVWsClientǁon_open__mutmut_11, 
        'xǁUStreamTVWsClientǁon_open__mutmut_12': xǁUStreamTVWsClientǁon_open__mutmut_12, 
        'xǁUStreamTVWsClientǁon_open__mutmut_13': xǁUStreamTVWsClientǁon_open__mutmut_13, 
        'xǁUStreamTVWsClientǁon_open__mutmut_14': xǁUStreamTVWsClientǁon_open__mutmut_14, 
        'xǁUStreamTVWsClientǁon_open__mutmut_15': xǁUStreamTVWsClientǁon_open__mutmut_15, 
        'xǁUStreamTVWsClientǁon_open__mutmut_16': xǁUStreamTVWsClientǁon_open__mutmut_16, 
        'xǁUStreamTVWsClientǁon_open__mutmut_17': xǁUStreamTVWsClientǁon_open__mutmut_17, 
        'xǁUStreamTVWsClientǁon_open__mutmut_18': xǁUStreamTVWsClientǁon_open__mutmut_18, 
        'xǁUStreamTVWsClientǁon_open__mutmut_19': xǁUStreamTVWsClientǁon_open__mutmut_19, 
        'xǁUStreamTVWsClientǁon_open__mutmut_20': xǁUStreamTVWsClientǁon_open__mutmut_20, 
        'xǁUStreamTVWsClientǁon_open__mutmut_21': xǁUStreamTVWsClientǁon_open__mutmut_21, 
        'xǁUStreamTVWsClientǁon_open__mutmut_22': xǁUStreamTVWsClientǁon_open__mutmut_22, 
        'xǁUStreamTVWsClientǁon_open__mutmut_23': xǁUStreamTVWsClientǁon_open__mutmut_23, 
        'xǁUStreamTVWsClientǁon_open__mutmut_24': xǁUStreamTVWsClientǁon_open__mutmut_24, 
        'xǁUStreamTVWsClientǁon_open__mutmut_25': xǁUStreamTVWsClientǁon_open__mutmut_25, 
        'xǁUStreamTVWsClientǁon_open__mutmut_26': xǁUStreamTVWsClientǁon_open__mutmut_26, 
        'xǁUStreamTVWsClientǁon_open__mutmut_27': xǁUStreamTVWsClientǁon_open__mutmut_27, 
        'xǁUStreamTVWsClientǁon_open__mutmut_28': xǁUStreamTVWsClientǁon_open__mutmut_28, 
        'xǁUStreamTVWsClientǁon_open__mutmut_29': xǁUStreamTVWsClientǁon_open__mutmut_29, 
        'xǁUStreamTVWsClientǁon_open__mutmut_30': xǁUStreamTVWsClientǁon_open__mutmut_30, 
        'xǁUStreamTVWsClientǁon_open__mutmut_31': xǁUStreamTVWsClientǁon_open__mutmut_31, 
        'xǁUStreamTVWsClientǁon_open__mutmut_32': xǁUStreamTVWsClientǁon_open__mutmut_32, 
        'xǁUStreamTVWsClientǁon_open__mutmut_33': xǁUStreamTVWsClientǁon_open__mutmut_33, 
        'xǁUStreamTVWsClientǁon_open__mutmut_34': xǁUStreamTVWsClientǁon_open__mutmut_34, 
        'xǁUStreamTVWsClientǁon_open__mutmut_35': xǁUStreamTVWsClientǁon_open__mutmut_35, 
        'xǁUStreamTVWsClientǁon_open__mutmut_36': xǁUStreamTVWsClientǁon_open__mutmut_36, 
        'xǁUStreamTVWsClientǁon_open__mutmut_37': xǁUStreamTVWsClientǁon_open__mutmut_37, 
        'xǁUStreamTVWsClientǁon_open__mutmut_38': xǁUStreamTVWsClientǁon_open__mutmut_38, 
        'xǁUStreamTVWsClientǁon_open__mutmut_39': xǁUStreamTVWsClientǁon_open__mutmut_39, 
        'xǁUStreamTVWsClientǁon_open__mutmut_40': xǁUStreamTVWsClientǁon_open__mutmut_40, 
        'xǁUStreamTVWsClientǁon_open__mutmut_41': xǁUStreamTVWsClientǁon_open__mutmut_41, 
        'xǁUStreamTVWsClientǁon_open__mutmut_42': xǁUStreamTVWsClientǁon_open__mutmut_42, 
        'xǁUStreamTVWsClientǁon_open__mutmut_43': xǁUStreamTVWsClientǁon_open__mutmut_43, 
        'xǁUStreamTVWsClientǁon_open__mutmut_44': xǁUStreamTVWsClientǁon_open__mutmut_44, 
        'xǁUStreamTVWsClientǁon_open__mutmut_45': xǁUStreamTVWsClientǁon_open__mutmut_45, 
        'xǁUStreamTVWsClientǁon_open__mutmut_46': xǁUStreamTVWsClientǁon_open__mutmut_46, 
        'xǁUStreamTVWsClientǁon_open__mutmut_47': xǁUStreamTVWsClientǁon_open__mutmut_47, 
        'xǁUStreamTVWsClientǁon_open__mutmut_48': xǁUStreamTVWsClientǁon_open__mutmut_48, 
        'xǁUStreamTVWsClientǁon_open__mutmut_49': xǁUStreamTVWsClientǁon_open__mutmut_49, 
        'xǁUStreamTVWsClientǁon_open__mutmut_50': xǁUStreamTVWsClientǁon_open__mutmut_50, 
        'xǁUStreamTVWsClientǁon_open__mutmut_51': xǁUStreamTVWsClientǁon_open__mutmut_51, 
        'xǁUStreamTVWsClientǁon_open__mutmut_52': xǁUStreamTVWsClientǁon_open__mutmut_52, 
        'xǁUStreamTVWsClientǁon_open__mutmut_53': xǁUStreamTVWsClientǁon_open__mutmut_53, 
        'xǁUStreamTVWsClientǁon_open__mutmut_54': xǁUStreamTVWsClientǁon_open__mutmut_54, 
        'xǁUStreamTVWsClientǁon_open__mutmut_55': xǁUStreamTVWsClientǁon_open__mutmut_55, 
        'xǁUStreamTVWsClientǁon_open__mutmut_56': xǁUStreamTVWsClientǁon_open__mutmut_56, 
        'xǁUStreamTVWsClientǁon_open__mutmut_57': xǁUStreamTVWsClientǁon_open__mutmut_57, 
        'xǁUStreamTVWsClientǁon_open__mutmut_58': xǁUStreamTVWsClientǁon_open__mutmut_58, 
        'xǁUStreamTVWsClientǁon_open__mutmut_59': xǁUStreamTVWsClientǁon_open__mutmut_59, 
        'xǁUStreamTVWsClientǁon_open__mutmut_60': xǁUStreamTVWsClientǁon_open__mutmut_60, 
        'xǁUStreamTVWsClientǁon_open__mutmut_61': xǁUStreamTVWsClientǁon_open__mutmut_61, 
        'xǁUStreamTVWsClientǁon_open__mutmut_62': xǁUStreamTVWsClientǁon_open__mutmut_62, 
        'xǁUStreamTVWsClientǁon_open__mutmut_63': xǁUStreamTVWsClientǁon_open__mutmut_63, 
        'xǁUStreamTVWsClientǁon_open__mutmut_64': xǁUStreamTVWsClientǁon_open__mutmut_64, 
        'xǁUStreamTVWsClientǁon_open__mutmut_65': xǁUStreamTVWsClientǁon_open__mutmut_65, 
        'xǁUStreamTVWsClientǁon_open__mutmut_66': xǁUStreamTVWsClientǁon_open__mutmut_66, 
        'xǁUStreamTVWsClientǁon_open__mutmut_67': xǁUStreamTVWsClientǁon_open__mutmut_67, 
        'xǁUStreamTVWsClientǁon_open__mutmut_68': xǁUStreamTVWsClientǁon_open__mutmut_68, 
        'xǁUStreamTVWsClientǁon_open__mutmut_69': xǁUStreamTVWsClientǁon_open__mutmut_69, 
        'xǁUStreamTVWsClientǁon_open__mutmut_70': xǁUStreamTVWsClientǁon_open__mutmut_70
    }
    
    def on_open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁon_open__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁon_open__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_open.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁon_open__mutmut_orig)
    xǁUStreamTVWsClientǁon_open__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁon_open'

    def xǁUStreamTVWsClientǁon_message__mutmut_orig(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_1(self, wsapp, data: str):
        try:
            parsed = None
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_2(self, wsapp, data: str):
        try:
            parsed = parse_json(None, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_3(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=None)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_4(self, wsapp, data: str):
        try:
            parsed = parse_json(schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_5(self, wsapp, data: str):
        try:
            parsed = parse_json(data, )
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_6(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(None)
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_7(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:51]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_8(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = None
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_9(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["XXcmdXX"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_10(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["CMD"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_11(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["Cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_12(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = None
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_13(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["XXargsXX"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_14(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["ARGS"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_15(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["Args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_16(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(None)  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_17(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(None)  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_18(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = None
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_19(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(None)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_20(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_21(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = None
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_22(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(None)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_23(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_24(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(None)
                        handler(self, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_25(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(None, argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_26(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, None)

    def xǁUStreamTVWsClientǁon_message__mutmut_27(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(argdata)

    def xǁUStreamTVWsClientǁon_message__mutmut_28(self, wsapp, data: str):
        try:
            parsed = parse_json(data, schema=self._schema_cmd)
        except PluginError:
            log.error(f"Could not parse message: {data[:50]}")
            return

        cmd: str = parsed["cmd"]
        args: list[dict] = parsed["args"]
        log.trace(f"Received '{cmd}' command")  # type: ignore[attr-defined]
        log.trace(f"{args!r}")  # type: ignore[attr-defined]

        handlers = self._MESSAGE_HANDLERS.get(cmd)
        if handlers is not None:
            for arg in args:
                for name, handler in handlers.items():
                    argdata = arg.get(name)
                    if argdata is not None:
                        log.debug(f"Processing '{cmd}' - '{name}'")
                        handler(self, )
    
    xǁUStreamTVWsClientǁon_message__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁon_message__mutmut_1': xǁUStreamTVWsClientǁon_message__mutmut_1, 
        'xǁUStreamTVWsClientǁon_message__mutmut_2': xǁUStreamTVWsClientǁon_message__mutmut_2, 
        'xǁUStreamTVWsClientǁon_message__mutmut_3': xǁUStreamTVWsClientǁon_message__mutmut_3, 
        'xǁUStreamTVWsClientǁon_message__mutmut_4': xǁUStreamTVWsClientǁon_message__mutmut_4, 
        'xǁUStreamTVWsClientǁon_message__mutmut_5': xǁUStreamTVWsClientǁon_message__mutmut_5, 
        'xǁUStreamTVWsClientǁon_message__mutmut_6': xǁUStreamTVWsClientǁon_message__mutmut_6, 
        'xǁUStreamTVWsClientǁon_message__mutmut_7': xǁUStreamTVWsClientǁon_message__mutmut_7, 
        'xǁUStreamTVWsClientǁon_message__mutmut_8': xǁUStreamTVWsClientǁon_message__mutmut_8, 
        'xǁUStreamTVWsClientǁon_message__mutmut_9': xǁUStreamTVWsClientǁon_message__mutmut_9, 
        'xǁUStreamTVWsClientǁon_message__mutmut_10': xǁUStreamTVWsClientǁon_message__mutmut_10, 
        'xǁUStreamTVWsClientǁon_message__mutmut_11': xǁUStreamTVWsClientǁon_message__mutmut_11, 
        'xǁUStreamTVWsClientǁon_message__mutmut_12': xǁUStreamTVWsClientǁon_message__mutmut_12, 
        'xǁUStreamTVWsClientǁon_message__mutmut_13': xǁUStreamTVWsClientǁon_message__mutmut_13, 
        'xǁUStreamTVWsClientǁon_message__mutmut_14': xǁUStreamTVWsClientǁon_message__mutmut_14, 
        'xǁUStreamTVWsClientǁon_message__mutmut_15': xǁUStreamTVWsClientǁon_message__mutmut_15, 
        'xǁUStreamTVWsClientǁon_message__mutmut_16': xǁUStreamTVWsClientǁon_message__mutmut_16, 
        'xǁUStreamTVWsClientǁon_message__mutmut_17': xǁUStreamTVWsClientǁon_message__mutmut_17, 
        'xǁUStreamTVWsClientǁon_message__mutmut_18': xǁUStreamTVWsClientǁon_message__mutmut_18, 
        'xǁUStreamTVWsClientǁon_message__mutmut_19': xǁUStreamTVWsClientǁon_message__mutmut_19, 
        'xǁUStreamTVWsClientǁon_message__mutmut_20': xǁUStreamTVWsClientǁon_message__mutmut_20, 
        'xǁUStreamTVWsClientǁon_message__mutmut_21': xǁUStreamTVWsClientǁon_message__mutmut_21, 
        'xǁUStreamTVWsClientǁon_message__mutmut_22': xǁUStreamTVWsClientǁon_message__mutmut_22, 
        'xǁUStreamTVWsClientǁon_message__mutmut_23': xǁUStreamTVWsClientǁon_message__mutmut_23, 
        'xǁUStreamTVWsClientǁon_message__mutmut_24': xǁUStreamTVWsClientǁon_message__mutmut_24, 
        'xǁUStreamTVWsClientǁon_message__mutmut_25': xǁUStreamTVWsClientǁon_message__mutmut_25, 
        'xǁUStreamTVWsClientǁon_message__mutmut_26': xǁUStreamTVWsClientǁon_message__mutmut_26, 
        'xǁUStreamTVWsClientǁon_message__mutmut_27': xǁUStreamTVWsClientǁon_message__mutmut_27, 
        'xǁUStreamTVWsClientǁon_message__mutmut_28': xǁUStreamTVWsClientǁon_message__mutmut_28
    }
    
    def on_message(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁon_message__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁon_message__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_message.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁon_message__mutmut_orig)
    xǁUStreamTVWsClientǁon_message__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁon_message'

    # noinspection PyMethodMayBeStatic
    def xǁUStreamTVWsClientǁ_handle_warning__mutmut_orig(self, data: dict):
        log.warning(f"{data['code']}: {str(data['message'])[:50]}")

    # noinspection PyMethodMayBeStatic
    def xǁUStreamTVWsClientǁ_handle_warning__mutmut_1(self, data: dict):
        log.warning(None)

    # noinspection PyMethodMayBeStatic
    def xǁUStreamTVWsClientǁ_handle_warning__mutmut_2(self, data: dict):
        log.warning(f"{data['XXcodeXX']}: {str(data['message'])[:50]}")

    # noinspection PyMethodMayBeStatic
    def xǁUStreamTVWsClientǁ_handle_warning__mutmut_3(self, data: dict):
        log.warning(f"{data['CODE']}: {str(data['message'])[:50]}")

    # noinspection PyMethodMayBeStatic
    def xǁUStreamTVWsClientǁ_handle_warning__mutmut_4(self, data: dict):
        log.warning(f"{data['Code']}: {str(data['message'])[:50]}")

    # noinspection PyMethodMayBeStatic
    def xǁUStreamTVWsClientǁ_handle_warning__mutmut_5(self, data: dict):
        log.warning(f"{data['code']}: {str(None)[:50]}")

    # noinspection PyMethodMayBeStatic
    def xǁUStreamTVWsClientǁ_handle_warning__mutmut_6(self, data: dict):
        log.warning(f"{data['code']}: {str(data['XXmessageXX'])[:50]}")

    # noinspection PyMethodMayBeStatic
    def xǁUStreamTVWsClientǁ_handle_warning__mutmut_7(self, data: dict):
        log.warning(f"{data['code']}: {str(data['MESSAGE'])[:50]}")

    # noinspection PyMethodMayBeStatic
    def xǁUStreamTVWsClientǁ_handle_warning__mutmut_8(self, data: dict):
        log.warning(f"{data['code']}: {str(data['Message'])[:50]}")

    # noinspection PyMethodMayBeStatic
    def xǁUStreamTVWsClientǁ_handle_warning__mutmut_9(self, data: dict):
        log.warning(f"{data['code']}: {str(data['message'])[:51]}")
    
    xǁUStreamTVWsClientǁ_handle_warning__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_handle_warning__mutmut_1': xǁUStreamTVWsClientǁ_handle_warning__mutmut_1, 
        'xǁUStreamTVWsClientǁ_handle_warning__mutmut_2': xǁUStreamTVWsClientǁ_handle_warning__mutmut_2, 
        'xǁUStreamTVWsClientǁ_handle_warning__mutmut_3': xǁUStreamTVWsClientǁ_handle_warning__mutmut_3, 
        'xǁUStreamTVWsClientǁ_handle_warning__mutmut_4': xǁUStreamTVWsClientǁ_handle_warning__mutmut_4, 
        'xǁUStreamTVWsClientǁ_handle_warning__mutmut_5': xǁUStreamTVWsClientǁ_handle_warning__mutmut_5, 
        'xǁUStreamTVWsClientǁ_handle_warning__mutmut_6': xǁUStreamTVWsClientǁ_handle_warning__mutmut_6, 
        'xǁUStreamTVWsClientǁ_handle_warning__mutmut_7': xǁUStreamTVWsClientǁ_handle_warning__mutmut_7, 
        'xǁUStreamTVWsClientǁ_handle_warning__mutmut_8': xǁUStreamTVWsClientǁ_handle_warning__mutmut_8, 
        'xǁUStreamTVWsClientǁ_handle_warning__mutmut_9': xǁUStreamTVWsClientǁ_handle_warning__mutmut_9
    }
    
    def _handle_warning(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_warning__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_warning__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _handle_warning.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_handle_warning__mutmut_orig)
    xǁUStreamTVWsClientǁ_handle_warning__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_handle_warning'

    # noinspection PyUnusedLocal
    def xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_orig(self, *args):
        self._set_error("This channel does not exist")

    # noinspection PyUnusedLocal
    def xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_1(self, *args):
        self._set_error(None)

    # noinspection PyUnusedLocal
    def xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_2(self, *args):
        self._set_error("XXThis channel does not existXX")

    # noinspection PyUnusedLocal
    def xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_3(self, *args):
        self._set_error("this channel does not exist")

    # noinspection PyUnusedLocal
    def xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_4(self, *args):
        self._set_error("THIS CHANNEL DOES NOT EXIST")
    
    xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_1': xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_1, 
        'xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_2': xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_2, 
        'xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_3': xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_3, 
        'xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_4': xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_4
    }
    
    def _handle_reject_nonexistent(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _handle_reject_nonexistent.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_orig)
    xǁUStreamTVWsClientǁ_handle_reject_nonexistent__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_handle_reject_nonexistent'

    # noinspection PyUnusedLocal
    def xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_orig(self, *args):
        self._set_error("This content is not available in your area")

    # noinspection PyUnusedLocal
    def xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_1(self, *args):
        self._set_error(None)

    # noinspection PyUnusedLocal
    def xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_2(self, *args):
        self._set_error("XXThis content is not available in your areaXX")

    # noinspection PyUnusedLocal
    def xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_3(self, *args):
        self._set_error("this content is not available in your area")

    # noinspection PyUnusedLocal
    def xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_4(self, *args):
        self._set_error("THIS CONTENT IS NOT AVAILABLE IN YOUR AREA")
    
    xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_1': xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_1, 
        'xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_2': xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_2, 
        'xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_3': xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_3, 
        'xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_4': xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_4
    }
    
    def _handle_reject_geo_lock(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _handle_reject_geo_lock.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_orig)
    xǁUStreamTVWsClientǁ_handle_reject_geo_lock__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_handle_reject_geo_lock'

    def xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_orig(self, arg: dict):
        self.cluster = arg["name"]
        log.info(f"Switching cluster to: {self.cluster}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_1(self, arg: dict):
        self.cluster = None
        log.info(f"Switching cluster to: {self.cluster}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_2(self, arg: dict):
        self.cluster = arg["XXnameXX"]
        log.info(f"Switching cluster to: {self.cluster}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_3(self, arg: dict):
        self.cluster = arg["NAME"]
        log.info(f"Switching cluster to: {self.cluster}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_4(self, arg: dict):
        self.cluster = arg["Name"]
        log.info(f"Switching cluster to: {self.cluster}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_5(self, arg: dict):
        self.cluster = arg["name"]
        log.info(None)
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_6(self, arg: dict):
        self.cluster = arg["name"]
        log.info(f"Switching cluster to: {self.cluster}")
        self.reconnect(url=None)
    
    xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_1': xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_1, 
        'xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_2': xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_2, 
        'xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_3': xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_3, 
        'xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_4': xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_4, 
        'xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_5': xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_5, 
        'xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_6': xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_6
    }
    
    def _handle_reject_cluster(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _handle_reject_cluster.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_orig)
    xǁUStreamTVWsClientǁ_handle_reject_cluster__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_handle_reject_cluster'

    def xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_orig(self, arg: dict):
        self.referrer = arg["redirectUrl"]
        log.info(f"Updating referrer to: {self.referrer}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_1(self, arg: dict):
        self.referrer = None
        log.info(f"Updating referrer to: {self.referrer}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_2(self, arg: dict):
        self.referrer = arg["XXredirectUrlXX"]
        log.info(f"Updating referrer to: {self.referrer}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_3(self, arg: dict):
        self.referrer = arg["redirecturl"]
        log.info(f"Updating referrer to: {self.referrer}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_4(self, arg: dict):
        self.referrer = arg["REDIRECTURL"]
        log.info(f"Updating referrer to: {self.referrer}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_5(self, arg: dict):
        self.referrer = arg["Redirecturl"]
        log.info(f"Updating referrer to: {self.referrer}")
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_6(self, arg: dict):
        self.referrer = arg["redirectUrl"]
        log.info(None)
        self.reconnect(url=self._get_url())

    def xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_7(self, arg: dict):
        self.referrer = arg["redirectUrl"]
        log.info(f"Updating referrer to: {self.referrer}")
        self.reconnect(url=None)
    
    xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_1': xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_1, 
        'xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_2': xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_2, 
        'xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_3': xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_3, 
        'xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_4': xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_4, 
        'xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_5': xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_5, 
        'xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_6': xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_6, 
        'xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_7': xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_7
    }
    
    def _handle_reject_referrer_lock(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _handle_reject_referrer_lock.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_orig)
    xǁUStreamTVWsClientǁ_handle_reject_referrer_lock__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_handle_reject_referrer_lock'

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_orig(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_1(self, data: dict):
        self.stream_cdn = None
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_2(self, data: dict):
        self.stream_cdn = urlunparse(None)
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_3(self, data: dict):
        self.stream_cdn = urlunparse((
            data["XXprotocolXX"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_4(self, data: dict):
        self.stream_cdn = urlunparse((
            data["PROTOCOL"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_5(self, data: dict):
        self.stream_cdn = urlunparse((
            data["Protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_6(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["XXdataXX"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_7(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["DATA"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_8(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["Data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_9(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][1]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_10(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["XXdataXX"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_11(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["DATA"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_12(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["Data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_13(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][1]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_14(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["XXsitesXX"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_15(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["SITES"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_16(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["Sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_17(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][1]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_18(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["XXhostXX"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_19(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["HOST"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_20(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["Host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_21(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["XXdataXX"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_22(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["DATA"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_23(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["Data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_24(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][1]["data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_25(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["XXdataXX"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_26(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["DATA"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_27(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["Data"][0]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_28(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][1]["sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_29(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["XXsitesXX"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_30(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["SITES"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_31(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["Sites"][0]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_32(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][1]["path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_33(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["XXpathXX"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_34(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["PATH"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_35(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["Path"],
            "",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_36(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "XXXX",
            "",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_37(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "XXXX",
            "",
        ))
        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_38(self, data: dict):
        self.stream_cdn = urlunparse((
            data["protocol"],
            data["data"][0]["data"][0]["sites"][0]["host"],
            data["data"][0]["data"][0]["sites"][0]["path"],
            "",
            "",
            "XXXX",
        ))
        self._set_ready()
    
    xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_1': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_1, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_2': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_2, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_3': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_3, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_4': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_4, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_5': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_5, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_6': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_6, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_7': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_7, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_8': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_8, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_9': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_9, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_10': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_10, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_11': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_11, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_12': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_12, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_13': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_13, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_14': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_14, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_15': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_15, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_16': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_16, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_17': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_17, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_18': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_18, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_19': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_19, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_20': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_20, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_21': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_21, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_22': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_22, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_23': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_23, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_24': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_24, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_25': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_25, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_26': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_26, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_27': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_27, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_28': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_28, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_29': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_29, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_30': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_30, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_31': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_31, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_32': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_32, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_33': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_33, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_34': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_34, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_35': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_35, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_36': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_36, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_37': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_37, 
        'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_38': xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_38
    }
    
    def _handle_module_info_cdn_config(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _handle_module_info_cdn_config.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_orig)
    xǁUStreamTVWsClientǁ_handle_module_info_cdn_config__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_handle_module_info_cdn_config'

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_orig(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_1(self, data: dict):
        if data.get(None) is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_2(self, data: dict):
        if data.get("XXcontentAvailableXX") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_3(self, data: dict):
        if data.get("contentavailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_4(self, data: dict):
        if data.get("CONTENTAVAILABLE") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_5(self, data: dict):
        if data.get("Contentavailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_6(self, data: dict):
        if data.get("contentAvailable") is not False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_7(self, data: dict):
        if data.get("contentAvailable") is True:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_8(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error(None)

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_9(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("XXThis stream is currently offlineXX")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_10(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("this stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_11(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("THIS STREAM IS CURRENTLY OFFLINE")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_12(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = None
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_13(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get(None)
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_14(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get(None, {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_15(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", None).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_16(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get({}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_17(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", ).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_18(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("XXstreamFormatsXX", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_19(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamformats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_20(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("STREAMFORMATS", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_21(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("Streamformats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_22(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("XXmp4/segmentedXX")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_23(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("MP4/SEGMENTED")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_24(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("Mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_25(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_26(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is not None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_27(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = None
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_28(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(None)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_29(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = None
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_30(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["XXstreamsXX"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_31(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["STREAMS"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_32(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["Streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_33(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(None)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_34(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = None
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_35(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(None)
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_36(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(None, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_37(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, None))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_38(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_39(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, ))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_40(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: None, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_41(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(None) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_42(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is not StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_43(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = None

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_44(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(None)

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_45(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(None, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_46(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, None))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_47(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_48(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, ))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_49(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: None, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_50(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(None) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_51(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is not StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_52(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = None
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_53(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(None)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_54(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error(None)
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_55(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("XXFailed parsing hashesXX")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_56(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_57(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("FAILED PARSING HASHES")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_58(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = None
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_59(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["XXchunkIdXX"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_60(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkid"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_61(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["CHUNKID"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_62(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["Chunkid"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_63(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = None
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_64(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["XXchunkTimeXX"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_65(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunktime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_66(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["CHUNKTIME"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_67(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["Chunktime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_68(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = None
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_69(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["XXcontentAccessXX"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_70(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentaccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_71(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["CONTENTACCESS"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_72(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["Contentaccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_73(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = None

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_74(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["XXhashesXX"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_75(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["HASHES"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_76(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["Hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_77(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = None
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_78(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(None)
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_79(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = None
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_80(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count != 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_81(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 1:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_82(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is not None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_83(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = None

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_84(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = None

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_85(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(None)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_86(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = None  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_87(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 11 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_88(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 + sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_89(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[1] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_90(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] / 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_91(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 11  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_92(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(None):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_93(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = None
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_94(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx - 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_95(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 2
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_96(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next <= count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_97(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = None
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_98(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] + segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_99(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(None, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_100(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, None):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_101(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_102(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, ):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_103(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id - diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_104(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        None,
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_105(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri=None,
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_106(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=None,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_107(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=None,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_108(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=None,
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_109(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=None,
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_110(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=None,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_111(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_112(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_113(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_114(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_115(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_116(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_117(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="XXXX",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_118(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time - timedelta(seconds=(num - current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_119(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=None),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_120(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num + current_id - 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_121(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id + 1) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_122(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 2) * duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_123(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) / duration / 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_124(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration * 1000),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()

    def xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_125(self, data: dict):
        if data.get("contentAvailable") is False:
            return self._set_error("This stream is currently offline")

        mp4_segmented = data.get("streamFormats", {}).get("mp4/segmented")
        if not mp4_segmented:
            return

        # parse the stream formats once
        if self.stream_initial_id is None:
            try:
                formats = self._schema_stream_formats.validate(mp4_segmented)
                formats = formats["streams"]
            except PluginError as err:
                return self._set_error(err)
            self.stream_formats_video = list(filter(lambda f: type(f) is StreamFormatVideo, formats))
            self.stream_formats_audio = list(filter(lambda f: type(f) is StreamFormatAudio, formats))

        # parse segment duration and hashes, and queue new segments
        try:
            segmentdata: dict = self._schema_stream_segments.validate(mp4_segmented)
        except PluginError:
            log.error("Failed parsing hashes")
            return

        current_id: int = segmentdata["chunkId"]
        duration: int = segmentdata["chunkTime"]
        path: str = segmentdata["contentAccess"]
        hashes: dict[int, str] = segmentdata["hashes"]

        sorted_ids = sorted(hashes.keys())
        count = len(sorted_ids)
        if count == 0:
            return

        # initial segment ID (needed by the workers to filter queued segments)
        if self.stream_initial_id is None:
            self.stream_initial_id = current_id

        current_time = datetime.now(timezone.utc)

        # lock the stream segments deques for the worker threads
        with self.stream_segments_lock:
            # interpolate and extrapolate segments from the provided id->hash data
            diff = 10 - sorted_ids[0] % 10  # if there's only one id->hash item, extrapolate until the next decimal
            for idx, segment_id in enumerate(sorted_ids):
                idx_next = idx + 1
                if idx_next < count:
                    # calculate the difference between IDs and use that to interpolate segment IDs
                    # the last id->hash item will use the previous diff to extrapolate segment IDs
                    diff = sorted_ids[idx_next] - segment_id
                for num in range(segment_id, segment_id + diff):
                    self._segments_append(
                        UStreamTVSegment(
                            uri="",
                            num=num,
                            duration=duration,
                            available_at=current_time + timedelta(seconds=(num - current_id - 1) * duration / 1001),
                            hash=hashes[segment_id],
                            path=path,
                        ),
                    )

        self._set_ready()
    
    xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_1': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_1, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_2': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_2, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_3': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_3, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_4': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_4, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_5': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_5, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_6': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_6, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_7': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_7, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_8': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_8, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_9': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_9, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_10': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_10, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_11': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_11, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_12': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_12, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_13': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_13, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_14': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_14, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_15': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_15, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_16': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_16, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_17': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_17, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_18': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_18, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_19': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_19, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_20': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_20, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_21': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_21, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_22': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_22, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_23': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_23, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_24': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_24, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_25': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_25, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_26': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_26, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_27': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_27, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_28': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_28, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_29': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_29, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_30': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_30, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_31': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_31, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_32': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_32, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_33': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_33, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_34': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_34, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_35': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_35, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_36': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_36, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_37': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_37, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_38': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_38, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_39': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_39, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_40': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_40, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_41': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_41, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_42': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_42, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_43': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_43, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_44': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_44, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_45': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_45, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_46': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_46, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_47': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_47, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_48': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_48, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_49': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_49, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_50': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_50, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_51': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_51, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_52': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_52, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_53': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_53, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_54': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_54, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_55': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_55, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_56': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_56, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_57': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_57, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_58': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_58, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_59': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_59, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_60': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_60, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_61': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_61, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_62': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_62, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_63': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_63, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_64': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_64, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_65': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_65, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_66': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_66, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_67': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_67, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_68': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_68, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_69': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_69, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_70': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_70, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_71': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_71, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_72': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_72, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_73': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_73, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_74': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_74, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_75': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_75, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_76': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_76, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_77': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_77, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_78': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_78, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_79': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_79, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_80': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_80, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_81': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_81, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_82': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_82, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_83': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_83, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_84': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_84, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_85': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_85, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_86': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_86, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_87': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_87, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_88': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_88, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_89': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_89, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_90': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_90, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_91': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_91, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_92': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_92, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_93': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_93, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_94': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_94, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_95': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_95, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_96': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_96, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_97': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_97, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_98': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_98, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_99': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_99, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_100': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_100, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_101': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_101, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_102': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_102, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_103': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_103, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_104': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_104, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_105': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_105, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_106': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_106, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_107': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_107, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_108': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_108, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_109': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_109, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_110': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_110, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_111': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_111, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_112': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_112, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_113': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_113, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_114': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_114, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_115': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_115, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_116': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_116, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_117': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_117, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_118': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_118, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_119': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_119, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_120': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_120, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_121': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_121, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_122': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_122, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_123': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_123, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_124': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_124, 
        'xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_125': xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_125
    }
    
    def _handle_module_info_stream(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _handle_module_info_stream.__signature__ = _mutmut_signature(xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_orig)
    xǁUStreamTVWsClientǁ_handle_module_info_stream__mutmut_orig.__name__ = 'xǁUStreamTVWsClientǁ_handle_module_info_stream'

    # ----

    _MESSAGE_HANDLERS: Mapping[str, Mapping[str, Callable[[UStreamTVWsClient, Any], None]]] = {
        "warning": {
            "code": _handle_warning,
        },
        "reject": {
            "cluster": _handle_reject_cluster,
            "referrerLock": _handle_reject_referrer_lock,
            "nonexistent": _handle_reject_nonexistent,
            "geoLock": _handle_reject_geo_lock,
        },
        "moduleInfo": {
            "cdnConfig": _handle_module_info_cdn_config,
            "stream": _handle_module_info_stream,
        },
    }


class UStreamTVStreamWriter(SegmentedStreamWriter[UStreamTVSegment, Response]):
    reader: UStreamTVStreamReader
    stream: UStreamTVStream

    def xǁUStreamTVStreamWriterǁ__init____mutmut_orig(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._has_init = False

    def xǁUStreamTVStreamWriterǁ__init____mutmut_1(self, *args, **kwargs):
        super().__init__(**kwargs)
        self._has_init = False

    def xǁUStreamTVStreamWriterǁ__init____mutmut_2(self, *args, **kwargs):
        super().__init__(*args, )
        self._has_init = False

    def xǁUStreamTVStreamWriterǁ__init____mutmut_3(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._has_init = None

    def xǁUStreamTVStreamWriterǁ__init____mutmut_4(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._has_init = True
    
    xǁUStreamTVStreamWriterǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVStreamWriterǁ__init____mutmut_1': xǁUStreamTVStreamWriterǁ__init____mutmut_1, 
        'xǁUStreamTVStreamWriterǁ__init____mutmut_2': xǁUStreamTVStreamWriterǁ__init____mutmut_2, 
        'xǁUStreamTVStreamWriterǁ__init____mutmut_3': xǁUStreamTVStreamWriterǁ__init____mutmut_3, 
        'xǁUStreamTVStreamWriterǁ__init____mutmut_4': xǁUStreamTVStreamWriterǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVStreamWriterǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVStreamWriterǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁUStreamTVStreamWriterǁ__init____mutmut_orig)
    xǁUStreamTVStreamWriterǁ__init____mutmut_orig.__name__ = 'xǁUStreamTVStreamWriterǁ__init__'

    def xǁUStreamTVStreamWriterǁput__mutmut_orig(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_1(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is not None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_2(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_3(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, )
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_4(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_5(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = None
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_6(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = False
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_7(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(None, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_8(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, None)
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_9(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_10(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, )
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_11(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(None, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_12(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, None, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_13(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, None))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_14(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_15(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_16(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, ))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_17(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, False))
            self.queue(segment, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_18(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(None, self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_19(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, None)

    def xǁUStreamTVStreamWriterǁput__mutmut_20(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(self.executor.submit(self.fetch, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_21(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, )

    def xǁUStreamTVStreamWriterǁput__mutmut_22(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(None, segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_23(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, None, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_24(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, None))

    def xǁUStreamTVStreamWriterǁput__mutmut_25(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(segment, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_26(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, False))

    def xǁUStreamTVStreamWriterǁput__mutmut_27(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, ))

    def xǁUStreamTVStreamWriterǁput__mutmut_28(self, segment):
        if self.closed:  # pragma: no cover
            return

        if segment is None:
            self.queue(None, None)
        else:
            if not self._has_init:
                self._has_init = True
                self.queue(segment, self.executor.submit(self.fetch, segment, True))
            self.queue(segment, self.executor.submit(self.fetch, segment, True))
    
    xǁUStreamTVStreamWriterǁput__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVStreamWriterǁput__mutmut_1': xǁUStreamTVStreamWriterǁput__mutmut_1, 
        'xǁUStreamTVStreamWriterǁput__mutmut_2': xǁUStreamTVStreamWriterǁput__mutmut_2, 
        'xǁUStreamTVStreamWriterǁput__mutmut_3': xǁUStreamTVStreamWriterǁput__mutmut_3, 
        'xǁUStreamTVStreamWriterǁput__mutmut_4': xǁUStreamTVStreamWriterǁput__mutmut_4, 
        'xǁUStreamTVStreamWriterǁput__mutmut_5': xǁUStreamTVStreamWriterǁput__mutmut_5, 
        'xǁUStreamTVStreamWriterǁput__mutmut_6': xǁUStreamTVStreamWriterǁput__mutmut_6, 
        'xǁUStreamTVStreamWriterǁput__mutmut_7': xǁUStreamTVStreamWriterǁput__mutmut_7, 
        'xǁUStreamTVStreamWriterǁput__mutmut_8': xǁUStreamTVStreamWriterǁput__mutmut_8, 
        'xǁUStreamTVStreamWriterǁput__mutmut_9': xǁUStreamTVStreamWriterǁput__mutmut_9, 
        'xǁUStreamTVStreamWriterǁput__mutmut_10': xǁUStreamTVStreamWriterǁput__mutmut_10, 
        'xǁUStreamTVStreamWriterǁput__mutmut_11': xǁUStreamTVStreamWriterǁput__mutmut_11, 
        'xǁUStreamTVStreamWriterǁput__mutmut_12': xǁUStreamTVStreamWriterǁput__mutmut_12, 
        'xǁUStreamTVStreamWriterǁput__mutmut_13': xǁUStreamTVStreamWriterǁput__mutmut_13, 
        'xǁUStreamTVStreamWriterǁput__mutmut_14': xǁUStreamTVStreamWriterǁput__mutmut_14, 
        'xǁUStreamTVStreamWriterǁput__mutmut_15': xǁUStreamTVStreamWriterǁput__mutmut_15, 
        'xǁUStreamTVStreamWriterǁput__mutmut_16': xǁUStreamTVStreamWriterǁput__mutmut_16, 
        'xǁUStreamTVStreamWriterǁput__mutmut_17': xǁUStreamTVStreamWriterǁput__mutmut_17, 
        'xǁUStreamTVStreamWriterǁput__mutmut_18': xǁUStreamTVStreamWriterǁput__mutmut_18, 
        'xǁUStreamTVStreamWriterǁput__mutmut_19': xǁUStreamTVStreamWriterǁput__mutmut_19, 
        'xǁUStreamTVStreamWriterǁput__mutmut_20': xǁUStreamTVStreamWriterǁput__mutmut_20, 
        'xǁUStreamTVStreamWriterǁput__mutmut_21': xǁUStreamTVStreamWriterǁput__mutmut_21, 
        'xǁUStreamTVStreamWriterǁput__mutmut_22': xǁUStreamTVStreamWriterǁput__mutmut_22, 
        'xǁUStreamTVStreamWriterǁput__mutmut_23': xǁUStreamTVStreamWriterǁput__mutmut_23, 
        'xǁUStreamTVStreamWriterǁput__mutmut_24': xǁUStreamTVStreamWriterǁput__mutmut_24, 
        'xǁUStreamTVStreamWriterǁput__mutmut_25': xǁUStreamTVStreamWriterǁput__mutmut_25, 
        'xǁUStreamTVStreamWriterǁput__mutmut_26': xǁUStreamTVStreamWriterǁput__mutmut_26, 
        'xǁUStreamTVStreamWriterǁput__mutmut_27': xǁUStreamTVStreamWriterǁput__mutmut_27, 
        'xǁUStreamTVStreamWriterǁput__mutmut_28': xǁUStreamTVStreamWriterǁput__mutmut_28
    }
    
    def put(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVStreamWriterǁput__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVStreamWriterǁput__mutmut_mutants"), args, kwargs, self)
        return result 
    
    put.__signature__ = _mutmut_signature(xǁUStreamTVStreamWriterǁput__mutmut_orig)
    xǁUStreamTVStreamWriterǁput__mutmut_orig.__name__ = 'xǁUStreamTVStreamWriterǁput'

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_orig(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_1(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = None
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_2(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(None)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_3(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at >= now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_4(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = None
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_5(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at + now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_6(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(None)
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_7(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_8(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(None):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_9(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                None,
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_10(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=None,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_11(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=None,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_12(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=None,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_13(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_14(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_15(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_16(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_17(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    None,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_18(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    None,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_19(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_20(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(f"Failed to fetch {self.stream.kind} segment {segment.num}: {err}")

    # noinspection PyMethodOverriding
    def xǁUStreamTVStreamWriterǁfetch__mutmut_21(self, segment: UStreamTVSegment, is_init: bool):  # type: ignore[override]
        if self.closed:  # pragma: no cover
            return

        now = datetime.now(timezone.utc)
        if segment.available_at > now:
            time_to_wait = (segment.available_at - now).total_seconds()
            log.debug(f"Waiting for {self.stream.kind} segment: {segment.num} ({time_to_wait:.01f}s)")
            if not self.reader.worker.wait(time_to_wait):
                return

        try:
            return self.session.http.get(
                segment.url(
                    self.stream.wsclient.stream_cdn,
                    self.stream.stream_format.initUrl if is_init else self.stream.stream_format.segmentUrl,
                ),
                timeout=self.timeout,
                retries=self.retries,
                exception=StreamError,
            )
        except StreamError as err:
            log.error(None)
    
    xǁUStreamTVStreamWriterǁfetch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVStreamWriterǁfetch__mutmut_1': xǁUStreamTVStreamWriterǁfetch__mutmut_1, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_2': xǁUStreamTVStreamWriterǁfetch__mutmut_2, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_3': xǁUStreamTVStreamWriterǁfetch__mutmut_3, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_4': xǁUStreamTVStreamWriterǁfetch__mutmut_4, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_5': xǁUStreamTVStreamWriterǁfetch__mutmut_5, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_6': xǁUStreamTVStreamWriterǁfetch__mutmut_6, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_7': xǁUStreamTVStreamWriterǁfetch__mutmut_7, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_8': xǁUStreamTVStreamWriterǁfetch__mutmut_8, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_9': xǁUStreamTVStreamWriterǁfetch__mutmut_9, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_10': xǁUStreamTVStreamWriterǁfetch__mutmut_10, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_11': xǁUStreamTVStreamWriterǁfetch__mutmut_11, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_12': xǁUStreamTVStreamWriterǁfetch__mutmut_12, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_13': xǁUStreamTVStreamWriterǁfetch__mutmut_13, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_14': xǁUStreamTVStreamWriterǁfetch__mutmut_14, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_15': xǁUStreamTVStreamWriterǁfetch__mutmut_15, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_16': xǁUStreamTVStreamWriterǁfetch__mutmut_16, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_17': xǁUStreamTVStreamWriterǁfetch__mutmut_17, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_18': xǁUStreamTVStreamWriterǁfetch__mutmut_18, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_19': xǁUStreamTVStreamWriterǁfetch__mutmut_19, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_20': xǁUStreamTVStreamWriterǁfetch__mutmut_20, 
        'xǁUStreamTVStreamWriterǁfetch__mutmut_21': xǁUStreamTVStreamWriterǁfetch__mutmut_21
    }
    
    def fetch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVStreamWriterǁfetch__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVStreamWriterǁfetch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    fetch.__signature__ = _mutmut_signature(xǁUStreamTVStreamWriterǁfetch__mutmut_orig)
    xǁUStreamTVStreamWriterǁfetch__mutmut_orig.__name__ = 'xǁUStreamTVStreamWriterǁfetch'

    def xǁUStreamTVStreamWriterǁwrite__mutmut_orig(self, segment: UStreamTVSegment, res: Response, *data):
        if self.closed:  # pragma: no cover
            return
        try:
            for chunk in res.iter_content(8192):
                self.reader.buffer.write(chunk)
            log.debug(f"Download of {self.stream.kind} segment {segment.num} complete")
        except OSError as err:
            log.error(f"Failed to read {self.stream.kind} segment {segment.num}: {err}")

    def xǁUStreamTVStreamWriterǁwrite__mutmut_1(self, segment: UStreamTVSegment, res: Response, *data):
        if self.closed:  # pragma: no cover
            return
        try:
            for chunk in res.iter_content(None):
                self.reader.buffer.write(chunk)
            log.debug(f"Download of {self.stream.kind} segment {segment.num} complete")
        except OSError as err:
            log.error(f"Failed to read {self.stream.kind} segment {segment.num}: {err}")

    def xǁUStreamTVStreamWriterǁwrite__mutmut_2(self, segment: UStreamTVSegment, res: Response, *data):
        if self.closed:  # pragma: no cover
            return
        try:
            for chunk in res.iter_content(8193):
                self.reader.buffer.write(chunk)
            log.debug(f"Download of {self.stream.kind} segment {segment.num} complete")
        except OSError as err:
            log.error(f"Failed to read {self.stream.kind} segment {segment.num}: {err}")

    def xǁUStreamTVStreamWriterǁwrite__mutmut_3(self, segment: UStreamTVSegment, res: Response, *data):
        if self.closed:  # pragma: no cover
            return
        try:
            for chunk in res.iter_content(8192):
                self.reader.buffer.write(None)
            log.debug(f"Download of {self.stream.kind} segment {segment.num} complete")
        except OSError as err:
            log.error(f"Failed to read {self.stream.kind} segment {segment.num}: {err}")

    def xǁUStreamTVStreamWriterǁwrite__mutmut_4(self, segment: UStreamTVSegment, res: Response, *data):
        if self.closed:  # pragma: no cover
            return
        try:
            for chunk in res.iter_content(8192):
                self.reader.buffer.write(chunk)
            log.debug(None)
        except OSError as err:
            log.error(f"Failed to read {self.stream.kind} segment {segment.num}: {err}")

    def xǁUStreamTVStreamWriterǁwrite__mutmut_5(self, segment: UStreamTVSegment, res: Response, *data):
        if self.closed:  # pragma: no cover
            return
        try:
            for chunk in res.iter_content(8192):
                self.reader.buffer.write(chunk)
            log.debug(f"Download of {self.stream.kind} segment {segment.num} complete")
        except OSError as err:
            log.error(None)
    
    xǁUStreamTVStreamWriterǁwrite__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVStreamWriterǁwrite__mutmut_1': xǁUStreamTVStreamWriterǁwrite__mutmut_1, 
        'xǁUStreamTVStreamWriterǁwrite__mutmut_2': xǁUStreamTVStreamWriterǁwrite__mutmut_2, 
        'xǁUStreamTVStreamWriterǁwrite__mutmut_3': xǁUStreamTVStreamWriterǁwrite__mutmut_3, 
        'xǁUStreamTVStreamWriterǁwrite__mutmut_4': xǁUStreamTVStreamWriterǁwrite__mutmut_4, 
        'xǁUStreamTVStreamWriterǁwrite__mutmut_5': xǁUStreamTVStreamWriterǁwrite__mutmut_5
    }
    
    def write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVStreamWriterǁwrite__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVStreamWriterǁwrite__mutmut_mutants"), args, kwargs, self)
        return result 
    
    write.__signature__ = _mutmut_signature(xǁUStreamTVStreamWriterǁwrite__mutmut_orig)
    xǁUStreamTVStreamWriterǁwrite__mutmut_orig.__name__ = 'xǁUStreamTVStreamWriterǁwrite'


class UStreamTVStreamWorker(SegmentedStreamWorker[UStreamTVSegment, Response]):
    reader: UStreamTVStreamReader
    writer: UStreamTVStreamWriter
    stream: UStreamTVStream

    def xǁUStreamTVStreamWorkerǁ__init____mutmut_orig(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wsclient = self.stream.wsclient
        self.segment_id = self.wsclient.stream_initial_id
        self.queue = self.wsclient.segments_subscribe()

    def xǁUStreamTVStreamWorkerǁ__init____mutmut_1(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.wsclient = self.stream.wsclient
        self.segment_id = self.wsclient.stream_initial_id
        self.queue = self.wsclient.segments_subscribe()

    def xǁUStreamTVStreamWorkerǁ__init____mutmut_2(self, *args, **kwargs):
        super().__init__(*args, )
        self.wsclient = self.stream.wsclient
        self.segment_id = self.wsclient.stream_initial_id
        self.queue = self.wsclient.segments_subscribe()

    def xǁUStreamTVStreamWorkerǁ__init____mutmut_3(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wsclient = None
        self.segment_id = self.wsclient.stream_initial_id
        self.queue = self.wsclient.segments_subscribe()

    def xǁUStreamTVStreamWorkerǁ__init____mutmut_4(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wsclient = self.stream.wsclient
        self.segment_id = None
        self.queue = self.wsclient.segments_subscribe()

    def xǁUStreamTVStreamWorkerǁ__init____mutmut_5(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wsclient = self.stream.wsclient
        self.segment_id = self.wsclient.stream_initial_id
        self.queue = None
    
    xǁUStreamTVStreamWorkerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVStreamWorkerǁ__init____mutmut_1': xǁUStreamTVStreamWorkerǁ__init____mutmut_1, 
        'xǁUStreamTVStreamWorkerǁ__init____mutmut_2': xǁUStreamTVStreamWorkerǁ__init____mutmut_2, 
        'xǁUStreamTVStreamWorkerǁ__init____mutmut_3': xǁUStreamTVStreamWorkerǁ__init____mutmut_3, 
        'xǁUStreamTVStreamWorkerǁ__init____mutmut_4': xǁUStreamTVStreamWorkerǁ__init____mutmut_4, 
        'xǁUStreamTVStreamWorkerǁ__init____mutmut_5': xǁUStreamTVStreamWorkerǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVStreamWorkerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVStreamWorkerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁUStreamTVStreamWorkerǁ__init____mutmut_orig)
    xǁUStreamTVStreamWorkerǁ__init____mutmut_orig.__name__ = 'xǁUStreamTVStreamWorkerǁ__init__'

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_orig(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_1(self):
        duration = None
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_2(self):
        duration = 5001
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_3(self):
        duration = 5000
        while self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_4(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = None
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_5(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = None
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_6(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(None):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_7(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration * 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_8(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1001 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_9(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 * 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_10(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 3):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_11(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    break

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_12(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num <= self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_13(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                break

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_14(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(None)
            yield segment
            self.segment_id = segment.num + 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_15(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = None

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_16(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num - 1

    def xǁUStreamTVStreamWorkerǁiter_segments__mutmut_17(self):
        duration = 5000
        while not self.closed:
            try:
                with self.wsclient.stream_segments_lock:
                    segment = self.queue.popleft()
                    duration = segment.duration
            except IndexError:
                # wait for new segments to be queued (half the last segment's duration in seconds)
                if self.wait(duration / 1000 / 2):
                    continue

            if self.closed:
                return

            if segment.num < self.segment_id:
                continue

            log.debug(f"Adding {self.stream.kind} segment {segment.num} to queue")
            yield segment
            self.segment_id = segment.num + 2
    
    xǁUStreamTVStreamWorkerǁiter_segments__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_1': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_1, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_2': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_2, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_3': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_3, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_4': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_4, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_5': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_5, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_6': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_6, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_7': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_7, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_8': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_8, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_9': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_9, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_10': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_10, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_11': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_11, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_12': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_12, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_13': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_13, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_14': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_14, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_15': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_15, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_16': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_16, 
        'xǁUStreamTVStreamWorkerǁiter_segments__mutmut_17': xǁUStreamTVStreamWorkerǁiter_segments__mutmut_17
    }
    
    def iter_segments(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁUStreamTVStreamWorkerǁiter_segments__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVStreamWorkerǁiter_segments__mutmut_mutants"), args, kwargs, self)
        return result 
    
    iter_segments.__signature__ = _mutmut_signature(xǁUStreamTVStreamWorkerǁiter_segments__mutmut_orig)
    xǁUStreamTVStreamWorkerǁiter_segments__mutmut_orig.__name__ = 'xǁUStreamTVStreamWorkerǁiter_segments'


class UStreamTVStreamReader(SegmentedStreamReader[UStreamTVSegment, Response]):
    __worker__ = UStreamTVStreamWorker
    __writer__ = UStreamTVStreamWriter

    stream: UStreamTVStream
    worker: UStreamTVStreamWorker
    writer: UStreamTVStreamWriter

    def open(self):
        self.stream.wsclient.opened.set()
        super().open()

    def close(self):
        super().close()
        self.stream.wsclient.close()


class UStreamTVStream(Stream):
    __shortname__ = "ustreamtv"

    def xǁUStreamTVStreamǁ__init____mutmut_orig(
        self,
        session,
        kind: str,
        wsclient: UStreamTVWsClient,
        stream_format: StreamFormatVideo | StreamFormatAudio,
    ):
        super().__init__(session)
        self.kind = kind
        self.wsclient = wsclient
        self.stream_format = stream_format

    def xǁUStreamTVStreamǁ__init____mutmut_1(
        self,
        session,
        kind: str,
        wsclient: UStreamTVWsClient,
        stream_format: StreamFormatVideo | StreamFormatAudio,
    ):
        super().__init__(None)
        self.kind = kind
        self.wsclient = wsclient
        self.stream_format = stream_format

    def xǁUStreamTVStreamǁ__init____mutmut_2(
        self,
        session,
        kind: str,
        wsclient: UStreamTVWsClient,
        stream_format: StreamFormatVideo | StreamFormatAudio,
    ):
        super().__init__(session)
        self.kind = None
        self.wsclient = wsclient
        self.stream_format = stream_format

    def xǁUStreamTVStreamǁ__init____mutmut_3(
        self,
        session,
        kind: str,
        wsclient: UStreamTVWsClient,
        stream_format: StreamFormatVideo | StreamFormatAudio,
    ):
        super().__init__(session)
        self.kind = kind
        self.wsclient = None
        self.stream_format = stream_format

    def xǁUStreamTVStreamǁ__init____mutmut_4(
        self,
        session,
        kind: str,
        wsclient: UStreamTVWsClient,
        stream_format: StreamFormatVideo | StreamFormatAudio,
    ):
        super().__init__(session)
        self.kind = kind
        self.wsclient = wsclient
        self.stream_format = None
    
    xǁUStreamTVStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVStreamǁ__init____mutmut_1': xǁUStreamTVStreamǁ__init____mutmut_1, 
        'xǁUStreamTVStreamǁ__init____mutmut_2': xǁUStreamTVStreamǁ__init____mutmut_2, 
        'xǁUStreamTVStreamǁ__init____mutmut_3': xǁUStreamTVStreamǁ__init____mutmut_3, 
        'xǁUStreamTVStreamǁ__init____mutmut_4': xǁUStreamTVStreamǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁUStreamTVStreamǁ__init____mutmut_orig)
    xǁUStreamTVStreamǁ__init____mutmut_orig.__name__ = 'xǁUStreamTVStreamǁ__init__'

    def xǁUStreamTVStreamǁopen__mutmut_orig(self):
        reader = UStreamTVStreamReader(self)
        reader.open()

        return reader

    def xǁUStreamTVStreamǁopen__mutmut_1(self):
        reader = None
        reader.open()

        return reader

    def xǁUStreamTVStreamǁopen__mutmut_2(self):
        reader = UStreamTVStreamReader(None)
        reader.open()

        return reader
    
    xǁUStreamTVStreamǁopen__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUStreamTVStreamǁopen__mutmut_1': xǁUStreamTVStreamǁopen__mutmut_1, 
        'xǁUStreamTVStreamǁopen__mutmut_2': xǁUStreamTVStreamǁopen__mutmut_2
    }
    
    def open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUStreamTVStreamǁopen__mutmut_orig"), object.__getattribute__(self, "xǁUStreamTVStreamǁopen__mutmut_mutants"), args, kwargs, self)
        return result 
    
    open.__signature__ = _mutmut_signature(xǁUStreamTVStreamǁopen__mutmut_orig)
    xǁUStreamTVStreamǁopen__mutmut_orig.__name__ = 'xǁUStreamTVStreamǁopen'


@pluginmatcher(
    re.compile(
        r"""
            https?://(?:(?:www\.)?ustream\.tv|video\.ibm\.com)
            (?:
                /combined-embed
                /(?P<combined_channel_id>\d+)
                (?:/video/(?P<combined_video_id>\d+))?
                |
                (?:(?:/embed/|/channel/(?:id/)?)(?P<channel_id>\d+))?
                (?:(?:/embed)?/recorded/(?P<video_id>\d+))?
            )
        """,
        re.VERBOSE,
    ),
)
@pluginargument(
    "password",
    sensitive=True,
    argument_name="ustream-password",
    metavar="PASSWORD",
    help="A password to access password protected UStream.tv channels.",
)
class UStreamTV(Plugin):
    STREAM_READY_TIMEOUT = 15

    def _get_media_app(self):
        video_id = self.match.group("video_id") or self.match.group("combined_video_id")
        if video_id:
            return video_id, "recorded"

        channel_id = self.match.group("channel_id") or self.match.group("combined_channel_id")
        if not channel_id:
            channel_id = self.session.http.get(
                self.url,
                headers={"User-Agent": useragents.CHROME},
                schema=validate.Schema(
                    validate.parse_html(),
                    validate.xml_xpath_string(".//meta[@name='ustream:channel_id'][@content][1]/@content"),
                ),
            )

        return channel_id, "channel"

    def _get_streams(self):
        if not MuxedStream.is_usable(self.session):
            return

        media_id, application = self._get_media_app()
        if not media_id:
            return

        wsclient = UStreamTVWsClient(
            self.session,
            media_id,
            application,
            referrer=self.url,
            cluster="live",
            password=self.get_option("password"),
        )
        log.debug(
            "Connecting to UStream API: "
            + ", ".join([
                f"media_id={media_id}",
                f"application={application}",
                f"referrer={self.url}",
                f"cluster={'live'}",
            ]),
        )
        wsclient.start()

        log.debug(f"Waiting for stream data (for at most {self.STREAM_READY_TIMEOUT} seconds)...")
        if (
            not wsclient.ready.wait(self.STREAM_READY_TIMEOUT)
            or not wsclient.is_alive()
            or wsclient.stream_error
        ):  # fmt: skip
            log.error(wsclient.stream_error or "Waiting for stream data timed out.")
            wsclient.close()
            return

        if not wsclient.stream_formats_audio:
            for video in wsclient.stream_formats_video:
                yield f"{video.height}p", UStreamTVStream(self.session, "video", wsclient, video)
        else:
            for video in wsclient.stream_formats_video:
                for audio in wsclient.stream_formats_audio:
                    yield (
                        f"{video.height}p+a{audio.bitrate}k",
                        MuxedStream(
                            self.session,
                            UStreamTVStream(self.session, "video", wsclient, video),
                            UStreamTVStream(self.session, "audio", wsclient, audio),
                        ),
                    )


__plugin__ = UStreamTV

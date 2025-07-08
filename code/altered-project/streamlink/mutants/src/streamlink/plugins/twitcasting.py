"""
$description Global live broadcasting and live broadcast archiving social platform.
$url twitcasting.tv
$type live
$metadata id
"""

import hashlib
import logging
import re
import sys

from streamlink.buffers import RingBuffer
from streamlink.plugin import Plugin, pluginargument, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.plugin.api.websocket import WebsocketClient
from streamlink.stream.hls import HLSStream
from streamlink.stream.stream import Stream, StreamIO
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
    re.compile(r"https?://twitcasting\.tv/(?P<channel>[^/]+)"),
)
@pluginargument(
    "password",
    sensitive=True,
    metavar="PASSWORD",
    help="Password for private Twitcasting streams.",
)
class TwitCasting(Plugin):
    _URL_API_STREAMSERVER = "https://twitcasting.tv/streamserver.php"

    # prefer websocket streams over HLS streams due to latency reasons
    _WEIGHTS = {
        "ws_main": sys.maxsize,
        "ws_mobilesource": sys.maxsize - 1,
        "ws_base": sys.maxsize - 2,
        "hls_high": sys.maxsize - 10,
        "hls_medium": sys.maxsize - 11,
        "hls_low": sys.maxsize - 12,
    }

    @classmethod
    def stream_weight(cls, stream):
        return (cls._WEIGHTS[stream], "none") if stream in cls._WEIGHTS else super().stream_weight(stream)

    def _api_query_streamserver(self):
        return self.session.http.get(
            self._URL_API_STREAMSERVER,
            params={
                "target": self.match["channel"],
                "mode": "client",
                "player": "pc_web",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {
                    validate.optional("movie"): {
                        "id": int,
                        "live": bool,
                    },
                    validate.optional("llfmp4"): {
                        "streams": {
                            str: validate.url(),
                        },
                    },
                    validate.optional("tc-hls"): {
                        "streams": {
                            str: validate.url(),
                        },
                    },
                },
                validate.union_get("movie", "llfmp4", "tc-hls"),
            ),
        )

    def _get_streams_hls(self, streams, params=None):
        for name, url in streams.items():
            yield f"hls_{name}", HLSStream(self.session, url, params=params)

    def _get_streams_websocket(self, streams, params=None):
        for name, url in streams.items():
            yield f"ws_{name}", TwitCastingStream(self.session, url, params=params)

    def _get_streams(self):
        movie, websocket, hls = self._api_query_streamserver()
        if not movie or not movie.get("id") or not movie.get("live"):
            log.error(f"No live stream available for user {self.match['channel']}")
            return
        if not websocket and not hls:
            log.error("Unsupported stream type")
            return

        self.id = movie.get("id")

        params = {}
        if password := self.options.get("password"):
            params |= {"word": hashlib.md5(password.encode()).hexdigest()}

        if websocket:
            yield from self._get_streams_websocket(websocket["streams"], params)
        if hls:
            yield from self._get_streams_hls(hls["streams"], params)


class TwitCastingWsClient(WebsocketClient):
    def xǁTwitCastingWsClientǁ__init____mutmut_orig(self, buffer: RingBuffer, *args, **kwargs):
        self.buffer = buffer
        super().__init__(*args, **kwargs)
    def xǁTwitCastingWsClientǁ__init____mutmut_1(self, buffer: RingBuffer, *args, **kwargs):
        self.buffer = None
        super().__init__(*args, **kwargs)
    def xǁTwitCastingWsClientǁ__init____mutmut_2(self, buffer: RingBuffer, *args, **kwargs):
        self.buffer = buffer
        super().__init__(**kwargs)
    def xǁTwitCastingWsClientǁ__init____mutmut_3(self, buffer: RingBuffer, *args, **kwargs):
        self.buffer = buffer
        super().__init__(*args, )
    
    xǁTwitCastingWsClientǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTwitCastingWsClientǁ__init____mutmut_1': xǁTwitCastingWsClientǁ__init____mutmut_1, 
        'xǁTwitCastingWsClientǁ__init____mutmut_2': xǁTwitCastingWsClientǁ__init____mutmut_2, 
        'xǁTwitCastingWsClientǁ__init____mutmut_3': xǁTwitCastingWsClientǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTwitCastingWsClientǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTwitCastingWsClientǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTwitCastingWsClientǁ__init____mutmut_orig)
    xǁTwitCastingWsClientǁ__init____mutmut_orig.__name__ = 'xǁTwitCastingWsClientǁ__init__'

    def xǁTwitCastingWsClientǁon_close__mutmut_orig(self, *args, **kwargs):
        super().on_close(*args, **kwargs)
        self.buffer.close()

    def xǁTwitCastingWsClientǁon_close__mutmut_1(self, *args, **kwargs):
        super().on_close(**kwargs)
        self.buffer.close()

    def xǁTwitCastingWsClientǁon_close__mutmut_2(self, *args, **kwargs):
        super().on_close(*args, )
        self.buffer.close()
    
    xǁTwitCastingWsClientǁon_close__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTwitCastingWsClientǁon_close__mutmut_1': xǁTwitCastingWsClientǁon_close__mutmut_1, 
        'xǁTwitCastingWsClientǁon_close__mutmut_2': xǁTwitCastingWsClientǁon_close__mutmut_2
    }
    
    def on_close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTwitCastingWsClientǁon_close__mutmut_orig"), object.__getattribute__(self, "xǁTwitCastingWsClientǁon_close__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_close.__signature__ = _mutmut_signature(xǁTwitCastingWsClientǁon_close__mutmut_orig)
    xǁTwitCastingWsClientǁon_close__mutmut_orig.__name__ = 'xǁTwitCastingWsClientǁon_close'

    def xǁTwitCastingWsClientǁon_data__mutmut_orig(self, wsapp, data, data_type, cont):
        if data_type == self.OPCODE_TEXT:
            return

        try:
            self.buffer.write(data)
        except Exception as err:
            log.error(err)
            self.close()

    def xǁTwitCastingWsClientǁon_data__mutmut_1(self, wsapp, data, data_type, cont):
        if data_type != self.OPCODE_TEXT:
            return

        try:
            self.buffer.write(data)
        except Exception as err:
            log.error(err)
            self.close()

    def xǁTwitCastingWsClientǁon_data__mutmut_2(self, wsapp, data, data_type, cont):
        if data_type == self.OPCODE_TEXT:
            return

        try:
            self.buffer.write(None)
        except Exception as err:
            log.error(err)
            self.close()

    def xǁTwitCastingWsClientǁon_data__mutmut_3(self, wsapp, data, data_type, cont):
        if data_type == self.OPCODE_TEXT:
            return

        try:
            self.buffer.write(data)
        except Exception as err:
            log.error(None)
            self.close()
    
    xǁTwitCastingWsClientǁon_data__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTwitCastingWsClientǁon_data__mutmut_1': xǁTwitCastingWsClientǁon_data__mutmut_1, 
        'xǁTwitCastingWsClientǁon_data__mutmut_2': xǁTwitCastingWsClientǁon_data__mutmut_2, 
        'xǁTwitCastingWsClientǁon_data__mutmut_3': xǁTwitCastingWsClientǁon_data__mutmut_3
    }
    
    def on_data(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTwitCastingWsClientǁon_data__mutmut_orig"), object.__getattribute__(self, "xǁTwitCastingWsClientǁon_data__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_data.__signature__ = _mutmut_signature(xǁTwitCastingWsClientǁon_data__mutmut_orig)
    xǁTwitCastingWsClientǁon_data__mutmut_orig.__name__ = 'xǁTwitCastingWsClientǁon_data'


class TwitCastingReader(StreamIO):
    def xǁTwitCastingReaderǁ__init____mutmut_orig(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_1(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = None
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_2(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = None
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_3(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = None

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_4(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout and self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_5(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get(None)

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_6(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("XXstream-timeoutXX")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_7(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("STREAM-TIMEOUT")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_8(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("Stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_9(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = None
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_10(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option(None)
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_11(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("XXringbuffer-sizeXX")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_12(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("RINGBUFFER-SIZE")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_13(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("Ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_14(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = None

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_15(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(None)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_16(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = None
    def xǁTwitCastingReaderǁ__init____mutmut_17(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            None,
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_18(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            None,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_19(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            None,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_20(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin=None,
        )
    def xǁTwitCastingReaderǁ__init____mutmut_21(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            stream.session,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_22(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.url,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_23(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            origin="https://twitcasting.tv/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_24(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            )
    def xǁTwitCastingReaderǁ__init____mutmut_25(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="XXhttps://twitcasting.tv/XX",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_26(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="HTTPS://TWITCASTING.TV/",
        )
    def xǁTwitCastingReaderǁ__init____mutmut_27(self, stream: "TwitCastingStream", timeout=None):
        super().__init__()
        self.session = stream.session
        self.stream = stream
        self.timeout = timeout or self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.wsclient = TwitCastingWsClient(
            self.buffer,
            stream.session,
            stream.url,
            origin="Https://twitcasting.tv/",
        )
    
    xǁTwitCastingReaderǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTwitCastingReaderǁ__init____mutmut_1': xǁTwitCastingReaderǁ__init____mutmut_1, 
        'xǁTwitCastingReaderǁ__init____mutmut_2': xǁTwitCastingReaderǁ__init____mutmut_2, 
        'xǁTwitCastingReaderǁ__init____mutmut_3': xǁTwitCastingReaderǁ__init____mutmut_3, 
        'xǁTwitCastingReaderǁ__init____mutmut_4': xǁTwitCastingReaderǁ__init____mutmut_4, 
        'xǁTwitCastingReaderǁ__init____mutmut_5': xǁTwitCastingReaderǁ__init____mutmut_5, 
        'xǁTwitCastingReaderǁ__init____mutmut_6': xǁTwitCastingReaderǁ__init____mutmut_6, 
        'xǁTwitCastingReaderǁ__init____mutmut_7': xǁTwitCastingReaderǁ__init____mutmut_7, 
        'xǁTwitCastingReaderǁ__init____mutmut_8': xǁTwitCastingReaderǁ__init____mutmut_8, 
        'xǁTwitCastingReaderǁ__init____mutmut_9': xǁTwitCastingReaderǁ__init____mutmut_9, 
        'xǁTwitCastingReaderǁ__init____mutmut_10': xǁTwitCastingReaderǁ__init____mutmut_10, 
        'xǁTwitCastingReaderǁ__init____mutmut_11': xǁTwitCastingReaderǁ__init____mutmut_11, 
        'xǁTwitCastingReaderǁ__init____mutmut_12': xǁTwitCastingReaderǁ__init____mutmut_12, 
        'xǁTwitCastingReaderǁ__init____mutmut_13': xǁTwitCastingReaderǁ__init____mutmut_13, 
        'xǁTwitCastingReaderǁ__init____mutmut_14': xǁTwitCastingReaderǁ__init____mutmut_14, 
        'xǁTwitCastingReaderǁ__init____mutmut_15': xǁTwitCastingReaderǁ__init____mutmut_15, 
        'xǁTwitCastingReaderǁ__init____mutmut_16': xǁTwitCastingReaderǁ__init____mutmut_16, 
        'xǁTwitCastingReaderǁ__init____mutmut_17': xǁTwitCastingReaderǁ__init____mutmut_17, 
        'xǁTwitCastingReaderǁ__init____mutmut_18': xǁTwitCastingReaderǁ__init____mutmut_18, 
        'xǁTwitCastingReaderǁ__init____mutmut_19': xǁTwitCastingReaderǁ__init____mutmut_19, 
        'xǁTwitCastingReaderǁ__init____mutmut_20': xǁTwitCastingReaderǁ__init____mutmut_20, 
        'xǁTwitCastingReaderǁ__init____mutmut_21': xǁTwitCastingReaderǁ__init____mutmut_21, 
        'xǁTwitCastingReaderǁ__init____mutmut_22': xǁTwitCastingReaderǁ__init____mutmut_22, 
        'xǁTwitCastingReaderǁ__init____mutmut_23': xǁTwitCastingReaderǁ__init____mutmut_23, 
        'xǁTwitCastingReaderǁ__init____mutmut_24': xǁTwitCastingReaderǁ__init____mutmut_24, 
        'xǁTwitCastingReaderǁ__init____mutmut_25': xǁTwitCastingReaderǁ__init____mutmut_25, 
        'xǁTwitCastingReaderǁ__init____mutmut_26': xǁTwitCastingReaderǁ__init____mutmut_26, 
        'xǁTwitCastingReaderǁ__init____mutmut_27': xǁTwitCastingReaderǁ__init____mutmut_27
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTwitCastingReaderǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTwitCastingReaderǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTwitCastingReaderǁ__init____mutmut_orig)
    xǁTwitCastingReaderǁ__init____mutmut_orig.__name__ = 'xǁTwitCastingReaderǁ__init__'

    def open(self):
        self.wsclient.start()

    def close(self):
        self.wsclient.close()
        self.buffer.close()

    def xǁTwitCastingReaderǁread__mutmut_orig(self, size):
        return self.buffer.read(
            size,
            block=self.wsclient.is_alive(),
            timeout=self.timeout,
        )

    def xǁTwitCastingReaderǁread__mutmut_1(self, size):
        return self.buffer.read(
            None,
            block=self.wsclient.is_alive(),
            timeout=self.timeout,
        )

    def xǁTwitCastingReaderǁread__mutmut_2(self, size):
        return self.buffer.read(
            size,
            block=None,
            timeout=self.timeout,
        )

    def xǁTwitCastingReaderǁread__mutmut_3(self, size):
        return self.buffer.read(
            size,
            block=self.wsclient.is_alive(),
            timeout=None,
        )

    def xǁTwitCastingReaderǁread__mutmut_4(self, size):
        return self.buffer.read(
            block=self.wsclient.is_alive(),
            timeout=self.timeout,
        )

    def xǁTwitCastingReaderǁread__mutmut_5(self, size):
        return self.buffer.read(
            size,
            timeout=self.timeout,
        )

    def xǁTwitCastingReaderǁread__mutmut_6(self, size):
        return self.buffer.read(
            size,
            block=self.wsclient.is_alive(),
            )
    
    xǁTwitCastingReaderǁread__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTwitCastingReaderǁread__mutmut_1': xǁTwitCastingReaderǁread__mutmut_1, 
        'xǁTwitCastingReaderǁread__mutmut_2': xǁTwitCastingReaderǁread__mutmut_2, 
        'xǁTwitCastingReaderǁread__mutmut_3': xǁTwitCastingReaderǁread__mutmut_3, 
        'xǁTwitCastingReaderǁread__mutmut_4': xǁTwitCastingReaderǁread__mutmut_4, 
        'xǁTwitCastingReaderǁread__mutmut_5': xǁTwitCastingReaderǁread__mutmut_5, 
        'xǁTwitCastingReaderǁread__mutmut_6': xǁTwitCastingReaderǁread__mutmut_6
    }
    
    def read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTwitCastingReaderǁread__mutmut_orig"), object.__getattribute__(self, "xǁTwitCastingReaderǁread__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read.__signature__ = _mutmut_signature(xǁTwitCastingReaderǁread__mutmut_orig)
    xǁTwitCastingReaderǁread__mutmut_orig.__name__ = 'xǁTwitCastingReaderǁread'


class TwitCastingStream(Stream):
    __shortname__ = "websocket"

    def xǁTwitCastingStreamǁ__init____mutmut_orig(self, session, url, params):
        super().__init__(session)
        self.url = update_qsd(url, params or {})

    def xǁTwitCastingStreamǁ__init____mutmut_1(self, session, url, params):
        super().__init__(None)
        self.url = update_qsd(url, params or {})

    def xǁTwitCastingStreamǁ__init____mutmut_2(self, session, url, params):
        super().__init__(session)
        self.url = None

    def xǁTwitCastingStreamǁ__init____mutmut_3(self, session, url, params):
        super().__init__(session)
        self.url = update_qsd(None, params or {})

    def xǁTwitCastingStreamǁ__init____mutmut_4(self, session, url, params):
        super().__init__(session)
        self.url = update_qsd(url, None)

    def xǁTwitCastingStreamǁ__init____mutmut_5(self, session, url, params):
        super().__init__(session)
        self.url = update_qsd(params or {})

    def xǁTwitCastingStreamǁ__init____mutmut_6(self, session, url, params):
        super().__init__(session)
        self.url = update_qsd(url, )

    def xǁTwitCastingStreamǁ__init____mutmut_7(self, session, url, params):
        super().__init__(session)
        self.url = update_qsd(url, params and {})
    
    xǁTwitCastingStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTwitCastingStreamǁ__init____mutmut_1': xǁTwitCastingStreamǁ__init____mutmut_1, 
        'xǁTwitCastingStreamǁ__init____mutmut_2': xǁTwitCastingStreamǁ__init____mutmut_2, 
        'xǁTwitCastingStreamǁ__init____mutmut_3': xǁTwitCastingStreamǁ__init____mutmut_3, 
        'xǁTwitCastingStreamǁ__init____mutmut_4': xǁTwitCastingStreamǁ__init____mutmut_4, 
        'xǁTwitCastingStreamǁ__init____mutmut_5': xǁTwitCastingStreamǁ__init____mutmut_5, 
        'xǁTwitCastingStreamǁ__init____mutmut_6': xǁTwitCastingStreamǁ__init____mutmut_6, 
        'xǁTwitCastingStreamǁ__init____mutmut_7': xǁTwitCastingStreamǁ__init____mutmut_7
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTwitCastingStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTwitCastingStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTwitCastingStreamǁ__init____mutmut_orig)
    xǁTwitCastingStreamǁ__init____mutmut_orig.__name__ = 'xǁTwitCastingStreamǁ__init__'

    def to_url(self):
        return self.url

    def xǁTwitCastingStreamǁopen__mutmut_orig(self):
        reader = TwitCastingReader(self)
        reader.open()
        return reader

    def xǁTwitCastingStreamǁopen__mutmut_1(self):
        reader = None
        reader.open()
        return reader

    def xǁTwitCastingStreamǁopen__mutmut_2(self):
        reader = TwitCastingReader(None)
        reader.open()
        return reader
    
    xǁTwitCastingStreamǁopen__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTwitCastingStreamǁopen__mutmut_1': xǁTwitCastingStreamǁopen__mutmut_1, 
        'xǁTwitCastingStreamǁopen__mutmut_2': xǁTwitCastingStreamǁopen__mutmut_2
    }
    
    def open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTwitCastingStreamǁopen__mutmut_orig"), object.__getattribute__(self, "xǁTwitCastingStreamǁopen__mutmut_mutants"), args, kwargs, self)
        return result 
    
    open.__signature__ = _mutmut_signature(xǁTwitCastingStreamǁopen__mutmut_orig)
    xǁTwitCastingStreamǁopen__mutmut_orig.__name__ = 'xǁTwitCastingStreamǁopen'


__plugin__ = TwitCasting

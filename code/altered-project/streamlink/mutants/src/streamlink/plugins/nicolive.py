"""
$description Japanese live-streaming and video hosting social platform.
$url live.nicovideo.jp
$type live, vod
$metadata id
$metadata author
$metadata title
$account Required by some streams
$notes Timeshift is supported
"""

from __future__ import annotations

import logging
import re
from threading import Event
from urllib.parse import urljoin

from streamlink.plugin import Plugin, pluginargument, pluginmatcher
from streamlink.plugin.api import useragents, validate
from streamlink.plugin.api.websocket import WebsocketClient
from streamlink.stream.hls import HLSSegment, HLSStream, HLSStreamReader, HLSStreamWriter
from streamlink.utils.parse import parse_json
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


class NicoLiveWsClient(WebsocketClient):
    STREAM_OPENED_TIMEOUT = 6

    ready: Event
    opened: Event
    hls_stream_url: str

    _SCHEMA_COOKIES = validate.Schema(
        [
            {
                "domain": str,
                "path": str,
                "name": str,
                "value": str,
                "secure": bool,
            },
        ],
    )

    def xǁNicoLiveWsClientǁ__init____mutmut_orig(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.opened = Event()
        self.ready = Event()

    def xǁNicoLiveWsClientǁ__init____mutmut_1(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.opened = Event()
        self.ready = Event()

    def xǁNicoLiveWsClientǁ__init____mutmut_2(self, *args, **kwargs):
        super().__init__(*args, )
        self.opened = Event()
        self.ready = Event()

    def xǁNicoLiveWsClientǁ__init____mutmut_3(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.opened = None
        self.ready = Event()

    def xǁNicoLiveWsClientǁ__init____mutmut_4(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.opened = Event()
        self.ready = None
    
    xǁNicoLiveWsClientǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNicoLiveWsClientǁ__init____mutmut_1': xǁNicoLiveWsClientǁ__init____mutmut_1, 
        'xǁNicoLiveWsClientǁ__init____mutmut_2': xǁNicoLiveWsClientǁ__init____mutmut_2, 
        'xǁNicoLiveWsClientǁ__init____mutmut_3': xǁNicoLiveWsClientǁ__init____mutmut_3, 
        'xǁNicoLiveWsClientǁ__init____mutmut_4': xǁNicoLiveWsClientǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNicoLiveWsClientǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁNicoLiveWsClientǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁNicoLiveWsClientǁ__init____mutmut_orig)
    xǁNicoLiveWsClientǁ__init____mutmut_orig.__name__ = 'xǁNicoLiveWsClientǁ__init__'

    def xǁNicoLiveWsClientǁon_open__mutmut_orig(self, wsapp):
        super().on_open(wsapp)
        self.send_playerversion()
        self.send_getpermit()

    def xǁNicoLiveWsClientǁon_open__mutmut_1(self, wsapp):
        super().on_open(None)
        self.send_playerversion()
        self.send_getpermit()
    
    xǁNicoLiveWsClientǁon_open__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNicoLiveWsClientǁon_open__mutmut_1': xǁNicoLiveWsClientǁon_open__mutmut_1
    }
    
    def on_open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNicoLiveWsClientǁon_open__mutmut_orig"), object.__getattribute__(self, "xǁNicoLiveWsClientǁon_open__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_open.__signature__ = _mutmut_signature(xǁNicoLiveWsClientǁon_open__mutmut_orig)
    xǁNicoLiveWsClientǁon_open__mutmut_orig.__name__ = 'xǁNicoLiveWsClientǁon_open'

    def xǁNicoLiveWsClientǁon_message__mutmut_orig(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_1(self, wsapp, data: str):
        log.debug(None)
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_2(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = None
        msgtype = message.get("type")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_3(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(None)
        msgtype = message.get("type")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_4(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = None
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_5(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get(None)
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_6(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("XXtypeXX")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_7(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("TYPE")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_8(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("Type")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_9(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = None

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_10(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get(None, {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_11(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("data", None)

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_12(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get({})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_13(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("data", )

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_14(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("XXdataXX", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_15(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("DATA", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_16(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("Data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_17(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(None):
            handler(self, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_18(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(None, msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_19(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, None)

    def xǁNicoLiveWsClientǁon_message__mutmut_20(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(msgdata)

    def xǁNicoLiveWsClientǁon_message__mutmut_21(self, wsapp, data: str):
        log.debug(f"Received: {data}")
        message = parse_json(data)
        msgtype = message.get("type")
        msgdata = message.get("data", {})

        if handler := self._MESSAGE_HANDLERS.get(msgtype):
            handler(self, )
    
    xǁNicoLiveWsClientǁon_message__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNicoLiveWsClientǁon_message__mutmut_1': xǁNicoLiveWsClientǁon_message__mutmut_1, 
        'xǁNicoLiveWsClientǁon_message__mutmut_2': xǁNicoLiveWsClientǁon_message__mutmut_2, 
        'xǁNicoLiveWsClientǁon_message__mutmut_3': xǁNicoLiveWsClientǁon_message__mutmut_3, 
        'xǁNicoLiveWsClientǁon_message__mutmut_4': xǁNicoLiveWsClientǁon_message__mutmut_4, 
        'xǁNicoLiveWsClientǁon_message__mutmut_5': xǁNicoLiveWsClientǁon_message__mutmut_5, 
        'xǁNicoLiveWsClientǁon_message__mutmut_6': xǁNicoLiveWsClientǁon_message__mutmut_6, 
        'xǁNicoLiveWsClientǁon_message__mutmut_7': xǁNicoLiveWsClientǁon_message__mutmut_7, 
        'xǁNicoLiveWsClientǁon_message__mutmut_8': xǁNicoLiveWsClientǁon_message__mutmut_8, 
        'xǁNicoLiveWsClientǁon_message__mutmut_9': xǁNicoLiveWsClientǁon_message__mutmut_9, 
        'xǁNicoLiveWsClientǁon_message__mutmut_10': xǁNicoLiveWsClientǁon_message__mutmut_10, 
        'xǁNicoLiveWsClientǁon_message__mutmut_11': xǁNicoLiveWsClientǁon_message__mutmut_11, 
        'xǁNicoLiveWsClientǁon_message__mutmut_12': xǁNicoLiveWsClientǁon_message__mutmut_12, 
        'xǁNicoLiveWsClientǁon_message__mutmut_13': xǁNicoLiveWsClientǁon_message__mutmut_13, 
        'xǁNicoLiveWsClientǁon_message__mutmut_14': xǁNicoLiveWsClientǁon_message__mutmut_14, 
        'xǁNicoLiveWsClientǁon_message__mutmut_15': xǁNicoLiveWsClientǁon_message__mutmut_15, 
        'xǁNicoLiveWsClientǁon_message__mutmut_16': xǁNicoLiveWsClientǁon_message__mutmut_16, 
        'xǁNicoLiveWsClientǁon_message__mutmut_17': xǁNicoLiveWsClientǁon_message__mutmut_17, 
        'xǁNicoLiveWsClientǁon_message__mutmut_18': xǁNicoLiveWsClientǁon_message__mutmut_18, 
        'xǁNicoLiveWsClientǁon_message__mutmut_19': xǁNicoLiveWsClientǁon_message__mutmut_19, 
        'xǁNicoLiveWsClientǁon_message__mutmut_20': xǁNicoLiveWsClientǁon_message__mutmut_20, 
        'xǁNicoLiveWsClientǁon_message__mutmut_21': xǁNicoLiveWsClientǁon_message__mutmut_21
    }
    
    def on_message(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNicoLiveWsClientǁon_message__mutmut_orig"), object.__getattribute__(self, "xǁNicoLiveWsClientǁon_message__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_message.__signature__ = _mutmut_signature(xǁNicoLiveWsClientǁon_message__mutmut_orig)
    xǁNicoLiveWsClientǁon_message__mutmut_orig.__name__ = 'xǁNicoLiveWsClientǁon_message'

    def on_message_ping(self, _data):
        self.send_pong()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_orig(self, data):
        reason = data.get("reason", "Unknown reason")
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_1(self, data):
        reason = None
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_2(self, data):
        reason = data.get(None, "Unknown reason")
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_3(self, data):
        reason = data.get("reason", None)
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_4(self, data):
        reason = data.get("Unknown reason")
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_5(self, data):
        reason = data.get("reason", )
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_6(self, data):
        reason = data.get("XXreasonXX", "Unknown reason")
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_7(self, data):
        reason = data.get("REASON", "Unknown reason")
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_8(self, data):
        reason = data.get("Reason", "Unknown reason")
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_9(self, data):
        reason = data.get("reason", "XXUnknown reasonXX")
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_10(self, data):
        reason = data.get("reason", "unknown reason")
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_11(self, data):
        reason = data.get("reason", "UNKNOWN REASON")
        log.info(f"Received disconnect message: {reason}")
        self.close()

    def xǁNicoLiveWsClientǁon_message_disconnect__mutmut_12(self, data):
        reason = data.get("reason", "Unknown reason")
        log.info(None)
        self.close()
    
    xǁNicoLiveWsClientǁon_message_disconnect__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_1': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_1, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_2': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_2, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_3': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_3, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_4': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_4, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_5': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_5, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_6': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_6, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_7': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_7, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_8': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_8, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_9': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_9, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_10': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_10, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_11': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_11, 
        'xǁNicoLiveWsClientǁon_message_disconnect__mutmut_12': xǁNicoLiveWsClientǁon_message_disconnect__mutmut_12
    }
    
    def on_message_disconnect(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNicoLiveWsClientǁon_message_disconnect__mutmut_orig"), object.__getattribute__(self, "xǁNicoLiveWsClientǁon_message_disconnect__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_message_disconnect.__signature__ = _mutmut_signature(xǁNicoLiveWsClientǁon_message_disconnect__mutmut_orig)
    xǁNicoLiveWsClientǁon_message_disconnect__mutmut_orig.__name__ = 'xǁNicoLiveWsClientǁon_message_disconnect'

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_orig(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_1(self, data):
        if data.get(None) != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_2(self, data):
        if data.get("XXprotocolXX") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_3(self, data):
        if data.get("PROTOCOL") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_4(self, data):
        if data.get("Protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_5(self, data):
        if data.get("protocol") == "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_6(self, data):
        if data.get("protocol") != "XXhlsXX" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_7(self, data):
        if data.get("protocol") != "HLS" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_8(self, data):
        if data.get("protocol") != "Hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_9(self, data):
        if data.get("protocol") != "hls" and not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_10(self, data):
        if data.get("protocol") != "hls" or data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_11(self, data):
        if data.get("protocol") != "hls" or not data.get(None):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_12(self, data):
        if data.get("protocol") != "hls" or not data.get("XXuriXX"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_13(self, data):
        if data.get("protocol") != "hls" or not data.get("URI"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_14(self, data):
        if data.get("protocol") != "hls" or not data.get("Uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_15(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get(None, []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_16(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", None):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_17(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get([]):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_18(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", ):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_19(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("XXcookiesXX", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_20(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("COOKIES", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_21(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("Cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_22(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(None):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_23(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = None
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_24(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get(None)
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_25(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("XXuriXX")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_26(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("URI")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_27(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("Uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_28(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(None):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_29(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug(None)
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_30(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("XXStream opened, keeping websocket connection aliveXX")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_31(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("stream opened, keeping websocket connection alive")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_32(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("STREAM OPENED, KEEPING WEBSOCKET CONNECTION ALIVE")
        else:
            log.info("Closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_33(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info(None)
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_34(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("XXClosing websocket connectionXX")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_35(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("closing websocket connection")
            self.close()

    def xǁNicoLiveWsClientǁon_message_stream__mutmut_36(self, data):
        if data.get("protocol") != "hls" or not data.get("uri"):
            return

        # cookies may be required by some HLS multivariant playlists
        if cookies := data.get("cookies", []):
            for cookie in self._SCHEMA_COOKIES.validate(cookies):
                self.session.http.cookies.set(**cookie)

        self.hls_stream_url = data.get("uri")
        self.ready.set()
        if self.opened.wait(self.STREAM_OPENED_TIMEOUT):
            log.debug("Stream opened, keeping websocket connection alive")
        else:
            log.info("CLOSING WEBSOCKET CONNECTION")
            self.close()
    
    xǁNicoLiveWsClientǁon_message_stream__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNicoLiveWsClientǁon_message_stream__mutmut_1': xǁNicoLiveWsClientǁon_message_stream__mutmut_1, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_2': xǁNicoLiveWsClientǁon_message_stream__mutmut_2, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_3': xǁNicoLiveWsClientǁon_message_stream__mutmut_3, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_4': xǁNicoLiveWsClientǁon_message_stream__mutmut_4, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_5': xǁNicoLiveWsClientǁon_message_stream__mutmut_5, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_6': xǁNicoLiveWsClientǁon_message_stream__mutmut_6, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_7': xǁNicoLiveWsClientǁon_message_stream__mutmut_7, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_8': xǁNicoLiveWsClientǁon_message_stream__mutmut_8, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_9': xǁNicoLiveWsClientǁon_message_stream__mutmut_9, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_10': xǁNicoLiveWsClientǁon_message_stream__mutmut_10, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_11': xǁNicoLiveWsClientǁon_message_stream__mutmut_11, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_12': xǁNicoLiveWsClientǁon_message_stream__mutmut_12, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_13': xǁNicoLiveWsClientǁon_message_stream__mutmut_13, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_14': xǁNicoLiveWsClientǁon_message_stream__mutmut_14, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_15': xǁNicoLiveWsClientǁon_message_stream__mutmut_15, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_16': xǁNicoLiveWsClientǁon_message_stream__mutmut_16, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_17': xǁNicoLiveWsClientǁon_message_stream__mutmut_17, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_18': xǁNicoLiveWsClientǁon_message_stream__mutmut_18, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_19': xǁNicoLiveWsClientǁon_message_stream__mutmut_19, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_20': xǁNicoLiveWsClientǁon_message_stream__mutmut_20, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_21': xǁNicoLiveWsClientǁon_message_stream__mutmut_21, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_22': xǁNicoLiveWsClientǁon_message_stream__mutmut_22, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_23': xǁNicoLiveWsClientǁon_message_stream__mutmut_23, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_24': xǁNicoLiveWsClientǁon_message_stream__mutmut_24, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_25': xǁNicoLiveWsClientǁon_message_stream__mutmut_25, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_26': xǁNicoLiveWsClientǁon_message_stream__mutmut_26, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_27': xǁNicoLiveWsClientǁon_message_stream__mutmut_27, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_28': xǁNicoLiveWsClientǁon_message_stream__mutmut_28, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_29': xǁNicoLiveWsClientǁon_message_stream__mutmut_29, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_30': xǁNicoLiveWsClientǁon_message_stream__mutmut_30, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_31': xǁNicoLiveWsClientǁon_message_stream__mutmut_31, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_32': xǁNicoLiveWsClientǁon_message_stream__mutmut_32, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_33': xǁNicoLiveWsClientǁon_message_stream__mutmut_33, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_34': xǁNicoLiveWsClientǁon_message_stream__mutmut_34, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_35': xǁNicoLiveWsClientǁon_message_stream__mutmut_35, 
        'xǁNicoLiveWsClientǁon_message_stream__mutmut_36': xǁNicoLiveWsClientǁon_message_stream__mutmut_36
    }
    
    def on_message_stream(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNicoLiveWsClientǁon_message_stream__mutmut_orig"), object.__getattribute__(self, "xǁNicoLiveWsClientǁon_message_stream__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_message_stream.__signature__ = _mutmut_signature(xǁNicoLiveWsClientǁon_message_stream__mutmut_orig)
    xǁNicoLiveWsClientǁon_message_stream__mutmut_orig.__name__ = 'xǁNicoLiveWsClientǁon_message_stream'

    _MESSAGE_HANDLERS = {
        "ping": on_message_ping,
        "disconnect": on_message_disconnect,
        "stream": on_message_stream,
    }

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_orig(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_1(self):
        self.send_json(None)

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_2(self):
        self.send_json({
            "XXtypeXX": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_3(self):
        self.send_json({
            "TYPE": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_4(self):
        self.send_json({
            "Type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_5(self):
        self.send_json({
            "type": "XXstartWatchingXX",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_6(self):
        self.send_json({
            "type": "startwatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_7(self):
        self.send_json({
            "type": "STARTWATCHING",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_8(self):
        self.send_json({
            "type": "Startwatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_9(self):
        self.send_json({
            "type": "startWatching",
            "XXdataXX": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_10(self):
        self.send_json({
            "type": "startWatching",
            "DATA": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_11(self):
        self.send_json({
            "type": "startWatching",
            "Data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_12(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "XXstreamXX": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_13(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "STREAM": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_14(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "Stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_15(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "XXqualityXX": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_16(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "QUALITY": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_17(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "Quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_18(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "XXabrXX",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_19(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "ABR",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_20(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "Abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_21(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "XXprotocolXX": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_22(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "PROTOCOL": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_23(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "Protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_24(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "XXhlsXX",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_25(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "HLS",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_26(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "Hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_27(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "XXlatencyXX": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_28(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "LATENCY": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_29(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "Latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_30(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "XXhighXX",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_31(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "HIGH",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_32(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "High",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_33(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "XXchasePlayXX": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_34(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chaseplay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_35(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "CHASEPLAY": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_36(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "Chaseplay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_37(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": True,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_38(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "XXroomXX": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_39(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "ROOM": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_40(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "Room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_41(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "XXprotocolXX": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_42(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "PROTOCOL": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_43(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "Protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_44(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "XXwebSocketXX",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_45(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "websocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_46(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "WEBSOCKET",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_47(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "Websocket",
                    "commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_48(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "XXcommentableXX": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_49(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "COMMENTABLE": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_50(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "Commentable": True,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_51(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": False,
                },
                "reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_52(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "XXreconnectXX": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_53(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "RECONNECT": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_54(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "Reconnect": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_playerversion__mutmut_55(self):
        self.send_json({
            "type": "startWatching",
            "data": {
                "stream": {
                    "quality": "abr",
                    "protocol": "hls",
                    "latency": "high",
                    "chasePlay": False,
                },
                "room": {
                    "protocol": "webSocket",
                    "commentable": True,
                },
                "reconnect": True,
            },
        })
    
    xǁNicoLiveWsClientǁsend_playerversion__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNicoLiveWsClientǁsend_playerversion__mutmut_1': xǁNicoLiveWsClientǁsend_playerversion__mutmut_1, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_2': xǁNicoLiveWsClientǁsend_playerversion__mutmut_2, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_3': xǁNicoLiveWsClientǁsend_playerversion__mutmut_3, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_4': xǁNicoLiveWsClientǁsend_playerversion__mutmut_4, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_5': xǁNicoLiveWsClientǁsend_playerversion__mutmut_5, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_6': xǁNicoLiveWsClientǁsend_playerversion__mutmut_6, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_7': xǁNicoLiveWsClientǁsend_playerversion__mutmut_7, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_8': xǁNicoLiveWsClientǁsend_playerversion__mutmut_8, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_9': xǁNicoLiveWsClientǁsend_playerversion__mutmut_9, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_10': xǁNicoLiveWsClientǁsend_playerversion__mutmut_10, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_11': xǁNicoLiveWsClientǁsend_playerversion__mutmut_11, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_12': xǁNicoLiveWsClientǁsend_playerversion__mutmut_12, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_13': xǁNicoLiveWsClientǁsend_playerversion__mutmut_13, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_14': xǁNicoLiveWsClientǁsend_playerversion__mutmut_14, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_15': xǁNicoLiveWsClientǁsend_playerversion__mutmut_15, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_16': xǁNicoLiveWsClientǁsend_playerversion__mutmut_16, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_17': xǁNicoLiveWsClientǁsend_playerversion__mutmut_17, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_18': xǁNicoLiveWsClientǁsend_playerversion__mutmut_18, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_19': xǁNicoLiveWsClientǁsend_playerversion__mutmut_19, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_20': xǁNicoLiveWsClientǁsend_playerversion__mutmut_20, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_21': xǁNicoLiveWsClientǁsend_playerversion__mutmut_21, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_22': xǁNicoLiveWsClientǁsend_playerversion__mutmut_22, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_23': xǁNicoLiveWsClientǁsend_playerversion__mutmut_23, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_24': xǁNicoLiveWsClientǁsend_playerversion__mutmut_24, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_25': xǁNicoLiveWsClientǁsend_playerversion__mutmut_25, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_26': xǁNicoLiveWsClientǁsend_playerversion__mutmut_26, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_27': xǁNicoLiveWsClientǁsend_playerversion__mutmut_27, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_28': xǁNicoLiveWsClientǁsend_playerversion__mutmut_28, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_29': xǁNicoLiveWsClientǁsend_playerversion__mutmut_29, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_30': xǁNicoLiveWsClientǁsend_playerversion__mutmut_30, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_31': xǁNicoLiveWsClientǁsend_playerversion__mutmut_31, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_32': xǁNicoLiveWsClientǁsend_playerversion__mutmut_32, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_33': xǁNicoLiveWsClientǁsend_playerversion__mutmut_33, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_34': xǁNicoLiveWsClientǁsend_playerversion__mutmut_34, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_35': xǁNicoLiveWsClientǁsend_playerversion__mutmut_35, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_36': xǁNicoLiveWsClientǁsend_playerversion__mutmut_36, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_37': xǁNicoLiveWsClientǁsend_playerversion__mutmut_37, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_38': xǁNicoLiveWsClientǁsend_playerversion__mutmut_38, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_39': xǁNicoLiveWsClientǁsend_playerversion__mutmut_39, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_40': xǁNicoLiveWsClientǁsend_playerversion__mutmut_40, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_41': xǁNicoLiveWsClientǁsend_playerversion__mutmut_41, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_42': xǁNicoLiveWsClientǁsend_playerversion__mutmut_42, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_43': xǁNicoLiveWsClientǁsend_playerversion__mutmut_43, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_44': xǁNicoLiveWsClientǁsend_playerversion__mutmut_44, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_45': xǁNicoLiveWsClientǁsend_playerversion__mutmut_45, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_46': xǁNicoLiveWsClientǁsend_playerversion__mutmut_46, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_47': xǁNicoLiveWsClientǁsend_playerversion__mutmut_47, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_48': xǁNicoLiveWsClientǁsend_playerversion__mutmut_48, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_49': xǁNicoLiveWsClientǁsend_playerversion__mutmut_49, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_50': xǁNicoLiveWsClientǁsend_playerversion__mutmut_50, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_51': xǁNicoLiveWsClientǁsend_playerversion__mutmut_51, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_52': xǁNicoLiveWsClientǁsend_playerversion__mutmut_52, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_53': xǁNicoLiveWsClientǁsend_playerversion__mutmut_53, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_54': xǁNicoLiveWsClientǁsend_playerversion__mutmut_54, 
        'xǁNicoLiveWsClientǁsend_playerversion__mutmut_55': xǁNicoLiveWsClientǁsend_playerversion__mutmut_55
    }
    
    def send_playerversion(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNicoLiveWsClientǁsend_playerversion__mutmut_orig"), object.__getattribute__(self, "xǁNicoLiveWsClientǁsend_playerversion__mutmut_mutants"), args, kwargs, self)
        return result 
    
    send_playerversion.__signature__ = _mutmut_signature(xǁNicoLiveWsClientǁsend_playerversion__mutmut_orig)
    xǁNicoLiveWsClientǁsend_playerversion__mutmut_orig.__name__ = 'xǁNicoLiveWsClientǁsend_playerversion'

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_orig(self):
        self.send_json({
            "type": "getAkashic",
            "data": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_1(self):
        self.send_json(None)

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_2(self):
        self.send_json({
            "XXtypeXX": "getAkashic",
            "data": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_3(self):
        self.send_json({
            "TYPE": "getAkashic",
            "data": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_4(self):
        self.send_json({
            "Type": "getAkashic",
            "data": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_5(self):
        self.send_json({
            "type": "XXgetAkashicXX",
            "data": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_6(self):
        self.send_json({
            "type": "getakashic",
            "data": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_7(self):
        self.send_json({
            "type": "GETAKASHIC",
            "data": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_8(self):
        self.send_json({
            "type": "Getakashic",
            "data": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_9(self):
        self.send_json({
            "type": "getAkashic",
            "XXdataXX": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_10(self):
        self.send_json({
            "type": "getAkashic",
            "DATA": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_11(self):
        self.send_json({
            "type": "getAkashic",
            "Data": {
                "chasePlay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_12(self):
        self.send_json({
            "type": "getAkashic",
            "data": {
                "XXchasePlayXX": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_13(self):
        self.send_json({
            "type": "getAkashic",
            "data": {
                "chaseplay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_14(self):
        self.send_json({
            "type": "getAkashic",
            "data": {
                "CHASEPLAY": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_15(self):
        self.send_json({
            "type": "getAkashic",
            "data": {
                "Chaseplay": False,
            },
        })

    def xǁNicoLiveWsClientǁsend_getpermit__mutmut_16(self):
        self.send_json({
            "type": "getAkashic",
            "data": {
                "chasePlay": True,
            },
        })
    
    xǁNicoLiveWsClientǁsend_getpermit__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNicoLiveWsClientǁsend_getpermit__mutmut_1': xǁNicoLiveWsClientǁsend_getpermit__mutmut_1, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_2': xǁNicoLiveWsClientǁsend_getpermit__mutmut_2, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_3': xǁNicoLiveWsClientǁsend_getpermit__mutmut_3, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_4': xǁNicoLiveWsClientǁsend_getpermit__mutmut_4, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_5': xǁNicoLiveWsClientǁsend_getpermit__mutmut_5, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_6': xǁNicoLiveWsClientǁsend_getpermit__mutmut_6, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_7': xǁNicoLiveWsClientǁsend_getpermit__mutmut_7, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_8': xǁNicoLiveWsClientǁsend_getpermit__mutmut_8, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_9': xǁNicoLiveWsClientǁsend_getpermit__mutmut_9, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_10': xǁNicoLiveWsClientǁsend_getpermit__mutmut_10, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_11': xǁNicoLiveWsClientǁsend_getpermit__mutmut_11, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_12': xǁNicoLiveWsClientǁsend_getpermit__mutmut_12, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_13': xǁNicoLiveWsClientǁsend_getpermit__mutmut_13, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_14': xǁNicoLiveWsClientǁsend_getpermit__mutmut_14, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_15': xǁNicoLiveWsClientǁsend_getpermit__mutmut_15, 
        'xǁNicoLiveWsClientǁsend_getpermit__mutmut_16': xǁNicoLiveWsClientǁsend_getpermit__mutmut_16
    }
    
    def send_getpermit(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNicoLiveWsClientǁsend_getpermit__mutmut_orig"), object.__getattribute__(self, "xǁNicoLiveWsClientǁsend_getpermit__mutmut_mutants"), args, kwargs, self)
        return result 
    
    send_getpermit.__signature__ = _mutmut_signature(xǁNicoLiveWsClientǁsend_getpermit__mutmut_orig)
    xǁNicoLiveWsClientǁsend_getpermit__mutmut_orig.__name__ = 'xǁNicoLiveWsClientǁsend_getpermit'

    def xǁNicoLiveWsClientǁsend_pong__mutmut_orig(self):
        self.send_json({"type": "pong"})
        self.send_json({"type": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_1(self):
        self.send_json(None)
        self.send_json({"type": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_2(self):
        self.send_json({"XXtypeXX": "pong"})
        self.send_json({"type": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_3(self):
        self.send_json({"TYPE": "pong"})
        self.send_json({"type": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_4(self):
        self.send_json({"Type": "pong"})
        self.send_json({"type": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_5(self):
        self.send_json({"type": "XXpongXX"})
        self.send_json({"type": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_6(self):
        self.send_json({"type": "PONG"})
        self.send_json({"type": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_7(self):
        self.send_json({"type": "Pong"})
        self.send_json({"type": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_8(self):
        self.send_json({"type": "pong"})
        self.send_json(None)

    def xǁNicoLiveWsClientǁsend_pong__mutmut_9(self):
        self.send_json({"type": "pong"})
        self.send_json({"XXtypeXX": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_10(self):
        self.send_json({"type": "pong"})
        self.send_json({"TYPE": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_11(self):
        self.send_json({"type": "pong"})
        self.send_json({"Type": "keepSeat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_12(self):
        self.send_json({"type": "pong"})
        self.send_json({"type": "XXkeepSeatXX"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_13(self):
        self.send_json({"type": "pong"})
        self.send_json({"type": "keepseat"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_14(self):
        self.send_json({"type": "pong"})
        self.send_json({"type": "KEEPSEAT"})

    def xǁNicoLiveWsClientǁsend_pong__mutmut_15(self):
        self.send_json({"type": "pong"})
        self.send_json({"type": "Keepseat"})
    
    xǁNicoLiveWsClientǁsend_pong__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNicoLiveWsClientǁsend_pong__mutmut_1': xǁNicoLiveWsClientǁsend_pong__mutmut_1, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_2': xǁNicoLiveWsClientǁsend_pong__mutmut_2, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_3': xǁNicoLiveWsClientǁsend_pong__mutmut_3, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_4': xǁNicoLiveWsClientǁsend_pong__mutmut_4, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_5': xǁNicoLiveWsClientǁsend_pong__mutmut_5, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_6': xǁNicoLiveWsClientǁsend_pong__mutmut_6, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_7': xǁNicoLiveWsClientǁsend_pong__mutmut_7, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_8': xǁNicoLiveWsClientǁsend_pong__mutmut_8, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_9': xǁNicoLiveWsClientǁsend_pong__mutmut_9, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_10': xǁNicoLiveWsClientǁsend_pong__mutmut_10, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_11': xǁNicoLiveWsClientǁsend_pong__mutmut_11, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_12': xǁNicoLiveWsClientǁsend_pong__mutmut_12, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_13': xǁNicoLiveWsClientǁsend_pong__mutmut_13, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_14': xǁNicoLiveWsClientǁsend_pong__mutmut_14, 
        'xǁNicoLiveWsClientǁsend_pong__mutmut_15': xǁNicoLiveWsClientǁsend_pong__mutmut_15
    }
    
    def send_pong(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNicoLiveWsClientǁsend_pong__mutmut_orig"), object.__getattribute__(self, "xǁNicoLiveWsClientǁsend_pong__mutmut_mutants"), args, kwargs, self)
        return result 
    
    send_pong.__signature__ = _mutmut_signature(xǁNicoLiveWsClientǁsend_pong__mutmut_orig)
    xǁNicoLiveWsClientǁsend_pong__mutmut_orig.__name__ = 'xǁNicoLiveWsClientǁsend_pong'


class NicoLiveHLSStreamWriter(HLSStreamWriter):
    reader: NicoLiveHLSStreamReader
    stream: NicoLiveHLSStream

    def xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_orig(self, segment: HLSSegment) -> bool:
        if "/blank/" in segment.uri:
            return True

        return super().should_filter_segment(segment)

    def xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_1(self, segment: HLSSegment) -> bool:
        if "XX/blank/XX" in segment.uri:
            return True

        return super().should_filter_segment(segment)

    def xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_2(self, segment: HLSSegment) -> bool:
        if "/BLANK/" in segment.uri:
            return True

        return super().should_filter_segment(segment)

    def xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_3(self, segment: HLSSegment) -> bool:
        if "/blank/" not in segment.uri:
            return True

        return super().should_filter_segment(segment)

    def xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_4(self, segment: HLSSegment) -> bool:
        if "/blank/" in segment.uri:
            return False

        return super().should_filter_segment(segment)

    def xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_5(self, segment: HLSSegment) -> bool:
        if "/blank/" in segment.uri:
            return True

        return super().should_filter_segment(None)
    
    xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_1': xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_1, 
        'xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_2': xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_2, 
        'xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_3': xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_3, 
        'xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_4': xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_4, 
        'xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_5': xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_5
    }
    
    def should_filter_segment(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_orig"), object.__getattribute__(self, "xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_mutants"), args, kwargs, self)
        return result 
    
    should_filter_segment.__signature__ = _mutmut_signature(xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_orig)
    xǁNicoLiveHLSStreamWriterǁshould_filter_segment__mutmut_orig.__name__ = 'xǁNicoLiveHLSStreamWriterǁshould_filter_segment'


class NicoLiveHLSStreamReader(HLSStreamReader):
    __writer__ = NicoLiveHLSStreamWriter

    writer: NicoLiveHLSStreamWriter
    stream: NicoLiveHLSStream

    def open(self):
        self.stream.wsclient.opened.set()
        super().open()

    def close(self):
        super().close()
        self.stream.wsclient.close()


class NicoLiveHLSStream(HLSStream):
    __reader__ = NicoLiveHLSStreamReader
    wsclient: NicoLiveWsClient

    def xǁNicoLiveHLSStreamǁ__init____mutmut_orig(self, *args, wsclient: NicoLiveWsClient, **kwargs):
        super().__init__(*args, **kwargs)
        self.wsclient = wsclient

    def xǁNicoLiveHLSStreamǁ__init____mutmut_1(self, *args, wsclient: NicoLiveWsClient, **kwargs):
        super().__init__(**kwargs)
        self.wsclient = wsclient

    def xǁNicoLiveHLSStreamǁ__init____mutmut_2(self, *args, wsclient: NicoLiveWsClient, **kwargs):
        super().__init__(*args, )
        self.wsclient = wsclient

    def xǁNicoLiveHLSStreamǁ__init____mutmut_3(self, *args, wsclient: NicoLiveWsClient, **kwargs):
        super().__init__(*args, **kwargs)
        self.wsclient = None
    
    xǁNicoLiveHLSStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNicoLiveHLSStreamǁ__init____mutmut_1': xǁNicoLiveHLSStreamǁ__init____mutmut_1, 
        'xǁNicoLiveHLSStreamǁ__init____mutmut_2': xǁNicoLiveHLSStreamǁ__init____mutmut_2, 
        'xǁNicoLiveHLSStreamǁ__init____mutmut_3': xǁNicoLiveHLSStreamǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNicoLiveHLSStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁNicoLiveHLSStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁNicoLiveHLSStreamǁ__init____mutmut_orig)
    xǁNicoLiveHLSStreamǁ__init____mutmut_orig.__name__ = 'xǁNicoLiveHLSStreamǁ__init__'


@pluginmatcher(
    re.compile(r"https?://(?P<domain>live\d*\.nicovideo\.jp)/watch/(lv|co|user/)\d+"),
)
@pluginargument(
    "email",
    sensitive=True,
    argument_name="niconico-email",
    metavar="EMAIL",
    help="The email or phone number associated with your Niconico account",
)
@pluginargument(
    "password",
    sensitive=True,
    argument_name="niconico-password",
    metavar="PASSWORD",
    help="The password of your Niconico account",
)
@pluginargument(
    "user-session",
    sensitive=True,
    argument_name="niconico-user-session",
    metavar="VALUE",
    help="""
        Value of the user-session token.

        Can be used as an alternative to providing a password.
    """,
)
@pluginargument(
    "purge-credentials",
    argument_name="niconico-purge-credentials",
    action="store_true",
    help="Purge cached Niconico credentials to initiate a new session and reauthenticate.",
)
@pluginargument(
    "timeshift-offset",
    type="hours_minutes_seconds",
    argument_name="niconico-timeshift-offset",
    metavar="[[XX:]XX:]XX | [XXh][XXm][XXs]",
    help="""
        Amount of time to skip from the beginning of a stream.

        Default is 0.
    """,
)
class NicoLive(Plugin):
    STREAM_READY_TIMEOUT = 6
    LOGIN_URL = "https://account.nicovideo.jp/login/redirector"
    LOGIN_URL_PARAMS = {
        "site": "niconico",
    }

    wsclient: NicoLiveWsClient

    def _get_streams(self):
        if self.get_option("purge_credentials"):
            self.clear_cookies()
            log.info("All credentials were successfully removed")

        self.session.http.headers.update({
            "User-Agent": useragents.CHROME,
        })

        self.niconico_web_login()

        data = self.get_data()

        wss_api_url = self.find_wss_api_url(data)
        if not wss_api_url:
            log.error(
                "Failed to get wss_api_url. "
                + "Please check if the URL is correct, and make sure your account has access to the video.",
            )
            return

        self.id, self.author, self.title = self.find_metadata(data)

        self.wsclient = NicoLiveWsClient(self.session, wss_api_url)
        self.wsclient.start()

        hls_stream_url = self._get_hls_stream_url()
        if not hls_stream_url:
            return

        offset = self.get_option("timeshift-offset")
        if offset and "timeshift" in wss_api_url:
            hls_stream_url = update_qsd(hls_stream_url, {"start": offset})

        return NicoLiveHLSStream.parse_variant_playlist(
            self.session,
            hls_stream_url,
            wsclient=self.wsclient,
            ffmpeg_options={"copyts": True},
        )

    def _get_hls_stream_url(self):
        log.debug(f"Waiting for permit (for at most {self.STREAM_READY_TIMEOUT} seconds)...")
        if not self.wsclient.ready.wait(self.STREAM_READY_TIMEOUT) or not self.wsclient.is_alive():
            log.error("Waiting for permit timed out.")
            self.wsclient.close()
            return

        return self.wsclient.hls_stream_url

    def get_data(self):
        return self.session.http.get(
            self.url,
            encoding="utf-8",
            schema=validate.Schema(
                validate.parse_html(),
                validate.xml_find(".//script[@id='embedded-data'][@data-props]"),
                validate.get("data-props"),
                validate.parse_json(),
            ),
        )

    @staticmethod
    def find_metadata(data):
        schema = validate.Schema(
            {
                "program": {
                    "nicoliveProgramId": str,
                    "supplier": {"name": str},
                    "title": str,
                },
            },
            validate.get("program"),
            validate.union_get(
                "nicoliveProgramId",
                ("supplier", "name"),
                "title",
            ),
        )

        return schema.validate(data)

    @staticmethod
    def find_wss_api_url(data):
        schema = validate.Schema(
            {
                "site": {
                    "relive": {
                        "webSocketUrl": validate.any(
                            validate.url(scheme="wss"),
                            "",
                        ),
                    },
                    validate.optional("frontendId"): int,
                },
            },
            validate.get("site"),
            validate.union_get(("relive", "webSocketUrl"), "frontendId"),
        )

        wss_api_url, frontend_id = schema.validate(data)
        if not wss_api_url:
            return

        if frontend_id is not None:
            wss_api_url = update_qsd(wss_api_url, {"frontend_id": frontend_id})

        return wss_api_url

    def niconico_web_login(self):
        user_session = self.get_option("user-session")
        email = self.get_option("email")
        password = self.get_option("password")

        if user_session is not None:
            log.info("Logging in via provided user session cookie")
            self.session.http.cookies.set(
                "user_session",
                user_session,
                path="/",
                domain="nicovideo.jp",
            )
            self.save_cookies()

        elif self.session.http.cookies.get("user_session"):
            log.info("Logging in via cached user session cookie")

        elif email is not None and password is not None:
            log.info("Logging in via provided email and password")
            root = self.session.http.post(
                self.LOGIN_URL,
                data={"mail_tel": email, "password": password},
                params=self.LOGIN_URL_PARAMS,
                schema=validate.Schema(validate.parse_html()),
            )

            if self.session.http.cookies.get("user_session"):
                log.info("Logged in.")
                self.save_cookies()
                return

            input_with_value = {}
            for elem in root.xpath(".//form[@action]//input"):
                if elem.attrib.get("value"):
                    input_with_value[elem.attrib.get("name")] = elem.attrib.get("value")
                elif elem.attrib.get("id") == "oneTimePw":
                    maxlength = int(elem.attrib.get("maxlength"))
                    oneTimePw = self.input_ask("Enter the 6 digit number included in email")
                    if len(oneTimePw) > maxlength:
                        log.error("invalid user input")
                        return
                    input_with_value[elem.attrib.get("name")] = oneTimePw
                else:
                    log.debug(f"unknown input: {elem.attrib.get('name')}")

            root = self.session.http.post(
                urljoin("https://account.nicovideo.jp", root.xpath("string(.//form[@action]/@action)")),
                data=input_with_value,
                schema=validate.Schema(validate.parse_html()),
            )
            log.debug(f"Cookies: {self.session.http.cookies.get_dict()}")
            if self.session.http.cookies.get("user_session") is None:
                error = root.xpath("string(//div[@class='formError']/div/text())")
                log.warning(f"Login failed: {error or 'unknown reason'}")
            else:
                log.info("Logged in.")
                self.save_cookies()


__plugin__ = NicoLive

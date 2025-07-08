from __future__ import annotations

import dataclasses
import itertools
import json
import logging
from collections import defaultdict
from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Generic, TypeVar, cast

import trio
from trio_websocket import ConnectionClosed, WebSocketConnection, connect_websocket_url  # type: ignore[import]

from streamlink.logger import ALL, ERROR, WARNING
from streamlink.webbrowser.cdp.devtools.target import SessionID, TargetID, attach_to_target, create_target
from streamlink.webbrowser.cdp.devtools.util import T_JSON_DICT, parse_json_event
from streamlink.webbrowser.cdp.exceptions import CDPError


if TYPE_CHECKING:
    try:
        from typing import Self, TypeAlias  # type: ignore[attr-defined]
    except ImportError:
        from typing_extensions import Self, TypeAlias


log = logging.getLogger(__name__)

MAX_BUFFER_SIZE = 10
MAX_MESSAGE_SIZE = 2**24  # ~16MiB
CMD_TIMEOUT = 2

TCmdResponse = TypeVar("TCmdResponse")
TEvent = TypeVar("TEvent")
TEventChannels: TypeAlias = "dict[type[TEvent], set[trio.MemorySendChannel[TEvent]]]"
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


class CDPEventListener(Generic[TEvent]):
    """
    Instances of this class are returned by :meth:`CDPBase.listen()`.

    The return types of each of its methods depend on the event type.

    Can be used as an async for-loop which indefinitely waits for events to be emitted,
    or can be used as an async context manager which yields the event and closes the listener when leaving the context manager.

    Example:

    .. code-block:: python

        async def listen(cdp_session: CDPSession):
            async for request in cdp_session.listen(devtools.fetch.RequestPaused):
                ...

        async def listen_once(cdp_session: CDPSession):
            async with cdp_session.listen(devtools.fetch.RequestPaused) as request:
                ...
    """

    _sender: trio.MemorySendChannel[TEvent]
    _receiver: trio.MemoryReceiveChannel[TEvent]

    def xǁCDPEventListenerǁ__init____mutmut_orig(self, event_channels: TEventChannels, event: type[TEvent], max_buffer_size: int | None = None):
        max_buffer_size = MAX_BUFFER_SIZE if max_buffer_size is None else max_buffer_size
        self._sender, self._receiver = trio.open_memory_channel(max_buffer_size)
        event_channels[event].add(self._sender)

    def xǁCDPEventListenerǁ__init____mutmut_1(self, event_channels: TEventChannels, event: type[TEvent], max_buffer_size: int | None = None):
        max_buffer_size = None
        self._sender, self._receiver = trio.open_memory_channel(max_buffer_size)
        event_channels[event].add(self._sender)

    def xǁCDPEventListenerǁ__init____mutmut_2(self, event_channels: TEventChannels, event: type[TEvent], max_buffer_size: int | None = None):
        max_buffer_size = MAX_BUFFER_SIZE if max_buffer_size is not None else max_buffer_size
        self._sender, self._receiver = trio.open_memory_channel(max_buffer_size)
        event_channels[event].add(self._sender)

    def xǁCDPEventListenerǁ__init____mutmut_3(self, event_channels: TEventChannels, event: type[TEvent], max_buffer_size: int | None = None):
        max_buffer_size = MAX_BUFFER_SIZE if max_buffer_size is None else max_buffer_size
        self._sender, self._receiver = None
        event_channels[event].add(self._sender)

    def xǁCDPEventListenerǁ__init____mutmut_4(self, event_channels: TEventChannels, event: type[TEvent], max_buffer_size: int | None = None):
        max_buffer_size = MAX_BUFFER_SIZE if max_buffer_size is None else max_buffer_size
        self._sender, self._receiver = trio.open_memory_channel(None)
        event_channels[event].add(self._sender)

    def xǁCDPEventListenerǁ__init____mutmut_5(self, event_channels: TEventChannels, event: type[TEvent], max_buffer_size: int | None = None):
        max_buffer_size = MAX_BUFFER_SIZE if max_buffer_size is None else max_buffer_size
        self._sender, self._receiver = trio.open_memory_channel(max_buffer_size)
        event_channels[event].add(None)
    
    xǁCDPEventListenerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPEventListenerǁ__init____mutmut_1': xǁCDPEventListenerǁ__init____mutmut_1, 
        'xǁCDPEventListenerǁ__init____mutmut_2': xǁCDPEventListenerǁ__init____mutmut_2, 
        'xǁCDPEventListenerǁ__init____mutmut_3': xǁCDPEventListenerǁ__init____mutmut_3, 
        'xǁCDPEventListenerǁ__init____mutmut_4': xǁCDPEventListenerǁ__init____mutmut_4, 
        'xǁCDPEventListenerǁ__init____mutmut_5': xǁCDPEventListenerǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPEventListenerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCDPEventListenerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCDPEventListenerǁ__init____mutmut_orig)
    xǁCDPEventListenerǁ__init____mutmut_orig.__name__ = 'xǁCDPEventListenerǁ__init__'

    async def receive(self) -> TEvent:
        """
        Await a single event without closing the listener's memory channel.
        """

        return await self._receiver.receive()

    def close(self) -> None:
        self._receiver.close()

    async def __aenter__(self) -> TEvent:
        return await self._receiver.receive()

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        # sync
        self.close()

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> TEvent:
        try:
            return await self._receiver.receive()
        except trio.EndOfChannel as err:
            self.close()
            raise StopAsyncIteration from err

    def __del__(self) -> None:
        self.close()


@dataclasses.dataclass
class _CDPCmdBuffer(Generic[TCmdResponse]):
    cmd: Generator[dict, dict, TCmdResponse]
    response: TCmdResponse | Exception | None = None
    event: trio.Event = dataclasses.field(default_factory=trio.Event)

    def set_response(self, response: TCmdResponse | Exception) -> None:
        self.response = response
        self.event.set()


# The design of CDPBase/CDPConnection/CDPSession is based on the trio-chrome-devtools-protocol project version 0.6.0
# https://github.com/HyperionGray/trio-chrome-devtools-protocol/blob/0.6.0/trio_cdp/__init__.py
#
# The MIT License (MIT)
#
# Copyright (c) 2018 Hyperion Gray
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


class CDPBase:
    """
    Low-level base class for Chrome Devtools Protocol connection & session management.

    It provides methods for sending CDP commands and receiving their responses, as well as for listening to CDP events.

    Both CDP commands and events can be sent and received in a global context and in a session context.

    The Chrome Devtools Protocol is documented at https://chromedevtools.github.io/devtools-protocol/
    """

    def xǁCDPBaseǁ__init____mutmut_orig(
        self,
        websocket: WebSocketConnection,
        target_id: TargetID | None = None,
        session_id: SessionID | None = None,
        cmd_timeout: float = CMD_TIMEOUT,
    ) -> None:
        self.websocket = websocket
        self.target_id = target_id
        self.session_id = session_id
        self.cmd_timeout = cmd_timeout
        self.event_channels: TEventChannels = defaultdict(set)
        self.cmd_buffers: dict[int, _CDPCmdBuffer] = {}
        self.cmd_id = itertools.count()

    def xǁCDPBaseǁ__init____mutmut_1(
        self,
        websocket: WebSocketConnection,
        target_id: TargetID | None = None,
        session_id: SessionID | None = None,
        cmd_timeout: float = CMD_TIMEOUT,
    ) -> None:
        self.websocket = None
        self.target_id = target_id
        self.session_id = session_id
        self.cmd_timeout = cmd_timeout
        self.event_channels: TEventChannels = defaultdict(set)
        self.cmd_buffers: dict[int, _CDPCmdBuffer] = {}
        self.cmd_id = itertools.count()

    def xǁCDPBaseǁ__init____mutmut_2(
        self,
        websocket: WebSocketConnection,
        target_id: TargetID | None = None,
        session_id: SessionID | None = None,
        cmd_timeout: float = CMD_TIMEOUT,
    ) -> None:
        self.websocket = websocket
        self.target_id = None
        self.session_id = session_id
        self.cmd_timeout = cmd_timeout
        self.event_channels: TEventChannels = defaultdict(set)
        self.cmd_buffers: dict[int, _CDPCmdBuffer] = {}
        self.cmd_id = itertools.count()

    def xǁCDPBaseǁ__init____mutmut_3(
        self,
        websocket: WebSocketConnection,
        target_id: TargetID | None = None,
        session_id: SessionID | None = None,
        cmd_timeout: float = CMD_TIMEOUT,
    ) -> None:
        self.websocket = websocket
        self.target_id = target_id
        self.session_id = None
        self.cmd_timeout = cmd_timeout
        self.event_channels: TEventChannels = defaultdict(set)
        self.cmd_buffers: dict[int, _CDPCmdBuffer] = {}
        self.cmd_id = itertools.count()

    def xǁCDPBaseǁ__init____mutmut_4(
        self,
        websocket: WebSocketConnection,
        target_id: TargetID | None = None,
        session_id: SessionID | None = None,
        cmd_timeout: float = CMD_TIMEOUT,
    ) -> None:
        self.websocket = websocket
        self.target_id = target_id
        self.session_id = session_id
        self.cmd_timeout = None
        self.event_channels: TEventChannels = defaultdict(set)
        self.cmd_buffers: dict[int, _CDPCmdBuffer] = {}
        self.cmd_id = itertools.count()

    def xǁCDPBaseǁ__init____mutmut_5(
        self,
        websocket: WebSocketConnection,
        target_id: TargetID | None = None,
        session_id: SessionID | None = None,
        cmd_timeout: float = CMD_TIMEOUT,
    ) -> None:
        self.websocket = websocket
        self.target_id = target_id
        self.session_id = session_id
        self.cmd_timeout = cmd_timeout
        self.event_channels: TEventChannels = None
        self.cmd_buffers: dict[int, _CDPCmdBuffer] = {}
        self.cmd_id = itertools.count()

    def xǁCDPBaseǁ__init____mutmut_6(
        self,
        websocket: WebSocketConnection,
        target_id: TargetID | None = None,
        session_id: SessionID | None = None,
        cmd_timeout: float = CMD_TIMEOUT,
    ) -> None:
        self.websocket = websocket
        self.target_id = target_id
        self.session_id = session_id
        self.cmd_timeout = cmd_timeout
        self.event_channels: TEventChannels = defaultdict(None)
        self.cmd_buffers: dict[int, _CDPCmdBuffer] = {}
        self.cmd_id = itertools.count()

    def xǁCDPBaseǁ__init____mutmut_7(
        self,
        websocket: WebSocketConnection,
        target_id: TargetID | None = None,
        session_id: SessionID | None = None,
        cmd_timeout: float = CMD_TIMEOUT,
    ) -> None:
        self.websocket = websocket
        self.target_id = target_id
        self.session_id = session_id
        self.cmd_timeout = cmd_timeout
        self.event_channels: TEventChannels = defaultdict(set)
        self.cmd_buffers: dict[int, _CDPCmdBuffer] = None
        self.cmd_id = itertools.count()

    def xǁCDPBaseǁ__init____mutmut_8(
        self,
        websocket: WebSocketConnection,
        target_id: TargetID | None = None,
        session_id: SessionID | None = None,
        cmd_timeout: float = CMD_TIMEOUT,
    ) -> None:
        self.websocket = websocket
        self.target_id = target_id
        self.session_id = session_id
        self.cmd_timeout = cmd_timeout
        self.event_channels: TEventChannels = defaultdict(set)
        self.cmd_buffers: dict[int, _CDPCmdBuffer] = {}
        self.cmd_id = None
    
    xǁCDPBaseǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPBaseǁ__init____mutmut_1': xǁCDPBaseǁ__init____mutmut_1, 
        'xǁCDPBaseǁ__init____mutmut_2': xǁCDPBaseǁ__init____mutmut_2, 
        'xǁCDPBaseǁ__init____mutmut_3': xǁCDPBaseǁ__init____mutmut_3, 
        'xǁCDPBaseǁ__init____mutmut_4': xǁCDPBaseǁ__init____mutmut_4, 
        'xǁCDPBaseǁ__init____mutmut_5': xǁCDPBaseǁ__init____mutmut_5, 
        'xǁCDPBaseǁ__init____mutmut_6': xǁCDPBaseǁ__init____mutmut_6, 
        'xǁCDPBaseǁ__init____mutmut_7': xǁCDPBaseǁ__init____mutmut_7, 
        'xǁCDPBaseǁ__init____mutmut_8': xǁCDPBaseǁ__init____mutmut_8
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPBaseǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCDPBaseǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCDPBaseǁ__init____mutmut_orig)
    xǁCDPBaseǁ__init____mutmut_orig.__name__ = 'xǁCDPBaseǁ__init__'

    async def xǁCDPBaseǁsend__mutmut_orig(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_1(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = None
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_2(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(None)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_3(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = None

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_4(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(None)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_5(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = None

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_6(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = None
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_7(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(None)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_8(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = None
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_9(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["XXidXX"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_10(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["ID"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_11(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["Id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_12(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = None

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_13(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["XXsessionIdXX"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_14(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionid"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_15(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["SESSIONID"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_16(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["Sessionid"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_17(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = None
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_18(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(None, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_19(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=None, sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_20(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=None)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_21(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_22(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_23(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), )
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_24(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=("XX,XX", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_25(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", "XX:XX"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_26(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=False)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_27(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(None, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_28(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, None, dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_29(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", None)
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_30(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log("Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_31(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_32(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", )
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_33(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "XXSending message: %(message)sXX", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_34(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_35(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "SENDING MESSAGE: %(MESSAGE)S", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_36(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(messageXX=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_37(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=None))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_38(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(None) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_39(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is not None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_40(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(None)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_41(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(None, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_42(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_43(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, )
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_44(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(None) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_45(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(None, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_46(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_47(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, )
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_48(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError(None)

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_49(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("XXSending CDP message and receiving its response timed outXX")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_50(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("sending cdp message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_51(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("SENDING CDP MESSAGE AND RECEIVING ITS RESPONSE TIMED OUT")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_52(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending cdp message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_53(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = None
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_54(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(None, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_55(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, None)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_56(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_57(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, )
        self.cmd_buffers.pop(cmd_id, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_58(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(None, None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_59(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(None)

        if isinstance(response, Exception):
            raise response

        return response

    async def xǁCDPBaseǁsend__mutmut_60(
        self,
        cmd: Generator[T_JSON_DICT, T_JSON_DICT, TCmdResponse],
        timeout: float | None = None,
    ) -> TCmdResponse:
        """
        Send a specific CDP command and await its response.

        :param cmd: See the ``streamlink.webbrowser.cdp.devtools`` package for the available commands.
        :param timeout: Override of the max amount of time a response can take. Uses the class's default value otherwise.
                        This override is mostly only relevant for awaiting JS code evaluations.
        :return: The return value depends on the used command.
        """

        cmd_id = next(self.cmd_id)
        cmd_buffer = _CDPCmdBuffer(cmd)

        self.cmd_buffers[cmd_id] = cmd_buffer

        cmd_data = next(cmd)
        cmd_data["id"] = cmd_id
        if self.session_id:
            cmd_data["sessionId"] = self.session_id

        message = json.dumps(cmd_data, separators=(",", ":"), sort_keys=True)
        log.log(ALL, "Sending message: %(message)s", dict(message=message))
        with trio.move_on_after(self.cmd_timeout if timeout is None else timeout) as cancel_scope:
            try:
                await self.websocket.send_message(message)
            except ConnectionClosed as err:
                self.cmd_buffers.pop(cmd_id, None)
                raise CDPError(err.reason) from err

            await cmd_buffer.event.wait()
        if cancel_scope.cancel_called:
            self.cmd_buffers.pop(cmd_id, None)
            raise CDPError("Sending CDP message and receiving its response timed out")

        response = cast(TCmdResponse, cmd_buffer.response)
        self.cmd_buffers.pop(cmd_id, )

        if isinstance(response, Exception):
            raise response

        return response
    
    xǁCDPBaseǁsend__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPBaseǁsend__mutmut_1': xǁCDPBaseǁsend__mutmut_1, 
        'xǁCDPBaseǁsend__mutmut_2': xǁCDPBaseǁsend__mutmut_2, 
        'xǁCDPBaseǁsend__mutmut_3': xǁCDPBaseǁsend__mutmut_3, 
        'xǁCDPBaseǁsend__mutmut_4': xǁCDPBaseǁsend__mutmut_4, 
        'xǁCDPBaseǁsend__mutmut_5': xǁCDPBaseǁsend__mutmut_5, 
        'xǁCDPBaseǁsend__mutmut_6': xǁCDPBaseǁsend__mutmut_6, 
        'xǁCDPBaseǁsend__mutmut_7': xǁCDPBaseǁsend__mutmut_7, 
        'xǁCDPBaseǁsend__mutmut_8': xǁCDPBaseǁsend__mutmut_8, 
        'xǁCDPBaseǁsend__mutmut_9': xǁCDPBaseǁsend__mutmut_9, 
        'xǁCDPBaseǁsend__mutmut_10': xǁCDPBaseǁsend__mutmut_10, 
        'xǁCDPBaseǁsend__mutmut_11': xǁCDPBaseǁsend__mutmut_11, 
        'xǁCDPBaseǁsend__mutmut_12': xǁCDPBaseǁsend__mutmut_12, 
        'xǁCDPBaseǁsend__mutmut_13': xǁCDPBaseǁsend__mutmut_13, 
        'xǁCDPBaseǁsend__mutmut_14': xǁCDPBaseǁsend__mutmut_14, 
        'xǁCDPBaseǁsend__mutmut_15': xǁCDPBaseǁsend__mutmut_15, 
        'xǁCDPBaseǁsend__mutmut_16': xǁCDPBaseǁsend__mutmut_16, 
        'xǁCDPBaseǁsend__mutmut_17': xǁCDPBaseǁsend__mutmut_17, 
        'xǁCDPBaseǁsend__mutmut_18': xǁCDPBaseǁsend__mutmut_18, 
        'xǁCDPBaseǁsend__mutmut_19': xǁCDPBaseǁsend__mutmut_19, 
        'xǁCDPBaseǁsend__mutmut_20': xǁCDPBaseǁsend__mutmut_20, 
        'xǁCDPBaseǁsend__mutmut_21': xǁCDPBaseǁsend__mutmut_21, 
        'xǁCDPBaseǁsend__mutmut_22': xǁCDPBaseǁsend__mutmut_22, 
        'xǁCDPBaseǁsend__mutmut_23': xǁCDPBaseǁsend__mutmut_23, 
        'xǁCDPBaseǁsend__mutmut_24': xǁCDPBaseǁsend__mutmut_24, 
        'xǁCDPBaseǁsend__mutmut_25': xǁCDPBaseǁsend__mutmut_25, 
        'xǁCDPBaseǁsend__mutmut_26': xǁCDPBaseǁsend__mutmut_26, 
        'xǁCDPBaseǁsend__mutmut_27': xǁCDPBaseǁsend__mutmut_27, 
        'xǁCDPBaseǁsend__mutmut_28': xǁCDPBaseǁsend__mutmut_28, 
        'xǁCDPBaseǁsend__mutmut_29': xǁCDPBaseǁsend__mutmut_29, 
        'xǁCDPBaseǁsend__mutmut_30': xǁCDPBaseǁsend__mutmut_30, 
        'xǁCDPBaseǁsend__mutmut_31': xǁCDPBaseǁsend__mutmut_31, 
        'xǁCDPBaseǁsend__mutmut_32': xǁCDPBaseǁsend__mutmut_32, 
        'xǁCDPBaseǁsend__mutmut_33': xǁCDPBaseǁsend__mutmut_33, 
        'xǁCDPBaseǁsend__mutmut_34': xǁCDPBaseǁsend__mutmut_34, 
        'xǁCDPBaseǁsend__mutmut_35': xǁCDPBaseǁsend__mutmut_35, 
        'xǁCDPBaseǁsend__mutmut_36': xǁCDPBaseǁsend__mutmut_36, 
        'xǁCDPBaseǁsend__mutmut_37': xǁCDPBaseǁsend__mutmut_37, 
        'xǁCDPBaseǁsend__mutmut_38': xǁCDPBaseǁsend__mutmut_38, 
        'xǁCDPBaseǁsend__mutmut_39': xǁCDPBaseǁsend__mutmut_39, 
        'xǁCDPBaseǁsend__mutmut_40': xǁCDPBaseǁsend__mutmut_40, 
        'xǁCDPBaseǁsend__mutmut_41': xǁCDPBaseǁsend__mutmut_41, 
        'xǁCDPBaseǁsend__mutmut_42': xǁCDPBaseǁsend__mutmut_42, 
        'xǁCDPBaseǁsend__mutmut_43': xǁCDPBaseǁsend__mutmut_43, 
        'xǁCDPBaseǁsend__mutmut_44': xǁCDPBaseǁsend__mutmut_44, 
        'xǁCDPBaseǁsend__mutmut_45': xǁCDPBaseǁsend__mutmut_45, 
        'xǁCDPBaseǁsend__mutmut_46': xǁCDPBaseǁsend__mutmut_46, 
        'xǁCDPBaseǁsend__mutmut_47': xǁCDPBaseǁsend__mutmut_47, 
        'xǁCDPBaseǁsend__mutmut_48': xǁCDPBaseǁsend__mutmut_48, 
        'xǁCDPBaseǁsend__mutmut_49': xǁCDPBaseǁsend__mutmut_49, 
        'xǁCDPBaseǁsend__mutmut_50': xǁCDPBaseǁsend__mutmut_50, 
        'xǁCDPBaseǁsend__mutmut_51': xǁCDPBaseǁsend__mutmut_51, 
        'xǁCDPBaseǁsend__mutmut_52': xǁCDPBaseǁsend__mutmut_52, 
        'xǁCDPBaseǁsend__mutmut_53': xǁCDPBaseǁsend__mutmut_53, 
        'xǁCDPBaseǁsend__mutmut_54': xǁCDPBaseǁsend__mutmut_54, 
        'xǁCDPBaseǁsend__mutmut_55': xǁCDPBaseǁsend__mutmut_55, 
        'xǁCDPBaseǁsend__mutmut_56': xǁCDPBaseǁsend__mutmut_56, 
        'xǁCDPBaseǁsend__mutmut_57': xǁCDPBaseǁsend__mutmut_57, 
        'xǁCDPBaseǁsend__mutmut_58': xǁCDPBaseǁsend__mutmut_58, 
        'xǁCDPBaseǁsend__mutmut_59': xǁCDPBaseǁsend__mutmut_59, 
        'xǁCDPBaseǁsend__mutmut_60': xǁCDPBaseǁsend__mutmut_60
    }
    
    def send(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPBaseǁsend__mutmut_orig"), object.__getattribute__(self, "xǁCDPBaseǁsend__mutmut_mutants"), args, kwargs, self)
        return result 
    
    send.__signature__ = _mutmut_signature(xǁCDPBaseǁsend__mutmut_orig)
    xǁCDPBaseǁsend__mutmut_orig.__name__ = 'xǁCDPBaseǁsend'

    def xǁCDPBaseǁlisten__mutmut_orig(self, event: type[TEvent], max_buffer_size: int | None = None) -> CDPEventListener[TEvent]:
        """
        Listen to a CDP event and return a new :class:`CDPEventListener` instance.

        :param event: See the ``streamlink.webbrowser.cdp.devtools`` package for the available events.
                      For events to be sent over the CDP connection, a specific domain needs to be enabled first.
        :param max_buffer_size: The buffer size of the ``trio`` memory channel.
        :return:
        """

        return CDPEventListener(self.event_channels, event, max_buffer_size)

    def xǁCDPBaseǁlisten__mutmut_1(self, event: type[TEvent], max_buffer_size: int | None = None) -> CDPEventListener[TEvent]:
        """
        Listen to a CDP event and return a new :class:`CDPEventListener` instance.

        :param event: See the ``streamlink.webbrowser.cdp.devtools`` package for the available events.
                      For events to be sent over the CDP connection, a specific domain needs to be enabled first.
        :param max_buffer_size: The buffer size of the ``trio`` memory channel.
        :return:
        """

        return CDPEventListener(None, event, max_buffer_size)

    def xǁCDPBaseǁlisten__mutmut_2(self, event: type[TEvent], max_buffer_size: int | None = None) -> CDPEventListener[TEvent]:
        """
        Listen to a CDP event and return a new :class:`CDPEventListener` instance.

        :param event: See the ``streamlink.webbrowser.cdp.devtools`` package for the available events.
                      For events to be sent over the CDP connection, a specific domain needs to be enabled first.
        :param max_buffer_size: The buffer size of the ``trio`` memory channel.
        :return:
        """

        return CDPEventListener(self.event_channels, None, max_buffer_size)

    def xǁCDPBaseǁlisten__mutmut_3(self, event: type[TEvent], max_buffer_size: int | None = None) -> CDPEventListener[TEvent]:
        """
        Listen to a CDP event and return a new :class:`CDPEventListener` instance.

        :param event: See the ``streamlink.webbrowser.cdp.devtools`` package for the available events.
                      For events to be sent over the CDP connection, a specific domain needs to be enabled first.
        :param max_buffer_size: The buffer size of the ``trio`` memory channel.
        :return:
        """

        return CDPEventListener(self.event_channels, event, None)

    def xǁCDPBaseǁlisten__mutmut_4(self, event: type[TEvent], max_buffer_size: int | None = None) -> CDPEventListener[TEvent]:
        """
        Listen to a CDP event and return a new :class:`CDPEventListener` instance.

        :param event: See the ``streamlink.webbrowser.cdp.devtools`` package for the available events.
                      For events to be sent over the CDP connection, a specific domain needs to be enabled first.
        :param max_buffer_size: The buffer size of the ``trio`` memory channel.
        :return:
        """

        return CDPEventListener(event, max_buffer_size)

    def xǁCDPBaseǁlisten__mutmut_5(self, event: type[TEvent], max_buffer_size: int | None = None) -> CDPEventListener[TEvent]:
        """
        Listen to a CDP event and return a new :class:`CDPEventListener` instance.

        :param event: See the ``streamlink.webbrowser.cdp.devtools`` package for the available events.
                      For events to be sent over the CDP connection, a specific domain needs to be enabled first.
        :param max_buffer_size: The buffer size of the ``trio`` memory channel.
        :return:
        """

        return CDPEventListener(self.event_channels, max_buffer_size)

    def xǁCDPBaseǁlisten__mutmut_6(self, event: type[TEvent], max_buffer_size: int | None = None) -> CDPEventListener[TEvent]:
        """
        Listen to a CDP event and return a new :class:`CDPEventListener` instance.

        :param event: See the ``streamlink.webbrowser.cdp.devtools`` package for the available events.
                      For events to be sent over the CDP connection, a specific domain needs to be enabled first.
        :param max_buffer_size: The buffer size of the ``trio`` memory channel.
        :return:
        """

        return CDPEventListener(self.event_channels, event, )
    
    xǁCDPBaseǁlisten__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPBaseǁlisten__mutmut_1': xǁCDPBaseǁlisten__mutmut_1, 
        'xǁCDPBaseǁlisten__mutmut_2': xǁCDPBaseǁlisten__mutmut_2, 
        'xǁCDPBaseǁlisten__mutmut_3': xǁCDPBaseǁlisten__mutmut_3, 
        'xǁCDPBaseǁlisten__mutmut_4': xǁCDPBaseǁlisten__mutmut_4, 
        'xǁCDPBaseǁlisten__mutmut_5': xǁCDPBaseǁlisten__mutmut_5, 
        'xǁCDPBaseǁlisten__mutmut_6': xǁCDPBaseǁlisten__mutmut_6
    }
    
    def listen(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPBaseǁlisten__mutmut_orig"), object.__getattribute__(self, "xǁCDPBaseǁlisten__mutmut_mutants"), args, kwargs, self)
        return result 
    
    listen.__signature__ = _mutmut_signature(xǁCDPBaseǁlisten__mutmut_orig)
    xǁCDPBaseǁlisten__mutmut_orig.__name__ = 'xǁCDPBaseǁlisten'

    def xǁCDPBaseǁ_handle_data__mutmut_orig(self, data: T_JSON_DICT) -> None:
        if "id" in data:
            self._handle_cmd_response(data)
        else:
            self._handle_event(data)

    def xǁCDPBaseǁ_handle_data__mutmut_1(self, data: T_JSON_DICT) -> None:
        if "XXidXX" in data:
            self._handle_cmd_response(data)
        else:
            self._handle_event(data)

    def xǁCDPBaseǁ_handle_data__mutmut_2(self, data: T_JSON_DICT) -> None:
        if "ID" in data:
            self._handle_cmd_response(data)
        else:
            self._handle_event(data)

    def xǁCDPBaseǁ_handle_data__mutmut_3(self, data: T_JSON_DICT) -> None:
        if "Id" in data:
            self._handle_cmd_response(data)
        else:
            self._handle_event(data)

    def xǁCDPBaseǁ_handle_data__mutmut_4(self, data: T_JSON_DICT) -> None:
        if "id" not in data:
            self._handle_cmd_response(data)
        else:
            self._handle_event(data)

    def xǁCDPBaseǁ_handle_data__mutmut_5(self, data: T_JSON_DICT) -> None:
        if "id" in data:
            self._handle_cmd_response(None)
        else:
            self._handle_event(data)

    def xǁCDPBaseǁ_handle_data__mutmut_6(self, data: T_JSON_DICT) -> None:
        if "id" in data:
            self._handle_cmd_response(data)
        else:
            self._handle_event(None)
    
    xǁCDPBaseǁ_handle_data__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPBaseǁ_handle_data__mutmut_1': xǁCDPBaseǁ_handle_data__mutmut_1, 
        'xǁCDPBaseǁ_handle_data__mutmut_2': xǁCDPBaseǁ_handle_data__mutmut_2, 
        'xǁCDPBaseǁ_handle_data__mutmut_3': xǁCDPBaseǁ_handle_data__mutmut_3, 
        'xǁCDPBaseǁ_handle_data__mutmut_4': xǁCDPBaseǁ_handle_data__mutmut_4, 
        'xǁCDPBaseǁ_handle_data__mutmut_5': xǁCDPBaseǁ_handle_data__mutmut_5, 
        'xǁCDPBaseǁ_handle_data__mutmut_6': xǁCDPBaseǁ_handle_data__mutmut_6
    }
    
    def _handle_data(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPBaseǁ_handle_data__mutmut_orig"), object.__getattribute__(self, "xǁCDPBaseǁ_handle_data__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _handle_data.__signature__ = _mutmut_signature(xǁCDPBaseǁ_handle_data__mutmut_orig)
    xǁCDPBaseǁ_handle_data__mutmut_orig.__name__ = 'xǁCDPBaseǁ_handle_data'

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_orig(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_1(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = None
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_2(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["XXidXX"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_3(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["ID"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_4(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["Id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_5(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = None
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_6(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(None)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_7(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(None, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_8(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, None, dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_9(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", None)
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_10(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log("Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_11(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_12(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", )
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_13(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "XXGot a CDP command response with an unknown ID: %(id)rXX", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_14(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "got a cdp command response with an unknown id: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_15(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "GOT A CDP COMMAND RESPONSE WITH AN UNKNOWN ID: %(ID)R", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_16(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a cdp command response with an unknown id: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_17(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(idXX=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_18(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=None))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_19(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get(None)))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_20(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("XXidXX")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_21(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("ID")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_22(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("Id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_23(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "XXerrorXX" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_24(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "ERROR" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_25(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "Error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_26(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" not in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_27(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(None)
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_28(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(None))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_29(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['XXerrorXX']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_30(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['ERROR']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_31(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['Error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_32(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "XXresultXX" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_33(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "RESULT" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_34(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "Result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_35(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_36(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(None)
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_37(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(None))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_38(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = None
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_39(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["XXresultXX"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_40(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["RESULT"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_41(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["Result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_42(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(None)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_43(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(None)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_44(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(None)
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_45(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(None))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_46(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(None).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} did not exit when expected!"))

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_47(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(None)

    def xǁCDPBaseǁ_handle_cmd_response__mutmut_48(self, data: T_JSON_DICT) -> None:
        try:
            cmd_id: int = data["id"]
            cmd_buffer = self.cmd_buffers.pop(cmd_id)
        except KeyError:
            log.log(WARNING, "Got a CDP command response with an unknown ID: %(id)r", dict(id=data.get("id")))
            return

        if "error" in data:
            cmd_buffer.set_response(CDPError(f"Error in CDP command response {cmd_id}: {data['error']}"))
            return
        if "result" not in data:
            cmd_buffer.set_response(CDPError(f"No result in CDP command response {cmd_id}"))
            return

        cmd_result: T_JSON_DICT = data["result"]
        try:
            # send the response to the command's generator function (the first send() must stop the generator)
            cmd_buffer.cmd.send(cmd_result)
        except StopIteration as cm:
            # and on success, set the response result
            cmd_buffer.set_response(cm.value)
        except Exception as err:
            # handle any errors raised by the generator's result logic
            cmd_buffer.set_response(CDPError(f"Generator of CDP command ID {cmd_id} raised {type(err).__name__}: {err}"))
        else:
            cmd_buffer.set_response(CDPError(None))
    
    xǁCDPBaseǁ_handle_cmd_response__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPBaseǁ_handle_cmd_response__mutmut_1': xǁCDPBaseǁ_handle_cmd_response__mutmut_1, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_2': xǁCDPBaseǁ_handle_cmd_response__mutmut_2, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_3': xǁCDPBaseǁ_handle_cmd_response__mutmut_3, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_4': xǁCDPBaseǁ_handle_cmd_response__mutmut_4, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_5': xǁCDPBaseǁ_handle_cmd_response__mutmut_5, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_6': xǁCDPBaseǁ_handle_cmd_response__mutmut_6, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_7': xǁCDPBaseǁ_handle_cmd_response__mutmut_7, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_8': xǁCDPBaseǁ_handle_cmd_response__mutmut_8, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_9': xǁCDPBaseǁ_handle_cmd_response__mutmut_9, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_10': xǁCDPBaseǁ_handle_cmd_response__mutmut_10, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_11': xǁCDPBaseǁ_handle_cmd_response__mutmut_11, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_12': xǁCDPBaseǁ_handle_cmd_response__mutmut_12, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_13': xǁCDPBaseǁ_handle_cmd_response__mutmut_13, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_14': xǁCDPBaseǁ_handle_cmd_response__mutmut_14, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_15': xǁCDPBaseǁ_handle_cmd_response__mutmut_15, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_16': xǁCDPBaseǁ_handle_cmd_response__mutmut_16, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_17': xǁCDPBaseǁ_handle_cmd_response__mutmut_17, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_18': xǁCDPBaseǁ_handle_cmd_response__mutmut_18, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_19': xǁCDPBaseǁ_handle_cmd_response__mutmut_19, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_20': xǁCDPBaseǁ_handle_cmd_response__mutmut_20, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_21': xǁCDPBaseǁ_handle_cmd_response__mutmut_21, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_22': xǁCDPBaseǁ_handle_cmd_response__mutmut_22, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_23': xǁCDPBaseǁ_handle_cmd_response__mutmut_23, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_24': xǁCDPBaseǁ_handle_cmd_response__mutmut_24, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_25': xǁCDPBaseǁ_handle_cmd_response__mutmut_25, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_26': xǁCDPBaseǁ_handle_cmd_response__mutmut_26, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_27': xǁCDPBaseǁ_handle_cmd_response__mutmut_27, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_28': xǁCDPBaseǁ_handle_cmd_response__mutmut_28, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_29': xǁCDPBaseǁ_handle_cmd_response__mutmut_29, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_30': xǁCDPBaseǁ_handle_cmd_response__mutmut_30, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_31': xǁCDPBaseǁ_handle_cmd_response__mutmut_31, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_32': xǁCDPBaseǁ_handle_cmd_response__mutmut_32, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_33': xǁCDPBaseǁ_handle_cmd_response__mutmut_33, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_34': xǁCDPBaseǁ_handle_cmd_response__mutmut_34, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_35': xǁCDPBaseǁ_handle_cmd_response__mutmut_35, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_36': xǁCDPBaseǁ_handle_cmd_response__mutmut_36, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_37': xǁCDPBaseǁ_handle_cmd_response__mutmut_37, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_38': xǁCDPBaseǁ_handle_cmd_response__mutmut_38, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_39': xǁCDPBaseǁ_handle_cmd_response__mutmut_39, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_40': xǁCDPBaseǁ_handle_cmd_response__mutmut_40, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_41': xǁCDPBaseǁ_handle_cmd_response__mutmut_41, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_42': xǁCDPBaseǁ_handle_cmd_response__mutmut_42, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_43': xǁCDPBaseǁ_handle_cmd_response__mutmut_43, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_44': xǁCDPBaseǁ_handle_cmd_response__mutmut_44, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_45': xǁCDPBaseǁ_handle_cmd_response__mutmut_45, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_46': xǁCDPBaseǁ_handle_cmd_response__mutmut_46, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_47': xǁCDPBaseǁ_handle_cmd_response__mutmut_47, 
        'xǁCDPBaseǁ_handle_cmd_response__mutmut_48': xǁCDPBaseǁ_handle_cmd_response__mutmut_48
    }
    
    def _handle_cmd_response(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPBaseǁ_handle_cmd_response__mutmut_orig"), object.__getattribute__(self, "xǁCDPBaseǁ_handle_cmd_response__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _handle_cmd_response.__signature__ = _mutmut_signature(xǁCDPBaseǁ_handle_cmd_response__mutmut_orig)
    xǁCDPBaseǁ_handle_cmd_response__mutmut_orig.__name__ = 'xǁCDPBaseǁ_handle_cmd_response'

    def xǁCDPBaseǁ_handle_event__mutmut_orig(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_1(self, data: T_JSON_DICT) -> None:
        if "XXmethodXX" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_2(self, data: T_JSON_DICT) -> None:
        if "METHOD" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_3(self, data: T_JSON_DICT) -> None:
        if "Method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_4(self, data: T_JSON_DICT) -> None:
        if "method" in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_5(self, data: T_JSON_DICT) -> None:
        if "method" not in data and "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_6(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "XXparamsXX" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_7(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "PARAMS" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_8(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "Params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_9(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_10(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning(None)
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_11(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("XXInvalid CDP event message received without method or paramsXX")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_12(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("invalid cdp event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_13(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("INVALID CDP EVENT MESSAGE RECEIVED WITHOUT METHOD OR PARAMS")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_14(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid cdp event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_15(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = None
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_16(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(None)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_17(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(None)
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_18(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['XXmethodXX']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_19(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['METHOD']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_20(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['Method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_21(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(None, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_22(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, None, dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_23(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", None)
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_24(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log("Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_25(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_26(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", )
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_27(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "XXReceived event: %(event)rXX", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_28(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_29(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "RECEIVED EVENT: %(EVENT)R", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_30(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(eventXX=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_31(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=None))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_32(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = None
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_33(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(None)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_34(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(None)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_35(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(None, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_36(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, None, dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_37(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", None)
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_38(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log("Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_39(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_40(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", )
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_41(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "XXUnable to propagate CDP event %(event)r due to full channelXX", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_42(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "unable to propagate cdp event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_43(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "UNABLE TO PROPAGATE CDP EVENT %(EVENT)R DUE TO FULL CHANNEL", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_44(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate cdp event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_45(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(eventXX=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_46(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=None))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_47(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(None)
                sender.close()
        self.event_channels[type(event)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_48(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] = broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_49(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(None)] -= broken_channels

    def xǁCDPBaseǁ_handle_event__mutmut_50(self, data: T_JSON_DICT) -> None:
        if "method" not in data or "params" not in data:
            log.warning("Invalid CDP event message received without method or params")
            return

        try:
            event = parse_json_event(data)
        except KeyError:
            log.warning(f"Unknown CDP event message received: {data['method']}")
            return

        log.log(ALL, "Received event: %(event)r", dict(event=event))
        broken_channels = set()
        for sender in self.event_channels[type(event)]:
            try:
                sender.send_nowait(event)
            except trio.WouldBlock:
                log.log(ERROR, "Unable to propagate CDP event %(event)r due to full channel", dict(event=event))
            except trio.BrokenResourceError:
                broken_channels.add(sender)
                sender.close()
        self.event_channels[type(event)] += broken_channels
    
    xǁCDPBaseǁ_handle_event__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPBaseǁ_handle_event__mutmut_1': xǁCDPBaseǁ_handle_event__mutmut_1, 
        'xǁCDPBaseǁ_handle_event__mutmut_2': xǁCDPBaseǁ_handle_event__mutmut_2, 
        'xǁCDPBaseǁ_handle_event__mutmut_3': xǁCDPBaseǁ_handle_event__mutmut_3, 
        'xǁCDPBaseǁ_handle_event__mutmut_4': xǁCDPBaseǁ_handle_event__mutmut_4, 
        'xǁCDPBaseǁ_handle_event__mutmut_5': xǁCDPBaseǁ_handle_event__mutmut_5, 
        'xǁCDPBaseǁ_handle_event__mutmut_6': xǁCDPBaseǁ_handle_event__mutmut_6, 
        'xǁCDPBaseǁ_handle_event__mutmut_7': xǁCDPBaseǁ_handle_event__mutmut_7, 
        'xǁCDPBaseǁ_handle_event__mutmut_8': xǁCDPBaseǁ_handle_event__mutmut_8, 
        'xǁCDPBaseǁ_handle_event__mutmut_9': xǁCDPBaseǁ_handle_event__mutmut_9, 
        'xǁCDPBaseǁ_handle_event__mutmut_10': xǁCDPBaseǁ_handle_event__mutmut_10, 
        'xǁCDPBaseǁ_handle_event__mutmut_11': xǁCDPBaseǁ_handle_event__mutmut_11, 
        'xǁCDPBaseǁ_handle_event__mutmut_12': xǁCDPBaseǁ_handle_event__mutmut_12, 
        'xǁCDPBaseǁ_handle_event__mutmut_13': xǁCDPBaseǁ_handle_event__mutmut_13, 
        'xǁCDPBaseǁ_handle_event__mutmut_14': xǁCDPBaseǁ_handle_event__mutmut_14, 
        'xǁCDPBaseǁ_handle_event__mutmut_15': xǁCDPBaseǁ_handle_event__mutmut_15, 
        'xǁCDPBaseǁ_handle_event__mutmut_16': xǁCDPBaseǁ_handle_event__mutmut_16, 
        'xǁCDPBaseǁ_handle_event__mutmut_17': xǁCDPBaseǁ_handle_event__mutmut_17, 
        'xǁCDPBaseǁ_handle_event__mutmut_18': xǁCDPBaseǁ_handle_event__mutmut_18, 
        'xǁCDPBaseǁ_handle_event__mutmut_19': xǁCDPBaseǁ_handle_event__mutmut_19, 
        'xǁCDPBaseǁ_handle_event__mutmut_20': xǁCDPBaseǁ_handle_event__mutmut_20, 
        'xǁCDPBaseǁ_handle_event__mutmut_21': xǁCDPBaseǁ_handle_event__mutmut_21, 
        'xǁCDPBaseǁ_handle_event__mutmut_22': xǁCDPBaseǁ_handle_event__mutmut_22, 
        'xǁCDPBaseǁ_handle_event__mutmut_23': xǁCDPBaseǁ_handle_event__mutmut_23, 
        'xǁCDPBaseǁ_handle_event__mutmut_24': xǁCDPBaseǁ_handle_event__mutmut_24, 
        'xǁCDPBaseǁ_handle_event__mutmut_25': xǁCDPBaseǁ_handle_event__mutmut_25, 
        'xǁCDPBaseǁ_handle_event__mutmut_26': xǁCDPBaseǁ_handle_event__mutmut_26, 
        'xǁCDPBaseǁ_handle_event__mutmut_27': xǁCDPBaseǁ_handle_event__mutmut_27, 
        'xǁCDPBaseǁ_handle_event__mutmut_28': xǁCDPBaseǁ_handle_event__mutmut_28, 
        'xǁCDPBaseǁ_handle_event__mutmut_29': xǁCDPBaseǁ_handle_event__mutmut_29, 
        'xǁCDPBaseǁ_handle_event__mutmut_30': xǁCDPBaseǁ_handle_event__mutmut_30, 
        'xǁCDPBaseǁ_handle_event__mutmut_31': xǁCDPBaseǁ_handle_event__mutmut_31, 
        'xǁCDPBaseǁ_handle_event__mutmut_32': xǁCDPBaseǁ_handle_event__mutmut_32, 
        'xǁCDPBaseǁ_handle_event__mutmut_33': xǁCDPBaseǁ_handle_event__mutmut_33, 
        'xǁCDPBaseǁ_handle_event__mutmut_34': xǁCDPBaseǁ_handle_event__mutmut_34, 
        'xǁCDPBaseǁ_handle_event__mutmut_35': xǁCDPBaseǁ_handle_event__mutmut_35, 
        'xǁCDPBaseǁ_handle_event__mutmut_36': xǁCDPBaseǁ_handle_event__mutmut_36, 
        'xǁCDPBaseǁ_handle_event__mutmut_37': xǁCDPBaseǁ_handle_event__mutmut_37, 
        'xǁCDPBaseǁ_handle_event__mutmut_38': xǁCDPBaseǁ_handle_event__mutmut_38, 
        'xǁCDPBaseǁ_handle_event__mutmut_39': xǁCDPBaseǁ_handle_event__mutmut_39, 
        'xǁCDPBaseǁ_handle_event__mutmut_40': xǁCDPBaseǁ_handle_event__mutmut_40, 
        'xǁCDPBaseǁ_handle_event__mutmut_41': xǁCDPBaseǁ_handle_event__mutmut_41, 
        'xǁCDPBaseǁ_handle_event__mutmut_42': xǁCDPBaseǁ_handle_event__mutmut_42, 
        'xǁCDPBaseǁ_handle_event__mutmut_43': xǁCDPBaseǁ_handle_event__mutmut_43, 
        'xǁCDPBaseǁ_handle_event__mutmut_44': xǁCDPBaseǁ_handle_event__mutmut_44, 
        'xǁCDPBaseǁ_handle_event__mutmut_45': xǁCDPBaseǁ_handle_event__mutmut_45, 
        'xǁCDPBaseǁ_handle_event__mutmut_46': xǁCDPBaseǁ_handle_event__mutmut_46, 
        'xǁCDPBaseǁ_handle_event__mutmut_47': xǁCDPBaseǁ_handle_event__mutmut_47, 
        'xǁCDPBaseǁ_handle_event__mutmut_48': xǁCDPBaseǁ_handle_event__mutmut_48, 
        'xǁCDPBaseǁ_handle_event__mutmut_49': xǁCDPBaseǁ_handle_event__mutmut_49, 
        'xǁCDPBaseǁ_handle_event__mutmut_50': xǁCDPBaseǁ_handle_event__mutmut_50
    }
    
    def _handle_event(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPBaseǁ_handle_event__mutmut_orig"), object.__getattribute__(self, "xǁCDPBaseǁ_handle_event__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _handle_event.__signature__ = _mutmut_signature(xǁCDPBaseǁ_handle_event__mutmut_orig)
    xǁCDPBaseǁ_handle_event__mutmut_orig.__name__ = 'xǁCDPBaseǁ_handle_event'


class CDPConnection(CDPBase, trio.abc.AsyncResource):
    """
    Don't instantiate this class yourself, see its :meth:`create()` classmethod.
    """

    def xǁCDPConnectionǁ__init____mutmut_orig(self, websocket: WebSocketConnection, cmd_timeout: float) -> None:
        super().__init__(websocket=websocket, cmd_timeout=cmd_timeout)
        self.sessions: dict[SessionID, CDPSession] = {}

    def xǁCDPConnectionǁ__init____mutmut_1(self, websocket: WebSocketConnection, cmd_timeout: float) -> None:
        super().__init__(websocket=None, cmd_timeout=cmd_timeout)
        self.sessions: dict[SessionID, CDPSession] = {}

    def xǁCDPConnectionǁ__init____mutmut_2(self, websocket: WebSocketConnection, cmd_timeout: float) -> None:
        super().__init__(websocket=websocket, cmd_timeout=None)
        self.sessions: dict[SessionID, CDPSession] = {}

    def xǁCDPConnectionǁ__init____mutmut_3(self, websocket: WebSocketConnection, cmd_timeout: float) -> None:
        super().__init__(cmd_timeout=cmd_timeout)
        self.sessions: dict[SessionID, CDPSession] = {}

    def xǁCDPConnectionǁ__init____mutmut_4(self, websocket: WebSocketConnection, cmd_timeout: float) -> None:
        super().__init__(websocket=websocket, )
        self.sessions: dict[SessionID, CDPSession] = {}

    def xǁCDPConnectionǁ__init____mutmut_5(self, websocket: WebSocketConnection, cmd_timeout: float) -> None:
        super().__init__(websocket=websocket, cmd_timeout=cmd_timeout)
        self.sessions: dict[SessionID, CDPSession] = None
    
    xǁCDPConnectionǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPConnectionǁ__init____mutmut_1': xǁCDPConnectionǁ__init____mutmut_1, 
        'xǁCDPConnectionǁ__init____mutmut_2': xǁCDPConnectionǁ__init____mutmut_2, 
        'xǁCDPConnectionǁ__init____mutmut_3': xǁCDPConnectionǁ__init____mutmut_3, 
        'xǁCDPConnectionǁ__init____mutmut_4': xǁCDPConnectionǁ__init____mutmut_4, 
        'xǁCDPConnectionǁ__init____mutmut_5': xǁCDPConnectionǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPConnectionǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCDPConnectionǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCDPConnectionǁ__init____mutmut_orig)
    xǁCDPConnectionǁ__init____mutmut_orig.__name__ = 'xǁCDPConnectionǁ__init__'

    @classmethod
    @asynccontextmanager
    async def create(cls, url: str, timeout: float | None = None) -> AsyncGenerator[Self, None]:
        """
        Establish a new CDP connection to the Chromium-based web browser's remote debugging interface.

        :param url: The websocket address
        :param timeout: The max amount of time a single CDP command response can take.
        :return:
        """

        async with trio.open_nursery() as nursery:
            websocket = await connect_websocket_url(nursery, url, max_message_size=MAX_MESSAGE_SIZE)
            cdp_connection = cls(websocket, timeout or CMD_TIMEOUT)
            nursery.start_soon(cdp_connection._task_reader)
            try:
                yield cdp_connection
            finally:
                await cdp_connection.aclose()

    async def aclose(self) -> None:
        """
        Close the websocket connection, close all memory channels and clean up all opened sessions.
        """

        await self.websocket.aclose()
        inst: CDPBase
        for inst in (self, *self.sessions.values()):
            for event_channels in inst.event_channels.values():
                for event_channel in event_channels:
                    event_channel.close()
            inst.event_channels.clear()
        self.sessions.clear()

    async def xǁCDPConnectionǁnew_target__mutmut_orig(self, url: str = "") -> CDPSession:
        """
        Create a new target (browser tab) and return a new :class:`CDPSession` instance.

        :param url: Optional URL. Leave empty for a blank target (preferred for proper navigation handling).
        :return:
        """

        target_id = await self.send(create_target(url))

        return await self.get_session(target_id)

    async def xǁCDPConnectionǁnew_target__mutmut_1(self, url: str = "XXXX") -> CDPSession:
        """
        Create a new target (browser tab) and return a new :class:`CDPSession` instance.

        :param url: Optional URL. Leave empty for a blank target (preferred for proper navigation handling).
        :return:
        """

        target_id = await self.send(create_target(url))

        return await self.get_session(target_id)

    async def xǁCDPConnectionǁnew_target__mutmut_2(self, url: str = "") -> CDPSession:
        """
        Create a new target (browser tab) and return a new :class:`CDPSession` instance.

        :param url: Optional URL. Leave empty for a blank target (preferred for proper navigation handling).
        :return:
        """

        target_id = None

        return await self.get_session(target_id)

    async def xǁCDPConnectionǁnew_target__mutmut_3(self, url: str = "") -> CDPSession:
        """
        Create a new target (browser tab) and return a new :class:`CDPSession` instance.

        :param url: Optional URL. Leave empty for a blank target (preferred for proper navigation handling).
        :return:
        """

        target_id = await self.send(None)

        return await self.get_session(target_id)

    async def xǁCDPConnectionǁnew_target__mutmut_4(self, url: str = "") -> CDPSession:
        """
        Create a new target (browser tab) and return a new :class:`CDPSession` instance.

        :param url: Optional URL. Leave empty for a blank target (preferred for proper navigation handling).
        :return:
        """

        target_id = await self.send(create_target(None))

        return await self.get_session(target_id)

    async def xǁCDPConnectionǁnew_target__mutmut_5(self, url: str = "") -> CDPSession:
        """
        Create a new target (browser tab) and return a new :class:`CDPSession` instance.

        :param url: Optional URL. Leave empty for a blank target (preferred for proper navigation handling).
        :return:
        """

        target_id = await self.send(create_target(url))

        return await self.get_session(None)
    
    xǁCDPConnectionǁnew_target__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPConnectionǁnew_target__mutmut_1': xǁCDPConnectionǁnew_target__mutmut_1, 
        'xǁCDPConnectionǁnew_target__mutmut_2': xǁCDPConnectionǁnew_target__mutmut_2, 
        'xǁCDPConnectionǁnew_target__mutmut_3': xǁCDPConnectionǁnew_target__mutmut_3, 
        'xǁCDPConnectionǁnew_target__mutmut_4': xǁCDPConnectionǁnew_target__mutmut_4, 
        'xǁCDPConnectionǁnew_target__mutmut_5': xǁCDPConnectionǁnew_target__mutmut_5
    }
    
    def new_target(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPConnectionǁnew_target__mutmut_orig"), object.__getattribute__(self, "xǁCDPConnectionǁnew_target__mutmut_mutants"), args, kwargs, self)
        return result 
    
    new_target.__signature__ = _mutmut_signature(xǁCDPConnectionǁnew_target__mutmut_orig)
    xǁCDPConnectionǁnew_target__mutmut_orig.__name__ = 'xǁCDPConnectionǁnew_target'

    async def xǁCDPConnectionǁget_session__mutmut_orig(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_1(self, target_id: TargetID) -> CDPSession:
        session_id = None
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_2(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(None)
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_3(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(None, True))
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_4(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, None))
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_5(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(True))
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_6(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, ))
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_7(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, False))
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_8(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = None
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_9(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = CDPSession(None, target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_10(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = CDPSession(self.websocket, target_id=None, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_11(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=None, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_12(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, cmd_timeout=None)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_13(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = CDPSession(target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_14(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = CDPSession(self.websocket, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_15(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = CDPSession(self.websocket, target_id=target_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_16(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, )
        self.sessions[session_id] = cdp_session

        return cdp_session

    async def xǁCDPConnectionǁget_session__mutmut_17(self, target_id: TargetID) -> CDPSession:
        session_id = await self.send(attach_to_target(target_id, True))
        cdp_session = CDPSession(self.websocket, target_id=target_id, session_id=session_id, cmd_timeout=self.cmd_timeout)
        self.sessions[session_id] = None

        return cdp_session
    
    xǁCDPConnectionǁget_session__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPConnectionǁget_session__mutmut_1': xǁCDPConnectionǁget_session__mutmut_1, 
        'xǁCDPConnectionǁget_session__mutmut_2': xǁCDPConnectionǁget_session__mutmut_2, 
        'xǁCDPConnectionǁget_session__mutmut_3': xǁCDPConnectionǁget_session__mutmut_3, 
        'xǁCDPConnectionǁget_session__mutmut_4': xǁCDPConnectionǁget_session__mutmut_4, 
        'xǁCDPConnectionǁget_session__mutmut_5': xǁCDPConnectionǁget_session__mutmut_5, 
        'xǁCDPConnectionǁget_session__mutmut_6': xǁCDPConnectionǁget_session__mutmut_6, 
        'xǁCDPConnectionǁget_session__mutmut_7': xǁCDPConnectionǁget_session__mutmut_7, 
        'xǁCDPConnectionǁget_session__mutmut_8': xǁCDPConnectionǁget_session__mutmut_8, 
        'xǁCDPConnectionǁget_session__mutmut_9': xǁCDPConnectionǁget_session__mutmut_9, 
        'xǁCDPConnectionǁget_session__mutmut_10': xǁCDPConnectionǁget_session__mutmut_10, 
        'xǁCDPConnectionǁget_session__mutmut_11': xǁCDPConnectionǁget_session__mutmut_11, 
        'xǁCDPConnectionǁget_session__mutmut_12': xǁCDPConnectionǁget_session__mutmut_12, 
        'xǁCDPConnectionǁget_session__mutmut_13': xǁCDPConnectionǁget_session__mutmut_13, 
        'xǁCDPConnectionǁget_session__mutmut_14': xǁCDPConnectionǁget_session__mutmut_14, 
        'xǁCDPConnectionǁget_session__mutmut_15': xǁCDPConnectionǁget_session__mutmut_15, 
        'xǁCDPConnectionǁget_session__mutmut_16': xǁCDPConnectionǁget_session__mutmut_16, 
        'xǁCDPConnectionǁget_session__mutmut_17': xǁCDPConnectionǁget_session__mutmut_17
    }
    
    def get_session(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPConnectionǁget_session__mutmut_orig"), object.__getattribute__(self, "xǁCDPConnectionǁget_session__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_session.__signature__ = _mutmut_signature(xǁCDPConnectionǁget_session__mutmut_orig)
    xǁCDPConnectionǁget_session__mutmut_orig.__name__ = 'xǁCDPConnectionǁget_session'

    async def xǁCDPConnectionǁ_task_reader__mutmut_orig(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_1(self) -> None:
        while False:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_2(self) -> None:
        while True:
            try:
                message = None
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_3(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                return

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_4(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = None
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_5(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(None)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_6(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(None) from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_7(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(None, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_8(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, None, dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_9(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", None)
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_10(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log("Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_11(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_12(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", )
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_13(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "XXReceived message: %(message)sXX", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_14(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_15(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "RECEIVED MESSAGE: %(MESSAGE)S", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_16(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(messageXX=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_17(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=None))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_18(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "XXsessionIdXX" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_19(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionid" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_20(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "SESSIONID" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_21(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "Sessionid" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_22(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_23(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(None)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_24(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = None
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_25(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(None)
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_26(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["XXsessionIdXX"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_27(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionid"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_28(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["SESSIONID"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_29(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["Sessionid"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_30(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_31(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(None)
                self.sessions[session_id]._handle_data(data)

    async def xǁCDPConnectionǁ_task_reader__mutmut_32(self) -> None:
        while True:
            try:
                message = await self.websocket.get_message()
            except ConnectionClosed:
                break

            try:
                data = json.loads(message)
            except json.JSONDecodeError as err:
                raise CDPError(f"Received invalid CDP JSON data: {err}") from err

            log.log(ALL, "Received message: %(message)s", dict(message=message))
            if "sessionId" not in data:
                self._handle_data(data)
            else:
                session_id = SessionID(data["sessionId"])
                if session_id not in self.sessions:
                    raise CDPError(f"Unknown CDP session ID: {session_id!r}")
                self.sessions[session_id]._handle_data(None)
    
    xǁCDPConnectionǁ_task_reader__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPConnectionǁ_task_reader__mutmut_1': xǁCDPConnectionǁ_task_reader__mutmut_1, 
        'xǁCDPConnectionǁ_task_reader__mutmut_2': xǁCDPConnectionǁ_task_reader__mutmut_2, 
        'xǁCDPConnectionǁ_task_reader__mutmut_3': xǁCDPConnectionǁ_task_reader__mutmut_3, 
        'xǁCDPConnectionǁ_task_reader__mutmut_4': xǁCDPConnectionǁ_task_reader__mutmut_4, 
        'xǁCDPConnectionǁ_task_reader__mutmut_5': xǁCDPConnectionǁ_task_reader__mutmut_5, 
        'xǁCDPConnectionǁ_task_reader__mutmut_6': xǁCDPConnectionǁ_task_reader__mutmut_6, 
        'xǁCDPConnectionǁ_task_reader__mutmut_7': xǁCDPConnectionǁ_task_reader__mutmut_7, 
        'xǁCDPConnectionǁ_task_reader__mutmut_8': xǁCDPConnectionǁ_task_reader__mutmut_8, 
        'xǁCDPConnectionǁ_task_reader__mutmut_9': xǁCDPConnectionǁ_task_reader__mutmut_9, 
        'xǁCDPConnectionǁ_task_reader__mutmut_10': xǁCDPConnectionǁ_task_reader__mutmut_10, 
        'xǁCDPConnectionǁ_task_reader__mutmut_11': xǁCDPConnectionǁ_task_reader__mutmut_11, 
        'xǁCDPConnectionǁ_task_reader__mutmut_12': xǁCDPConnectionǁ_task_reader__mutmut_12, 
        'xǁCDPConnectionǁ_task_reader__mutmut_13': xǁCDPConnectionǁ_task_reader__mutmut_13, 
        'xǁCDPConnectionǁ_task_reader__mutmut_14': xǁCDPConnectionǁ_task_reader__mutmut_14, 
        'xǁCDPConnectionǁ_task_reader__mutmut_15': xǁCDPConnectionǁ_task_reader__mutmut_15, 
        'xǁCDPConnectionǁ_task_reader__mutmut_16': xǁCDPConnectionǁ_task_reader__mutmut_16, 
        'xǁCDPConnectionǁ_task_reader__mutmut_17': xǁCDPConnectionǁ_task_reader__mutmut_17, 
        'xǁCDPConnectionǁ_task_reader__mutmut_18': xǁCDPConnectionǁ_task_reader__mutmut_18, 
        'xǁCDPConnectionǁ_task_reader__mutmut_19': xǁCDPConnectionǁ_task_reader__mutmut_19, 
        'xǁCDPConnectionǁ_task_reader__mutmut_20': xǁCDPConnectionǁ_task_reader__mutmut_20, 
        'xǁCDPConnectionǁ_task_reader__mutmut_21': xǁCDPConnectionǁ_task_reader__mutmut_21, 
        'xǁCDPConnectionǁ_task_reader__mutmut_22': xǁCDPConnectionǁ_task_reader__mutmut_22, 
        'xǁCDPConnectionǁ_task_reader__mutmut_23': xǁCDPConnectionǁ_task_reader__mutmut_23, 
        'xǁCDPConnectionǁ_task_reader__mutmut_24': xǁCDPConnectionǁ_task_reader__mutmut_24, 
        'xǁCDPConnectionǁ_task_reader__mutmut_25': xǁCDPConnectionǁ_task_reader__mutmut_25, 
        'xǁCDPConnectionǁ_task_reader__mutmut_26': xǁCDPConnectionǁ_task_reader__mutmut_26, 
        'xǁCDPConnectionǁ_task_reader__mutmut_27': xǁCDPConnectionǁ_task_reader__mutmut_27, 
        'xǁCDPConnectionǁ_task_reader__mutmut_28': xǁCDPConnectionǁ_task_reader__mutmut_28, 
        'xǁCDPConnectionǁ_task_reader__mutmut_29': xǁCDPConnectionǁ_task_reader__mutmut_29, 
        'xǁCDPConnectionǁ_task_reader__mutmut_30': xǁCDPConnectionǁ_task_reader__mutmut_30, 
        'xǁCDPConnectionǁ_task_reader__mutmut_31': xǁCDPConnectionǁ_task_reader__mutmut_31, 
        'xǁCDPConnectionǁ_task_reader__mutmut_32': xǁCDPConnectionǁ_task_reader__mutmut_32
    }
    
    def _task_reader(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPConnectionǁ_task_reader__mutmut_orig"), object.__getattribute__(self, "xǁCDPConnectionǁ_task_reader__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _task_reader.__signature__ = _mutmut_signature(xǁCDPConnectionǁ_task_reader__mutmut_orig)
    xǁCDPConnectionǁ_task_reader__mutmut_orig.__name__ = 'xǁCDPConnectionǁ_task_reader'


class CDPSession(CDPBase):
    pass

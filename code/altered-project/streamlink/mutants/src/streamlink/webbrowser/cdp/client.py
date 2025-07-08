from __future__ import annotations

import base64
import re
from collections.abc import AsyncGenerator, Awaitable, Callable, Coroutine, Mapping
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

import trio

from streamlink.session import Streamlink
from streamlink.webbrowser.cdp.connection import CDPConnection, CDPSession
from streamlink.webbrowser.cdp.devtools import fetch, network, page, runtime, target
from streamlink.webbrowser.cdp.exceptions import CDPError
from streamlink.webbrowser.chromium import ChromiumWebbrowser


if TYPE_CHECKING:
    try:
        from typing import Self, TypeAlias  # type: ignore[attr-defined]
    except ImportError:
        from typing_extensions import Self, TypeAlias


TRequestHandlerCallable: TypeAlias = "Callable[[CDPClientSession, fetch.RequestPaused], Awaitable]"


_re_url_pattern_wildcard = re.compile(r"(.+?)?(\\+)?([*?])")
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
class RequestPausedHandler:
    async_handler: TRequestHandlerCallable
    url_pattern: str = "*"
    on_request: bool = False

    def __post_init__(self) -> None:
        self._re_url: re.Pattern = self._url_pattern_to_regex_pattern(self.url_pattern)

    def matches(self, request: fetch.RequestPaused) -> bool:
        on_request: bool = request.response_status_code is None and request.response_error_reason is None
        return on_request is self.on_request and self._re_url.match(request.request.url) is not None

    @staticmethod
    def _url_pattern_to_regex_pattern(url_pattern: str) -> re.Pattern:
        pos = 0
        regex = ""

        for match in _re_url_pattern_wildcard.finditer(url_pattern):
            regex += re.escape(match[1]) if match[1] else ""
            if match[2]:
                if len(match[2]) % 2:
                    regex += f"{re.escape(match[2][:-1])}\\{match[3]}"
                else:
                    regex += re.escape(match[2])
                    regex += ".+" if match[3] == "*" else "."
            else:
                regex += ".+" if match[3] == "*" else "."

            pos = match.end()

        regex += re.escape(url_pattern[pos:])

        return re.compile(f"^{regex}$")


@dataclass
class CMRequestProxy:
    body: str
    response_code: int
    response_headers: Mapping[str, str] | None


class CDPClient:
    """
    The public interface around :class:`ChromiumWebbrowser <streamlink.webbrowser.chromium.ChromiumWebbrowser>`
    and :class:`CDPConnection <streamlink.webbrowser.cdp.connection.CDPConnection>`.

    It launches the Chromium-based web browser, establishes the remote debugging WebSocket connection using
    the `Chrome Devtools Protocol <https://chromedevtools.github.io/devtools-protocol/>`_,  and provides
    the :meth:`session()` method for creating a new :class:`CDPClientSession` that is tied to an empty new browser tab.

    :class:`CDPClientSession` provides a high-level API for navigating websites, intercepting network requests and responses,
    as well as evaluating JavaScript expressions and retrieving async results.

    Don't instantiate this class yourself, use the :meth:`CDPClient.launch()` async context manager classmethod.

    For low-level Chrome Devtools Protocol interfaces, please see Streamlink's automatically generated
    ``streamlink.webbrowser.cdp.devtools`` package, but be aware that only a subset of the available domains is supported.
    """

    def xǁCDPClientǁ__init____mutmut_orig(self, cdp_connection: CDPConnection, nursery: trio.Nursery, headless: bool):
        self.cdp_connection = cdp_connection
        self.nursery = nursery
        self.headless = headless

    def xǁCDPClientǁ__init____mutmut_1(self, cdp_connection: CDPConnection, nursery: trio.Nursery, headless: bool):
        self.cdp_connection = None
        self.nursery = nursery
        self.headless = headless

    def xǁCDPClientǁ__init____mutmut_2(self, cdp_connection: CDPConnection, nursery: trio.Nursery, headless: bool):
        self.cdp_connection = cdp_connection
        self.nursery = None
        self.headless = headless

    def xǁCDPClientǁ__init____mutmut_3(self, cdp_connection: CDPConnection, nursery: trio.Nursery, headless: bool):
        self.cdp_connection = cdp_connection
        self.nursery = nursery
        self.headless = None
    
    xǁCDPClientǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientǁ__init____mutmut_1': xǁCDPClientǁ__init____mutmut_1, 
        'xǁCDPClientǁ__init____mutmut_2': xǁCDPClientǁ__init____mutmut_2, 
        'xǁCDPClientǁ__init____mutmut_3': xǁCDPClientǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCDPClientǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCDPClientǁ__init____mutmut_orig)
    xǁCDPClientǁ__init____mutmut_orig.__name__ = 'xǁCDPClientǁ__init__'

    @classmethod
    def launch(
        cls,
        session: Streamlink,
        runner: Callable[[Self], Coroutine],
        executable: str | None = None,
        timeout: float | None = None,
        cdp_host: str | None = None,
        cdp_port: int | None = None,
        cdp_timeout: float | None = None,
        headless: bool | None = None,
    ) -> Any:
        """
        Start a new :mod:`trio` runloop and do the following things:

        1. Launch the Chromium-based web browser using the provided parameters or respective session options
        2. Initialize a new :class:`CDPConnection <streamlink.webbrowser.cdp.connection.CDPConnection>`
           and connect to the browser's remote debugging interface
        3. Create a new :class:`CDPClient` instance
        4. Execute the async runner callback with the :class:`CDPClient` instance as only argument

        If the ``webbrowser`` session option is set to ``False``, then a :exc:`CDPError` will be raised.

        Example:

        .. code-block:: python

            async def fake_response(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
                if request.response_status_code is not None and 300 <= request.response_status_code < 400:
                    await client_session.continue_request(request)
                else:
                    async with client_session.alter_request(request) as cmproxy:
                        cmproxy.body = "<!doctype html><html><body>foo</body></html>"

            async def my_app_logic(client: CDPClient):
                async with client.session() as client_session:
                    client_session.add_request_handler(fake_response, "*")
                    async with client_session.navigate("https://google.com") as frame_id:
                        await client_session.loaded(frame_id)
                        return await client_session.evaluate("document.body.innerText")

            assert CDPClient.launch(session, my_app_logic) == "foo"

        :param session:     The Streamlink session object
        :param runner:      An async client callback function which receives the :class:`CDPClient` instance as only parameter.
        :param executable:  Optional path to the Chromium-based web browser executable.
                            If unset, falls back to the ``webbrowser-executable`` session option.
                            Otherwise, it'll be looked up according to the rules of the :class:`ChromiumBrowser` implementation.
        :param timeout:     Optional global timeout value, including web browser launch time.
                            If unset, falls back to the ``webbrowser-timeout`` session option.
        :param cdp_host:    Optional remote debugging host.
                            If unset, falls back to the ``webbrowser-cdp-host`` session option.
                            Otherwise, ``127.0.0.1`` will be used.
        :param cdp_port:    Optional remote debugging port.
                            If unset, falls back to the ``webbrowser-cdp-port`` session option.
                            Otherwise, a random free port will be chosen.
        :param cdp_timeout: Optional CDP command timeout value.
                            If unset, falls back to the ``webbrowser-cdp-timeout`` session option.
        :param headless:    Optional boolean flag whether to launch the web browser in headless mode or not.
                            If unset, falls back to the ``webbrowser-headless`` session option.
        """
        if not session.get_option("webbrowser"):
            raise CDPError("The webbrowser API has been disabled by the user")

        async def run_wrapper() -> Any:
            async with cls.run(
                session=session,
                executable=session.get_option("webbrowser-executable") if executable is None else executable,
                timeout=session.get_option("webbrowser-timeout") if timeout is None else timeout,
                cdp_host=session.get_option("webbrowser-cdp-host") if cdp_host is None else cdp_host,
                cdp_port=session.get_option("webbrowser-cdp-port") if cdp_port is None else cdp_port,
                cdp_timeout=session.get_option("webbrowser-cdp-timeout") if cdp_timeout is None else cdp_timeout,
                headless=session.get_option("webbrowser-headless") if headless is None else headless,
            ) as cdp_client:
                return await runner(cdp_client)

        return trio.run(run_wrapper, strict_exception_groups=True)

    @classmethod
    @asynccontextmanager
    async def run(
        cls,
        session: Streamlink,
        executable: str | None = None,
        timeout: float | None = None,
        cdp_host: str | None = None,
        cdp_port: int | None = None,
        cdp_timeout: float | None = None,
        headless: bool = False,
    ) -> AsyncGenerator[Self, None]:
        webbrowser = ChromiumWebbrowser(executable=executable, host=cdp_host, port=cdp_port)
        nursery: trio.Nursery
        async with webbrowser.launch(headless=headless, timeout=timeout) as nursery:
            websocket_url = webbrowser.get_websocket_url(session)
            cdp_connection: CDPConnection
            async with CDPConnection.create(websocket_url, timeout=cdp_timeout) as cdp_connection:
                yield cls(cdp_connection, nursery, headless)

    @asynccontextmanager
    async def session(
        self,
        fail_unhandled_requests: bool = False,
        max_buffer_size: int | None = None,
    ) -> AsyncGenerator[CDPClientSession, None]:
        """
        Create a new CDP session on an empty target (browser tab).

        :param fail_unhandled_requests: Whether network requests which are not matched by any request handlers should fail.
        :param max_buffer_size: Optional size of the send/receive memory channel for paused HTTP requests/responses.
        """
        cdp_session = await self.cdp_connection.new_target()
        yield CDPClientSession(self, cdp_session, fail_unhandled_requests, max_buffer_size)


class CDPClientSession:
    """
    High-level API for navigating websites, intercepting network requests/responses,
    and for evaluating async JavaScript expressions.

    Don't instantiate this class yourself, use the :meth:`CDPClient.session()` async contextmanager.
    """

    def xǁCDPClientSessionǁ__init____mutmut_orig(
        self,
        cdp_client: CDPClient,
        cdp_session: CDPSession,
        fail_unhandled_requests: bool = False,
        max_buffer_size: int | None = None,
    ):
        self.cdp_client = cdp_client
        self.cdp_session = cdp_session
        self._fail_unhandled = fail_unhandled_requests
        self._request_handlers: list[RequestPausedHandler] = []
        self._requests_handled: set[str] = set()
        self._max_buffer_size = max_buffer_size

    def xǁCDPClientSessionǁ__init____mutmut_1(
        self,
        cdp_client: CDPClient,
        cdp_session: CDPSession,
        fail_unhandled_requests: bool = True,
        max_buffer_size: int | None = None,
    ):
        self.cdp_client = cdp_client
        self.cdp_session = cdp_session
        self._fail_unhandled = fail_unhandled_requests
        self._request_handlers: list[RequestPausedHandler] = []
        self._requests_handled: set[str] = set()
        self._max_buffer_size = max_buffer_size

    def xǁCDPClientSessionǁ__init____mutmut_2(
        self,
        cdp_client: CDPClient,
        cdp_session: CDPSession,
        fail_unhandled_requests: bool = False,
        max_buffer_size: int | None = None,
    ):
        self.cdp_client = None
        self.cdp_session = cdp_session
        self._fail_unhandled = fail_unhandled_requests
        self._request_handlers: list[RequestPausedHandler] = []
        self._requests_handled: set[str] = set()
        self._max_buffer_size = max_buffer_size

    def xǁCDPClientSessionǁ__init____mutmut_3(
        self,
        cdp_client: CDPClient,
        cdp_session: CDPSession,
        fail_unhandled_requests: bool = False,
        max_buffer_size: int | None = None,
    ):
        self.cdp_client = cdp_client
        self.cdp_session = None
        self._fail_unhandled = fail_unhandled_requests
        self._request_handlers: list[RequestPausedHandler] = []
        self._requests_handled: set[str] = set()
        self._max_buffer_size = max_buffer_size

    def xǁCDPClientSessionǁ__init____mutmut_4(
        self,
        cdp_client: CDPClient,
        cdp_session: CDPSession,
        fail_unhandled_requests: bool = False,
        max_buffer_size: int | None = None,
    ):
        self.cdp_client = cdp_client
        self.cdp_session = cdp_session
        self._fail_unhandled = None
        self._request_handlers: list[RequestPausedHandler] = []
        self._requests_handled: set[str] = set()
        self._max_buffer_size = max_buffer_size

    def xǁCDPClientSessionǁ__init____mutmut_5(
        self,
        cdp_client: CDPClient,
        cdp_session: CDPSession,
        fail_unhandled_requests: bool = False,
        max_buffer_size: int | None = None,
    ):
        self.cdp_client = cdp_client
        self.cdp_session = cdp_session
        self._fail_unhandled = fail_unhandled_requests
        self._request_handlers: list[RequestPausedHandler] = None
        self._requests_handled: set[str] = set()
        self._max_buffer_size = max_buffer_size

    def xǁCDPClientSessionǁ__init____mutmut_6(
        self,
        cdp_client: CDPClient,
        cdp_session: CDPSession,
        fail_unhandled_requests: bool = False,
        max_buffer_size: int | None = None,
    ):
        self.cdp_client = cdp_client
        self.cdp_session = cdp_session
        self._fail_unhandled = fail_unhandled_requests
        self._request_handlers: list[RequestPausedHandler] = []
        self._requests_handled: set[str] = None
        self._max_buffer_size = max_buffer_size

    def xǁCDPClientSessionǁ__init____mutmut_7(
        self,
        cdp_client: CDPClient,
        cdp_session: CDPSession,
        fail_unhandled_requests: bool = False,
        max_buffer_size: int | None = None,
    ):
        self.cdp_client = cdp_client
        self.cdp_session = cdp_session
        self._fail_unhandled = fail_unhandled_requests
        self._request_handlers: list[RequestPausedHandler] = []
        self._requests_handled: set[str] = set()
        self._max_buffer_size = None
    
    xǁCDPClientSessionǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientSessionǁ__init____mutmut_1': xǁCDPClientSessionǁ__init____mutmut_1, 
        'xǁCDPClientSessionǁ__init____mutmut_2': xǁCDPClientSessionǁ__init____mutmut_2, 
        'xǁCDPClientSessionǁ__init____mutmut_3': xǁCDPClientSessionǁ__init____mutmut_3, 
        'xǁCDPClientSessionǁ__init____mutmut_4': xǁCDPClientSessionǁ__init____mutmut_4, 
        'xǁCDPClientSessionǁ__init____mutmut_5': xǁCDPClientSessionǁ__init____mutmut_5, 
        'xǁCDPClientSessionǁ__init____mutmut_6': xǁCDPClientSessionǁ__init____mutmut_6, 
        'xǁCDPClientSessionǁ__init____mutmut_7': xǁCDPClientSessionǁ__init____mutmut_7
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientSessionǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCDPClientSessionǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCDPClientSessionǁ__init____mutmut_orig)
    xǁCDPClientSessionǁ__init____mutmut_orig.__name__ = 'xǁCDPClientSessionǁ__init__'

    def xǁCDPClientSessionǁadd_request_handler__mutmut_orig(
        self,
        async_handler: TRequestHandlerCallable,
        url_pattern: str = "*",
        on_request: bool = False,
    ):
        """
        :param async_handler: An async request handler which must call :meth:`continue_request()`, :meth:`fail_request()`,
                              :meth:`fulfill_request()` or :meth:`alter_request()`, or the next matching request handler
                              will be run. If no matching request handler was found or if no matching one called one of
                              the just mentioned methods, then the request will be continued if the session was initialized
                              with ``fail_unhandled_requests=False``, otherwise it will be blocked.
        :param url_pattern:   An optional URL wildcard string which defaults to ``"*"``. Only matching URLs will cause
                              ``Fetch.requestPraused`` events to be emitted over the CDP connection.
                              The async request handler will be called on each matching URL unless another request handler
                              has already handled the request (see description above).
        :param on_request:    Whether to intercept the network request or the network response.
        """
        self._request_handlers.append(
            RequestPausedHandler(async_handler=async_handler, url_pattern=url_pattern, on_request=on_request),
        )

    def xǁCDPClientSessionǁadd_request_handler__mutmut_1(
        self,
        async_handler: TRequestHandlerCallable,
        url_pattern: str = "XX*XX",
        on_request: bool = False,
    ):
        """
        :param async_handler: An async request handler which must call :meth:`continue_request()`, :meth:`fail_request()`,
                              :meth:`fulfill_request()` or :meth:`alter_request()`, or the next matching request handler
                              will be run. If no matching request handler was found or if no matching one called one of
                              the just mentioned methods, then the request will be continued if the session was initialized
                              with ``fail_unhandled_requests=False``, otherwise it will be blocked.
        :param url_pattern:   An optional URL wildcard string which defaults to ``"*"``. Only matching URLs will cause
                              ``Fetch.requestPraused`` events to be emitted over the CDP connection.
                              The async request handler will be called on each matching URL unless another request handler
                              has already handled the request (see description above).
        :param on_request:    Whether to intercept the network request or the network response.
        """
        self._request_handlers.append(
            RequestPausedHandler(async_handler=async_handler, url_pattern=url_pattern, on_request=on_request),
        )

    def xǁCDPClientSessionǁadd_request_handler__mutmut_2(
        self,
        async_handler: TRequestHandlerCallable,
        url_pattern: str = "*",
        on_request: bool = True,
    ):
        """
        :param async_handler: An async request handler which must call :meth:`continue_request()`, :meth:`fail_request()`,
                              :meth:`fulfill_request()` or :meth:`alter_request()`, or the next matching request handler
                              will be run. If no matching request handler was found or if no matching one called one of
                              the just mentioned methods, then the request will be continued if the session was initialized
                              with ``fail_unhandled_requests=False``, otherwise it will be blocked.
        :param url_pattern:   An optional URL wildcard string which defaults to ``"*"``. Only matching URLs will cause
                              ``Fetch.requestPraused`` events to be emitted over the CDP connection.
                              The async request handler will be called on each matching URL unless another request handler
                              has already handled the request (see description above).
        :param on_request:    Whether to intercept the network request or the network response.
        """
        self._request_handlers.append(
            RequestPausedHandler(async_handler=async_handler, url_pattern=url_pattern, on_request=on_request),
        )

    def xǁCDPClientSessionǁadd_request_handler__mutmut_3(
        self,
        async_handler: TRequestHandlerCallable,
        url_pattern: str = "*",
        on_request: bool = False,
    ):
        """
        :param async_handler: An async request handler which must call :meth:`continue_request()`, :meth:`fail_request()`,
                              :meth:`fulfill_request()` or :meth:`alter_request()`, or the next matching request handler
                              will be run. If no matching request handler was found or if no matching one called one of
                              the just mentioned methods, then the request will be continued if the session was initialized
                              with ``fail_unhandled_requests=False``, otherwise it will be blocked.
        :param url_pattern:   An optional URL wildcard string which defaults to ``"*"``. Only matching URLs will cause
                              ``Fetch.requestPraused`` events to be emitted over the CDP connection.
                              The async request handler will be called on each matching URL unless another request handler
                              has already handled the request (see description above).
        :param on_request:    Whether to intercept the network request or the network response.
        """
        self._request_handlers.append(
            None,
        )

    def xǁCDPClientSessionǁadd_request_handler__mutmut_4(
        self,
        async_handler: TRequestHandlerCallable,
        url_pattern: str = "*",
        on_request: bool = False,
    ):
        """
        :param async_handler: An async request handler which must call :meth:`continue_request()`, :meth:`fail_request()`,
                              :meth:`fulfill_request()` or :meth:`alter_request()`, or the next matching request handler
                              will be run. If no matching request handler was found or if no matching one called one of
                              the just mentioned methods, then the request will be continued if the session was initialized
                              with ``fail_unhandled_requests=False``, otherwise it will be blocked.
        :param url_pattern:   An optional URL wildcard string which defaults to ``"*"``. Only matching URLs will cause
                              ``Fetch.requestPraused`` events to be emitted over the CDP connection.
                              The async request handler will be called on each matching URL unless another request handler
                              has already handled the request (see description above).
        :param on_request:    Whether to intercept the network request or the network response.
        """
        self._request_handlers.append(
            RequestPausedHandler(async_handler=None, url_pattern=url_pattern, on_request=on_request),
        )

    def xǁCDPClientSessionǁadd_request_handler__mutmut_5(
        self,
        async_handler: TRequestHandlerCallable,
        url_pattern: str = "*",
        on_request: bool = False,
    ):
        """
        :param async_handler: An async request handler which must call :meth:`continue_request()`, :meth:`fail_request()`,
                              :meth:`fulfill_request()` or :meth:`alter_request()`, or the next matching request handler
                              will be run. If no matching request handler was found or if no matching one called one of
                              the just mentioned methods, then the request will be continued if the session was initialized
                              with ``fail_unhandled_requests=False``, otherwise it will be blocked.
        :param url_pattern:   An optional URL wildcard string which defaults to ``"*"``. Only matching URLs will cause
                              ``Fetch.requestPraused`` events to be emitted over the CDP connection.
                              The async request handler will be called on each matching URL unless another request handler
                              has already handled the request (see description above).
        :param on_request:    Whether to intercept the network request or the network response.
        """
        self._request_handlers.append(
            RequestPausedHandler(async_handler=async_handler, url_pattern=None, on_request=on_request),
        )

    def xǁCDPClientSessionǁadd_request_handler__mutmut_6(
        self,
        async_handler: TRequestHandlerCallable,
        url_pattern: str = "*",
        on_request: bool = False,
    ):
        """
        :param async_handler: An async request handler which must call :meth:`continue_request()`, :meth:`fail_request()`,
                              :meth:`fulfill_request()` or :meth:`alter_request()`, or the next matching request handler
                              will be run. If no matching request handler was found or if no matching one called one of
                              the just mentioned methods, then the request will be continued if the session was initialized
                              with ``fail_unhandled_requests=False``, otherwise it will be blocked.
        :param url_pattern:   An optional URL wildcard string which defaults to ``"*"``. Only matching URLs will cause
                              ``Fetch.requestPraused`` events to be emitted over the CDP connection.
                              The async request handler will be called on each matching URL unless another request handler
                              has already handled the request (see description above).
        :param on_request:    Whether to intercept the network request or the network response.
        """
        self._request_handlers.append(
            RequestPausedHandler(async_handler=async_handler, url_pattern=url_pattern, on_request=None),
        )

    def xǁCDPClientSessionǁadd_request_handler__mutmut_7(
        self,
        async_handler: TRequestHandlerCallable,
        url_pattern: str = "*",
        on_request: bool = False,
    ):
        """
        :param async_handler: An async request handler which must call :meth:`continue_request()`, :meth:`fail_request()`,
                              :meth:`fulfill_request()` or :meth:`alter_request()`, or the next matching request handler
                              will be run. If no matching request handler was found or if no matching one called one of
                              the just mentioned methods, then the request will be continued if the session was initialized
                              with ``fail_unhandled_requests=False``, otherwise it will be blocked.
        :param url_pattern:   An optional URL wildcard string which defaults to ``"*"``. Only matching URLs will cause
                              ``Fetch.requestPraused`` events to be emitted over the CDP connection.
                              The async request handler will be called on each matching URL unless another request handler
                              has already handled the request (see description above).
        :param on_request:    Whether to intercept the network request or the network response.
        """
        self._request_handlers.append(
            RequestPausedHandler(url_pattern=url_pattern, on_request=on_request),
        )

    def xǁCDPClientSessionǁadd_request_handler__mutmut_8(
        self,
        async_handler: TRequestHandlerCallable,
        url_pattern: str = "*",
        on_request: bool = False,
    ):
        """
        :param async_handler: An async request handler which must call :meth:`continue_request()`, :meth:`fail_request()`,
                              :meth:`fulfill_request()` or :meth:`alter_request()`, or the next matching request handler
                              will be run. If no matching request handler was found or if no matching one called one of
                              the just mentioned methods, then the request will be continued if the session was initialized
                              with ``fail_unhandled_requests=False``, otherwise it will be blocked.
        :param url_pattern:   An optional URL wildcard string which defaults to ``"*"``. Only matching URLs will cause
                              ``Fetch.requestPraused`` events to be emitted over the CDP connection.
                              The async request handler will be called on each matching URL unless another request handler
                              has already handled the request (see description above).
        :param on_request:    Whether to intercept the network request or the network response.
        """
        self._request_handlers.append(
            RequestPausedHandler(async_handler=async_handler, on_request=on_request),
        )

    def xǁCDPClientSessionǁadd_request_handler__mutmut_9(
        self,
        async_handler: TRequestHandlerCallable,
        url_pattern: str = "*",
        on_request: bool = False,
    ):
        """
        :param async_handler: An async request handler which must call :meth:`continue_request()`, :meth:`fail_request()`,
                              :meth:`fulfill_request()` or :meth:`alter_request()`, or the next matching request handler
                              will be run. If no matching request handler was found or if no matching one called one of
                              the just mentioned methods, then the request will be continued if the session was initialized
                              with ``fail_unhandled_requests=False``, otherwise it will be blocked.
        :param url_pattern:   An optional URL wildcard string which defaults to ``"*"``. Only matching URLs will cause
                              ``Fetch.requestPraused`` events to be emitted over the CDP connection.
                              The async request handler will be called on each matching URL unless another request handler
                              has already handled the request (see description above).
        :param on_request:    Whether to intercept the network request or the network response.
        """
        self._request_handlers.append(
            RequestPausedHandler(async_handler=async_handler, url_pattern=url_pattern, ),
        )
    
    xǁCDPClientSessionǁadd_request_handler__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientSessionǁadd_request_handler__mutmut_1': xǁCDPClientSessionǁadd_request_handler__mutmut_1, 
        'xǁCDPClientSessionǁadd_request_handler__mutmut_2': xǁCDPClientSessionǁadd_request_handler__mutmut_2, 
        'xǁCDPClientSessionǁadd_request_handler__mutmut_3': xǁCDPClientSessionǁadd_request_handler__mutmut_3, 
        'xǁCDPClientSessionǁadd_request_handler__mutmut_4': xǁCDPClientSessionǁadd_request_handler__mutmut_4, 
        'xǁCDPClientSessionǁadd_request_handler__mutmut_5': xǁCDPClientSessionǁadd_request_handler__mutmut_5, 
        'xǁCDPClientSessionǁadd_request_handler__mutmut_6': xǁCDPClientSessionǁadd_request_handler__mutmut_6, 
        'xǁCDPClientSessionǁadd_request_handler__mutmut_7': xǁCDPClientSessionǁadd_request_handler__mutmut_7, 
        'xǁCDPClientSessionǁadd_request_handler__mutmut_8': xǁCDPClientSessionǁadd_request_handler__mutmut_8, 
        'xǁCDPClientSessionǁadd_request_handler__mutmut_9': xǁCDPClientSessionǁadd_request_handler__mutmut_9
    }
    
    def add_request_handler(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientSessionǁadd_request_handler__mutmut_orig"), object.__getattribute__(self, "xǁCDPClientSessionǁadd_request_handler__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add_request_handler.__signature__ = _mutmut_signature(xǁCDPClientSessionǁadd_request_handler__mutmut_orig)
    xǁCDPClientSessionǁadd_request_handler__mutmut_orig.__name__ = 'xǁCDPClientSessionǁadd_request_handler'

    @asynccontextmanager
    async def navigate(self, url: str, referrer: str | None = None) -> AsyncGenerator[page.FrameId, None]:
        """
        Async context manager for opening the URL with an optional referrer and starting the optional interception
        of network requests and responses.
        If the target gets detached from the session, e.g. by closing the tab, then the whole CDP connection gets terminated,
        including all other concurrent sessions.
        Doesn't wait for the request to finish loading. See :meth:`loaded()`.

        :param url: The URL.
        :param referrer: An optional referrer.
        :return: Yields the ``FrameID`` that can be passed to the :meth:`loaded()` call.
        """

        request_patterns = [
            fetch.RequestPattern(
                url_pattern=url_pattern,
                request_stage=fetch.RequestStage.REQUEST if on_request else fetch.RequestStage.RESPONSE,
            )
            for url_pattern, on_request in sorted(
                {(request_handler.url_pattern, request_handler.on_request) for request_handler in self._request_handlers},
            )
        ]

        async with trio.open_nursery() as nursery:
            nursery.start_soon(self._on_target_detached_from_target)

            if self.cdp_client.headless:
                await self._update_user_agent()

            if request_patterns:
                nursery.start_soon(self._on_fetch_request_paused)
                await self.cdp_session.send(fetch.enable(request_patterns, True))

            await self.cdp_session.send(page.enable())

            try:
                frame_id, _loader_id, error = await self.cdp_session.send(page.navigate(url=url, referrer=referrer))
                if error:
                    raise CDPError(f"Navigation error: {error}")

                yield frame_id

            finally:
                await self.cdp_session.send(page.disable())
                if request_patterns:
                    await self.cdp_session.send(fetch.disable())
                nursery.cancel_scope.cancel()

    async def xǁCDPClientSessionǁloaded__mutmut_orig(self, frame_id: page.FrameId):
        """
        Wait for the navigated page to finish loading.
        """
        async for frame_stopped_loading in self.cdp_session.listen(page.FrameStoppedLoading):  # pragma: no branch
            if frame_stopped_loading.frame_id == frame_id:
                return

    async def xǁCDPClientSessionǁloaded__mutmut_1(self, frame_id: page.FrameId):
        """
        Wait for the navigated page to finish loading.
        """
        async for frame_stopped_loading in self.cdp_session.listen(None):  # pragma: no branch
            if frame_stopped_loading.frame_id == frame_id:
                return

    async def xǁCDPClientSessionǁloaded__mutmut_2(self, frame_id: page.FrameId):
        """
        Wait for the navigated page to finish loading.
        """
        async for frame_stopped_loading in self.cdp_session.listen(page.FrameStoppedLoading):  # pragma: no branch
            if frame_stopped_loading.frame_id != frame_id:
                return
    
    xǁCDPClientSessionǁloaded__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientSessionǁloaded__mutmut_1': xǁCDPClientSessionǁloaded__mutmut_1, 
        'xǁCDPClientSessionǁloaded__mutmut_2': xǁCDPClientSessionǁloaded__mutmut_2
    }
    
    def loaded(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientSessionǁloaded__mutmut_orig"), object.__getattribute__(self, "xǁCDPClientSessionǁloaded__mutmut_mutants"), args, kwargs, self)
        return result 
    
    loaded.__signature__ = _mutmut_signature(xǁCDPClientSessionǁloaded__mutmut_orig)
    xǁCDPClientSessionǁloaded__mutmut_orig.__name__ = 'xǁCDPClientSessionǁloaded'

    async def xǁCDPClientSessionǁevaluate__mutmut_orig(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_1(self, expression: str, await_promise: bool = False, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_2(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = None
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_3(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=None,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_4(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=None,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_5(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_6(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_7(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = None
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_8(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(None, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_9(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=None)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_10(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_11(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, )
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_12(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(None)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_13(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception or error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_14(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description and error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_15(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ != "object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_16(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "XXobjectXX" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_17(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "OBJECT" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_18(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "Object" and remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_19(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" or remote_obj.subtype == "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_20(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype != "error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_21(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "XXerrorXX":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_22(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "ERROR":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_23(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "Error":
            raise CDPError(remote_obj.description)
        return remote_obj.value

    async def xǁCDPClientSessionǁevaluate__mutmut_24(self, expression: str, await_promise: bool = True, timeout: float | None = None) -> Any:
        """
        Evaluate an optionally async JavaScript expression and return its result.

        :param expression: The JavaScript expression.
        :param await_promise: Whether to await a returned :js:class:`Promise` object.
        :param timeout: Optional timeout override value. Uses the session's single CDP command timeout value by default,
                        which may be too short depending on the script execution time.
        :raise CDPError: On evaluation error or if the result is a subtype of :js:class:`window.Error`.
        :return: Only JS-primitive result values are supported, e.g. strings or numbers.
                 Other kinds of return values must be serialized, e.g. via :js:meth:`JSON.stringify()`.
        """
        evaluate = runtime.evaluate(
            expression=expression,
            await_promise=await_promise,
        )
        remote_obj, error = await self.cdp_session.send(evaluate, timeout=timeout)
        if error:
            raise CDPError(error.exception and error.exception.description or error.text)
        if remote_obj.type_ == "object" and remote_obj.subtype == "error":
            raise CDPError(None)
        return remote_obj.value
    
    xǁCDPClientSessionǁevaluate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientSessionǁevaluate__mutmut_1': xǁCDPClientSessionǁevaluate__mutmut_1, 
        'xǁCDPClientSessionǁevaluate__mutmut_2': xǁCDPClientSessionǁevaluate__mutmut_2, 
        'xǁCDPClientSessionǁevaluate__mutmut_3': xǁCDPClientSessionǁevaluate__mutmut_3, 
        'xǁCDPClientSessionǁevaluate__mutmut_4': xǁCDPClientSessionǁevaluate__mutmut_4, 
        'xǁCDPClientSessionǁevaluate__mutmut_5': xǁCDPClientSessionǁevaluate__mutmut_5, 
        'xǁCDPClientSessionǁevaluate__mutmut_6': xǁCDPClientSessionǁevaluate__mutmut_6, 
        'xǁCDPClientSessionǁevaluate__mutmut_7': xǁCDPClientSessionǁevaluate__mutmut_7, 
        'xǁCDPClientSessionǁevaluate__mutmut_8': xǁCDPClientSessionǁevaluate__mutmut_8, 
        'xǁCDPClientSessionǁevaluate__mutmut_9': xǁCDPClientSessionǁevaluate__mutmut_9, 
        'xǁCDPClientSessionǁevaluate__mutmut_10': xǁCDPClientSessionǁevaluate__mutmut_10, 
        'xǁCDPClientSessionǁevaluate__mutmut_11': xǁCDPClientSessionǁevaluate__mutmut_11, 
        'xǁCDPClientSessionǁevaluate__mutmut_12': xǁCDPClientSessionǁevaluate__mutmut_12, 
        'xǁCDPClientSessionǁevaluate__mutmut_13': xǁCDPClientSessionǁevaluate__mutmut_13, 
        'xǁCDPClientSessionǁevaluate__mutmut_14': xǁCDPClientSessionǁevaluate__mutmut_14, 
        'xǁCDPClientSessionǁevaluate__mutmut_15': xǁCDPClientSessionǁevaluate__mutmut_15, 
        'xǁCDPClientSessionǁevaluate__mutmut_16': xǁCDPClientSessionǁevaluate__mutmut_16, 
        'xǁCDPClientSessionǁevaluate__mutmut_17': xǁCDPClientSessionǁevaluate__mutmut_17, 
        'xǁCDPClientSessionǁevaluate__mutmut_18': xǁCDPClientSessionǁevaluate__mutmut_18, 
        'xǁCDPClientSessionǁevaluate__mutmut_19': xǁCDPClientSessionǁevaluate__mutmut_19, 
        'xǁCDPClientSessionǁevaluate__mutmut_20': xǁCDPClientSessionǁevaluate__mutmut_20, 
        'xǁCDPClientSessionǁevaluate__mutmut_21': xǁCDPClientSessionǁevaluate__mutmut_21, 
        'xǁCDPClientSessionǁevaluate__mutmut_22': xǁCDPClientSessionǁevaluate__mutmut_22, 
        'xǁCDPClientSessionǁevaluate__mutmut_23': xǁCDPClientSessionǁevaluate__mutmut_23, 
        'xǁCDPClientSessionǁevaluate__mutmut_24': xǁCDPClientSessionǁevaluate__mutmut_24
    }
    
    def evaluate(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientSessionǁevaluate__mutmut_orig"), object.__getattribute__(self, "xǁCDPClientSessionǁevaluate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    evaluate.__signature__ = _mutmut_signature(xǁCDPClientSessionǁevaluate__mutmut_orig)
    xǁCDPClientSessionǁevaluate__mutmut_orig.__name__ = 'xǁCDPClientSessionǁevaluate'

    async def xǁCDPClientSessionǁcontinue_request__mutmut_orig(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                method=method,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_1(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            None,
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_2(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=None,
                url=url,
                method=method,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_3(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=None,
                method=method,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_4(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                method=None,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_5(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                method=method,
                post_data=None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_6(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                method=method,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                headers=None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_7(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                url=url,
                method=method,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_8(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                method=method,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_9(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_10(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                method=method,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_11(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                method=method,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_12(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                method=method,
                post_data=base64.b64encode(None).decode() if post_data is not None else None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_13(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                method=method,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is None else None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_14(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                method=method,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                headers=self._headers_entries_from_mapping(None),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁcontinue_request__mutmut_15(
        self,
        request: fetch.RequestPaused,
        url: str | None = None,
        method: str | None = None,
        post_data: str | None = None,
        headers: Mapping[str, str] | None = None,
    ):
        """
        Continue a request and optionally override the request method, URL, POST data or request headers.
        """
        await self.cdp_session.send(
            fetch.continue_request(
                request_id=request.request_id,
                url=url,
                method=method,
                post_data=base64.b64encode(post_data.encode()).decode() if post_data is not None else None,
                headers=self._headers_entries_from_mapping(headers),
            ),
        )
        self._requests_handled.add(None)
    
    xǁCDPClientSessionǁcontinue_request__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientSessionǁcontinue_request__mutmut_1': xǁCDPClientSessionǁcontinue_request__mutmut_1, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_2': xǁCDPClientSessionǁcontinue_request__mutmut_2, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_3': xǁCDPClientSessionǁcontinue_request__mutmut_3, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_4': xǁCDPClientSessionǁcontinue_request__mutmut_4, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_5': xǁCDPClientSessionǁcontinue_request__mutmut_5, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_6': xǁCDPClientSessionǁcontinue_request__mutmut_6, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_7': xǁCDPClientSessionǁcontinue_request__mutmut_7, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_8': xǁCDPClientSessionǁcontinue_request__mutmut_8, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_9': xǁCDPClientSessionǁcontinue_request__mutmut_9, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_10': xǁCDPClientSessionǁcontinue_request__mutmut_10, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_11': xǁCDPClientSessionǁcontinue_request__mutmut_11, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_12': xǁCDPClientSessionǁcontinue_request__mutmut_12, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_13': xǁCDPClientSessionǁcontinue_request__mutmut_13, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_14': xǁCDPClientSessionǁcontinue_request__mutmut_14, 
        'xǁCDPClientSessionǁcontinue_request__mutmut_15': xǁCDPClientSessionǁcontinue_request__mutmut_15
    }
    
    def continue_request(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientSessionǁcontinue_request__mutmut_orig"), object.__getattribute__(self, "xǁCDPClientSessionǁcontinue_request__mutmut_mutants"), args, kwargs, self)
        return result 
    
    continue_request.__signature__ = _mutmut_signature(xǁCDPClientSessionǁcontinue_request__mutmut_orig)
    xǁCDPClientSessionǁcontinue_request__mutmut_orig.__name__ = 'xǁCDPClientSessionǁcontinue_request'

    async def xǁCDPClientSessionǁfail_request__mutmut_orig(
        self,
        request: fetch.RequestPaused,
        error_reason: str | None = None,
    ):
        """
        Let a request fail, with an optional error reason which defaults to ``BlockedByClient``.
        """
        await self.cdp_session.send(
            fetch.fail_request(
                request_id=request.request_id,
                error_reason=network.ErrorReason(error_reason or network.ErrorReason.BLOCKED_BY_CLIENT),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfail_request__mutmut_1(
        self,
        request: fetch.RequestPaused,
        error_reason: str | None = None,
    ):
        """
        Let a request fail, with an optional error reason which defaults to ``BlockedByClient``.
        """
        await self.cdp_session.send(
            None,
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfail_request__mutmut_2(
        self,
        request: fetch.RequestPaused,
        error_reason: str | None = None,
    ):
        """
        Let a request fail, with an optional error reason which defaults to ``BlockedByClient``.
        """
        await self.cdp_session.send(
            fetch.fail_request(
                request_id=None,
                error_reason=network.ErrorReason(error_reason or network.ErrorReason.BLOCKED_BY_CLIENT),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfail_request__mutmut_3(
        self,
        request: fetch.RequestPaused,
        error_reason: str | None = None,
    ):
        """
        Let a request fail, with an optional error reason which defaults to ``BlockedByClient``.
        """
        await self.cdp_session.send(
            fetch.fail_request(
                request_id=request.request_id,
                error_reason=None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfail_request__mutmut_4(
        self,
        request: fetch.RequestPaused,
        error_reason: str | None = None,
    ):
        """
        Let a request fail, with an optional error reason which defaults to ``BlockedByClient``.
        """
        await self.cdp_session.send(
            fetch.fail_request(
                error_reason=network.ErrorReason(error_reason or network.ErrorReason.BLOCKED_BY_CLIENT),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfail_request__mutmut_5(
        self,
        request: fetch.RequestPaused,
        error_reason: str | None = None,
    ):
        """
        Let a request fail, with an optional error reason which defaults to ``BlockedByClient``.
        """
        await self.cdp_session.send(
            fetch.fail_request(
                request_id=request.request_id,
                ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfail_request__mutmut_6(
        self,
        request: fetch.RequestPaused,
        error_reason: str | None = None,
    ):
        """
        Let a request fail, with an optional error reason which defaults to ``BlockedByClient``.
        """
        await self.cdp_session.send(
            fetch.fail_request(
                request_id=request.request_id,
                error_reason=network.ErrorReason(None),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfail_request__mutmut_7(
        self,
        request: fetch.RequestPaused,
        error_reason: str | None = None,
    ):
        """
        Let a request fail, with an optional error reason which defaults to ``BlockedByClient``.
        """
        await self.cdp_session.send(
            fetch.fail_request(
                request_id=request.request_id,
                error_reason=network.ErrorReason(error_reason and network.ErrorReason.BLOCKED_BY_CLIENT),
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfail_request__mutmut_8(
        self,
        request: fetch.RequestPaused,
        error_reason: str | None = None,
    ):
        """
        Let a request fail, with an optional error reason which defaults to ``BlockedByClient``.
        """
        await self.cdp_session.send(
            fetch.fail_request(
                request_id=request.request_id,
                error_reason=network.ErrorReason(error_reason or network.ErrorReason.BLOCKED_BY_CLIENT),
            ),
        )
        self._requests_handled.add(None)
    
    xǁCDPClientSessionǁfail_request__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientSessionǁfail_request__mutmut_1': xǁCDPClientSessionǁfail_request__mutmut_1, 
        'xǁCDPClientSessionǁfail_request__mutmut_2': xǁCDPClientSessionǁfail_request__mutmut_2, 
        'xǁCDPClientSessionǁfail_request__mutmut_3': xǁCDPClientSessionǁfail_request__mutmut_3, 
        'xǁCDPClientSessionǁfail_request__mutmut_4': xǁCDPClientSessionǁfail_request__mutmut_4, 
        'xǁCDPClientSessionǁfail_request__mutmut_5': xǁCDPClientSessionǁfail_request__mutmut_5, 
        'xǁCDPClientSessionǁfail_request__mutmut_6': xǁCDPClientSessionǁfail_request__mutmut_6, 
        'xǁCDPClientSessionǁfail_request__mutmut_7': xǁCDPClientSessionǁfail_request__mutmut_7, 
        'xǁCDPClientSessionǁfail_request__mutmut_8': xǁCDPClientSessionǁfail_request__mutmut_8
    }
    
    def fail_request(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientSessionǁfail_request__mutmut_orig"), object.__getattribute__(self, "xǁCDPClientSessionǁfail_request__mutmut_mutants"), args, kwargs, self)
        return result 
    
    fail_request.__signature__ = _mutmut_signature(xǁCDPClientSessionǁfail_request__mutmut_orig)
    xǁCDPClientSessionǁfail_request__mutmut_orig.__name__ = 'xǁCDPClientSessionǁfail_request'

    async def xǁCDPClientSessionǁfulfill_request__mutmut_orig(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=response_code,
                response_headers=self._headers_entries_from_mapping(response_headers),
                body=base64.b64encode(body.encode()).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_1(
        self,
        request: fetch.RequestPaused,
        response_code: int = 201,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=response_code,
                response_headers=self._headers_entries_from_mapping(response_headers),
                body=base64.b64encode(body.encode()).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_2(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            None,
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_3(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=None,
                response_code=response_code,
                response_headers=self._headers_entries_from_mapping(response_headers),
                body=base64.b64encode(body.encode()).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_4(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=None,
                response_headers=self._headers_entries_from_mapping(response_headers),
                body=base64.b64encode(body.encode()).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_5(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=response_code,
                response_headers=None,
                body=base64.b64encode(body.encode()).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_6(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=response_code,
                response_headers=self._headers_entries_from_mapping(response_headers),
                body=None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_7(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                response_code=response_code,
                response_headers=self._headers_entries_from_mapping(response_headers),
                body=base64.b64encode(body.encode()).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_8(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_headers=self._headers_entries_from_mapping(response_headers),
                body=base64.b64encode(body.encode()).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_9(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=response_code,
                body=base64.b64encode(body.encode()).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_10(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=response_code,
                response_headers=self._headers_entries_from_mapping(response_headers),
                ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_11(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=response_code,
                response_headers=self._headers_entries_from_mapping(None),
                body=base64.b64encode(body.encode()).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_12(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=response_code,
                response_headers=self._headers_entries_from_mapping(response_headers),
                body=base64.b64encode(None).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_13(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=response_code,
                response_headers=self._headers_entries_from_mapping(response_headers),
                body=base64.b64encode(body.encode()).decode() if body is None else None,
            ),
        )
        self._requests_handled.add(request.request_id)

    async def xǁCDPClientSessionǁfulfill_request__mutmut_14(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
        body: str | None = None,
    ) -> None:
        """
        Fulfill a response and override its status code, headers and body.
        """
        await self.cdp_session.send(
            fetch.fulfill_request(
                request_id=request.request_id,
                response_code=response_code,
                response_headers=self._headers_entries_from_mapping(response_headers),
                body=base64.b64encode(body.encode()).decode() if body is not None else None,
            ),
        )
        self._requests_handled.add(None)
    
    xǁCDPClientSessionǁfulfill_request__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientSessionǁfulfill_request__mutmut_1': xǁCDPClientSessionǁfulfill_request__mutmut_1, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_2': xǁCDPClientSessionǁfulfill_request__mutmut_2, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_3': xǁCDPClientSessionǁfulfill_request__mutmut_3, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_4': xǁCDPClientSessionǁfulfill_request__mutmut_4, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_5': xǁCDPClientSessionǁfulfill_request__mutmut_5, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_6': xǁCDPClientSessionǁfulfill_request__mutmut_6, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_7': xǁCDPClientSessionǁfulfill_request__mutmut_7, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_8': xǁCDPClientSessionǁfulfill_request__mutmut_8, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_9': xǁCDPClientSessionǁfulfill_request__mutmut_9, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_10': xǁCDPClientSessionǁfulfill_request__mutmut_10, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_11': xǁCDPClientSessionǁfulfill_request__mutmut_11, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_12': xǁCDPClientSessionǁfulfill_request__mutmut_12, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_13': xǁCDPClientSessionǁfulfill_request__mutmut_13, 
        'xǁCDPClientSessionǁfulfill_request__mutmut_14': xǁCDPClientSessionǁfulfill_request__mutmut_14
    }
    
    def fulfill_request(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientSessionǁfulfill_request__mutmut_orig"), object.__getattribute__(self, "xǁCDPClientSessionǁfulfill_request__mutmut_mutants"), args, kwargs, self)
        return result 
    
    fulfill_request.__signature__ = _mutmut_signature(xǁCDPClientSessionǁfulfill_request__mutmut_orig)
    xǁCDPClientSessionǁfulfill_request__mutmut_orig.__name__ = 'xǁCDPClientSessionǁfulfill_request'

    @asynccontextmanager
    async def alter_request(
        self,
        request: fetch.RequestPaused,
        response_code: int = 200,
        response_headers: Mapping[str, str] | None = None,
    ) -> AsyncGenerator[CMRequestProxy, None]:
        """
        Async context manager wrapper around :meth:`fulfill_request()` which retrieves the response body,
        so it can be altered. The status code and headers can be altered in the method call directly,
        or by setting the respective parameters on the context manager's proxy object.
        """
        if request.response_status_code is None:
            body = ""
        else:
            body, b64encoded = await self.cdp_session.send(fetch.get_response_body(request.request_id))
            if b64encoded:  # pragma: no branch
                body = base64.b64decode(body).decode()
        proxy = CMRequestProxy(body=body, response_code=response_code, response_headers=response_headers)
        yield proxy
        await self.fulfill_request(
            request=request,
            response_code=proxy.response_code,
            response_headers=proxy.response_headers,
            body=proxy.body,
        )

    @staticmethod
    def _headers_entries_from_mapping(headers: Mapping[str, str] | None):
        return None if headers is None else [fetch.HeaderEntry(name=name, value=value) for name, value in headers.items()]

    async def xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_orig(self) -> None:
        detached_from_target: target.DetachedFromTarget
        async for detached_from_target in self.cdp_client.cdp_connection.listen(target.DetachedFromTarget):
            if detached_from_target.session_id == self.cdp_session.session_id:
                raise CDPError("Target has been detached")

    async def xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_1(self) -> None:
        detached_from_target: target.DetachedFromTarget
        async for detached_from_target in self.cdp_client.cdp_connection.listen(None):
            if detached_from_target.session_id == self.cdp_session.session_id:
                raise CDPError("Target has been detached")

    async def xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_2(self) -> None:
        detached_from_target: target.DetachedFromTarget
        async for detached_from_target in self.cdp_client.cdp_connection.listen(target.DetachedFromTarget):
            if detached_from_target.session_id != self.cdp_session.session_id:
                raise CDPError("Target has been detached")

    async def xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_3(self) -> None:
        detached_from_target: target.DetachedFromTarget
        async for detached_from_target in self.cdp_client.cdp_connection.listen(target.DetachedFromTarget):
            if detached_from_target.session_id == self.cdp_session.session_id:
                raise CDPError(None)

    async def xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_4(self) -> None:
        detached_from_target: target.DetachedFromTarget
        async for detached_from_target in self.cdp_client.cdp_connection.listen(target.DetachedFromTarget):
            if detached_from_target.session_id == self.cdp_session.session_id:
                raise CDPError("XXTarget has been detachedXX")

    async def xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_5(self) -> None:
        detached_from_target: target.DetachedFromTarget
        async for detached_from_target in self.cdp_client.cdp_connection.listen(target.DetachedFromTarget):
            if detached_from_target.session_id == self.cdp_session.session_id:
                raise CDPError("target has been detached")

    async def xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_6(self) -> None:
        detached_from_target: target.DetachedFromTarget
        async for detached_from_target in self.cdp_client.cdp_connection.listen(target.DetachedFromTarget):
            if detached_from_target.session_id == self.cdp_session.session_id:
                raise CDPError("TARGET HAS BEEN DETACHED")
    
    xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_1': xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_1, 
        'xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_2': xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_2, 
        'xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_3': xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_3, 
        'xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_4': xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_4, 
        'xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_5': xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_5, 
        'xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_6': xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_6
    }
    
    def _on_target_detached_from_target(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_orig"), object.__getattribute__(self, "xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _on_target_detached_from_target.__signature__ = _mutmut_signature(xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_orig)
    xǁCDPClientSessionǁ_on_target_detached_from_target__mutmut_orig.__name__ = 'xǁCDPClientSessionǁ_on_target_detached_from_target'

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_orig(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_1(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(None, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_2(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=None):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_3(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_4(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, ):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_5(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if handler.matches(request):
                    continue
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_6(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(None):
                    continue
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_7(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    break
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_8(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(None, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_9(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, None)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_10(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_11(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, )
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_12(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, request)
                if request.request_id not in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_13(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    return
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_14(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(None)
                else:
                    await self.continue_request(request)

    async def xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_15(self) -> None:
        request: fetch.RequestPaused
        async for request in self.cdp_session.listen(fetch.RequestPaused, max_buffer_size=self._max_buffer_size):
            for handler in self._request_handlers:
                if not handler.matches(request):
                    continue
                await handler.async_handler(self, request)
                if request.request_id in self._requests_handled:
                    break
            else:
                if self._fail_unhandled:
                    await self.fail_request(request)
                else:
                    await self.continue_request(None)
    
    xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_1': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_1, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_2': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_2, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_3': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_3, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_4': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_4, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_5': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_5, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_6': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_6, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_7': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_7, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_8': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_8, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_9': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_9, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_10': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_10, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_11': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_11, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_12': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_12, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_13': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_13, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_14': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_14, 
        'xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_15': xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_15
    }
    
    def _on_fetch_request_paused(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_orig"), object.__getattribute__(self, "xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _on_fetch_request_paused.__signature__ = _mutmut_signature(xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_orig)
    xǁCDPClientSessionǁ_on_fetch_request_paused__mutmut_orig.__name__ = 'xǁCDPClientSessionǁ_on_fetch_request_paused'

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_orig(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_1(self) -> None:
        user_agent: str = None
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_2(self) -> None:
        user_agent: str = await self.evaluate(None, await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_3(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=None)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_4(self) -> None:
        user_agent: str = await self.evaluate(await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_5(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", )
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_6(self) -> None:
        user_agent: str = await self.evaluate("XXnavigator.userAgentXX", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_7(self) -> None:
        user_agent: str = await self.evaluate("navigator.useragent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_8(self) -> None:
        user_agent: str = await self.evaluate("NAVIGATOR.USERAGENT", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_9(self) -> None:
        user_agent: str = await self.evaluate("Navigator.useragent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_10(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=True)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_11(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_12(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError(None)
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_13(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("XXCould not read navigator.userAgent valueXX")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_14(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("could not read navigator.useragent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_15(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("COULD NOT READ NAVIGATOR.USERAGENT VALUE")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_16(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.useragent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_17(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = None
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_18(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(None, "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_19(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", None, user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_20(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", None, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_21(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=None)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_22(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub("", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_23(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_24(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_25(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, )
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_26(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"XXHeadlessXX", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_27(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_28(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"HEADLESS", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_29(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_30(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "XXXX", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=user_agent))

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_31(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(None)

    async def xǁCDPClientSessionǁ_update_user_agent__mutmut_32(self) -> None:
        user_agent: str = await self.evaluate("navigator.userAgent", await_promise=False)
        if not user_agent:  # pragma: no cover
            raise CDPError("Could not read navigator.userAgent value")
        user_agent = re.sub(r"Headless", "", user_agent, flags=re.IGNORECASE)
        await self.cdp_session.send(network.set_user_agent_override(user_agent=None))
    
    xǁCDPClientSessionǁ_update_user_agent__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCDPClientSessionǁ_update_user_agent__mutmut_1': xǁCDPClientSessionǁ_update_user_agent__mutmut_1, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_2': xǁCDPClientSessionǁ_update_user_agent__mutmut_2, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_3': xǁCDPClientSessionǁ_update_user_agent__mutmut_3, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_4': xǁCDPClientSessionǁ_update_user_agent__mutmut_4, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_5': xǁCDPClientSessionǁ_update_user_agent__mutmut_5, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_6': xǁCDPClientSessionǁ_update_user_agent__mutmut_6, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_7': xǁCDPClientSessionǁ_update_user_agent__mutmut_7, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_8': xǁCDPClientSessionǁ_update_user_agent__mutmut_8, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_9': xǁCDPClientSessionǁ_update_user_agent__mutmut_9, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_10': xǁCDPClientSessionǁ_update_user_agent__mutmut_10, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_11': xǁCDPClientSessionǁ_update_user_agent__mutmut_11, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_12': xǁCDPClientSessionǁ_update_user_agent__mutmut_12, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_13': xǁCDPClientSessionǁ_update_user_agent__mutmut_13, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_14': xǁCDPClientSessionǁ_update_user_agent__mutmut_14, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_15': xǁCDPClientSessionǁ_update_user_agent__mutmut_15, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_16': xǁCDPClientSessionǁ_update_user_agent__mutmut_16, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_17': xǁCDPClientSessionǁ_update_user_agent__mutmut_17, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_18': xǁCDPClientSessionǁ_update_user_agent__mutmut_18, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_19': xǁCDPClientSessionǁ_update_user_agent__mutmut_19, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_20': xǁCDPClientSessionǁ_update_user_agent__mutmut_20, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_21': xǁCDPClientSessionǁ_update_user_agent__mutmut_21, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_22': xǁCDPClientSessionǁ_update_user_agent__mutmut_22, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_23': xǁCDPClientSessionǁ_update_user_agent__mutmut_23, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_24': xǁCDPClientSessionǁ_update_user_agent__mutmut_24, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_25': xǁCDPClientSessionǁ_update_user_agent__mutmut_25, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_26': xǁCDPClientSessionǁ_update_user_agent__mutmut_26, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_27': xǁCDPClientSessionǁ_update_user_agent__mutmut_27, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_28': xǁCDPClientSessionǁ_update_user_agent__mutmut_28, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_29': xǁCDPClientSessionǁ_update_user_agent__mutmut_29, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_30': xǁCDPClientSessionǁ_update_user_agent__mutmut_30, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_31': xǁCDPClientSessionǁ_update_user_agent__mutmut_31, 
        'xǁCDPClientSessionǁ_update_user_agent__mutmut_32': xǁCDPClientSessionǁ_update_user_agent__mutmut_32
    }
    
    def _update_user_agent(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCDPClientSessionǁ_update_user_agent__mutmut_orig"), object.__getattribute__(self, "xǁCDPClientSessionǁ_update_user_agent__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _update_user_agent.__signature__ = _mutmut_signature(xǁCDPClientSessionǁ_update_user_agent__mutmut_orig)
    xǁCDPClientSessionǁ_update_user_agent__mutmut_orig.__name__ = 'xǁCDPClientSessionǁ_update_user_agent'

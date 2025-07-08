from __future__ import annotations

import json
import logging
from threading import RLock, Thread, current_thread
from typing import Any
from urllib.parse import unquote_plus, urlparse

from certifi import where as certify_where
from websocket import ABNF, STATUS_NORMAL, WebSocketApp, enableTrace  # type: ignore[attr-defined,import]

from streamlink.logger import TRACE, root as rootlogger
from streamlink.session import Streamlink


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


class WebsocketClient(Thread):
    OPCODE_CONT: int = ABNF.OPCODE_CONT
    OPCODE_TEXT: int = ABNF.OPCODE_TEXT
    OPCODE_BINARY: int = ABNF.OPCODE_BINARY
    OPCODE_CLOSE: int = ABNF.OPCODE_CLOSE
    OPCODE_PING: int = ABNF.OPCODE_PING
    OPCODE_PONG: int = ABNF.OPCODE_PONG

    _id: int = 0

    ws: WebSocketApp

    def xǁWebsocketClientǁ__init____mutmut_orig(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_1(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = True,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_2(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 1,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_3(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "XXXX",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_4(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level < TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_5(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(None, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_6(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=None)  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_7(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_8(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, )  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_9(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(False, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_10(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(None, logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_11(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), None))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_12(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_13(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), ))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_14(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(None), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_15(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_16(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = None
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_17(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = None
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_18(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_19(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(None):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_20(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(False for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_21(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith(None)):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_22(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("XXUser-Agent: XX")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_23(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("user-agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_24(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("USER-AGENT: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_25(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_26(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(None)

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_27(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['XXUser-AgentXX']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_28(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['user-agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_29(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['USER-AGENT']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_30(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_31(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = None
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_32(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = None
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_33(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option(None)
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_34(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("XXhttp-proxyXX")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_35(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("HTTP-PROXY")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_36(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("Http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_37(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = None
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_38(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(None)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_39(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = None
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_40(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["XXproxy_typeXX"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_41(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["PROXY_TYPE"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_42(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["Proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_43(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = None
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_44(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["XXhttp_proxy_hostXX"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_45(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["HTTP_PROXY_HOST"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_46(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["Http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_47(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = None
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_48(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["XXhttp_proxy_portXX"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_49(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["HTTP_PROXY_PORT"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_50(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["Http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_51(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = None

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_52(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["XXhttp_proxy_authXX"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_53(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["HTTP_PROXY_AUTH"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_54(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["Http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_55(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(None), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_56(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(None)

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_57(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password and "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_58(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "XXXX")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_59(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = None
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_60(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = True
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_61(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = None

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_62(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_63(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = None
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_64(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault(None, certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_65(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", None)

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_66(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault(certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_67(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", )

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_68(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("XXca_certsXX", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_69(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("CA_CERTS", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_70(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("Ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_71(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = None
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_72(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(None, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_73(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, None, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_74(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, None, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_75(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, None)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_76(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_77(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_78(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_79(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, )
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_80(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = None

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_81(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockoptXX=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_82(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            ssloptXX=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_83(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            hostXX=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_84(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            originXX=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_85(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_originXX=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_86(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_intervalXX=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_87(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeoutXX=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_88(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payloadXX=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_89(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=None,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_90(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=None,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_91(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=None,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_92(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=None,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_93(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=None,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_94(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=None,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_95(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=None,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_96(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=None,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_97(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_98(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_99(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_100(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_101(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_102(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_103(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_104(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_105(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_106(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id = 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_107(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id -= 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_108(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 2
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_109(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=None,
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_110(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=None,
        )

    def xǁWebsocketClientǁ__init____mutmut_111(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            daemon=True,
        )

    def xǁWebsocketClientǁ__init____mutmut_112(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            )

    def xǁWebsocketClientǁ__init____mutmut_113(
        self,
        session: Streamlink,
        url: str,
        subprotocols: list[str] | None = None,
        header: list[str] | dict[str, str] | None = None,
        cookie: str | None = None,
        sockopt: tuple | None = None,
        sslopt: dict | None = None,
        host: str | None = None,
        origin: str | None = None,
        suppress_origin: bool = False,
        ping_interval: int | float = 0,
        ping_timeout: int | float | None = None,
        ping_payload: str = "",
    ):
        if rootlogger.level <= TRACE:
            enableTrace(True, handler=next(iter(rootlogger.handlers), logging.StreamHandler()))  # type: ignore

        if not header:
            header = []
        elif isinstance(header, dict):
            header = [f"{k!s}: {v!s}" for k, v in header.items()]
        if not any(True for h in header if h.startswith("User-Agent: ")):
            header.append(f"User-Agent: {session.http.headers['User-Agent']!s}")

        proxy_options: dict[str, Any] = {}
        http_proxy: str | None = session.get_option("http-proxy")
        if http_proxy:
            p = urlparse(http_proxy)
            proxy_options["proxy_type"] = p.scheme
            proxy_options["http_proxy_host"] = p.hostname
            if p.port:  # pragma: no branch
                proxy_options["http_proxy_port"] = p.port
            if p.username:  # pragma: no branch
                proxy_options["http_proxy_auth"] = unquote_plus(p.username), unquote_plus(p.password or "")

        self._reconnect = False
        self._reconnect_lock = RLock()

        if not sslopt:  # pragma: no cover
            sslopt = {}
        sslopt.setdefault("ca_certs", certify_where())

        self.session = session
        self._ws_init(url, subprotocols, header, cookie)
        self._ws_rundata = dict(
            sockopt=sockopt,
            sslopt=sslopt,
            host=host,
            origin=origin,
            suppress_origin=suppress_origin,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            ping_payload=ping_payload,
            **proxy_options,
        )

        self._id += 1
        super().__init__(
            name=f"Thread-{self.__class__.__name__}-{self._id}",
            daemon=False,
        )
    
    xǁWebsocketClientǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebsocketClientǁ__init____mutmut_1': xǁWebsocketClientǁ__init____mutmut_1, 
        'xǁWebsocketClientǁ__init____mutmut_2': xǁWebsocketClientǁ__init____mutmut_2, 
        'xǁWebsocketClientǁ__init____mutmut_3': xǁWebsocketClientǁ__init____mutmut_3, 
        'xǁWebsocketClientǁ__init____mutmut_4': xǁWebsocketClientǁ__init____mutmut_4, 
        'xǁWebsocketClientǁ__init____mutmut_5': xǁWebsocketClientǁ__init____mutmut_5, 
        'xǁWebsocketClientǁ__init____mutmut_6': xǁWebsocketClientǁ__init____mutmut_6, 
        'xǁWebsocketClientǁ__init____mutmut_7': xǁWebsocketClientǁ__init____mutmut_7, 
        'xǁWebsocketClientǁ__init____mutmut_8': xǁWebsocketClientǁ__init____mutmut_8, 
        'xǁWebsocketClientǁ__init____mutmut_9': xǁWebsocketClientǁ__init____mutmut_9, 
        'xǁWebsocketClientǁ__init____mutmut_10': xǁWebsocketClientǁ__init____mutmut_10, 
        'xǁWebsocketClientǁ__init____mutmut_11': xǁWebsocketClientǁ__init____mutmut_11, 
        'xǁWebsocketClientǁ__init____mutmut_12': xǁWebsocketClientǁ__init____mutmut_12, 
        'xǁWebsocketClientǁ__init____mutmut_13': xǁWebsocketClientǁ__init____mutmut_13, 
        'xǁWebsocketClientǁ__init____mutmut_14': xǁWebsocketClientǁ__init____mutmut_14, 
        'xǁWebsocketClientǁ__init____mutmut_15': xǁWebsocketClientǁ__init____mutmut_15, 
        'xǁWebsocketClientǁ__init____mutmut_16': xǁWebsocketClientǁ__init____mutmut_16, 
        'xǁWebsocketClientǁ__init____mutmut_17': xǁWebsocketClientǁ__init____mutmut_17, 
        'xǁWebsocketClientǁ__init____mutmut_18': xǁWebsocketClientǁ__init____mutmut_18, 
        'xǁWebsocketClientǁ__init____mutmut_19': xǁWebsocketClientǁ__init____mutmut_19, 
        'xǁWebsocketClientǁ__init____mutmut_20': xǁWebsocketClientǁ__init____mutmut_20, 
        'xǁWebsocketClientǁ__init____mutmut_21': xǁWebsocketClientǁ__init____mutmut_21, 
        'xǁWebsocketClientǁ__init____mutmut_22': xǁWebsocketClientǁ__init____mutmut_22, 
        'xǁWebsocketClientǁ__init____mutmut_23': xǁWebsocketClientǁ__init____mutmut_23, 
        'xǁWebsocketClientǁ__init____mutmut_24': xǁWebsocketClientǁ__init____mutmut_24, 
        'xǁWebsocketClientǁ__init____mutmut_25': xǁWebsocketClientǁ__init____mutmut_25, 
        'xǁWebsocketClientǁ__init____mutmut_26': xǁWebsocketClientǁ__init____mutmut_26, 
        'xǁWebsocketClientǁ__init____mutmut_27': xǁWebsocketClientǁ__init____mutmut_27, 
        'xǁWebsocketClientǁ__init____mutmut_28': xǁWebsocketClientǁ__init____mutmut_28, 
        'xǁWebsocketClientǁ__init____mutmut_29': xǁWebsocketClientǁ__init____mutmut_29, 
        'xǁWebsocketClientǁ__init____mutmut_30': xǁWebsocketClientǁ__init____mutmut_30, 
        'xǁWebsocketClientǁ__init____mutmut_31': xǁWebsocketClientǁ__init____mutmut_31, 
        'xǁWebsocketClientǁ__init____mutmut_32': xǁWebsocketClientǁ__init____mutmut_32, 
        'xǁWebsocketClientǁ__init____mutmut_33': xǁWebsocketClientǁ__init____mutmut_33, 
        'xǁWebsocketClientǁ__init____mutmut_34': xǁWebsocketClientǁ__init____mutmut_34, 
        'xǁWebsocketClientǁ__init____mutmut_35': xǁWebsocketClientǁ__init____mutmut_35, 
        'xǁWebsocketClientǁ__init____mutmut_36': xǁWebsocketClientǁ__init____mutmut_36, 
        'xǁWebsocketClientǁ__init____mutmut_37': xǁWebsocketClientǁ__init____mutmut_37, 
        'xǁWebsocketClientǁ__init____mutmut_38': xǁWebsocketClientǁ__init____mutmut_38, 
        'xǁWebsocketClientǁ__init____mutmut_39': xǁWebsocketClientǁ__init____mutmut_39, 
        'xǁWebsocketClientǁ__init____mutmut_40': xǁWebsocketClientǁ__init____mutmut_40, 
        'xǁWebsocketClientǁ__init____mutmut_41': xǁWebsocketClientǁ__init____mutmut_41, 
        'xǁWebsocketClientǁ__init____mutmut_42': xǁWebsocketClientǁ__init____mutmut_42, 
        'xǁWebsocketClientǁ__init____mutmut_43': xǁWebsocketClientǁ__init____mutmut_43, 
        'xǁWebsocketClientǁ__init____mutmut_44': xǁWebsocketClientǁ__init____mutmut_44, 
        'xǁWebsocketClientǁ__init____mutmut_45': xǁWebsocketClientǁ__init____mutmut_45, 
        'xǁWebsocketClientǁ__init____mutmut_46': xǁWebsocketClientǁ__init____mutmut_46, 
        'xǁWebsocketClientǁ__init____mutmut_47': xǁWebsocketClientǁ__init____mutmut_47, 
        'xǁWebsocketClientǁ__init____mutmut_48': xǁWebsocketClientǁ__init____mutmut_48, 
        'xǁWebsocketClientǁ__init____mutmut_49': xǁWebsocketClientǁ__init____mutmut_49, 
        'xǁWebsocketClientǁ__init____mutmut_50': xǁWebsocketClientǁ__init____mutmut_50, 
        'xǁWebsocketClientǁ__init____mutmut_51': xǁWebsocketClientǁ__init____mutmut_51, 
        'xǁWebsocketClientǁ__init____mutmut_52': xǁWebsocketClientǁ__init____mutmut_52, 
        'xǁWebsocketClientǁ__init____mutmut_53': xǁWebsocketClientǁ__init____mutmut_53, 
        'xǁWebsocketClientǁ__init____mutmut_54': xǁWebsocketClientǁ__init____mutmut_54, 
        'xǁWebsocketClientǁ__init____mutmut_55': xǁWebsocketClientǁ__init____mutmut_55, 
        'xǁWebsocketClientǁ__init____mutmut_56': xǁWebsocketClientǁ__init____mutmut_56, 
        'xǁWebsocketClientǁ__init____mutmut_57': xǁWebsocketClientǁ__init____mutmut_57, 
        'xǁWebsocketClientǁ__init____mutmut_58': xǁWebsocketClientǁ__init____mutmut_58, 
        'xǁWebsocketClientǁ__init____mutmut_59': xǁWebsocketClientǁ__init____mutmut_59, 
        'xǁWebsocketClientǁ__init____mutmut_60': xǁWebsocketClientǁ__init____mutmut_60, 
        'xǁWebsocketClientǁ__init____mutmut_61': xǁWebsocketClientǁ__init____mutmut_61, 
        'xǁWebsocketClientǁ__init____mutmut_62': xǁWebsocketClientǁ__init____mutmut_62, 
        'xǁWebsocketClientǁ__init____mutmut_63': xǁWebsocketClientǁ__init____mutmut_63, 
        'xǁWebsocketClientǁ__init____mutmut_64': xǁWebsocketClientǁ__init____mutmut_64, 
        'xǁWebsocketClientǁ__init____mutmut_65': xǁWebsocketClientǁ__init____mutmut_65, 
        'xǁWebsocketClientǁ__init____mutmut_66': xǁWebsocketClientǁ__init____mutmut_66, 
        'xǁWebsocketClientǁ__init____mutmut_67': xǁWebsocketClientǁ__init____mutmut_67, 
        'xǁWebsocketClientǁ__init____mutmut_68': xǁWebsocketClientǁ__init____mutmut_68, 
        'xǁWebsocketClientǁ__init____mutmut_69': xǁWebsocketClientǁ__init____mutmut_69, 
        'xǁWebsocketClientǁ__init____mutmut_70': xǁWebsocketClientǁ__init____mutmut_70, 
        'xǁWebsocketClientǁ__init____mutmut_71': xǁWebsocketClientǁ__init____mutmut_71, 
        'xǁWebsocketClientǁ__init____mutmut_72': xǁWebsocketClientǁ__init____mutmut_72, 
        'xǁWebsocketClientǁ__init____mutmut_73': xǁWebsocketClientǁ__init____mutmut_73, 
        'xǁWebsocketClientǁ__init____mutmut_74': xǁWebsocketClientǁ__init____mutmut_74, 
        'xǁWebsocketClientǁ__init____mutmut_75': xǁWebsocketClientǁ__init____mutmut_75, 
        'xǁWebsocketClientǁ__init____mutmut_76': xǁWebsocketClientǁ__init____mutmut_76, 
        'xǁWebsocketClientǁ__init____mutmut_77': xǁWebsocketClientǁ__init____mutmut_77, 
        'xǁWebsocketClientǁ__init____mutmut_78': xǁWebsocketClientǁ__init____mutmut_78, 
        'xǁWebsocketClientǁ__init____mutmut_79': xǁWebsocketClientǁ__init____mutmut_79, 
        'xǁWebsocketClientǁ__init____mutmut_80': xǁWebsocketClientǁ__init____mutmut_80, 
        'xǁWebsocketClientǁ__init____mutmut_81': xǁWebsocketClientǁ__init____mutmut_81, 
        'xǁWebsocketClientǁ__init____mutmut_82': xǁWebsocketClientǁ__init____mutmut_82, 
        'xǁWebsocketClientǁ__init____mutmut_83': xǁWebsocketClientǁ__init____mutmut_83, 
        'xǁWebsocketClientǁ__init____mutmut_84': xǁWebsocketClientǁ__init____mutmut_84, 
        'xǁWebsocketClientǁ__init____mutmut_85': xǁWebsocketClientǁ__init____mutmut_85, 
        'xǁWebsocketClientǁ__init____mutmut_86': xǁWebsocketClientǁ__init____mutmut_86, 
        'xǁWebsocketClientǁ__init____mutmut_87': xǁWebsocketClientǁ__init____mutmut_87, 
        'xǁWebsocketClientǁ__init____mutmut_88': xǁWebsocketClientǁ__init____mutmut_88, 
        'xǁWebsocketClientǁ__init____mutmut_89': xǁWebsocketClientǁ__init____mutmut_89, 
        'xǁWebsocketClientǁ__init____mutmut_90': xǁWebsocketClientǁ__init____mutmut_90, 
        'xǁWebsocketClientǁ__init____mutmut_91': xǁWebsocketClientǁ__init____mutmut_91, 
        'xǁWebsocketClientǁ__init____mutmut_92': xǁWebsocketClientǁ__init____mutmut_92, 
        'xǁWebsocketClientǁ__init____mutmut_93': xǁWebsocketClientǁ__init____mutmut_93, 
        'xǁWebsocketClientǁ__init____mutmut_94': xǁWebsocketClientǁ__init____mutmut_94, 
        'xǁWebsocketClientǁ__init____mutmut_95': xǁWebsocketClientǁ__init____mutmut_95, 
        'xǁWebsocketClientǁ__init____mutmut_96': xǁWebsocketClientǁ__init____mutmut_96, 
        'xǁWebsocketClientǁ__init____mutmut_97': xǁWebsocketClientǁ__init____mutmut_97, 
        'xǁWebsocketClientǁ__init____mutmut_98': xǁWebsocketClientǁ__init____mutmut_98, 
        'xǁWebsocketClientǁ__init____mutmut_99': xǁWebsocketClientǁ__init____mutmut_99, 
        'xǁWebsocketClientǁ__init____mutmut_100': xǁWebsocketClientǁ__init____mutmut_100, 
        'xǁWebsocketClientǁ__init____mutmut_101': xǁWebsocketClientǁ__init____mutmut_101, 
        'xǁWebsocketClientǁ__init____mutmut_102': xǁWebsocketClientǁ__init____mutmut_102, 
        'xǁWebsocketClientǁ__init____mutmut_103': xǁWebsocketClientǁ__init____mutmut_103, 
        'xǁWebsocketClientǁ__init____mutmut_104': xǁWebsocketClientǁ__init____mutmut_104, 
        'xǁWebsocketClientǁ__init____mutmut_105': xǁWebsocketClientǁ__init____mutmut_105, 
        'xǁWebsocketClientǁ__init____mutmut_106': xǁWebsocketClientǁ__init____mutmut_106, 
        'xǁWebsocketClientǁ__init____mutmut_107': xǁWebsocketClientǁ__init____mutmut_107, 
        'xǁWebsocketClientǁ__init____mutmut_108': xǁWebsocketClientǁ__init____mutmut_108, 
        'xǁWebsocketClientǁ__init____mutmut_109': xǁWebsocketClientǁ__init____mutmut_109, 
        'xǁWebsocketClientǁ__init____mutmut_110': xǁWebsocketClientǁ__init____mutmut_110, 
        'xǁWebsocketClientǁ__init____mutmut_111': xǁWebsocketClientǁ__init____mutmut_111, 
        'xǁWebsocketClientǁ__init____mutmut_112': xǁWebsocketClientǁ__init____mutmut_112, 
        'xǁWebsocketClientǁ__init____mutmut_113': xǁWebsocketClientǁ__init____mutmut_113
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebsocketClientǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁWebsocketClientǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁWebsocketClientǁ__init____mutmut_orig)
    xǁWebsocketClientǁ__init____mutmut_orig.__name__ = 'xǁWebsocketClientǁ__init__'

    def xǁWebsocketClientǁ_ws_init__mutmut_orig(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_1(self, url, subprotocols, header, cookie):
        self.ws = None

    def xǁWebsocketClientǁ_ws_init__mutmut_2(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=None,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_3(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=None,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_4(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=None,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_5(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=None,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_6(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=None,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_7(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=None,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_8(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=None,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_9(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=None,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_10(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=None,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_11(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=None,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_12(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=None,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_13(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=None,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_14(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_15(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_16(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_17(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_18(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_19(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_20(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_21(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_22(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_23(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_cont_message=self.on_cont_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_24(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_data=self.on_data,
        )

    def xǁWebsocketClientǁ_ws_init__mutmut_25(self, url, subprotocols, header, cookie):
        self.ws = WebSocketApp(
            url=url,
            subprotocols=subprotocols,
            header=header,
            cookie=cookie,
            on_open=self.on_open,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong,
            on_message=self.on_message,
            on_cont_message=self.on_cont_message,
            )
    
    xǁWebsocketClientǁ_ws_init__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebsocketClientǁ_ws_init__mutmut_1': xǁWebsocketClientǁ_ws_init__mutmut_1, 
        'xǁWebsocketClientǁ_ws_init__mutmut_2': xǁWebsocketClientǁ_ws_init__mutmut_2, 
        'xǁWebsocketClientǁ_ws_init__mutmut_3': xǁWebsocketClientǁ_ws_init__mutmut_3, 
        'xǁWebsocketClientǁ_ws_init__mutmut_4': xǁWebsocketClientǁ_ws_init__mutmut_4, 
        'xǁWebsocketClientǁ_ws_init__mutmut_5': xǁWebsocketClientǁ_ws_init__mutmut_5, 
        'xǁWebsocketClientǁ_ws_init__mutmut_6': xǁWebsocketClientǁ_ws_init__mutmut_6, 
        'xǁWebsocketClientǁ_ws_init__mutmut_7': xǁWebsocketClientǁ_ws_init__mutmut_7, 
        'xǁWebsocketClientǁ_ws_init__mutmut_8': xǁWebsocketClientǁ_ws_init__mutmut_8, 
        'xǁWebsocketClientǁ_ws_init__mutmut_9': xǁWebsocketClientǁ_ws_init__mutmut_9, 
        'xǁWebsocketClientǁ_ws_init__mutmut_10': xǁWebsocketClientǁ_ws_init__mutmut_10, 
        'xǁWebsocketClientǁ_ws_init__mutmut_11': xǁWebsocketClientǁ_ws_init__mutmut_11, 
        'xǁWebsocketClientǁ_ws_init__mutmut_12': xǁWebsocketClientǁ_ws_init__mutmut_12, 
        'xǁWebsocketClientǁ_ws_init__mutmut_13': xǁWebsocketClientǁ_ws_init__mutmut_13, 
        'xǁWebsocketClientǁ_ws_init__mutmut_14': xǁWebsocketClientǁ_ws_init__mutmut_14, 
        'xǁWebsocketClientǁ_ws_init__mutmut_15': xǁWebsocketClientǁ_ws_init__mutmut_15, 
        'xǁWebsocketClientǁ_ws_init__mutmut_16': xǁWebsocketClientǁ_ws_init__mutmut_16, 
        'xǁWebsocketClientǁ_ws_init__mutmut_17': xǁWebsocketClientǁ_ws_init__mutmut_17, 
        'xǁWebsocketClientǁ_ws_init__mutmut_18': xǁWebsocketClientǁ_ws_init__mutmut_18, 
        'xǁWebsocketClientǁ_ws_init__mutmut_19': xǁWebsocketClientǁ_ws_init__mutmut_19, 
        'xǁWebsocketClientǁ_ws_init__mutmut_20': xǁWebsocketClientǁ_ws_init__mutmut_20, 
        'xǁWebsocketClientǁ_ws_init__mutmut_21': xǁWebsocketClientǁ_ws_init__mutmut_21, 
        'xǁWebsocketClientǁ_ws_init__mutmut_22': xǁWebsocketClientǁ_ws_init__mutmut_22, 
        'xǁWebsocketClientǁ_ws_init__mutmut_23': xǁWebsocketClientǁ_ws_init__mutmut_23, 
        'xǁWebsocketClientǁ_ws_init__mutmut_24': xǁWebsocketClientǁ_ws_init__mutmut_24, 
        'xǁWebsocketClientǁ_ws_init__mutmut_25': xǁWebsocketClientǁ_ws_init__mutmut_25
    }
    
    def _ws_init(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebsocketClientǁ_ws_init__mutmut_orig"), object.__getattribute__(self, "xǁWebsocketClientǁ_ws_init__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ws_init.__signature__ = _mutmut_signature(xǁWebsocketClientǁ_ws_init__mutmut_orig)
    xǁWebsocketClientǁ_ws_init__mutmut_orig.__name__ = 'xǁWebsocketClientǁ_ws_init'

    def xǁWebsocketClientǁrun__mutmut_orig(self) -> None:
        while True:
            log.debug(f"Connecting to: {self.ws.url}")
            self.ws.run_forever(**self._ws_rundata)
            # check if closed via a reconnect() call
            with self._reconnect_lock:
                if not self._reconnect:
                    return
                self._reconnect = False

    def xǁWebsocketClientǁrun__mutmut_1(self) -> None:
        while False:
            log.debug(f"Connecting to: {self.ws.url}")
            self.ws.run_forever(**self._ws_rundata)
            # check if closed via a reconnect() call
            with self._reconnect_lock:
                if not self._reconnect:
                    return
                self._reconnect = False

    def xǁWebsocketClientǁrun__mutmut_2(self) -> None:
        while True:
            log.debug(None)
            self.ws.run_forever(**self._ws_rundata)
            # check if closed via a reconnect() call
            with self._reconnect_lock:
                if not self._reconnect:
                    return
                self._reconnect = False

    def xǁWebsocketClientǁrun__mutmut_3(self) -> None:
        while True:
            log.debug(f"Connecting to: {self.ws.url}")
            self.ws.run_forever(**self._ws_rundata)
            # check if closed via a reconnect() call
            with self._reconnect_lock:
                if self._reconnect:
                    return
                self._reconnect = False

    def xǁWebsocketClientǁrun__mutmut_4(self) -> None:
        while True:
            log.debug(f"Connecting to: {self.ws.url}")
            self.ws.run_forever(**self._ws_rundata)
            # check if closed via a reconnect() call
            with self._reconnect_lock:
                if not self._reconnect:
                    return
                self._reconnect = None

    def xǁWebsocketClientǁrun__mutmut_5(self) -> None:
        while True:
            log.debug(f"Connecting to: {self.ws.url}")
            self.ws.run_forever(**self._ws_rundata)
            # check if closed via a reconnect() call
            with self._reconnect_lock:
                if not self._reconnect:
                    return
                self._reconnect = True
    
    xǁWebsocketClientǁrun__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebsocketClientǁrun__mutmut_1': xǁWebsocketClientǁrun__mutmut_1, 
        'xǁWebsocketClientǁrun__mutmut_2': xǁWebsocketClientǁrun__mutmut_2, 
        'xǁWebsocketClientǁrun__mutmut_3': xǁWebsocketClientǁrun__mutmut_3, 
        'xǁWebsocketClientǁrun__mutmut_4': xǁWebsocketClientǁrun__mutmut_4, 
        'xǁWebsocketClientǁrun__mutmut_5': xǁWebsocketClientǁrun__mutmut_5
    }
    
    def run(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebsocketClientǁrun__mutmut_orig"), object.__getattribute__(self, "xǁWebsocketClientǁrun__mutmut_mutants"), args, kwargs, self)
        return result 
    
    run.__signature__ = _mutmut_signature(xǁWebsocketClientǁrun__mutmut_orig)
    xǁWebsocketClientǁrun__mutmut_orig.__name__ = 'xǁWebsocketClientǁrun'

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_orig(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_1(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_2(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug(None)
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_3(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("XXReconnecting...XX")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_4(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_5(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("RECONNECTING...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_6(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = None
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_7(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = False
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_8(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts and {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_9(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=None,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_10(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=None,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_11(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=None,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_12(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=None,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_13(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_14(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_15(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_16(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_17(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is not None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_18(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is not None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_19(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is not None else header,
                cookie=self.ws.cookie if cookie is None else cookie,
            )

    # ----

    def xǁWebsocketClientǁreconnect__mutmut_20(
        self,
        url: str | None = None,
        subprotocols: list[str] | None = None,
        header: list | dict | None = None,
        cookie: str | None = None,
        closeopts: dict | None = None,
    ) -> None:
        with self._reconnect_lock:
            # ws connection is not active (anymore)
            if not self.ws.keep_running:
                return
            log.debug("Reconnecting...")
            self._reconnect = True
            self.ws.close(**(closeopts or {}))
            self._ws_init(
                url=self.ws.url if url is None else url,
                subprotocols=self.ws.subprotocols if subprotocols is None else subprotocols,
                header=self.ws.header if header is None else header,
                cookie=self.ws.cookie if cookie is not None else cookie,
            )
    
    xǁWebsocketClientǁreconnect__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebsocketClientǁreconnect__mutmut_1': xǁWebsocketClientǁreconnect__mutmut_1, 
        'xǁWebsocketClientǁreconnect__mutmut_2': xǁWebsocketClientǁreconnect__mutmut_2, 
        'xǁWebsocketClientǁreconnect__mutmut_3': xǁWebsocketClientǁreconnect__mutmut_3, 
        'xǁWebsocketClientǁreconnect__mutmut_4': xǁWebsocketClientǁreconnect__mutmut_4, 
        'xǁWebsocketClientǁreconnect__mutmut_5': xǁWebsocketClientǁreconnect__mutmut_5, 
        'xǁWebsocketClientǁreconnect__mutmut_6': xǁWebsocketClientǁreconnect__mutmut_6, 
        'xǁWebsocketClientǁreconnect__mutmut_7': xǁWebsocketClientǁreconnect__mutmut_7, 
        'xǁWebsocketClientǁreconnect__mutmut_8': xǁWebsocketClientǁreconnect__mutmut_8, 
        'xǁWebsocketClientǁreconnect__mutmut_9': xǁWebsocketClientǁreconnect__mutmut_9, 
        'xǁWebsocketClientǁreconnect__mutmut_10': xǁWebsocketClientǁreconnect__mutmut_10, 
        'xǁWebsocketClientǁreconnect__mutmut_11': xǁWebsocketClientǁreconnect__mutmut_11, 
        'xǁWebsocketClientǁreconnect__mutmut_12': xǁWebsocketClientǁreconnect__mutmut_12, 
        'xǁWebsocketClientǁreconnect__mutmut_13': xǁWebsocketClientǁreconnect__mutmut_13, 
        'xǁWebsocketClientǁreconnect__mutmut_14': xǁWebsocketClientǁreconnect__mutmut_14, 
        'xǁWebsocketClientǁreconnect__mutmut_15': xǁWebsocketClientǁreconnect__mutmut_15, 
        'xǁWebsocketClientǁreconnect__mutmut_16': xǁWebsocketClientǁreconnect__mutmut_16, 
        'xǁWebsocketClientǁreconnect__mutmut_17': xǁWebsocketClientǁreconnect__mutmut_17, 
        'xǁWebsocketClientǁreconnect__mutmut_18': xǁWebsocketClientǁreconnect__mutmut_18, 
        'xǁWebsocketClientǁreconnect__mutmut_19': xǁWebsocketClientǁreconnect__mutmut_19, 
        'xǁWebsocketClientǁreconnect__mutmut_20': xǁWebsocketClientǁreconnect__mutmut_20
    }
    
    def reconnect(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebsocketClientǁreconnect__mutmut_orig"), object.__getattribute__(self, "xǁWebsocketClientǁreconnect__mutmut_mutants"), args, kwargs, self)
        return result 
    
    reconnect.__signature__ = _mutmut_signature(xǁWebsocketClientǁreconnect__mutmut_orig)
    xǁWebsocketClientǁreconnect__mutmut_orig.__name__ = 'xǁWebsocketClientǁreconnect'

    def xǁWebsocketClientǁclose__mutmut_orig(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_1(self, status: int = STATUS_NORMAL, reason: str | bytes = "XXXX", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_2(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 4) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_3(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = None
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_4(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(None, encoding="utf-8")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_5(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding=None)
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_6(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(encoding="utf-8")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_7(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, )
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_8(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="XXutf-8XX")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_9(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="UTF-8")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_10(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="Utf-8")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_11(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=None, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_12(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=status, reason=None, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_13(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=status, reason=reason, timeout=None)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_14(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_15(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=status, timeout=timeout)
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_16(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=status, reason=reason, )
        if self.is_alive() and current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_17(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() or current_thread() is not self:
            self.join()

    def xǁWebsocketClientǁclose__mutmut_18(self, status: int = STATUS_NORMAL, reason: str | bytes = "", timeout: int = 3) -> None:
        if isinstance(reason, str):
            reason = bytes(reason, encoding="utf-8")
        self.ws.close(status=status, reason=reason, timeout=timeout)
        if self.is_alive() and current_thread() is self:
            self.join()
    
    xǁWebsocketClientǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebsocketClientǁclose__mutmut_1': xǁWebsocketClientǁclose__mutmut_1, 
        'xǁWebsocketClientǁclose__mutmut_2': xǁWebsocketClientǁclose__mutmut_2, 
        'xǁWebsocketClientǁclose__mutmut_3': xǁWebsocketClientǁclose__mutmut_3, 
        'xǁWebsocketClientǁclose__mutmut_4': xǁWebsocketClientǁclose__mutmut_4, 
        'xǁWebsocketClientǁclose__mutmut_5': xǁWebsocketClientǁclose__mutmut_5, 
        'xǁWebsocketClientǁclose__mutmut_6': xǁWebsocketClientǁclose__mutmut_6, 
        'xǁWebsocketClientǁclose__mutmut_7': xǁWebsocketClientǁclose__mutmut_7, 
        'xǁWebsocketClientǁclose__mutmut_8': xǁWebsocketClientǁclose__mutmut_8, 
        'xǁWebsocketClientǁclose__mutmut_9': xǁWebsocketClientǁclose__mutmut_9, 
        'xǁWebsocketClientǁclose__mutmut_10': xǁWebsocketClientǁclose__mutmut_10, 
        'xǁWebsocketClientǁclose__mutmut_11': xǁWebsocketClientǁclose__mutmut_11, 
        'xǁWebsocketClientǁclose__mutmut_12': xǁWebsocketClientǁclose__mutmut_12, 
        'xǁWebsocketClientǁclose__mutmut_13': xǁWebsocketClientǁclose__mutmut_13, 
        'xǁWebsocketClientǁclose__mutmut_14': xǁWebsocketClientǁclose__mutmut_14, 
        'xǁWebsocketClientǁclose__mutmut_15': xǁWebsocketClientǁclose__mutmut_15, 
        'xǁWebsocketClientǁclose__mutmut_16': xǁWebsocketClientǁclose__mutmut_16, 
        'xǁWebsocketClientǁclose__mutmut_17': xǁWebsocketClientǁclose__mutmut_17, 
        'xǁWebsocketClientǁclose__mutmut_18': xǁWebsocketClientǁclose__mutmut_18
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebsocketClientǁclose__mutmut_orig"), object.__getattribute__(self, "xǁWebsocketClientǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁWebsocketClientǁclose__mutmut_orig)
    xǁWebsocketClientǁclose__mutmut_orig.__name__ = 'xǁWebsocketClientǁclose'

    def xǁWebsocketClientǁsend__mutmut_orig(self, data: str | bytes, opcode: int = ABNF.OPCODE_TEXT) -> None:
        return self.ws.send(data, opcode)

    def xǁWebsocketClientǁsend__mutmut_1(self, data: str | bytes, opcode: int = ABNF.OPCODE_TEXT) -> None:
        return self.ws.send(None, opcode)

    def xǁWebsocketClientǁsend__mutmut_2(self, data: str | bytes, opcode: int = ABNF.OPCODE_TEXT) -> None:
        return self.ws.send(data, None)

    def xǁWebsocketClientǁsend__mutmut_3(self, data: str | bytes, opcode: int = ABNF.OPCODE_TEXT) -> None:
        return self.ws.send(opcode)

    def xǁWebsocketClientǁsend__mutmut_4(self, data: str | bytes, opcode: int = ABNF.OPCODE_TEXT) -> None:
        return self.ws.send(data, )
    
    xǁWebsocketClientǁsend__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebsocketClientǁsend__mutmut_1': xǁWebsocketClientǁsend__mutmut_1, 
        'xǁWebsocketClientǁsend__mutmut_2': xǁWebsocketClientǁsend__mutmut_2, 
        'xǁWebsocketClientǁsend__mutmut_3': xǁWebsocketClientǁsend__mutmut_3, 
        'xǁWebsocketClientǁsend__mutmut_4': xǁWebsocketClientǁsend__mutmut_4
    }
    
    def send(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebsocketClientǁsend__mutmut_orig"), object.__getattribute__(self, "xǁWebsocketClientǁsend__mutmut_mutants"), args, kwargs, self)
        return result 
    
    send.__signature__ = _mutmut_signature(xǁWebsocketClientǁsend__mutmut_orig)
    xǁWebsocketClientǁsend__mutmut_orig.__name__ = 'xǁWebsocketClientǁsend'

    def xǁWebsocketClientǁsend_json__mutmut_orig(self, data: Any) -> None:
        return self.send(json.dumps(data, indent=None, separators=(",", ":")))

    def xǁWebsocketClientǁsend_json__mutmut_1(self, data: Any) -> None:
        return self.send(None)

    def xǁWebsocketClientǁsend_json__mutmut_2(self, data: Any) -> None:
        return self.send(json.dumps(None, indent=None, separators=(",", ":")))

    def xǁWebsocketClientǁsend_json__mutmut_3(self, data: Any) -> None:
        return self.send(json.dumps(data, indent=None, separators=None))

    def xǁWebsocketClientǁsend_json__mutmut_4(self, data: Any) -> None:
        return self.send(json.dumps(indent=None, separators=(",", ":")))

    def xǁWebsocketClientǁsend_json__mutmut_5(self, data: Any) -> None:
        return self.send(json.dumps(data, separators=(",", ":")))

    def xǁWebsocketClientǁsend_json__mutmut_6(self, data: Any) -> None:
        return self.send(json.dumps(data, indent=None, ))

    def xǁWebsocketClientǁsend_json__mutmut_7(self, data: Any) -> None:
        return self.send(json.dumps(data, indent=None, separators=("XX,XX", ":")))

    def xǁWebsocketClientǁsend_json__mutmut_8(self, data: Any) -> None:
        return self.send(json.dumps(data, indent=None, separators=(",", "XX:XX")))
    
    xǁWebsocketClientǁsend_json__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebsocketClientǁsend_json__mutmut_1': xǁWebsocketClientǁsend_json__mutmut_1, 
        'xǁWebsocketClientǁsend_json__mutmut_2': xǁWebsocketClientǁsend_json__mutmut_2, 
        'xǁWebsocketClientǁsend_json__mutmut_3': xǁWebsocketClientǁsend_json__mutmut_3, 
        'xǁWebsocketClientǁsend_json__mutmut_4': xǁWebsocketClientǁsend_json__mutmut_4, 
        'xǁWebsocketClientǁsend_json__mutmut_5': xǁWebsocketClientǁsend_json__mutmut_5, 
        'xǁWebsocketClientǁsend_json__mutmut_6': xǁWebsocketClientǁsend_json__mutmut_6, 
        'xǁWebsocketClientǁsend_json__mutmut_7': xǁWebsocketClientǁsend_json__mutmut_7, 
        'xǁWebsocketClientǁsend_json__mutmut_8': xǁWebsocketClientǁsend_json__mutmut_8
    }
    
    def send_json(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebsocketClientǁsend_json__mutmut_orig"), object.__getattribute__(self, "xǁWebsocketClientǁsend_json__mutmut_mutants"), args, kwargs, self)
        return result 
    
    send_json.__signature__ = _mutmut_signature(xǁWebsocketClientǁsend_json__mutmut_orig)
    xǁWebsocketClientǁsend_json__mutmut_orig.__name__ = 'xǁWebsocketClientǁsend_json'

    # ----

    # noinspection PyMethodMayBeStatic
    def xǁWebsocketClientǁon_open__mutmut_orig(self, wsapp: WebSocketApp) -> None:
        log.debug(f"Connected: {wsapp.url}")  # pragma: no cover

    # ----

    # noinspection PyMethodMayBeStatic
    def xǁWebsocketClientǁon_open__mutmut_1(self, wsapp: WebSocketApp) -> None:
        log.debug(None)  # pragma: no cover
    
    xǁWebsocketClientǁon_open__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebsocketClientǁon_open__mutmut_1': xǁWebsocketClientǁon_open__mutmut_1
    }
    
    def on_open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebsocketClientǁon_open__mutmut_orig"), object.__getattribute__(self, "xǁWebsocketClientǁon_open__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_open.__signature__ = _mutmut_signature(xǁWebsocketClientǁon_open__mutmut_orig)
    xǁWebsocketClientǁon_open__mutmut_orig.__name__ = 'xǁWebsocketClientǁon_open'

    # noinspection PyMethodMayBeStatic
    # noinspection PyUnusedLocal
    def xǁWebsocketClientǁon_error__mutmut_orig(self, wsapp: WebSocketApp, error: Exception) -> None:
        log.error(error)  # pragma: no cover

    # noinspection PyMethodMayBeStatic
    # noinspection PyUnusedLocal
    def xǁWebsocketClientǁon_error__mutmut_1(self, wsapp: WebSocketApp, error: Exception) -> None:
        log.error(None)  # pragma: no cover
    
    xǁWebsocketClientǁon_error__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebsocketClientǁon_error__mutmut_1': xǁWebsocketClientǁon_error__mutmut_1
    }
    
    def on_error(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebsocketClientǁon_error__mutmut_orig"), object.__getattribute__(self, "xǁWebsocketClientǁon_error__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_error.__signature__ = _mutmut_signature(xǁWebsocketClientǁon_error__mutmut_orig)
    xǁWebsocketClientǁon_error__mutmut_orig.__name__ = 'xǁWebsocketClientǁon_error'

    # noinspection PyMethodMayBeStatic
    # noinspection PyUnusedLocal
    def xǁWebsocketClientǁon_close__mutmut_orig(self, wsapp: WebSocketApp, status: int, message: str) -> None:
        log.debug(f"Closed: {wsapp.url}")  # pragma: no cover

    # noinspection PyMethodMayBeStatic
    # noinspection PyUnusedLocal
    def xǁWebsocketClientǁon_close__mutmut_1(self, wsapp: WebSocketApp, status: int, message: str) -> None:
        log.debug(None)  # pragma: no cover
    
    xǁWebsocketClientǁon_close__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁWebsocketClientǁon_close__mutmut_1': xǁWebsocketClientǁon_close__mutmut_1
    }
    
    def on_close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁWebsocketClientǁon_close__mutmut_orig"), object.__getattribute__(self, "xǁWebsocketClientǁon_close__mutmut_mutants"), args, kwargs, self)
        return result 
    
    on_close.__signature__ = _mutmut_signature(xǁWebsocketClientǁon_close__mutmut_orig)
    xǁWebsocketClientǁon_close__mutmut_orig.__name__ = 'xǁWebsocketClientǁon_close'

    def on_ping(self, wsapp: WebSocketApp, data: bytes) -> None:
        pass  # pragma: no cover

    def on_pong(self, wsapp: WebSocketApp, data: bytes) -> None:
        pass  # pragma: no cover

    def on_message(self, wsapp: WebSocketApp, data: str) -> None:
        pass  # pragma: no cover

    def on_cont_message(self, wsapp: WebSocketApp, data: bytes, cont: Any) -> None:
        pass  # pragma: no cover

    def on_data(self, wsapp: WebSocketApp, data: bytes | str, data_type: int, cont: Any) -> None:
        pass  # pragma: no cover

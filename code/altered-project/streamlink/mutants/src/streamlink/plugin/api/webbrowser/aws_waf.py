from __future__ import annotations

import logging
import time
from urllib.parse import urlparse

import trio
from requests.cookies import RequestsCookieJar

from streamlink.compat import BaseExceptionGroup
from streamlink.session import Streamlink
from streamlink.webbrowser.cdp import CDPClient, CDPClientSession, devtools


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


class AWSWAF:
    """
    Solves the AWS Web Application Firewall challenge in a locally spawned web browser.
    Headless mode is detected by AWS.
    """

    HOSTNAME = ".token.awswaf.com"
    TOKEN = "aws-waf-token"
    EXPIRATION = 3600 * 24 * 4

    def xǁAWSWAFǁ__init____mutmut_orig(self, session: Streamlink):
        self.session = session

    def xǁAWSWAFǁ__init____mutmut_1(self, session: Streamlink):
        self.session = None
    
    xǁAWSWAFǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAWSWAFǁ__init____mutmut_1': xǁAWSWAFǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAWSWAFǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁAWSWAFǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁAWSWAFǁ__init____mutmut_orig)
    xǁAWSWAFǁ__init____mutmut_orig.__name__ = 'xǁAWSWAFǁ__init__'

    def xǁAWSWAFǁacquire__mutmut_orig(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_1(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = ""
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_2(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = None
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_3(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(None)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_4(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(2)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_5(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = None

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_6(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option(None)

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_7(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("XXwebbrowser-timeoutXX")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_8(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("WEBBROWSER-TIMEOUT")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_9(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("Webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_10(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = None
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_11(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get(None, "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_12(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", None)
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_13(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_14(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", )
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_15(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("XXCookieXX", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_16(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_17(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("COOKIE", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_18(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "XXXX")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_19(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = None

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_20(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next(None, None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_21(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next(None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_22(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), )

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_23(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(None) if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_24(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.rsplit(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_25(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split("XX;XX") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_26(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(None)), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_27(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = None
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_28(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = None
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_29(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(None).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_30(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is not None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_31(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None or (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_32(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url != url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_33(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url and hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_34(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname or hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_35(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(None)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_36(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(None)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_37(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_38(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(None)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_39(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(None, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_40(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body=None)

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_41(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_42(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, )

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_43(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="XXXX")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_44(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=None) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_45(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=101) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_46(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(None, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_47(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=None)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_48(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_49(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, )
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_50(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=False)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_51(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(None):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_52(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(None) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_53(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(None)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_54(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = None
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_55(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(None, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_56(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, None)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_57(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_58(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, )
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_59(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception(None)
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_60(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("XXFailed acquiring AWS WAF tokenXX")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_61(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("failed acquiring aws waf token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_62(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("FAILED ACQUIRING AWS WAF TOKEN")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_63(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring aws waf token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_64(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(None)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_65(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_66(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error(None)
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_67(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("XXNo AWS WAF token has been acquiredXX")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_68(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("no aws waf token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_69(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("NO AWS WAF TOKEN HAS BEEN ACQUIRED")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_70(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No aws waf token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_71(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return True

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_72(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = None
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_73(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(None).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_74(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = None
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_75(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain=None,
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_76(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=None,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_77(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_78(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_79(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_80(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split(None, 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_81(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", None),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_82(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split(1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_83(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", ),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_84(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.rsplit("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_85(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("XX=XX", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_86(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 2),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_87(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="XXXX" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_88(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_89(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() - self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return True

    def xǁAWSWAFǁacquire__mutmut_90(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(None)

        return True

    def xǁAWSWAFǁacquire__mutmut_91(self, url: str) -> bool:
        send: trio.MemorySendChannel[str | None]
        receive: trio.MemoryReceiveChannel[str | None]

        data = None
        send, receive = trio.open_memory_channel(1)
        timeout = self.session.get_option("webbrowser-timeout")

        async def on_request(client_session: CDPClientSession, request: devtools.fetch.RequestPaused):
            cookies = request.request.headers.get("Cookie", "")
            cookie = next((cookie for cookie in cookies.split(";") if cookie.startswith(f"{self.TOKEN}=")), None)

            req_url = request.request.url
            hostname = urlparse(req_url).hostname
            # pass through all requests if the cookie wasn't set yet and the request URL is the initial one or an AWS one
            if cookie is None and (req_url == url or hostname and hostname.endswith(self.HOSTNAME)):
                return await client_session.continue_request(request)

            # return cookie once found
            if cookie is not None:
                await send.send(cookie)

            # block all unneeded requests
            return await client_session.fulfill_request(request, body="")

        async def acquire_token(client: CDPClient):
            client_session: CDPClientSession
            async with client.session(max_buffer_size=100) as client_session:
                client_session.add_request_handler(on_request, on_request=True)
                with trio.move_on_after(timeout):
                    async with client_session.navigate(url) as frame_id:
                        await client_session.loaded(frame_id)
                        return await receive.receive()

        try:
            data = CDPClient.launch(self.session, acquire_token)
        except BaseExceptionGroup:
            log.exception("Failed acquiring AWS WAF token")
        except Exception as err:
            log.error(err)

        if not data:
            log.error("No AWS WAF token has been acquired")
            return False

        domain = urlparse(url).hostname
        cookiejar = RequestsCookieJar()
        cookiejar.set(
            *data.split("=", 1),
            domain="" if not domain else f".{domain}",
            expires=time.time() + self.EXPIRATION,
        )
        self.session.http.cookies.update(cookiejar)

        return False
    
    xǁAWSWAFǁacquire__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAWSWAFǁacquire__mutmut_1': xǁAWSWAFǁacquire__mutmut_1, 
        'xǁAWSWAFǁacquire__mutmut_2': xǁAWSWAFǁacquire__mutmut_2, 
        'xǁAWSWAFǁacquire__mutmut_3': xǁAWSWAFǁacquire__mutmut_3, 
        'xǁAWSWAFǁacquire__mutmut_4': xǁAWSWAFǁacquire__mutmut_4, 
        'xǁAWSWAFǁacquire__mutmut_5': xǁAWSWAFǁacquire__mutmut_5, 
        'xǁAWSWAFǁacquire__mutmut_6': xǁAWSWAFǁacquire__mutmut_6, 
        'xǁAWSWAFǁacquire__mutmut_7': xǁAWSWAFǁacquire__mutmut_7, 
        'xǁAWSWAFǁacquire__mutmut_8': xǁAWSWAFǁacquire__mutmut_8, 
        'xǁAWSWAFǁacquire__mutmut_9': xǁAWSWAFǁacquire__mutmut_9, 
        'xǁAWSWAFǁacquire__mutmut_10': xǁAWSWAFǁacquire__mutmut_10, 
        'xǁAWSWAFǁacquire__mutmut_11': xǁAWSWAFǁacquire__mutmut_11, 
        'xǁAWSWAFǁacquire__mutmut_12': xǁAWSWAFǁacquire__mutmut_12, 
        'xǁAWSWAFǁacquire__mutmut_13': xǁAWSWAFǁacquire__mutmut_13, 
        'xǁAWSWAFǁacquire__mutmut_14': xǁAWSWAFǁacquire__mutmut_14, 
        'xǁAWSWAFǁacquire__mutmut_15': xǁAWSWAFǁacquire__mutmut_15, 
        'xǁAWSWAFǁacquire__mutmut_16': xǁAWSWAFǁacquire__mutmut_16, 
        'xǁAWSWAFǁacquire__mutmut_17': xǁAWSWAFǁacquire__mutmut_17, 
        'xǁAWSWAFǁacquire__mutmut_18': xǁAWSWAFǁacquire__mutmut_18, 
        'xǁAWSWAFǁacquire__mutmut_19': xǁAWSWAFǁacquire__mutmut_19, 
        'xǁAWSWAFǁacquire__mutmut_20': xǁAWSWAFǁacquire__mutmut_20, 
        'xǁAWSWAFǁacquire__mutmut_21': xǁAWSWAFǁacquire__mutmut_21, 
        'xǁAWSWAFǁacquire__mutmut_22': xǁAWSWAFǁacquire__mutmut_22, 
        'xǁAWSWAFǁacquire__mutmut_23': xǁAWSWAFǁacquire__mutmut_23, 
        'xǁAWSWAFǁacquire__mutmut_24': xǁAWSWAFǁacquire__mutmut_24, 
        'xǁAWSWAFǁacquire__mutmut_25': xǁAWSWAFǁacquire__mutmut_25, 
        'xǁAWSWAFǁacquire__mutmut_26': xǁAWSWAFǁacquire__mutmut_26, 
        'xǁAWSWAFǁacquire__mutmut_27': xǁAWSWAFǁacquire__mutmut_27, 
        'xǁAWSWAFǁacquire__mutmut_28': xǁAWSWAFǁacquire__mutmut_28, 
        'xǁAWSWAFǁacquire__mutmut_29': xǁAWSWAFǁacquire__mutmut_29, 
        'xǁAWSWAFǁacquire__mutmut_30': xǁAWSWAFǁacquire__mutmut_30, 
        'xǁAWSWAFǁacquire__mutmut_31': xǁAWSWAFǁacquire__mutmut_31, 
        'xǁAWSWAFǁacquire__mutmut_32': xǁAWSWAFǁacquire__mutmut_32, 
        'xǁAWSWAFǁacquire__mutmut_33': xǁAWSWAFǁacquire__mutmut_33, 
        'xǁAWSWAFǁacquire__mutmut_34': xǁAWSWAFǁacquire__mutmut_34, 
        'xǁAWSWAFǁacquire__mutmut_35': xǁAWSWAFǁacquire__mutmut_35, 
        'xǁAWSWAFǁacquire__mutmut_36': xǁAWSWAFǁacquire__mutmut_36, 
        'xǁAWSWAFǁacquire__mutmut_37': xǁAWSWAFǁacquire__mutmut_37, 
        'xǁAWSWAFǁacquire__mutmut_38': xǁAWSWAFǁacquire__mutmut_38, 
        'xǁAWSWAFǁacquire__mutmut_39': xǁAWSWAFǁacquire__mutmut_39, 
        'xǁAWSWAFǁacquire__mutmut_40': xǁAWSWAFǁacquire__mutmut_40, 
        'xǁAWSWAFǁacquire__mutmut_41': xǁAWSWAFǁacquire__mutmut_41, 
        'xǁAWSWAFǁacquire__mutmut_42': xǁAWSWAFǁacquire__mutmut_42, 
        'xǁAWSWAFǁacquire__mutmut_43': xǁAWSWAFǁacquire__mutmut_43, 
        'xǁAWSWAFǁacquire__mutmut_44': xǁAWSWAFǁacquire__mutmut_44, 
        'xǁAWSWAFǁacquire__mutmut_45': xǁAWSWAFǁacquire__mutmut_45, 
        'xǁAWSWAFǁacquire__mutmut_46': xǁAWSWAFǁacquire__mutmut_46, 
        'xǁAWSWAFǁacquire__mutmut_47': xǁAWSWAFǁacquire__mutmut_47, 
        'xǁAWSWAFǁacquire__mutmut_48': xǁAWSWAFǁacquire__mutmut_48, 
        'xǁAWSWAFǁacquire__mutmut_49': xǁAWSWAFǁacquire__mutmut_49, 
        'xǁAWSWAFǁacquire__mutmut_50': xǁAWSWAFǁacquire__mutmut_50, 
        'xǁAWSWAFǁacquire__mutmut_51': xǁAWSWAFǁacquire__mutmut_51, 
        'xǁAWSWAFǁacquire__mutmut_52': xǁAWSWAFǁacquire__mutmut_52, 
        'xǁAWSWAFǁacquire__mutmut_53': xǁAWSWAFǁacquire__mutmut_53, 
        'xǁAWSWAFǁacquire__mutmut_54': xǁAWSWAFǁacquire__mutmut_54, 
        'xǁAWSWAFǁacquire__mutmut_55': xǁAWSWAFǁacquire__mutmut_55, 
        'xǁAWSWAFǁacquire__mutmut_56': xǁAWSWAFǁacquire__mutmut_56, 
        'xǁAWSWAFǁacquire__mutmut_57': xǁAWSWAFǁacquire__mutmut_57, 
        'xǁAWSWAFǁacquire__mutmut_58': xǁAWSWAFǁacquire__mutmut_58, 
        'xǁAWSWAFǁacquire__mutmut_59': xǁAWSWAFǁacquire__mutmut_59, 
        'xǁAWSWAFǁacquire__mutmut_60': xǁAWSWAFǁacquire__mutmut_60, 
        'xǁAWSWAFǁacquire__mutmut_61': xǁAWSWAFǁacquire__mutmut_61, 
        'xǁAWSWAFǁacquire__mutmut_62': xǁAWSWAFǁacquire__mutmut_62, 
        'xǁAWSWAFǁacquire__mutmut_63': xǁAWSWAFǁacquire__mutmut_63, 
        'xǁAWSWAFǁacquire__mutmut_64': xǁAWSWAFǁacquire__mutmut_64, 
        'xǁAWSWAFǁacquire__mutmut_65': xǁAWSWAFǁacquire__mutmut_65, 
        'xǁAWSWAFǁacquire__mutmut_66': xǁAWSWAFǁacquire__mutmut_66, 
        'xǁAWSWAFǁacquire__mutmut_67': xǁAWSWAFǁacquire__mutmut_67, 
        'xǁAWSWAFǁacquire__mutmut_68': xǁAWSWAFǁacquire__mutmut_68, 
        'xǁAWSWAFǁacquire__mutmut_69': xǁAWSWAFǁacquire__mutmut_69, 
        'xǁAWSWAFǁacquire__mutmut_70': xǁAWSWAFǁacquire__mutmut_70, 
        'xǁAWSWAFǁacquire__mutmut_71': xǁAWSWAFǁacquire__mutmut_71, 
        'xǁAWSWAFǁacquire__mutmut_72': xǁAWSWAFǁacquire__mutmut_72, 
        'xǁAWSWAFǁacquire__mutmut_73': xǁAWSWAFǁacquire__mutmut_73, 
        'xǁAWSWAFǁacquire__mutmut_74': xǁAWSWAFǁacquire__mutmut_74, 
        'xǁAWSWAFǁacquire__mutmut_75': xǁAWSWAFǁacquire__mutmut_75, 
        'xǁAWSWAFǁacquire__mutmut_76': xǁAWSWAFǁacquire__mutmut_76, 
        'xǁAWSWAFǁacquire__mutmut_77': xǁAWSWAFǁacquire__mutmut_77, 
        'xǁAWSWAFǁacquire__mutmut_78': xǁAWSWAFǁacquire__mutmut_78, 
        'xǁAWSWAFǁacquire__mutmut_79': xǁAWSWAFǁacquire__mutmut_79, 
        'xǁAWSWAFǁacquire__mutmut_80': xǁAWSWAFǁacquire__mutmut_80, 
        'xǁAWSWAFǁacquire__mutmut_81': xǁAWSWAFǁacquire__mutmut_81, 
        'xǁAWSWAFǁacquire__mutmut_82': xǁAWSWAFǁacquire__mutmut_82, 
        'xǁAWSWAFǁacquire__mutmut_83': xǁAWSWAFǁacquire__mutmut_83, 
        'xǁAWSWAFǁacquire__mutmut_84': xǁAWSWAFǁacquire__mutmut_84, 
        'xǁAWSWAFǁacquire__mutmut_85': xǁAWSWAFǁacquire__mutmut_85, 
        'xǁAWSWAFǁacquire__mutmut_86': xǁAWSWAFǁacquire__mutmut_86, 
        'xǁAWSWAFǁacquire__mutmut_87': xǁAWSWAFǁacquire__mutmut_87, 
        'xǁAWSWAFǁacquire__mutmut_88': xǁAWSWAFǁacquire__mutmut_88, 
        'xǁAWSWAFǁacquire__mutmut_89': xǁAWSWAFǁacquire__mutmut_89, 
        'xǁAWSWAFǁacquire__mutmut_90': xǁAWSWAFǁacquire__mutmut_90, 
        'xǁAWSWAFǁacquire__mutmut_91': xǁAWSWAFǁacquire__mutmut_91
    }
    
    def acquire(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAWSWAFǁacquire__mutmut_orig"), object.__getattribute__(self, "xǁAWSWAFǁacquire__mutmut_mutants"), args, kwargs, self)
        return result 
    
    acquire.__signature__ = _mutmut_signature(xǁAWSWAFǁacquire__mutmut_orig)
    xǁAWSWAFǁacquire__mutmut_orig.__name__ = 'xǁAWSWAFǁacquire'

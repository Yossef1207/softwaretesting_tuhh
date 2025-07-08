from __future__ import annotations

import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from pathlib import Path

import trio

import streamlink.validate as validate
from streamlink.compat import is_darwin, is_win32
from streamlink.session import Streamlink
from streamlink.utils.socket import find_free_port_ipv4, find_free_port_ipv6
from streamlink.webbrowser.webbrowser import Webbrowser
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


class ChromiumWebbrowser(Webbrowser):
    ERROR_RESOLVE = "Could not find Chromium-based web browser executable"

    @classmethod
    def names(cls) -> list[str]:
        return [
            "chromium",
            "chromium-browser",
            "chrome",
            "google-chrome",
            "google-chrome-stable",
        ]

    @classmethod
    def fallback_paths(cls) -> list[str | Path]:
        if is_win32:
            ms_edge: list[str | Path] = [
                str(Path(base) / sub / "msedge.exe")
                for sub in (
                    "Microsoft\\Edge\\Application",
                    "Microsoft\\Edge Beta\\Application",
                    "Microsoft\\Edge Dev\\Application",
                )
                for base in [
                    os.getenv(env)
                    for env in (
                        "PROGRAMFILES",
                        "PROGRAMFILES(X86)",
                    )
                ]
                if base is not None
            ]
            google_chrome: list[str | Path] = [
                str(Path(base) / sub / "chrome.exe")
                for sub in (
                    "Google\\Chrome\\Application",
                    "Google\\Chrome Beta\\Application",
                    "Google\\Chrome Canary\\Application",
                )
                for base in [
                    os.getenv(env)
                    for env in (
                        "PROGRAMFILES",
                        "PROGRAMFILES(X86)",
                        "LOCALAPPDATA",
                    )
                ]
                if base is not None
            ]
            return ms_edge + google_chrome

        if is_darwin:
            return [
                "/Applications/Chromium.app/Contents/MacOS/Chromium",
                str(Path.home() / "Applications/Chromium.app/Contents/MacOS/Chromium"),
                "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                str(Path.home() / "Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
            ]

        return []

    @classmethod
    def launch_args(cls) -> list[str]:
        # https://docs.google.com/spreadsheets/d/1n-vw_PCPS45jX3Jt9jQaAhFqBY6Ge1vWF_Pa0k7dCk4
        # https://peter.sh/experiments/chromium-command-line-switches/
        return [
            # Don't auto-play videos
            "--autoplay-policy=user-gesture-required",
            # Suppress all permission prompts by automatically denying them
            "--deny-permission-prompts",
            # Disable various background network services, including
            #   extension updating, safe browsing service, upgrade detector, translate, UMA
            "--disable-background-networking",
            # Chromium treats "foreground" tabs as "backgrounded" if the surrounding window is occluded by another window
            "--disable-backgrounding-occluded-windows",
            # Disable crashdump collection (reporting is already disabled in Chromium)
            "--disable-breakpad",
            # Disables client-side phishing detection
            "--disable-client-side-phishing-detection",
            # Disable some built-in extensions that aren't affected by `--disable-extensions`
            "--disable-component-extensions-with-background-pages",
            # Don't update the browser 'components' listed at chrome://components/
            "--disable-component-update",
            # Disable installation of default apps
            "--disable-default-apps",
            # Disable all chrome extensions
            "--disable-extensions",
            # Hide toolbar button that opens dialog for controlling media sessions
            "--disable-features=GlobalMediaControls",
            # Disable the "Chrome Media Router" which creates some background network activity to discover castable targets
            "--disable-features=MediaRouter",
            # Disables Chrome translation, both the manual option and the popup prompt
            "--disable-features=Translate",
            # Suppresses hang monitor dialogs in renderer processes
            #   This flag may allow slow unload handlers on a page to prevent the tab from closing
            "--disable-hang-monitor",
            # Disables logging
            "--disable-logging",
            # Disables the Web Notification and the Push APIs
            "--disable-notifications",
            # Disable popup blocking. `--block-new-web-contents` is the strict version of this
            "--disable-popup-blocking",
            # Reloading a page that came from a POST normally prompts the user
            "--disable-prompt-on-repost",
            # Disable syncing with Google
            "--disable-sync",
            # Forces the maximum disk space to be used by the disk cache, in bytes
            "--disk-cache-size=0",
            # Disable reporting to UMA, but allows for collection
            "--metrics-recording-only",
            # Mute any audio
            "--mute-audio",
            # Disable the default browser check, do not prompt to set it as such
            "--no-default-browser-check",
            # Disables all experiments set on about:flags
            "--no-experiments",
            # Skip first run wizards
            "--no-first-run",
            # Disables the service process from adding itself as an autorun process
            #   This does not delete existing autorun registrations, it just prevents the service from registering a new one
            "--no-service-autorun",
            # Avoid potential instability of using Gnome Keyring or KDE wallet
            "--password-store=basic",
            # No initial CDP target (no empty default tab)
            "--silent-launch",
            # Use mock keychain on Mac to prevent the blocking permissions dialog asking:
            #   Do you want the application "Chromium.app" to accept incoming network connections?
            "--use-mock-keychain",
            # When not using headless mode, try to disrupt the user as little as possible
            "--window-size=0,0",
        ]

    def xǁChromiumWebbrowserǁ__init____mutmut_orig(
        self,
        *args,
        host: str | None = None,
        port: int | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.host = host or "127.0.0.1"
        self.port = port

    def xǁChromiumWebbrowserǁ__init____mutmut_1(
        self,
        *args,
        host: str | None = None,
        port: int | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.host = host or "127.0.0.1"
        self.port = port

    def xǁChromiumWebbrowserǁ__init____mutmut_2(
        self,
        *args,
        host: str | None = None,
        port: int | None = None,
        **kwargs,
    ):
        super().__init__(*args, )
        self.host = host or "127.0.0.1"
        self.port = port

    def xǁChromiumWebbrowserǁ__init____mutmut_3(
        self,
        *args,
        host: str | None = None,
        port: int | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.host = None
        self.port = port

    def xǁChromiumWebbrowserǁ__init____mutmut_4(
        self,
        *args,
        host: str | None = None,
        port: int | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.host = host and "127.0.0.1"
        self.port = port

    def xǁChromiumWebbrowserǁ__init____mutmut_5(
        self,
        *args,
        host: str | None = None,
        port: int | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.host = host or "XX127.0.0.1XX"
        self.port = port

    def xǁChromiumWebbrowserǁ__init____mutmut_6(
        self,
        *args,
        host: str | None = None,
        port: int | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.host = host or "127.0.0.1"
        self.port = None
    
    xǁChromiumWebbrowserǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁChromiumWebbrowserǁ__init____mutmut_1': xǁChromiumWebbrowserǁ__init____mutmut_1, 
        'xǁChromiumWebbrowserǁ__init____mutmut_2': xǁChromiumWebbrowserǁ__init____mutmut_2, 
        'xǁChromiumWebbrowserǁ__init____mutmut_3': xǁChromiumWebbrowserǁ__init____mutmut_3, 
        'xǁChromiumWebbrowserǁ__init____mutmut_4': xǁChromiumWebbrowserǁ__init____mutmut_4, 
        'xǁChromiumWebbrowserǁ__init____mutmut_5': xǁChromiumWebbrowserǁ__init____mutmut_5, 
        'xǁChromiumWebbrowserǁ__init____mutmut_6': xǁChromiumWebbrowserǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁChromiumWebbrowserǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁChromiumWebbrowserǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁChromiumWebbrowserǁ__init____mutmut_orig)
    xǁChromiumWebbrowserǁ__init____mutmut_orig.__name__ = 'xǁChromiumWebbrowserǁ__init__'

    @asynccontextmanager
    async def launch(self, headless: bool = False, timeout: float | None = None) -> AsyncGenerator[trio.Nursery, None]:
        if self.port is None:
            if ":" in self.host:
                self.port = await find_free_port_ipv6(self.host)
            else:
                self.port = await find_free_port_ipv4(self.host)

        # no async rmtree
        with self._create_temp_dir() as user_data_dir:
            arguments = self.arguments.copy()
            if headless:
                arguments.append("--headless=new")
            arguments.extend([
                f"--remote-debugging-host={self.host}",
                f"--remote-debugging-port={self.port}",
                f"--user-data-dir={user_data_dir}",
            ])

            async with super()._launch(self.executable, arguments, headless=headless, timeout=timeout) as nursery:
                yield nursery

            # Even though we've awaited the process termination in the async generator above,
            # the rmtree() call of the temp-dir's context manager can sometimes still fail.
            # This is probably caused by filesystem commits of the OS, not sure,
            # but we have to wait a bit in order to be able to gracefully remove the temp user data dir.
            # A terrible solution to use a static timer :(
            await trio.sleep(0.5)

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_orig(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_1(self, session: Streamlink) -> str:
        return session.http.get(
            None,
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_2(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=None,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_3(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=None,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_4(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=None,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_5(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=None,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_6(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies=None,
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_7(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=None,
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_8(self, session: Streamlink) -> str:
        return session.http.get(
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_9(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_10(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_11(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_12(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_13(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_14(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_15(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if 'XX:XX' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_16(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' not in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_17(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=11,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_18(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=1.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_19(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=1.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_20(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=1.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_21(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "XXhttpXX": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_22(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "HTTP": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_23(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "Http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_24(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "XXXX",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_25(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                None,
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_26(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                None,
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_27(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                None,
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_28(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_29(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_30(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_31(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"XXwebSocketDebuggerUrlXX": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_32(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"websocketdebuggerurl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_33(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"WEBSOCKETDEBUGGERURL": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_34(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"Websocketdebuggerurl": validate.url(scheme="ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_35(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme=None)},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_36(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="XXwsXX")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_37(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="WS")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_38(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="Ws")},
                validate.get("webSocketDebuggerUrl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_39(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get(None),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_40(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("XXwebSocketDebuggerUrlXX"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_41(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("websocketdebuggerurl"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_42(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("WEBSOCKETDEBUGGERURL"),
            ),
        )

    def xǁChromiumWebbrowserǁget_websocket_url__mutmut_43(self, session: Streamlink) -> str:
        return session.http.get(
            f"http://{f'[{self.host}]' if ':' in self.host else self.host}:{self.port}/json/version",
            retries=10,
            retry_backoff=0.25,
            retry_max_backoff=0.25,
            timeout=0.1,
            proxies={
                "http": "",
            },
            schema=validate.Schema(
                validate.parse_json(),
                {"webSocketDebuggerUrl": validate.url(scheme="ws")},
                validate.get("Websocketdebuggerurl"),
            ),
        )
    
    xǁChromiumWebbrowserǁget_websocket_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁChromiumWebbrowserǁget_websocket_url__mutmut_1': xǁChromiumWebbrowserǁget_websocket_url__mutmut_1, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_2': xǁChromiumWebbrowserǁget_websocket_url__mutmut_2, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_3': xǁChromiumWebbrowserǁget_websocket_url__mutmut_3, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_4': xǁChromiumWebbrowserǁget_websocket_url__mutmut_4, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_5': xǁChromiumWebbrowserǁget_websocket_url__mutmut_5, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_6': xǁChromiumWebbrowserǁget_websocket_url__mutmut_6, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_7': xǁChromiumWebbrowserǁget_websocket_url__mutmut_7, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_8': xǁChromiumWebbrowserǁget_websocket_url__mutmut_8, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_9': xǁChromiumWebbrowserǁget_websocket_url__mutmut_9, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_10': xǁChromiumWebbrowserǁget_websocket_url__mutmut_10, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_11': xǁChromiumWebbrowserǁget_websocket_url__mutmut_11, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_12': xǁChromiumWebbrowserǁget_websocket_url__mutmut_12, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_13': xǁChromiumWebbrowserǁget_websocket_url__mutmut_13, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_14': xǁChromiumWebbrowserǁget_websocket_url__mutmut_14, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_15': xǁChromiumWebbrowserǁget_websocket_url__mutmut_15, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_16': xǁChromiumWebbrowserǁget_websocket_url__mutmut_16, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_17': xǁChromiumWebbrowserǁget_websocket_url__mutmut_17, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_18': xǁChromiumWebbrowserǁget_websocket_url__mutmut_18, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_19': xǁChromiumWebbrowserǁget_websocket_url__mutmut_19, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_20': xǁChromiumWebbrowserǁget_websocket_url__mutmut_20, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_21': xǁChromiumWebbrowserǁget_websocket_url__mutmut_21, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_22': xǁChromiumWebbrowserǁget_websocket_url__mutmut_22, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_23': xǁChromiumWebbrowserǁget_websocket_url__mutmut_23, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_24': xǁChromiumWebbrowserǁget_websocket_url__mutmut_24, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_25': xǁChromiumWebbrowserǁget_websocket_url__mutmut_25, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_26': xǁChromiumWebbrowserǁget_websocket_url__mutmut_26, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_27': xǁChromiumWebbrowserǁget_websocket_url__mutmut_27, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_28': xǁChromiumWebbrowserǁget_websocket_url__mutmut_28, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_29': xǁChromiumWebbrowserǁget_websocket_url__mutmut_29, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_30': xǁChromiumWebbrowserǁget_websocket_url__mutmut_30, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_31': xǁChromiumWebbrowserǁget_websocket_url__mutmut_31, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_32': xǁChromiumWebbrowserǁget_websocket_url__mutmut_32, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_33': xǁChromiumWebbrowserǁget_websocket_url__mutmut_33, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_34': xǁChromiumWebbrowserǁget_websocket_url__mutmut_34, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_35': xǁChromiumWebbrowserǁget_websocket_url__mutmut_35, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_36': xǁChromiumWebbrowserǁget_websocket_url__mutmut_36, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_37': xǁChromiumWebbrowserǁget_websocket_url__mutmut_37, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_38': xǁChromiumWebbrowserǁget_websocket_url__mutmut_38, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_39': xǁChromiumWebbrowserǁget_websocket_url__mutmut_39, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_40': xǁChromiumWebbrowserǁget_websocket_url__mutmut_40, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_41': xǁChromiumWebbrowserǁget_websocket_url__mutmut_41, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_42': xǁChromiumWebbrowserǁget_websocket_url__mutmut_42, 
        'xǁChromiumWebbrowserǁget_websocket_url__mutmut_43': xǁChromiumWebbrowserǁget_websocket_url__mutmut_43
    }
    
    def get_websocket_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁChromiumWebbrowserǁget_websocket_url__mutmut_orig"), object.__getattribute__(self, "xǁChromiumWebbrowserǁget_websocket_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_websocket_url.__signature__ = _mutmut_signature(xǁChromiumWebbrowserǁget_websocket_url__mutmut_orig)
    xǁChromiumWebbrowserǁget_websocket_url__mutmut_orig.__name__ = 'xǁChromiumWebbrowserǁget_websocket_url'

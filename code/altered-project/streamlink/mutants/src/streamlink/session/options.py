from __future__ import annotations

import warnings
from collections.abc import Callable, Iterator, Mapping
from pathlib import Path
from socket import AF_INET, AF_INET6
from typing import TYPE_CHECKING, Any, ClassVar

import urllib3.util.connection as urllib3_util_connection
from requests.adapters import HTTPAdapter

from streamlink.exceptions import StreamlinkDeprecationWarning
from streamlink.options import Options
from streamlink.session.http import TLSNoDHAdapter
from streamlink.utils.url import update_scheme


if TYPE_CHECKING:
    from streamlink.session import Streamlink


_session_file = str(Path(__file__).parent / "session.py")

_original_allowed_gai_family = urllib3_util_connection.allowed_gai_family  # type: ignore[attr-defined]
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


def x__get_deprecation_stacklevel_offset__mutmut_orig():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_1():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = None
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_2():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = None
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_3():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 1
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_4():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename != _session_file and frame.f_code.co_name in ("set_option", "get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_5():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file or frame.f_code.co_name in ("set_option", "get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_6():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name not in ("set_option", "get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_7():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("XXset_optionXX", "get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_8():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("SET_OPTION", "get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_9():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("Set_option", "get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_10():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "XXget_optionXX"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_11():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "GET_OPTION"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_12():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "Get_option"):
            offset += 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_13():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "get_option"):
            offset = 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_14():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "get_option"):
            offset -= 1
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_15():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "get_option"):
            offset += 2
            break
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_16():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "get_option"):
            offset += 1
            return
        frame = frame.f_back

    return offset


def x__get_deprecation_stacklevel_offset__mutmut_17():
    """Deal with stacklevels of both session.{g,s}et_option() and session.options.{g,s}et() calls"""
    from inspect import currentframe  # noqa: PLC0415

    frame = currentframe().f_back.f_back
    offset = 0
    while frame:
        if frame.f_code.co_filename == _session_file and frame.f_code.co_name in ("set_option", "get_option"):
            offset += 1
            break
        frame = None

    return offset

x__get_deprecation_stacklevel_offset__mutmut_mutants : ClassVar[MutantDict] = {
'x__get_deprecation_stacklevel_offset__mutmut_1': x__get_deprecation_stacklevel_offset__mutmut_1, 
    'x__get_deprecation_stacklevel_offset__mutmut_2': x__get_deprecation_stacklevel_offset__mutmut_2, 
    'x__get_deprecation_stacklevel_offset__mutmut_3': x__get_deprecation_stacklevel_offset__mutmut_3, 
    'x__get_deprecation_stacklevel_offset__mutmut_4': x__get_deprecation_stacklevel_offset__mutmut_4, 
    'x__get_deprecation_stacklevel_offset__mutmut_5': x__get_deprecation_stacklevel_offset__mutmut_5, 
    'x__get_deprecation_stacklevel_offset__mutmut_6': x__get_deprecation_stacklevel_offset__mutmut_6, 
    'x__get_deprecation_stacklevel_offset__mutmut_7': x__get_deprecation_stacklevel_offset__mutmut_7, 
    'x__get_deprecation_stacklevel_offset__mutmut_8': x__get_deprecation_stacklevel_offset__mutmut_8, 
    'x__get_deprecation_stacklevel_offset__mutmut_9': x__get_deprecation_stacklevel_offset__mutmut_9, 
    'x__get_deprecation_stacklevel_offset__mutmut_10': x__get_deprecation_stacklevel_offset__mutmut_10, 
    'x__get_deprecation_stacklevel_offset__mutmut_11': x__get_deprecation_stacklevel_offset__mutmut_11, 
    'x__get_deprecation_stacklevel_offset__mutmut_12': x__get_deprecation_stacklevel_offset__mutmut_12, 
    'x__get_deprecation_stacklevel_offset__mutmut_13': x__get_deprecation_stacklevel_offset__mutmut_13, 
    'x__get_deprecation_stacklevel_offset__mutmut_14': x__get_deprecation_stacklevel_offset__mutmut_14, 
    'x__get_deprecation_stacklevel_offset__mutmut_15': x__get_deprecation_stacklevel_offset__mutmut_15, 
    'x__get_deprecation_stacklevel_offset__mutmut_16': x__get_deprecation_stacklevel_offset__mutmut_16, 
    'x__get_deprecation_stacklevel_offset__mutmut_17': x__get_deprecation_stacklevel_offset__mutmut_17
}

def _get_deprecation_stacklevel_offset(*args, **kwargs):
    result = _mutmut_trampoline(x__get_deprecation_stacklevel_offset__mutmut_orig, x__get_deprecation_stacklevel_offset__mutmut_mutants, args, kwargs)
    return result 

_get_deprecation_stacklevel_offset.__signature__ = _mutmut_signature(x__get_deprecation_stacklevel_offset__mutmut_orig)
x__get_deprecation_stacklevel_offset__mutmut_orig.__name__ = 'x__get_deprecation_stacklevel_offset'


class StreamlinkOptions(Options):
    """
    Streamlink's session options.

    The following options can be accessed using the :meth:`Streamlink.get_option() <streamlink.session.Streamlink.get_option>`
    and :meth:`Streamlink.set_option() <streamlink.session.Streamlink.set_option>` methods, as well as the regular
    :meth:`get` and :meth:`set` methods of this :class:`Options <streamlink.options.Options>` subclass.

    .. list-table::
        :header-rows: 1
        :width: 100%

        * - key
          - type
          - default
          - description
        * - user-input-requester
          - ``UserInputRequester | None``
          - ``None``
          - Instance of ``UserInputRequester`` to collect input from the user at runtime
        * - locale
          - ``str``
          - *system locale*
          - Locale setting, in the RFC 1766 format,
            e.g. ``en_US`` or ``es_ES``
        * - interface
          - ``str | None``
          - ``None``
          - Network interface address
        * - ipv4
          - ``bool``
          - ``False``
          - Resolve address names to IPv4 only, overrides ``ipv6``
        * - ipv6
          - ``bool``
          - ``False``
          - Resolve address names to IPv6 only, overrides ``ipv4``
        * - http-proxy
          - ``str | None``
          - ``None``
          - Proxy address for all HTTP/HTTPS requests
        * - https-proxy *(deprecated)*
          - ``str | None``
          - ``None``
          - Proxy address for all HTTP/HTTPS requests
        * - http-cookies
          - ``dict[str, str] | str``
          - ``{}``
          - A ``dict`` or a semicolon ``;`` delimited ``str`` of cookies to add to each HTTP/HTTPS request,
            e.g. ``foo=bar;baz=qux``
        * - http-headers
          - ``dict[str, str] | str``
          - ``{}``
          - A ``dict`` or a semicolon ``;`` delimited ``str`` of headers to add to each HTTP/HTTPS request,
            e.g. ``foo=bar;baz=qux``
        * - http-query-params
          - ``dict[str, str] | str``
          - ``{}``
          - A ``dict`` or an ampersand ``&`` delimited ``str`` of query string parameters to add to each HTTP/HTTPS request,
            e.g. ``foo=bar&baz=qux``
        * - http-trust-env
          - ``bool``
          - ``True``
          - Trust HTTP settings set in the environment,
            such as environment variables (``HTTP_PROXY``, etc.) and ``~/.netrc`` authentication
        * - http-ssl-verify
          - ``bool``
          - ``True``
          - Verify TLS/SSL certificates
        * - http-disable-dh
          - ``bool``
          - ``False``
          - Disable TLS/SSL Diffie-Hellman key exchange
        * - http-ssl-cert
          - ``str | tuple | None``
          - ``None``
          - TLS/SSL certificate to use, can be either a .pem file (``str``) or a .crt/.key pair (``tuple``)
        * - http-timeout
          - ``float``
          - ``20.0``
          - General timeout used by all HTTP/HTTPS requests, except the ones covered by other options
        * - ringbuffer-size
          - ``int``
          - ``16777216`` (16 MiB)
          - The size of the internal ring buffer used by most stream types
        * - mux-subtitles
          - ``bool``
          - ``False``
          - Make supported plugins mux available subtitles into the output stream
        * - stream-segment-attempts
          - ``int``
          - ``3``
          - Number of segment download attempts in segmented streams
        * - stream-segment-threads
          - ``int``
          - ``1``
          - The size of the thread pool used to download segments in parallel
        * - stream-segment-timeout
          - ``float``
          - ``10.0``
          - Segment connect and read timeout
        * - stream-timeout
          - ``float``
          - ``60.0``
          - Timeout for reading data from stream
        * - hls-live-edge
          - ``int``
          - ``3``
          - Number of segments from the live position of the HLS stream to start reading
        * - hls-live-restart
          - ``bool``
          - ``False``
          - Skip to the beginning of a live HLS stream, or as far back as possible
        * - hls-start-offset
          - ``float``
          - ``0.0``
          - Number of seconds to skip from the beginning of the HLS stream,
            interpreted as a negative offset for livestreams
        * - hls-duration
          - ``float | None``
          - ``None``
          - Limit the HLS stream playback duration, rounded to the nearest HLS segment
        * - hls-playlist-reload-attempts
          - ``int``
          - ``3``
          - Max number of HLS playlist reload attempts before giving up
        * - hls-playlist-reload-time
          - ``str | float``
          - ``"default"``
          - Override the HLS playlist reload time, either in seconds (``float``) or as a ``str`` keyword:

            - ``segment``: duration of the last segment
            - ``live-edge``: sum of segment durations of the ``hls-live-edge`` value minus one
            - ``default``: the playlist's target duration
        * - hls-segment-queue-threshold
          - ``float``
          - ``3``
          - Factor of the playlist's targetduration which sets the threshold for stopping early on missing segments
        * - hls-segment-stream-data
          - ``bool``
          - ``False``
          - Stream data of HLS segment downloads to the output instead of waiting for the full response
        * - hls-segment-ignore-names
          - ``List[str]``
          - ``[]``
          - List of HLS segment names without file endings which should get filtered out
        * - hls-segment-key-uri
          - ``str | None``
          - ``None``
          - Override the address of the encrypted HLS stream's key,
            with support for the following string template variables:
            ``{url}``, ``{scheme}``, ``{netloc}``, ``{path}``, ``{query}``
        * - hls-audio-select
          - ``List[str]``
          - ``[]``
          - Select a specific audio source or sources when multiple audio sources are available,
            by language code or name, or ``"*"`` (asterisk)
        * - dash-manifest-reload-attempts
          - ``int``
          - ``3``
          - Max number of DASH manifest reload attempts before giving up
        * - ffmpeg-ffmpeg
          - ``str | None``
          - ``None``
          - Override for the ``ffmpeg``/``ffmpeg.exe`` binary path,
            which by default gets looked up via the ``PATH`` env var
        * - ffmpeg-no-validation
          - ``bool``
          - ``False``
          - Disable FFmpeg validation and version logging
        * - ffmpeg-verbose
          - ``bool``
          - ``False``
          - Append FFmpeg's stderr stream to the Python's stderr stream
        * - ffmpeg-verbose-path
          - ``str | None``
          - ``None``
          - Write FFmpeg's stderr stream to the filesystem at the specified path
        * - ffmpeg-loglevel
          - ``str | None``
          - ``None``
          - Set FFmpeg's ``-loglevel`` value
        * - ffmpeg-fout
          - ``str | None``
          - ``None``
          - Set the output format of muxed streams, e.g. ``"matroska"``
        * - ffmpeg-video-transcode
          - ``str | None``
          - ``None``
          - The codec to use if transcoding video when muxing streams, e.g. ``"h264"``
        * - ffmpeg-audio-transcode
          - ``str | None``
          - ``None``
          - The codec to use if transcoding video when muxing streams, e.g. ``"aac"``
        * - ffmpeg-copyts
          - ``bool``
          - ``False``
          - Don't shift input stream timestamps when muxing streams
        * - ffmpeg-start-at-zero
          - ``bool``
          - ``False``
          - When ``ffmpeg-copyts`` is ``True``, shift timestamps to zero
        * - webbrowser
          - ``bool``
          - ``True``
          - Enable or disable support for Streamlink's webbrowser API
        * - webbrowser-executable
          - ``str | None``
          - ``None``
          - Path to the web browser's executable
        * - webbrowser-timeout
          - ``float``
          - ``20.0``
          - The maximum amount of time which the webbrowser can take to launch and execute
        * - webbrowser-cdp-host
          - ``str | None``
          - ``None``
          - Custom host for the Chrome Devtools Protocol (CDP) interface
        * - webbrowser-cdp-port
          - ``int | None``
          - ``None``
          - Custom port for the Chrome Devtools Protocol (CDP) interface
        * - webbrowser-cdp-timeout
          - ``float``
          - ``2.0``
          - The maximum amount of time for waiting on a single CDP command response
        * - webbrowser-headless
          - ``bool``
          - ``False``
          - Whether to launch the webbrowser in headless mode or not
    """

    def xǁStreamlinkOptionsǁ__init____mutmut_orig(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_1(self, session: Streamlink) -> None:
        super().__init__(None)
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_2(self, session: Streamlink) -> None:
        super().__init__({
            "XXuser-input-requesterXX": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_3(self, session: Streamlink) -> None:
        super().__init__({
            "USER-INPUT-REQUESTER": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_4(self, session: Streamlink) -> None:
        super().__init__({
            "User-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_5(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "XXlocaleXX": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_6(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "LOCALE": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_7(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "Locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_8(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "XXinterfaceXX": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_9(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "INTERFACE": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_10(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "Interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_11(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "XXipv4XX": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_12(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "IPV4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_13(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "Ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_14(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": True,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_15(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "XXipv6XX": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_16(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "IPV6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_17(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "Ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_18(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": True,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_19(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "XXringbuffer-sizeXX": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_20(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "RINGBUFFER-SIZE": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_21(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "Ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_22(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1025 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_23(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 / 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_24(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1025 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_25(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 / 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_26(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 17,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_27(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "XXmux-subtitlesXX": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_28(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "MUX-SUBTITLES": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_29(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "Mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_30(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": True,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_31(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "XXstream-segment-attemptsXX": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_32(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "STREAM-SEGMENT-ATTEMPTS": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_33(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "Stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_34(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 4,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_35(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "XXstream-segment-threadsXX": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_36(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "STREAM-SEGMENT-THREADS": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_37(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "Stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_38(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 2,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_39(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "XXstream-segment-timeoutXX": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_40(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "STREAM-SEGMENT-TIMEOUT": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_41(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "Stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_42(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 11.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_43(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "XXstream-timeoutXX": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_44(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "STREAM-TIMEOUT": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_45(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "Stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_46(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 61.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_47(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "XXhls-live-edgeXX": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_48(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "HLS-LIVE-EDGE": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_49(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "Hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_50(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 4,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_51(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "XXhls-live-restartXX": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_52(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "HLS-LIVE-RESTART": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_53(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "Hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_54(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": True,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_55(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "XXhls-start-offsetXX": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_56(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "HLS-START-OFFSET": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_57(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "Hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_58(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 1.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_59(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "XXhls-durationXX": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_60(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "HLS-DURATION": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_61(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "Hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_62(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "XXhls-playlist-reload-attemptsXX": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_63(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "HLS-PLAYLIST-RELOAD-ATTEMPTS": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_64(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "Hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_65(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 4,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_66(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "XXhls-playlist-reload-timeXX": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_67(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "HLS-PLAYLIST-RELOAD-TIME": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_68(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "Hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_69(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "XXdefaultXX",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_70(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "DEFAULT",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_71(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "Default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_72(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "XXhls-segment-queue-thresholdXX": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_73(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "HLS-SEGMENT-QUEUE-THRESHOLD": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_74(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "Hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_75(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 4,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_76(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "XXhls-segment-stream-dataXX": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_77(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "HLS-SEGMENT-STREAM-DATA": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_78(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "Hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_79(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": True,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_80(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "XXhls-segment-ignore-namesXX": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_81(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "HLS-SEGMENT-IGNORE-NAMES": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_82(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "Hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_83(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "XXhls-segment-key-uriXX": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_84(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "HLS-SEGMENT-KEY-URI": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_85(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "Hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_86(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "XXhls-audio-selectXX": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_87(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "HLS-AUDIO-SELECT": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_88(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "Hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_89(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "XXdash-manifest-reload-attemptsXX": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_90(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "DASH-MANIFEST-RELOAD-ATTEMPTS": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_91(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "Dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_92(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 4,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_93(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "XXffmpeg-ffmpegXX": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_94(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "FFMPEG-FFMPEG": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_95(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "Ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_96(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "XXffmpeg-no-validationXX": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_97(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "FFMPEG-NO-VALIDATION": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_98(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "Ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_99(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": True,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_100(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "XXffmpeg-verboseXX": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_101(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "FFMPEG-VERBOSE": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_102(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "Ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_103(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": True,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_104(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "XXffmpeg-verbose-pathXX": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_105(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "FFMPEG-VERBOSE-PATH": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_106(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "Ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_107(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "XXffmpeg-loglevelXX": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_108(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "FFMPEG-LOGLEVEL": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_109(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "Ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_110(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "XXffmpeg-foutXX": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_111(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "FFMPEG-FOUT": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_112(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "Ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_113(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "XXffmpeg-video-transcodeXX": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_114(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "FFMPEG-VIDEO-TRANSCODE": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_115(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "Ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_116(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "XXffmpeg-audio-transcodeXX": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_117(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "FFMPEG-AUDIO-TRANSCODE": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_118(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "Ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_119(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "XXffmpeg-copytsXX": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_120(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "FFMPEG-COPYTS": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_121(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "Ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_122(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": True,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_123(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "XXffmpeg-start-at-zeroXX": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_124(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "FFMPEG-START-AT-ZERO": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_125(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "Ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_126(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": True,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_127(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "XXwebbrowserXX": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_128(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "WEBBROWSER": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_129(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "Webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_130(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": False,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_131(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "XXwebbrowser-executableXX": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_132(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "WEBBROWSER-EXECUTABLE": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_133(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "Webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_134(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "XXwebbrowser-timeoutXX": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_135(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "WEBBROWSER-TIMEOUT": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_136(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "Webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_137(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 21.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_138(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "XXwebbrowser-cdp-hostXX": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_139(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "WEBBROWSER-CDP-HOST": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_140(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "Webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_141(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "XXwebbrowser-cdp-portXX": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_142(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "WEBBROWSER-CDP-PORT": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_143(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "Webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_144(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "XXwebbrowser-cdp-timeoutXX": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_145(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "WEBBROWSER-CDP-TIMEOUT": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_146(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "Webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_147(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 3.0,
            "webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_148(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "XXwebbrowser-headlessXX": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_149(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "WEBBROWSER-HEADLESS": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_150(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "Webbrowser-headless": False,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_151(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": True,
        })
        self.session = session

    def xǁStreamlinkOptionsǁ__init____mutmut_152(self, session: Streamlink) -> None:
        super().__init__({
            "user-input-requester": None,
            "locale": None,
            "interface": None,
            "ipv4": False,
            "ipv6": False,
            "ringbuffer-size": 1024 * 1024 * 16,  # 16 MB
            "mux-subtitles": False,
            "stream-segment-attempts": 3,
            "stream-segment-threads": 1,
            "stream-segment-timeout": 10.0,
            "stream-timeout": 60.0,
            "hls-live-edge": 3,
            "hls-live-restart": False,
            "hls-start-offset": 0.0,
            "hls-duration": None,
            "hls-playlist-reload-attempts": 3,
            "hls-playlist-reload-time": "default",
            "hls-segment-queue-threshold": 3,
            "hls-segment-stream-data": False,
            "hls-segment-ignore-names": [],
            "hls-segment-key-uri": None,
            "hls-audio-select": [],
            "dash-manifest-reload-attempts": 3,
            "ffmpeg-ffmpeg": None,
            "ffmpeg-no-validation": False,
            "ffmpeg-verbose": False,
            "ffmpeg-verbose-path": None,
            "ffmpeg-loglevel": None,
            "ffmpeg-fout": None,
            "ffmpeg-video-transcode": None,
            "ffmpeg-audio-transcode": None,
            "ffmpeg-copyts": False,
            "ffmpeg-start-at-zero": False,
            "webbrowser": True,
            "webbrowser-executable": None,
            "webbrowser-timeout": 20.0,
            "webbrowser-cdp-host": None,
            "webbrowser-cdp-port": None,
            "webbrowser-cdp-timeout": 2.0,
            "webbrowser-headless": False,
        })
        self.session = None
    
    xǁStreamlinkOptionsǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkOptionsǁ__init____mutmut_1': xǁStreamlinkOptionsǁ__init____mutmut_1, 
        'xǁStreamlinkOptionsǁ__init____mutmut_2': xǁStreamlinkOptionsǁ__init____mutmut_2, 
        'xǁStreamlinkOptionsǁ__init____mutmut_3': xǁStreamlinkOptionsǁ__init____mutmut_3, 
        'xǁStreamlinkOptionsǁ__init____mutmut_4': xǁStreamlinkOptionsǁ__init____mutmut_4, 
        'xǁStreamlinkOptionsǁ__init____mutmut_5': xǁStreamlinkOptionsǁ__init____mutmut_5, 
        'xǁStreamlinkOptionsǁ__init____mutmut_6': xǁStreamlinkOptionsǁ__init____mutmut_6, 
        'xǁStreamlinkOptionsǁ__init____mutmut_7': xǁStreamlinkOptionsǁ__init____mutmut_7, 
        'xǁStreamlinkOptionsǁ__init____mutmut_8': xǁStreamlinkOptionsǁ__init____mutmut_8, 
        'xǁStreamlinkOptionsǁ__init____mutmut_9': xǁStreamlinkOptionsǁ__init____mutmut_9, 
        'xǁStreamlinkOptionsǁ__init____mutmut_10': xǁStreamlinkOptionsǁ__init____mutmut_10, 
        'xǁStreamlinkOptionsǁ__init____mutmut_11': xǁStreamlinkOptionsǁ__init____mutmut_11, 
        'xǁStreamlinkOptionsǁ__init____mutmut_12': xǁStreamlinkOptionsǁ__init____mutmut_12, 
        'xǁStreamlinkOptionsǁ__init____mutmut_13': xǁStreamlinkOptionsǁ__init____mutmut_13, 
        'xǁStreamlinkOptionsǁ__init____mutmut_14': xǁStreamlinkOptionsǁ__init____mutmut_14, 
        'xǁStreamlinkOptionsǁ__init____mutmut_15': xǁStreamlinkOptionsǁ__init____mutmut_15, 
        'xǁStreamlinkOptionsǁ__init____mutmut_16': xǁStreamlinkOptionsǁ__init____mutmut_16, 
        'xǁStreamlinkOptionsǁ__init____mutmut_17': xǁStreamlinkOptionsǁ__init____mutmut_17, 
        'xǁStreamlinkOptionsǁ__init____mutmut_18': xǁStreamlinkOptionsǁ__init____mutmut_18, 
        'xǁStreamlinkOptionsǁ__init____mutmut_19': xǁStreamlinkOptionsǁ__init____mutmut_19, 
        'xǁStreamlinkOptionsǁ__init____mutmut_20': xǁStreamlinkOptionsǁ__init____mutmut_20, 
        'xǁStreamlinkOptionsǁ__init____mutmut_21': xǁStreamlinkOptionsǁ__init____mutmut_21, 
        'xǁStreamlinkOptionsǁ__init____mutmut_22': xǁStreamlinkOptionsǁ__init____mutmut_22, 
        'xǁStreamlinkOptionsǁ__init____mutmut_23': xǁStreamlinkOptionsǁ__init____mutmut_23, 
        'xǁStreamlinkOptionsǁ__init____mutmut_24': xǁStreamlinkOptionsǁ__init____mutmut_24, 
        'xǁStreamlinkOptionsǁ__init____mutmut_25': xǁStreamlinkOptionsǁ__init____mutmut_25, 
        'xǁStreamlinkOptionsǁ__init____mutmut_26': xǁStreamlinkOptionsǁ__init____mutmut_26, 
        'xǁStreamlinkOptionsǁ__init____mutmut_27': xǁStreamlinkOptionsǁ__init____mutmut_27, 
        'xǁStreamlinkOptionsǁ__init____mutmut_28': xǁStreamlinkOptionsǁ__init____mutmut_28, 
        'xǁStreamlinkOptionsǁ__init____mutmut_29': xǁStreamlinkOptionsǁ__init____mutmut_29, 
        'xǁStreamlinkOptionsǁ__init____mutmut_30': xǁStreamlinkOptionsǁ__init____mutmut_30, 
        'xǁStreamlinkOptionsǁ__init____mutmut_31': xǁStreamlinkOptionsǁ__init____mutmut_31, 
        'xǁStreamlinkOptionsǁ__init____mutmut_32': xǁStreamlinkOptionsǁ__init____mutmut_32, 
        'xǁStreamlinkOptionsǁ__init____mutmut_33': xǁStreamlinkOptionsǁ__init____mutmut_33, 
        'xǁStreamlinkOptionsǁ__init____mutmut_34': xǁStreamlinkOptionsǁ__init____mutmut_34, 
        'xǁStreamlinkOptionsǁ__init____mutmut_35': xǁStreamlinkOptionsǁ__init____mutmut_35, 
        'xǁStreamlinkOptionsǁ__init____mutmut_36': xǁStreamlinkOptionsǁ__init____mutmut_36, 
        'xǁStreamlinkOptionsǁ__init____mutmut_37': xǁStreamlinkOptionsǁ__init____mutmut_37, 
        'xǁStreamlinkOptionsǁ__init____mutmut_38': xǁStreamlinkOptionsǁ__init____mutmut_38, 
        'xǁStreamlinkOptionsǁ__init____mutmut_39': xǁStreamlinkOptionsǁ__init____mutmut_39, 
        'xǁStreamlinkOptionsǁ__init____mutmut_40': xǁStreamlinkOptionsǁ__init____mutmut_40, 
        'xǁStreamlinkOptionsǁ__init____mutmut_41': xǁStreamlinkOptionsǁ__init____mutmut_41, 
        'xǁStreamlinkOptionsǁ__init____mutmut_42': xǁStreamlinkOptionsǁ__init____mutmut_42, 
        'xǁStreamlinkOptionsǁ__init____mutmut_43': xǁStreamlinkOptionsǁ__init____mutmut_43, 
        'xǁStreamlinkOptionsǁ__init____mutmut_44': xǁStreamlinkOptionsǁ__init____mutmut_44, 
        'xǁStreamlinkOptionsǁ__init____mutmut_45': xǁStreamlinkOptionsǁ__init____mutmut_45, 
        'xǁStreamlinkOptionsǁ__init____mutmut_46': xǁStreamlinkOptionsǁ__init____mutmut_46, 
        'xǁStreamlinkOptionsǁ__init____mutmut_47': xǁStreamlinkOptionsǁ__init____mutmut_47, 
        'xǁStreamlinkOptionsǁ__init____mutmut_48': xǁStreamlinkOptionsǁ__init____mutmut_48, 
        'xǁStreamlinkOptionsǁ__init____mutmut_49': xǁStreamlinkOptionsǁ__init____mutmut_49, 
        'xǁStreamlinkOptionsǁ__init____mutmut_50': xǁStreamlinkOptionsǁ__init____mutmut_50, 
        'xǁStreamlinkOptionsǁ__init____mutmut_51': xǁStreamlinkOptionsǁ__init____mutmut_51, 
        'xǁStreamlinkOptionsǁ__init____mutmut_52': xǁStreamlinkOptionsǁ__init____mutmut_52, 
        'xǁStreamlinkOptionsǁ__init____mutmut_53': xǁStreamlinkOptionsǁ__init____mutmut_53, 
        'xǁStreamlinkOptionsǁ__init____mutmut_54': xǁStreamlinkOptionsǁ__init____mutmut_54, 
        'xǁStreamlinkOptionsǁ__init____mutmut_55': xǁStreamlinkOptionsǁ__init____mutmut_55, 
        'xǁStreamlinkOptionsǁ__init____mutmut_56': xǁStreamlinkOptionsǁ__init____mutmut_56, 
        'xǁStreamlinkOptionsǁ__init____mutmut_57': xǁStreamlinkOptionsǁ__init____mutmut_57, 
        'xǁStreamlinkOptionsǁ__init____mutmut_58': xǁStreamlinkOptionsǁ__init____mutmut_58, 
        'xǁStreamlinkOptionsǁ__init____mutmut_59': xǁStreamlinkOptionsǁ__init____mutmut_59, 
        'xǁStreamlinkOptionsǁ__init____mutmut_60': xǁStreamlinkOptionsǁ__init____mutmut_60, 
        'xǁStreamlinkOptionsǁ__init____mutmut_61': xǁStreamlinkOptionsǁ__init____mutmut_61, 
        'xǁStreamlinkOptionsǁ__init____mutmut_62': xǁStreamlinkOptionsǁ__init____mutmut_62, 
        'xǁStreamlinkOptionsǁ__init____mutmut_63': xǁStreamlinkOptionsǁ__init____mutmut_63, 
        'xǁStreamlinkOptionsǁ__init____mutmut_64': xǁStreamlinkOptionsǁ__init____mutmut_64, 
        'xǁStreamlinkOptionsǁ__init____mutmut_65': xǁStreamlinkOptionsǁ__init____mutmut_65, 
        'xǁStreamlinkOptionsǁ__init____mutmut_66': xǁStreamlinkOptionsǁ__init____mutmut_66, 
        'xǁStreamlinkOptionsǁ__init____mutmut_67': xǁStreamlinkOptionsǁ__init____mutmut_67, 
        'xǁStreamlinkOptionsǁ__init____mutmut_68': xǁStreamlinkOptionsǁ__init____mutmut_68, 
        'xǁStreamlinkOptionsǁ__init____mutmut_69': xǁStreamlinkOptionsǁ__init____mutmut_69, 
        'xǁStreamlinkOptionsǁ__init____mutmut_70': xǁStreamlinkOptionsǁ__init____mutmut_70, 
        'xǁStreamlinkOptionsǁ__init____mutmut_71': xǁStreamlinkOptionsǁ__init____mutmut_71, 
        'xǁStreamlinkOptionsǁ__init____mutmut_72': xǁStreamlinkOptionsǁ__init____mutmut_72, 
        'xǁStreamlinkOptionsǁ__init____mutmut_73': xǁStreamlinkOptionsǁ__init____mutmut_73, 
        'xǁStreamlinkOptionsǁ__init____mutmut_74': xǁStreamlinkOptionsǁ__init____mutmut_74, 
        'xǁStreamlinkOptionsǁ__init____mutmut_75': xǁStreamlinkOptionsǁ__init____mutmut_75, 
        'xǁStreamlinkOptionsǁ__init____mutmut_76': xǁStreamlinkOptionsǁ__init____mutmut_76, 
        'xǁStreamlinkOptionsǁ__init____mutmut_77': xǁStreamlinkOptionsǁ__init____mutmut_77, 
        'xǁStreamlinkOptionsǁ__init____mutmut_78': xǁStreamlinkOptionsǁ__init____mutmut_78, 
        'xǁStreamlinkOptionsǁ__init____mutmut_79': xǁStreamlinkOptionsǁ__init____mutmut_79, 
        'xǁStreamlinkOptionsǁ__init____mutmut_80': xǁStreamlinkOptionsǁ__init____mutmut_80, 
        'xǁStreamlinkOptionsǁ__init____mutmut_81': xǁStreamlinkOptionsǁ__init____mutmut_81, 
        'xǁStreamlinkOptionsǁ__init____mutmut_82': xǁStreamlinkOptionsǁ__init____mutmut_82, 
        'xǁStreamlinkOptionsǁ__init____mutmut_83': xǁStreamlinkOptionsǁ__init____mutmut_83, 
        'xǁStreamlinkOptionsǁ__init____mutmut_84': xǁStreamlinkOptionsǁ__init____mutmut_84, 
        'xǁStreamlinkOptionsǁ__init____mutmut_85': xǁStreamlinkOptionsǁ__init____mutmut_85, 
        'xǁStreamlinkOptionsǁ__init____mutmut_86': xǁStreamlinkOptionsǁ__init____mutmut_86, 
        'xǁStreamlinkOptionsǁ__init____mutmut_87': xǁStreamlinkOptionsǁ__init____mutmut_87, 
        'xǁStreamlinkOptionsǁ__init____mutmut_88': xǁStreamlinkOptionsǁ__init____mutmut_88, 
        'xǁStreamlinkOptionsǁ__init____mutmut_89': xǁStreamlinkOptionsǁ__init____mutmut_89, 
        'xǁStreamlinkOptionsǁ__init____mutmut_90': xǁStreamlinkOptionsǁ__init____mutmut_90, 
        'xǁStreamlinkOptionsǁ__init____mutmut_91': xǁStreamlinkOptionsǁ__init____mutmut_91, 
        'xǁStreamlinkOptionsǁ__init____mutmut_92': xǁStreamlinkOptionsǁ__init____mutmut_92, 
        'xǁStreamlinkOptionsǁ__init____mutmut_93': xǁStreamlinkOptionsǁ__init____mutmut_93, 
        'xǁStreamlinkOptionsǁ__init____mutmut_94': xǁStreamlinkOptionsǁ__init____mutmut_94, 
        'xǁStreamlinkOptionsǁ__init____mutmut_95': xǁStreamlinkOptionsǁ__init____mutmut_95, 
        'xǁStreamlinkOptionsǁ__init____mutmut_96': xǁStreamlinkOptionsǁ__init____mutmut_96, 
        'xǁStreamlinkOptionsǁ__init____mutmut_97': xǁStreamlinkOptionsǁ__init____mutmut_97, 
        'xǁStreamlinkOptionsǁ__init____mutmut_98': xǁStreamlinkOptionsǁ__init____mutmut_98, 
        'xǁStreamlinkOptionsǁ__init____mutmut_99': xǁStreamlinkOptionsǁ__init____mutmut_99, 
        'xǁStreamlinkOptionsǁ__init____mutmut_100': xǁStreamlinkOptionsǁ__init____mutmut_100, 
        'xǁStreamlinkOptionsǁ__init____mutmut_101': xǁStreamlinkOptionsǁ__init____mutmut_101, 
        'xǁStreamlinkOptionsǁ__init____mutmut_102': xǁStreamlinkOptionsǁ__init____mutmut_102, 
        'xǁStreamlinkOptionsǁ__init____mutmut_103': xǁStreamlinkOptionsǁ__init____mutmut_103, 
        'xǁStreamlinkOptionsǁ__init____mutmut_104': xǁStreamlinkOptionsǁ__init____mutmut_104, 
        'xǁStreamlinkOptionsǁ__init____mutmut_105': xǁStreamlinkOptionsǁ__init____mutmut_105, 
        'xǁStreamlinkOptionsǁ__init____mutmut_106': xǁStreamlinkOptionsǁ__init____mutmut_106, 
        'xǁStreamlinkOptionsǁ__init____mutmut_107': xǁStreamlinkOptionsǁ__init____mutmut_107, 
        'xǁStreamlinkOptionsǁ__init____mutmut_108': xǁStreamlinkOptionsǁ__init____mutmut_108, 
        'xǁStreamlinkOptionsǁ__init____mutmut_109': xǁStreamlinkOptionsǁ__init____mutmut_109, 
        'xǁStreamlinkOptionsǁ__init____mutmut_110': xǁStreamlinkOptionsǁ__init____mutmut_110, 
        'xǁStreamlinkOptionsǁ__init____mutmut_111': xǁStreamlinkOptionsǁ__init____mutmut_111, 
        'xǁStreamlinkOptionsǁ__init____mutmut_112': xǁStreamlinkOptionsǁ__init____mutmut_112, 
        'xǁStreamlinkOptionsǁ__init____mutmut_113': xǁStreamlinkOptionsǁ__init____mutmut_113, 
        'xǁStreamlinkOptionsǁ__init____mutmut_114': xǁStreamlinkOptionsǁ__init____mutmut_114, 
        'xǁStreamlinkOptionsǁ__init____mutmut_115': xǁStreamlinkOptionsǁ__init____mutmut_115, 
        'xǁStreamlinkOptionsǁ__init____mutmut_116': xǁStreamlinkOptionsǁ__init____mutmut_116, 
        'xǁStreamlinkOptionsǁ__init____mutmut_117': xǁStreamlinkOptionsǁ__init____mutmut_117, 
        'xǁStreamlinkOptionsǁ__init____mutmut_118': xǁStreamlinkOptionsǁ__init____mutmut_118, 
        'xǁStreamlinkOptionsǁ__init____mutmut_119': xǁStreamlinkOptionsǁ__init____mutmut_119, 
        'xǁStreamlinkOptionsǁ__init____mutmut_120': xǁStreamlinkOptionsǁ__init____mutmut_120, 
        'xǁStreamlinkOptionsǁ__init____mutmut_121': xǁStreamlinkOptionsǁ__init____mutmut_121, 
        'xǁStreamlinkOptionsǁ__init____mutmut_122': xǁStreamlinkOptionsǁ__init____mutmut_122, 
        'xǁStreamlinkOptionsǁ__init____mutmut_123': xǁStreamlinkOptionsǁ__init____mutmut_123, 
        'xǁStreamlinkOptionsǁ__init____mutmut_124': xǁStreamlinkOptionsǁ__init____mutmut_124, 
        'xǁStreamlinkOptionsǁ__init____mutmut_125': xǁStreamlinkOptionsǁ__init____mutmut_125, 
        'xǁStreamlinkOptionsǁ__init____mutmut_126': xǁStreamlinkOptionsǁ__init____mutmut_126, 
        'xǁStreamlinkOptionsǁ__init____mutmut_127': xǁStreamlinkOptionsǁ__init____mutmut_127, 
        'xǁStreamlinkOptionsǁ__init____mutmut_128': xǁStreamlinkOptionsǁ__init____mutmut_128, 
        'xǁStreamlinkOptionsǁ__init____mutmut_129': xǁStreamlinkOptionsǁ__init____mutmut_129, 
        'xǁStreamlinkOptionsǁ__init____mutmut_130': xǁStreamlinkOptionsǁ__init____mutmut_130, 
        'xǁStreamlinkOptionsǁ__init____mutmut_131': xǁStreamlinkOptionsǁ__init____mutmut_131, 
        'xǁStreamlinkOptionsǁ__init____mutmut_132': xǁStreamlinkOptionsǁ__init____mutmut_132, 
        'xǁStreamlinkOptionsǁ__init____mutmut_133': xǁStreamlinkOptionsǁ__init____mutmut_133, 
        'xǁStreamlinkOptionsǁ__init____mutmut_134': xǁStreamlinkOptionsǁ__init____mutmut_134, 
        'xǁStreamlinkOptionsǁ__init____mutmut_135': xǁStreamlinkOptionsǁ__init____mutmut_135, 
        'xǁStreamlinkOptionsǁ__init____mutmut_136': xǁStreamlinkOptionsǁ__init____mutmut_136, 
        'xǁStreamlinkOptionsǁ__init____mutmut_137': xǁStreamlinkOptionsǁ__init____mutmut_137, 
        'xǁStreamlinkOptionsǁ__init____mutmut_138': xǁStreamlinkOptionsǁ__init____mutmut_138, 
        'xǁStreamlinkOptionsǁ__init____mutmut_139': xǁStreamlinkOptionsǁ__init____mutmut_139, 
        'xǁStreamlinkOptionsǁ__init____mutmut_140': xǁStreamlinkOptionsǁ__init____mutmut_140, 
        'xǁStreamlinkOptionsǁ__init____mutmut_141': xǁStreamlinkOptionsǁ__init____mutmut_141, 
        'xǁStreamlinkOptionsǁ__init____mutmut_142': xǁStreamlinkOptionsǁ__init____mutmut_142, 
        'xǁStreamlinkOptionsǁ__init____mutmut_143': xǁStreamlinkOptionsǁ__init____mutmut_143, 
        'xǁStreamlinkOptionsǁ__init____mutmut_144': xǁStreamlinkOptionsǁ__init____mutmut_144, 
        'xǁStreamlinkOptionsǁ__init____mutmut_145': xǁStreamlinkOptionsǁ__init____mutmut_145, 
        'xǁStreamlinkOptionsǁ__init____mutmut_146': xǁStreamlinkOptionsǁ__init____mutmut_146, 
        'xǁStreamlinkOptionsǁ__init____mutmut_147': xǁStreamlinkOptionsǁ__init____mutmut_147, 
        'xǁStreamlinkOptionsǁ__init____mutmut_148': xǁStreamlinkOptionsǁ__init____mutmut_148, 
        'xǁStreamlinkOptionsǁ__init____mutmut_149': xǁStreamlinkOptionsǁ__init____mutmut_149, 
        'xǁStreamlinkOptionsǁ__init____mutmut_150': xǁStreamlinkOptionsǁ__init____mutmut_150, 
        'xǁStreamlinkOptionsǁ__init____mutmut_151': xǁStreamlinkOptionsǁ__init____mutmut_151, 
        'xǁStreamlinkOptionsǁ__init____mutmut_152': xǁStreamlinkOptionsǁ__init____mutmut_152
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkOptionsǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkOptionsǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStreamlinkOptionsǁ__init____mutmut_orig)
    xǁStreamlinkOptionsǁ__init____mutmut_orig.__name__ = 'xǁStreamlinkOptionsǁ__init__'

    # ---- utils

    @staticmethod
    def _parse_key_equals_value_string(delimiter: str, value: str) -> Iterator[tuple[str, str]]:
        for keyval in value.split(delimiter):
            try:
                key, val = keyval.split("=", 1)
                yield key.strip(), val.strip()
            except ValueError:
                continue

    @staticmethod
    def _deprecate_https_proxy(key: str) -> None:
        if key == "https-proxy":
            warnings.warn(
                "The `https-proxy` option has been deprecated in favor of a single `http-proxy` option",
                StreamlinkDeprecationWarning,
                stacklevel=4 + _get_deprecation_stacklevel_offset(),
            )

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_orig(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("https" if key == "https-proxy" else "http")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_1(self, key):
        self._deprecate_https_proxy(None)
        return self.session.http.proxies.get("https" if key == "https-proxy" else "http")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_2(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get(None)

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_3(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("XXhttpsXX" if key == "https-proxy" else "http")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_4(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("HTTPS" if key == "https-proxy" else "http")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_5(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("Https" if key == "https-proxy" else "http")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_6(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("https" if key != "https-proxy" else "http")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_7(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("https" if key == "XXhttps-proxyXX" else "http")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_8(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("https" if key == "HTTPS-PROXY" else "http")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_9(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("https" if key == "Https-proxy" else "http")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_10(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("https" if key == "https-proxy" else "XXhttpXX")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_11(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("https" if key == "https-proxy" else "HTTP")

    # ---- getters

    def xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_12(self, key):
        self._deprecate_https_proxy(key)
        return self.session.http.proxies.get("https" if key == "https-proxy" else "Http")
    
    xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_1': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_1, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_2': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_2, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_3': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_3, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_4': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_4, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_5': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_5, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_6': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_6, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_7': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_7, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_8': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_8, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_9': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_9, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_10': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_10, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_11': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_11, 
        'xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_12': xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_12
    }
    
    def _get_http_proxy(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_http_proxy.__signature__ = _mutmut_signature(xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_orig)
    xǁStreamlinkOptionsǁ_get_http_proxy__mutmut_orig.__name__ = 'xǁStreamlinkOptionsǁ_get_http_proxy'

    def xǁStreamlinkOptionsǁ_get_http_attr__mutmut_orig(self, key):
        return getattr(self.session.http, self._OPTIONS_HTTP_ATTRS[key])

    def xǁStreamlinkOptionsǁ_get_http_attr__mutmut_1(self, key):
        return getattr(None, self._OPTIONS_HTTP_ATTRS[key])

    def xǁStreamlinkOptionsǁ_get_http_attr__mutmut_2(self, key):
        return getattr(self.session.http, None)

    def xǁStreamlinkOptionsǁ_get_http_attr__mutmut_3(self, key):
        return getattr(self._OPTIONS_HTTP_ATTRS[key])

    def xǁStreamlinkOptionsǁ_get_http_attr__mutmut_4(self, key):
        return getattr(self.session.http, )
    
    xǁStreamlinkOptionsǁ_get_http_attr__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkOptionsǁ_get_http_attr__mutmut_1': xǁStreamlinkOptionsǁ_get_http_attr__mutmut_1, 
        'xǁStreamlinkOptionsǁ_get_http_attr__mutmut_2': xǁStreamlinkOptionsǁ_get_http_attr__mutmut_2, 
        'xǁStreamlinkOptionsǁ_get_http_attr__mutmut_3': xǁStreamlinkOptionsǁ_get_http_attr__mutmut_3, 
        'xǁStreamlinkOptionsǁ_get_http_attr__mutmut_4': xǁStreamlinkOptionsǁ_get_http_attr__mutmut_4
    }
    
    def _get_http_attr(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkOptionsǁ_get_http_attr__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkOptionsǁ_get_http_attr__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_http_attr.__signature__ = _mutmut_signature(xǁStreamlinkOptionsǁ_get_http_attr__mutmut_orig)
    xǁStreamlinkOptionsǁ_get_http_attr__mutmut_orig.__name__ = 'xǁStreamlinkOptionsǁ_get_http_attr'

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_orig(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_1(self, key, value):
        for adapter in self.session.http.adapters.values():
            if isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_2(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                break
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_3(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_4(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop(None, None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_5(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop(None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_6(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", )
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_7(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("XXsource_addressXX", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_8(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("SOURCE_ADDRESS", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_9(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("Source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_10(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=None)
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_11(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 1))
        self.set_explicit(key, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_12(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(None, None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_13(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_14(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(None if not value else value)

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_15(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, )

    # ---- setters

    def xǁStreamlinkOptionsǁ_set_interface__mutmut_16(self, key, value):
        for adapter in self.session.http.adapters.values():
            if not isinstance(adapter, HTTPAdapter):
                continue
            if not value:
                adapter.poolmanager.connection_pool_kw.pop("source_address", None)
            else:
                # https://docs.python.org/3/library/socket.html#socket.create_connection
                adapter.poolmanager.connection_pool_kw.update(source_address=(value, 0))
        self.set_explicit(key, None if value else value)
    
    xǁStreamlinkOptionsǁ_set_interface__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkOptionsǁ_set_interface__mutmut_1': xǁStreamlinkOptionsǁ_set_interface__mutmut_1, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_2': xǁStreamlinkOptionsǁ_set_interface__mutmut_2, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_3': xǁStreamlinkOptionsǁ_set_interface__mutmut_3, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_4': xǁStreamlinkOptionsǁ_set_interface__mutmut_4, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_5': xǁStreamlinkOptionsǁ_set_interface__mutmut_5, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_6': xǁStreamlinkOptionsǁ_set_interface__mutmut_6, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_7': xǁStreamlinkOptionsǁ_set_interface__mutmut_7, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_8': xǁStreamlinkOptionsǁ_set_interface__mutmut_8, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_9': xǁStreamlinkOptionsǁ_set_interface__mutmut_9, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_10': xǁStreamlinkOptionsǁ_set_interface__mutmut_10, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_11': xǁStreamlinkOptionsǁ_set_interface__mutmut_11, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_12': xǁStreamlinkOptionsǁ_set_interface__mutmut_12, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_13': xǁStreamlinkOptionsǁ_set_interface__mutmut_13, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_14': xǁStreamlinkOptionsǁ_set_interface__mutmut_14, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_15': xǁStreamlinkOptionsǁ_set_interface__mutmut_15, 
        'xǁStreamlinkOptionsǁ_set_interface__mutmut_16': xǁStreamlinkOptionsǁ_set_interface__mutmut_16
    }
    
    def _set_interface(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkOptionsǁ_set_interface__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkOptionsǁ_set_interface__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _set_interface.__signature__ = _mutmut_signature(xǁStreamlinkOptionsǁ_set_interface__mutmut_orig)
    xǁStreamlinkOptionsǁ_set_interface__mutmut_orig.__name__ = 'xǁStreamlinkOptionsǁ_set_interface'

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_orig(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_1(self, key, value):
        self.set_explicit(None, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_2(self, key, value):
        self.set_explicit(key, None)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_3(self, key, value):
        self.set_explicit(value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_4(self, key, value):
        self.set_explicit(key, )
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_5(self, key, value):
        self.set_explicit(key, value)
        if value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_6(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = None  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_7(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key != "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_8(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "XXipv4XX":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_9(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "IPV4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_10(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "Ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_11(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit(None, False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_12(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", None)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_13(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit(False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_14(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", )
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_15(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("XXipv6XX", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_16(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("IPV6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_17(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("Ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_18(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", True)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_19(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = None  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_20(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: None  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_21(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit(None, False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_22(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", None)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_23(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit(False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_24(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", )
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_25(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("XXipv4XX", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_26(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("IPV4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_27(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("Ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_28(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", True)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET6  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_29(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = None  # type: ignore[attr-defined]

    def xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_30(self, key, value):
        self.set_explicit(key, value)
        if not value:
            urllib3_util_connection.allowed_gai_family = _original_allowed_gai_family  # type: ignore[attr-defined]
        elif key == "ipv4":
            self.set_explicit("ipv6", False)
            urllib3_util_connection.allowed_gai_family = lambda: AF_INET  # type: ignore[attr-defined]
        else:
            self.set_explicit("ipv4", False)
            urllib3_util_connection.allowed_gai_family = lambda: None  # type: ignore[attr-defined]
    
    xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_1': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_1, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_2': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_2, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_3': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_3, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_4': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_4, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_5': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_5, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_6': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_6, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_7': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_7, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_8': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_8, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_9': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_9, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_10': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_10, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_11': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_11, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_12': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_12, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_13': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_13, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_14': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_14, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_15': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_15, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_16': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_16, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_17': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_17, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_18': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_18, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_19': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_19, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_20': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_20, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_21': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_21, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_22': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_22, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_23': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_23, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_24': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_24, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_25': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_25, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_26': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_26, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_27': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_27, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_28': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_28, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_29': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_29, 
        'xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_30': xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_30
    }
    
    def _set_ipv4_ipv6(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _set_ipv4_ipv6.__signature__ = _mutmut_signature(xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_orig)
    xǁStreamlinkOptionsǁ_set_ipv4_ipv6__mutmut_orig.__name__ = 'xǁStreamlinkOptionsǁ_set_ipv4_ipv6'

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_orig(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("https://", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_1(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = None  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_2(self, key, value):
        self.session.http.proxies["XXhttpXX"] \
            = self.session.http.proxies["https"] \
            = update_scheme("https://", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_3(self, key, value):
        self.session.http.proxies["HTTP"] \
            = self.session.http.proxies["https"] \
            = update_scheme("https://", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_4(self, key, value):
        self.session.http.proxies["Http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("https://", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_5(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["XXhttpsXX"] \
            = update_scheme("https://", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_6(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["HTTPS"] \
            = update_scheme("https://", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_7(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["Https"] \
            = update_scheme("https://", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_8(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme(None, value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_9(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("https://", None, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_10(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("https://", value, force=None)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_11(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme(value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_12(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("https://", force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_13(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("https://", value, )  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_14(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("XXhttps://XX", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_15(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("HTTPS://", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_16(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("Https://", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_17(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("https://", value, force=True)  # fmt: skip
        self._deprecate_https_proxy(key)

    def xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_18(self, key, value):
        self.session.http.proxies["http"] \
            = self.session.http.proxies["https"] \
            = update_scheme("https://", value, force=False)  # fmt: skip
        self._deprecate_https_proxy(None)
    
    xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_1': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_1, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_2': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_2, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_3': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_3, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_4': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_4, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_5': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_5, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_6': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_6, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_7': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_7, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_8': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_8, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_9': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_9, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_10': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_10, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_11': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_11, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_12': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_12, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_13': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_13, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_14': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_14, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_15': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_15, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_16': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_16, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_17': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_17, 
        'xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_18': xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_18
    }
    
    def _set_http_proxy(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _set_http_proxy.__signature__ = _mutmut_signature(xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_orig)
    xǁStreamlinkOptionsǁ_set_http_proxy__mutmut_orig.__name__ = 'xǁStreamlinkOptionsǁ_set_http_proxy'

    def xǁStreamlinkOptionsǁ_set_http_attr__mutmut_orig(self, key, value):
        setattr(self.session.http, self._OPTIONS_HTTP_ATTRS[key], value)

    def xǁStreamlinkOptionsǁ_set_http_attr__mutmut_1(self, key, value):
        setattr(None, self._OPTIONS_HTTP_ATTRS[key], value)

    def xǁStreamlinkOptionsǁ_set_http_attr__mutmut_2(self, key, value):
        setattr(self.session.http, None, value)

    def xǁStreamlinkOptionsǁ_set_http_attr__mutmut_3(self, key, value):
        setattr(self.session.http, self._OPTIONS_HTTP_ATTRS[key], None)

    def xǁStreamlinkOptionsǁ_set_http_attr__mutmut_4(self, key, value):
        setattr(self._OPTIONS_HTTP_ATTRS[key], value)

    def xǁStreamlinkOptionsǁ_set_http_attr__mutmut_5(self, key, value):
        setattr(self.session.http, value)

    def xǁStreamlinkOptionsǁ_set_http_attr__mutmut_6(self, key, value):
        setattr(self.session.http, self._OPTIONS_HTTP_ATTRS[key], )
    
    xǁStreamlinkOptionsǁ_set_http_attr__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkOptionsǁ_set_http_attr__mutmut_1': xǁStreamlinkOptionsǁ_set_http_attr__mutmut_1, 
        'xǁStreamlinkOptionsǁ_set_http_attr__mutmut_2': xǁStreamlinkOptionsǁ_set_http_attr__mutmut_2, 
        'xǁStreamlinkOptionsǁ_set_http_attr__mutmut_3': xǁStreamlinkOptionsǁ_set_http_attr__mutmut_3, 
        'xǁStreamlinkOptionsǁ_set_http_attr__mutmut_4': xǁStreamlinkOptionsǁ_set_http_attr__mutmut_4, 
        'xǁStreamlinkOptionsǁ_set_http_attr__mutmut_5': xǁStreamlinkOptionsǁ_set_http_attr__mutmut_5, 
        'xǁStreamlinkOptionsǁ_set_http_attr__mutmut_6': xǁStreamlinkOptionsǁ_set_http_attr__mutmut_6
    }
    
    def _set_http_attr(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkOptionsǁ_set_http_attr__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkOptionsǁ_set_http_attr__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _set_http_attr.__signature__ = _mutmut_signature(xǁStreamlinkOptionsǁ_set_http_attr__mutmut_orig)
    xǁStreamlinkOptionsǁ_set_http_attr__mutmut_orig.__name__ = 'xǁStreamlinkOptionsǁ_set_http_attr'

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_orig(self, key, value):
        self.set_explicit(key, value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("https://", adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_1(self, key, value):
        self.set_explicit(None, value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("https://", adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_2(self, key, value):
        self.set_explicit(key, None)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("https://", adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_3(self, key, value):
        self.set_explicit(value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("https://", adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_4(self, key, value):
        self.set_explicit(key, )
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("https://", adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_5(self, key, value):
        self.set_explicit(key, value)
        if value:
            adapter = None
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("https://", adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_6(self, key, value):
        self.set_explicit(key, value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = None

        self.session.http.mount("https://", adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_7(self, key, value):
        self.set_explicit(key, value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount(None, adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_8(self, key, value):
        self.set_explicit(key, value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("https://", None)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_9(self, key, value):
        self.set_explicit(key, value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount(adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_10(self, key, value):
        self.set_explicit(key, value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("https://", )

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_11(self, key, value):
        self.set_explicit(key, value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("XXhttps://XX", adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_12(self, key, value):
        self.set_explicit(key, value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("HTTPS://", adapter)

    def xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_13(self, key, value):
        self.set_explicit(key, value)
        if value:
            adapter = TLSNoDHAdapter()
        else:
            adapter = HTTPAdapter()

        self.session.http.mount("Https://", adapter)
    
    xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_1': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_1, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_2': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_2, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_3': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_3, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_4': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_4, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_5': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_5, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_6': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_6, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_7': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_7, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_8': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_8, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_9': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_9, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_10': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_10, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_11': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_11, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_12': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_12, 
        'xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_13': xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_13
    }
    
    def _set_http_disable_dh(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _set_http_disable_dh.__signature__ = _mutmut_signature(xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_orig)
    xǁStreamlinkOptionsǁ_set_http_disable_dh__mutmut_orig.__name__ = 'xǁStreamlinkOptionsǁ_set_http_disable_dh'

    @staticmethod
    def _factory_set_http_attr_key_equals_value(delimiter: str) -> Callable[[StreamlinkOptions, str, Any], None]:
        def inner(self: "StreamlinkOptions", key: str, value: Any) -> None:
            getattr(self.session.http, self._OPTIONS_HTTP_ATTRS[key]).update(
                value if isinstance(value, dict) else dict(self._parse_key_equals_value_string(delimiter, value)),
            )

        return inner

    @staticmethod
    def _factory_set_deprecated(name: str, mapper: Callable[[Any], Any]) -> Callable[[StreamlinkOptions, str, Any], None]:
        def inner(self: StreamlinkOptions, key: str, value: Any) -> None:
            self.set_explicit(name, mapper(value))
            warnings.warn(
                f"`{key}` has been deprecated in favor of the `{name}` option",
                StreamlinkDeprecationWarning,
                stacklevel=3 + _get_deprecation_stacklevel_offset(),
            )

        return inner

    # TODO: py39 support end: remove explicit dummy context binding of static method
    _factory_set_http_attr_key_equals_value = _factory_set_http_attr_key_equals_value.__get__(object)
    _factory_set_deprecated = _factory_set_deprecated.__get__(object)

    # ----

    _OPTIONS_HTTP_ATTRS: ClassVar[Mapping[str, str]] = {
        "http-cookies": "cookies",
        "http-headers": "headers",
        "http-query-params": "params",
        "http-ssl-cert": "cert",
        "http-ssl-verify": "verify",
        "http-trust-env": "trust_env",
        "http-timeout": "timeout",
    }

    _MAP_GETTERS: ClassVar[Mapping[str, Callable[[StreamlinkOptions, str], Any]]] = {
        "http-proxy": _get_http_proxy,
        "https-proxy": _get_http_proxy,
        "http-cookies": _get_http_attr,
        "http-headers": _get_http_attr,
        "http-query-params": _get_http_attr,
        "http-ssl-cert": _get_http_attr,
        "http-ssl-verify": _get_http_attr,
        "http-trust-env": _get_http_attr,
        "http-timeout": _get_http_attr,
    }

    _MAP_SETTERS: ClassVar[Mapping[str, Callable[[StreamlinkOptions, str, Any], None]]] = {
        "interface": _set_interface,
        "ipv4": _set_ipv4_ipv6,
        "ipv6": _set_ipv4_ipv6,
        "http-proxy": _set_http_proxy,
        "https-proxy": _set_http_proxy,
        "http-cookies": _factory_set_http_attr_key_equals_value(";"),
        "http-headers": _factory_set_http_attr_key_equals_value(";"),
        "http-query-params": _factory_set_http_attr_key_equals_value("&"),
        "http-disable-dh": _set_http_disable_dh,
        "http-ssl-cert": _set_http_attr,
        "http-ssl-verify": _set_http_attr,
        "http-trust-env": _set_http_attr,
        "http-timeout": _set_http_attr,
    }

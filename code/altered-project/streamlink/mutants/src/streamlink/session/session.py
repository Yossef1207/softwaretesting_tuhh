from __future__ import annotations

import logging
import warnings
from collections.abc import Mapping
from functools import lru_cache
from typing import Any

import streamlink.compat  # noqa: F401
from streamlink import __version__
from streamlink.exceptions import NoPluginError, PluginError, StreamlinkDeprecationWarning
from streamlink.logger import StreamlinkLogger
from streamlink.options import Options
from streamlink.plugin.plugin import Plugin
from streamlink.session.http import HTTPSession
from streamlink.session.options import StreamlinkOptions
from streamlink.session.plugins import StreamlinkPlugins
from streamlink.utils.l10n import Localization
from streamlink.utils.url import update_scheme


# Ensure that the Logger class returned is Streamslink's for using the API (for backwards compatibility)
logging.setLoggerClass(StreamlinkLogger)
log = logging.getLogger(".".join(__name__.split(".")[:-1]))
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


class Streamlink:
    """
    The Streamlink session is used to load and resolve plugins, and to store options used by plugins and stream implementations.
    """

    def xǁStreamlinkǁ__init____mutmut_orig(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(self)
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(builtin=plugins_builtin, lazy=plugins_lazy)

    def xǁStreamlinkǁ__init____mutmut_1(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = False,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(self)
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(builtin=plugins_builtin, lazy=plugins_lazy)

    def xǁStreamlinkǁ__init____mutmut_2(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = False,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(self)
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(builtin=plugins_builtin, lazy=plugins_lazy)

    def xǁStreamlinkǁ__init____mutmut_3(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = None

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(self)
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(builtin=plugins_builtin, lazy=plugins_lazy)

    def xǁStreamlinkǁ__init____mutmut_4(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = None
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(builtin=plugins_builtin, lazy=plugins_lazy)

    def xǁStreamlinkǁ__init____mutmut_5(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(None)
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(builtin=plugins_builtin, lazy=plugins_lazy)

    def xǁStreamlinkǁ__init____mutmut_6(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(self)
        if options:
            self.options.update(None)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(builtin=plugins_builtin, lazy=plugins_lazy)

    def xǁStreamlinkǁ__init____mutmut_7(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(self)
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = None

    def xǁStreamlinkǁ__init____mutmut_8(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(self)
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(builtin=None, lazy=plugins_lazy)

    def xǁStreamlinkǁ__init____mutmut_9(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(self)
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(builtin=plugins_builtin, lazy=None)

    def xǁStreamlinkǁ__init____mutmut_10(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(self)
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(lazy=plugins_lazy)

    def xǁStreamlinkǁ__init____mutmut_11(
        self,
        options: Mapping[str, Any] | Options | None = None,
        *,
        plugins_builtin: bool = True,
        plugins_lazy: bool = True,
    ):
        """
        :param options: Custom options
        :param plugins_builtin: Whether to load built-in plugins or not
        :param plugins_lazy: Load built-in plugins lazily. This option falls back to loading all built-in plugins
                             if the pre-built plugin JSON metadata is not available (e.g. in editable installs) or is invalid.
        """

        #: An instance of Streamlink's :class:`requests.Session` subclass.
        #: Used for any kind of HTTP request made by plugin and stream implementations.
        self.http: HTTPSession = HTTPSession()

        #: Options of this session instance.
        #: :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` is a subclass
        #: of :class:`Options <streamlink.options.Options>` with special getter/setter mappings.
        self.options: StreamlinkOptions = StreamlinkOptions(self)
        if options:
            self.options.update(options)

        #: Plugins of this session instance.
        self.plugins: StreamlinkPlugins = StreamlinkPlugins(builtin=plugins_builtin, )
    
    xǁStreamlinkǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkǁ__init____mutmut_1': xǁStreamlinkǁ__init____mutmut_1, 
        'xǁStreamlinkǁ__init____mutmut_2': xǁStreamlinkǁ__init____mutmut_2, 
        'xǁStreamlinkǁ__init____mutmut_3': xǁStreamlinkǁ__init____mutmut_3, 
        'xǁStreamlinkǁ__init____mutmut_4': xǁStreamlinkǁ__init____mutmut_4, 
        'xǁStreamlinkǁ__init____mutmut_5': xǁStreamlinkǁ__init____mutmut_5, 
        'xǁStreamlinkǁ__init____mutmut_6': xǁStreamlinkǁ__init____mutmut_6, 
        'xǁStreamlinkǁ__init____mutmut_7': xǁStreamlinkǁ__init____mutmut_7, 
        'xǁStreamlinkǁ__init____mutmut_8': xǁStreamlinkǁ__init____mutmut_8, 
        'xǁStreamlinkǁ__init____mutmut_9': xǁStreamlinkǁ__init____mutmut_9, 
        'xǁStreamlinkǁ__init____mutmut_10': xǁStreamlinkǁ__init____mutmut_10, 
        'xǁStreamlinkǁ__init____mutmut_11': xǁStreamlinkǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStreamlinkǁ__init____mutmut_orig)
    xǁStreamlinkǁ__init____mutmut_orig.__name__ = 'xǁStreamlinkǁ__init__'

    def xǁStreamlinkǁset_option__mutmut_orig(self, key: str, value: Any) -> None:
        """
        Sets general options used by plugins and streams originating from this session object.

        This is a convenience wrapper for :meth:`self.options.set() <streamlink.session.options.StreamlinkOptions.set>`.

        Please see :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` for the available options.

        :param key: key of the option
        :param value: value to set the option to
        """

        self.options.set(key, value)

    def xǁStreamlinkǁset_option__mutmut_1(self, key: str, value: Any) -> None:
        """
        Sets general options used by plugins and streams originating from this session object.

        This is a convenience wrapper for :meth:`self.options.set() <streamlink.session.options.StreamlinkOptions.set>`.

        Please see :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` for the available options.

        :param key: key of the option
        :param value: value to set the option to
        """

        self.options.set(None, value)

    def xǁStreamlinkǁset_option__mutmut_2(self, key: str, value: Any) -> None:
        """
        Sets general options used by plugins and streams originating from this session object.

        This is a convenience wrapper for :meth:`self.options.set() <streamlink.session.options.StreamlinkOptions.set>`.

        Please see :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` for the available options.

        :param key: key of the option
        :param value: value to set the option to
        """

        self.options.set(key, None)

    def xǁStreamlinkǁset_option__mutmut_3(self, key: str, value: Any) -> None:
        """
        Sets general options used by plugins and streams originating from this session object.

        This is a convenience wrapper for :meth:`self.options.set() <streamlink.session.options.StreamlinkOptions.set>`.

        Please see :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` for the available options.

        :param key: key of the option
        :param value: value to set the option to
        """

        self.options.set(value)

    def xǁStreamlinkǁset_option__mutmut_4(self, key: str, value: Any) -> None:
        """
        Sets general options used by plugins and streams originating from this session object.

        This is a convenience wrapper for :meth:`self.options.set() <streamlink.session.options.StreamlinkOptions.set>`.

        Please see :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` for the available options.

        :param key: key of the option
        :param value: value to set the option to
        """

        self.options.set(key, )
    
    xǁStreamlinkǁset_option__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkǁset_option__mutmut_1': xǁStreamlinkǁset_option__mutmut_1, 
        'xǁStreamlinkǁset_option__mutmut_2': xǁStreamlinkǁset_option__mutmut_2, 
        'xǁStreamlinkǁset_option__mutmut_3': xǁStreamlinkǁset_option__mutmut_3, 
        'xǁStreamlinkǁset_option__mutmut_4': xǁStreamlinkǁset_option__mutmut_4
    }
    
    def set_option(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkǁset_option__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkǁset_option__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set_option.__signature__ = _mutmut_signature(xǁStreamlinkǁset_option__mutmut_orig)
    xǁStreamlinkǁset_option__mutmut_orig.__name__ = 'xǁStreamlinkǁset_option'

    def xǁStreamlinkǁget_option__mutmut_orig(self, key: str) -> Any:
        """
        Returns the current value of the specified option.

        This is a convenience wrapper for :meth:`self.options.get() <streamlink.session.options.StreamlinkOptions.get>`.

        Please see :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` for the available options.

        :param key: key of the option
        """

        return self.options.get(key)

    def xǁStreamlinkǁget_option__mutmut_1(self, key: str) -> Any:
        """
        Returns the current value of the specified option.

        This is a convenience wrapper for :meth:`self.options.get() <streamlink.session.options.StreamlinkOptions.get>`.

        Please see :class:`StreamlinkOptions <streamlink.session.options.StreamlinkOptions>` for the available options.

        :param key: key of the option
        """

        return self.options.get(None)
    
    xǁStreamlinkǁget_option__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkǁget_option__mutmut_1': xǁStreamlinkǁget_option__mutmut_1
    }
    
    def get_option(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkǁget_option__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkǁget_option__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_option.__signature__ = _mutmut_signature(xǁStreamlinkǁget_option__mutmut_orig)
    xǁStreamlinkǁget_option__mutmut_orig.__name__ = 'xǁStreamlinkǁget_option'

    @lru_cache(maxsize=128)  # noqa: B019
    def resolve_url(
        self,
        url: str,
        follow_redirect: bool = True,
    ) -> tuple[str, type[Plugin], str]:
        """
        Attempts to find a plugin that can use this URL.

        The default protocol (https) will be prefixed to the URL if not specified.

        Return values of this method are cached via :meth:`functools.lru_cache`.

        :param url: a URL to match against loaded plugins
        :param follow_redirect: follow redirects
        :raise NoPluginError: on plugin resolve failure
        :return: A tuple of plugin name, plugin class and resolved URL
        """

        url = update_scheme("https://", url, force=False)
        if resolved := self.plugins.match_url(url):
            return resolved[0], resolved[1], url

        if follow_redirect:
            # Attempt to handle a redirect URL
            try:
                res = self.http.head(url, allow_redirects=True, acceptable_status=[501])  # type: ignore[call-arg]

                # Fall back to GET request if server doesn't handle HEAD.
                if res.status_code == 501:
                    res = self.http.get(url, stream=True)

                if res.url != url:
                    return self.resolve_url(res.url, follow_redirect=follow_redirect)
            except PluginError:
                pass

        raise NoPluginError

    def xǁStreamlinkǁresolve_url_no_redirect__mutmut_orig(self, url: str) -> tuple[str, type[Plugin], str]:
        """
        Attempts to find a plugin that can use this URL.

        The default protocol (https) will be prefixed to the URL if not specified.

        :param url: a URL to match against loaded plugins
        :raise NoPluginError: on plugin resolve failure
        :return: A tuple of plugin name, plugin class and resolved URL
        """

        return self.resolve_url(url, follow_redirect=False)

    def xǁStreamlinkǁresolve_url_no_redirect__mutmut_1(self, url: str) -> tuple[str, type[Plugin], str]:
        """
        Attempts to find a plugin that can use this URL.

        The default protocol (https) will be prefixed to the URL if not specified.

        :param url: a URL to match against loaded plugins
        :raise NoPluginError: on plugin resolve failure
        :return: A tuple of plugin name, plugin class and resolved URL
        """

        return self.resolve_url(None, follow_redirect=False)

    def xǁStreamlinkǁresolve_url_no_redirect__mutmut_2(self, url: str) -> tuple[str, type[Plugin], str]:
        """
        Attempts to find a plugin that can use this URL.

        The default protocol (https) will be prefixed to the URL if not specified.

        :param url: a URL to match against loaded plugins
        :raise NoPluginError: on plugin resolve failure
        :return: A tuple of plugin name, plugin class and resolved URL
        """

        return self.resolve_url(url, follow_redirect=None)

    def xǁStreamlinkǁresolve_url_no_redirect__mutmut_3(self, url: str) -> tuple[str, type[Plugin], str]:
        """
        Attempts to find a plugin that can use this URL.

        The default protocol (https) will be prefixed to the URL if not specified.

        :param url: a URL to match against loaded plugins
        :raise NoPluginError: on plugin resolve failure
        :return: A tuple of plugin name, plugin class and resolved URL
        """

        return self.resolve_url(follow_redirect=False)

    def xǁStreamlinkǁresolve_url_no_redirect__mutmut_4(self, url: str) -> tuple[str, type[Plugin], str]:
        """
        Attempts to find a plugin that can use this URL.

        The default protocol (https) will be prefixed to the URL if not specified.

        :param url: a URL to match against loaded plugins
        :raise NoPluginError: on plugin resolve failure
        :return: A tuple of plugin name, plugin class and resolved URL
        """

        return self.resolve_url(url, )

    def xǁStreamlinkǁresolve_url_no_redirect__mutmut_5(self, url: str) -> tuple[str, type[Plugin], str]:
        """
        Attempts to find a plugin that can use this URL.

        The default protocol (https) will be prefixed to the URL if not specified.

        :param url: a URL to match against loaded plugins
        :raise NoPluginError: on plugin resolve failure
        :return: A tuple of plugin name, plugin class and resolved URL
        """

        return self.resolve_url(url, follow_redirect=True)
    
    xǁStreamlinkǁresolve_url_no_redirect__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkǁresolve_url_no_redirect__mutmut_1': xǁStreamlinkǁresolve_url_no_redirect__mutmut_1, 
        'xǁStreamlinkǁresolve_url_no_redirect__mutmut_2': xǁStreamlinkǁresolve_url_no_redirect__mutmut_2, 
        'xǁStreamlinkǁresolve_url_no_redirect__mutmut_3': xǁStreamlinkǁresolve_url_no_redirect__mutmut_3, 
        'xǁStreamlinkǁresolve_url_no_redirect__mutmut_4': xǁStreamlinkǁresolve_url_no_redirect__mutmut_4, 
        'xǁStreamlinkǁresolve_url_no_redirect__mutmut_5': xǁStreamlinkǁresolve_url_no_redirect__mutmut_5
    }
    
    def resolve_url_no_redirect(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkǁresolve_url_no_redirect__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkǁresolve_url_no_redirect__mutmut_mutants"), args, kwargs, self)
        return result 
    
    resolve_url_no_redirect.__signature__ = _mutmut_signature(xǁStreamlinkǁresolve_url_no_redirect__mutmut_orig)
    xǁStreamlinkǁresolve_url_no_redirect__mutmut_orig.__name__ = 'xǁStreamlinkǁresolve_url_no_redirect'

    def xǁStreamlinkǁstreams__mutmut_orig(self, url: str, options: Options | None = None, **params):
        """
        Attempts to find a plugin and extracts streams from the *url* if a plugin was found.

        :param url: a URL to match against loaded plugins
        :param options: Optional options instance passed to the resolved plugin
        :param params: Additional keyword arguments passed to :meth:`Plugin.streams() <streamlink.plugin.Plugin.streams>`
        :raises NoPluginError: on plugin resolve failure
        :return: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
        """

        _pluginname, pluginclass, resolved_url = self.resolve_url(url)
        plugin = pluginclass(self, resolved_url, options)

        return plugin.streams(**params)

    def xǁStreamlinkǁstreams__mutmut_1(self, url: str, options: Options | None = None, **params):
        """
        Attempts to find a plugin and extracts streams from the *url* if a plugin was found.

        :param url: a URL to match against loaded plugins
        :param options: Optional options instance passed to the resolved plugin
        :param params: Additional keyword arguments passed to :meth:`Plugin.streams() <streamlink.plugin.Plugin.streams>`
        :raises NoPluginError: on plugin resolve failure
        :return: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
        """

        _pluginname, pluginclass, resolved_url = None
        plugin = pluginclass(self, resolved_url, options)

        return plugin.streams(**params)

    def xǁStreamlinkǁstreams__mutmut_2(self, url: str, options: Options | None = None, **params):
        """
        Attempts to find a plugin and extracts streams from the *url* if a plugin was found.

        :param url: a URL to match against loaded plugins
        :param options: Optional options instance passed to the resolved plugin
        :param params: Additional keyword arguments passed to :meth:`Plugin.streams() <streamlink.plugin.Plugin.streams>`
        :raises NoPluginError: on plugin resolve failure
        :return: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
        """

        _pluginname, pluginclass, resolved_url = self.resolve_url(None)
        plugin = pluginclass(self, resolved_url, options)

        return plugin.streams(**params)

    def xǁStreamlinkǁstreams__mutmut_3(self, url: str, options: Options | None = None, **params):
        """
        Attempts to find a plugin and extracts streams from the *url* if a plugin was found.

        :param url: a URL to match against loaded plugins
        :param options: Optional options instance passed to the resolved plugin
        :param params: Additional keyword arguments passed to :meth:`Plugin.streams() <streamlink.plugin.Plugin.streams>`
        :raises NoPluginError: on plugin resolve failure
        :return: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
        """

        _pluginname, pluginclass, resolved_url = self.resolve_url(url)
        plugin = None

        return plugin.streams(**params)

    def xǁStreamlinkǁstreams__mutmut_4(self, url: str, options: Options | None = None, **params):
        """
        Attempts to find a plugin and extracts streams from the *url* if a plugin was found.

        :param url: a URL to match against loaded plugins
        :param options: Optional options instance passed to the resolved plugin
        :param params: Additional keyword arguments passed to :meth:`Plugin.streams() <streamlink.plugin.Plugin.streams>`
        :raises NoPluginError: on plugin resolve failure
        :return: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
        """

        _pluginname, pluginclass, resolved_url = self.resolve_url(url)
        plugin = pluginclass(None, resolved_url, options)

        return plugin.streams(**params)

    def xǁStreamlinkǁstreams__mutmut_5(self, url: str, options: Options | None = None, **params):
        """
        Attempts to find a plugin and extracts streams from the *url* if a plugin was found.

        :param url: a URL to match against loaded plugins
        :param options: Optional options instance passed to the resolved plugin
        :param params: Additional keyword arguments passed to :meth:`Plugin.streams() <streamlink.plugin.Plugin.streams>`
        :raises NoPluginError: on plugin resolve failure
        :return: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
        """

        _pluginname, pluginclass, resolved_url = self.resolve_url(url)
        plugin = pluginclass(self, None, options)

        return plugin.streams(**params)

    def xǁStreamlinkǁstreams__mutmut_6(self, url: str, options: Options | None = None, **params):
        """
        Attempts to find a plugin and extracts streams from the *url* if a plugin was found.

        :param url: a URL to match against loaded plugins
        :param options: Optional options instance passed to the resolved plugin
        :param params: Additional keyword arguments passed to :meth:`Plugin.streams() <streamlink.plugin.Plugin.streams>`
        :raises NoPluginError: on plugin resolve failure
        :return: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
        """

        _pluginname, pluginclass, resolved_url = self.resolve_url(url)
        plugin = pluginclass(self, resolved_url, None)

        return plugin.streams(**params)

    def xǁStreamlinkǁstreams__mutmut_7(self, url: str, options: Options | None = None, **params):
        """
        Attempts to find a plugin and extracts streams from the *url* if a plugin was found.

        :param url: a URL to match against loaded plugins
        :param options: Optional options instance passed to the resolved plugin
        :param params: Additional keyword arguments passed to :meth:`Plugin.streams() <streamlink.plugin.Plugin.streams>`
        :raises NoPluginError: on plugin resolve failure
        :return: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
        """

        _pluginname, pluginclass, resolved_url = self.resolve_url(url)
        plugin = pluginclass(resolved_url, options)

        return plugin.streams(**params)

    def xǁStreamlinkǁstreams__mutmut_8(self, url: str, options: Options | None = None, **params):
        """
        Attempts to find a plugin and extracts streams from the *url* if a plugin was found.

        :param url: a URL to match against loaded plugins
        :param options: Optional options instance passed to the resolved plugin
        :param params: Additional keyword arguments passed to :meth:`Plugin.streams() <streamlink.plugin.Plugin.streams>`
        :raises NoPluginError: on plugin resolve failure
        :return: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
        """

        _pluginname, pluginclass, resolved_url = self.resolve_url(url)
        plugin = pluginclass(self, options)

        return plugin.streams(**params)

    def xǁStreamlinkǁstreams__mutmut_9(self, url: str, options: Options | None = None, **params):
        """
        Attempts to find a plugin and extracts streams from the *url* if a plugin was found.

        :param url: a URL to match against loaded plugins
        :param options: Optional options instance passed to the resolved plugin
        :param params: Additional keyword arguments passed to :meth:`Plugin.streams() <streamlink.plugin.Plugin.streams>`
        :raises NoPluginError: on plugin resolve failure
        :return: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
        """

        _pluginname, pluginclass, resolved_url = self.resolve_url(url)
        plugin = pluginclass(self, resolved_url, )

        return plugin.streams(**params)
    
    xǁStreamlinkǁstreams__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkǁstreams__mutmut_1': xǁStreamlinkǁstreams__mutmut_1, 
        'xǁStreamlinkǁstreams__mutmut_2': xǁStreamlinkǁstreams__mutmut_2, 
        'xǁStreamlinkǁstreams__mutmut_3': xǁStreamlinkǁstreams__mutmut_3, 
        'xǁStreamlinkǁstreams__mutmut_4': xǁStreamlinkǁstreams__mutmut_4, 
        'xǁStreamlinkǁstreams__mutmut_5': xǁStreamlinkǁstreams__mutmut_5, 
        'xǁStreamlinkǁstreams__mutmut_6': xǁStreamlinkǁstreams__mutmut_6, 
        'xǁStreamlinkǁstreams__mutmut_7': xǁStreamlinkǁstreams__mutmut_7, 
        'xǁStreamlinkǁstreams__mutmut_8': xǁStreamlinkǁstreams__mutmut_8, 
        'xǁStreamlinkǁstreams__mutmut_9': xǁStreamlinkǁstreams__mutmut_9
    }
    
    def streams(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkǁstreams__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkǁstreams__mutmut_mutants"), args, kwargs, self)
        return result 
    
    streams.__signature__ = _mutmut_signature(xǁStreamlinkǁstreams__mutmut_orig)
    xǁStreamlinkǁstreams__mutmut_orig.__name__ = 'xǁStreamlinkǁstreams'

    def xǁStreamlinkǁget_plugins__mutmut_orig(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            "`Streamlink.get_plugins()` has been deprecated in favor of `Streamlink.plugins.get_loaded()`",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_1(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            None,
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_2(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            "`Streamlink.get_plugins()` has been deprecated in favor of `Streamlink.plugins.get_loaded()`",
            None,
            stacklevel=2,
        )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_3(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            "`Streamlink.get_plugins()` has been deprecated in favor of `Streamlink.plugins.get_loaded()`",
            StreamlinkDeprecationWarning,
            stacklevel=None,
        )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_4(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_5(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            "`Streamlink.get_plugins()` has been deprecated in favor of `Streamlink.plugins.get_loaded()`",
            stacklevel=2,
        )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_6(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            "`Streamlink.get_plugins()` has been deprecated in favor of `Streamlink.plugins.get_loaded()`",
            StreamlinkDeprecationWarning,
            )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_7(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            "XX`Streamlink.get_plugins()` has been deprecated in favor of `Streamlink.plugins.get_loaded()`XX",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_8(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            "`streamlink.get_plugins()` has been deprecated in favor of `streamlink.plugins.get_loaded()`",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_9(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            "`STREAMLINK.GET_PLUGINS()` HAS BEEN DEPRECATED IN FAVOR OF `STREAMLINK.PLUGINS.GET_LOADED()`",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_10(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            "`streamlink.get_plugins()` has been deprecated in favor of `streamlink.plugins.get_loaded()`",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.get_loaded()

    def xǁStreamlinkǁget_plugins__mutmut_11(self):
        """
        Returns the loaded plugins of this session.

        Deprecated in favor of :meth:`plugins.get_loaded() <streamlink.session.plugins.StreamlinkPlugins.get_loaded>`.
        """
        warnings.warn(
            "`Streamlink.get_plugins()` has been deprecated in favor of `Streamlink.plugins.get_loaded()`",
            StreamlinkDeprecationWarning,
            stacklevel=3,
        )
        return self.plugins.get_loaded()
    
    xǁStreamlinkǁget_plugins__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkǁget_plugins__mutmut_1': xǁStreamlinkǁget_plugins__mutmut_1, 
        'xǁStreamlinkǁget_plugins__mutmut_2': xǁStreamlinkǁget_plugins__mutmut_2, 
        'xǁStreamlinkǁget_plugins__mutmut_3': xǁStreamlinkǁget_plugins__mutmut_3, 
        'xǁStreamlinkǁget_plugins__mutmut_4': xǁStreamlinkǁget_plugins__mutmut_4, 
        'xǁStreamlinkǁget_plugins__mutmut_5': xǁStreamlinkǁget_plugins__mutmut_5, 
        'xǁStreamlinkǁget_plugins__mutmut_6': xǁStreamlinkǁget_plugins__mutmut_6, 
        'xǁStreamlinkǁget_plugins__mutmut_7': xǁStreamlinkǁget_plugins__mutmut_7, 
        'xǁStreamlinkǁget_plugins__mutmut_8': xǁStreamlinkǁget_plugins__mutmut_8, 
        'xǁStreamlinkǁget_plugins__mutmut_9': xǁStreamlinkǁget_plugins__mutmut_9, 
        'xǁStreamlinkǁget_plugins__mutmut_10': xǁStreamlinkǁget_plugins__mutmut_10, 
        'xǁStreamlinkǁget_plugins__mutmut_11': xǁStreamlinkǁget_plugins__mutmut_11
    }
    
    def get_plugins(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkǁget_plugins__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkǁget_plugins__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_plugins.__signature__ = _mutmut_signature(xǁStreamlinkǁget_plugins__mutmut_orig)
    xǁStreamlinkǁget_plugins__mutmut_orig.__name__ = 'xǁStreamlinkǁget_plugins'

    def xǁStreamlinkǁload_builtin_plugins__mutmut_orig(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            "`Streamlink.load_builtin_plugins()` has been deprecated in favor of the `plugins_builtin` keyword argument",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_1(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            None,
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_2(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            "`Streamlink.load_builtin_plugins()` has been deprecated in favor of the `plugins_builtin` keyword argument",
            None,
            stacklevel=2,
        )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_3(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            "`Streamlink.load_builtin_plugins()` has been deprecated in favor of the `plugins_builtin` keyword argument",
            StreamlinkDeprecationWarning,
            stacklevel=None,
        )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_4(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_5(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            "`Streamlink.load_builtin_plugins()` has been deprecated in favor of the `plugins_builtin` keyword argument",
            stacklevel=2,
        )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_6(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            "`Streamlink.load_builtin_plugins()` has been deprecated in favor of the `plugins_builtin` keyword argument",
            StreamlinkDeprecationWarning,
            )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_7(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            "XX`Streamlink.load_builtin_plugins()` has been deprecated in favor of the `plugins_builtin` keyword argumentXX",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_8(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            "`streamlink.load_builtin_plugins()` has been deprecated in favor of the `plugins_builtin` keyword argument",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_9(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            "`STREAMLINK.LOAD_BUILTIN_PLUGINS()` HAS BEEN DEPRECATED IN FAVOR OF THE `PLUGINS_BUILTIN` KEYWORD ARGUMENT",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_10(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            "`streamlink.load_builtin_plugins()` has been deprecated in favor of the `plugins_builtin` keyword argument",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        self.plugins.load_builtin()

    def xǁStreamlinkǁload_builtin_plugins__mutmut_11(self):
        """
        Loads Streamlink's built-in plugins.

        Deprecated in favor of using the :class:`plugins_builtin <streamlink.session.Streamlink>` keyword argument.
        """
        warnings.warn(
            "`Streamlink.load_builtin_plugins()` has been deprecated in favor of the `plugins_builtin` keyword argument",
            StreamlinkDeprecationWarning,
            stacklevel=3,
        )
        self.plugins.load_builtin()
    
    xǁStreamlinkǁload_builtin_plugins__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkǁload_builtin_plugins__mutmut_1': xǁStreamlinkǁload_builtin_plugins__mutmut_1, 
        'xǁStreamlinkǁload_builtin_plugins__mutmut_2': xǁStreamlinkǁload_builtin_plugins__mutmut_2, 
        'xǁStreamlinkǁload_builtin_plugins__mutmut_3': xǁStreamlinkǁload_builtin_plugins__mutmut_3, 
        'xǁStreamlinkǁload_builtin_plugins__mutmut_4': xǁStreamlinkǁload_builtin_plugins__mutmut_4, 
        'xǁStreamlinkǁload_builtin_plugins__mutmut_5': xǁStreamlinkǁload_builtin_plugins__mutmut_5, 
        'xǁStreamlinkǁload_builtin_plugins__mutmut_6': xǁStreamlinkǁload_builtin_plugins__mutmut_6, 
        'xǁStreamlinkǁload_builtin_plugins__mutmut_7': xǁStreamlinkǁload_builtin_plugins__mutmut_7, 
        'xǁStreamlinkǁload_builtin_plugins__mutmut_8': xǁStreamlinkǁload_builtin_plugins__mutmut_8, 
        'xǁStreamlinkǁload_builtin_plugins__mutmut_9': xǁStreamlinkǁload_builtin_plugins__mutmut_9, 
        'xǁStreamlinkǁload_builtin_plugins__mutmut_10': xǁStreamlinkǁload_builtin_plugins__mutmut_10, 
        'xǁStreamlinkǁload_builtin_plugins__mutmut_11': xǁStreamlinkǁload_builtin_plugins__mutmut_11
    }
    
    def load_builtin_plugins(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkǁload_builtin_plugins__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkǁload_builtin_plugins__mutmut_mutants"), args, kwargs, self)
        return result 
    
    load_builtin_plugins.__signature__ = _mutmut_signature(xǁStreamlinkǁload_builtin_plugins__mutmut_orig)
    xǁStreamlinkǁload_builtin_plugins__mutmut_orig.__name__ = 'xǁStreamlinkǁload_builtin_plugins'

    def xǁStreamlinkǁload_plugins__mutmut_orig(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "`Streamlink.load_plugins()` has been deprecated in favor of `Streamlink.plugins.load_path()`",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_1(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            None,
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_2(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "`Streamlink.load_plugins()` has been deprecated in favor of `Streamlink.plugins.load_path()`",
            None,
            stacklevel=2,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_3(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "`Streamlink.load_plugins()` has been deprecated in favor of `Streamlink.plugins.load_path()`",
            StreamlinkDeprecationWarning,
            stacklevel=None,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_4(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_5(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "`Streamlink.load_plugins()` has been deprecated in favor of `Streamlink.plugins.load_path()`",
            stacklevel=2,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_6(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "`Streamlink.load_plugins()` has been deprecated in favor of `Streamlink.plugins.load_path()`",
            StreamlinkDeprecationWarning,
            )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_7(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "XX`Streamlink.load_plugins()` has been deprecated in favor of `Streamlink.plugins.load_path()`XX",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_8(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "`streamlink.load_plugins()` has been deprecated in favor of `streamlink.plugins.load_path()`",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_9(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "`STREAMLINK.LOAD_PLUGINS()` HAS BEEN DEPRECATED IN FAVOR OF `STREAMLINK.PLUGINS.LOAD_PATH()`",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_10(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "`streamlink.load_plugins()` has been deprecated in favor of `streamlink.plugins.load_path()`",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_11(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "`Streamlink.load_plugins()` has been deprecated in favor of `Streamlink.plugins.load_path()`",
            StreamlinkDeprecationWarning,
            stacklevel=3,
        )
        return self.plugins.load_path(path)

    def xǁStreamlinkǁload_plugins__mutmut_12(self, path: str) -> bool:
        """
        Loads plugins from a specific path.

        Deprecated in favor of :meth:`plugins.load_path() <streamlink.session.plugins.StreamlinkPlugins.load_path>`.
        """
        warnings.warn(
            "`Streamlink.load_plugins()` has been deprecated in favor of `Streamlink.plugins.load_path()`",
            StreamlinkDeprecationWarning,
            stacklevel=2,
        )
        return self.plugins.load_path(None)
    
    xǁStreamlinkǁload_plugins__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkǁload_plugins__mutmut_1': xǁStreamlinkǁload_plugins__mutmut_1, 
        'xǁStreamlinkǁload_plugins__mutmut_2': xǁStreamlinkǁload_plugins__mutmut_2, 
        'xǁStreamlinkǁload_plugins__mutmut_3': xǁStreamlinkǁload_plugins__mutmut_3, 
        'xǁStreamlinkǁload_plugins__mutmut_4': xǁStreamlinkǁload_plugins__mutmut_4, 
        'xǁStreamlinkǁload_plugins__mutmut_5': xǁStreamlinkǁload_plugins__mutmut_5, 
        'xǁStreamlinkǁload_plugins__mutmut_6': xǁStreamlinkǁload_plugins__mutmut_6, 
        'xǁStreamlinkǁload_plugins__mutmut_7': xǁStreamlinkǁload_plugins__mutmut_7, 
        'xǁStreamlinkǁload_plugins__mutmut_8': xǁStreamlinkǁload_plugins__mutmut_8, 
        'xǁStreamlinkǁload_plugins__mutmut_9': xǁStreamlinkǁload_plugins__mutmut_9, 
        'xǁStreamlinkǁload_plugins__mutmut_10': xǁStreamlinkǁload_plugins__mutmut_10, 
        'xǁStreamlinkǁload_plugins__mutmut_11': xǁStreamlinkǁload_plugins__mutmut_11, 
        'xǁStreamlinkǁload_plugins__mutmut_12': xǁStreamlinkǁload_plugins__mutmut_12
    }
    
    def load_plugins(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkǁload_plugins__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkǁload_plugins__mutmut_mutants"), args, kwargs, self)
        return result 
    
    load_plugins.__signature__ = _mutmut_signature(xǁStreamlinkǁload_plugins__mutmut_orig)
    xǁStreamlinkǁload_plugins__mutmut_orig.__name__ = 'xǁStreamlinkǁload_plugins'

    @property
    def version(self):
        return __version__

    @property
    def localization(self):
        return Localization(self.get_option("locale"))


__all__ = ["Streamlink"]

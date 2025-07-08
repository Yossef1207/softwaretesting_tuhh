from __future__ import annotations

import base64
import hashlib
import importlib.metadata
import json
import logging
import pkgutil
import re
from collections.abc import Iterator, Mapping
from contextlib import suppress
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING, Literal, TypedDict

import streamlink.plugins
from streamlink.options import Argument, Arguments

# noinspection PyProtectedMember
from streamlink.plugin.plugin import _PLUGINARGUMENT_TYPE_REGISTRY, NO_PRIORITY, NORMAL_PRIORITY, Matcher, Matchers, Plugin
from streamlink.utils.module import exec_module, get_finder


if TYPE_CHECKING:
    try:
        from typing import TypeAlias  # type: ignore[attr-defined]
    except ImportError:
        from typing_extensions import TypeAlias

    from _typeshed.importlib import PathEntryFinderProtocol


log = logging.getLogger(".".join(__name__.split(".")[:-1]))

# The path to Streamlink's built-in plugins
_PLUGINS_PATH = Path(streamlink.plugins.__path__[0])

# Hardcoded plugins JSON file path
_PLUGINSDATA_PATH = _PLUGINS_PATH / "_plugins.json"
# Hardcoded package name to look up metadata
_PLUGINSDATA_PACKAGENAME = "streamlink"
# The `parts` value of the plugins JSON file contained in the package's `RECORD` metadata file
_PLUGINSDATA_PACKAGEPATH = "streamlink", "plugins", "_plugins.json"
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


class StreamlinkPlugins:
    """
    Streamlink's session-plugins implementation. This class is responsible for loading plugins and resolving them from URLs.

    See the :attr:`Streamlink.plugins <streamlink.session.Streamlink.plugins>` attribute.

    Unless disabled by the user, Streamlink will try to load built-in plugins lazily, when accessing them for the first time
    while resolving input URLs. This is done by reading and interpreting serialized data of each plugin's
    :func:`pluginmatcher <streamlink.plugin.pluginmatcher>` and :func:`pluginargument <streamlink.plugin.pluginargument>`
    data from a pre-built plugins JSON file which is included in Streamlink's wheel packages.

    Plugins which are sideloaded, either from specific user directories or custom input directories,
    always have a higher priority than built-in plugins.
    """

    def xǁStreamlinkPluginsǁ__init____mutmut_orig(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_1(self, builtin: bool = False, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_2(self, builtin: bool = True, lazy: bool = False):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_3(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = None

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_4(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = None
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_5(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = None

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_6(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin or lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_7(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = None
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_8(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = None
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_9(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = None

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_10(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = True

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_11(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin or not lazy:
            self.load_builtin()

    def xǁStreamlinkPluginsǁ__init____mutmut_12(self, builtin: bool = True, lazy: bool = True):
        # Loaded plugins
        self._plugins: dict[str, type[Plugin]] = {}

        # Data of built-in plugins which can be loaded lazily
        self._matchers: dict[str, Matchers] = {}
        self._arguments: dict[str, Arguments] = {}

        # Attempt to load built-in plugins lazily first
        if builtin and lazy:
            data = StreamlinkPluginsData.load()
            if data:
                self._matchers, self._arguments = data
            else:
                lazy = False

        # Load built-ins if lazy-loading is disabled or if loading plugins data has failed
        if builtin and lazy:
            self.load_builtin()
    
    xǁStreamlinkPluginsǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁ__init____mutmut_1': xǁStreamlinkPluginsǁ__init____mutmut_1, 
        'xǁStreamlinkPluginsǁ__init____mutmut_2': xǁStreamlinkPluginsǁ__init____mutmut_2, 
        'xǁStreamlinkPluginsǁ__init____mutmut_3': xǁStreamlinkPluginsǁ__init____mutmut_3, 
        'xǁStreamlinkPluginsǁ__init____mutmut_4': xǁStreamlinkPluginsǁ__init____mutmut_4, 
        'xǁStreamlinkPluginsǁ__init____mutmut_5': xǁStreamlinkPluginsǁ__init____mutmut_5, 
        'xǁStreamlinkPluginsǁ__init____mutmut_6': xǁStreamlinkPluginsǁ__init____mutmut_6, 
        'xǁStreamlinkPluginsǁ__init____mutmut_7': xǁStreamlinkPluginsǁ__init____mutmut_7, 
        'xǁStreamlinkPluginsǁ__init____mutmut_8': xǁStreamlinkPluginsǁ__init____mutmut_8, 
        'xǁStreamlinkPluginsǁ__init____mutmut_9': xǁStreamlinkPluginsǁ__init____mutmut_9, 
        'xǁStreamlinkPluginsǁ__init____mutmut_10': xǁStreamlinkPluginsǁ__init____mutmut_10, 
        'xǁStreamlinkPluginsǁ__init____mutmut_11': xǁStreamlinkPluginsǁ__init____mutmut_11, 
        'xǁStreamlinkPluginsǁ__init____mutmut_12': xǁStreamlinkPluginsǁ__init____mutmut_12
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁ__init____mutmut_orig)
    xǁStreamlinkPluginsǁ__init____mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁ__init__'

    def __getitem__(self, item: str) -> type[Plugin]:
        """Access a loaded plugin class by name"""
        return self._plugins[item]

    def xǁStreamlinkPluginsǁ__setitem____mutmut_orig(self, key: str, value: type[Plugin]) -> None:
        """Add/override a plugin class by name"""
        self._plugins[key] = value

    def xǁStreamlinkPluginsǁ__setitem____mutmut_1(self, key: str, value: type[Plugin]) -> None:
        """Add/override a plugin class by name"""
        self._plugins[key] = None
    
    xǁStreamlinkPluginsǁ__setitem____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁ__setitem____mutmut_1': xǁStreamlinkPluginsǁ__setitem____mutmut_1
    }
    
    def __setitem__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁ__setitem____mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁ__setitem____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __setitem__.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁ__setitem____mutmut_orig)
    xǁStreamlinkPluginsǁ__setitem____mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁ__setitem__'

    def xǁStreamlinkPluginsǁ__delitem____mutmut_orig(self, key: str) -> None:
        """Remove a loaded plugin by name"""
        self._plugins.pop(key, None)

    def xǁStreamlinkPluginsǁ__delitem____mutmut_1(self, key: str) -> None:
        """Remove a loaded plugin by name"""
        self._plugins.pop(None, None)

    def xǁStreamlinkPluginsǁ__delitem____mutmut_2(self, key: str) -> None:
        """Remove a loaded plugin by name"""
        self._plugins.pop(None)

    def xǁStreamlinkPluginsǁ__delitem____mutmut_3(self, key: str) -> None:
        """Remove a loaded plugin by name"""
        self._plugins.pop(key, )
    
    xǁStreamlinkPluginsǁ__delitem____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁ__delitem____mutmut_1': xǁStreamlinkPluginsǁ__delitem____mutmut_1, 
        'xǁStreamlinkPluginsǁ__delitem____mutmut_2': xǁStreamlinkPluginsǁ__delitem____mutmut_2, 
        'xǁStreamlinkPluginsǁ__delitem____mutmut_3': xǁStreamlinkPluginsǁ__delitem____mutmut_3
    }
    
    def __delitem__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁ__delitem____mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁ__delitem____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __delitem__.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁ__delitem____mutmut_orig)
    xǁStreamlinkPluginsǁ__delitem____mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁ__delitem__'

    def xǁStreamlinkPluginsǁ__contains____mutmut_orig(self, item: str) -> bool:
        """Check if a plugin is loaded"""
        return item in self._plugins

    def xǁStreamlinkPluginsǁ__contains____mutmut_1(self, item: str) -> bool:
        """Check if a plugin is loaded"""
        return item not in self._plugins
    
    xǁStreamlinkPluginsǁ__contains____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁ__contains____mutmut_1': xǁStreamlinkPluginsǁ__contains____mutmut_1
    }
    
    def __contains__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁ__contains____mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁ__contains____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __contains__.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁ__contains____mutmut_orig)
    xǁStreamlinkPluginsǁ__contains____mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁ__contains__'

    def xǁStreamlinkPluginsǁget_names__mutmut_orig(self) -> list[str]:
        """Get a list of the names of all available plugins"""
        return sorted(self._plugins.keys() | self._matchers.keys())

    def xǁStreamlinkPluginsǁget_names__mutmut_1(self) -> list[str]:
        """Get a list of the names of all available plugins"""
        return sorted(None)

    def xǁStreamlinkPluginsǁget_names__mutmut_2(self) -> list[str]:
        """Get a list of the names of all available plugins"""
        return sorted(self._plugins.keys() & self._matchers.keys())
    
    xǁStreamlinkPluginsǁget_names__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁget_names__mutmut_1': xǁStreamlinkPluginsǁget_names__mutmut_1, 
        'xǁStreamlinkPluginsǁget_names__mutmut_2': xǁStreamlinkPluginsǁget_names__mutmut_2
    }
    
    def get_names(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁget_names__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁget_names__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_names.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁget_names__mutmut_orig)
    xǁStreamlinkPluginsǁget_names__mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁget_names'

    def xǁStreamlinkPluginsǁget_loaded__mutmut_orig(self) -> dict[str, type[Plugin]]:
        """Get a mapping of all loaded plugins"""
        return dict(self._plugins)

    def xǁStreamlinkPluginsǁget_loaded__mutmut_1(self) -> dict[str, type[Plugin]]:
        """Get a mapping of all loaded plugins"""
        return dict(None)
    
    xǁStreamlinkPluginsǁget_loaded__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁget_loaded__mutmut_1': xǁStreamlinkPluginsǁget_loaded__mutmut_1
    }
    
    def get_loaded(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁget_loaded__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁget_loaded__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_loaded.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁget_loaded__mutmut_orig)
    xǁStreamlinkPluginsǁget_loaded__mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁget_loaded'

    def xǁStreamlinkPluginsǁload_builtin__mutmut_orig(self) -> bool:
        """Load Streamlink's built-in plugins"""
        return self.load_path(_PLUGINS_PATH)

    def xǁStreamlinkPluginsǁload_builtin__mutmut_1(self) -> bool:
        """Load Streamlink's built-in plugins"""
        return self.load_path(None)
    
    xǁStreamlinkPluginsǁload_builtin__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁload_builtin__mutmut_1': xǁStreamlinkPluginsǁload_builtin__mutmut_1
    }
    
    def load_builtin(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁload_builtin__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁload_builtin__mutmut_mutants"), args, kwargs, self)
        return result 
    
    load_builtin.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁload_builtin__mutmut_orig)
    xǁStreamlinkPluginsǁload_builtin__mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁload_builtin'

    def xǁStreamlinkPluginsǁload_path__mutmut_orig(self, path: str | Path) -> bool:
        """Load plugins from a custom directory"""
        plugins = self._load_plugins_from_path(path)
        self.update(plugins)

        return bool(plugins)

    def xǁStreamlinkPluginsǁload_path__mutmut_1(self, path: str | Path) -> bool:
        """Load plugins from a custom directory"""
        plugins = None
        self.update(plugins)

        return bool(plugins)

    def xǁStreamlinkPluginsǁload_path__mutmut_2(self, path: str | Path) -> bool:
        """Load plugins from a custom directory"""
        plugins = self._load_plugins_from_path(None)
        self.update(plugins)

        return bool(plugins)

    def xǁStreamlinkPluginsǁload_path__mutmut_3(self, path: str | Path) -> bool:
        """Load plugins from a custom directory"""
        plugins = self._load_plugins_from_path(path)
        self.update(None)

        return bool(plugins)

    def xǁStreamlinkPluginsǁload_path__mutmut_4(self, path: str | Path) -> bool:
        """Load plugins from a custom directory"""
        plugins = self._load_plugins_from_path(path)
        self.update(plugins)

        return bool(None)
    
    xǁStreamlinkPluginsǁload_path__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁload_path__mutmut_1': xǁStreamlinkPluginsǁload_path__mutmut_1, 
        'xǁStreamlinkPluginsǁload_path__mutmut_2': xǁStreamlinkPluginsǁload_path__mutmut_2, 
        'xǁStreamlinkPluginsǁload_path__mutmut_3': xǁStreamlinkPluginsǁload_path__mutmut_3, 
        'xǁStreamlinkPluginsǁload_path__mutmut_4': xǁStreamlinkPluginsǁload_path__mutmut_4
    }
    
    def load_path(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁload_path__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁload_path__mutmut_mutants"), args, kwargs, self)
        return result 
    
    load_path.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁload_path__mutmut_orig)
    xǁStreamlinkPluginsǁload_path__mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁload_path'

    def xǁStreamlinkPluginsǁupdate__mutmut_orig(self, plugins: Mapping[str, type[Plugin]]):
        """Add/override loaded plugins"""
        self._plugins.update(plugins)

    def xǁStreamlinkPluginsǁupdate__mutmut_1(self, plugins: Mapping[str, type[Plugin]]):
        """Add/override loaded plugins"""
        self._plugins.update(None)
    
    xǁStreamlinkPluginsǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁupdate__mutmut_1': xǁStreamlinkPluginsǁupdate__mutmut_1
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁupdate__mutmut_orig)
    xǁStreamlinkPluginsǁupdate__mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁupdate'

    def clear(self):
        """Remove all loaded plugins from the session"""
        self._plugins.clear()

    def xǁStreamlinkPluginsǁiter_arguments__mutmut_orig(self) -> Iterator[tuple[str, Arguments]]:
        """Iterate through all plugins and their :class:`Arguments <streamlink.options.Arguments>`"""
        yield from (
            (name, plugin.arguments)
            for name, plugin in self._plugins.items()
            if plugin.arguments
        )  # fmt: skip
        yield from (
            (name, arguments)
            for name, arguments in self._arguments.items()
            if arguments and name not in self._plugins
        )  # fmt: skip

    def xǁStreamlinkPluginsǁiter_arguments__mutmut_1(self) -> Iterator[tuple[str, Arguments]]:
        """Iterate through all plugins and their :class:`Arguments <streamlink.options.Arguments>`"""
        yield from (
            (name, plugin.arguments)
            for name, plugin in self._plugins.items()
            if plugin.arguments
        )  # fmt: skip
        yield from (
            (name, arguments)
            for name, arguments in self._arguments.items()
            if arguments or name not in self._plugins
        )  # fmt: skip

    def xǁStreamlinkPluginsǁiter_arguments__mutmut_2(self) -> Iterator[tuple[str, Arguments]]:
        """Iterate through all plugins and their :class:`Arguments <streamlink.options.Arguments>`"""
        yield from (
            (name, plugin.arguments)
            for name, plugin in self._plugins.items()
            if plugin.arguments
        )  # fmt: skip
        yield from (
            (name, arguments)
            for name, arguments in self._arguments.items()
            if arguments and name in self._plugins
        )  # fmt: skip
    
    xǁStreamlinkPluginsǁiter_arguments__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁiter_arguments__mutmut_1': xǁStreamlinkPluginsǁiter_arguments__mutmut_1, 
        'xǁStreamlinkPluginsǁiter_arguments__mutmut_2': xǁStreamlinkPluginsǁiter_arguments__mutmut_2
    }
    
    def iter_arguments(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁiter_arguments__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁiter_arguments__mutmut_mutants"), args, kwargs, self)
        return result 
    
    iter_arguments.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁiter_arguments__mutmut_orig)
    xǁStreamlinkPluginsǁiter_arguments__mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁiter_arguments'

    def xǁStreamlinkPluginsǁiter_matchers__mutmut_orig(self) -> Iterator[tuple[str, Matchers]]:
        """Iterate through all plugins and their :class:`Matchers <streamlink.plugin.plugin.Matchers>`"""
        yield from (
            (name, plugin.matchers)
            for name, plugin in self._plugins.items()
            if plugin.matchers
        )  # fmt: skip
        yield from (
            (name, matchers)
            for name, matchers in self._matchers.items()
            if matchers and name not in self._plugins
        )  # fmt: skip

    def xǁStreamlinkPluginsǁiter_matchers__mutmut_1(self) -> Iterator[tuple[str, Matchers]]:
        """Iterate through all plugins and their :class:`Matchers <streamlink.plugin.plugin.Matchers>`"""
        yield from (
            (name, plugin.matchers)
            for name, plugin in self._plugins.items()
            if plugin.matchers
        )  # fmt: skip
        yield from (
            (name, matchers)
            for name, matchers in self._matchers.items()
            if matchers or name not in self._plugins
        )  # fmt: skip

    def xǁStreamlinkPluginsǁiter_matchers__mutmut_2(self) -> Iterator[tuple[str, Matchers]]:
        """Iterate through all plugins and their :class:`Matchers <streamlink.plugin.plugin.Matchers>`"""
        yield from (
            (name, plugin.matchers)
            for name, plugin in self._plugins.items()
            if plugin.matchers
        )  # fmt: skip
        yield from (
            (name, matchers)
            for name, matchers in self._matchers.items()
            if matchers and name in self._plugins
        )  # fmt: skip
    
    xǁStreamlinkPluginsǁiter_matchers__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁiter_matchers__mutmut_1': xǁStreamlinkPluginsǁiter_matchers__mutmut_1, 
        'xǁStreamlinkPluginsǁiter_matchers__mutmut_2': xǁStreamlinkPluginsǁiter_matchers__mutmut_2
    }
    
    def iter_matchers(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁiter_matchers__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁiter_matchers__mutmut_mutants"), args, kwargs, self)
        return result 
    
    iter_matchers.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁiter_matchers__mutmut_orig)
    xǁStreamlinkPluginsǁiter_matchers__mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁiter_matchers'

    def xǁStreamlinkPluginsǁmatch_url__mutmut_orig(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_1(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = ""
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_2(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = None

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_3(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority >= priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_4(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority or matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_5(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(None) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_6(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_7(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = None
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_8(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = None

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_9(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is not None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_10(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_11(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(None)
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_12(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = None
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_13(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(None, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_14(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, None)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_15(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(_PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_16(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, )
            if not lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_17(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if lookup:
                return None
            self._plugins[match] = lookup[1]

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_18(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = None

        return match, self._plugins[match]

    def xǁStreamlinkPluginsǁmatch_url__mutmut_19(self, url: str) -> tuple[str, type[Plugin]] | None:
        """Find a matching plugin by URL and load plugins which haven't been loaded yet"""
        match: str | None = None
        priority: int = NO_PRIORITY

        for name, matchers in self.iter_matchers():
            for matcher in matchers:
                if matcher.priority > priority and matcher.pattern.match(url) is not None:
                    match = name
                    priority = matcher.priority

        if match is None:
            return None

        # plugin not loaded yet?
        # if a custom plugin with the same name has already been loaded, skip loading the built-in plugin
        if match not in self._plugins:
            log.debug(f"Loading plugin: {match}")
            lookup = self._load_plugin_from_path(match, _PLUGINS_PATH)
            if not lookup:
                return None
            self._plugins[match] = lookup[2]

        return match, self._plugins[match]
    
    xǁStreamlinkPluginsǁmatch_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁmatch_url__mutmut_1': xǁStreamlinkPluginsǁmatch_url__mutmut_1, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_2': xǁStreamlinkPluginsǁmatch_url__mutmut_2, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_3': xǁStreamlinkPluginsǁmatch_url__mutmut_3, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_4': xǁStreamlinkPluginsǁmatch_url__mutmut_4, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_5': xǁStreamlinkPluginsǁmatch_url__mutmut_5, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_6': xǁStreamlinkPluginsǁmatch_url__mutmut_6, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_7': xǁStreamlinkPluginsǁmatch_url__mutmut_7, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_8': xǁStreamlinkPluginsǁmatch_url__mutmut_8, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_9': xǁStreamlinkPluginsǁmatch_url__mutmut_9, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_10': xǁStreamlinkPluginsǁmatch_url__mutmut_10, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_11': xǁStreamlinkPluginsǁmatch_url__mutmut_11, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_12': xǁStreamlinkPluginsǁmatch_url__mutmut_12, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_13': xǁStreamlinkPluginsǁmatch_url__mutmut_13, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_14': xǁStreamlinkPluginsǁmatch_url__mutmut_14, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_15': xǁStreamlinkPluginsǁmatch_url__mutmut_15, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_16': xǁStreamlinkPluginsǁmatch_url__mutmut_16, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_17': xǁStreamlinkPluginsǁmatch_url__mutmut_17, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_18': xǁStreamlinkPluginsǁmatch_url__mutmut_18, 
        'xǁStreamlinkPluginsǁmatch_url__mutmut_19': xǁStreamlinkPluginsǁmatch_url__mutmut_19
    }
    
    def match_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁmatch_url__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁmatch_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    match_url.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁmatch_url__mutmut_orig)
    xǁStreamlinkPluginsǁmatch_url__mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁmatch_url'

    def xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_orig(self, name: str, path: Path) -> tuple[ModuleType, type[Plugin]] | None:
        finder = get_finder(path)

        return self._load_plugin_from_finder(name, finder)

    def xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_1(self, name: str, path: Path) -> tuple[ModuleType, type[Plugin]] | None:
        finder = None

        return self._load_plugin_from_finder(name, finder)

    def xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_2(self, name: str, path: Path) -> tuple[ModuleType, type[Plugin]] | None:
        finder = get_finder(None)

        return self._load_plugin_from_finder(name, finder)

    def xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_3(self, name: str, path: Path) -> tuple[ModuleType, type[Plugin]] | None:
        finder = get_finder(path)

        return self._load_plugin_from_finder(None, finder)

    def xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_4(self, name: str, path: Path) -> tuple[ModuleType, type[Plugin]] | None:
        finder = get_finder(path)

        return self._load_plugin_from_finder(name, None)

    def xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_5(self, name: str, path: Path) -> tuple[ModuleType, type[Plugin]] | None:
        finder = get_finder(path)

        return self._load_plugin_from_finder(finder)

    def xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_6(self, name: str, path: Path) -> tuple[ModuleType, type[Plugin]] | None:
        finder = get_finder(path)

        return self._load_plugin_from_finder(name, )
    
    xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_1': xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_1, 
        'xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_2': xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_2, 
        'xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_3': xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_3, 
        'xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_4': xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_4, 
        'xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_5': xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_5, 
        'xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_6': xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_6
    }
    
    def _load_plugin_from_path(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _load_plugin_from_path.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_orig)
    xǁStreamlinkPluginsǁ_load_plugin_from_path__mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁ_load_plugin_from_path'

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_orig(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_1(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = None
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_2(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules(None):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_3(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(None)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_4(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = None  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_5(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(None, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_6(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=None)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_7(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_8(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, )  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_9(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is not None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_10(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                break
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_11(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = None
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_12(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name not in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_13(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins and name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_14(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name not in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_15(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) or mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_16(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(None, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_17(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, None) as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_18(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open("rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_19(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, ) as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_20(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "XXrbXX") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_21(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "RB") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_22(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "Rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_23(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = None
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_24(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(None)
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_25(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(None)
            plugins[name] = plugin

        return plugins

    def xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_26(self, path: str | Path) -> dict[str, type[Plugin]]:
        plugins: dict[str, type[Plugin]] = {}
        for finder, name, _ in pkgutil.iter_modules([str(path)]):
            lookup = self._load_plugin_from_finder(name, finder=finder)  # type: ignore[arg-type]
            if lookup is None:
                continue
            mod, plugin = lookup
            if (name in self._plugins or name in self._matchers) and mod.__file__:
                with open(mod.__file__, "rb") as fh:
                    sha256 = hashlib.sha256(fh.read())
                log.info(f"Plugin {name} is being overridden by {mod.__file__} (sha256:{sha256.hexdigest()})")
            plugins[name] = None

        return plugins
    
    xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_1': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_1, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_2': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_2, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_3': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_3, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_4': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_4, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_5': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_5, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_6': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_6, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_7': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_7, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_8': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_8, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_9': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_9, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_10': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_10, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_11': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_11, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_12': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_12, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_13': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_13, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_14': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_14, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_15': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_15, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_16': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_16, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_17': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_17, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_18': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_18, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_19': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_19, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_20': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_20, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_21': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_21, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_22': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_22, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_23': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_23, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_24': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_24, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_25': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_25, 
        'xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_26': xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_26
    }
    
    def _load_plugins_from_path(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_orig"), object.__getattribute__(self, "xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _load_plugins_from_path.__signature__ = _mutmut_signature(xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_orig)
    xǁStreamlinkPluginsǁ_load_plugins_from_path__mutmut_orig.__name__ = 'xǁStreamlinkPluginsǁ_load_plugins_from_path'

    @staticmethod
    def _load_plugin_from_finder(name: str, finder: PathEntryFinderProtocol) -> tuple[ModuleType, type[Plugin]] | None:
        try:
            # set the full plugin module name, even for sideloaded plugins
            mod = exec_module(finder, f"streamlink.plugins.{name}", override=True)
        except ImportError as err:
            log.exception(f"Failed to load plugin {name} from {err.path}\n")
            return None

        if not hasattr(mod, "__plugin__") or not issubclass(mod.__plugin__, Plugin):
            return None

        return mod, mod.__plugin__


_RE_STRIP_JSON_COMMENTS = re.compile(rb"^(?:\s*//[^\n]*\n+)+")

_TListOfConstants: TypeAlias = "list[bool | int | float | str | None]"
_TConstantOrListOfConstants: TypeAlias = "bool | int | float | str | _TListOfConstants | None"
_TMappingOfConstantOrListOfConstants: TypeAlias = "dict[str, _TConstantOrListOfConstants]"


class _TPluginMatcherData(TypedDict):
    pattern: str
    flags: int | None
    priority: int | None
    name: str | None


class _TPluginArgumentData(TypedDict):
    name: str
    action: str | None
    nargs: int | Literal["*", "?", "+"] | None
    const: _TConstantOrListOfConstants
    default: _TConstantOrListOfConstants
    type: str | None
    type_args: _TListOfConstants | None
    type_kwargs: _TMappingOfConstantOrListOfConstants | None
    choices: _TListOfConstants | None
    required: bool | None
    help: str | None
    metavar: str | list[str] | None
    dest: str | None
    requires: str | list[str] | None
    prompt: str | None
    sensitive: bool | None
    argument_name: str | None


class _TPluginData(TypedDict):
    matchers: list[_TPluginMatcherData]
    arguments: list[_TPluginArgumentData]


class StreamlinkPluginsData:
    @classmethod
    def load(cls) -> tuple[dict[str, Matchers], dict[str, Arguments]] | None:
        # specific errors get logged, others are ignored intentionally
        with suppress(Exception):
            content = _PLUGINSDATA_PATH.read_bytes()

            cls._validate(content)

            return cls._parse(content)

        return None

    @staticmethod
    def _validate(content: bytes) -> None:
        # find plugins JSON checksum in package metadata
        # https://packaging.python.org/en/latest/specifications/recording-installed-packages/#the-record-file
        mode, filehash = next(
            (packagepath.hash.mode, packagepath.hash.value)
            for packagepath in importlib.metadata.files(_PLUGINSDATA_PACKAGENAME) or []
            if packagepath.hash is not None and packagepath.parts == _PLUGINSDATA_PACKAGEPATH
        )
        if mode not in hashlib.algorithms_guaranteed or not filehash:
            log.error("Unknown plugins data hash mode, falling back to loading all plugins")
            raise Exception

        # compare checksums
        hashalg = getattr(hashlib, mode)
        hashobj = hashalg(content)
        digest = base64.urlsafe_b64encode(hashobj.digest()).decode("utf-8").rstrip("=")
        if digest != filehash:
            log.error("Plugins data checksum mismatch, falling back to loading all plugins")
            raise Exception

    @classmethod
    def _parse(cls, content: bytes) -> tuple[dict[str, Matchers], dict[str, Arguments]]:
        content = _RE_STRIP_JSON_COMMENTS.sub(b"", content)
        data: dict[str, _TPluginData] = json.loads(content)

        try:
            matchers = cls._build_matchers(data)
        except Exception:
            log.exception("Error while loading pluginmatcher data from JSON")
            raise

        try:
            arguments = cls._build_arguments(data)
        except Exception:
            log.exception("Error while loading pluginargument data from JSON")
            raise

        return matchers, arguments

    @classmethod
    def _build_matchers(cls, data: dict[str, _TPluginData]) -> dict[str, Matchers]:
        res = {}
        for pluginname, plugindata in data.items():
            matchers = Matchers()
            for m in plugindata.get("matchers") or []:
                matcher = cls._build_matcher(m)
                matchers.add(matcher)

            res[pluginname] = matchers

        return res

    @staticmethod
    def _build_matcher(data: _TPluginMatcherData) -> Matcher:
        return Matcher(
            pattern=re.compile(data.get("pattern"), data.get("flags") or 0),
            priority=data.get("priority") or NORMAL_PRIORITY,
            name=data.get("name"),
        )

    @classmethod
    def _build_arguments(cls, data: dict[str, _TPluginData]) -> dict[str, Arguments]:
        res = {}
        for pluginname, plugindata in data.items():
            if not plugindata.get("arguments"):
                continue
            arguments = Arguments()
            for a in reversed(plugindata.get("arguments") or []):
                if argument := cls._build_argument(a):
                    arguments.add(argument)

            res[pluginname] = arguments

        return res

    @staticmethod
    def _build_argument(data: _TPluginArgumentData) -> Argument | None:
        name: str = data.get("name")  # type: ignore[assignment]
        type_data = data.get("type")
        if not type_data:
            argument_type = None
        elif argument_type := _PLUGINARGUMENT_TYPE_REGISTRY.get(type_data):
            type_args = data.get("type_args") or ()
            type_kwargs = data.get("type_kwargs") or {}
            if type_args or type_kwargs:
                argument_type = argument_type(*type_args, **type_kwargs)
        else:
            return None

        return Argument(
            name=name,
            action=data.get("action"),
            nargs=data.get("nargs"),
            const=data.get("const"),
            default=data.get("default"),
            type=argument_type,
            choices=data.get("choices"),
            required=data.get("required") or False,
            help=data.get("help"),
            metavar=data.get("metavar"),
            dest=data.get("dest"),
            requires=data.get("requires"),
            prompt=data.get("prompt"),
            sensitive=data.get("sensitive") or False,
            argument_name=data.get("argument_name"),
        )

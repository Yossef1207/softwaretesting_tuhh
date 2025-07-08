from __future__ import annotations

import json
import os
import shutil
import tempfile
from contextlib import suppress
from datetime import datetime
from pathlib import Path
from time import time
from typing import Any

from streamlink.compat import is_win32


if is_win32:
    xdg_cache = os.environ.get("APPDATA", os.path.expanduser("~"))
else:
    xdg_cache = os.environ.get("XDG_CACHE_HOME", os.path.expanduser("~/.cache"))

# TODO: fix macOS path and deprecate old one (with fallback logic)
CACHE_DIR = Path(xdg_cache) / "streamlink"
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


# TODO: rewrite data structure
#  - replace prefix logic with namespaces
#  - change timestamps from (timezoned) epoch values to ISO8601 strings (UTC)
#  - add JSON schema information
#  - add translation logic, to keep backwards compatibility
class Cache:
    def xǁCacheǁ__init____mutmut_orig(
        self,
        filename: str | Path,
        key_prefix: str = "",
    ):
        """
        Caches Python values as JSON and prunes expired entries.

        :param filename: A file name or :class:`Path` object, relative to the cache directory
        :param key_prefix: Optional prefix for each key to be retrieved from or stored in the cache
        """

        self.key_prefix = key_prefix
        self.filename = CACHE_DIR / Path(filename)

        self._cache: dict[str, dict[str, Any]] = {}
    def xǁCacheǁ__init____mutmut_1(
        self,
        filename: str | Path,
        key_prefix: str = "XXXX",
    ):
        """
        Caches Python values as JSON and prunes expired entries.

        :param filename: A file name or :class:`Path` object, relative to the cache directory
        :param key_prefix: Optional prefix for each key to be retrieved from or stored in the cache
        """

        self.key_prefix = key_prefix
        self.filename = CACHE_DIR / Path(filename)

        self._cache: dict[str, dict[str, Any]] = {}
    def xǁCacheǁ__init____mutmut_2(
        self,
        filename: str | Path,
        key_prefix: str = "",
    ):
        """
        Caches Python values as JSON and prunes expired entries.

        :param filename: A file name or :class:`Path` object, relative to the cache directory
        :param key_prefix: Optional prefix for each key to be retrieved from or stored in the cache
        """

        self.key_prefix = None
        self.filename = CACHE_DIR / Path(filename)

        self._cache: dict[str, dict[str, Any]] = {}
    def xǁCacheǁ__init____mutmut_3(
        self,
        filename: str | Path,
        key_prefix: str = "",
    ):
        """
        Caches Python values as JSON and prunes expired entries.

        :param filename: A file name or :class:`Path` object, relative to the cache directory
        :param key_prefix: Optional prefix for each key to be retrieved from or stored in the cache
        """

        self.key_prefix = key_prefix
        self.filename = None

        self._cache: dict[str, dict[str, Any]] = {}
    def xǁCacheǁ__init____mutmut_4(
        self,
        filename: str | Path,
        key_prefix: str = "",
    ):
        """
        Caches Python values as JSON and prunes expired entries.

        :param filename: A file name or :class:`Path` object, relative to the cache directory
        :param key_prefix: Optional prefix for each key to be retrieved from or stored in the cache
        """

        self.key_prefix = key_prefix
        self.filename = CACHE_DIR * Path(filename)

        self._cache: dict[str, dict[str, Any]] = {}
    def xǁCacheǁ__init____mutmut_5(
        self,
        filename: str | Path,
        key_prefix: str = "",
    ):
        """
        Caches Python values as JSON and prunes expired entries.

        :param filename: A file name or :class:`Path` object, relative to the cache directory
        :param key_prefix: Optional prefix for each key to be retrieved from or stored in the cache
        """

        self.key_prefix = key_prefix
        self.filename = CACHE_DIR / Path(None)

        self._cache: dict[str, dict[str, Any]] = {}
    def xǁCacheǁ__init____mutmut_6(
        self,
        filename: str | Path,
        key_prefix: str = "",
    ):
        """
        Caches Python values as JSON and prunes expired entries.

        :param filename: A file name or :class:`Path` object, relative to the cache directory
        :param key_prefix: Optional prefix for each key to be retrieved from or stored in the cache
        """

        self.key_prefix = key_prefix
        self.filename = CACHE_DIR / Path(filename)

        self._cache: dict[str, dict[str, Any]] = None
    
    xǁCacheǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCacheǁ__init____mutmut_1': xǁCacheǁ__init____mutmut_1, 
        'xǁCacheǁ__init____mutmut_2': xǁCacheǁ__init____mutmut_2, 
        'xǁCacheǁ__init____mutmut_3': xǁCacheǁ__init____mutmut_3, 
        'xǁCacheǁ__init____mutmut_4': xǁCacheǁ__init____mutmut_4, 
        'xǁCacheǁ__init____mutmut_5': xǁCacheǁ__init____mutmut_5, 
        'xǁCacheǁ__init____mutmut_6': xǁCacheǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCacheǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCacheǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCacheǁ__init____mutmut_orig)
    xǁCacheǁ__init____mutmut_orig.__name__ = 'xǁCacheǁ__init__'

    def xǁCacheǁ_load__mutmut_orig(self):
        self._cache = {}
        if self.filename.exists():
            with suppress(Exception):
                with self.filename.open("r") as fd:
                    data = json.load(fd)
                    self._cache.update(**data)

    def xǁCacheǁ_load__mutmut_1(self):
        self._cache = None
        if self.filename.exists():
            with suppress(Exception):
                with self.filename.open("r") as fd:
                    data = json.load(fd)
                    self._cache.update(**data)

    def xǁCacheǁ_load__mutmut_2(self):
        self._cache = {}
        if self.filename.exists():
            with suppress(None):
                with self.filename.open("r") as fd:
                    data = json.load(fd)
                    self._cache.update(**data)

    def xǁCacheǁ_load__mutmut_3(self):
        self._cache = {}
        if self.filename.exists():
            with suppress(Exception):
                with self.filename.open(None) as fd:
                    data = json.load(fd)
                    self._cache.update(**data)

    def xǁCacheǁ_load__mutmut_4(self):
        self._cache = {}
        if self.filename.exists():
            with suppress(Exception):
                with self.filename.open("XXrXX") as fd:
                    data = json.load(fd)
                    self._cache.update(**data)

    def xǁCacheǁ_load__mutmut_5(self):
        self._cache = {}
        if self.filename.exists():
            with suppress(Exception):
                with self.filename.open("R") as fd:
                    data = json.load(fd)
                    self._cache.update(**data)

    def xǁCacheǁ_load__mutmut_6(self):
        self._cache = {}
        if self.filename.exists():
            with suppress(Exception):
                with self.filename.open("R") as fd:
                    data = json.load(fd)
                    self._cache.update(**data)

    def xǁCacheǁ_load__mutmut_7(self):
        self._cache = {}
        if self.filename.exists():
            with suppress(Exception):
                with self.filename.open("r") as fd:
                    data = None
                    self._cache.update(**data)

    def xǁCacheǁ_load__mutmut_8(self):
        self._cache = {}
        if self.filename.exists():
            with suppress(Exception):
                with self.filename.open("r") as fd:
                    data = json.load(None)
                    self._cache.update(**data)
    
    xǁCacheǁ_load__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCacheǁ_load__mutmut_1': xǁCacheǁ_load__mutmut_1, 
        'xǁCacheǁ_load__mutmut_2': xǁCacheǁ_load__mutmut_2, 
        'xǁCacheǁ_load__mutmut_3': xǁCacheǁ_load__mutmut_3, 
        'xǁCacheǁ_load__mutmut_4': xǁCacheǁ_load__mutmut_4, 
        'xǁCacheǁ_load__mutmut_5': xǁCacheǁ_load__mutmut_5, 
        'xǁCacheǁ_load__mutmut_6': xǁCacheǁ_load__mutmut_6, 
        'xǁCacheǁ_load__mutmut_7': xǁCacheǁ_load__mutmut_7, 
        'xǁCacheǁ_load__mutmut_8': xǁCacheǁ_load__mutmut_8
    }
    
    def _load(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCacheǁ_load__mutmut_orig"), object.__getattribute__(self, "xǁCacheǁ_load__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _load.__signature__ = _mutmut_signature(xǁCacheǁ_load__mutmut_orig)
    xǁCacheǁ_load__mutmut_orig.__name__ = 'xǁCacheǁ_load'

    def xǁCacheǁ_prune__mutmut_orig(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_1(self):
        now = None
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_2(self):
        now = time()
        pruned = None

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_3(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = None
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_4(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get(None, now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_5(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", None)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_6(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get(now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_7(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", )
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_8(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("XXexpiresXX", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_9(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("EXPIRES", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_10(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("Expires", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_11(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires < now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_12(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires <= now:
                pruned.append(None)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_13(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(None, None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_14(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(None)

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_15(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, )

        return len(pruned) > 0

    def xǁCacheǁ_prune__mutmut_16(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) >= 0

    def xǁCacheǁ_prune__mutmut_17(self):
        now = time()
        pruned = []

        for key, value in self._cache.items():
            expires = value.get("expires", now)
            if expires <= now:
                pruned.append(key)

        for key in pruned:
            self._cache.pop(key, None)

        return len(pruned) > 1
    
    xǁCacheǁ_prune__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCacheǁ_prune__mutmut_1': xǁCacheǁ_prune__mutmut_1, 
        'xǁCacheǁ_prune__mutmut_2': xǁCacheǁ_prune__mutmut_2, 
        'xǁCacheǁ_prune__mutmut_3': xǁCacheǁ_prune__mutmut_3, 
        'xǁCacheǁ_prune__mutmut_4': xǁCacheǁ_prune__mutmut_4, 
        'xǁCacheǁ_prune__mutmut_5': xǁCacheǁ_prune__mutmut_5, 
        'xǁCacheǁ_prune__mutmut_6': xǁCacheǁ_prune__mutmut_6, 
        'xǁCacheǁ_prune__mutmut_7': xǁCacheǁ_prune__mutmut_7, 
        'xǁCacheǁ_prune__mutmut_8': xǁCacheǁ_prune__mutmut_8, 
        'xǁCacheǁ_prune__mutmut_9': xǁCacheǁ_prune__mutmut_9, 
        'xǁCacheǁ_prune__mutmut_10': xǁCacheǁ_prune__mutmut_10, 
        'xǁCacheǁ_prune__mutmut_11': xǁCacheǁ_prune__mutmut_11, 
        'xǁCacheǁ_prune__mutmut_12': xǁCacheǁ_prune__mutmut_12, 
        'xǁCacheǁ_prune__mutmut_13': xǁCacheǁ_prune__mutmut_13, 
        'xǁCacheǁ_prune__mutmut_14': xǁCacheǁ_prune__mutmut_14, 
        'xǁCacheǁ_prune__mutmut_15': xǁCacheǁ_prune__mutmut_15, 
        'xǁCacheǁ_prune__mutmut_16': xǁCacheǁ_prune__mutmut_16, 
        'xǁCacheǁ_prune__mutmut_17': xǁCacheǁ_prune__mutmut_17
    }
    
    def _prune(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCacheǁ_prune__mutmut_orig"), object.__getattribute__(self, "xǁCacheǁ_prune__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _prune.__signature__ = _mutmut_signature(xǁCacheǁ_prune__mutmut_orig)
    xǁCacheǁ_prune__mutmut_orig.__name__ = 'xǁCacheǁ_prune'

    def xǁCacheǁ_save__mutmut_orig(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_1(self):
        fd, tempname = None
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_2(self):
        fd, tempname = tempfile.mkstemp()
        fd = None
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_3(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(None, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_4(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, None)
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_5(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen("w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_6(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, )
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_7(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "XXwXX")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_8(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "W")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_9(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "W")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_10(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(None, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_11(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, None, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_12(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=None, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_13(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=None)
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_14(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_15(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_16(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_17(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, )
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_18(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=3, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_19(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=("XX,XX", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_20(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", "XX: XX"))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_21(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=None, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_22(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=None)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_23(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_24(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, )
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_25(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=False, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_26(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=False)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_27(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(None, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_28(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, None)
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_29(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_30(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, )
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_31(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(None))
        except OSError:
            with suppress(Exception):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_32(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(None):
                os.remove(tempname)

    def xǁCacheǁ_save__mutmut_33(self):
        fd, tempname = tempfile.mkstemp()
        fd = os.fdopen(fd, "w")
        try:
            json.dump(self._cache, fd, indent=2, separators=(",", ": "))
        except Exception:
            raise
        finally:
            fd.close()

        # Silently ignore errors
        try:
            self.filename.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(tempname, str(self.filename))
        except OSError:
            with suppress(Exception):
                os.remove(None)
    
    xǁCacheǁ_save__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCacheǁ_save__mutmut_1': xǁCacheǁ_save__mutmut_1, 
        'xǁCacheǁ_save__mutmut_2': xǁCacheǁ_save__mutmut_2, 
        'xǁCacheǁ_save__mutmut_3': xǁCacheǁ_save__mutmut_3, 
        'xǁCacheǁ_save__mutmut_4': xǁCacheǁ_save__mutmut_4, 
        'xǁCacheǁ_save__mutmut_5': xǁCacheǁ_save__mutmut_5, 
        'xǁCacheǁ_save__mutmut_6': xǁCacheǁ_save__mutmut_6, 
        'xǁCacheǁ_save__mutmut_7': xǁCacheǁ_save__mutmut_7, 
        'xǁCacheǁ_save__mutmut_8': xǁCacheǁ_save__mutmut_8, 
        'xǁCacheǁ_save__mutmut_9': xǁCacheǁ_save__mutmut_9, 
        'xǁCacheǁ_save__mutmut_10': xǁCacheǁ_save__mutmut_10, 
        'xǁCacheǁ_save__mutmut_11': xǁCacheǁ_save__mutmut_11, 
        'xǁCacheǁ_save__mutmut_12': xǁCacheǁ_save__mutmut_12, 
        'xǁCacheǁ_save__mutmut_13': xǁCacheǁ_save__mutmut_13, 
        'xǁCacheǁ_save__mutmut_14': xǁCacheǁ_save__mutmut_14, 
        'xǁCacheǁ_save__mutmut_15': xǁCacheǁ_save__mutmut_15, 
        'xǁCacheǁ_save__mutmut_16': xǁCacheǁ_save__mutmut_16, 
        'xǁCacheǁ_save__mutmut_17': xǁCacheǁ_save__mutmut_17, 
        'xǁCacheǁ_save__mutmut_18': xǁCacheǁ_save__mutmut_18, 
        'xǁCacheǁ_save__mutmut_19': xǁCacheǁ_save__mutmut_19, 
        'xǁCacheǁ_save__mutmut_20': xǁCacheǁ_save__mutmut_20, 
        'xǁCacheǁ_save__mutmut_21': xǁCacheǁ_save__mutmut_21, 
        'xǁCacheǁ_save__mutmut_22': xǁCacheǁ_save__mutmut_22, 
        'xǁCacheǁ_save__mutmut_23': xǁCacheǁ_save__mutmut_23, 
        'xǁCacheǁ_save__mutmut_24': xǁCacheǁ_save__mutmut_24, 
        'xǁCacheǁ_save__mutmut_25': xǁCacheǁ_save__mutmut_25, 
        'xǁCacheǁ_save__mutmut_26': xǁCacheǁ_save__mutmut_26, 
        'xǁCacheǁ_save__mutmut_27': xǁCacheǁ_save__mutmut_27, 
        'xǁCacheǁ_save__mutmut_28': xǁCacheǁ_save__mutmut_28, 
        'xǁCacheǁ_save__mutmut_29': xǁCacheǁ_save__mutmut_29, 
        'xǁCacheǁ_save__mutmut_30': xǁCacheǁ_save__mutmut_30, 
        'xǁCacheǁ_save__mutmut_31': xǁCacheǁ_save__mutmut_31, 
        'xǁCacheǁ_save__mutmut_32': xǁCacheǁ_save__mutmut_32, 
        'xǁCacheǁ_save__mutmut_33': xǁCacheǁ_save__mutmut_33
    }
    
    def _save(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCacheǁ_save__mutmut_orig"), object.__getattribute__(self, "xǁCacheǁ_save__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _save.__signature__ = _mutmut_signature(xǁCacheǁ_save__mutmut_orig)
    xǁCacheǁ_save__mutmut_orig.__name__ = 'xǁCacheǁ_save'

    def xǁCacheǁset__mutmut_orig(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=value, expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_1(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = None

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=value, expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_2(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is not None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=value, expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_3(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires = time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=value, expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_4(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires -= time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=value, expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_5(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = None
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=value, expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_6(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = None

        self._cache[key] = dict(value=value, expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_7(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 1

        self._cache[key] = dict(value=value, expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_8(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = None
        self._save()

    def xǁCacheǁset__mutmut_9(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(valueXX=value, expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_10(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=value, expiresXX=expires)
        self._save()

    def xǁCacheǁset__mutmut_11(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=None, expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_12(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=value, expires=None)
        self._save()

    def xǁCacheǁset__mutmut_13(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(expires=expires)
        self._save()

    def xǁCacheǁset__mutmut_14(
        self,
        key: str,
        value: Any,
        expires: float = 60 * 60 * 24 * 7,
        expires_at: datetime | None = None,
    ) -> None:
        """
        Store the given value using the key name and expiration time.

        Prunes the cache of all expired key-value pairs before setting the new key-value pair.

        :param key: A specific key name
        :param value: Any kind of value that can be JSON-serialized
        :param expires: Expiration time in seconds, with the default being one week
        :param expires_at: Optional expiration date, which overrides the expiration time
        """

        self._load()
        self._prune()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if expires_at is None:
            expires += time()
        else:
            try:
                expires = expires_at.timestamp()
            except OverflowError:
                expires = 0

        self._cache[key] = dict(value=value, )
        self._save()
    
    xǁCacheǁset__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCacheǁset__mutmut_1': xǁCacheǁset__mutmut_1, 
        'xǁCacheǁset__mutmut_2': xǁCacheǁset__mutmut_2, 
        'xǁCacheǁset__mutmut_3': xǁCacheǁset__mutmut_3, 
        'xǁCacheǁset__mutmut_4': xǁCacheǁset__mutmut_4, 
        'xǁCacheǁset__mutmut_5': xǁCacheǁset__mutmut_5, 
        'xǁCacheǁset__mutmut_6': xǁCacheǁset__mutmut_6, 
        'xǁCacheǁset__mutmut_7': xǁCacheǁset__mutmut_7, 
        'xǁCacheǁset__mutmut_8': xǁCacheǁset__mutmut_8, 
        'xǁCacheǁset__mutmut_9': xǁCacheǁset__mutmut_9, 
        'xǁCacheǁset__mutmut_10': xǁCacheǁset__mutmut_10, 
        'xǁCacheǁset__mutmut_11': xǁCacheǁset__mutmut_11, 
        'xǁCacheǁset__mutmut_12': xǁCacheǁset__mutmut_12, 
        'xǁCacheǁset__mutmut_13': xǁCacheǁset__mutmut_13, 
        'xǁCacheǁset__mutmut_14': xǁCacheǁset__mutmut_14
    }
    
    def set(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCacheǁset__mutmut_orig"), object.__getattribute__(self, "xǁCacheǁset__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set.__signature__ = _mutmut_signature(xǁCacheǁset__mutmut_orig)
    xǁCacheǁset__mutmut_orig.__name__ = 'xǁCacheǁset'

    def xǁCacheǁget__mutmut_orig(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if key in self._cache and "value" in self._cache[key]:
            return self._cache[key]["value"]
        else:
            return default

    def xǁCacheǁget__mutmut_1(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = None

        if key in self._cache and "value" in self._cache[key]:
            return self._cache[key]["value"]
        else:
            return default

    def xǁCacheǁget__mutmut_2(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if key not in self._cache and "value" in self._cache[key]:
            return self._cache[key]["value"]
        else:
            return default

    def xǁCacheǁget__mutmut_3(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if key in self._cache or "value" in self._cache[key]:
            return self._cache[key]["value"]
        else:
            return default

    def xǁCacheǁget__mutmut_4(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if key in self._cache and "XXvalueXX" in self._cache[key]:
            return self._cache[key]["value"]
        else:
            return default

    def xǁCacheǁget__mutmut_5(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if key in self._cache and "VALUE" in self._cache[key]:
            return self._cache[key]["value"]
        else:
            return default

    def xǁCacheǁget__mutmut_6(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if key in self._cache and "Value" in self._cache[key]:
            return self._cache[key]["value"]
        else:
            return default

    def xǁCacheǁget__mutmut_7(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if key in self._cache and "value" not in self._cache[key]:
            return self._cache[key]["value"]
        else:
            return default

    def xǁCacheǁget__mutmut_8(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if key in self._cache and "value" in self._cache[key]:
            return self._cache[key]["XXvalueXX"]
        else:
            return default

    def xǁCacheǁget__mutmut_9(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if key in self._cache and "value" in self._cache[key]:
            return self._cache[key]["VALUE"]
        else:
            return default

    def xǁCacheǁget__mutmut_10(
        self,
        key: str,
        default: Any | None = None,
    ) -> Any:
        """
        Attempt to retrieve the given key from the cache.

        Prunes the cache of all expired key-value pairs before retrieving the key's value.

        :param key: A specific key name
        :param default: An optional default value if no key was stored, or if it has expired
        :return: The retrieved value or optional default value
        """

        self._load()

        if self._prune():
            self._save()

        if self.key_prefix:
            key = f"{self.key_prefix}:{key}"

        if key in self._cache and "value" in self._cache[key]:
            return self._cache[key]["Value"]
        else:
            return default
    
    xǁCacheǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCacheǁget__mutmut_1': xǁCacheǁget__mutmut_1, 
        'xǁCacheǁget__mutmut_2': xǁCacheǁget__mutmut_2, 
        'xǁCacheǁget__mutmut_3': xǁCacheǁget__mutmut_3, 
        'xǁCacheǁget__mutmut_4': xǁCacheǁget__mutmut_4, 
        'xǁCacheǁget__mutmut_5': xǁCacheǁget__mutmut_5, 
        'xǁCacheǁget__mutmut_6': xǁCacheǁget__mutmut_6, 
        'xǁCacheǁget__mutmut_7': xǁCacheǁget__mutmut_7, 
        'xǁCacheǁget__mutmut_8': xǁCacheǁget__mutmut_8, 
        'xǁCacheǁget__mutmut_9': xǁCacheǁget__mutmut_9, 
        'xǁCacheǁget__mutmut_10': xǁCacheǁget__mutmut_10
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCacheǁget__mutmut_orig"), object.__getattribute__(self, "xǁCacheǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁCacheǁget__mutmut_orig)
    xǁCacheǁget__mutmut_orig.__name__ = 'xǁCacheǁget'

    def xǁCacheǁget_all__mutmut_orig(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = f"{self.key_prefix}:"
            else:
                prefix = ""
            if key.startswith(prefix):
                okey = key[len(prefix) :]
                ret[okey] = value["value"]

        return ret

    def xǁCacheǁget_all__mutmut_1(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = None
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = f"{self.key_prefix}:"
            else:
                prefix = ""
            if key.startswith(prefix):
                okey = key[len(prefix) :]
                ret[okey] = value["value"]

        return ret

    def xǁCacheǁget_all__mutmut_2(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = None
            else:
                prefix = ""
            if key.startswith(prefix):
                okey = key[len(prefix) :]
                ret[okey] = value["value"]

        return ret

    def xǁCacheǁget_all__mutmut_3(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = f"{self.key_prefix}:"
            else:
                prefix = None
            if key.startswith(prefix):
                okey = key[len(prefix) :]
                ret[okey] = value["value"]

        return ret

    def xǁCacheǁget_all__mutmut_4(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = f"{self.key_prefix}:"
            else:
                prefix = "XXXX"
            if key.startswith(prefix):
                okey = key[len(prefix) :]
                ret[okey] = value["value"]

        return ret

    def xǁCacheǁget_all__mutmut_5(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = f"{self.key_prefix}:"
            else:
                prefix = ""
            if key.startswith(None):
                okey = key[len(prefix) :]
                ret[okey] = value["value"]

        return ret

    def xǁCacheǁget_all__mutmut_6(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = f"{self.key_prefix}:"
            else:
                prefix = ""
            if key.startswith(prefix):
                okey = None
                ret[okey] = value["value"]

        return ret

    def xǁCacheǁget_all__mutmut_7(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = f"{self.key_prefix}:"
            else:
                prefix = ""
            if key.startswith(prefix):
                okey = key[len(prefix) :]
                ret[okey] = None

        return ret

    def xǁCacheǁget_all__mutmut_8(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = f"{self.key_prefix}:"
            else:
                prefix = ""
            if key.startswith(prefix):
                okey = key[len(prefix) :]
                ret[okey] = value["XXvalueXX"]

        return ret

    def xǁCacheǁget_all__mutmut_9(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = f"{self.key_prefix}:"
            else:
                prefix = ""
            if key.startswith(prefix):
                okey = key[len(prefix) :]
                ret[okey] = value["VALUE"]

        return ret

    def xǁCacheǁget_all__mutmut_10(self) -> dict[str, Any]:
        """
        Retrieve all cached key-value pairs.

        Prunes the cache of all expired key-value pairs first.

        :return: A dictionary of all cached key-value pairs.
        """

        ret = {}
        self._load()

        if self._prune():
            self._save()

        for key, value in self._cache.items():
            if self.key_prefix:
                prefix = f"{self.key_prefix}:"
            else:
                prefix = ""
            if key.startswith(prefix):
                okey = key[len(prefix) :]
                ret[okey] = value["Value"]

        return ret
    
    xǁCacheǁget_all__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCacheǁget_all__mutmut_1': xǁCacheǁget_all__mutmut_1, 
        'xǁCacheǁget_all__mutmut_2': xǁCacheǁget_all__mutmut_2, 
        'xǁCacheǁget_all__mutmut_3': xǁCacheǁget_all__mutmut_3, 
        'xǁCacheǁget_all__mutmut_4': xǁCacheǁget_all__mutmut_4, 
        'xǁCacheǁget_all__mutmut_5': xǁCacheǁget_all__mutmut_5, 
        'xǁCacheǁget_all__mutmut_6': xǁCacheǁget_all__mutmut_6, 
        'xǁCacheǁget_all__mutmut_7': xǁCacheǁget_all__mutmut_7, 
        'xǁCacheǁget_all__mutmut_8': xǁCacheǁget_all__mutmut_8, 
        'xǁCacheǁget_all__mutmut_9': xǁCacheǁget_all__mutmut_9, 
        'xǁCacheǁget_all__mutmut_10': xǁCacheǁget_all__mutmut_10
    }
    
    def get_all(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCacheǁget_all__mutmut_orig"), object.__getattribute__(self, "xǁCacheǁget_all__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_all.__signature__ = _mutmut_signature(xǁCacheǁget_all__mutmut_orig)
    xǁCacheǁget_all__mutmut_orig.__name__ = 'xǁCacheǁget_all'


__all__ = ["Cache"]

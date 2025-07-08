from __future__ import annotations

import sys
from importlib.machinery import FileFinder
from importlib.util import module_from_spec
from pathlib import Path
from pkgutil import get_importer
from types import ModuleType
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from _typeshed.importlib import PathEntryFinderProtocol
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


def x_get_finder__mutmut_orig(path: str | Path) -> PathEntryFinderProtocol:
    path = str(path)
    finder = get_importer(path)
    if not finder:
        raise ImportError(f"Not a package path: {path}", path=path)

    return finder


def x_get_finder__mutmut_1(path: str | Path) -> PathEntryFinderProtocol:
    path = None
    finder = get_importer(path)
    if not finder:
        raise ImportError(f"Not a package path: {path}", path=path)

    return finder


def x_get_finder__mutmut_2(path: str | Path) -> PathEntryFinderProtocol:
    path = str(None)
    finder = get_importer(path)
    if not finder:
        raise ImportError(f"Not a package path: {path}", path=path)

    return finder


def x_get_finder__mutmut_3(path: str | Path) -> PathEntryFinderProtocol:
    path = str(path)
    finder = None
    if not finder:
        raise ImportError(f"Not a package path: {path}", path=path)

    return finder


def x_get_finder__mutmut_4(path: str | Path) -> PathEntryFinderProtocol:
    path = str(path)
    finder = get_importer(None)
    if not finder:
        raise ImportError(f"Not a package path: {path}", path=path)

    return finder


def x_get_finder__mutmut_5(path: str | Path) -> PathEntryFinderProtocol:
    path = str(path)
    finder = get_importer(path)
    if finder:
        raise ImportError(f"Not a package path: {path}", path=path)

    return finder


def x_get_finder__mutmut_6(path: str | Path) -> PathEntryFinderProtocol:
    path = str(path)
    finder = get_importer(path)
    if not finder:
        raise ImportError(None, path=path)

    return finder


def x_get_finder__mutmut_7(path: str | Path) -> PathEntryFinderProtocol:
    path = str(path)
    finder = get_importer(path)
    if not finder:
        raise ImportError(f"Not a package path: {path}", path=None)

    return finder


def x_get_finder__mutmut_8(path: str | Path) -> PathEntryFinderProtocol:
    path = str(path)
    finder = get_importer(path)
    if not finder:
        raise ImportError(path=path)

    return finder


def x_get_finder__mutmut_9(path: str | Path) -> PathEntryFinderProtocol:
    path = str(path)
    finder = get_importer(path)
    if not finder:
        raise ImportError(f"Not a package path: {path}", )

    return finder

x_get_finder__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_finder__mutmut_1': x_get_finder__mutmut_1, 
    'x_get_finder__mutmut_2': x_get_finder__mutmut_2, 
    'x_get_finder__mutmut_3': x_get_finder__mutmut_3, 
    'x_get_finder__mutmut_4': x_get_finder__mutmut_4, 
    'x_get_finder__mutmut_5': x_get_finder__mutmut_5, 
    'x_get_finder__mutmut_6': x_get_finder__mutmut_6, 
    'x_get_finder__mutmut_7': x_get_finder__mutmut_7, 
    'x_get_finder__mutmut_8': x_get_finder__mutmut_8, 
    'x_get_finder__mutmut_9': x_get_finder__mutmut_9
}

def get_finder(*args, **kwargs):
    result = _mutmut_trampoline(x_get_finder__mutmut_orig, x_get_finder__mutmut_mutants, args, kwargs)
    return result 

get_finder.__signature__ = _mutmut_signature(x_get_finder__mutmut_orig)
x_get_finder__mutmut_orig.__name__ = 'x_get_finder'


def x_load_module__mutmut_orig(name: str, path: str | Path, override: bool = False) -> ModuleType:
    finder = get_finder(path)

    return exec_module(finder, name, override)


def x_load_module__mutmut_1(name: str, path: str | Path, override: bool = True) -> ModuleType:
    finder = get_finder(path)

    return exec_module(finder, name, override)


def x_load_module__mutmut_2(name: str, path: str | Path, override: bool = False) -> ModuleType:
    finder = None

    return exec_module(finder, name, override)


def x_load_module__mutmut_3(name: str, path: str | Path, override: bool = False) -> ModuleType:
    finder = get_finder(None)

    return exec_module(finder, name, override)


def x_load_module__mutmut_4(name: str, path: str | Path, override: bool = False) -> ModuleType:
    finder = get_finder(path)

    return exec_module(None, name, override)


def x_load_module__mutmut_5(name: str, path: str | Path, override: bool = False) -> ModuleType:
    finder = get_finder(path)

    return exec_module(finder, None, override)


def x_load_module__mutmut_6(name: str, path: str | Path, override: bool = False) -> ModuleType:
    finder = get_finder(path)

    return exec_module(finder, name, None)


def x_load_module__mutmut_7(name: str, path: str | Path, override: bool = False) -> ModuleType:
    finder = get_finder(path)

    return exec_module(name, override)


def x_load_module__mutmut_8(name: str, path: str | Path, override: bool = False) -> ModuleType:
    finder = get_finder(path)

    return exec_module(finder, override)


def x_load_module__mutmut_9(name: str, path: str | Path, override: bool = False) -> ModuleType:
    finder = get_finder(path)

    return exec_module(finder, name, )

x_load_module__mutmut_mutants : ClassVar[MutantDict] = {
'x_load_module__mutmut_1': x_load_module__mutmut_1, 
    'x_load_module__mutmut_2': x_load_module__mutmut_2, 
    'x_load_module__mutmut_3': x_load_module__mutmut_3, 
    'x_load_module__mutmut_4': x_load_module__mutmut_4, 
    'x_load_module__mutmut_5': x_load_module__mutmut_5, 
    'x_load_module__mutmut_6': x_load_module__mutmut_6, 
    'x_load_module__mutmut_7': x_load_module__mutmut_7, 
    'x_load_module__mutmut_8': x_load_module__mutmut_8, 
    'x_load_module__mutmut_9': x_load_module__mutmut_9
}

def load_module(*args, **kwargs):
    result = _mutmut_trampoline(x_load_module__mutmut_orig, x_load_module__mutmut_mutants, args, kwargs)
    return result 

load_module.__signature__ = _mutmut_signature(x_load_module__mutmut_orig)
x_load_module__mutmut_orig.__name__ = 'x_load_module'


def x_exec_module__mutmut_orig(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_1(finder: PathEntryFinderProtocol, name: str, override: bool = True) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_2(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = None
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_3(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(None)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_4(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_5(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec and not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_6(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_7(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            None,
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_8(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=None,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_9(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_10(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_11(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_12(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_13(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_14(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override or (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_15(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(None)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_16(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_17(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(None)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_18(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = None
    spec.loader.exec_module(mod)

    return mod


def x_exec_module__mutmut_19(finder: PathEntryFinderProtocol, name: str, override: bool = False) -> ModuleType:
    spec = finder.find_spec(name)
    if not spec or not spec.loader:
        raise ImportError(
            f"No module named '{name}'",
            name=name,
            path=finder.path if isinstance(finder, FileFinder) else None,
        )

    if not override and (mod := sys.modules.get(spec.name)):
        return mod

    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(None)

    return mod

x_exec_module__mutmut_mutants : ClassVar[MutantDict] = {
'x_exec_module__mutmut_1': x_exec_module__mutmut_1, 
    'x_exec_module__mutmut_2': x_exec_module__mutmut_2, 
    'x_exec_module__mutmut_3': x_exec_module__mutmut_3, 
    'x_exec_module__mutmut_4': x_exec_module__mutmut_4, 
    'x_exec_module__mutmut_5': x_exec_module__mutmut_5, 
    'x_exec_module__mutmut_6': x_exec_module__mutmut_6, 
    'x_exec_module__mutmut_7': x_exec_module__mutmut_7, 
    'x_exec_module__mutmut_8': x_exec_module__mutmut_8, 
    'x_exec_module__mutmut_9': x_exec_module__mutmut_9, 
    'x_exec_module__mutmut_10': x_exec_module__mutmut_10, 
    'x_exec_module__mutmut_11': x_exec_module__mutmut_11, 
    'x_exec_module__mutmut_12': x_exec_module__mutmut_12, 
    'x_exec_module__mutmut_13': x_exec_module__mutmut_13, 
    'x_exec_module__mutmut_14': x_exec_module__mutmut_14, 
    'x_exec_module__mutmut_15': x_exec_module__mutmut_15, 
    'x_exec_module__mutmut_16': x_exec_module__mutmut_16, 
    'x_exec_module__mutmut_17': x_exec_module__mutmut_17, 
    'x_exec_module__mutmut_18': x_exec_module__mutmut_18, 
    'x_exec_module__mutmut_19': x_exec_module__mutmut_19
}

def exec_module(*args, **kwargs):
    result = _mutmut_trampoline(x_exec_module__mutmut_orig, x_exec_module__mutmut_mutants, args, kwargs)
    return result 

exec_module.__signature__ = _mutmut_signature(x_exec_module__mutmut_orig)
x_exec_module__mutmut_orig.__name__ = 'x_exec_module'

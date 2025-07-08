from __future__ import annotations

import importlib
import inspect
import os
import sys
import warnings
from collections.abc import Callable, Mapping
from typing import Any


try:
    from builtins import BaseExceptionGroup, ExceptionGroup  # type: ignore[attr-defined]
except ImportError:  # pragma: no cover
    from exceptiongroup import BaseExceptionGroup, ExceptionGroup  # type: ignore[import]


from streamlink.exceptions import StreamlinkDeprecationWarning


# compatibility import of charset_normalizer/chardet via requests<3.0
try:
    from requests.compat import chardet as charset_normalizer  # type: ignore
except ImportError:  # pragma: no cover
    import charset_normalizer


is_darwin = sys.platform == "darwin"
is_win32 = os.name == "nt"


detect_encoding = charset_normalizer.detect
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


def x_deprecated__mutmut_orig(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_1(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = None
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_2(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[2].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_3(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = None

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_4(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get(None, None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_5(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get(None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_6(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", )

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_7(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("XX__getattr__XX", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_8(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__GETATTR__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_9(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name not in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_10(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = None
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_11(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['XX__spec__XX'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_12(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__SPEC__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_13(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = None
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_14(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                None,
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_15(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                None,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_16(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=None,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_17(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_18(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_19(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_20(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg and f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_21(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=3,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_22(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = None
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_23(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(None)
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_24(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.rsplit(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_25(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split("XX.XX")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_26(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = None
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_27(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(None)
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_28(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(None))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_29(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module("XX.XX".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_30(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = None

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_31(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(None, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_32(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, None, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_33(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_34(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_35(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, )

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_36(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_37(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(None)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_38(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = None

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_39(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["XX__getattr__XX"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_40(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__GETATTR__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_41(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() & [deprecated.__name__]:
        if item in mod_globals:
            del mod_globals[item]


def x_deprecated__mutmut_42(items: Mapping[str, tuple[str | None, Any, Any]]) -> None:
    """
    Deprecate specific module attributes.

    This removes the deprecated attributes from the module's global context,
    adds/overrides the module's :func:`__getattr__` function, and emits a :class:`StreamlinkDeprecationWarning`
    if one of the deprecated attributes is accessed.

    :param items: A mapping of module attribute names to tuples which contain the following optional items:
                  1. an import path string (for looking up an external object while accessing the attribute)
                  2. a direct return object (if no import path was set)
                  3. a custom warning message
    """

    mod_globals = inspect.stack()[1].frame.f_globals
    orig_getattr: Callable[[str], Any] | None = mod_globals.get("__getattr__", None)

    def __getattr__(name: str) -> Any:
        if name in items:
            origin = f"{mod_globals['__spec__'].name}.{name}"
            path, obj, msg = items[name]
            warnings.warn(
                msg or f"'{origin}' has been deprecated",
                StreamlinkDeprecationWarning,
                stacklevel=2,
            )
            if path:
                *parts, name = path.split(".")
                imported = importlib.import_module(".".join(parts))
                obj = getattr(imported, name, None)

            return obj

        if orig_getattr is not None:
            return orig_getattr(name)

        raise AttributeError

    mod_globals["__getattr__"] = __getattr__

    # delete the deprecated module attributes and the imported `deprecated` function
    for item in items.keys() | [deprecated.__name__]:
        if item not in mod_globals:
            del mod_globals[item]

x_deprecated__mutmut_mutants : ClassVar[MutantDict] = {
'x_deprecated__mutmut_1': x_deprecated__mutmut_1, 
    'x_deprecated__mutmut_2': x_deprecated__mutmut_2, 
    'x_deprecated__mutmut_3': x_deprecated__mutmut_3, 
    'x_deprecated__mutmut_4': x_deprecated__mutmut_4, 
    'x_deprecated__mutmut_5': x_deprecated__mutmut_5, 
    'x_deprecated__mutmut_6': x_deprecated__mutmut_6, 
    'x_deprecated__mutmut_7': x_deprecated__mutmut_7, 
    'x_deprecated__mutmut_8': x_deprecated__mutmut_8, 
    'x_deprecated__mutmut_9': x_deprecated__mutmut_9, 
    'x_deprecated__mutmut_10': x_deprecated__mutmut_10, 
    'x_deprecated__mutmut_11': x_deprecated__mutmut_11, 
    'x_deprecated__mutmut_12': x_deprecated__mutmut_12, 
    'x_deprecated__mutmut_13': x_deprecated__mutmut_13, 
    'x_deprecated__mutmut_14': x_deprecated__mutmut_14, 
    'x_deprecated__mutmut_15': x_deprecated__mutmut_15, 
    'x_deprecated__mutmut_16': x_deprecated__mutmut_16, 
    'x_deprecated__mutmut_17': x_deprecated__mutmut_17, 
    'x_deprecated__mutmut_18': x_deprecated__mutmut_18, 
    'x_deprecated__mutmut_19': x_deprecated__mutmut_19, 
    'x_deprecated__mutmut_20': x_deprecated__mutmut_20, 
    'x_deprecated__mutmut_21': x_deprecated__mutmut_21, 
    'x_deprecated__mutmut_22': x_deprecated__mutmut_22, 
    'x_deprecated__mutmut_23': x_deprecated__mutmut_23, 
    'x_deprecated__mutmut_24': x_deprecated__mutmut_24, 
    'x_deprecated__mutmut_25': x_deprecated__mutmut_25, 
    'x_deprecated__mutmut_26': x_deprecated__mutmut_26, 
    'x_deprecated__mutmut_27': x_deprecated__mutmut_27, 
    'x_deprecated__mutmut_28': x_deprecated__mutmut_28, 
    'x_deprecated__mutmut_29': x_deprecated__mutmut_29, 
    'x_deprecated__mutmut_30': x_deprecated__mutmut_30, 
    'x_deprecated__mutmut_31': x_deprecated__mutmut_31, 
    'x_deprecated__mutmut_32': x_deprecated__mutmut_32, 
    'x_deprecated__mutmut_33': x_deprecated__mutmut_33, 
    'x_deprecated__mutmut_34': x_deprecated__mutmut_34, 
    'x_deprecated__mutmut_35': x_deprecated__mutmut_35, 
    'x_deprecated__mutmut_36': x_deprecated__mutmut_36, 
    'x_deprecated__mutmut_37': x_deprecated__mutmut_37, 
    'x_deprecated__mutmut_38': x_deprecated__mutmut_38, 
    'x_deprecated__mutmut_39': x_deprecated__mutmut_39, 
    'x_deprecated__mutmut_40': x_deprecated__mutmut_40, 
    'x_deprecated__mutmut_41': x_deprecated__mutmut_41, 
    'x_deprecated__mutmut_42': x_deprecated__mutmut_42
}

def deprecated(*args, **kwargs):
    result = _mutmut_trampoline(x_deprecated__mutmut_orig, x_deprecated__mutmut_mutants, args, kwargs)
    return result 

deprecated.__signature__ = _mutmut_signature(x_deprecated__mutmut_orig)
x_deprecated__mutmut_orig.__name__ = 'x_deprecated'


__all__ = [
    "BaseExceptionGroup",
    "ExceptionGroup",
    "deprecated",
    "detect_encoding",
    "is_darwin",
    "is_win32",
]

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
class StreamlinkError(Exception):
    """
    Any error caused by Streamlink will be caught with this exception.
    """


# TODO: don't use PluginError for failed HTTP requests or validation schema failures
class PluginError(StreamlinkError):
    """
    Plugin related error.
    """


class FatalPluginError(PluginError):
    """
    Plugin related error that cannot be recovered from.

    Plugins should use this ``Exception`` when errors that can
    never be recovered from are encountered. For example, when
    a user's input is required and none can be given.
    """


class NoPluginError(StreamlinkError):
    """
    Error raised by :py:meth:`Streamlink.resolve_url() <streamlink.Streamlink.resolve_url()>`
    and :py:meth:`Streamlink.resolve_url_no_redirect() <streamlink.Streamlink.resolve_url_no_redirect()>`
    when no plugin could be found for the given input URL.
    """


class NoStreamsError(StreamlinkError):
    """
    Plugins should use this ``Exception`` in :py:meth:`Plugin._get_streams() <streamlink.plugin.Plugin._get_streams()>`
    when returning ``None`` or an empty ``dict`` is not possible, e.g. in nested function calls.
    """


class StreamError(StreamlinkError):
    """
    Stream related error.
    """


# https://stackoverflow.com/a/49797717
class _StreamlinkWarningMeta(type):
    def __new__(mcs, name, bases, namespace, **kw):
        name = namespace.get("__name__", name)
        return super().__new__(mcs, name, bases, namespace, **kw)


class StreamlinkWarning(UserWarning, metaclass=_StreamlinkWarningMeta):
    pass


class StreamlinkDeprecationWarning(StreamlinkWarning):
    __name__ = "StreamlinkDeprecation"


__all__ = [
    "StreamlinkError",
    "PluginError",
    "FatalPluginError",
    "NoPluginError",
    "NoStreamsError",
    "StreamError",
    "StreamlinkWarning",
    "StreamlinkDeprecationWarning",
]

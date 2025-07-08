from streamlink.session import Streamlink
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


def x_streams__mutmut_orig(url: str, **params):
    """
    Initializes an empty Streamlink session, attempts to find a plugin and extracts streams from the URL if a plugin was found.

    :param url: a URL to match against loaded plugins
    :param params: Additional keyword arguments passed to :meth:`Streamlink.streams() <streamlink.session.Streamlink.streams>`
    :raises NoPluginError: on plugin resolve failure
    :returns: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
    """

    session = Streamlink()

    return session.streams(url, **params)


def x_streams__mutmut_1(url: str, **params):
    """
    Initializes an empty Streamlink session, attempts to find a plugin and extracts streams from the URL if a plugin was found.

    :param url: a URL to match against loaded plugins
    :param params: Additional keyword arguments passed to :meth:`Streamlink.streams() <streamlink.session.Streamlink.streams>`
    :raises NoPluginError: on plugin resolve failure
    :returns: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
    """

    session = None

    return session.streams(url, **params)


def x_streams__mutmut_2(url: str, **params):
    """
    Initializes an empty Streamlink session, attempts to find a plugin and extracts streams from the URL if a plugin was found.

    :param url: a URL to match against loaded plugins
    :param params: Additional keyword arguments passed to :meth:`Streamlink.streams() <streamlink.session.Streamlink.streams>`
    :raises NoPluginError: on plugin resolve failure
    :returns: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
    """

    session = Streamlink()

    return session.streams(None, **params)


def x_streams__mutmut_3(url: str, **params):
    """
    Initializes an empty Streamlink session, attempts to find a plugin and extracts streams from the URL if a plugin was found.

    :param url: a URL to match against loaded plugins
    :param params: Additional keyword arguments passed to :meth:`Streamlink.streams() <streamlink.session.Streamlink.streams>`
    :raises NoPluginError: on plugin resolve failure
    :returns: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
    """

    session = Streamlink()

    return session.streams(**params)


def x_streams__mutmut_4(url: str, **params):
    """
    Initializes an empty Streamlink session, attempts to find a plugin and extracts streams from the URL if a plugin was found.

    :param url: a URL to match against loaded plugins
    :param params: Additional keyword arguments passed to :meth:`Streamlink.streams() <streamlink.session.Streamlink.streams>`
    :raises NoPluginError: on plugin resolve failure
    :returns: A :class:`dict` of stream names and :class:`Stream <streamlink.stream.Stream>` instances
    """

    session = Streamlink()

    return session.streams(url, )

x_streams__mutmut_mutants : ClassVar[MutantDict] = {
'x_streams__mutmut_1': x_streams__mutmut_1, 
    'x_streams__mutmut_2': x_streams__mutmut_2, 
    'x_streams__mutmut_3': x_streams__mutmut_3, 
    'x_streams__mutmut_4': x_streams__mutmut_4
}

def streams(*args, **kwargs):
    result = _mutmut_trampoline(x_streams__mutmut_orig, x_streams__mutmut_mutants, args, kwargs)
    return result 

streams.__signature__ = _mutmut_signature(x_streams__mutmut_orig)
x_streams__mutmut_orig.__name__ = 'x_streams'

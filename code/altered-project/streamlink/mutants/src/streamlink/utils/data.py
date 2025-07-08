from __future__ import annotations

from typing import Any
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


def x_search_dict__mutmut_orig(data: dict | list, key: Any):
    """
    Search for a key in a nested dict, or list of nested dicts, and return the values.

    :param data: dict/list to search
    :param key: key to find
    :return: matches for key
    """
    if isinstance(data, dict):
        for dkey, value in data.items():
            if dkey == key:
                yield value
            yield from search_dict(value, key)
    elif isinstance(data, list):
        for value in data:
            yield from search_dict(value, key)


def x_search_dict__mutmut_1(data: dict | list, key: Any):
    """
    Search for a key in a nested dict, or list of nested dicts, and return the values.

    :param data: dict/list to search
    :param key: key to find
    :return: matches for key
    """
    if isinstance(data, dict):
        for dkey, value in data.items():
            if dkey != key:
                yield value
            yield from search_dict(value, key)
    elif isinstance(data, list):
        for value in data:
            yield from search_dict(value, key)


def x_search_dict__mutmut_2(data: dict | list, key: Any):
    """
    Search for a key in a nested dict, or list of nested dicts, and return the values.

    :param data: dict/list to search
    :param key: key to find
    :return: matches for key
    """
    if isinstance(data, dict):
        for dkey, value in data.items():
            if dkey == key:
                yield value
            yield from search_dict(None, key)
    elif isinstance(data, list):
        for value in data:
            yield from search_dict(value, key)


def x_search_dict__mutmut_3(data: dict | list, key: Any):
    """
    Search for a key in a nested dict, or list of nested dicts, and return the values.

    :param data: dict/list to search
    :param key: key to find
    :return: matches for key
    """
    if isinstance(data, dict):
        for dkey, value in data.items():
            if dkey == key:
                yield value
            yield from search_dict(value, None)
    elif isinstance(data, list):
        for value in data:
            yield from search_dict(value, key)


def x_search_dict__mutmut_4(data: dict | list, key: Any):
    """
    Search for a key in a nested dict, or list of nested dicts, and return the values.

    :param data: dict/list to search
    :param key: key to find
    :return: matches for key
    """
    if isinstance(data, dict):
        for dkey, value in data.items():
            if dkey == key:
                yield value
            yield from search_dict(key)
    elif isinstance(data, list):
        for value in data:
            yield from search_dict(value, key)


def x_search_dict__mutmut_5(data: dict | list, key: Any):
    """
    Search for a key in a nested dict, or list of nested dicts, and return the values.

    :param data: dict/list to search
    :param key: key to find
    :return: matches for key
    """
    if isinstance(data, dict):
        for dkey, value in data.items():
            if dkey == key:
                yield value
            yield from search_dict(value, )
    elif isinstance(data, list):
        for value in data:
            yield from search_dict(value, key)


def x_search_dict__mutmut_6(data: dict | list, key: Any):
    """
    Search for a key in a nested dict, or list of nested dicts, and return the values.

    :param data: dict/list to search
    :param key: key to find
    :return: matches for key
    """
    if isinstance(data, dict):
        for dkey, value in data.items():
            if dkey == key:
                yield value
            yield from search_dict(value, key)
    elif isinstance(data, list):
        for value in data:
            yield from search_dict(None, key)


def x_search_dict__mutmut_7(data: dict | list, key: Any):
    """
    Search for a key in a nested dict, or list of nested dicts, and return the values.

    :param data: dict/list to search
    :param key: key to find
    :return: matches for key
    """
    if isinstance(data, dict):
        for dkey, value in data.items():
            if dkey == key:
                yield value
            yield from search_dict(value, key)
    elif isinstance(data, list):
        for value in data:
            yield from search_dict(value, None)


def x_search_dict__mutmut_8(data: dict | list, key: Any):
    """
    Search for a key in a nested dict, or list of nested dicts, and return the values.

    :param data: dict/list to search
    :param key: key to find
    :return: matches for key
    """
    if isinstance(data, dict):
        for dkey, value in data.items():
            if dkey == key:
                yield value
            yield from search_dict(value, key)
    elif isinstance(data, list):
        for value in data:
            yield from search_dict(key)


def x_search_dict__mutmut_9(data: dict | list, key: Any):
    """
    Search for a key in a nested dict, or list of nested dicts, and return the values.

    :param data: dict/list to search
    :param key: key to find
    :return: matches for key
    """
    if isinstance(data, dict):
        for dkey, value in data.items():
            if dkey == key:
                yield value
            yield from search_dict(value, key)
    elif isinstance(data, list):
        for value in data:
            yield from search_dict(value, )

x_search_dict__mutmut_mutants : ClassVar[MutantDict] = {
'x_search_dict__mutmut_1': x_search_dict__mutmut_1, 
    'x_search_dict__mutmut_2': x_search_dict__mutmut_2, 
    'x_search_dict__mutmut_3': x_search_dict__mutmut_3, 
    'x_search_dict__mutmut_4': x_search_dict__mutmut_4, 
    'x_search_dict__mutmut_5': x_search_dict__mutmut_5, 
    'x_search_dict__mutmut_6': x_search_dict__mutmut_6, 
    'x_search_dict__mutmut_7': x_search_dict__mutmut_7, 
    'x_search_dict__mutmut_8': x_search_dict__mutmut_8, 
    'x_search_dict__mutmut_9': x_search_dict__mutmut_9
}

def search_dict(*args, **kwargs):
    result = yield from _mutmut_yield_from_trampoline(x_search_dict__mutmut_orig, x_search_dict__mutmut_mutants, args, kwargs)
    return result 

search_dict.__signature__ = _mutmut_signature(x_search_dict__mutmut_orig)
x_search_dict__mutmut_orig.__name__ = 'x_search_dict'

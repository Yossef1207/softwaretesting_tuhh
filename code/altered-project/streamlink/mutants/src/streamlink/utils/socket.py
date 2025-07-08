from __future__ import annotations

from collections.abc import Callable, Coroutine

import trio
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


def x__factory_find_free_port__mutmut_orig(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_1(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = None
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_2(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(None, None, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_3(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, None, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_4(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, address_family, None)
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_5(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(None, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_6(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_7(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_8(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, address_family, )
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_9(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(None, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_10(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, None) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_11(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_12(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, ) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_13(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(None)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_14(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[2]

    find_free_port.__name__ = name

    return find_free_port


def x__factory_find_free_port__mutmut_15(name: str, address_family: int) -> Callable[[str], Coroutine[None, None, int]]:
    async def find_free_port(host: str) -> int:  # pragma: no cover
        *_, (*_gai, address) = await trio.socket.getaddrinfo(host, None, address_family, trio.socket.SOCK_STREAM)
        with trio.socket.socket(address_family, trio.socket.SOCK_STREAM) as s:
            await s.bind(address)
            s.listen()
            return s.getsockname()[1]

    find_free_port.__name__ = None

    return find_free_port

x__factory_find_free_port__mutmut_mutants : ClassVar[MutantDict] = {
'x__factory_find_free_port__mutmut_1': x__factory_find_free_port__mutmut_1, 
    'x__factory_find_free_port__mutmut_2': x__factory_find_free_port__mutmut_2, 
    'x__factory_find_free_port__mutmut_3': x__factory_find_free_port__mutmut_3, 
    'x__factory_find_free_port__mutmut_4': x__factory_find_free_port__mutmut_4, 
    'x__factory_find_free_port__mutmut_5': x__factory_find_free_port__mutmut_5, 
    'x__factory_find_free_port__mutmut_6': x__factory_find_free_port__mutmut_6, 
    'x__factory_find_free_port__mutmut_7': x__factory_find_free_port__mutmut_7, 
    'x__factory_find_free_port__mutmut_8': x__factory_find_free_port__mutmut_8, 
    'x__factory_find_free_port__mutmut_9': x__factory_find_free_port__mutmut_9, 
    'x__factory_find_free_port__mutmut_10': x__factory_find_free_port__mutmut_10, 
    'x__factory_find_free_port__mutmut_11': x__factory_find_free_port__mutmut_11, 
    'x__factory_find_free_port__mutmut_12': x__factory_find_free_port__mutmut_12, 
    'x__factory_find_free_port__mutmut_13': x__factory_find_free_port__mutmut_13, 
    'x__factory_find_free_port__mutmut_14': x__factory_find_free_port__mutmut_14, 
    'x__factory_find_free_port__mutmut_15': x__factory_find_free_port__mutmut_15
}

def _factory_find_free_port(*args, **kwargs):
    result = _mutmut_trampoline(x__factory_find_free_port__mutmut_orig, x__factory_find_free_port__mutmut_mutants, args, kwargs)
    return result 

_factory_find_free_port.__signature__ = _mutmut_signature(x__factory_find_free_port__mutmut_orig)
x__factory_find_free_port__mutmut_orig.__name__ = 'x__factory_find_free_port'


find_free_port_ipv4 = _factory_find_free_port("find_free_port_ipv4", trio.socket.AF_INET)
find_free_port_ipv6 = _factory_find_free_port("find_free_port_ipv6", trio.socket.AF_INET6)


del _factory_find_free_port

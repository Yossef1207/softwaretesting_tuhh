import re
from urllib.parse import parse_qsl, quote_plus, urlencode, urljoin, urlparse, urlunparse
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


def x_absolute_url__mutmut_orig(baseurl, url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = urljoin(baseurl, url)

    return url


def x_absolute_url__mutmut_1(baseurl, url):
    parsed = None
    if not parsed.scheme:
        url = urljoin(baseurl, url)

    return url


def x_absolute_url__mutmut_2(baseurl, url):
    parsed = urlparse(None)
    if not parsed.scheme:
        url = urljoin(baseurl, url)

    return url


def x_absolute_url__mutmut_3(baseurl, url):
    parsed = urlparse(url)
    if parsed.scheme:
        url = urljoin(baseurl, url)

    return url


def x_absolute_url__mutmut_4(baseurl, url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = None

    return url


def x_absolute_url__mutmut_5(baseurl, url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = urljoin(None, url)

    return url


def x_absolute_url__mutmut_6(baseurl, url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = urljoin(baseurl, None)

    return url


def x_absolute_url__mutmut_7(baseurl, url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = urljoin(url)

    return url


def x_absolute_url__mutmut_8(baseurl, url):
    parsed = urlparse(url)
    if not parsed.scheme:
        url = urljoin(baseurl, )

    return url

x_absolute_url__mutmut_mutants : ClassVar[MutantDict] = {
'x_absolute_url__mutmut_1': x_absolute_url__mutmut_1, 
    'x_absolute_url__mutmut_2': x_absolute_url__mutmut_2, 
    'x_absolute_url__mutmut_3': x_absolute_url__mutmut_3, 
    'x_absolute_url__mutmut_4': x_absolute_url__mutmut_4, 
    'x_absolute_url__mutmut_5': x_absolute_url__mutmut_5, 
    'x_absolute_url__mutmut_6': x_absolute_url__mutmut_6, 
    'x_absolute_url__mutmut_7': x_absolute_url__mutmut_7, 
    'x_absolute_url__mutmut_8': x_absolute_url__mutmut_8
}

def absolute_url(*args, **kwargs):
    result = _mutmut_trampoline(x_absolute_url__mutmut_orig, x_absolute_url__mutmut_mutants, args, kwargs)
    return result 

absolute_url.__signature__ = _mutmut_signature(x_absolute_url__mutmut_orig)
x_absolute_url__mutmut_orig.__name__ = 'x_absolute_url'


def x_prepend_www__mutmut_orig(url):
    parsed = urlparse(url)
    if not parsed.netloc.startswith("www."):
        # noinspection PyProtectedMember
        parsed = parsed._replace(netloc=f"www.{parsed.netloc}")

    return parsed.geturl()


def x_prepend_www__mutmut_1(url):
    parsed = None
    if not parsed.netloc.startswith("www."):
        # noinspection PyProtectedMember
        parsed = parsed._replace(netloc=f"www.{parsed.netloc}")

    return parsed.geturl()


def x_prepend_www__mutmut_2(url):
    parsed = urlparse(None)
    if not parsed.netloc.startswith("www."):
        # noinspection PyProtectedMember
        parsed = parsed._replace(netloc=f"www.{parsed.netloc}")

    return parsed.geturl()


def x_prepend_www__mutmut_3(url):
    parsed = urlparse(url)
    if parsed.netloc.startswith("www."):
        # noinspection PyProtectedMember
        parsed = parsed._replace(netloc=f"www.{parsed.netloc}")

    return parsed.geturl()


def x_prepend_www__mutmut_4(url):
    parsed = urlparse(url)
    if not parsed.netloc.startswith(None):
        # noinspection PyProtectedMember
        parsed = parsed._replace(netloc=f"www.{parsed.netloc}")

    return parsed.geturl()


def x_prepend_www__mutmut_5(url):
    parsed = urlparse(url)
    if not parsed.netloc.startswith("XXwww.XX"):
        # noinspection PyProtectedMember
        parsed = parsed._replace(netloc=f"www.{parsed.netloc}")

    return parsed.geturl()


def x_prepend_www__mutmut_6(url):
    parsed = urlparse(url)
    if not parsed.netloc.startswith("WWW."):
        # noinspection PyProtectedMember
        parsed = parsed._replace(netloc=f"www.{parsed.netloc}")

    return parsed.geturl()


def x_prepend_www__mutmut_7(url):
    parsed = urlparse(url)
    if not parsed.netloc.startswith("Www."):
        # noinspection PyProtectedMember
        parsed = parsed._replace(netloc=f"www.{parsed.netloc}")

    return parsed.geturl()


def x_prepend_www__mutmut_8(url):
    parsed = urlparse(url)
    if not parsed.netloc.startswith("www."):
        # noinspection PyProtectedMember
        parsed = None

    return parsed.geturl()


def x_prepend_www__mutmut_9(url):
    parsed = urlparse(url)
    if not parsed.netloc.startswith("www."):
        # noinspection PyProtectedMember
        parsed = parsed._replace(netloc=None)

    return parsed.geturl()

x_prepend_www__mutmut_mutants : ClassVar[MutantDict] = {
'x_prepend_www__mutmut_1': x_prepend_www__mutmut_1, 
    'x_prepend_www__mutmut_2': x_prepend_www__mutmut_2, 
    'x_prepend_www__mutmut_3': x_prepend_www__mutmut_3, 
    'x_prepend_www__mutmut_4': x_prepend_www__mutmut_4, 
    'x_prepend_www__mutmut_5': x_prepend_www__mutmut_5, 
    'x_prepend_www__mutmut_6': x_prepend_www__mutmut_6, 
    'x_prepend_www__mutmut_7': x_prepend_www__mutmut_7, 
    'x_prepend_www__mutmut_8': x_prepend_www__mutmut_8, 
    'x_prepend_www__mutmut_9': x_prepend_www__mutmut_9
}

def prepend_www(*args, **kwargs):
    result = _mutmut_trampoline(x_prepend_www__mutmut_orig, x_prepend_www__mutmut_mutants, args, kwargs)
    return result 

prepend_www.__signature__ = _mutmut_signature(x_prepend_www__mutmut_orig)
x_prepend_www__mutmut_orig.__name__ = 'x_prepend_www'


_re_uri_implicit_scheme = re.compile(r"""^[a-z0-9][a-z0-9.+-]*://""", re.IGNORECASE)


def x_update_scheme__mutmut_orig(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_1(current: str, target: str, force: bool = False) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_2(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = None

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_3(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(None)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_4(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_5(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(None) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_6(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) or not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_7(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_8(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith(None)
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_9(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("XX//XX")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_10(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//") and not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_11(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_12(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme or not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_13(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_14(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(None).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_15(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(None)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_16(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_17(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(None).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_18(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(None)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(current).scheme))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_19(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(None)

    # keep the target scheme
    return target


def x_update_scheme__mutmut_20(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=None))

    # keep the target scheme
    return target


def x_update_scheme__mutmut_21(current: str, target: str, force: bool = True) -> str:
    """
    Take the scheme from the current URL and apply it to the target URL if it is missing
    :param current: current URL
    :param target: target URL
    :param force: always apply the current scheme to the target, even if a target scheme exists
    :return: target URL with the current URL's scheme
    """
    target_p = urlparse(target)

    if (
        # target URLs with implicit scheme and netloc including a port: ("http://", "foo.bar:1234") -> "http://foo.bar:1234"
        # urllib.parse.urlparse has incorrect behavior in py<3.9, so we'll have to use a regex here
        # py>=3.9: urlparse("127.0.0.1:1234") == ParseResult(scheme='127.0.0.1', netloc='', path='1234', ...)
        # py<3.9 : urlparse("127.0.0.1:1234") == ParseResult(scheme='', netloc='', path='127.0.0.1:1234', ...)
        not _re_uri_implicit_scheme.search(target) and not target.startswith("//")
        # target URLs without scheme and without netloc: ("http://", "foo.bar/foo") -> "http://foo.bar/foo"
        or not target_p.scheme and not target_p.netloc
    ):  # fmt: skip
        return f"{urlparse(current).scheme}://{urlunparse(target_p)}"

    # target URLs without scheme but with netloc: ("http://", "//foo.bar/foo") -> "http://foo.bar/foo"
    if not target_p.scheme:
        return f"{urlparse(current).scheme}:{urlunparse(target_p)}"

    # target URLs with scheme
    # override the target scheme
    if force:
        return urlunparse(target_p._replace(scheme=urlparse(None).scheme))

    # keep the target scheme
    return target

x_update_scheme__mutmut_mutants : ClassVar[MutantDict] = {
'x_update_scheme__mutmut_1': x_update_scheme__mutmut_1, 
    'x_update_scheme__mutmut_2': x_update_scheme__mutmut_2, 
    'x_update_scheme__mutmut_3': x_update_scheme__mutmut_3, 
    'x_update_scheme__mutmut_4': x_update_scheme__mutmut_4, 
    'x_update_scheme__mutmut_5': x_update_scheme__mutmut_5, 
    'x_update_scheme__mutmut_6': x_update_scheme__mutmut_6, 
    'x_update_scheme__mutmut_7': x_update_scheme__mutmut_7, 
    'x_update_scheme__mutmut_8': x_update_scheme__mutmut_8, 
    'x_update_scheme__mutmut_9': x_update_scheme__mutmut_9, 
    'x_update_scheme__mutmut_10': x_update_scheme__mutmut_10, 
    'x_update_scheme__mutmut_11': x_update_scheme__mutmut_11, 
    'x_update_scheme__mutmut_12': x_update_scheme__mutmut_12, 
    'x_update_scheme__mutmut_13': x_update_scheme__mutmut_13, 
    'x_update_scheme__mutmut_14': x_update_scheme__mutmut_14, 
    'x_update_scheme__mutmut_15': x_update_scheme__mutmut_15, 
    'x_update_scheme__mutmut_16': x_update_scheme__mutmut_16, 
    'x_update_scheme__mutmut_17': x_update_scheme__mutmut_17, 
    'x_update_scheme__mutmut_18': x_update_scheme__mutmut_18, 
    'x_update_scheme__mutmut_19': x_update_scheme__mutmut_19, 
    'x_update_scheme__mutmut_20': x_update_scheme__mutmut_20, 
    'x_update_scheme__mutmut_21': x_update_scheme__mutmut_21
}

def update_scheme(*args, **kwargs):
    result = _mutmut_trampoline(x_update_scheme__mutmut_orig, x_update_scheme__mutmut_mutants, args, kwargs)
    return result 

update_scheme.__signature__ = _mutmut_signature(x_update_scheme__mutmut_orig)
x_update_scheme__mutmut_orig.__name__ = 'x_update_scheme'


def x_url_equal__mutmut_orig(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_1(
    first,
    second,
    ignore_scheme=True,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_2(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=True,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_3(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=True,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_4(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=True,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_5(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=True,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_6(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=True,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_7(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = None
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_8(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(None)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_9(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = None

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_10(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(None)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_11(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme != secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_12(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme and ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_13(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme) or (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_14(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc != secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_15(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc and ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_16(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc) or (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_17(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path != secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_18(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path and ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_19(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path) or (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_20(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params != secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_21(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params and ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_22(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params) or (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_23(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query != secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_24(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query and ignore_query)
        and (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_25(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query) or (firstp.fragment == secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_26(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment != secondp.fragment or ignore_fragment)
    )


def x_url_equal__mutmut_27(
    first,
    second,
    ignore_scheme=False,
    ignore_netloc=False,
    ignore_path=False,
    ignore_params=False,
    ignore_query=False,
    ignore_fragment=False,
):
    """
    Compare two URLs and return True if they are equal, some parts of the URLs can be ignored
    :param first: URL
    :param second: URL
    :param ignore_scheme: ignore the scheme
    :param ignore_netloc: ignore the netloc
    :param ignore_path: ignore the path
    :param ignore_params: ignore the params
    :param ignore_query: ignore the query string
    :param ignore_fragment: ignore the fragment
    :return: result of comparison
    """
    # <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    firstp = urlparse(first)
    secondp = urlparse(second)

    return (
        (firstp.scheme == secondp.scheme or ignore_scheme)
        and (firstp.netloc == secondp.netloc or ignore_netloc)
        and (firstp.path == secondp.path or ignore_path)
        and (firstp.params == secondp.params or ignore_params)
        and (firstp.query == secondp.query or ignore_query)
        and (firstp.fragment == secondp.fragment and ignore_fragment)
    )

x_url_equal__mutmut_mutants : ClassVar[MutantDict] = {
'x_url_equal__mutmut_1': x_url_equal__mutmut_1, 
    'x_url_equal__mutmut_2': x_url_equal__mutmut_2, 
    'x_url_equal__mutmut_3': x_url_equal__mutmut_3, 
    'x_url_equal__mutmut_4': x_url_equal__mutmut_4, 
    'x_url_equal__mutmut_5': x_url_equal__mutmut_5, 
    'x_url_equal__mutmut_6': x_url_equal__mutmut_6, 
    'x_url_equal__mutmut_7': x_url_equal__mutmut_7, 
    'x_url_equal__mutmut_8': x_url_equal__mutmut_8, 
    'x_url_equal__mutmut_9': x_url_equal__mutmut_9, 
    'x_url_equal__mutmut_10': x_url_equal__mutmut_10, 
    'x_url_equal__mutmut_11': x_url_equal__mutmut_11, 
    'x_url_equal__mutmut_12': x_url_equal__mutmut_12, 
    'x_url_equal__mutmut_13': x_url_equal__mutmut_13, 
    'x_url_equal__mutmut_14': x_url_equal__mutmut_14, 
    'x_url_equal__mutmut_15': x_url_equal__mutmut_15, 
    'x_url_equal__mutmut_16': x_url_equal__mutmut_16, 
    'x_url_equal__mutmut_17': x_url_equal__mutmut_17, 
    'x_url_equal__mutmut_18': x_url_equal__mutmut_18, 
    'x_url_equal__mutmut_19': x_url_equal__mutmut_19, 
    'x_url_equal__mutmut_20': x_url_equal__mutmut_20, 
    'x_url_equal__mutmut_21': x_url_equal__mutmut_21, 
    'x_url_equal__mutmut_22': x_url_equal__mutmut_22, 
    'x_url_equal__mutmut_23': x_url_equal__mutmut_23, 
    'x_url_equal__mutmut_24': x_url_equal__mutmut_24, 
    'x_url_equal__mutmut_25': x_url_equal__mutmut_25, 
    'x_url_equal__mutmut_26': x_url_equal__mutmut_26, 
    'x_url_equal__mutmut_27': x_url_equal__mutmut_27
}

def url_equal(*args, **kwargs):
    result = _mutmut_trampoline(x_url_equal__mutmut_orig, x_url_equal__mutmut_mutants, args, kwargs)
    return result 

url_equal.__signature__ = _mutmut_signature(x_url_equal__mutmut_orig)
x_url_equal__mutmut_orig.__name__ = 'x_url_equal'


def x_url_concat__mutmut_orig(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_1(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = None
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_2(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get(None, True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_3(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", None)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_4(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get(True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_5(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", )
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_6(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("XXallow_fragmentsXX", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_7(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("ALLOW_FRAGMENTS", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_8(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("Allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_9(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", False)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_10(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = None
    return base


def x_url_concat__mutmut_11(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(None, part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_12(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", None, allow_fragments)
    return base


def x_url_concat__mutmut_13(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), None)
    return base


def x_url_concat__mutmut_14(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_15(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", allow_fragments)
    return base


def x_url_concat__mutmut_16(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("/"), )
    return base


def x_url_concat__mutmut_17(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip(None) + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_18(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.lstrip("/") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_19(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("XX/XX") + "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_20(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("/") - "/", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_21(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "XX/XX", part.strip("/"), allow_fragments)
    return base


def x_url_concat__mutmut_22(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip(None), allow_fragments)
    return base


def x_url_concat__mutmut_23(base, *parts, **kwargs):
    """
    Join extra paths to a URL, does not join absolute paths
    :param base: the base URL
    :param parts: a list of the parts to join
    :param allow_fragments: include url fragments
    :return: the joined URL
    """
    allow_fragments = kwargs.get("allow_fragments", True)
    for part in parts:
        base = urljoin(base.rstrip("/") + "/", part.strip("XX/XX"), allow_fragments)
    return base

x_url_concat__mutmut_mutants : ClassVar[MutantDict] = {
'x_url_concat__mutmut_1': x_url_concat__mutmut_1, 
    'x_url_concat__mutmut_2': x_url_concat__mutmut_2, 
    'x_url_concat__mutmut_3': x_url_concat__mutmut_3, 
    'x_url_concat__mutmut_4': x_url_concat__mutmut_4, 
    'x_url_concat__mutmut_5': x_url_concat__mutmut_5, 
    'x_url_concat__mutmut_6': x_url_concat__mutmut_6, 
    'x_url_concat__mutmut_7': x_url_concat__mutmut_7, 
    'x_url_concat__mutmut_8': x_url_concat__mutmut_8, 
    'x_url_concat__mutmut_9': x_url_concat__mutmut_9, 
    'x_url_concat__mutmut_10': x_url_concat__mutmut_10, 
    'x_url_concat__mutmut_11': x_url_concat__mutmut_11, 
    'x_url_concat__mutmut_12': x_url_concat__mutmut_12, 
    'x_url_concat__mutmut_13': x_url_concat__mutmut_13, 
    'x_url_concat__mutmut_14': x_url_concat__mutmut_14, 
    'x_url_concat__mutmut_15': x_url_concat__mutmut_15, 
    'x_url_concat__mutmut_16': x_url_concat__mutmut_16, 
    'x_url_concat__mutmut_17': x_url_concat__mutmut_17, 
    'x_url_concat__mutmut_18': x_url_concat__mutmut_18, 
    'x_url_concat__mutmut_19': x_url_concat__mutmut_19, 
    'x_url_concat__mutmut_20': x_url_concat__mutmut_20, 
    'x_url_concat__mutmut_21': x_url_concat__mutmut_21, 
    'x_url_concat__mutmut_22': x_url_concat__mutmut_22, 
    'x_url_concat__mutmut_23': x_url_concat__mutmut_23
}

def url_concat(*args, **kwargs):
    result = _mutmut_trampoline(x_url_concat__mutmut_orig, x_url_concat__mutmut_mutants, args, kwargs)
    return result 

url_concat.__signature__ = _mutmut_signature(x_url_concat__mutmut_orig)
x_url_concat__mutmut_orig.__name__ = 'x_url_concat'


def x_update_qsd__mutmut_orig(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_1(url, qsd=None, remove=None, keep_blank_values=False, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_2(url, qsd=None, remove=None, keep_blank_values=True, safe="XXXX", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_3(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = None
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_4(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd and {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_5(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = None

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_6(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove and []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_7(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = None
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_8(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(None)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_9(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = None

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_10(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(None)

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_11(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(None, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_12(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=None))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_13(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_14(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, ))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_15(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=False))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_16(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove != "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_17(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "XX*XX":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_18(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = None

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_19(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(None)

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_20(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_21(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_22(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = None

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_23(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(None):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_24(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_25(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value or not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_26(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_27(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values or key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_28(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_29(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = None

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_30(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=None, safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_31(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=None, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_32(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=None)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_33(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(safe=safe, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_34(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, quote_via=quote_via)

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_35(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, )

    return parsed._replace(query=query).geturl()


def x_update_qsd__mutmut_36(url, qsd=None, remove=None, keep_blank_values=True, safe="", quote_via=quote_plus):
    """
    Update or remove keys from a query string in a URL

    :param url: URL to update
    :param qsd: dict of keys to update, a None value leaves it unchanged
    :param remove: list of keys to remove, or "*" to remove all
                   note: updated keys are never removed, even if unchanged
    :param keep_blank_values: whether params with blank values should be kept or not
    :param safe: string of reserved encoding characters, passed to the quote_via function
    :param quote_via: function which encodes query string keys and values. Default: urllib.parse.quote_plus
    :return: updated URL
    """
    qsd = qsd or {}
    remove = remove or []

    # parse current query string
    parsed = urlparse(url)
    current_qsd = dict(parse_qsl(parsed.query, keep_blank_values=True))

    # * removes all possible keys
    if remove == "*":
        remove = list(current_qsd.keys())

    # remove keys before updating, but leave updated keys untouched
    for key in remove:
        if key not in qsd:
            del current_qsd[key]

    # and update the query string
    for key, value in qsd.items():
        if value is not None:
            current_qsd[key] = value

    for key, value in list(current_qsd.items()):  # use list() to create a view of the current_qsd
        if not value and not keep_blank_values and key not in qsd:
            del current_qsd[key]

    query = urlencode(query=current_qsd, safe=safe, quote_via=quote_via)

    return parsed._replace(query=None).geturl()

x_update_qsd__mutmut_mutants : ClassVar[MutantDict] = {
'x_update_qsd__mutmut_1': x_update_qsd__mutmut_1, 
    'x_update_qsd__mutmut_2': x_update_qsd__mutmut_2, 
    'x_update_qsd__mutmut_3': x_update_qsd__mutmut_3, 
    'x_update_qsd__mutmut_4': x_update_qsd__mutmut_4, 
    'x_update_qsd__mutmut_5': x_update_qsd__mutmut_5, 
    'x_update_qsd__mutmut_6': x_update_qsd__mutmut_6, 
    'x_update_qsd__mutmut_7': x_update_qsd__mutmut_7, 
    'x_update_qsd__mutmut_8': x_update_qsd__mutmut_8, 
    'x_update_qsd__mutmut_9': x_update_qsd__mutmut_9, 
    'x_update_qsd__mutmut_10': x_update_qsd__mutmut_10, 
    'x_update_qsd__mutmut_11': x_update_qsd__mutmut_11, 
    'x_update_qsd__mutmut_12': x_update_qsd__mutmut_12, 
    'x_update_qsd__mutmut_13': x_update_qsd__mutmut_13, 
    'x_update_qsd__mutmut_14': x_update_qsd__mutmut_14, 
    'x_update_qsd__mutmut_15': x_update_qsd__mutmut_15, 
    'x_update_qsd__mutmut_16': x_update_qsd__mutmut_16, 
    'x_update_qsd__mutmut_17': x_update_qsd__mutmut_17, 
    'x_update_qsd__mutmut_18': x_update_qsd__mutmut_18, 
    'x_update_qsd__mutmut_19': x_update_qsd__mutmut_19, 
    'x_update_qsd__mutmut_20': x_update_qsd__mutmut_20, 
    'x_update_qsd__mutmut_21': x_update_qsd__mutmut_21, 
    'x_update_qsd__mutmut_22': x_update_qsd__mutmut_22, 
    'x_update_qsd__mutmut_23': x_update_qsd__mutmut_23, 
    'x_update_qsd__mutmut_24': x_update_qsd__mutmut_24, 
    'x_update_qsd__mutmut_25': x_update_qsd__mutmut_25, 
    'x_update_qsd__mutmut_26': x_update_qsd__mutmut_26, 
    'x_update_qsd__mutmut_27': x_update_qsd__mutmut_27, 
    'x_update_qsd__mutmut_28': x_update_qsd__mutmut_28, 
    'x_update_qsd__mutmut_29': x_update_qsd__mutmut_29, 
    'x_update_qsd__mutmut_30': x_update_qsd__mutmut_30, 
    'x_update_qsd__mutmut_31': x_update_qsd__mutmut_31, 
    'x_update_qsd__mutmut_32': x_update_qsd__mutmut_32, 
    'x_update_qsd__mutmut_33': x_update_qsd__mutmut_33, 
    'x_update_qsd__mutmut_34': x_update_qsd__mutmut_34, 
    'x_update_qsd__mutmut_35': x_update_qsd__mutmut_35, 
    'x_update_qsd__mutmut_36': x_update_qsd__mutmut_36
}

def update_qsd(*args, **kwargs):
    result = _mutmut_trampoline(x_update_qsd__mutmut_orig, x_update_qsd__mutmut_mutants, args, kwargs)
    return result 

update_qsd.__signature__ = _mutmut_signature(x_update_qsd__mutmut_orig)
x_update_qsd__mutmut_orig.__name__ = 'x_update_qsd'

from __future__ import annotations

from streamlink.exceptions import StreamError
from streamlink.session import Streamlink
from streamlink.stream.stream import Stream
from streamlink.stream.wrappers import StreamIOIterWrapper, StreamIOThreadWrapper
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


class HTTPStream(Stream):
    """
    An HTTP stream using the :mod:`requests` library.
    """

    __shortname__ = "http"

    args: dict
    """A dict of keyword arguments passed to :meth:`requests.Session.request`, such as method, headers, cookies, etc."""

    def xǁHTTPStreamǁ__init____mutmut_orig(
        self,
        session: Streamlink,
        url: str,
        buffered: bool = True,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param url: The URL of the HTTP stream
        :param buffered: Wrap stream output in an additional reader-thread
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.args = self.session.http.valid_request_args(**kwargs)
        self.args["url"] = url
        self.buffered = buffered

    def xǁHTTPStreamǁ__init____mutmut_1(
        self,
        session: Streamlink,
        url: str,
        buffered: bool = False,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param url: The URL of the HTTP stream
        :param buffered: Wrap stream output in an additional reader-thread
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.args = self.session.http.valid_request_args(**kwargs)
        self.args["url"] = url
        self.buffered = buffered

    def xǁHTTPStreamǁ__init____mutmut_2(
        self,
        session: Streamlink,
        url: str,
        buffered: bool = True,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param url: The URL of the HTTP stream
        :param buffered: Wrap stream output in an additional reader-thread
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(None)
        self.args = self.session.http.valid_request_args(**kwargs)
        self.args["url"] = url
        self.buffered = buffered

    def xǁHTTPStreamǁ__init____mutmut_3(
        self,
        session: Streamlink,
        url: str,
        buffered: bool = True,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param url: The URL of the HTTP stream
        :param buffered: Wrap stream output in an additional reader-thread
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.args = None
        self.args["url"] = url
        self.buffered = buffered

    def xǁHTTPStreamǁ__init____mutmut_4(
        self,
        session: Streamlink,
        url: str,
        buffered: bool = True,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param url: The URL of the HTTP stream
        :param buffered: Wrap stream output in an additional reader-thread
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.args = self.session.http.valid_request_args(**kwargs)
        self.args["url"] = None
        self.buffered = buffered

    def xǁHTTPStreamǁ__init____mutmut_5(
        self,
        session: Streamlink,
        url: str,
        buffered: bool = True,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param url: The URL of the HTTP stream
        :param buffered: Wrap stream output in an additional reader-thread
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.args = self.session.http.valid_request_args(**kwargs)
        self.args["XXurlXX"] = url
        self.buffered = buffered

    def xǁHTTPStreamǁ__init____mutmut_6(
        self,
        session: Streamlink,
        url: str,
        buffered: bool = True,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param url: The URL of the HTTP stream
        :param buffered: Wrap stream output in an additional reader-thread
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.args = self.session.http.valid_request_args(**kwargs)
        self.args["URL"] = url
        self.buffered = buffered

    def xǁHTTPStreamǁ__init____mutmut_7(
        self,
        session: Streamlink,
        url: str,
        buffered: bool = True,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param url: The URL of the HTTP stream
        :param buffered: Wrap stream output in an additional reader-thread
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.args = self.session.http.valid_request_args(**kwargs)
        self.args["Url"] = url
        self.buffered = buffered

    def xǁHTTPStreamǁ__init____mutmut_8(
        self,
        session: Streamlink,
        url: str,
        buffered: bool = True,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param url: The URL of the HTTP stream
        :param buffered: Wrap stream output in an additional reader-thread
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.args = self.session.http.valid_request_args(**kwargs)
        self.args["url"] = url
        self.buffered = None
    
    xǁHTTPStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁHTTPStreamǁ__init____mutmut_1': xǁHTTPStreamǁ__init____mutmut_1, 
        'xǁHTTPStreamǁ__init____mutmut_2': xǁHTTPStreamǁ__init____mutmut_2, 
        'xǁHTTPStreamǁ__init____mutmut_3': xǁHTTPStreamǁ__init____mutmut_3, 
        'xǁHTTPStreamǁ__init____mutmut_4': xǁHTTPStreamǁ__init____mutmut_4, 
        'xǁHTTPStreamǁ__init____mutmut_5': xǁHTTPStreamǁ__init____mutmut_5, 
        'xǁHTTPStreamǁ__init____mutmut_6': xǁHTTPStreamǁ__init____mutmut_6, 
        'xǁHTTPStreamǁ__init____mutmut_7': xǁHTTPStreamǁ__init____mutmut_7, 
        'xǁHTTPStreamǁ__init____mutmut_8': xǁHTTPStreamǁ__init____mutmut_8
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁHTTPStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁHTTPStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁHTTPStreamǁ__init____mutmut_orig)
    xǁHTTPStreamǁ__init____mutmut_orig.__name__ = 'xǁHTTPStreamǁ__init__'

    def xǁHTTPStreamǁ__json____mutmut_orig(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            url=req.url,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_1(self):  # noqa: PLW3201
        req = None

        return dict(
            type=self.shortname(),
            method=req.method,
            url=req.url,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_2(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            typeXX=self.shortname(),
            method=req.method,
            url=req.url,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_3(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            methodXX=req.method,
            url=req.url,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_4(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            urlXX=req.url,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_5(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            url=req.url,
            headersXX=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_6(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            url=req.url,
            headers=dict(req.headers),
            bodyXX=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_7(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=None,
            method=req.method,
            url=req.url,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_8(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=None,
            url=req.url,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_9(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            url=None,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_10(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            url=req.url,
            headers=None,
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_11(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            url=req.url,
            headers=dict(req.headers),
            body=None,
        )

    def xǁHTTPStreamǁ__json____mutmut_12(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            method=req.method,
            url=req.url,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_13(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            url=req.url,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_14(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            headers=dict(req.headers),
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_15(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            url=req.url,
            body=req.body,
        )

    def xǁHTTPStreamǁ__json____mutmut_16(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            url=req.url,
            headers=dict(req.headers),
            )

    def xǁHTTPStreamǁ__json____mutmut_17(self):  # noqa: PLW3201
        req = self.session.http.prepare_new_request(**self.args)

        return dict(
            type=self.shortname(),
            method=req.method,
            url=req.url,
            headers=dict(None),
            body=req.body,
        )
    
    xǁHTTPStreamǁ__json____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁHTTPStreamǁ__json____mutmut_1': xǁHTTPStreamǁ__json____mutmut_1, 
        'xǁHTTPStreamǁ__json____mutmut_2': xǁHTTPStreamǁ__json____mutmut_2, 
        'xǁHTTPStreamǁ__json____mutmut_3': xǁHTTPStreamǁ__json____mutmut_3, 
        'xǁHTTPStreamǁ__json____mutmut_4': xǁHTTPStreamǁ__json____mutmut_4, 
        'xǁHTTPStreamǁ__json____mutmut_5': xǁHTTPStreamǁ__json____mutmut_5, 
        'xǁHTTPStreamǁ__json____mutmut_6': xǁHTTPStreamǁ__json____mutmut_6, 
        'xǁHTTPStreamǁ__json____mutmut_7': xǁHTTPStreamǁ__json____mutmut_7, 
        'xǁHTTPStreamǁ__json____mutmut_8': xǁHTTPStreamǁ__json____mutmut_8, 
        'xǁHTTPStreamǁ__json____mutmut_9': xǁHTTPStreamǁ__json____mutmut_9, 
        'xǁHTTPStreamǁ__json____mutmut_10': xǁHTTPStreamǁ__json____mutmut_10, 
        'xǁHTTPStreamǁ__json____mutmut_11': xǁHTTPStreamǁ__json____mutmut_11, 
        'xǁHTTPStreamǁ__json____mutmut_12': xǁHTTPStreamǁ__json____mutmut_12, 
        'xǁHTTPStreamǁ__json____mutmut_13': xǁHTTPStreamǁ__json____mutmut_13, 
        'xǁHTTPStreamǁ__json____mutmut_14': xǁHTTPStreamǁ__json____mutmut_14, 
        'xǁHTTPStreamǁ__json____mutmut_15': xǁHTTPStreamǁ__json____mutmut_15, 
        'xǁHTTPStreamǁ__json____mutmut_16': xǁHTTPStreamǁ__json____mutmut_16, 
        'xǁHTTPStreamǁ__json____mutmut_17': xǁHTTPStreamǁ__json____mutmut_17
    }
    
    def __json__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁHTTPStreamǁ__json____mutmut_orig"), object.__getattribute__(self, "xǁHTTPStreamǁ__json____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __json__.__signature__ = _mutmut_signature(xǁHTTPStreamǁ__json____mutmut_orig)
    xǁHTTPStreamǁ__json____mutmut_orig.__name__ = 'xǁHTTPStreamǁ__json__'

    def to_url(self):
        return self.url

    @property
    def url(self) -> str:
        """
        The URL to the stream, prepared by :mod:`requests` with parameters read from :attr:`args`.
        """

        return self.session.http.prepare_new_request(**self.args).url  # type: ignore[return-value]

    def xǁHTTPStreamǁopen__mutmut_orig(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_1(self):
        reqargs = None
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_2(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault(None, "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_3(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", None)
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_4(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_5(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", )
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_6(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("XXmethodXX", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_7(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("METHOD", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_8(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("Method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_9(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "XXGETXX")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_10(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "get")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_11(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "Get")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_12(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = None
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_13(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get(None)
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_14(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("XXstream-timeoutXX")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_15(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("STREAM-TIMEOUT")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_16(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("Stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_17(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = None

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_18(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=None,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_19(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=None,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_20(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=None,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_21(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_22(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_23(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_24(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_25(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=False,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_26(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = None
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_27(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(None)
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_28(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(None))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_29(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8193))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_30(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = None

        return fd

    def xǁHTTPStreamǁopen__mutmut_31(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(None, fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_32(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, None, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_33(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, timeout=None)

        return fd

    def xǁHTTPStreamǁopen__mutmut_34(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(fd, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_35(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, timeout=timeout)

        return fd

    def xǁHTTPStreamǁopen__mutmut_36(self):
        reqargs = self.session.http.valid_request_args(**self.args)
        reqargs.setdefault("method", "GET")
        timeout = self.session.options.get("stream-timeout")
        res = self.session.http.request(
            stream=True,
            exception=StreamError,
            timeout=timeout,
            **reqargs,
        )

        fd = StreamIOIterWrapper(res.iter_content(8192))
        if self.buffered:
            fd = StreamIOThreadWrapper(self.session, fd, )

        return fd
    
    xǁHTTPStreamǁopen__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁHTTPStreamǁopen__mutmut_1': xǁHTTPStreamǁopen__mutmut_1, 
        'xǁHTTPStreamǁopen__mutmut_2': xǁHTTPStreamǁopen__mutmut_2, 
        'xǁHTTPStreamǁopen__mutmut_3': xǁHTTPStreamǁopen__mutmut_3, 
        'xǁHTTPStreamǁopen__mutmut_4': xǁHTTPStreamǁopen__mutmut_4, 
        'xǁHTTPStreamǁopen__mutmut_5': xǁHTTPStreamǁopen__mutmut_5, 
        'xǁHTTPStreamǁopen__mutmut_6': xǁHTTPStreamǁopen__mutmut_6, 
        'xǁHTTPStreamǁopen__mutmut_7': xǁHTTPStreamǁopen__mutmut_7, 
        'xǁHTTPStreamǁopen__mutmut_8': xǁHTTPStreamǁopen__mutmut_8, 
        'xǁHTTPStreamǁopen__mutmut_9': xǁHTTPStreamǁopen__mutmut_9, 
        'xǁHTTPStreamǁopen__mutmut_10': xǁHTTPStreamǁopen__mutmut_10, 
        'xǁHTTPStreamǁopen__mutmut_11': xǁHTTPStreamǁopen__mutmut_11, 
        'xǁHTTPStreamǁopen__mutmut_12': xǁHTTPStreamǁopen__mutmut_12, 
        'xǁHTTPStreamǁopen__mutmut_13': xǁHTTPStreamǁopen__mutmut_13, 
        'xǁHTTPStreamǁopen__mutmut_14': xǁHTTPStreamǁopen__mutmut_14, 
        'xǁHTTPStreamǁopen__mutmut_15': xǁHTTPStreamǁopen__mutmut_15, 
        'xǁHTTPStreamǁopen__mutmut_16': xǁHTTPStreamǁopen__mutmut_16, 
        'xǁHTTPStreamǁopen__mutmut_17': xǁHTTPStreamǁopen__mutmut_17, 
        'xǁHTTPStreamǁopen__mutmut_18': xǁHTTPStreamǁopen__mutmut_18, 
        'xǁHTTPStreamǁopen__mutmut_19': xǁHTTPStreamǁopen__mutmut_19, 
        'xǁHTTPStreamǁopen__mutmut_20': xǁHTTPStreamǁopen__mutmut_20, 
        'xǁHTTPStreamǁopen__mutmut_21': xǁHTTPStreamǁopen__mutmut_21, 
        'xǁHTTPStreamǁopen__mutmut_22': xǁHTTPStreamǁopen__mutmut_22, 
        'xǁHTTPStreamǁopen__mutmut_23': xǁHTTPStreamǁopen__mutmut_23, 
        'xǁHTTPStreamǁopen__mutmut_24': xǁHTTPStreamǁopen__mutmut_24, 
        'xǁHTTPStreamǁopen__mutmut_25': xǁHTTPStreamǁopen__mutmut_25, 
        'xǁHTTPStreamǁopen__mutmut_26': xǁHTTPStreamǁopen__mutmut_26, 
        'xǁHTTPStreamǁopen__mutmut_27': xǁHTTPStreamǁopen__mutmut_27, 
        'xǁHTTPStreamǁopen__mutmut_28': xǁHTTPStreamǁopen__mutmut_28, 
        'xǁHTTPStreamǁopen__mutmut_29': xǁHTTPStreamǁopen__mutmut_29, 
        'xǁHTTPStreamǁopen__mutmut_30': xǁHTTPStreamǁopen__mutmut_30, 
        'xǁHTTPStreamǁopen__mutmut_31': xǁHTTPStreamǁopen__mutmut_31, 
        'xǁHTTPStreamǁopen__mutmut_32': xǁHTTPStreamǁopen__mutmut_32, 
        'xǁHTTPStreamǁopen__mutmut_33': xǁHTTPStreamǁopen__mutmut_33, 
        'xǁHTTPStreamǁopen__mutmut_34': xǁHTTPStreamǁopen__mutmut_34, 
        'xǁHTTPStreamǁopen__mutmut_35': xǁHTTPStreamǁopen__mutmut_35, 
        'xǁHTTPStreamǁopen__mutmut_36': xǁHTTPStreamǁopen__mutmut_36
    }
    
    def open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁHTTPStreamǁopen__mutmut_orig"), object.__getattribute__(self, "xǁHTTPStreamǁopen__mutmut_mutants"), args, kwargs, self)
        return result 
    
    open.__signature__ = _mutmut_signature(xǁHTTPStreamǁopen__mutmut_orig)
    xǁHTTPStreamǁopen__mutmut_orig.__name__ = 'xǁHTTPStreamǁopen'

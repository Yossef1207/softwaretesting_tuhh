from __future__ import annotations

import re
import ssl
import time
import warnings
from typing import Any

import requests.adapters
import urllib3
from requests import PreparedRequest, Request, Session
from requests.adapters import HTTPAdapter

import streamlink.session.http_useragents as useragents
from streamlink.exceptions import PluginError, StreamlinkDeprecationWarning
from streamlink.packages.requests_file import FileAdapter
from streamlink.utils.parse import parse_json, parse_xml


try:
    from urllib3.util import create_urllib3_context  # type: ignore[attr-defined]
except ImportError:  # pragma: no cover
    # urllib3 <2.0.0 compat import
    from urllib3.util.ssl_ import create_urllib3_context
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


# urllib3>=2.0.0: enforce_content_length now defaults to True (keep the override for backwards compatibility)
class _HTTPResponse(urllib3.response.HTTPResponse):
    def xǁ_HTTPResponseǁ__init____mutmut_orig(self, *args, **kwargs):
        # Always enforce content length validation!
        # This fixes a bug in requests which doesn't raise errors on HTTP responses where
        # the "Content-Length" header doesn't match the response's body length.
        # https://github.com/psf/requests/issues/4956#issuecomment-573325001
        #
        # Summary:
        # This bug is related to urllib3.response.HTTPResponse.stream() which calls urllib3.response.HTTPResponse.read() as
        # a wrapper for http.client.HTTPResponse.read(amt=...), where no http.client.IncompleteRead exception gets raised
        # due to "backwards compatiblity" of an old bug if a specific amount is attempted to be read on an incomplete response.
        #
        # urllib3.response.HTTPResponse.read() however has an additional check implemented via the enforce_content_length
        # parameter, but it doesn't check by default and requests doesn't set the parameter for enabling it either.
        #
        # Fix this by overriding urllib3.response.HTTPResponse's constructor and always setting enforce_content_length to True,
        # as there is no way to make requests set this parameter on its own.
        kwargs["enforce_content_length"] = True
        super().__init__(*args, **kwargs)
    def xǁ_HTTPResponseǁ__init____mutmut_1(self, *args, **kwargs):
        # Always enforce content length validation!
        # This fixes a bug in requests which doesn't raise errors on HTTP responses where
        # the "Content-Length" header doesn't match the response's body length.
        # https://github.com/psf/requests/issues/4956#issuecomment-573325001
        #
        # Summary:
        # This bug is related to urllib3.response.HTTPResponse.stream() which calls urllib3.response.HTTPResponse.read() as
        # a wrapper for http.client.HTTPResponse.read(amt=...), where no http.client.IncompleteRead exception gets raised
        # due to "backwards compatiblity" of an old bug if a specific amount is attempted to be read on an incomplete response.
        #
        # urllib3.response.HTTPResponse.read() however has an additional check implemented via the enforce_content_length
        # parameter, but it doesn't check by default and requests doesn't set the parameter for enabling it either.
        #
        # Fix this by overriding urllib3.response.HTTPResponse's constructor and always setting enforce_content_length to True,
        # as there is no way to make requests set this parameter on its own.
        kwargs["enforce_content_length"] = None
        super().__init__(*args, **kwargs)
    def xǁ_HTTPResponseǁ__init____mutmut_2(self, *args, **kwargs):
        # Always enforce content length validation!
        # This fixes a bug in requests which doesn't raise errors on HTTP responses where
        # the "Content-Length" header doesn't match the response's body length.
        # https://github.com/psf/requests/issues/4956#issuecomment-573325001
        #
        # Summary:
        # This bug is related to urllib3.response.HTTPResponse.stream() which calls urllib3.response.HTTPResponse.read() as
        # a wrapper for http.client.HTTPResponse.read(amt=...), where no http.client.IncompleteRead exception gets raised
        # due to "backwards compatiblity" of an old bug if a specific amount is attempted to be read on an incomplete response.
        #
        # urllib3.response.HTTPResponse.read() however has an additional check implemented via the enforce_content_length
        # parameter, but it doesn't check by default and requests doesn't set the parameter for enabling it either.
        #
        # Fix this by overriding urllib3.response.HTTPResponse's constructor and always setting enforce_content_length to True,
        # as there is no way to make requests set this parameter on its own.
        kwargs["XXenforce_content_lengthXX"] = True
        super().__init__(*args, **kwargs)
    def xǁ_HTTPResponseǁ__init____mutmut_3(self, *args, **kwargs):
        # Always enforce content length validation!
        # This fixes a bug in requests which doesn't raise errors on HTTP responses where
        # the "Content-Length" header doesn't match the response's body length.
        # https://github.com/psf/requests/issues/4956#issuecomment-573325001
        #
        # Summary:
        # This bug is related to urllib3.response.HTTPResponse.stream() which calls urllib3.response.HTTPResponse.read() as
        # a wrapper for http.client.HTTPResponse.read(amt=...), where no http.client.IncompleteRead exception gets raised
        # due to "backwards compatiblity" of an old bug if a specific amount is attempted to be read on an incomplete response.
        #
        # urllib3.response.HTTPResponse.read() however has an additional check implemented via the enforce_content_length
        # parameter, but it doesn't check by default and requests doesn't set the parameter for enabling it either.
        #
        # Fix this by overriding urllib3.response.HTTPResponse's constructor and always setting enforce_content_length to True,
        # as there is no way to make requests set this parameter on its own.
        kwargs["ENFORCE_CONTENT_LENGTH"] = True
        super().__init__(*args, **kwargs)
    def xǁ_HTTPResponseǁ__init____mutmut_4(self, *args, **kwargs):
        # Always enforce content length validation!
        # This fixes a bug in requests which doesn't raise errors on HTTP responses where
        # the "Content-Length" header doesn't match the response's body length.
        # https://github.com/psf/requests/issues/4956#issuecomment-573325001
        #
        # Summary:
        # This bug is related to urllib3.response.HTTPResponse.stream() which calls urllib3.response.HTTPResponse.read() as
        # a wrapper for http.client.HTTPResponse.read(amt=...), where no http.client.IncompleteRead exception gets raised
        # due to "backwards compatiblity" of an old bug if a specific amount is attempted to be read on an incomplete response.
        #
        # urllib3.response.HTTPResponse.read() however has an additional check implemented via the enforce_content_length
        # parameter, but it doesn't check by default and requests doesn't set the parameter for enabling it either.
        #
        # Fix this by overriding urllib3.response.HTTPResponse's constructor and always setting enforce_content_length to True,
        # as there is no way to make requests set this parameter on its own.
        kwargs["Enforce_content_length"] = True
        super().__init__(*args, **kwargs)
    def xǁ_HTTPResponseǁ__init____mutmut_5(self, *args, **kwargs):
        # Always enforce content length validation!
        # This fixes a bug in requests which doesn't raise errors on HTTP responses where
        # the "Content-Length" header doesn't match the response's body length.
        # https://github.com/psf/requests/issues/4956#issuecomment-573325001
        #
        # Summary:
        # This bug is related to urllib3.response.HTTPResponse.stream() which calls urllib3.response.HTTPResponse.read() as
        # a wrapper for http.client.HTTPResponse.read(amt=...), where no http.client.IncompleteRead exception gets raised
        # due to "backwards compatiblity" of an old bug if a specific amount is attempted to be read on an incomplete response.
        #
        # urllib3.response.HTTPResponse.read() however has an additional check implemented via the enforce_content_length
        # parameter, but it doesn't check by default and requests doesn't set the parameter for enabling it either.
        #
        # Fix this by overriding urllib3.response.HTTPResponse's constructor and always setting enforce_content_length to True,
        # as there is no way to make requests set this parameter on its own.
        kwargs["enforce_content_length"] = False
        super().__init__(*args, **kwargs)
    def xǁ_HTTPResponseǁ__init____mutmut_6(self, *args, **kwargs):
        # Always enforce content length validation!
        # This fixes a bug in requests which doesn't raise errors on HTTP responses where
        # the "Content-Length" header doesn't match the response's body length.
        # https://github.com/psf/requests/issues/4956#issuecomment-573325001
        #
        # Summary:
        # This bug is related to urllib3.response.HTTPResponse.stream() which calls urllib3.response.HTTPResponse.read() as
        # a wrapper for http.client.HTTPResponse.read(amt=...), where no http.client.IncompleteRead exception gets raised
        # due to "backwards compatiblity" of an old bug if a specific amount is attempted to be read on an incomplete response.
        #
        # urllib3.response.HTTPResponse.read() however has an additional check implemented via the enforce_content_length
        # parameter, but it doesn't check by default and requests doesn't set the parameter for enabling it either.
        #
        # Fix this by overriding urllib3.response.HTTPResponse's constructor and always setting enforce_content_length to True,
        # as there is no way to make requests set this parameter on its own.
        kwargs["enforce_content_length"] = True
        super().__init__(**kwargs)
    def xǁ_HTTPResponseǁ__init____mutmut_7(self, *args, **kwargs):
        # Always enforce content length validation!
        # This fixes a bug in requests which doesn't raise errors on HTTP responses where
        # the "Content-Length" header doesn't match the response's body length.
        # https://github.com/psf/requests/issues/4956#issuecomment-573325001
        #
        # Summary:
        # This bug is related to urllib3.response.HTTPResponse.stream() which calls urllib3.response.HTTPResponse.read() as
        # a wrapper for http.client.HTTPResponse.read(amt=...), where no http.client.IncompleteRead exception gets raised
        # due to "backwards compatiblity" of an old bug if a specific amount is attempted to be read on an incomplete response.
        #
        # urllib3.response.HTTPResponse.read() however has an additional check implemented via the enforce_content_length
        # parameter, but it doesn't check by default and requests doesn't set the parameter for enabling it either.
        #
        # Fix this by overriding urllib3.response.HTTPResponse's constructor and always setting enforce_content_length to True,
        # as there is no way to make requests set this parameter on its own.
        kwargs["enforce_content_length"] = True
        super().__init__(*args, )
    
    xǁ_HTTPResponseǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁ_HTTPResponseǁ__init____mutmut_1': xǁ_HTTPResponseǁ__init____mutmut_1, 
        'xǁ_HTTPResponseǁ__init____mutmut_2': xǁ_HTTPResponseǁ__init____mutmut_2, 
        'xǁ_HTTPResponseǁ__init____mutmut_3': xǁ_HTTPResponseǁ__init____mutmut_3, 
        'xǁ_HTTPResponseǁ__init____mutmut_4': xǁ_HTTPResponseǁ__init____mutmut_4, 
        'xǁ_HTTPResponseǁ__init____mutmut_5': xǁ_HTTPResponseǁ__init____mutmut_5, 
        'xǁ_HTTPResponseǁ__init____mutmut_6': xǁ_HTTPResponseǁ__init____mutmut_6, 
        'xǁ_HTTPResponseǁ__init____mutmut_7': xǁ_HTTPResponseǁ__init____mutmut_7
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁ_HTTPResponseǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁ_HTTPResponseǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁ_HTTPResponseǁ__init____mutmut_orig)
    xǁ_HTTPResponseǁ__init____mutmut_orig.__name__ = 'xǁ_HTTPResponseǁ__init__'


# override all urllib3.response.HTTPResponse references in requests.adapters.HTTPAdapter.send
urllib3.connectionpool.HTTPConnectionPool.ResponseCls = _HTTPResponse  # type: ignore[attr-defined]
requests.adapters.HTTPResponse = _HTTPResponse  # type: ignore[misc]


# Never convert percent-encoded characters to uppercase in urllib3>=1.25.8.
# This is required for sites which compare request URLs byte by byte and return different responses depending on that.
# Older versions of urllib3 are not compatible with this override and will always convert to uppercase characters.
#
# https://datatracker.ietf.org/doc/html/rfc3986#section-2.1
# > The uppercase hexadecimal digits 'A' through 'F' are equivalent to
# > the lowercase digits 'a' through 'f', respectively.  If two URIs
# > differ only in the case of hexadecimal digits used in percent-encoded
# > octets, they are equivalent.  For consistency, URI producers and
# > normalizers should use uppercase hexadecimal digits for all percent-
# > encodings.
class Urllib3UtilUrlPercentReOverride:
    # urllib3>=2.0.0: _PERCENT_RE, urllib3<2.0.0: PERCENT_RE
    _re_percent_encoding: re.Pattern = getattr(
        urllib3.util.url,
        "_PERCENT_RE",
        getattr(urllib3.util.url, "PERCENT_RE", re.compile(r"%[a-fA-F0-9]{2}")),
    )

    # urllib3>=1.25.8
    # https://github.com/urllib3/urllib3/blame/1.25.8/src/urllib3/util/url.py#L219-L227
    @classmethod
    def subn(cls, repl: Any, string: str, count: Any = None) -> tuple[str, int]:
        return string, len(cls._re_percent_encoding.findall(string))


# urllib3>=2.0.0: _PERCENT_RE, urllib3<2.0.0: PERCENT_RE
urllib3.util.url._PERCENT_RE = urllib3.util.url.PERCENT_RE = Urllib3UtilUrlPercentReOverride  # type: ignore[attr-defined]


# requests.Request.__init__ keywords, except for "hooks"
_VALID_REQUEST_ARGS = "method", "url", "headers", "files", "data", "params", "auth", "cookies", "json"


class HTTPSession(Session):
    params: dict

    def xǁHTTPSessionǁ__init____mutmut_orig(self):
        super().__init__()

        self.headers["User-Agent"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount("file://", FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_1(self):
        super().__init__()

        self.headers["User-Agent"] = None
        self.timeout = 20.0

        self.mount("file://", FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_2(self):
        super().__init__()

        self.headers["XXUser-AgentXX"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount("file://", FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_3(self):
        super().__init__()

        self.headers["user-agent"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount("file://", FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_4(self):
        super().__init__()

        self.headers["USER-AGENT"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount("file://", FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_5(self):
        super().__init__()

        self.headers["User-agent"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount("file://", FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_6(self):
        super().__init__()

        self.headers["User-Agent"] = useragents.FIREFOX
        self.timeout = None

        self.mount("file://", FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_7(self):
        super().__init__()

        self.headers["User-Agent"] = useragents.FIREFOX
        self.timeout = 21.0

        self.mount("file://", FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_8(self):
        super().__init__()

        self.headers["User-Agent"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount(None, FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_9(self):
        super().__init__()

        self.headers["User-Agent"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount("file://", None)

    def xǁHTTPSessionǁ__init____mutmut_10(self):
        super().__init__()

        self.headers["User-Agent"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount(FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_11(self):
        super().__init__()

        self.headers["User-Agent"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount("file://", )

    def xǁHTTPSessionǁ__init____mutmut_12(self):
        super().__init__()

        self.headers["User-Agent"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount("XXfile://XX", FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_13(self):
        super().__init__()

        self.headers["User-Agent"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount("FILE://", FileAdapter())

    def xǁHTTPSessionǁ__init____mutmut_14(self):
        super().__init__()

        self.headers["User-Agent"] = useragents.FIREFOX
        self.timeout = 20.0

        self.mount("File://", FileAdapter())
    
    xǁHTTPSessionǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁHTTPSessionǁ__init____mutmut_1': xǁHTTPSessionǁ__init____mutmut_1, 
        'xǁHTTPSessionǁ__init____mutmut_2': xǁHTTPSessionǁ__init____mutmut_2, 
        'xǁHTTPSessionǁ__init____mutmut_3': xǁHTTPSessionǁ__init____mutmut_3, 
        'xǁHTTPSessionǁ__init____mutmut_4': xǁHTTPSessionǁ__init____mutmut_4, 
        'xǁHTTPSessionǁ__init____mutmut_5': xǁHTTPSessionǁ__init____mutmut_5, 
        'xǁHTTPSessionǁ__init____mutmut_6': xǁHTTPSessionǁ__init____mutmut_6, 
        'xǁHTTPSessionǁ__init____mutmut_7': xǁHTTPSessionǁ__init____mutmut_7, 
        'xǁHTTPSessionǁ__init____mutmut_8': xǁHTTPSessionǁ__init____mutmut_8, 
        'xǁHTTPSessionǁ__init____mutmut_9': xǁHTTPSessionǁ__init____mutmut_9, 
        'xǁHTTPSessionǁ__init____mutmut_10': xǁHTTPSessionǁ__init____mutmut_10, 
        'xǁHTTPSessionǁ__init____mutmut_11': xǁHTTPSessionǁ__init____mutmut_11, 
        'xǁHTTPSessionǁ__init____mutmut_12': xǁHTTPSessionǁ__init____mutmut_12, 
        'xǁHTTPSessionǁ__init____mutmut_13': xǁHTTPSessionǁ__init____mutmut_13, 
        'xǁHTTPSessionǁ__init____mutmut_14': xǁHTTPSessionǁ__init____mutmut_14
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁHTTPSessionǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁHTTPSessionǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁHTTPSessionǁ__init____mutmut_orig)
    xǁHTTPSessionǁ__init____mutmut_orig.__name__ = 'xǁHTTPSessionǁ__init__'

    @classmethod
    def determine_json_encoding(cls, sample: bytes):
        """
        Determine which Unicode encoding the JSON text sample is encoded with

        RFC4627 suggests that the encoding of JSON text can be determined
        by checking the pattern of NULL bytes in first 4 octets of the text.
        https://datatracker.ietf.org/doc/html/rfc4627#section-3

        :param sample: a sample of at least 4 bytes of the JSON text
        :return: the most likely encoding of the JSON text
        """
        warnings.warn("Deprecated HTTPSession.determine_json_encoding() call", StreamlinkDeprecationWarning, stacklevel=1)
        data = int.from_bytes(sample[:4], "big")

        if data & 0xFFFFFF00 == 0:
            return "UTF-32BE"
        elif data & 0xFF00FF00 == 0:
            return "UTF-16BE"
        elif data & 0x00FFFFFF == 0:
            return "UTF-32LE"
        elif data & 0x00FF00FF == 0:
            return "UTF-16LE"
        else:
            return "UTF-8"

    @classmethod
    def json(cls, res, *args, **kwargs):
        """Parses JSON from a response."""
        if res.encoding is None:
            # encoding is unknown: let ``json.loads`` figure it out from the bytes data via ``json.detect_encoding``
            return parse_json(res.content, *args, **kwargs)
        else:
            # encoding is explicitly set: get the decoded string value and let ``json.loads`` parse it
            return parse_json(res.text, *args, **kwargs)

    @classmethod
    def xml(cls, res, *args, **kwargs):
        """Parses XML from a response."""
        return parse_xml(res.text, *args, **kwargs)

    def xǁHTTPSessionǁresolve_url__mutmut_orig(self, url):
        """Resolves any redirects and returns the final URL."""
        return self.get(url, stream=True).url

    def xǁHTTPSessionǁresolve_url__mutmut_1(self, url):
        """Resolves any redirects and returns the final URL."""
        return self.get(None, stream=True).url

    def xǁHTTPSessionǁresolve_url__mutmut_2(self, url):
        """Resolves any redirects and returns the final URL."""
        return self.get(url, stream=None).url

    def xǁHTTPSessionǁresolve_url__mutmut_3(self, url):
        """Resolves any redirects and returns the final URL."""
        return self.get(stream=True).url

    def xǁHTTPSessionǁresolve_url__mutmut_4(self, url):
        """Resolves any redirects and returns the final URL."""
        return self.get(url, ).url

    def xǁHTTPSessionǁresolve_url__mutmut_5(self, url):
        """Resolves any redirects and returns the final URL."""
        return self.get(url, stream=False).url
    
    xǁHTTPSessionǁresolve_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁHTTPSessionǁresolve_url__mutmut_1': xǁHTTPSessionǁresolve_url__mutmut_1, 
        'xǁHTTPSessionǁresolve_url__mutmut_2': xǁHTTPSessionǁresolve_url__mutmut_2, 
        'xǁHTTPSessionǁresolve_url__mutmut_3': xǁHTTPSessionǁresolve_url__mutmut_3, 
        'xǁHTTPSessionǁresolve_url__mutmut_4': xǁHTTPSessionǁresolve_url__mutmut_4, 
        'xǁHTTPSessionǁresolve_url__mutmut_5': xǁHTTPSessionǁresolve_url__mutmut_5
    }
    
    def resolve_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁHTTPSessionǁresolve_url__mutmut_orig"), object.__getattribute__(self, "xǁHTTPSessionǁresolve_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    resolve_url.__signature__ = _mutmut_signature(xǁHTTPSessionǁresolve_url__mutmut_orig)
    xǁHTTPSessionǁresolve_url__mutmut_orig.__name__ = 'xǁHTTPSessionǁresolve_url'

    @staticmethod
    def valid_request_args(**req_keywords) -> dict:
        return {k: v for k, v in req_keywords.items() if k in _VALID_REQUEST_ARGS}

    def xǁHTTPSessionǁprepare_new_request__mutmut_orig(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("method", "GET")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_1(self, **req_keywords) -> PreparedRequest:
        valid_args = None
        valid_args.setdefault("method", "GET")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_2(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault(None, "GET")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_3(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("method", None)
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_4(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("GET")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_5(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("method", )
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_6(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("XXmethodXX", "GET")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_7(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("METHOD", "GET")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_8(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("Method", "GET")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_9(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("method", "XXGETXX")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_10(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("method", "get")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_11(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("method", "Get")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_12(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("method", "GET")
        request = None

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(request)

    def xǁHTTPSessionǁprepare_new_request__mutmut_13(self, **req_keywords) -> PreparedRequest:
        valid_args = self.valid_request_args(**req_keywords)
        valid_args.setdefault("method", "GET")
        request = Request(**valid_args)

        # prepare request with the session context, which might add params, headers, cookies, etc.
        return self.prepare_request(None)
    
    xǁHTTPSessionǁprepare_new_request__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁHTTPSessionǁprepare_new_request__mutmut_1': xǁHTTPSessionǁprepare_new_request__mutmut_1, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_2': xǁHTTPSessionǁprepare_new_request__mutmut_2, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_3': xǁHTTPSessionǁprepare_new_request__mutmut_3, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_4': xǁHTTPSessionǁprepare_new_request__mutmut_4, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_5': xǁHTTPSessionǁprepare_new_request__mutmut_5, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_6': xǁHTTPSessionǁprepare_new_request__mutmut_6, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_7': xǁHTTPSessionǁprepare_new_request__mutmut_7, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_8': xǁHTTPSessionǁprepare_new_request__mutmut_8, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_9': xǁHTTPSessionǁprepare_new_request__mutmut_9, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_10': xǁHTTPSessionǁprepare_new_request__mutmut_10, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_11': xǁHTTPSessionǁprepare_new_request__mutmut_11, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_12': xǁHTTPSessionǁprepare_new_request__mutmut_12, 
        'xǁHTTPSessionǁprepare_new_request__mutmut_13': xǁHTTPSessionǁprepare_new_request__mutmut_13
    }
    
    def prepare_new_request(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁHTTPSessionǁprepare_new_request__mutmut_orig"), object.__getattribute__(self, "xǁHTTPSessionǁprepare_new_request__mutmut_mutants"), args, kwargs, self)
        return result 
    
    prepare_new_request.__signature__ = _mutmut_signature(xǁHTTPSessionǁprepare_new_request__mutmut_orig)
    xǁHTTPSessionǁprepare_new_request__mutmut_orig.__name__ = 'xǁHTTPSessionǁprepare_new_request'

    def xǁHTTPSessionǁrequest__mutmut_orig(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_1(self, method, url, *args, **kwargs):
        acceptable_status = None
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_2(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop(None, [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_3(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", None)
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_4(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop([])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_5(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", )
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_6(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("XXacceptable_statusXX", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_7(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("ACCEPTABLE_STATUS", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_8(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("Acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_9(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = None
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_10(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop(None, None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_11(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop(None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_12(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", )
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_13(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("XXencodingXX", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_14(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("ENCODING", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_15(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("Encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_16(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = None
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_17(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop(None, PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_18(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", None)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_19(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop(PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_20(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", )
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_21(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("XXexceptionXX", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_22(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("EXCEPTION", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_23(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("Exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_24(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = None
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_25(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop(None, {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_26(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", None)
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_27(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop({})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_28(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", )
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_29(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("XXheadersXX", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_30(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("HEADERS", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_31(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("Headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_32(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = None
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_33(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop(None, {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_34(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", None)
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_35(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop({})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_36(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", )
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_37(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("XXparamsXX", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_38(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("PARAMS", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_39(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("Params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_40(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = None
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_41(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop(None, self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_42(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", None)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_43(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop(self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_44(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", )
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_45(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("XXproxiesXX", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_46(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("PROXIES", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_47(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("Proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_48(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = None
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_49(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop(None, True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_50(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", None)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_51(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop(True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_52(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", )
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_53(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("XXraise_for_statusXX", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_54(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("RAISE_FOR_STATUS", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_55(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("Raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_56(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", False)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_57(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = None
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_58(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop(None, None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_59(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop(None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_60(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", )
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_61(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("XXschemaXX", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_62(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("SCHEMA", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_63(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("Schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_64(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = None
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_65(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop(None, None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_66(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop(None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_67(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", )
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_68(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("XXsessionXX", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_69(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("SESSION", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_70(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("Session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_71(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = None
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_72(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop(None, self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_73(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", None)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_74(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop(self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_75(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", )
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_76(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("XXtimeoutXX", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_77(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("TIMEOUT", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_78(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("Timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_79(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = None
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_80(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop(None, 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_81(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", None)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_82(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop(0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_83(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", )
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_84(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("XXretriesXX", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_85(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("RETRIES", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_86(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("Retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_87(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 1)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_88(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = None
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_89(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop(None, 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_90(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", None)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_91(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop(0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_92(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", )
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_93(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("XXretry_backoffXX", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_94(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("RETRY_BACKOFF", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_95(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("Retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_96(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 1.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_97(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = None
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_98(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop(None, 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_99(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", None)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_100(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop(10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_101(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", )
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_102(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("XXretry_max_backoffXX", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_103(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("RETRY_MAX_BACKOFF", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_104(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("Retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_105(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 11.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_106(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = None

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_107(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 1

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_108(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(None)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_109(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(None)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_110(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while False:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_111(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = None
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_112(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    None,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_113(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    None,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_114(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=None,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_115(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=None,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_116(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=None,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_117(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=None,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_118(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_119(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_120(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_121(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_122(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_123(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_124(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_125(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_126(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status or res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_127(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_128(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                return
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_129(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries > total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_130(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = None
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_131(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(None)
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_132(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = None
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_133(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries = 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_134(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries -= 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_135(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 2
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_136(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = None
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_137(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(None, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_138(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, None)
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_139(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_140(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, )
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_141(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff / (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_142(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (3 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_143(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 * (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_144(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries + 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_145(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 2)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_146(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(None)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_147(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_148(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = None

        if schema:
            res = schema.validate(res.text, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_149(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = None

        return res

    def xǁHTTPSessionǁrequest__mutmut_150(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(None, name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_151(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name=None, exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_152(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", exception=None)

        return res

    def xǁHTTPSessionǁrequest__mutmut_153(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(name="response text", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_154(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_155(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="response text", )

        return res

    def xǁHTTPSessionǁrequest__mutmut_156(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="XXresponse textXX", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_157(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="RESPONSE TEXT", exception=PluginError)

        return res

    def xǁHTTPSessionǁrequest__mutmut_158(self, method, url, *args, **kwargs):
        acceptable_status = kwargs.pop("acceptable_status", [])
        encoding = kwargs.pop("encoding", None)
        exception = kwargs.pop("exception", PluginError)
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        proxies = kwargs.pop("proxies", self.proxies)
        raise_for_status = kwargs.pop("raise_for_status", True)
        schema = kwargs.pop("schema", None)
        session = kwargs.pop("session", None)
        timeout = kwargs.pop("timeout", self.timeout)
        total_retries = kwargs.pop("retries", 0)
        retry_backoff = kwargs.pop("retry_backoff", 0.3)
        retry_max_backoff = kwargs.pop("retry_max_backoff", 10.0)
        retries = 0

        if session:
            headers.update(session.headers)
            params.update(session.params)

        while True:
            try:
                res = super().request(
                    method,
                    url,
                    *args,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    proxies=proxies,
                    **kwargs,
                )
                if raise_for_status and res.status_code not in acceptable_status:
                    res.raise_for_status()
                break
            except KeyboardInterrupt:
                raise
            except Exception as rerr:
                if retries >= total_retries:
                    err = exception(f"Unable to open URL: {url} ({rerr})")
                    err.err = rerr
                    raise err from None  # TODO: fix this
                retries += 1
                # back off retrying, but only to a maximum sleep time
                delay = min(retry_max_backoff, retry_backoff * (2 ** (retries - 1)))
                time.sleep(delay)

        if encoding is not None:
            res.encoding = encoding

        if schema:
            res = schema.validate(res.text, name="Response text", exception=PluginError)

        return res
    
    xǁHTTPSessionǁrequest__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁHTTPSessionǁrequest__mutmut_1': xǁHTTPSessionǁrequest__mutmut_1, 
        'xǁHTTPSessionǁrequest__mutmut_2': xǁHTTPSessionǁrequest__mutmut_2, 
        'xǁHTTPSessionǁrequest__mutmut_3': xǁHTTPSessionǁrequest__mutmut_3, 
        'xǁHTTPSessionǁrequest__mutmut_4': xǁHTTPSessionǁrequest__mutmut_4, 
        'xǁHTTPSessionǁrequest__mutmut_5': xǁHTTPSessionǁrequest__mutmut_5, 
        'xǁHTTPSessionǁrequest__mutmut_6': xǁHTTPSessionǁrequest__mutmut_6, 
        'xǁHTTPSessionǁrequest__mutmut_7': xǁHTTPSessionǁrequest__mutmut_7, 
        'xǁHTTPSessionǁrequest__mutmut_8': xǁHTTPSessionǁrequest__mutmut_8, 
        'xǁHTTPSessionǁrequest__mutmut_9': xǁHTTPSessionǁrequest__mutmut_9, 
        'xǁHTTPSessionǁrequest__mutmut_10': xǁHTTPSessionǁrequest__mutmut_10, 
        'xǁHTTPSessionǁrequest__mutmut_11': xǁHTTPSessionǁrequest__mutmut_11, 
        'xǁHTTPSessionǁrequest__mutmut_12': xǁHTTPSessionǁrequest__mutmut_12, 
        'xǁHTTPSessionǁrequest__mutmut_13': xǁHTTPSessionǁrequest__mutmut_13, 
        'xǁHTTPSessionǁrequest__mutmut_14': xǁHTTPSessionǁrequest__mutmut_14, 
        'xǁHTTPSessionǁrequest__mutmut_15': xǁHTTPSessionǁrequest__mutmut_15, 
        'xǁHTTPSessionǁrequest__mutmut_16': xǁHTTPSessionǁrequest__mutmut_16, 
        'xǁHTTPSessionǁrequest__mutmut_17': xǁHTTPSessionǁrequest__mutmut_17, 
        'xǁHTTPSessionǁrequest__mutmut_18': xǁHTTPSessionǁrequest__mutmut_18, 
        'xǁHTTPSessionǁrequest__mutmut_19': xǁHTTPSessionǁrequest__mutmut_19, 
        'xǁHTTPSessionǁrequest__mutmut_20': xǁHTTPSessionǁrequest__mutmut_20, 
        'xǁHTTPSessionǁrequest__mutmut_21': xǁHTTPSessionǁrequest__mutmut_21, 
        'xǁHTTPSessionǁrequest__mutmut_22': xǁHTTPSessionǁrequest__mutmut_22, 
        'xǁHTTPSessionǁrequest__mutmut_23': xǁHTTPSessionǁrequest__mutmut_23, 
        'xǁHTTPSessionǁrequest__mutmut_24': xǁHTTPSessionǁrequest__mutmut_24, 
        'xǁHTTPSessionǁrequest__mutmut_25': xǁHTTPSessionǁrequest__mutmut_25, 
        'xǁHTTPSessionǁrequest__mutmut_26': xǁHTTPSessionǁrequest__mutmut_26, 
        'xǁHTTPSessionǁrequest__mutmut_27': xǁHTTPSessionǁrequest__mutmut_27, 
        'xǁHTTPSessionǁrequest__mutmut_28': xǁHTTPSessionǁrequest__mutmut_28, 
        'xǁHTTPSessionǁrequest__mutmut_29': xǁHTTPSessionǁrequest__mutmut_29, 
        'xǁHTTPSessionǁrequest__mutmut_30': xǁHTTPSessionǁrequest__mutmut_30, 
        'xǁHTTPSessionǁrequest__mutmut_31': xǁHTTPSessionǁrequest__mutmut_31, 
        'xǁHTTPSessionǁrequest__mutmut_32': xǁHTTPSessionǁrequest__mutmut_32, 
        'xǁHTTPSessionǁrequest__mutmut_33': xǁHTTPSessionǁrequest__mutmut_33, 
        'xǁHTTPSessionǁrequest__mutmut_34': xǁHTTPSessionǁrequest__mutmut_34, 
        'xǁHTTPSessionǁrequest__mutmut_35': xǁHTTPSessionǁrequest__mutmut_35, 
        'xǁHTTPSessionǁrequest__mutmut_36': xǁHTTPSessionǁrequest__mutmut_36, 
        'xǁHTTPSessionǁrequest__mutmut_37': xǁHTTPSessionǁrequest__mutmut_37, 
        'xǁHTTPSessionǁrequest__mutmut_38': xǁHTTPSessionǁrequest__mutmut_38, 
        'xǁHTTPSessionǁrequest__mutmut_39': xǁHTTPSessionǁrequest__mutmut_39, 
        'xǁHTTPSessionǁrequest__mutmut_40': xǁHTTPSessionǁrequest__mutmut_40, 
        'xǁHTTPSessionǁrequest__mutmut_41': xǁHTTPSessionǁrequest__mutmut_41, 
        'xǁHTTPSessionǁrequest__mutmut_42': xǁHTTPSessionǁrequest__mutmut_42, 
        'xǁHTTPSessionǁrequest__mutmut_43': xǁHTTPSessionǁrequest__mutmut_43, 
        'xǁHTTPSessionǁrequest__mutmut_44': xǁHTTPSessionǁrequest__mutmut_44, 
        'xǁHTTPSessionǁrequest__mutmut_45': xǁHTTPSessionǁrequest__mutmut_45, 
        'xǁHTTPSessionǁrequest__mutmut_46': xǁHTTPSessionǁrequest__mutmut_46, 
        'xǁHTTPSessionǁrequest__mutmut_47': xǁHTTPSessionǁrequest__mutmut_47, 
        'xǁHTTPSessionǁrequest__mutmut_48': xǁHTTPSessionǁrequest__mutmut_48, 
        'xǁHTTPSessionǁrequest__mutmut_49': xǁHTTPSessionǁrequest__mutmut_49, 
        'xǁHTTPSessionǁrequest__mutmut_50': xǁHTTPSessionǁrequest__mutmut_50, 
        'xǁHTTPSessionǁrequest__mutmut_51': xǁHTTPSessionǁrequest__mutmut_51, 
        'xǁHTTPSessionǁrequest__mutmut_52': xǁHTTPSessionǁrequest__mutmut_52, 
        'xǁHTTPSessionǁrequest__mutmut_53': xǁHTTPSessionǁrequest__mutmut_53, 
        'xǁHTTPSessionǁrequest__mutmut_54': xǁHTTPSessionǁrequest__mutmut_54, 
        'xǁHTTPSessionǁrequest__mutmut_55': xǁHTTPSessionǁrequest__mutmut_55, 
        'xǁHTTPSessionǁrequest__mutmut_56': xǁHTTPSessionǁrequest__mutmut_56, 
        'xǁHTTPSessionǁrequest__mutmut_57': xǁHTTPSessionǁrequest__mutmut_57, 
        'xǁHTTPSessionǁrequest__mutmut_58': xǁHTTPSessionǁrequest__mutmut_58, 
        'xǁHTTPSessionǁrequest__mutmut_59': xǁHTTPSessionǁrequest__mutmut_59, 
        'xǁHTTPSessionǁrequest__mutmut_60': xǁHTTPSessionǁrequest__mutmut_60, 
        'xǁHTTPSessionǁrequest__mutmut_61': xǁHTTPSessionǁrequest__mutmut_61, 
        'xǁHTTPSessionǁrequest__mutmut_62': xǁHTTPSessionǁrequest__mutmut_62, 
        'xǁHTTPSessionǁrequest__mutmut_63': xǁHTTPSessionǁrequest__mutmut_63, 
        'xǁHTTPSessionǁrequest__mutmut_64': xǁHTTPSessionǁrequest__mutmut_64, 
        'xǁHTTPSessionǁrequest__mutmut_65': xǁHTTPSessionǁrequest__mutmut_65, 
        'xǁHTTPSessionǁrequest__mutmut_66': xǁHTTPSessionǁrequest__mutmut_66, 
        'xǁHTTPSessionǁrequest__mutmut_67': xǁHTTPSessionǁrequest__mutmut_67, 
        'xǁHTTPSessionǁrequest__mutmut_68': xǁHTTPSessionǁrequest__mutmut_68, 
        'xǁHTTPSessionǁrequest__mutmut_69': xǁHTTPSessionǁrequest__mutmut_69, 
        'xǁHTTPSessionǁrequest__mutmut_70': xǁHTTPSessionǁrequest__mutmut_70, 
        'xǁHTTPSessionǁrequest__mutmut_71': xǁHTTPSessionǁrequest__mutmut_71, 
        'xǁHTTPSessionǁrequest__mutmut_72': xǁHTTPSessionǁrequest__mutmut_72, 
        'xǁHTTPSessionǁrequest__mutmut_73': xǁHTTPSessionǁrequest__mutmut_73, 
        'xǁHTTPSessionǁrequest__mutmut_74': xǁHTTPSessionǁrequest__mutmut_74, 
        'xǁHTTPSessionǁrequest__mutmut_75': xǁHTTPSessionǁrequest__mutmut_75, 
        'xǁHTTPSessionǁrequest__mutmut_76': xǁHTTPSessionǁrequest__mutmut_76, 
        'xǁHTTPSessionǁrequest__mutmut_77': xǁHTTPSessionǁrequest__mutmut_77, 
        'xǁHTTPSessionǁrequest__mutmut_78': xǁHTTPSessionǁrequest__mutmut_78, 
        'xǁHTTPSessionǁrequest__mutmut_79': xǁHTTPSessionǁrequest__mutmut_79, 
        'xǁHTTPSessionǁrequest__mutmut_80': xǁHTTPSessionǁrequest__mutmut_80, 
        'xǁHTTPSessionǁrequest__mutmut_81': xǁHTTPSessionǁrequest__mutmut_81, 
        'xǁHTTPSessionǁrequest__mutmut_82': xǁHTTPSessionǁrequest__mutmut_82, 
        'xǁHTTPSessionǁrequest__mutmut_83': xǁHTTPSessionǁrequest__mutmut_83, 
        'xǁHTTPSessionǁrequest__mutmut_84': xǁHTTPSessionǁrequest__mutmut_84, 
        'xǁHTTPSessionǁrequest__mutmut_85': xǁHTTPSessionǁrequest__mutmut_85, 
        'xǁHTTPSessionǁrequest__mutmut_86': xǁHTTPSessionǁrequest__mutmut_86, 
        'xǁHTTPSessionǁrequest__mutmut_87': xǁHTTPSessionǁrequest__mutmut_87, 
        'xǁHTTPSessionǁrequest__mutmut_88': xǁHTTPSessionǁrequest__mutmut_88, 
        'xǁHTTPSessionǁrequest__mutmut_89': xǁHTTPSessionǁrequest__mutmut_89, 
        'xǁHTTPSessionǁrequest__mutmut_90': xǁHTTPSessionǁrequest__mutmut_90, 
        'xǁHTTPSessionǁrequest__mutmut_91': xǁHTTPSessionǁrequest__mutmut_91, 
        'xǁHTTPSessionǁrequest__mutmut_92': xǁHTTPSessionǁrequest__mutmut_92, 
        'xǁHTTPSessionǁrequest__mutmut_93': xǁHTTPSessionǁrequest__mutmut_93, 
        'xǁHTTPSessionǁrequest__mutmut_94': xǁHTTPSessionǁrequest__mutmut_94, 
        'xǁHTTPSessionǁrequest__mutmut_95': xǁHTTPSessionǁrequest__mutmut_95, 
        'xǁHTTPSessionǁrequest__mutmut_96': xǁHTTPSessionǁrequest__mutmut_96, 
        'xǁHTTPSessionǁrequest__mutmut_97': xǁHTTPSessionǁrequest__mutmut_97, 
        'xǁHTTPSessionǁrequest__mutmut_98': xǁHTTPSessionǁrequest__mutmut_98, 
        'xǁHTTPSessionǁrequest__mutmut_99': xǁHTTPSessionǁrequest__mutmut_99, 
        'xǁHTTPSessionǁrequest__mutmut_100': xǁHTTPSessionǁrequest__mutmut_100, 
        'xǁHTTPSessionǁrequest__mutmut_101': xǁHTTPSessionǁrequest__mutmut_101, 
        'xǁHTTPSessionǁrequest__mutmut_102': xǁHTTPSessionǁrequest__mutmut_102, 
        'xǁHTTPSessionǁrequest__mutmut_103': xǁHTTPSessionǁrequest__mutmut_103, 
        'xǁHTTPSessionǁrequest__mutmut_104': xǁHTTPSessionǁrequest__mutmut_104, 
        'xǁHTTPSessionǁrequest__mutmut_105': xǁHTTPSessionǁrequest__mutmut_105, 
        'xǁHTTPSessionǁrequest__mutmut_106': xǁHTTPSessionǁrequest__mutmut_106, 
        'xǁHTTPSessionǁrequest__mutmut_107': xǁHTTPSessionǁrequest__mutmut_107, 
        'xǁHTTPSessionǁrequest__mutmut_108': xǁHTTPSessionǁrequest__mutmut_108, 
        'xǁHTTPSessionǁrequest__mutmut_109': xǁHTTPSessionǁrequest__mutmut_109, 
        'xǁHTTPSessionǁrequest__mutmut_110': xǁHTTPSessionǁrequest__mutmut_110, 
        'xǁHTTPSessionǁrequest__mutmut_111': xǁHTTPSessionǁrequest__mutmut_111, 
        'xǁHTTPSessionǁrequest__mutmut_112': xǁHTTPSessionǁrequest__mutmut_112, 
        'xǁHTTPSessionǁrequest__mutmut_113': xǁHTTPSessionǁrequest__mutmut_113, 
        'xǁHTTPSessionǁrequest__mutmut_114': xǁHTTPSessionǁrequest__mutmut_114, 
        'xǁHTTPSessionǁrequest__mutmut_115': xǁHTTPSessionǁrequest__mutmut_115, 
        'xǁHTTPSessionǁrequest__mutmut_116': xǁHTTPSessionǁrequest__mutmut_116, 
        'xǁHTTPSessionǁrequest__mutmut_117': xǁHTTPSessionǁrequest__mutmut_117, 
        'xǁHTTPSessionǁrequest__mutmut_118': xǁHTTPSessionǁrequest__mutmut_118, 
        'xǁHTTPSessionǁrequest__mutmut_119': xǁHTTPSessionǁrequest__mutmut_119, 
        'xǁHTTPSessionǁrequest__mutmut_120': xǁHTTPSessionǁrequest__mutmut_120, 
        'xǁHTTPSessionǁrequest__mutmut_121': xǁHTTPSessionǁrequest__mutmut_121, 
        'xǁHTTPSessionǁrequest__mutmut_122': xǁHTTPSessionǁrequest__mutmut_122, 
        'xǁHTTPSessionǁrequest__mutmut_123': xǁHTTPSessionǁrequest__mutmut_123, 
        'xǁHTTPSessionǁrequest__mutmut_124': xǁHTTPSessionǁrequest__mutmut_124, 
        'xǁHTTPSessionǁrequest__mutmut_125': xǁHTTPSessionǁrequest__mutmut_125, 
        'xǁHTTPSessionǁrequest__mutmut_126': xǁHTTPSessionǁrequest__mutmut_126, 
        'xǁHTTPSessionǁrequest__mutmut_127': xǁHTTPSessionǁrequest__mutmut_127, 
        'xǁHTTPSessionǁrequest__mutmut_128': xǁHTTPSessionǁrequest__mutmut_128, 
        'xǁHTTPSessionǁrequest__mutmut_129': xǁHTTPSessionǁrequest__mutmut_129, 
        'xǁHTTPSessionǁrequest__mutmut_130': xǁHTTPSessionǁrequest__mutmut_130, 
        'xǁHTTPSessionǁrequest__mutmut_131': xǁHTTPSessionǁrequest__mutmut_131, 
        'xǁHTTPSessionǁrequest__mutmut_132': xǁHTTPSessionǁrequest__mutmut_132, 
        'xǁHTTPSessionǁrequest__mutmut_133': xǁHTTPSessionǁrequest__mutmut_133, 
        'xǁHTTPSessionǁrequest__mutmut_134': xǁHTTPSessionǁrequest__mutmut_134, 
        'xǁHTTPSessionǁrequest__mutmut_135': xǁHTTPSessionǁrequest__mutmut_135, 
        'xǁHTTPSessionǁrequest__mutmut_136': xǁHTTPSessionǁrequest__mutmut_136, 
        'xǁHTTPSessionǁrequest__mutmut_137': xǁHTTPSessionǁrequest__mutmut_137, 
        'xǁHTTPSessionǁrequest__mutmut_138': xǁHTTPSessionǁrequest__mutmut_138, 
        'xǁHTTPSessionǁrequest__mutmut_139': xǁHTTPSessionǁrequest__mutmut_139, 
        'xǁHTTPSessionǁrequest__mutmut_140': xǁHTTPSessionǁrequest__mutmut_140, 
        'xǁHTTPSessionǁrequest__mutmut_141': xǁHTTPSessionǁrequest__mutmut_141, 
        'xǁHTTPSessionǁrequest__mutmut_142': xǁHTTPSessionǁrequest__mutmut_142, 
        'xǁHTTPSessionǁrequest__mutmut_143': xǁHTTPSessionǁrequest__mutmut_143, 
        'xǁHTTPSessionǁrequest__mutmut_144': xǁHTTPSessionǁrequest__mutmut_144, 
        'xǁHTTPSessionǁrequest__mutmut_145': xǁHTTPSessionǁrequest__mutmut_145, 
        'xǁHTTPSessionǁrequest__mutmut_146': xǁHTTPSessionǁrequest__mutmut_146, 
        'xǁHTTPSessionǁrequest__mutmut_147': xǁHTTPSessionǁrequest__mutmut_147, 
        'xǁHTTPSessionǁrequest__mutmut_148': xǁHTTPSessionǁrequest__mutmut_148, 
        'xǁHTTPSessionǁrequest__mutmut_149': xǁHTTPSessionǁrequest__mutmut_149, 
        'xǁHTTPSessionǁrequest__mutmut_150': xǁHTTPSessionǁrequest__mutmut_150, 
        'xǁHTTPSessionǁrequest__mutmut_151': xǁHTTPSessionǁrequest__mutmut_151, 
        'xǁHTTPSessionǁrequest__mutmut_152': xǁHTTPSessionǁrequest__mutmut_152, 
        'xǁHTTPSessionǁrequest__mutmut_153': xǁHTTPSessionǁrequest__mutmut_153, 
        'xǁHTTPSessionǁrequest__mutmut_154': xǁHTTPSessionǁrequest__mutmut_154, 
        'xǁHTTPSessionǁrequest__mutmut_155': xǁHTTPSessionǁrequest__mutmut_155, 
        'xǁHTTPSessionǁrequest__mutmut_156': xǁHTTPSessionǁrequest__mutmut_156, 
        'xǁHTTPSessionǁrequest__mutmut_157': xǁHTTPSessionǁrequest__mutmut_157, 
        'xǁHTTPSessionǁrequest__mutmut_158': xǁHTTPSessionǁrequest__mutmut_158
    }
    
    def request(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁHTTPSessionǁrequest__mutmut_orig"), object.__getattribute__(self, "xǁHTTPSessionǁrequest__mutmut_mutants"), args, kwargs, self)
        return result 
    
    request.__signature__ = _mutmut_signature(xǁHTTPSessionǁrequest__mutmut_orig)
    xǁHTTPSessionǁrequest__mutmut_orig.__name__ = 'xǁHTTPSessionǁrequest'


class SSLContextAdapter(HTTPAdapter):
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_orig(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!SHA1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_1(self) -> ssl.SSLContext:
        ctx = None
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!SHA1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_2(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = None
        ciphers += ":!SHA1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_3(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(None)
        ciphers += ":!SHA1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_4(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = "XX:XX".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!SHA1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_5(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["XXnameXX"] for cipher in ctx.get_ciphers())
        ciphers += ":!SHA1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_6(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["NAME"] for cipher in ctx.get_ciphers())
        ciphers += ":!SHA1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_7(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["Name"] for cipher in ctx.get_ciphers())
        ciphers += ":!SHA1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_8(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers = ":!SHA1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_9(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers -= ":!SHA1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_10(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += "XX:!SHA1XX"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_11(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!sha1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_12(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!sha1"
        ctx.set_ciphers(ciphers)

        return ctx
    # noinspection PyMethodMayBeStatic
    def xǁSSLContextAdapterǁget_ssl_context__mutmut_13(self) -> ssl.SSLContext:
        ctx = create_urllib3_context()
        ctx.load_default_certs()

        # disable weak digest ciphers by default
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!SHA1"
        ctx.set_ciphers(None)

        return ctx
    
    xǁSSLContextAdapterǁget_ssl_context__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSSLContextAdapterǁget_ssl_context__mutmut_1': xǁSSLContextAdapterǁget_ssl_context__mutmut_1, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_2': xǁSSLContextAdapterǁget_ssl_context__mutmut_2, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_3': xǁSSLContextAdapterǁget_ssl_context__mutmut_3, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_4': xǁSSLContextAdapterǁget_ssl_context__mutmut_4, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_5': xǁSSLContextAdapterǁget_ssl_context__mutmut_5, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_6': xǁSSLContextAdapterǁget_ssl_context__mutmut_6, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_7': xǁSSLContextAdapterǁget_ssl_context__mutmut_7, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_8': xǁSSLContextAdapterǁget_ssl_context__mutmut_8, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_9': xǁSSLContextAdapterǁget_ssl_context__mutmut_9, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_10': xǁSSLContextAdapterǁget_ssl_context__mutmut_10, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_11': xǁSSLContextAdapterǁget_ssl_context__mutmut_11, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_12': xǁSSLContextAdapterǁget_ssl_context__mutmut_12, 
        'xǁSSLContextAdapterǁget_ssl_context__mutmut_13': xǁSSLContextAdapterǁget_ssl_context__mutmut_13
    }
    
    def get_ssl_context(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSSLContextAdapterǁget_ssl_context__mutmut_orig"), object.__getattribute__(self, "xǁSSLContextAdapterǁget_ssl_context__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_ssl_context.__signature__ = _mutmut_signature(xǁSSLContextAdapterǁget_ssl_context__mutmut_orig)
    xǁSSLContextAdapterǁget_ssl_context__mutmut_orig.__name__ = 'xǁSSLContextAdapterǁget_ssl_context'

    def xǁSSLContextAdapterǁinit_poolmanager__mutmut_orig(self, *args, **kwargs):
        kwargs["ssl_context"] = self.get_ssl_context()
        return super().init_poolmanager(*args, **kwargs)

    def xǁSSLContextAdapterǁinit_poolmanager__mutmut_1(self, *args, **kwargs):
        kwargs["ssl_context"] = None
        return super().init_poolmanager(*args, **kwargs)

    def xǁSSLContextAdapterǁinit_poolmanager__mutmut_2(self, *args, **kwargs):
        kwargs["XXssl_contextXX"] = self.get_ssl_context()
        return super().init_poolmanager(*args, **kwargs)

    def xǁSSLContextAdapterǁinit_poolmanager__mutmut_3(self, *args, **kwargs):
        kwargs["SSL_CONTEXT"] = self.get_ssl_context()
        return super().init_poolmanager(*args, **kwargs)

    def xǁSSLContextAdapterǁinit_poolmanager__mutmut_4(self, *args, **kwargs):
        kwargs["Ssl_context"] = self.get_ssl_context()
        return super().init_poolmanager(*args, **kwargs)

    def xǁSSLContextAdapterǁinit_poolmanager__mutmut_5(self, *args, **kwargs):
        kwargs["ssl_context"] = self.get_ssl_context()
        return super().init_poolmanager(**kwargs)

    def xǁSSLContextAdapterǁinit_poolmanager__mutmut_6(self, *args, **kwargs):
        kwargs["ssl_context"] = self.get_ssl_context()
        return super().init_poolmanager(*args, )
    
    xǁSSLContextAdapterǁinit_poolmanager__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSSLContextAdapterǁinit_poolmanager__mutmut_1': xǁSSLContextAdapterǁinit_poolmanager__mutmut_1, 
        'xǁSSLContextAdapterǁinit_poolmanager__mutmut_2': xǁSSLContextAdapterǁinit_poolmanager__mutmut_2, 
        'xǁSSLContextAdapterǁinit_poolmanager__mutmut_3': xǁSSLContextAdapterǁinit_poolmanager__mutmut_3, 
        'xǁSSLContextAdapterǁinit_poolmanager__mutmut_4': xǁSSLContextAdapterǁinit_poolmanager__mutmut_4, 
        'xǁSSLContextAdapterǁinit_poolmanager__mutmut_5': xǁSSLContextAdapterǁinit_poolmanager__mutmut_5, 
        'xǁSSLContextAdapterǁinit_poolmanager__mutmut_6': xǁSSLContextAdapterǁinit_poolmanager__mutmut_6
    }
    
    def init_poolmanager(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSSLContextAdapterǁinit_poolmanager__mutmut_orig"), object.__getattribute__(self, "xǁSSLContextAdapterǁinit_poolmanager__mutmut_mutants"), args, kwargs, self)
        return result 
    
    init_poolmanager.__signature__ = _mutmut_signature(xǁSSLContextAdapterǁinit_poolmanager__mutmut_orig)
    xǁSSLContextAdapterǁinit_poolmanager__mutmut_orig.__name__ = 'xǁSSLContextAdapterǁinit_poolmanager'

    def xǁSSLContextAdapterǁproxy_manager_for__mutmut_orig(self, *args, **kwargs):
        kwargs["ssl_context"] = self.poolmanager.connection_pool_kw["ssl_context"]
        return super().proxy_manager_for(*args, **kwargs)

    def xǁSSLContextAdapterǁproxy_manager_for__mutmut_1(self, *args, **kwargs):
        kwargs["ssl_context"] = None
        return super().proxy_manager_for(*args, **kwargs)

    def xǁSSLContextAdapterǁproxy_manager_for__mutmut_2(self, *args, **kwargs):
        kwargs["XXssl_contextXX"] = self.poolmanager.connection_pool_kw["ssl_context"]
        return super().proxy_manager_for(*args, **kwargs)

    def xǁSSLContextAdapterǁproxy_manager_for__mutmut_3(self, *args, **kwargs):
        kwargs["SSL_CONTEXT"] = self.poolmanager.connection_pool_kw["ssl_context"]
        return super().proxy_manager_for(*args, **kwargs)

    def xǁSSLContextAdapterǁproxy_manager_for__mutmut_4(self, *args, **kwargs):
        kwargs["Ssl_context"] = self.poolmanager.connection_pool_kw["ssl_context"]
        return super().proxy_manager_for(*args, **kwargs)

    def xǁSSLContextAdapterǁproxy_manager_for__mutmut_5(self, *args, **kwargs):
        kwargs["ssl_context"] = self.poolmanager.connection_pool_kw["XXssl_contextXX"]
        return super().proxy_manager_for(*args, **kwargs)

    def xǁSSLContextAdapterǁproxy_manager_for__mutmut_6(self, *args, **kwargs):
        kwargs["ssl_context"] = self.poolmanager.connection_pool_kw["SSL_CONTEXT"]
        return super().proxy_manager_for(*args, **kwargs)

    def xǁSSLContextAdapterǁproxy_manager_for__mutmut_7(self, *args, **kwargs):
        kwargs["ssl_context"] = self.poolmanager.connection_pool_kw["Ssl_context"]
        return super().proxy_manager_for(*args, **kwargs)

    def xǁSSLContextAdapterǁproxy_manager_for__mutmut_8(self, *args, **kwargs):
        kwargs["ssl_context"] = self.poolmanager.connection_pool_kw["ssl_context"]
        return super().proxy_manager_for(**kwargs)

    def xǁSSLContextAdapterǁproxy_manager_for__mutmut_9(self, *args, **kwargs):
        kwargs["ssl_context"] = self.poolmanager.connection_pool_kw["ssl_context"]
        return super().proxy_manager_for(*args, )
    
    xǁSSLContextAdapterǁproxy_manager_for__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSSLContextAdapterǁproxy_manager_for__mutmut_1': xǁSSLContextAdapterǁproxy_manager_for__mutmut_1, 
        'xǁSSLContextAdapterǁproxy_manager_for__mutmut_2': xǁSSLContextAdapterǁproxy_manager_for__mutmut_2, 
        'xǁSSLContextAdapterǁproxy_manager_for__mutmut_3': xǁSSLContextAdapterǁproxy_manager_for__mutmut_3, 
        'xǁSSLContextAdapterǁproxy_manager_for__mutmut_4': xǁSSLContextAdapterǁproxy_manager_for__mutmut_4, 
        'xǁSSLContextAdapterǁproxy_manager_for__mutmut_5': xǁSSLContextAdapterǁproxy_manager_for__mutmut_5, 
        'xǁSSLContextAdapterǁproxy_manager_for__mutmut_6': xǁSSLContextAdapterǁproxy_manager_for__mutmut_6, 
        'xǁSSLContextAdapterǁproxy_manager_for__mutmut_7': xǁSSLContextAdapterǁproxy_manager_for__mutmut_7, 
        'xǁSSLContextAdapterǁproxy_manager_for__mutmut_8': xǁSSLContextAdapterǁproxy_manager_for__mutmut_8, 
        'xǁSSLContextAdapterǁproxy_manager_for__mutmut_9': xǁSSLContextAdapterǁproxy_manager_for__mutmut_9
    }
    
    def proxy_manager_for(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSSLContextAdapterǁproxy_manager_for__mutmut_orig"), object.__getattribute__(self, "xǁSSLContextAdapterǁproxy_manager_for__mutmut_mutants"), args, kwargs, self)
        return result 
    
    proxy_manager_for.__signature__ = _mutmut_signature(xǁSSLContextAdapterǁproxy_manager_for__mutmut_orig)
    xǁSSLContextAdapterǁproxy_manager_for__mutmut_orig.__name__ = 'xǁSSLContextAdapterǁproxy_manager_for'

    def xǁSSLContextAdapterǁsend__mutmut_orig(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_1(self, *args, verify=False, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_2(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get(None):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_3(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("XXssl_contextXX"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_4(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("SSL_CONTEXT"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_5(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("Ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_6(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = None
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_7(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = bool(None)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_8(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = None
        return super().send(*args, verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_9(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_10(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=None, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_11(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(verify=verify, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_12(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, **kwargs)

    def xǁSSLContextAdapterǁsend__mutmut_13(self, *args, verify=True, **kwargs):
        # Always update the `check_hostname` and `verify_mode` attributes of our custom `SSLContext` before sending a request:
        # If `verify` is `False`, then `requests` will set `cert_reqs=ssl.CERT_NONE` on the `HTTPSConnectionPool` object,
        # which leads to `SSLContext` incompatibilities later on in `urllib3.connection._ssl_wrap_socket_and_match_hostname()`
        # due to the default values of our `SSLContext`, namely `check_hostname=True` and `verify_mode=ssl.CERT_REQUIRED`.
        if ssl_context := self.poolmanager.connection_pool_kw.get("ssl_context"):  # pragma: no branch
            ssl_context.check_hostname = bool(verify)
            ssl_context.verify_mode = ssl.CERT_NONE if not verify else ssl.CERT_REQUIRED
        return super().send(*args, verify=verify, )
    
    xǁSSLContextAdapterǁsend__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSSLContextAdapterǁsend__mutmut_1': xǁSSLContextAdapterǁsend__mutmut_1, 
        'xǁSSLContextAdapterǁsend__mutmut_2': xǁSSLContextAdapterǁsend__mutmut_2, 
        'xǁSSLContextAdapterǁsend__mutmut_3': xǁSSLContextAdapterǁsend__mutmut_3, 
        'xǁSSLContextAdapterǁsend__mutmut_4': xǁSSLContextAdapterǁsend__mutmut_4, 
        'xǁSSLContextAdapterǁsend__mutmut_5': xǁSSLContextAdapterǁsend__mutmut_5, 
        'xǁSSLContextAdapterǁsend__mutmut_6': xǁSSLContextAdapterǁsend__mutmut_6, 
        'xǁSSLContextAdapterǁsend__mutmut_7': xǁSSLContextAdapterǁsend__mutmut_7, 
        'xǁSSLContextAdapterǁsend__mutmut_8': xǁSSLContextAdapterǁsend__mutmut_8, 
        'xǁSSLContextAdapterǁsend__mutmut_9': xǁSSLContextAdapterǁsend__mutmut_9, 
        'xǁSSLContextAdapterǁsend__mutmut_10': xǁSSLContextAdapterǁsend__mutmut_10, 
        'xǁSSLContextAdapterǁsend__mutmut_11': xǁSSLContextAdapterǁsend__mutmut_11, 
        'xǁSSLContextAdapterǁsend__mutmut_12': xǁSSLContextAdapterǁsend__mutmut_12, 
        'xǁSSLContextAdapterǁsend__mutmut_13': xǁSSLContextAdapterǁsend__mutmut_13
    }
    
    def send(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSSLContextAdapterǁsend__mutmut_orig"), object.__getattribute__(self, "xǁSSLContextAdapterǁsend__mutmut_mutants"), args, kwargs, self)
        return result 
    
    send.__signature__ = _mutmut_signature(xǁSSLContextAdapterǁsend__mutmut_orig)
    xǁSSLContextAdapterǁsend__mutmut_orig.__name__ = 'xǁSSLContextAdapterǁsend'


class TLSNoDHAdapter(SSLContextAdapter):
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_orig(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!DH"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_1(self) -> ssl.SSLContext:
        ctx = None

        # disable DH ciphers
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!DH"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_2(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = None
        ciphers += ":!DH"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_3(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(None)
        ciphers += ":!DH"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_4(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = "XX:XX".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!DH"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_5(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(cipher["XXnameXX"] for cipher in ctx.get_ciphers())
        ciphers += ":!DH"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_6(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(cipher["NAME"] for cipher in ctx.get_ciphers())
        ciphers += ":!DH"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_7(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(cipher["Name"] for cipher in ctx.get_ciphers())
        ciphers += ":!DH"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_8(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers = ":!DH"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_9(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers -= ":!DH"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_10(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += "XX:!DHXX"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_11(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!dh"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_12(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!dh"
        ctx.set_ciphers(ciphers)

        return ctx
    def xǁTLSNoDHAdapterǁget_ssl_context__mutmut_13(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # disable DH ciphers
        ciphers = ":".join(cipher["name"] for cipher in ctx.get_ciphers())
        ciphers += ":!DH"
        ctx.set_ciphers(None)

        return ctx
    
    xǁTLSNoDHAdapterǁget_ssl_context__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_1': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_1, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_2': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_2, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_3': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_3, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_4': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_4, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_5': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_5, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_6': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_6, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_7': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_7, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_8': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_8, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_9': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_9, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_10': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_10, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_11': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_11, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_12': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_12, 
        'xǁTLSNoDHAdapterǁget_ssl_context__mutmut_13': xǁTLSNoDHAdapterǁget_ssl_context__mutmut_13
    }
    
    def get_ssl_context(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTLSNoDHAdapterǁget_ssl_context__mutmut_orig"), object.__getattribute__(self, "xǁTLSNoDHAdapterǁget_ssl_context__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_ssl_context.__signature__ = _mutmut_signature(xǁTLSNoDHAdapterǁget_ssl_context__mutmut_orig)
    xǁTLSNoDHAdapterǁget_ssl_context__mutmut_orig.__name__ = 'xǁTLSNoDHAdapterǁget_ssl_context'


class TLSSecLevel1Adapter(SSLContextAdapter):
    def xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_orig(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # https://www.openssl.org/docs/manmaster/man3/SSL_CTX_set_security_level.html
        ctx.set_ciphers("DEFAULT:@SECLEVEL=1")

        return ctx
    def xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_1(self) -> ssl.SSLContext:
        ctx = None

        # https://www.openssl.org/docs/manmaster/man3/SSL_CTX_set_security_level.html
        ctx.set_ciphers("DEFAULT:@SECLEVEL=1")

        return ctx
    def xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_2(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # https://www.openssl.org/docs/manmaster/man3/SSL_CTX_set_security_level.html
        ctx.set_ciphers(None)

        return ctx
    def xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_3(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # https://www.openssl.org/docs/manmaster/man3/SSL_CTX_set_security_level.html
        ctx.set_ciphers("XXDEFAULT:@SECLEVEL=1XX")

        return ctx
    def xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_4(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # https://www.openssl.org/docs/manmaster/man3/SSL_CTX_set_security_level.html
        ctx.set_ciphers("default:@seclevel=1")

        return ctx
    def xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_5(self) -> ssl.SSLContext:
        ctx = super().get_ssl_context()

        # https://www.openssl.org/docs/manmaster/man3/SSL_CTX_set_security_level.html
        ctx.set_ciphers("Default:@seclevel=1")

        return ctx
    
    xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_1': xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_1, 
        'xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_2': xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_2, 
        'xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_3': xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_3, 
        'xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_4': xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_4, 
        'xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_5': xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_5
    }
    
    def get_ssl_context(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_orig"), object.__getattribute__(self, "xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_ssl_context.__signature__ = _mutmut_signature(xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_orig)
    xǁTLSSecLevel1Adapterǁget_ssl_context__mutmut_orig.__name__ = 'xǁTLSSecLevel1Adapterǁget_ssl_context'


__all__ = ["HTTPSession", "SSLContextAdapter", "TLSNoDHAdapter", "TLSSecLevel1Adapter"]
